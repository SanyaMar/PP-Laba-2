import os
import csv
import shutil
from typing import List


def replace_images(class_name: str, second_dataset: str) -> List[str]:
    '''
    Данная функция изменяет имена изображений, объединяя номер изображения и класс в формате class_number.jpg, 
    Parameters: class_name: str, second_dataset: str
    Returns: none
    '''
    relative_path = os.path.relpath(second_dataset)
    class_path = os.path.join(relative_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = [os.path.join(class_path, name) for name in image_names]
    new_image_names = [f"{class_name}_{name}" for name in image_names]
    new_image_rel_paths = [os.path.join(relative_path, name) for name in new_image_names]
    for old, new in zip(image_rel_paths, new_image_rel_paths):
        os.replace(old, new)

    os.chdir(second_dataset)

    if os.path.isdir(class_name):
        os.rmdir(class_name)
 
    os.chdir('..')


def getting_absolute_path(class_name: str, second_dataset: str) -> List[str]:
    '''
    Данная функция возвращает список list абсолютных путей изображений
    Parameters: class_name : str, second_dataset: str
    Returns: list
    ''' 
    absolute_path = os.path.abspath(second_dataset)
    image_names = os.listdir(absolute_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    image_absolute_path = [os.path.join(absolute_path, name) for name in image_names] 
    
    return image_absolute_path

def getting_relative_path(class_name: str, second_dataset: str) -> List[str]:
    '''
    Данная функция возвращает список list относительных путей изображений(относительно dataset)
    Parameters: class_name : str, second_dataset: str
    Returns: list
    '''
    relative_path = os.path.relpath(second_dataset)
    image_names = os.listdir(relative_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    image_relative_path = [os.path.join(relative_path, name) for name in image_names] 
    
    return image_relative_path


def main(first_dataset: str, second_dataset: str) -> str:
    first_class="cat"
    second_class="dog"

    if os.path.isdir(second_dataset):
        shutil.rmtree(second_dataset)

    path_dataset_1 = os.path.relpath(first_dataset)
    path_dataset_2 = os.path.relpath(second_dataset)
    shutil.copytree(path_dataset_1, path_dataset_2)

    replace_images(first_class, second_dataset)
    replace_images(second_class, second_dataset)

    dog_abs_paths = getting_absolute_path(first_class, second_dataset)
    dog_rel_paths = getting_relative_path(first_class, second_dataset)
    cat_abs_paths = getting_absolute_path(second_class, second_dataset)
    cat_rel_paths = getting_relative_path(second_class, second_dataset)

    with open('paths_2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, first_class])
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, second_class])



if __name__ == "__main__":
    main("dataset_1", "dataset_2")