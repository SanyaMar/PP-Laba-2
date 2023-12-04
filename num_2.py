import os


def getting_absolute_path(class_name: str) -> list[str]:
    
    absolute_path = os.path.abspath('dataset_2')
    image_names = os.listdir(absolute_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    name=map(lambda name: os.path.join(absolute_path, name), image_names)
    image_absolute_path = list(name)
    
    return image_absolute_path

def getting_relative_path(class_name: str)-> list[str]:
    
    absolute_path = os.path.relpath('dataset_2')
    image_names = os.listdir(absolute_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    name=map(lambda name: os.path.join(absolute_path, name), image_names)
    image_absolute_path = list(name)
    
    return image_absolute_path
