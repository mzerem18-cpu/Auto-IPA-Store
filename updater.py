import requests
import json
import re

# لیستی ئەو ئەپانەی دەتەوێت ئۆتۆماتیک بن
apps_to_track = [
    {"name": "Gardenscapes", "url": "https://ipasoon.icu/details/Gardenscapes"},
    {"name": "GeckoOut", "url": "https://ipasoon.icu/details/GeckoOut"},
    {"name": "KineMaster", "url": "https://ipasoon.icu/details/KineMasterVideoEditor"},
    {"name": "Royal Match", "url": "https://ipasoon.icu/details/RoyalMatch"},
    {"name": "WhatsApp Business", "url": "https://ipasoon.icu/details/WhatsAppBusiness"}
]

def get_latest_link(page_url):
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"}
    try:
        response = requests.get(page_url, headers=headers, timeout=10)
        # گەڕان بەدوای لینکی .ipa لەناو کۆدی لاپەڕەکەدا
        match = re.search(r'https?://[^\s<>"]+\.ipa[^\s<>"]*', response.text)
        if match:
            return match.group(0).replace('\\', '')
    except:
        return None
    return None

def update_store():
    store_data = {
        "name": "Portal Store",
        "identifier": "com.portal.store",
        "apps": []
    }

    for app in apps_to_track:
        link = get_latest_link(app["url"])
        if link:
            app_info = {
                "name": app["name"],
                "bundleIdentifier": f"com.portal.{app['name'].replace(' ', '').lower()}",
                "version": "Latest",
                "downloadURL": link,
                "iconURL": "https://ipasoon.icu/favicon.ico",
                "size": 150000000
            }
            store_data["apps"].append(app_info)
            print(f"✅ {app['name']} نوێکرایەوە")

    with open("source.json", "w", encoding="utf-8") as f:
        json.dump(store_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_store()
