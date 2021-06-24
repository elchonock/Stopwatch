# C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WinRАR
import os
import time
from zipfile import ZipFile
# 1. The files and directories to be backed up are specified in a list.
source = [r'H:\my_source_dir']

# 2. The backup must be stored in a # main backup directory
target_dir = r'H:\MyTargetDir'

today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = input("input a comment -->")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" + comment.replace(' ', '_') + ".zip"

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
# Create target directory if it is not present
if not os.path.exists(today):
    os.mkdir(today)
    print('dir created')

# 5. We use the zip command to put the files in a zip archive
my_zip_file = ZipFile(target, mode='a')   #'C:\\"Program Files"\\7-Zip\\7z a -t7z -r "{0}" "{1}"'.format(target, ' '.join(source))

for folders in source:
    for folder, subfolder, files in os.walk(folders):
        my_zip_file.write(folder)
        for filename in files:
            my_zip_file.write(os.path.join(folder, filename))

my_zip_file.close()


# for folder, subfolder, files in os.walk(str(source)):
#     my_zip_file.write(folder)
#     for filename in files:
#         my_zip_file.write(os.path.join(folder, filename))
#
# my_zip_file.close()


# for folder, subfolder, files in os.walk(source):
# zip_obj.write(folder)
# for filename in files:
#     zip_obj.write(os.path.join(folder, filename))
# Run the backup


# print('Zip command is:')
# print(zip_command)
# print('Running:')
#
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')