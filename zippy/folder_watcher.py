import zipfile, time, os, re, threading


class FolderWatcher:
    def __init__(self, watch_folder, subfolder_keyword_map, parent_folder = None):
        self.watch_folder = watch_folder
        self.parent_folder = parent_folder if parent_folder else watch_folder
        self.subfolder_keyword_map = subfolder_keyword_map
        self.running=True
        self.watcher_thread = threading.Thread(target=self.watch_loop).start()

    def watch_loop(self):
        while self.running:
            zip_file = next((f for f in os.listdir(self.watch_folder) if '.zip' in f), None)
            if zip_file is not None:
                print('Found zip file: ', zip_file)
                self.smart_extract_zip(zip_file)
                print('Deleting zip file')
                os.remove(f'{self.watch_folder}/{zip_file}')
            time.sleep(2)

    def smart_extract_zip(self, zip_file):
        subfolder = self.parse_assignment_type(zip_file)
        assignment_number_str = self.parse_num_str(zip_file)
        dest_folder = f'{self.parent_folder}/{subfolder}/{assignment_number_str}'
        print(f'Extracting {zip_file} to {dest_folder}')
        with zipfile.ZipFile(f'{self.parent_folder}/{zip_file}', 'r') as zip_ref:
            zip_ref.extractall(dest_folder)

    def parse_num_str(self, filename):
        assignment_number = re.search('([0-9]+)', filename).group().zfill(2)
        return assignment_number
        
    def parse_assignment_type(self, filename):
        for subfolder, keywords in self.subfolder_keyword_map.items():
            if any((kw for kw in keywords if kw in filename)):
                return subfolder
        return None
