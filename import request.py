import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/n')
print(f"Статус код:{response.status_code}")
print(f"Текст отыета:{respons.text}")
data = response.json()
print(f"Заголовок текста:{data['title']}")
payload={'user': 'Ivan', 'age':25}
response = request.get('https://httpbin.org/get', params=payload)
print(response.url)
print(response.text)
url = 'https://.org/post'
payload_json={'title':'foo', 'body': 'bar', 'userID':n}
response=request.post(url,json=payload_json)
