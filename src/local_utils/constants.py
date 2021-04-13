import os

# region Dataset

SRC_PATH = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'src'))
WORKSPACE_PATH = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'workspace'))
DATA_PATH = os.path.abspath(os.path.join(WORKSPACE_PATH, 'dataset'))

CARS_PATH = os.path.abspath(os.path.join(DATA_PATH, 'cars'))
CARS_IMAGES_PATH = os.path.abspath(os.path.join(CARS_PATH, 'images'))
CARS_ANNOTATIONS_PATH = os.path.abspath(os.path.join(CARS_PATH, 'annotations'))

PLATES_PATH = os.path.abspath(os.path.join(DATA_PATH, 'plates'))
PLATES_IMAGES_PATH = os.path.abspath(os.path.join(PLATES_PATH, 'images'))
PLATES_ANNOTATIONS_PATH = os.path.abspath(os.path.join(PLATES_PATH, 'annotations'))

CHARACTERS_PATH = os.path.abspath(os.path.join(PLATES_PATH, 'characters'))
CHARACTERS_IMAGES_PATH = os.path.abspath(os.path.join(CHARACTERS_PATH, 'images'))

# endregion Dataset

# region Output

OUTPUT_PATH = os.path.abspath(os.path.join(WORKSPACE_PATH, 'output'))

CARS_HISTORY_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'cars_history.csv'))
CARS_BEST_MODEL_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'cars_model_best.h5'))

PLATES_HISTORY_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'plates_history.csv'))
PLATES_BEST_MODEL_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'plates_model_best.h5'))

CHARACTERS_HISTORY_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'characters_history.csv'))
CHARACTERS_BEST_MODEL_FILE = os.path.abspath(os.path.join(OUTPUT_PATH, 'characters_model_best.h5'))

# endregion Output

# region Validation

RANDOM_SEED = 69228148822869
VALIDATION_SPLIT = 0.2

# endregion Validation

# region Training

CARS_TRAINING_SET_FILE = os.path.abspath(os.path.join(CARS_PATH, 'training_set.txt'))
CARS_VALIDATION_SET_FILE = os.path.abspath(os.path.join(CARS_PATH, 'validation_set.txt'))
CARS_LABELS_FILE = os.path.abspath(os.path.join(CARS_PATH, 'labels.txt'))

PLATES_TRAINING_SET_FILE = os.path.abspath(os.path.join(PLATES_PATH, 'training_set.txt'))
PLATES_VALIDATION_SET_FILE = os.path.abspath(os.path.join(PLATES_PATH, 'validation_set.txt'))
PLATES_LABELS_FILE = os.path.abspath(os.path.join(PLATES_PATH, 'labels.txt'))

CHARACTERS_LABELS_FILE = os.path.abspath(os.path.join(CHARACTERS_PATH, 'labels.txt'))

# endregion Training

# region Model

MODEL_CONFIG_FILE = os.path.abspath(os.path.join(SRC_PATH, 'configs', 'ssd300_mobilenetv2.json'))

# endregion Model

# region Inference

CONFIDENCE_THRESHOLD = 0.9
PREDICTIONS = 10
COORD_DELTA = 5

HAAR_CASCADES_PATH = os.path.abspath(os.path.join(SRC_PATH, 'haar_cascades'))
LICENSE_PLATE_CASCADES_FILE = os.path.abspath(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_russian_plate_number.xml'))

# endregion Inference

# region Plates

PLATES_SIZE = (520, 112)

# endregion Plates

# region Characters

CHARACTERS_SIZE = (32, 32)

# endregion Characters
