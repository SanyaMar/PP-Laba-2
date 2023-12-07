import os

from typing import Optional

class Iterator:
    def __init__(self, class_name: str, path_dataset_1: str) -> None:
        self.counter = 0
        self.class_name = class_name
        self.data = os.listdir(os.path.join(path_dataset_1, self.class_name))
        self.limit = len(self.data)

    def __iter__(self):
        """
        Возвращает сам объект-итератор
        """
        return self
    
    def __next__(self) -> Optional[str]:
        """
        Возвращает следующий путь к файлу в списке данных, если он доступен, в противном случае возвращает None

        Returns: str or none
        """
        if self.counter < self.limit:
            next_path = os.path.join(self.class_name, self.data[self.counter])
            self.counter += 1
            return next_path
        else:
            return None


if __name__ == "__main__":

    dog = Iterator('dog', "dataset_1")
    cat = Iterator('cat', "dataset_1")

    print(next(dog))
    print(next(dog))
    print(next(dog))
    print(next(cat))
    print(next(cat))
    print(next(cat))
    