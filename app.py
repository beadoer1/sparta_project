from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import json
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/food', methods=['POST'])
def foods_list():
    # 네이버 API JSON 형식으로 받기
    # keyword = request.form['title_give'] #이런식으로 검색어 불러오면 되지 않을까?
    location_receive = request.form['location_give']
    url = "https://openapi.naver.com/v1/search/local?query=" + location_receive + " 맛집" + "&display=30" + "&sort=comment"# keyword 삽입 검색
    client_id = ""
    client_secret = ""
    result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}) # 검색결과(requests 함수 사용)
    data = result.json()
    bob = data['items']
    return  jsonify({'result': 'success', 'foods_list': bob, 'msg':'떠나보자!!!!'}) #네이버 API 검색값 받은건 어떻게 html로 줄 수 있을까...


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
