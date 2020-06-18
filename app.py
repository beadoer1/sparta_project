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

# POST 값을 이용해 검색어를 받아 검색결과를 return
@app.route('/api/food', methods=['POST'])
def foods_list():
    # 네이버 API JSON 형식으로 받기
    # keyword = request.form['title_give'] 형식을 이용 POST 요청값을 검색어에 반영
    location_receive = request.form['location_give']
    url = "https://openapi.naver.com/v1/search/local?query=" + location_receive + " 맛집" + "&display=30" + "&sort=comment" # 검색어 삽입 및 '맛집'과 조건들 삽입하여 검색
    client_id = ""
    client_secret = ""
    result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}) # 검색결과(requests 함수 사용)
    data = result.json() # 결과값을 json으로 나타내어 data에 저장
    bob = data['items'] # data 내 items 항목만 bob에 저장 
    return  jsonify({'result': 'success', 'foods_list': bob, 'msg':'떠나보자!!!!'}) 


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
