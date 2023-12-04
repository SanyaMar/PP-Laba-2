import os
import csv
import shutil

def replace_images(class_name: str) -> list[str]:
    
    relative_path = os.path.relpath('dataset_2')
    class_path = os.path.join(relative_path, class_name)
    image_names = os.listdir(class_path)
    names=map(lambda name: os.path.join(class_path, name), image_names)
    image_rel_paths = list(names)
    new=map(lambda name: os.path.join(relative_path, f'{class_name}_{name}'), image_names)
    new_image_rel_paths = list(new)
    for old, new in zip(image_rel_paths, new_image_rel_paths):
        os.replace(old, new)

    os.chdir('dataset_2')

    if os.path.isdir(class_name):
        os.rmdir(class_name)

    os.chdir('..')

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


def main()-> None:
    first_class="cat"
    second_class="dog"

    if os.path.isdir('dataset_2'):
        shutil.rmtree('dataset_2')

    path_dataset_1 = os.path.relpath('dataset_1')
    path_dataset_2 = os.path.relpath('dataset_2')
    shutil.copytree(path_dataset_1, path_dataset_2)

    replace_images(first_class)
    replace_images(second_class)

    dog_abs_paths = getting_absolute_path(first_class)
    dog_rel_paths = getting_relative_path(first_class)
    cat_abs_paths = getting_absolute_path(second_class)
    cat_rel_paths = getting_relative_path(second_class)

    with open('paths_2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, first_class])
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, second_class])



if __name__ == "__main__":
    main()