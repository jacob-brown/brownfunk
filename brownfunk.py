#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Jacob Brown
# Email j.brown19@imperial.ac.uk
# Date:   2020-04-14
# Last Modified: 2020-07-02


""" helpful functions defined by Jacob Brown """

# timer
import time
import shutil

def timer(state="S"):
    global startTimer

    """" timer(), timer("e") to start and stop timer """
    if state.lower() == "s":

        print("timer started")
        startTimer = time.time()  # start the timer from import

    elif state.lower() == "e":

        duration = time.time() - startTimer
        duration = round(duration)
        string = (
            "\n..........................\n"
            "   Time elapsed: {} sec"
            "\n..........................\n".format(duration)
        )

        print(string)

    else:
        stop("state not found, s or e only.")


# write csv
def write_csv(list_file, path):

    """ Write list to csv """

    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for i in list_file:
            if isinstance(i, list):
                writer.writerow(i)  # multi-column
            else:
                writer.writerow([i])  # single column


### save a text file without a new line at the end
def saveTxt(dirfile, listToSave, sep="\n"):
    with open(dirfile, "w") as f:
        for num, val in enumerate(listToSave):
            if num == len(listToSave) - 1:
                f.write(val)
            else:
                f.write(val + sep)


def open_csv(file):
    import csv

    """ open a csv into a list format """

    tmp = []  # initialise the list
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            tmp.append(row)  # add row to list

    return tmp


# sub process wrapper
def subprocessToList(command, returnError=False):
    """ wrapper for a subprocess command """
    p = subprocess.Popen(
        [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    out, er = p.communicate()
    out_string = out.decode()
    files = out_string.replace("\t", ":").split("\n")
    files.remove("")
    if returnError:
        return files, er
    else:
        return files


def groupBy(nestedList):

    """group by within a nested list
    index 0 key, index 1 value"""

    # group by
    data = np.array([int(i[1]) for i in nestedList])
    groups = np.array([i[0] for i in nestedList])
    groups_un = np.unique(groups)
    sums = sc.ndimage.sum(data, groups, groups_un)

    # create list and save
    store = []
    for i in range(0, len(sums)):
        store.append([groups_un[i], sums[i]])

    return store





def renameFileRecursion(fileIn):
    counter = 1
    while os.path.exists(fileIn):
        file, extention = os.path.splitext(fileIn)
        if counter > 1:
            file = file[0:len(file)-2]
        fileIn = file +'_' + str(counter) + extention
        counter = counter + 1
    return fileIn


def moveFile(fileFrom, fileTo):
    # rename if needed
    fileTo = renameFileRecursion(fileTo)
    # move
    shutil.move(fileFrom, fileTo)a