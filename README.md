# beyless_train_header
detectron2 trainer header

### 1. required packages
x86_64 based workstation
nvidia GPU

ubuntu linux operating system
nvidia-driver >= 440

docker
nvidia-docker

### 2. launch docker container
$ export WORKDIR="your work directory"
$ cd $WORKDIR
$ git clone https://github.com/changseok93/beyless_train_header
$ cd beyless_train_header/docker
$ bash ./bootstrap.sh


### 3. prepare dataset
dataset must match this directory structure (coco style)

dataset
|
├── json
│   ├── train.json
│   └── val.json
├── train
|   ├── images....
|   └── images....
└── val
    ├── images....
    └── images....
    
#### download beyless sample dataset
$ cd $WORKDIR/dataset
$ bash ./download_beyless_dataset.sh

### 4. train your model
$WORKDIR/run.py is detectron trainer

example : 
$ cd $WORKDIR
$ python3 run.py --config_file faster_rcnn_R_101_C4_3x.yaml --num_gpu 1 --batch_size 1

--config_file : select your training model in $WORKDIR/config/...  you can change model parameter, structure there. this completly follow detectron2 rule
--num_gpu : config number of gpu card for current training job
--batch_size : number of batch

for more options, please run <$ python3 run.py --help or -h> 

