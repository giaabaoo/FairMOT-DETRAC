# FairMOT-DETRAC
_Multi-object tracking on [DETRAC dataset](https://detrac-db.rit.albany.edu/)._

In this project, we employ the FairMOT model and finetuning the method with a different domain using DETRAC dataset to track vehicles in cities. Specifically, the main contributions are:

1. Problem formulation.
2. Preprocessing.
3. Analyze the dataset.
4. Evaluation and inference are conducted to benchmark the dataset with an adjustment of a heuristic measure during online inference.
5. Lastly, we also employ an enhanced data association technique in namely BYTE to improve the re-identification performance of our tracker.

## Demo

### Using default heuristic in FairMOT

![Default](FairMOT/results/default_heuristic.gif)

### Adjust the heuristic
![Adjusted](FairMOT/results/adjusted_heuristic.gif)

### Apply BYTE tracking
![BYTE](FairMOT/results/byte_track.gif)

## Usage
## Important notes!!
> **Get access** to the [UA-DETRAC dataset](https://detrac-db.rit.albany.edu/download) by downloading the training and testing images in XML format. 
>
> The weights of our tracking vehicles model can be found at [drive](https://drive.google.com/file/d/169Swt-nXM72NLHvWo1R9vP8bqwbTp2kX/view?usp=sharing).
>
> Moreover, as the model utilize DCNv2 in the upsampling module, please follow SE_DCNv2_latest README.md to install DCNv2 on your virtual environment. 


## Preprocess dataset

Before training on the DETRAC dataset, we will need to convert the annotations from XML to the desired input format of FairMOT.

Firstly, we convert the XML annotations into txt files by running:
```
python gen_labels_detrac.py
```

Next, we split the dataset into training and testing set within images and labels_with_ids folders:
```
python preprocess_detrac.py
```

Lastly, we generate the data following the format in **data/** folder
```
python gen_src_data_detrac.py
```

### Train classification

To train the task, run the following command:

```
cd experiments
sh detrac_dla34.sh
```

### Evaluation

To evaluate on default heuristic, run the following command:

```
cd experiments
sh eval_detrac_dl34_wo_heuristic.sh
```

To evaluate on adjusted heuristic, run the following command:

```
cd experiments
sh eval_detrac_dl34.sh
```

To evaluate using BYTE data association, run the following command:

```
cd experiments
sh bytetrack_detrac.sh
```

Eventually, the full evaluation of our testing process can be found at **results/** folder.

## Citation
```
@article{zhang2021fairmot,
  title={Fairmot: On the fairness of detection and re-identification in multiple object tracking},
  author={Zhang, Yifu and Wang, Chunyu and Wang, Xinggang and Zeng, Wenjun and Liu, Wenyu},
  journal={International Journal of Computer Vision},
  volume={129},
  pages={3069--3087},
  year={2021},
  publisher={Springer}
}
```

```
@article{zhang2022bytetrack,
  title={ByteTrack: Multi-Object Tracking by Associating Every Detection Box},
  author={Zhang, Yifu and Sun, Peize and Jiang, Yi and Yu, Dongdong and Weng, Fucheng and Yuan, Zehuan and Luo, Ping and Liu, Wenyu and Wang, Xinggang},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2022}
}
```
## Contributors
- Dinh-Huan Nguyen
- Gia-Bao Dinh Ho