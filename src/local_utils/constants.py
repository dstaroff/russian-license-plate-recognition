import os

WORKSPACE = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'workspace'))
DATA_PATH = os.path.abspath(os.path.join(WORKSPACE, 'dataset'))
IMAGES_PATH = os.path.abspath(os.path.join(DATA_PATH, 'images'))
ANNOTATIONS_PATH = os.path.abspath(os.path.join(DATA_PATH, 'annotations'))