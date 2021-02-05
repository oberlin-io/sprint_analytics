import yaml
import os

class Config():

    def __init__(self, root_path):
        
        self.root_path = root_path
        self.pack_path = 'config'
        self.config_filepath = os.path.join(
            self.root_path,
            self.pack_path,
            'config.yaml'
            )


    def set(self):

        with open(self.config_filepath) as f:
            self.config = yaml.safe_load(f.read())


    def get(self):

        return self.config
