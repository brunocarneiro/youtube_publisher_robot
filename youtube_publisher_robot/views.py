from youtube_publisher_robot.upload import upload_video
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from youtube_publisher_robot.async import DownUpThread

@csrf_exempt
def creative (request):
    if request.POST:
        url = request.POST.get('url')
        title = request.POST.get('title')
        keywords = request.POST.get('keywords')
        description = request.POST.get('description')
        category = request.POST.get('category')
        
        DownUpThread(url, title, keywords, description, category).start()
        return HttpResponse(status=200)
        
    else:
        return HttpResponseForbidden()
