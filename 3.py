import os, sys
with open(f'./logs/{model_name}/extract_f0_feature.log','w') as f:
    print("Starting...")
if f0method != "rmvpe_gpu":
    os.system("python infer/modules/train/extract/extract_f0_print.py ./logs/{model_name} 2 {f0method}")
else:
    os.system("python infer/modules/train/extract/extract_f0_rmvpe.py 1 0 0 ./logs/{model_name} True")
os.system("python infer/modules/train/extract_feature_print.py cuda:0 1 0 0 ./logs/{model_name} v2")
with open(f'./logs/{model_name}/extract_f0_feature.log','r') as f:
    if 'all-feature-done' in f.read():
        clear_output()
        display(Button(description="\u2714 Готово", button_style="success"))
    else:
        print("Ошибка предварительной обработки данных... Убедитесь, что данные были предварительно обработаны.")
