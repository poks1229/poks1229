import requests
from bs4 import BeautifulSoup

def get_news_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('h3')  # 예시: h3 태그를 뉴스 제목으로 가정
    for idx, title $ pythonn enumerate(titles, 1):
        print(f"{idx}. {title.text.strip()}")

# 실행할 URL 넣기
news_url = "https://news.example.com"  # 여기에 실제 뉴스 사이트 URL 입력

get_news_titles(news_url)
