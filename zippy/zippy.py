import zipfile, time, os, re, threading


class FolderWatcher:
    def __init__(self, folder, keyword_to_folder_map):
        self.folder = folder
        self.keyword_to_folder_map = keyword_to_folder_map
        self.running=True
        self.watcher_thread = threading.Thread(target=self.watch_loop).start()

    def watch_loop(self):
        while self.running:
            zip_file = next((f for f in os.listdir(self.folder) if '.zip' in f), None)
            if zip_file is not None:
                print('Found zip file: ', zip_file)
                self.smart_extract_zip(zip_file)
                print('Deleting zip file')
                os.remove(f'{self.folder}/{zip_file}')
            time.sleep(2)

    def smart_extract_zip(self, zip_file):
        assignment_kw = self.guess_assignment_type(zip_file)
        assignment_number_str = self.assignment_num_str(zip_file)
        dest_folder = f'{self.folder}/{self.keyword_to_folder_map[assignment_kw]}/{assignment_number_str}'
        print(f'Extracting {zip_file} to {dest_folder}')
        with zipfile.ZipFile(f'{self.folder}/{zip_file}', 'r') as zip_ref:
            zip_ref.extractall(dest_folder)

    def assignment_num_str(self, filename):
        assignment_number = re.search('([0-9]+)', filename).group()
        assignment_number = assignment_number.zfill(2)
        return assignment_number
        
    def guess_assignment_type(self, filename):
        for assignment_keyword in self.keyword_to_folder_map.keys():
            if assignment_keyword in filename:
                return assignment_keyword
        return None

cse_3100 = FolderWatcher('CSE 3100', {'hw': 'Homework', 'lab': 'Lab', 'thought': 'Code for Thought'})
