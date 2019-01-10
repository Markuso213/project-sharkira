#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:07:26 2019

@author: mumrah
"""
#%%
import os
import time
import argparse
import sys
import numpy as np
import re
from collections import defaultdict
####################################################################
########## Viable sources
####################################################################
strings= [
'https://www.youtube.com/watch?v=j1z4YncAjQM', #Random dude
'https://www.youtube.com/watch?v=3hn-D7kar5o', #Scary flying shark
'https://www.youtube.com/watch?v=7IPtYTO0Vb4', #baby shrk
'https://www.youtube.com/watch?v=vumJwdNXTks', #Baby shark educational
'https://www.youtube.com/watch?v=A3ytTKZf344', #Reggae shark
'https://www.youtube.com/watch?v=020g-0hhCAU', #Baby shark, smallezt
]

videos = defaultdict(set)
with open('files/youtubevideos.py') as inputfile:
   for line in inputfile:
      c = re.split(r', ', line)
      try:
         videos[c[1]].add(c[0])
      except:
         pass

####################################################################
########## Parsing
####################################################################
parser = argparse.ArgumentParser(description='This right here is SHAKIRA\'s party')
parser.add_argument('--silent', action='store_true', default=False, help='silences the countdown timer')
parser.add_argument('--timer', action='store', default=100, help='sets a timer in seconds', type=int)
parser.add_argument('--random', action='store_true', default=False, help='randomizes which video is played')
if '--random' in sys.argv:
   pass
else:
   parser.add_argument('song', action='store', default=1, help='choose which video to be played', type=int)
   
parser.add_argument('--chromecast', action='store_true', default=False, help='activate in order to play on Chromecast using mkchromcast application.')
parser.add_argument('--vlc', action='store_true', default=False, help='activate in order to play using VLC on current user.')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
####################################################################
                                       ########## End of parsing
####################################################################
try:
   print(args.silent, args.random)
except:
   print('failed', sys.argv)






random = np.random.randint(0,len(strings))
if args.chromecast:
   str1, str2 = 'mkchromecast -y ', ' --video'
if args.vlc:
   str1, str2 = 'vlc ', ''
def execute():
   def countdown():
      for i in range(args.timer):
         
         if not args.silent:
            print('A shark will appear in {} seconds'.format(args.timer-i))
         time.sleep(1)
      if args.random:
         os.system([str1 + os.system([str1 + strings[random]+ str2][0])+ str2][0])
      else:
         os.system([str1 + os.system([str1 + strings[args.song]+ str2][0])+ str2][0])
   countdown() 
execute()

#try:
#   execute()
#except KeyboardInterrupt:
#   print('\n Process interrupted by user. There will be no video :(')




##############3



nottested = [
'https://www.youtube.com/watch?v=0qOMyGVqjso',
'https://www.youtube.com/watch?v=yR4-MiNWAZw',
'https://www.youtube.com/watch?v=8KqcJYV6ZOU',
'https://www.youtube.com/watch?v=N9bJqwAyirE', #Sillen
]




strings_which_no_wrok= ['https://www.youtube.com/watch?v=CaePHaV_iUk', #Baby shark instructional
'https://www.youtube.com/watch?v=uCJDbU8OeAc',
'',
'',

]



