import sys

from pytube import YouTube

ids = ""
resolution = "720p"

if len(sys.argv) > 1:
  ids = sys.argv[1].replace(' ', '').replace(';', ',').split(',')

if len(sys.argv) > 2:
  resolution = sys.argv[2]

if not ids or len(ids) == 0 or ids[0] == "help":
  print("USAGE:\n./video-download VIDEO_ID [RESOLUTION (default 720p)] or")
  print("\n./video-download VIDEO_ID print (to see all streams) or")
  print("\n./video-download VIDEO_ID itag=NUMBER (to download specific stream)")
else:
  for id in ids:
    url = "https://www.youtube.com/watch?v=" + id

    if resolution == "print":
      print(YouTube(url).streams)
    elif resolution.startswith("itag="):
      itag = int(resolution.removeprefix("itag="))
      YouTube(url).streams.get_by_itag(itag).download()
    else:
      YouTube(url).streams.get_by_resolution(resolution).download()
