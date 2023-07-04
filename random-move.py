import os
import shutil
import random
import math

APART_NUMS = 10
FOLDER_INPUT = "../../Youtube/@GrumpyDog1/input/"
FOLDER_OUTPUT = "../../Youtube/@GrumpyDog1/output/"

def random_move():
  file_list = []
  file_list = file_list + get_files(FOLDER_INPUT)

  nums_per_folder = math.ceil(  len(file_list) / APART_NUMS )
  print("APART_NUMS " + str(APART_NUMS) + " is created!")

  for i in range(1, APART_NUMS+1):
    dir = FOLDER_OUTPUT + str(i)
    isExist = os.path.exists( dir )
    if not isExist:
      os.makedirs( dir )
      print("The new directory " + dir + " is created!")

  random.shuffle(file_list)
  count = 0
  folder_count = 1
  for item in file_list:
    dir = FOLDER_OUTPUT + str(folder_count)
    shutil.move(item, dir + "/" + os.path.basename(item) )
    print("Move " + os.path.basename(item) + " To " +  dir)

    count = count + 1
    if count >= nums_per_folder :
      count = 0
      folder_count = folder_count + 1

def get_files(path):
  file_list = os.listdir(path)
   
  for i, item in enumerate(file_list):
    file_list[i] = path + file_list[i]

  return file_list

random_move()