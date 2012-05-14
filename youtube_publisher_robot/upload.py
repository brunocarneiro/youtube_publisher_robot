import gdata
import gdata.media
import gdata.youtube
import gdata.youtube.service
import gdata.geo

yt_service = gdata.youtube.service.YouTubeService()
yt_service.email = 'socialsharedvideos@gmail.com'
yt_service.password = 'youtube_social'
yt_service.source = 'youtube_publisher'
yt_service.developer_key='AI39si60VF9d_sgcxjKiY_GG8Z6Df94YXzZCaoscJXF9QwIwp4cN3R8-vQQfXwr6znAMXHT6FSh9og63XuaGpTpJK34MKL-3jw'
yt_service.client_id = 'youtube_publisher'
yt_service.ProgrammaticLogin()


def upload_video(title, description, keywords, category, file_location):
    """
    Upload a video file to YouTube.
    """
    # prepare a media group object to hold our video's meta-data
    my_media_group = gdata.media.Group(
      title=gdata.media.Title(text=title),
      description=gdata.media.Description(description_type='plain',
                                          text=description),
      keywords=gdata.media.Keywords(text=keywords),
      category=[gdata.media.Category(
          text=category,
          scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
          label='Autos')],
      player=None
    )
    
    # prepare a geo.where object to hold the geographical location
    # of where the video was recorded
    where = gdata.geo.Where()
    where.set_location((37.0,-122.0))
    
    # create the gdata.youtube.YouTubeVideoEntry to be uploaded
    video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group,
                                                  geo=where)
    
    new_entry = yt_service.InsertVideoEntry(video_entry, file_location)
    return new_entry

#EXAMPLE CALL    
#upload_video('My Test Movie', 'My description', 'cars, funny', 'Autos', '/home/bruno/Projetos/youtube/ujiK3jXxrNY.flv')