from guessit import guessit
import tmdbsimple as tmdb
import os
import hashlib
import time
import urllib2
import sys
arr1 = os.listdir("I:\Movies")
path1 = 'I:\Movies\\' + arr1[0]
print path1

def calc_hash(filepath):
    readsize = 64*1024 #64kb
    with open(filepath,'rb') as file:
        size = os.path.getsize(filepath)
        data = file.read(readsize)
        
        file.seek(-readsize,os.SEEK_END)
        data += file.read(readsize)
        return hashlib.md5(data).hexdigest()

def get_subtitles(path):
    i=0
    print 'Calculating hash of video file...'
    hash = calc_hash(path)
    replace = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov"]
    for c in replace:
        path = path.replace(c,"")
    if os.path.exists(path+".srt"):
        print "It seems you already have the subtitle"
    elif not os.path.exists(path+".srt"):
        print 'Searching for subtitles...'
        print '[',
        while(i<5):
            time.sleep(1)
            print '####',
            i = i+1
        print ']'
        print 'Subtitle Downloaded'
        headers = { 'User-Agent' : 'SubDB/1.0 (subtitle-downloader/1.0; Subterra_v0.1a)' }
        url = "http://api.thesubdb.com/?action=download&hash="+hash+"&language=en"
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req).read()

        with open(path+".srt","wb") as file1:
            file1.write(response)
        
get_subtitles(path1)

