from youtube_publisher_robot.upload import upload_video
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def creative (request):
    if request.POST:
        url = request.POST.get('url')
        #download file
        result = os.system('python /home/bruno/workspace/youtube_publisher_robot/youtube_publisher_robot/youtube-dl.py %s' %url )
        upload_video('My Test Movie', 'My description', 'cars, funny', 'Autos', '/home/bruno/Projetos/youtube/ujiK3jXxrNY.flv')
        return HttpResponse(status=200)
        
    else:
        return HttpResponseForbidden()
