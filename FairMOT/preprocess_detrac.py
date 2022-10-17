from multiprocessing import process
import os
import numpy as np
import shutil
from pathlib import Path
import os.path as osp
from tqdm import tqdm
import pdb

if __name__ == '__main__':
    original_label_path = "./DETRAC_dataset/full_txt"
    original_image_path = "./DETRAC_dataset/Insight-MVT_Annotation_Train"

    image_path = "./DETRAC_dataset/fairmot_detrac_dataset/images"
    Path(os.path.join(image_path, "train")).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(image_path, "val")).mkdir(parents=True, exist_ok=True)

    label_path = "./DETRAC_dataset/fairmot_detrac_dataset/labels_with_ids"
    Path(os.path.join(label_path, "train")).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(label_path, "val")).mkdir(parents=True, exist_ok=True)
    
    folders = np.array(os.listdir(original_label_path))
    indices = np.random.permutation(len(folders)).astype(np.int32)
    chosen_videos = folders[indices]

    train = chosen_videos[:17]
    val = chosen_videos[17:]

    for video in tqdm(train):
        src_path = osp.join(original_image_path, video)
        dst_path = osp.join(image_path, "train", video)
        shutil.copytree(src_path, dst_path)

        src_path = osp.join(original_label_path, video)
        dst_path = osp.join(label_path, "train", video)
        shutil.copytree(src_path, dst_path)

    for video in tqdm(val):
        src_path = osp.join(original_image_path, video)
        dst_path = osp.join(image_path, "val", video)
        shutil.copytree(src_path, dst_path)

        src_path = osp.join(original_label_path, video)
        dst_path = osp.join(label_path, "val", video)
        shutil.copytree(src_path, dst_path)

    