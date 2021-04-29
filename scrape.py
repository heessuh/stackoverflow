import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

questionlist = []

def getQuestions(tag):
    url = f'https://stackoverflow.com/questions/tagged/{tag}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    for item in questions:
        question = {
            'tag': tag,
            'title': item.find('a', {'class': 'question-hyperlink'}).text,
            'link': 'https://stackoverflow.com' + item.find('a', {'class': 'question-hyperlink'})['href'],
            'votes': int(item.find('span', {'class': 'vote-count-post'}).text),
            'date': item.find('span', {'class': 'relativetime'})['title'],
        }
        questionlist.append(question)
    return


#for x in range(1, 3):
# getQuestions(tag)

