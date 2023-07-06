from distutils import extension
from os import scandir, rename
import os
from os.path import splitext, exists, join
import shutil
import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

#

downloads_path = str(Path.home() / "Downloads")
source_dir = downloads_path

if not os.path.isdir(f"{Path.home()}/Downloads/sortedDownloads"):

    # if the demo_folder2 directory is
    # not present then create it.
    os.makedirs(f"{Path.home()}/Downloads/sortedDownloads")

dest_dir_images = (
    f"{Path.home()}/Downloads/sortedDownloads"  ## Need to implement Environment or .env
)


def make_unique(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + "(" + str(counter) + ")" + extension
        counter += 1

    return path


### Mover function
def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = make_unique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                ### This checks the extensions to redirect
                if (
                    name.endswith(".jpg")
                    or name.endswith(".jpeg")
                    or name.endswith(".png")
                    or name.endswith(".bmp")
                ):
                    dest = dest_dir_images
                    move(dest, entry, name)


#### Base Watchdog module for continuious checking for directory items change
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    path = source_dir  ### path should be changed to source directory
    event_handler = (
        MoverHandler()
    )  ### this is where the change will happen according to the class name
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
