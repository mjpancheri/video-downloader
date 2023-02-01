import sys

from pytube import YouTube

url = ""
resolution = "720p"

if len(sys.argv) > 1:
  url = "https://www.youtube.com/watch?v=" + sys.argv[1]

if len(sys.argv) > 2:
  resolution = sys.argv[2]

if not url:
  print("USAGE:\n./video-download VIDEO_ID [RESOLUTION (default 720p)]")
else:
  YouTube(url).streams.get_by_resolution(resolution).download()
