cd ../src
python byte_track.py mot \
--data_dir "/home/dhgbao/CV/Project/fairmot-for-vehicle-tracking/FairMOT/DETRAC_dataset" \
--val_detrac True \
--load_model '../exp/mot/detrac_dla34_1/model_last.pth' --match_thres 0.8 \
--save_videos True --save_images True \

# --load_model '/home/dhgbao/CV/Project/ByteTrack/YOLOX_outputs/yolox_x_detrac/best_ckpt.pth.tar' --match_thres 0.8 \
# --video_name "MVI_39781"
# --show_images True --save_videos True 
cd ../experiments