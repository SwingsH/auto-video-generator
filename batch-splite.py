import os
import subprocess

def launch(path):
  os.chdir("../../Youtube/")
  subprocess.run(["Z:"], shell=True, check=True) 
  subprocess.run(["dir"], shell=True, check=True)
  subprocess.run(["scenedetect","-i" ,"test_1.mp4", "-o" ,"xxx" ,"-d" ,"1" ,"detect-content","split-video"], shell=True, check=True)
  subprocess.run(["scenedetect","-i" ,"test_2.mp4", "-o" ,"xxx" ,"-d" ,"1" ,"detect-content" ,"split-video"], shell=True, check=True)

launch("clips")
