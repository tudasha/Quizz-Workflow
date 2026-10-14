import sys
from pathlib import Path

# The tools are scripts run from coach/general/tools, not an installed package.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
