import os
import subprocess

ROOT = "../../Youtube/@GrumpyDog1/doing-src"
OUT = "../clips"
FOLDERS = []
FOLDERS.append("")

def launch():
  file_list = []
  for f in FOLDERS:
    file_list = file_list + get_files( ROOT + f)

  subprocess.run(["X:"], shell=True, check=True)
  os.chdir(ROOT)
  subprocess.run(["dir"], shell=True, check=True)

  #print(file_list)

  for item in file_list:
    subprocess.run(["scenedetect","-i" , item, "-o" ,OUT ,"-d" ,"1" ,"detect-content" ,"split-video"], shell=True, check=True)
  
def get_files(path):
  file_list = os.listdir(path)
   
  for i, item in enumerate(file_list):
    file_list[i] = file_list[i]

  return file_list

launch()
