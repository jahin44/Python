import os
dir= "C:\joy"
if not os.path.exists(dir):
    print("creating")
    os.makedirs(dir,exist_ok=True)
