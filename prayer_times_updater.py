import requests

def fetch_prayer_times(city):
    url = "http://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country": "Bangladesh",
        "method": 2
    }
    res = requests.get(url, params=params)
    timings = res.json().get("data", {}).get("timings", {})
    return timings

def update_readme(city, start_marker, end_marker):
    timings = fetch_prayer_times(city)
    if not timings:
        table = "| Fajr | Dhuhr | Asr | Maghrib | Isha |\n|------|-------|-----|---------|------|\n| N/A | N/A | N/A | N/A | N/A |\n"
    else:
        table = (
            "| Fajr | Dhuhr | Asr | Maghrib | Isha |\n"
            "|------|-------|-----|---------|------|\n"
            f"| {timings.get('Fajr','N/A')} | {timings.get('Dhuhr','N/A')} | {timings.get('Asr','N/A')} | {timings.get('Maghrib','N/A')} | {timings.get('Isha','N/A')} |\n"
        )
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    before = content.split(f"<!-- {start_marker} -->")[0] + f"<!-- {start_marker} -->\n"
    after = content.split(f"<!-- {end_marker} -->")[-1]
    new_content = before + table + f"<!-- {end_marker} -->" + after
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

cities = [
    ("Dhaka", "PRAYER-TIME-DHAKA-START", "PRAYER-TIME-DHAKA-END"),
    ("Chittagong", "PRAYER-TIME-CHITTAGONG-START", "PRAYER-TIME-CHITTAGONG-END"),
    ("Sylhet", "PRAYER-TIME-SYLHET-START", "PRAYER-TIME-SYLHET-END"),
    ("Barisal", "PRAYER-TIME-BARISAL-START", "PRAYER-TIME-BARISAL-END"),
    ("Khulna", "PRAYER-TIME-KHULNA-START", "PRAYER-TIME-KHULNA-END"),
    ("Mymensingh", "PRAYER-TIME-MYMENSINGH-START", "PRAYER-TIME-MYMENSINGH-END"),
    ("Rajshahi", "PRAYER-TIME-RAJSHAHI-START", "PRAYER-TIME-RAJSHAHI-END"),
    ("Rangpur", "PRAYER-TIME-RANGPUR-START", "PRAYER-TIME-RANGPUR-END"),
]

for city, start, end in cities:
    update_readme(city, start, end)