import argparse
import os
import shutil
import datetime
from stat import ST_SIZE, ST_ATIME


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='.',
                        help='Which directory to organize?')
    parser.add_argument('--by', default='extension', help='Organize by?',
                        choices=['extension', 'size', 'last_used'])

    args = parser.parse_args()
    organize(args)


# getMetaData() recursively list out all the files and
# returns the required metadata for all the files
fileMetaData = []



def getMetaData(path):
    for file in os.scandir(path):
        if not file.is_dir():
            fileName = file.name
            filePath = file.path
            fileExtension = fileName.split('.')[-1]
            fileSize = os.stat(filePath)[ST_SIZE]
            fileLastUsed = os.stat(filePath)[ST_ATIME]
            fileMetaData.append(
                [fileName, filePath, fileExtension, fileSize, fileLastUsed])

        # If there are any subfolders availabe
        else:
            fileMetaData + [data for data in (getMetaData(file.path))]

    return fileMetaData

# This function arrange the files by their extension


def byExtension(path, metaData, organizedPath):
    for data in metaData:
        fileName = data[0]
        filePath = data[1]
        extension = data[2]

        if not os.path.exists(organizedPath + extension):
            os.makedirs(organizedPath + extension)

        shutil.move(filePath, organizedPath + extension + '\\' + fileName)

# This function arrange the files by their size


def bySize(path, metaData, organizedPath):
    for data in metaData:
        fileName = data[0]
        filePath = data[1]
        size = data[3]

        if size <= 1048576:     # 1 MB = 1048576 bytes
            if not os.path.exists(organizedPath + 'within 1 MB'):
                os.makedirs(organizedPath + 'within 1 MB')

            shutil.move(filePath, organizedPath + 'within 1 MB\\' + fileName)

        elif size <= 10485760:
            if not os.path.exists(organizedPath + 'within 10 MB'):
                os.makedirs(organizedPath + 'within 10 MB')

            shutil.move(filePath, organizedPath + 'within 10 MB\\' + fileName)

        elif size <= 104857600:
            if not os.path.exists(organizedPath + 'within 100 MB'):
                os.makedirs(organizedPath + 'within 100 MB')

            shutil.move(filePath, organizedPath + 'within 100 MB\\' + fileName)

        # If any file more than 100 MB
        else:
            if not os.path.exists(organizedPath + 'more than 100 MB'):
                os.makedirs(organizedPath + 'more than 100 MB')

            shutil.move(filePath, organizedPath +
                        'more than 100 MB\\' + fileName)

# This function arrange the files by their last used date


def byLastUsed(path, metaData, organizedPath):
    currDate = datetime.date.today()
    for data in metaData:
        fileName = data[0]
        filePath = data[1]
        lastUsed = datetime.date.fromtimestamp(data[4])

        if lastUsed == currDate:
            if not os.path.exists(organizedPath + 'today'):
                os.makedirs(organizedPath + 'today')

            shutil.move(filePath, organizedPath + 'today\\' + fileName)

        elif currDate - lastUsed == datetime.timedelta(days=1):
            if not os.path.exists(organizedPath + 'yesterday'):
                os.makedirs(organizedPath + 'yesterday')

            shutil.move(filePath, organizedPath + 'yesterday\\' + fileName)

        # File used for the last 7 days
        elif currDate - lastUsed <= datetime.timedelta(days=7):
            if not os.path.exists(organizedPath + 'this week'):
                os.makedirs(organizedPath + 'this week')

            shutil.move(filePath, organizedPath + 'this week\\' + fileName)

        # If any file used more than a week ago
        else:
            if not os.path.exists(organizedPath + 'more than a week ago'):
                os.makedirs(organizedPath + 'more than a week ago')

            shutil.move(filePath, organizedPath +
                        'more than a week ago\\' + fileName)

# This function check the condition by which the files
# needs to be arranged and then call the required function


def organize(args):
    path = args.path
    organizeBy = args.by
    print(path)

    # For exception handling during wrong path input
    try:
        metaData = getMetaData(path)
    except FileNotFoundError:
        print('Invalid directory')
        return

    if not os.path.exists(path + '\\organized'):
        os.makedirs(path + '\\organized')
    organizedPath = path + '\\organized\\'

    if organizeBy == 'extension':
        byExtension(path, metaData, organizedPath)
    elif organizeBy == 'size':
        bySize(path, metaData, organizedPath)
    else:
        byLastUsed(path, metaData, organizedPath)

    print('All files have been organized--- \nOrganized folder path:',
          path + '\\organized')


# Driver code
if __name__ == '__main__':
    main()
