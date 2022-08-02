import os
import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

source_dir ="/Users/intern3.bpl/Downloads"
dest_dir_images = "/Users/intern3.bpl/DownloadedImages"

class MoverHandler(FileSystemEventHandler):
    def on_modified(self,event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                print(entry.name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()