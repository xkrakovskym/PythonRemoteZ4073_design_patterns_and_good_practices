from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}, Size: {self.size} bytes")


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)


file1 = File("file1.txt", 100)
file2 = File("file2.txt", 2000)
file3 = File("file3.txt", 5000)


dir1 = Directory("dir1")
dir1.add(file1)

dir2 = Directory("dir2")
dir2.add(file3)

root_dir = Directory("root")
root_dir.add(dir1)
root_dir.add(dir2)
root_dir.add(file2)

root_dir.display()
