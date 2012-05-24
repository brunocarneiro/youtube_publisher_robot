from threading import Thread
import os
from youtube_publisher_robot.upload import upload_video

class DownUpThread(Thread):
    
    def __init__( self, url, title=None, keywords=None, description=None, category=None ):
        self.url = url
        self.title = title
        self.keywords = keywords
        self.description = description
        self.category = category
        Thread.__init__(self)
    
    def run(self):
        result = os.system('python %s/youtube_publisher_robot/youtube_publisher_robot/youtube-dl.py %s' %(os.getcwd(),self.url) )
        upload_video(self.title, self.description, self.keywords, self.category, '%s/%s'%(os.getcwd(),self.url) )