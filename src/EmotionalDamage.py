import requests, base64, json, random, webbrowser

req = requests.get('https://api.github.com/repos/satanural/Failure/contents/src/urls.json')
if req.status_code == requests.codes.ok:
    enc = req.json()['content']
    content = str(base64.b64decode(enc), 'utf-8')
    links = json.loads(content)

    url = random.sample(links, 1)
    webbrowser.open(url[0])
else:
    print('Error: ' + str(req.status_code))
