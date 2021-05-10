import os
from natsort import natsorted
import subprocess


def main():
    skip = False
    path = "/Users/dani/PycharmProjects/pythonProject/Editor_results/"
    count = 1

    old_name_1 = "/abed-2pop Pop. 1: Strategy distributions (complete history).csv"
    old_name_2 = "/abed-2pop Pop. 2: Strategy distributions (complete history).csv"
    new_name_1 = '/1pop'
    new_name_2 = '/2pop'
    count = 1

    # prendo le cartelle riordinate
    # accedo alla cartella
    # rinomino il file
    # repeat per lunghezza dir

    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
    subdir = natsorted(list_subfolders_with_paths)
    print(subdir)

    if not skip:
        for sd in subdir:
            path_old_1 = sd + old_name_1
            path_old_2 = sd + old_name_2
            path_new_1 = sd + new_name_1 + str(count) + '.csv'
            path_new_2 = sd + new_name_2 + str(count) + '.csv'
            os.rename(src=path_old_1, dst=path_new_1)
            os.rename(src=path_old_2, dst=path_new_2)
            count += 1

    # subprocess.call(path + "dividi_et_impera.sh")
    subprocess.call("./dividi_et_impera.sh", shell=True)


if __name__ == '__main__':
    main()
