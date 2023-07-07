import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# This is perfect for my use case

# Join multiple videos in defferent folders into one

FIXED_W = 1920
FIXED_h = 1080


OUTPUT_FNAME = 'GrumpyDog1_all_A.mp4'
ROOT = "../../Youtube/@GrumpyDog1/clips_apart/"
ROOT_NUM = 50
FOLDERS = []
FOLDERS.append("../../Youtube/@GrumpyDog1/clips_apart/1")

"""
OUTPUT_FNAME = '0201_dog_2023-06-27.mp4'
FOLDERS = []
FOLDERS.append("../../Youtube/@cutetv7/@dog/")
"""

"""
OUTPUT_FNAME = '0202_dog_2023-06-27.mp4'
FOLDERS = []
FOLDERS.append("../../Youtube/@cutestanimalsbaby/@dog/")
"""

def merge_videos_folder_group(root_folder):
  print(root_folder)
  for i in range(1, ROOT_NUM + 1):
    folder = [ROOT + str(i) + "/"]
    print(folder)
    merge_videos(folder, str(i))

def merge_videos(folders, outputname):
  videos = []
  file_list = []
  for f in folders:
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
  final_video.write_videofile(outputname, audio_codec='aac')

def show_video_size(fname):
  clip = VideoFileClip(fname).margin( right=420, left=420)
  value = clip.size
  clip.close()

  # printing size
  print("Clip Size ", end = " : ")
  print(value)

def get_files(path):
  file_list = os.listdir(path)
  for i, item in enumerate(file_list):
    file_list[i] = path + file_list[i]
  return file_list

#merge_videos(FOLDERS, OUTPUT_FNAME)
merge_videos_folder_group(ROOT)
