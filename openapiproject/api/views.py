from django.shortcuts import render,HttpResponse
import os
import sys
import urllib.request
import json

# Create your views here.
client_id = "G7uRr0ZhzUrKSO1YNGcs"
client_secret = "HsE25A3WDF"


def search(request):
    return render(request, 'search.html')

def result(request):
    keyword = request.POST['keyword']
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    rq = urllib.request.Request(url)
    rq.add_header("X-Naver-Client-Id",client_id)
    rq.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(rq)
    rescode = response.getcode()
    if(rescode==200):
        data = response.read().decode('utf-8')
        result = json.loads(data)
        print('접근 성공')
        print(result['items'])
        return render(request, 'result.html',{'posts' : result['items']})
    else:

        return HttpResponse('API 접근불가')
