import json

# ئەو لینکەی کە تۆ ناردووتە
direct_link = "https://ipasoon.icu/js/output/a1948f3724874993a3c72db119fab61e_ashte_AnalogueProCamera_14_CristianTeichnerAnalogue.signed.ipa"

def update_json():
    # زانیارییەکانی ستۆرەکە
    store_data = {
        "name": "Portal Store",
        "identifier": "com.portal.store",
        "apps": [
            {
                "name": "Analogue Pro Camera",
                "bundleIdentifier": "com.cristian.analogue",
                "version": "14",
                "versionDate": "2026-05-04",
                "downloadURL": direct_link,
                "iconURL": "https://ipasoon.icu/favicon.ico",
                "size": 134217728,
                "description": "ئەم ئەپڵیکەیشنە بە ئۆتۆماتیکی نوێکراوەتەوە"
            }
        ]
    }

    # نووسینی زانیارییەکان بۆ ناو فایلی source.json
    with open("source.json", "w", encoding="utf-8") as f:
        json.dump(store_data, f, indent=4, ensure_ascii=False)
    
    print("فایلی source.json بە سەرکەوتوویی نوێکرایەوە!")

if __name__ == "__main__":
    update_json()
