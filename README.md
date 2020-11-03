# beyless_train_header
detectron2 trainer header<br>

### 1. required packages
x86_64 based workstation<br>
nvidia GPU<br>
<br>
ubuntu linux operating system<br>
nvidia-driver >= 440<br>
<br>
docker<br>
nvidia-docker<br>
<br>
### 2. launch docker container
$ export WORKDIR="your work directory"<br>
$ cd $WORKDIR<br>
$ git clone https://github.com/changseok93/beyless_train_header<br>
$ cd beyless_train_header/docker<br>
$ bash ./bootstrap.sh<br>
<br>

### 3. prepare dataset
dataset must match this directory structure (coco style)<br>
<br>
dataset<br>
|<br>
├── json<br>
│   ├── train.json<br>
│   └── val.json<br>
├── train<br>
|   ├── images....<br>
|   └── images....<br>
└── val<br>
    ├── images....<br>
    └── images....<br>
    <br>
#### download beyless sample dataset
$ cd $WORKDIR/dataset<br>
$ bash ./download_beyless_dataset.sh<br>
<br>
### 4. train your model
$WORKDIR/run.py is detectron trainer<br>
<br>
example : <br>
$ cd $WORKDIR<br>
$ python3 run.py --config_file faster_rcnn_R_101_C4_3x.yaml --num_gpu 1 --batch_size 1<br>
<br>
--config_file : select your training model in $WORKDIR/config/...  you can change model parameter, structure there. this completly follow detectron2 rule<br>
--num_gpu : config number of gpu card for current training job<br>
--batch_size : number of batch<br>
<br>
for more options, please run <$ python3 run.py --help or -h> <br>

