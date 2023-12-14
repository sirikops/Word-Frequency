#Purpose: find the occurence of a certain word
#Run file: python project1.py
import os
import re

word = "August"
songfile = "song.txt"
statsfile = "stats.txt"
i = 0 #keeps track of word count

#defensive programming go brrr
if os.path.exists("stats.txt"):
  os.remove("stats.txt") #removes if exists
else:
  statsCreate = open(statsfile, "x")

# os.remove("stats.txt") #removes file
stats = open(statsfile, "w") #read and write
stats.write("")

file = open(songfile, "r") #read from file


lines = re.split("\n", file.read()) #each line is now an element in the list

for x in lines:
  find = re.search(word, x)
  if find != None:
    i = i + 1 #counts elements

stats.write("Occurence of " + word + ": " + str(i))

#stats = open("stats.txt", "r")
#print(stats.read()) #to check if this really worked

#because we are not heathens, close file
file.close()
stats.close()