import yaml

def create_config(config_exists: bool = False):
    if config_exists:
        operation = input('You alredy have a config file. Do you want to edit it? [n]: ')
        if operation in ('yes', 'y'):
            edit_config()
    config = {}
    num_watch_folders = int(input("How many folders would you like to watch?"))
    for _ in range(num_watch_folders):
        watch_folder = input("Absolute path of the folder to be watched: ")
        parent_folder = input("Parent folder to unzip files to (if same as watch folder just press enter): ") or watch_folder
        subfolder_yn = input("Would you like to parse file names and organize them into subfolders? (y/n): ")
        if subfolder_yn == 'n':
            pass



def edit_config():
    pass

if __name__ == '__main__':
    create_config()