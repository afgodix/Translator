#deep API test
import requests, re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

def translateEn(question):
    

    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
	    "q": question,
	    "source": "ru" if has_cyrillic(question) else 'en',
	    "target": "en" if has_cyrillic(question) else 'ru'
    }
    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "e11b8ee67bmshfd2e3f164efecc3p1cf5a8jsnd7bf6ed0cccd",
	    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()['data']['translations']['translatedText']

def translateEs(question):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
	    "q": question,
	    "source": "ru" if has_cyrillic(question) else 'es',
	    "target": "es" if has_cyrillic(question) else 'ru'
    }
    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "e11b8ee67bmshfd2e3f164efecc3p1cf5a8jsnd7bf6ed0cccd",
	    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()['data']['translations']['translatedText']
