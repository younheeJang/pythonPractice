import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:

        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

page = requests.get('https://blog.naver.com/edam0530')

print(type(page))

print(page.text)

print(page.status_code)

if page:
    print('success')
else:
    print('connot get page')