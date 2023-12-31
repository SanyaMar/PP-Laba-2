import os

from typing import Optional

def get_next_instance(class_name: str, first_dataset: str) -> Optional[str]:
    """
    Данная функция возвращает относительрный путь для объекта класса, переданного
    в функцию
    Parameters: class_name: str, first_dataset: str
    Returns: none
    """
    path = os.path.join(first_dataset, class_name)
    class_names = os.listdir(path)
    class_names.append(None)
    for i in range(len(class_names)):
        if class_names[i] is not None:
            yield os.path.join(path, class_names[i])
        elif class_names[i] is None:
            yield None   

print(*get_next_instance('cat', "dataset_1"))
