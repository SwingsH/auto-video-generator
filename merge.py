import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# This is perfect for my use case

# Join multiple videos in defferent folders into one

FIXED_W = 1920
FIXED_h = 1080
OUTPUT_FNAME = 'mgr.mp4'
FOLDERS = []
FOLDERS.append("../../Youtube/@xxx/@cat/")
FOLDERS.append("../../Youtube/@xxxx/@cat/")

def merge_videos():
  videos = []
  file_list = []
  for f in FOLDERS:
    file_list = file_list + get_files(f)

  for item in file_list:
    clip = VideoFileClip( item )
    w, h = clip.size

    # Scale
    if w < FIXED_W or h < FIXED_h:
      ratio = min( FIXED_W / w  , FIXED_h / h )
      if ratio != 1.0 :
        clip = clip.resize(ratio)
    
    #Margin
    margin_right  = 0
    margin_left   = 0
    w, h = clip.size
    margin_right  = int((FIXED_W - w) / 2)
    margin_left   = int((FIXED_W - w) / 2)
    clip = clip.margin( right = margin_right, left = margin_left)
    print("Clip Size ", end = " : ")
    print(clip.size)
    videos.append( clip )

  #videos.append(VideoFileClip('../../Youtube/@cutestanimalsbaby/01/01-Scene-001.mp4'))
  final_video = concatenate_videoclips(videos)
  final_video.write_videofile(OUTPUT_FNAME, audio_codec='aac')

def show_video_size(fname):
  clip = VideoFileClip(fname).margin( right=420, left=420)
  value = clip.size
  clip.close()

  # printing size
  print("Clip Size ", end = " : ")
  print(value)

def get_files(path):
  # Get the list of all files and directories
  # path = "../../Youtube/@cutestanimalsbaby/@cat/"
  file_list = os.listdir(path)
   
  for i, item in enumerate(file_list):
    file_list[i] = path + file_list[i]

  return file_list

merge_videos()
#get_files()
