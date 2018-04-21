import os

class BarcodeMediaPlayer():
    '''Main player object'''

    def __init__(self, config):

        # Determine if config is a file or a directory
        if os.path.isdir(config):
            self.config_dir = config
        else:
            raise NotImplemented('File-based configuration not yet implemented.')

        # Read config
        self.read_config()

    def cli(self):
        '''Invoke the BarcodeMediaPlayer CLI'''

        print 'cli'

    def read_config(self):
        '''Read the configuration'''

        print 'read_config'
        import fnmatch
        from .objects import get_object_from_xml

        for root, dirnames, filenames in os.walk(self.config_dir):
            for filename in fnmatch.filter(filenames, '*.xml'):
                media_object = get_object_from_xml(filename)
