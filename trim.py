import os
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips

FOLDER = "../../Youtube/@GrumpyDog1/"
FOLDER_TOO_SHORT = "../../Youtube/@GrumpyDog1/tooshort/"

def trim():
  videos = []
  file_list = []
  file_list = file_list + get_files(FOLDER)

  for item in file_list:
    clip = VideoFileClip( item )
    print(clip.duration )
    clip.close()
    if clip.duration < 4.5 :
      shutil.move(item, FOLDER_TOO_SHORT + os.path.basename(item) )
    videos.append( clip )

def get_files(path):
  file_list = os.listdir(path)
   
  for i, item in enumerate(file_list):
    file_list[i] = path + file_list[i]

  return file_list

trim()