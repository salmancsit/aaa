from django.http import HttpResponse
import json

from FeedEvaluate import main
#import FeedEvaluate 
#import feedparser
#from FeedEvaluate import EvaluateLocalFeed

def index(request):

     
        #alarm = EvaluateLocalFeed.objects.all()[0].EvaluateLocalFeed_setting
        #return HttpResponse (EvaluateLocalFeed('https://www.thenews.com.pk/rss/2/15'), content_type='text/plain'))
        #response_a = execfile('FeedEvaluate.py')
        #return response_a



    #return HttpResponse(id) 
     #return HttpResponse(execfile('C:\Users\MuhammadSalman\Desktop\mysite\polls\FeedEvaluate.py'))

     #a=execfile('C:\Users\MuhammadSalman\Desktop\mysite\polls\FeedEvaluate.py')
     news_json=json.dumps(main())
     return HttpResponse(news_json)
    #return HttpResponse(execfile('C:\Users\MuhammadSalman\Desktop\mysite\polls\FeedEvaluate.py'),content_type='text/plain')
    #return HttpResponse( main(),content_type='text/plain')
    
     #return HttpResponse(EvaluateLocalFeed('https://dailytimes.com.pk/feed/'))
