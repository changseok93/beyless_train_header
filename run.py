import argparse
import glob
import time
import subprocess
import random
import torch

parser = argparse.ArgumentParser(description='beyless detectron2 train/inference command generator')
parser.add_argument('--datapath', type=str, default='/home/appuser/beyless_train_header/dataset', help='dataset path')
parser.add_argument('--num_gpu', type=int, default=2, help='number of gpu')
parser.add_argument('--config_root', type=str, default='/home/appuser/beyless_train_header/configs', help='path to config file directory')
parser.add_argument('--config_file', type=str, default='faster_rcnn_R_50_C4_1x.yaml', help='.yarm type config file')
parser.add_argument('--batch_size', type=int, default=4, help='number of batch')
parser.add_argument('--output_dir', type=str, default='/home/appuser/beyless_train_header/results', help='result directory')
parser.add_argument('--train_dataset', type=str, default='"(\'beive_train\',)"', help='dataset path')
parser.add_argument('--num_worker', type=int, default=16, help='dataset path')
parser.add_argument('--num_class', type=int, default=15, help='dataset path')
args = parser.parse_args()


def gpu_group_selector(num_gpu):
    # predefined variables
    total_gpu = int(torch.cuda.device_count())

    print('[please select gpu group]')
    num_menu = int(total_gpu / num_gpu)
    for i in range(num_menu):
        print('{}. gpu id :[{}]'.format(i, [j for j in range(i*num_gpu, (i+1)*num_gpu)]))
    print('{}. manual'.format(num_menu))

    selector = int(input("input :"))
    print('user gpu id : [{}]'.format([j for j in range(selector*num_gpu, (selector+1)*num_gpu)]))

    return [j for j in range(selector*num_gpu, (selector+1)*num_gpu)]

def validate_config_file(config_root, config_file):
    files = glob.glob('{}/**/*'.format(args.config_root), recursive=True)
    for file in files:
        if file.split('/')[-1] == args.config_file:
            return file

    print('can`t found config-file in config-root, please check file name or path again')

def create_random_port():
    rand = random.randrange(50000,65353)
    dist_url = 'tcp://127.0.0.1:{}'.format(rand)
    return dist_url

def generate_command(args):
    t0 = time.time()
    config_file = validate_config_file(args.config_root, args.config_file)
    group = ','.join(str(gpu_group_selector(args.num_gpu)).split(', '))
    output_dir = '{}/{}_{}/'.format(args.output_dir, args.config_file, t0)
    dist_url = create_random_port()


    command_prefix = "CUDA_VISIBLE_DEVICES={}".format(group[1:-1])
    command_postfix = '--datapath {} --num-gpus {} --config-file {} --dist-url {} SOLVER.IMS_PER_BATCH {} OUTPUT_DIR {} DATASETS.TRAIN "(\'custom_train\',)" DATALOADER.NUM_WORKERS {} INPUT.CROP.SIZE "[1.0, 1.0]" MODEL.ROI_HEADS.NUM_CLASSES {} CUDNN_BENCHMARK True'.format(
    args.datapath, args.num_gpu, config_file, dist_url, args.batch_size, output_dir, args.num_worker, args.num_class,
    )

    command = '{} python3 ./core/train_net.py {}'.format(command_prefix, command_postfix)
    return command
if __name__ == "__main__":
    command = generate_command(args)
    subprocess.run([command], shell=True, check=True)
