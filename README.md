# video-downloader
Project using the `pytube` lib to download youtube videos.

## Config
> You need to import `pytube` and `kivymd`
```bash
pip pytube kivymd
```

## How it works
> Giving a youtube video URL, the program will download this video in the chosen resolution (default 720p).

### command-line
```bash
python video-download.py VIDEO_URL [RESOLUTION]
```

### GUI
```bash
python youtube.py
```

### Tips
> You can generate a installer with `pyinstaller`
```bash
pyinstaller video-download.py
```
or
```bash
pyinstaller youtube.py
```
