from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from apitweepytfg import tweepy_stream
import json
import urllib.request
from urllib.error import HTTPError

class TweepyApi(APIView):

    def get(request):
        twitterStream = tweepy_stream.TwitterStreamer()
        hash_tag_list = request.GET['hash_tag_list']
        maxTweets = request.GET['maxTweets']

        tweets = twitterStream.stream_tweets(hash_tag_list, maxTweets)

        data = {}
        count = 1

        for text in tweets:
            data[count] = text
            count += 1

        return JsonResponse(data, safe=False)


    def setenv(request):

        task = json.loads(request.body)
        task = task['task']


        res = requests.post('http://botalifoc.dsic.upv.es:5000/set_env', json={"task": task})
        if res.ok:
            return JsonResponse(res.json())
        else:
            return JsonResponse({"task":"failed"})

    def tag(request):

        tweets = json.loads(request.body)
        tweets = json.loads(tweets['tweets'])

        res = requests.post('http://botalifoc.dsic.upv.es:5000/tag', json=tweets)

        if res.ok:
            return JsonResponse(res.json())
        else:
            return JsonResponse({"1": "failed"})

    def post(request):

        return "succesful"