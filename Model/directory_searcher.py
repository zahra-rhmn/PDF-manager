import glob
import os
import string


def search_with_sub(directory):
    pdfs = []
    for subdir in os.walk(directory):
        address = subdir[0]
        files = subdir[2]
        for f in files:
            if f[-4::1].lower() == '.pdf':
                pdfs.append((address, f))
    return pdfs


def search_all_pc():
    pdfs = []
    list_of_drives = []

    for lt in string.ascii_uppercase:
        if os.path.exists(lt + ':'):
            list_of_drives.append(lt+':\\')
    for drive in list_of_drives:
        pdfs = pdfs + search_with_sub(drive)
    return pdfs


def search_directory(path):
    pdfs = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            if f[-4::1] == '.pdf':
                pdfs.append((path, f))
    return pdfs

print(len(search_all_pc()))