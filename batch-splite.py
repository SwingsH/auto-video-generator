import os
import subprocess

ROOT = "../../Youtube/@GrumpyDog1/"
FOLDERS = []
FOLDERS.append("../../Youtube/@cutetv7/@cat/")
FOLDERS.append("../../Youtube/@cutestanimalsbaby/@cat/")

def launch(path):
  file_list = []
  for f in FOLDERS:
    file_list = file_list + get_files(f)

  subprocess.run(["Z:"], shell=True, check=True)
  os.chdir(ROOT)
  #subprocess.run(["cd"], shell=True, check=True, cwd="Z:/_SwingsHuang/_WorkNormal/_CutAnimal/Youtube/@cutestanimalsbaby/")  # doesn't capture outpu
  #subprocess.run(["dir"], shell=True, check=True)

  print(file_list)

  #for item in file_list:
  #  subprocess.run(["scenedetect","-i" , item, "-o" ,"xxx" ,"-d" ,"1" ,"detect-content" ,"split-video"], shell=True, check=True)
  
def get_files(path):
  file_list = os.listdir(path)
   
  for i, item in enumerate(file_list):
    file_list[i] = path + file_list[i]

  return file_list

launch("clips")
