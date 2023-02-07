import sys

from pytube import YouTube

ids = ""
resolution = "720p"

if len(sys.argv) > 1:
  ids = sys.argv[1].replace(' ', '').replace(';', ',').split(',')

if len(sys.argv) > 2:
  resolution = sys.argv[2]

if not ids or len(ids) == 0:
  print("USAGE:\n./video-download VIDEO_ID [RESOLUTION (default 720p)]")
else:
  for id in ids:
    url = "https://www.youtube.com/watch?v=" + id
    YouTube(url).streams.get_by_resolution(resolution).download()
