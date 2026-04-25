import argparse
from core.scanner import scan_subdomains, scan_endpoints
from core.utils import info
from colorama import init

init()

def load_wordlist(path):
    with open(path, "r") as f:
        return [line.strip() for line in f]

def main():
    parser = argparse.ArgumentParser(description="Recon Assistant Tool")
    
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-w", "--wordlist", default="data/wordlist.txt", help="Wordlist path")

    args = parser.parse_args()

    domain = args.domain
    wordlist = load_wordlist(args.wordlist)

    subs = scan_subdomains(domain, wordlist)

    if subs:
        endpoints = scan_endpoints(subs)

        with open("output/results.txt", "w") as f:
            for item in endpoints:
                f.write(item + "\n")

        info("Results saved in output/results.txt")
    else:
        info("No subdomains found")

if __name__ == "__main__":
    main()
