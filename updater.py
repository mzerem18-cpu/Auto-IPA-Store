import json

# لێرە تەنها ئەو لینکە نوێیانە دابنێ کە خۆت دەرت هێناون
raw_links = [
    "https://ipasoon.icu/js/output/9c716edbf98446f78b333b19642c4649_ashte_Gardenscapes_960_complayrixgardenscapesm3ios.signed.ipa",
    "https://ipasoon.icu/js/output/9f75c47d294342f6b0d30ece44c64000_ashte_GeckoOut_1600_comdalakgamesslitherrush.signed.ipa",
    "https://ipasoon.icu/js/output/9d4c9a46c12047abb75aebd87fc69619_ashte_KineMasterVideoEditor_817_comkinemasterkios.signed.ipa",
    "https://ipasoon.icu/js/output/a0eb7c650bb04773bad13694d7c87963_ashte_RoyalMatch_35908_comdreamgamesroyalmatch.signed.ipa",
    "https://ipasoon.icu/js/output/9cabc105732b46869b99d2d385d649a4_ashte_WhatsAppBusiness_261674_netwhatsappWhatsAppSMB.signed.ipa"
]

def format_name(url):
    # دەرهێنانی ناوی ئەپەکە لە ناو لینکەکە بە شێوەیەکی جوان
    try:
        name = url.split('_ashte_')[1].split('_')[0]
        return name
    except:
        return "Unknown App"

def update_json():
    store_data = {
        "name": "Portal Store",
        "identifier": "com.portal.store",
        "apps": []
    }

    for link in raw_links:
        app_name = format_name(link)
        app_entry = {
            "name": app_name,
            "bundleIdentifier": f"com.portal.{app_name.lower()}",
            "version": "Latest",
            "downloadURL": link,
            "iconURL": "https://ipasoon.icu/favicon.ico",
            "size": 150000000
        }
        store_data["apps"].append(app_entry)

    with open("source.json", "w", encoding="utf-8") as f:
        json.dump(store_data, f, indent=4, ensure_ascii=False)
    
    print("بە سەرکەوتوویی source.json دروستکرا!")

if __name__ == "__main__":
    update_json()
