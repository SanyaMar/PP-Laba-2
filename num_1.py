import os
import csv

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

def main():
    first_class="dog"
    second_class="cat"

    dog_abs_paths = getting_absolute_path(first_class)
    dog_rel_paths = getting_relative_path(first_class)
    cat_abs_paths = getting_absolute_path(second_class)
    cat_rel_paths = getting_relative_path(second_class)

    with open('paths.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([full_path, rel_path, first_class])
        for full_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([full_path, rel_path, second_class])


if __name__ == "__main__":
    main()