import requests
import json
import re

url = "https://ipasoon.icu/details/AnalogueProCamera"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
}

try:
    response = requests.get(url, headers=headers)
    html_content = response.text
    
    # گەڕان بەدوای لینکە تازەکەدا
    match = re.search(r'(https://ipasoon\.icu/js/output/[a-zA-Z0-9_]+\.signed\.ipa)', html_content)
    
    if match:
        fresh_link = match.group(1)
        
        # دروستکردنی فایلی JSON
        store_data = {
          "name": "My Auto Store",
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
        print("Done! Link updated.")
    else:
        print("Link not found on the page.")

except Exception as e:
    print(f"Error occurred: {e}")
