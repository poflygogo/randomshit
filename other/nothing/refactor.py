import os


curr_path = os.path.dirname(__file__)
for folder in os.listdir(curr_path):
    if os.path.isdir(os.path.join(curr_path, folder)):
        new_name = folder.replace('.', '')
        new_path = os.path.join(curr_path, new_name)
        os.rename(os.path.join(curr_path, folder), new_path)
