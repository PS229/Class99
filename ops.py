import os 
import shutil

#path = "/Users/Shagrithaya/TestFolder2"
#source = "/Users/Shagrithaya/TestFolder/file.txt"
#destination = "/Users/Shagrithaya/TestFolder2/file.txt"
#dest = shutil.copy(source,destination)
#print(os.listdir(path))

path1 = "/Users/Shagrithaya/TestFolder2"
src = "/Users/Shagrithaya/TestFolder/file.txt"
destination1 = "/Users/Shagrithaya/TestFolder2/file2.txt"
dest = shutil.move(src,destination1)