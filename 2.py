import os, sys
os.system ("cd '/content/drive/MyDrive/project-main' && python download_files.py && pip install -r 'requirements-safe.txt'")
os.system ("pip install pyngrok")
os.system ("rm -r /content/sample_data")
os.system ("mkdir -p /content/dataset")
