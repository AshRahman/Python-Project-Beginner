import os
import shutil
import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir ="/Users/intern3.bpl/Downloads"
dest_dir_images = "/Users/intern3.bpl/DownloadedImages" ## Need to implement Environment or .env

source_dir_home ="/Users/Rocka/Downloads"
dest_dir_images_home = "/Users/Rocka/DownloadedImages"

def move(dest, entry,name):
    file_exists = os.path.exists(dest+"/"+name)
    if file_exists:
        unique_name= makeUnique(name)
        os.rename(entry,unique_name)
    shutil.move(entry,dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self,event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name  = entry.name
                dest=source_dir
                
                if name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.jpg'):
                    dest = dest_dir_images
                    move(dest,entry,name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()