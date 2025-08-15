import requests
import pandas as pd
import config

number = config.number
account_id = config.account_id
past_company = config.past_company
api_key = config.api_key
pages = int(config.pages)

col_names = ['industry', 'name', 'profile_url', 'public_profile_url', 'location', 'headline']

all_results = []
cursor = ''

for i in range(pages):
    print(f"Fetching page {i + 1}...")
    if i == 0:
        url = f"https://api11.unipile.com:{number}/api/v1/linkedin/search?account_id={account_id}"
    else:
        url = f"https://api11.unipile.com:{number}/api/v1/linkedin/search?cursor={cursor}&account_id={account_id}"

    payload = {
        "api": "classic",
        "category": "people",
        "past_company": [past_company]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        break
    
    cursor = response.json()['cursor']
    data = response.json()
    items = data.get('items', [])
    if not items:
        break
    all_results.extend(items)

if all_results:
    df = pd.DataFrame(all_results)
    df = df[col_names]
    df.to_csv('api_search_results2.csv', index=False)
else:
    print("No results found.")
