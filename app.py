from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta                   

# HTML을 주는 부분

@app.route('/')
def home():
    return render_template('index.html')

# 네이버 API Json 형식으로 받기
import os
import sys
import urllib.request
client_id = ""
client_secret = ""
encText = urllib.parse.quote("서울 맛집")
url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=30" + "sort=comment" # 30개까지, Comment 많은 순으로 출력
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)