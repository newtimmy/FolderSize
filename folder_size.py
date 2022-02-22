import os

# def get_size(start_path):
#     total_size = 0
#     count = 0
#     foldersize = 0
#
#     all_paths = []
#     path_and_size = []
#     max_folder_size = 0
#
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         count = 0
#         count +=1
#         current_path = dirpath
#         #print(current_path)
#         sum_of_files = 0
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             #print(fp)
#
#             #print(dirpath)
#             #print(current_path)
#             #print(dirpath)
#             if current_path not in all_paths:
#                 #print("path: " + str(current_path) + " size: " + str(foldersize))
#                 path_and_size.append([foldersize, current_path])
#                 all_paths.append(current_path)
#                 foldersize = 0
#                 current_path= dirpath
#             current_path = dirpath
#             # skip if it is symbolic link
#             if not os.path.islink(fp):
#                 size_of_file = os.path.getsize(fp)
#                 total_size += size_of_file
#                 sum_of_files += size_of_file
#                 foldersize += sum_of_files
#                 if foldersize >= max_folder_size:
#                     max_folder_size = foldersize
#                     #biggest_folder = current_path
#         #print("path: " + str(dirpath) + "size: " + str(sum_of_files))
#         count +=1
#
#     #path_and_size.sort(reverse=False, key = myFunc)
#
#     #print(path_and_size)
#
#     return total_size, start_path

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

        #total_size_return = self.convert_to_proper_size(total_size)

        return total_size


import os





#print(get_size(start_path), 'bytes')

# def myFunc(e):
#     return e

start_path = 'C:/Users/Timm/PycharmProjects'

list = []

for dirpath, dirnames, filenames in os.walk(start_path):
    #print(get_size(dirpath))
    list.append(Folder(dirpath))

list.sort(reverse=True, key=lambda x: x.size)

for element in list:
    print(element.path + " " + str(element.convert_to_proper_size(element.size)))
#print(get_size("C:/Users/Timm/PycharmProjects/pythonProject/venv/Scripts"))


#print(get_size(start_path), 'bytes')

