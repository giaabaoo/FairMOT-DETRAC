cd ../src
python track.py mot --val_detrac True \
--data_dir "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset" \
--load_model '../exp/mot/detrac_dla34_1/model_last.pth' --conf_thres 0.6 \
--min-box-area 100 \
--wo_heuristics True \
--save_videos True --save_images True \
# --video_name "MVI_39781"
cd ../experiments