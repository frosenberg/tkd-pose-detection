from pytube import YouTube
from pytube.exceptions import VideoUnavailable

# where to save 
SAVE_PATH = "./dataset/raw_videos" 

# maps readable names to youtube video ids
videos = { 
            'hyong1-diagram-mika' : 'https://www.youtube.com/watch?v=DIjtwNUYGmM',
            'hyong2-diagram-mika' : 'https://www.youtube.com/watch?v=kbHf_RR-QSk&ab_channel=TaekwondoMika',
            'hyong3-diagram-mika' : 'https://www.youtube.com/watch?v=-DN-MpKMaCM&ab_channel=TaekwondoMika',
            'hyong4-diagram-mika' : 'https://www.youtube.com/watch?v=f8yn23YCPng&ab_channel=TaekwondoMika', 
            'hyong5-diagram-mika' : 'https://www.youtube.com/watch?v=Q3r9Rw0MeIo&t=32s&ab_channel=TaekwondoMika', 
            'hyong6-diagram-mika' : 'https://www.youtube.com/watch?v=deU4BSpbUwE&ab_channel=TaekwondoMika', 
            'hyong7-diagram-mika' : 'https://www.youtube.com/watch?v=5JL1GtKSNq4&ab_channel=TaekwondoMika', 
            'hyong8-diagram-mika' : 'https://www.youtube.com/watch?v=nTF6E79iRvg&ab_channel=TaekwondoMika', 
            'hyong9-diagram-mika' : 'https://www.youtube.com/watch?v=Y6AEDqikTGo&ab_channel=TaekwondoMika', 
            'hyong10-diagram-mika' : 'https://www.youtube.com/watch?v=oUz1Oq4Tm0c&ab_channel=TaekwondoMika'
        } 
  
for name, url in videos.items():
    try:
        yt = YouTube(url)
    except VideoUnavailable as err: 
        print(f'Video {url} is unavailable, skipping.')
    else: 

        # filters out all the files with "mp4" extension 
        streams = yt.streams.filter(file_extension='mp4', res="720p")
        print(streams)
     
        try:
            fn = name + '.mp4'
            # downloading the video 
            streams.first().download(output_path=SAVE_PATH, filename=fn) 
        except: 
            print("Download error!")
        else: 
            print('Download completed!')


   
     

