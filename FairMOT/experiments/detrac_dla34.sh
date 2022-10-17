cd ../src
python train.py mot --exp_id detrac_dla34_1 --gpus 0 --batch_size 4 --load_model '../exp/mot/detrac_dla34_1/model_last.pth' --resume --num_epochs 30 --lr_step '50' --data_cfg '../src/lib/cfg/detrac.json'
cd ../experiments