import subprocess, requests, argparse, warnings
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
warnings.filterwarnings("ignore")

VULN_FINGERPRINTS = {
    "azurewebsites.net": "404 Web Site not found",
    "s3.amazonaws.com": "NoSuchBucket",
    "herokudns.com": "No such app",
    "github.io": "There isn't a GitHub Pages site here",
    "surge.sh": "project not found"
}

COMMON = ["www", "mail", "dev", "test", "staging", "api", "app", "portal"]

def check_one(sub):
    try:
        result = subprocess.run(["nslookup", "-type=CNAME", sub], capture_output=True, text=True, timeout=5)
        for vuln_domain, fingerprint in VULN_FINGERPRINTS.items():
            if vuln_domain in result.stdout:
                try:
                    r = requests.get(f"https://{sub}", timeout=6, verify=False)
                    if fingerprint.lower() in r.text.lower():
                        return f"[!!!] POTENTIAL TAKEOVER: {sub} -> {vuln_domain}"
                    else:
                        return f"[*] {sub} -> {vuln_domain} -> Protected"
                except:
                    return f"[?] {sub} -> {vuln_domain} -> No HTTP response"
        return None
    except:
        return None

parser = argparse.ArgumentParser(description="Tabarak X V6 - Accurate Subdomain Takeover Scanner")
parser.add_argument("-d", "--domain", required=True)
parser.add_argument("-t", "--threads", type=int, default=15)
args = parser.parse_args()

domain = args.domain.strip()
print(f"\n=== Tabarak X V6 - Accurate Scan for {domain} ===\n")
subs = [f"{p}.{domain}" for p in COMMON] + [f"{p}-tst.{domain}" for p in COMMON]

with ThreadPoolExecutor(max_workers=args.threads) as ex:
    results = [r for r in ex.map(check_one, subs) if r]

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("results.txt", "a", encoding="utf-8") as f:
    f.write(f"\n\n===== V6 Scan {domain} at {now} - {len(subs)} subs =====\n")
    for r in results:
        f.write(r + "\n")
    if not results:
        f.write("No candidates found\n")

for r in results:
    print(r)

if any("VULN FOUND" in x or "POTENTIAL" in x for x in results):
    print(f"\n!!! JACKPOT! Saved to results.txt - Report this to {domain} bug bounty!")
else:
    print(f"\nDone! {domain} is SECURE. Results saved to results.txt")
print("Check file: results.txt")
