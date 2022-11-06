import os, webbrowser

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar
from pytube import YouTube

class Window(MDFloatLayout):
  def progress_download(self, stream, chunk, bites_remaining):
    msg = "Remaining: %.2f bytes" % (bites_remaining)
    Snackbar(text=msg).open()

  def complete_download(self, stream, file_path):
    Snackbar(text="Done!").open()
    if self.ids.open_browser.active:
      webbrowser.open_new(os.path.realpath(file_path))

  def download(self):
    if self.ids.url.text:
      Snackbar(text="Downloading...").open()
      YouTube(self.ids.url.text, self.progress_download,
        self.complete_download).streams.get_by_resolution("720p").download()
    else:
      Snackbar(text="Type a video url!").open()

class Download(MDApp):
  pass

if __name__=="__main__":
  Download().run()
