import os

class Folder:

    def __init__(self, path):
        self.path = path
        self.size = self.get_size(self.path)

    def convert_to_proper_size(self, size_of_file):
        if size_of_file < 1024:
            return str(size_of_file) + " Byte"
        else:
            if size_of_file < 1024 * 1024:
                return str(round(size_of_file / 1024, 2)) + "kB"
            else:
                if size_of_file < 1024 * 1024 * 1024:
                    return str(round(size_of_file / (1024 * 1024), 2)) + "MB"
                else:
                    if size_of_file < 1024 * 1024 * 1024 * 1024:
                        return str(round(size_of_file / (1024 * 1024 * 1024), 2)) + "GB"

    def get_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
                    #print(total_size)
                    #print(f)

        return total_size

start_path = 'C:/Users'
list = []

for dirpath, dirnames, filenames in os.walk(start_path):
    list.append(Folder(dirpath))

list.sort(reverse=True, key=lambda x: x.size)

for element in list:
    print(element.path + " " + str(element.convert_to_proper_size(element.size)))


