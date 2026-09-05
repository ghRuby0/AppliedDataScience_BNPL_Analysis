# Creates some data layer folders in the parent folder of the current-working-directory

from pathlib import Path

parent = Path.cwd().parent
(parent / "i_landing_layer").mkdir(parents=True, exist_ok=True) 

