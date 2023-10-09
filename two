import os, sys
    input("Your dataset folder is empty.")
os.system("mkdir -p ./logs/{model_name}")
with open(f'./logs/{model_name}/preprocess.log','w') as f:
    print("Starting...")
os.system("python infer/modules/train/preprocess.py {dataset_folder} 40000 2 ./logs/{model_name} False 3.0 > /dev/null 2>&1")
with open(f'./logs/{model_name}/preprocess.log','r') as f:
