from playwright.sync_api import sync_playwright
import re
import argparse
import json

URL_REGEX = r'(https?://[^\s/]+)(/[^\s<>"]*)?'
FULL_URL_REGEX = r'https?://[^\s/]+/[^\s<>"]*'

def fetch_links(url, regex):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        links = re.findall(regex, content)
        browser.close()
        return links

def json_handler(urls):
    json_result = {}
    for url in urls:
        links = fetch_links(url, URL_REGEX)
        for link in links:
            domain, path = link
            if domain and path:
                if not json_result.get(domain):
                    json_result[domain] = [path]
                else:
                    json_result[domain].append(path)
    print(json.dumps(json_result, indent=4))

def stdout_handler(urls):
    for url in urls:
        links = fetch_links(url, FULL_URL_REGEX)
        for link in links:
            print(link)

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action='append', required=True, help="URL to scrape")
parser.add_argument("-o", "--output", choices=["stdout", "json"], required=True, help="Output format")
args = parser.parse_args()

if args.output == "json":
    json_handler(args.url)
else:
    stdout_handler(args.url)
