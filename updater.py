import requests
import json
import re

# لێرەدا هەوڵ دەدەین ڕاستەوخۆ دەستمان بگات بە لیستی ئەپەکان
url = "https://ipasoon.icu/details/AnalogueProCamera"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

def update_json(link):
    store_data = {
        "name": "Auto IPA Store",
        "identifier": "com.user.store",
        "apps": [{
            "name": "Analogue Pro Camera",
            "bundleIdentifier": "com.cristian.analogue",
            "version": "14",
            "downloadURL": link,
            "iconURL": "https://ipasoon.icu/favicon.ico",
            "size": 134220000
        }]
    }
    with open("source.json", "w") as f:
        json.dump(store_data, f, indent=4)
    print(f"Successfully updated with: {link}")

try:
    session = requests.Session()
    response = session.get(url, headers=headers, timeout=15)
    html_content = response.text
    
    # گەڕان بەدوای لینکی IPA لە ناو کۆدەکەدا
    match = re.search(r'https?://[^\s<>"]+signed\.ipa[^\s<>"]*', html_content)
    
    if match:
        update_json(match.group(0).replace('\\', ''))
    else:
        # ئەگەر نەدۆزرایەوە، لینکی گشتی بەکاردەهێنین بۆ تاقیکردنەوە
        print("Link not found, page might be protected.")
        # لێرەدا دەتوانیت لینکی ئەو فایلە دابنێیت کە پێشتر لە Storm Sniffer دۆزیبووتەوە
        # تەنها بۆ ئەوەی بزانیت سیستەمەکە ئیش دەکات
        # update_json("https://ipasoon.icu/js/output/YOUR_CAPTURED_LINK.ipa")

except Exception as e:
    print(f"Error: {e}")
