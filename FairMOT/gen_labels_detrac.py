import os.path as osp
import os
from turtle import left
import cv2
import json
import numpy as np
import pdb
from xml.etree import ElementTree
import xmltodict
from collections import OrderedDict
from tqdm import tqdm
from pathlib import Path

def mkdirs(d):
    Path(d).mkdir(parents=True, exist_ok=True)


def load_func(fpath):
    print('fpath', fpath)
    assert os.path.exists(fpath)
    with open(fpath, 'r') as fid:
        lines = fid.readlines()
    records =[json.loads(line.strip('\n')) for line in lines]
    return records


def gen_labels_detrac(data_root, ann_root, label_root, chosen_videos, chosen_annotations):
    mkdirs(label_root)

    count = 0
    for i, xml_file_path in enumerate(chosen_annotations):
        # print(i)

        my_dict = {}
        with open(os.path.join(ann_root, xml_file_path), 'r', encoding='utf-8') as file:
            my_xml = file.read()
            my_dict = xmltodict.parse(my_xml)

        frames_list = my_dict['sequence']['frame']

        for frame in tqdm(frames_list):
            
            chosen_frame = frame["@num"]
            target_list = frame['target_list'].values()

            image_zframeid = chosen_frame.zfill(5)
            image_name = "img" +  image_zframeid + ".jpg"
            video_name = xml_file_path.replace('_v3.xml', "")
            image_path = data_root + "/" + xml_file_path.replace('_v3.xml', "") + "/" + image_name
           
            if not osp.exists(image_path):
                continue

            image = cv2.imread(
                image_path,
                cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION
            )
            img_height, img_width = image.shape[0:2]
            
        
            for attr in target_list:
                if type(attr) is list:
                    for obj in attr:
                        tid_curr = int(obj['@id'])
                        left = float(obj['box']['@left'])
                        top = float(obj['box']['@top'])
                        width = float(obj['box']['@width'])
                        height = float(obj['box']['@height'])

                        left += width / 2
                        top += height / 2

                        # pdb.set_trace()

                        # label_fpath = os.path.join(data_root,image_path).replace('images', 'labels_with_ids').replace('.jpg', '.txt')
                        
                        Path(os.path.join(label_root, video_name)).mkdir(parents=True, exist_ok=True)
                        label_fpath = os.path.join(label_root, video_name, image_name).replace('.jpg', '.txt')
                        # pdb.set_trace()
                        label_str = '0 {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                            tid_curr, left / img_width, top / img_height, width / img_width, height / img_height)
                        with open(label_fpath, 'a') as f:
                            f.write(label_str)
                        # pdb.set_trace()
                        count += 1
                        # print(count)
                else:
                    left = float(attr['box']['@left'])
                    top = float(attr['box']['@top'])
                    width = float(attr['box']['@width'])
                    height = float(attr['box']['@height'])

                    left += width / 2
                    top += height / 2
                    Path(os.path.join(label_root, video_name)).mkdir(parents=True, exist_ok=True)

                    label_fpath = os.path.join(label_root, video_name, image_name).replace('.jpg', '.txt')
                    label_str = '0 {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                        tid_curr, left / img_width, top / img_height, width / img_width, height / img_height)
                    with open(label_fpath, 'a') as f:
                        f.write(label_str)
                    count += 1
                    # print(count)

if __name__ == '__main__':
    data_root = './DETRAC_dataset/Insight-MVT_Annotation_Train'
    ann_root = './DETRAC_dataset/DETRAC-Train-Annotations-XML-v3'
    label_root = './DETRAC_dataset/full_txt'

    folders = np.array(os.listdir(data_root))
    indices = np.random.permutation(len(folders)).astype(np.int32)[:22]
    chosen_videos = folders[indices]

    chosen_annotations = []
    for files in os.listdir(ann_root):
        video_name = files.replace("_v3.xml","")
        if video_name in chosen_videos:
            chosen_annotations.append(files)

    gen_labels_detrac(data_root, ann_root, label_root, chosen_videos, chosen_annotations)
