import os
import csv
import shutil
import random


def main() -> None:
    if os.path.isdir('dataset_3'):
        shutil.rmtree('dataset_3')

    path_dataset_2 = os.path.relpath('dataset_2')
    path_dataset_3 = os.path.relpath('dataset_3')

    shutil.copytree(path_dataset_2, path_dataset_3)

    names = os.listdir(path_dataset_3)

    path = [os.path.join(path_dataset_3, name) for name in names] 
    rel_paths = list(path)

    random_numbers = random.sample(range(0, 10000), 2002)

    new_names = [f'{number}.jpg' for number in random_numbers]
    
    new_path = [os.path.join(path_dataset_3, name) for name in new_names] 
    new_rel_paths = list(new_path)

    for old_name, new_name in zip(rel_paths, new_rel_paths):
        os.replace(old_name, new_name)
    
    abs_path = [os.path.join(os.path.abspath('dataset3'), name) for name in new_names] 
    new_abs_paths = list(abs_path)

    with open('paths_3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path, old_rel_path in zip(new_abs_paths, new_rel_paths, rel_paths):
            if 'cat' in old_rel_path:
                class_name = 'cat'
            else:
                class_name = 'dog'
            writer.writerow([full_path, rel_path, class_name])
            


if __name__ == "__main__":
    main()