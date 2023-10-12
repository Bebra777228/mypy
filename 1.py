import os, sys
os.system ("wget https://huggingface.co/Rejekts/project/resolve/main/project-main.zip -O '/content/project-main.zip' && unzip -n 'project-main.zip' -d /content/drive/MyDrive")
os.system ("cd '/content/drive/MyDrive/project-main' && python download_files.py && pip install -r 'requirements-safe.txt'")
os.system ("pip install pyngrok")
os.system ("rm /content/project-main.zip")
os.system ("rm -r /content/sample_data")
os.system ("mkdir -p /content/dataset")
