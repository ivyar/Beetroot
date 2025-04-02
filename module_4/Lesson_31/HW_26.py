import requests
import json

# 1
def save_text(url):
    response = requests.get(url)
    with open('module_4/Lesson_31/robots.txt', 'a', encoding="utf-8") as file:
        file.write(response.text)

url = "https://en.wikipedia.org/wiki/Cat"
save_text(url)

url = "https://x.com/UKRINFORM/status/1654059751192371200"
save_text(url)

# 2
country = input("Введіть назву країни: ")
url = f'https://restcountries.com/v3.1/name/{country}'
response = requests.get(url)
data = response.json()[0]

info = {
    'name': data['name']['common'],
    'capital': data['capital'][0],
    'population': data['population'],
    'area': data['area'],
    'languages': ', '.join(data['languages'].values()),
    'currencies': ', '.join([c['name'] for c in data['currencies'].values()])
}

for key, value in info.items():
    print(f"{key}: {value}")

with open(f'module_4/Lesson_31/country_info.json', "w", encoding="utf-8") as file:
    json.dump(info, file, ensure_ascii=False, indent=4)

# 3
jokes = []

for _ in range(5):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json()['value']
    jokes.append(joke)
    print(joke)

with open(f'module_4/Lesson_31/jokes.txt', "w", encoding="utf-8") as file:
    for joke in jokes:
        file.write(joke + '\n')