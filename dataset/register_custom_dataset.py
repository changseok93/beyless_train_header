from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog
from os.path import join

def regist_beive_dataset(dataset_dir='/home/appuser/beive/dataset'):
    for d in ["train", "val", "test"]:
        json_file = join(dataset_dir, "json", d + ".json")
        image_root = join(dataset_dir, d)
        name = "beive_{}".format(d)
        # BoxMode.XYXY_ABS -> 0
        # BoxMode.XYWH_ABS -> 1
        register_coco_instances(name, {"bbox_mode":1}, json_file, image_root)

    beive_train_metadata = MetadataCatalog.get("beive_train")
    beive_val_metadata = MetadataCatalog.get("beive_val")
    beive_test_metadata = MetadataCatalog.get("beive_test")
    
    print(beive_train_metadata)
    print(beive_val_metadata)
    print(beive_test_metadata)

