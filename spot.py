import os

for root, dirs, files in os.walk("C:\\Users\\personal\\Desktop\\media\\MOVIES\\HORROR"):
    for file in files:
        if file.endswith(".mp4"):
            print(os.path.join(root, file))
            


