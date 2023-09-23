from google.colab import drive
drive.mount('/content/drive')
from IPython.display import clear_output
from ipywidgets import Button
import os
if not os.path.exists('/content/drive'):
    print("Your drive is not mounted. Creating Fake Drive.")
    os.makedirs('/content/drive/MyDrive')

import wget
url = "https://huggingface.co/Rejekts/project/resolve/main/project-main.zip"
file = wget.download(url,out="project-main.zip")
print(file)
