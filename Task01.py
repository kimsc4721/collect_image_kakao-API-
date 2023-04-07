import requests
import json

# Search image
url = "http://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK <a48ed63631fede1ce659896209d2e72f>"
}
data = {
    "query" : "펭수"
}

# requesting an image search
response = requests.post(url, headers=headers, data=data)
# if the request failed,
if response.status_code !=200:
    print("error! because", response.json())
else: # 성공했다면,
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        # Set a filename for the saved image
        count = count + 1