import os
import sys

import questionary

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.app import ColorTrackingApp
from src.utils.color_presets import SUPPORTED_COLORS


def main():
    selected = questionary.select(
        "🎨 Choose a color to track:", choices=list(SUPPORTED_COLORS.keys())
    ).ask()

    if selected is None:
        print("No color selected — exiting.")
        return

    bgr = SUPPORTED_COLORS[selected]
    app = ColorTrackingApp(bgr)
    app.run()


if __name__ == "__main__":
    main()
