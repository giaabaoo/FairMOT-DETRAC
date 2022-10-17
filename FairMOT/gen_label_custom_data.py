


from xml.dom import xmlbuilder


# parse file xml

def gen_labels_crowd(data_root, label_root, ann_root):
    mkdirs(label_root)
    anns_data = load_func(ann_root)

    tid_curr = 0
    for i, ann_data in enumerate(anns_data):
        print(i)
        image_name = '{}.jpg'.format(ann_data['ID'])
        img_path = os.path.join(data_root, image_name)
        anns = ann_data['gtboxes']
        img = cv2.imread(
            img_path,
            cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION
        )
        img_height, img_width = img.shape[0:2]
        for i in range(len(anns)):
            if 'extra' in anns[i] and 'ignore' in anns[i]['extra'] and anns[i]['extra']['ignore'] == 1:
                continue
            x, y, w, h = anns[i]['fbox']
            x += w / 2
            y += h / 2
            label_fpath = img_path.replace('images', 'labels_with_ids').replace('.png', '.txt').replace('.jpg', '.txt')
            label_str = '0 {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                tid_curr, x / img_width, y / img_height, w / img_width, h / img_height)
            with open(label_fpath, 'a') as f:
                f.write(label_str)
            tid_curr += 1