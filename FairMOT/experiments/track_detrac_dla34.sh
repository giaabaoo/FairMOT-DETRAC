cd ../src
python track.py mot --val_detrac True --data_dir "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset" --load_model '../exp/mot/detrac_dla34_1/model_last.pth' --conf_thres 0.6
cd ../experiments