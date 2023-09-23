from google.colab import drive
drive.mount('/content/drive')
from IPython.display import clear_output
from ipywidgets import Button
import os
if not os.path.exists('/content/drive'):
    print("Your drive is not mounted. Creating Fake Drive.")
    os.makedirs('/content/drive/MyDrive')
link = 'https://huggingface.co/Rejekts/project/resolve/main/project-main.zip'
wget {link} -O '/content/project-main.zip' && unzip -n 'project-main.zip' -d /content/drive/MyDrive
cd '/content/drive/MyDrive/project-main' && python download_files.py && pip install -r 'requirements-safe.txt'
rm /content/project-main.zip
rm -r /content/sample_data
mkdir -p /content/dataset
clear_output()
Button(description="\u2714 Готово", button_style="success")
