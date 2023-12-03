import os
from typing import List

# Функция должна возвращять список абсолютных путей для изображений
def getting_absolute_path(images_class: str) : 
    absolute_path = os.path.abspath('dataset')
    class_path = os.path.join(absolute_path, images_class)
    image_names = os.listdir(class_path)
    name=map(lambda name: os.path.join(class_path, name), image_names)
    image_absolute_path = list(name)
    return image_absolute_path#список с путями на каждый элемент


def getting_relative_path(images_class:str):
    absolute_path = os.path.relpath('dataset')
    class_path = os.path.join(absolute_path, images_class)
    image_names = os.listdir(class_path)
    name=map(lambda name: os.path.join(class_path, name), image_names)
    image_absolute_path = list(name)
    return image_absolute_path#список с путями на каждый элемент

