import os
from pathlib import Path
import os.path as osp
import pdb
from socket import gaierror
import cv2
from numpy import half
from tqdm import tqdm

def read_image(image_path):
    image = cv2.imread(image_path)

    height, width = image.shape[0:2]

    return height, width


if __name__ == '__main__':
    labels_path = "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset/fairmot_detrac_dataset/labels_with_ids"
    images_path = "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset/fairmot_detrac_dataset/images"

    gt_path = "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset/fairmot_detrac_dataset/gt_txt"

    Path(gt_path).mkdir(parents=True, exist_ok=True)
    Path(osp.join(gt_path, "train")).mkdir(parents=True, exist_ok=True)
    Path(osp.join(gt_path, "val")).mkdir(parents=True, exist_ok=True)

    # for video_folder in tqdm(sorted(os.listdir(osp.join(labels_path, "train")))):
    #     Path(osp.join(gt_path, "train", video_folder)).mkdir(parents=True, exist_ok=True)
        
    #     with open(osp.join(gt_path, "train", video_folder, "gt.txt"), "w") as gt_txt:
    #         for files in sorted(os.listdir(osp.join(labels_path, "train", video_folder))):
    #             frame = int(files.replace(".txt", "").replace("img", ""))

    #             with open(osp.join(labels_path, "train", video_folder, files), "r") as txt:
    #                 lines = txt.readlines() 
    #                 height, width = read_image(osp.join(images_path, "train", video_folder, files.replace(".txt", ".jpg")))
    #                 for line in lines:
    #                     _, idx, x1, y1, w, h = line.split()
    #                     x1 = float(x1)*width - float(w)*width/2
    #                     y1 = float(y1)*height -float(h)*height/2
    #                     w = float(w)*width 
    #                     h = float(h)*height 

    #                     content = "{},{},{},{},{},{},1,-1,-1,-1\n".format(frame, idx, x1, y1, w, h)
    #                     gt_txt.write(content)

    for video_folder in tqdm(sorted(os.listdir(osp.join(labels_path, "val")))):
        Path(osp.join(gt_path, "val", video_folder)).mkdir(parents=True, exist_ok=True)
        
        with open(osp.join(gt_path, "val", video_folder, "gt.txt"), "w") as gt_txt:
            for files in sorted(os.listdir(osp.join(labels_path, "val", video_folder))):
                frame = int(files.replace(".txt", "").replace("img", ""))

                with open(osp.join(labels_path, "val", video_folder, files), "r") as txt:
                    lines = txt.readlines() 
                    height, width = read_image(osp.join(images_path, "val", video_folder, files.replace(".txt", ".jpg")))
                    for line in lines:
                        _, idx, x1, y1, w, h = line.split()
                        x1 = float(x1)*width - float(w)*width/2
                        y1 = float(y1)*height -float(h)*height/2
                        w = float(w)*width 
                        h = float(h)*height 

                        content = "{},{},{},{},{},{},1,-1,-1,-1\n".format(frame, idx, x1, y1, w, h)
                        gt_txt.write(content)
