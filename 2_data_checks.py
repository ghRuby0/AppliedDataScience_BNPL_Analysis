# Extracts files from .zip, checks all the files are there.

import zipfile
import os
from pathlib import Path

# Extracts all the .zip files and deletes them.
for file in Path("../i_landing_layer").iterdir():
    if ".zip" in file.name:
        with zipfile.ZipFile(file, "r") as archive:
            archive.extractall("../i_landing_layer")
        os.remove(file)

# Checks all the data exist. Deletes .SUCCESS files
for file in Path("../i_landing_layer/tables").iterdir():
    if file.is_dir():
        print("(Directory)", file.name)
        for subfile in file.iterdir():
            print(" > ", subfile.name)
            if "SUCCESS" in subfile.name:
                os.remove(subfile)
    else:
        print("(File)", file.name)

# Renames the folders for clarity
Path("../i_landing_layer/tables/transactions_20210228_20210827_snapshot").rename("../i_landing_layer/tables/trans_period_1")
Path("../i_landing_layer/tables/transactions_20210828_20220227_snapshot").rename("../i_landing_layer/tables/trans_period_2")
Path("../i_landing_layer/tables/transactions_20220228_20220828_snapshot").rename("../i_landing_layer/tables/trans_period_3")