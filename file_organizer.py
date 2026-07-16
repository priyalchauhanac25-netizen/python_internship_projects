import os
import shutil

source_folder = "Test_Files"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Python Files": [".py"]
}


for folder_name in file_categories:

    folder_path = os.path.join(source_folder, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file_name)[1]

        for folder_name, extensions in file_categories.items():

            if extension in extensions:

                destination = os.path.join(
                    source_folder,
                    folder_name,
                    file_name
                )

                shutil.move(file_path, destination)

                print(file_name, "moved to", folder_name)

                break


print("File organization completed successfully!")