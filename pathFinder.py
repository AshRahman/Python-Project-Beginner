from pathlib import Path
import os

downloads_path = str(Path.home() / "Downloads")

if not os.path.isdir(f"{Path.home()}/Downloads/sortedDownloads"):

    # if the demo_folder2 directory is
    # not present then create it.
    os.makedirs(f"{Path.home()}/Downloads/sortedDownloads")
