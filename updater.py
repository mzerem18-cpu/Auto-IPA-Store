import requests
import json
import re

# لینکی لاپەڕەی سەرەکی یارییەکە
url = "https://ipasoon.icu/details/AnalogueProCamera"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
}

try:
    response = requests.get(url, headers=headers)
    html_content = response.text
    
    # ئەم کۆدە بەدوای هەر لینکێکدا دەگەڕێت کە بە ipa کۆتایی بێت
    links = re.findall(r'https?://[^\s<>"]+\.ipa[^\s<>"]*', html_content)
    
    if links:
        # یەکەم لینک کە دەیدۆزێتەوە هەڵیدەبژێرێت
        fresh_link = links[0].replace('\\', '')
        print(f"Link Found: {fresh_link}")
        
        store_data = {
          "name": "Auto IPA Store",
          "identifier": "com.user.store",
          "apps": [
            {
              "name": "Analogue Pro Camera",
              "bundleIdentifier": "com.cristian.analogue",
              "version": "14",
              "downloadURL": fresh_link,
              "iconURL": "https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/ios/ios.png",
              "size": 134220000
            }
          ]
        }
        
        with open("source.json", "w") as f:
            json.dump(store_data, f, indent=4)
    else:
        print("No IPA link found on page.")

except Exception as e:
    print(f"Error: {e}")
