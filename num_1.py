import os
import csv
from typing import List


def getting_absolute_path(images_class: str, path_dataset: str) -> List[str]:
    '''
    Данная функция возвращает список list абсолютных путей изображений
    Parameters: class_name : str, second_dataset: str
    Returns: list
    ''' 
    absolute_path = os.path.abspath(path_dataset) 
    class_path = os.path.join(absolute_path, images_class) 
    image_names = os.listdir(class_path) 
    image_absolute_path = [os.path.join(class_path, name) for name in image_names] 
 
    return image_absolute_path


def getting_relative_path(images_class: str,  path_dataset: str) -> List[str]:
    '''
    Данная функция возвращает список list относительных путей изображений(относительно dataset)
    Parameters: class_name : str, path_dataset: str
    Returns: list
    '''
    relative_path = os.path.relpath(path_dataset)
    class_path = os.path.join(relative_path, images_class)
    image_names = os.listdir(class_path)
    image_relative_path = [os.path.join(class_path, name)for name in image_names]

    return image_relative_path


def main(path_dataset: str) -> str:
    first_class ="cat"
    second_class ="dog"

    cat_abs_paths = getting_absolute_path(first_class, path_dataset)
    cat_rel_paths = getting_relative_path(first_class, path_dataset)
    dog_abs_paths = getting_absolute_path(second_class, path_dataset)
    dog_rel_paths = getting_relative_path(second_class, path_dataset)

    with open('paths_1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, first_class])
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, second_class])


if __name__ == "__main__":
    main("dataset_1")