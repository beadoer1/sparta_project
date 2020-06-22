from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import json
with open('config.json', 'r') as f:
    config = json.load(f)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# Naver API Client_id, secret 불러오기
client_id0 = config['DEFAULT']['client_id0']
client_id1 = config['DEFAULT']['client_id1']
client_id2 = config['DEFAULT']['client_id2']
client_secret0 = config['DEFAULT']['client_secret0']
client_secret1 = config['DEFAULT']['client_secret1']
client_secret2 = config['DEFAULT']['client_secret2']

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

    # POST 값을 이용해 검색어를 받아 검색결과를 return


@app.route('/api/play', methods=['POST'])
def plays_list():
    # 네이버 API JSON 형식으로 받기
    # keyword = request.form['title_give'] 형식을 이용 POST 요청값을 검색어에 반영
    location_receive = request.form['location_give']
    url = "https://openapi.naver.com/v1/search/local?query=" + location_receive + \
        "명소" + "&display=3" + "&sort=comment"  # 검색어 삽입 및 '맛집'과 조건들 삽입하여 검색
    client_id = client_id0
    client_secret = client_secret0
    result0 = requests.get(urlparse(url).geturl(), headers={
                           "X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})  # 검색결과(requests 함수 사용)
    data0 = result0.json()  # 결과값을 json으로 나타내어 data에 저장
    nolja = data0['items']  # data 내 items 항목만 bob에 저장
    return jsonify({'result': 'success', 'plays_list': nolja})

# POST 값을 이용해 검색어를 받아 검색결과를 return


@app.route('/api/food', methods=['POST'])
def foods_list():
    # 네이버 API JSON 형식으로 받기
    # keyword = request.form['title_give'] 형식을 이용 POST 요청값을 검색어에 반영
    location_receive = request.form['location_give']
    url = "https://openapi.naver.com/v1/search/local?query=" + location_receive + \
        " 맛집" + "&display=3" + "&sort=comment"  # 검색어 삽입 및 '맛집'과 조건들 삽입하여 검색
    client_id = client_id1
    client_secret = client_secret1
    result1 = requests.get(urlparse(url).geturl(), headers={
                           "X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})  # 검색결과(requests 함수 사용)
    data1 = result1.json()  # 결과값을 json으로 나타내어 data에 저장
    bob = data1['items']  # data 내 items 항목만 bob에 저장
    return jsonify({'result': 'success', 'foods_list': bob, 'msg': '떠나보자!!!!'})

# POST 값을 이용해 검색어를 받아 검색결과를 return


@app.route('/api/home', methods=['POST'])
def homes_list():
    # 네이버 API JSON 형식으로 받기
    # keyword = request.form['title_give'] 형식을 이용 POST 요청값을 검색어에 반영
    location_receive = request.form['location_give']
    url = "https://openapi.naver.com/v1/search/local?query=" + location_receive + \
        "숙소" + "&display=15" + "&sort=comment"  # 검색어 삽입 및 '맛집'과 조건들 삽입하여 검색
    client_id = client_id2
    client_secret = client_secret2
    result2 = requests.get(urlparse(url).geturl(), headers={
                           "X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})  # 검색결과(requests 함수 사용)
    data2 = result2.json()  # 결과값을 json으로 나타내어 data에 저장
  
    for i in data2['items']:
        # meta tag를 스크래핑하기
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(i['link'], headers = headers, verify=True)
        soup = BeautifulSoup(data.text, 'html.parser')
        og_image = soup.select_one('meta[property="og:image"]')
        i['image'] = og_image
        print(i)
        
    jib = data2['items']    
    return jsonify({'result': 'success', 'homes_list': jib})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
