import requests
import threading
from core.utils import info, good

alive = []

def check_sub(domain, sub):
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code < 500:
            good(f"{url} [{r.status_code}]")
            alive.append(url)
    except:
        pass

def scan_subdomains(domain, wordlist):
    threads = []
    info("Scanning subdomains...")

    for sub in wordlist:
        t = threading.Thread(target=check_sub, args=(domain, sub))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return alive


def scan_endpoints(urls):
    endpoints = ["/api", "/login", "/admin", "/graphql"]
    found = []

    info("Scanning endpoints...")

    for base in urls:
        for ep in endpoints:
            full = base + ep
            try:
                r = requests.get(full, timeout=3)
                if r.status_code < 500:
                    good(f"{full} [{r.status_code}]")
                    found.append(full)
            except:
                pass

    return found
