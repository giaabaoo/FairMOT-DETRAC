import os
from tqdm import tqdm
import shutil
import pdb
 
if __name__ == '__main__':
    srcdata_path = "./src/data"

    train_path = "./DETRAC_dataset/fairmot_detrac_dataset/labels_with_ids/train"
    val_path = "./DETRAC_dataset/fairmot_detrac_dataset/labels_with_ids/val"

    with open(os.path.join(srcdata_path,"detrac.train"), "w") as f:
        for folder in tqdm(sorted(os.listdir(train_path))):
            custom_train_path = "fairmot_detrac_dataset/images/train"
            for files in sorted(os.listdir(os.path.join(train_path,folder))):
                file_content = os.path.join(custom_train_path,folder, files.replace(".txt",".jpg")) + '\n'
                f.write(file_content)
           

    with open(os.path.join(srcdata_path,"detrac.val"), "w") as f:
        for folder in tqdm(sorted(os.listdir(val_path))):
            custom_val_path = "fairmot_detrac_dataset/images/val"
            for files in sorted(os.listdir(os.path.join(val_path,folder))):
                file_content = os.path.join(custom_val_path,folder, files.replace(".txt",".jpg")) + '\n'
                f.write(file_content)
           