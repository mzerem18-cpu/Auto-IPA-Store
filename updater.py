import requests
import json
import re

# لینکی ئەو لاپەڕەیەی کە یارییەکەی تێدایە
url = "https://ipasoon.icu/details/AnalogueProCamera"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
}

try:
    # ناردنی داواکاری بۆ ماڵپەڕەکە
    response = requests.get(url, headers=headers, timeout=15)
    html_content = response.text
    
    # گەڕان بەدوای لینکی .ipa لەناو کۆدی ماڵپەڕەکەدا
    match = re.search(r'https?://[^\s<>"]+\.ipa[^\s<>"]*', html_content)
    
    if match:
        # پاککردنەوەی لینکەکە لە هەر هێمایەکی زیادە
        fresh_link = match.group(0).replace('\\', '')
        
        # دروستکردنی فایلی source.json بە زانیارییە نوێیەکان
        store_data = {
            "name": "Auto Store",
            "identifier": "com.user.store",
            "apps": [{
                "name": "Analogue Pro Camera",
                "bundleIdentifier": "com.cristian.analogue",
                "version": "14",
                "downloadURL": fresh_link,
                "iconURL": "https://ipasoon.icu/favicon.ico",
                "size": 134220000
            }]
        }
        
        # پاشەکەوتکردنی ئەنجامەکە
        with open("source.json", "w") as f:
            json.dump(store_data, f, indent=4)
        
        print(f"بە سەرکەوتوویی لینکەکە دۆزرایەوە: {fresh_link}")
    else:
        print("ببورە، نەمانتوانی لینکەکە لەناو ماڵپەڕەکە بدۆزینەوە. ڕەنگە ماڵپەڕەکە گۆڕابێت.")
        
except Exception as e:
    print(f"هەڵەیەک ڕوویدا: {e}")
