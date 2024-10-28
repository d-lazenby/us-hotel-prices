from pathlib import Path
import os

# Path(__file__): the current file path
# Path(__file__).parent: its parent dir
# Path(__file__).parent.resolve: absolute path to parent
# Path(__file__).parent.resolve.parent: the grandparent dir of the current file
PARENT_DIR = Path(__file__).parent.resolve().parent

DATA_DIR = PARENT_DIR / "data"
