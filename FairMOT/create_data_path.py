import os 
import numpy as np
from tqdm import tqdm
train_dir = '../detrac_dataset/images/train'
val_dir = '../detrac_dataset/images/val'

with open('./src/data/detrac.train','w') as f:
    for filename in tqdm(os.listdir(train_dir)):
        f.write(os.path.join(train_dir[3:],filename)+'\n')

with open('./src/data/detrac.val','w') as f:
    for filename in tqdm(os.listdir(val_dir)):
        f.write(os.path.join(val_dir[3:],filename)+'\n') 
        
    
