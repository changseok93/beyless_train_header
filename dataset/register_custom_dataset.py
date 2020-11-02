from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog
from os.path import join

def regist_custom_dataset(dataset_dir='/home/appuser/beyless_train_header/dataset'):
    for d in ["train", "val", "test"]:
        json_file = join(dataset_dir, "json", d + ".json")
        image_root = join(dataset_dir, d)
        name = "custom_{}".format(d)
        # BoxMode.XYXY_ABS -> 0
        # BoxMode.XYWH_ABS -> 1
        register_coco_instances(name, {"bbox_mode":1}, json_file, image_root)

    custom_train_metadata = MetadataCatalog.get("custom_train")
    custom_val_metadata = MetadataCatalog.get("custom_val")
    custom_test_metadata = MetadataCatalog.get("custom_test")
    

