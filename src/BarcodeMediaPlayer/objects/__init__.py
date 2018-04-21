import xml.etree.ElementTree as ET

from .album import Album
from .playlist import Playlist

def get_object_from_xml(path):
    print 'get_object_from_xml %s' % path
