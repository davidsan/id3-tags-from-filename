#!/usr/bin/env python

# Add track and artist ID3 tag to one or multiple files passed in arguments

from mutagen.mp3 import EasyMP3 as MP3
import sys, re

for arg in sys.argv[1:]:
    try:
        filename = arg
        audio = MP3(filename)
        
        match = re.search( r'^(.*?)\s*-\s*(.*?)\s*.mp3$', filename, re.M)

        if not match:
            print 'incorrect format for', arg
            continue

        artist = match.group(1)
        title = match.group(2)
        
        print 'Processing :', artist, '-', title
        
        # Sets the title and the artist of the song
        audio['title'] = title
        audio['titlesort'] = title
        audio['artist'] = artist
        audio['artistsort'] = artist
        audio['albumartistsort'] = artist
        
        # Save the new ID3 tags
        audio.save()
    except IOError as e:
        print 'cannot open', arg



