import os
from datetime import datetime

directory = "dirs"

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

        ymd = datetime.now().strftime("%Y-%m-%d")

        new_filename = f"{filename[:-4]}-{ymd}.txt"

        new_filepath = os.path.join(directory, new_filename)

        os.rename(filepath, new_filepath)

        print(f"file {filename} has been renamed to {new_filename}")

   
