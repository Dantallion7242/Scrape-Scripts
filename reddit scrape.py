import time
import httpx
import pandas as pd

base_url = 'https://www.reddit.com'
endpoint = '/r/sportsbetting'
category = '/hot'

url = base_url + endpoint + category + ".json"
after_post_id = None

dataset = []
for _ in range(5):  # Specify the number of iterations
    params = {
        'limit': 100,
        't': 'year',  # time
        'after': after_post_id
    }
    response = httpx.get(url, params=params)
    print(f'fetching "{response.url}"...')
    if response.status_code != 200:
        raise Exception('Failed to fetch')

    json_data = response.json()

    dataset.extend([rec['data'] for rec in json_data['data']['children']])
    after_post_id = json_data['data']['after']
    time.sleep(0.5)
name = endpoint.replace('/r/', '')
df = pd.DataFrame(dataset)
df.to_csv(name+'reddit_python.csv', index=False)