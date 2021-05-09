from pathlib import Path
import sys
import os
import logging as _logging
import logging.config
import yaml

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QSystemTrayIcon, QMenu, QAction)  # type: ignore

from .app.types import AppData  # type: ignore
from .app.windows import AppWindows  # type: ignore

from simsapa.assets import icons_rc

logger = _logging.getLogger(__name__)


def main():
    if os.path.exists("logging.yaml"):
        with open("logging.yaml", 'r') as f:
            config = yaml.safe_load(f.read())
            _logging.config.dictConfig(config)

    logger.info("main()")

    paths = [
        Path.cwd().joinpath("appdata.sqlite3"),
        Path.home().joinpath(".config/simsapa/assets/appdata.sqlite3"),
    ]

    db_path = None

    for p in paths:
        if p.is_file():
            db_path = p

    if db_path is None:
        print("ERROR: Cannot find appdata.sqlite3")
        exit(1)

    app_data = AppData(db_path)

    app = QApplication(sys.argv)

    # Create systray
    app.setQuitOnLastWindowClosed(False)

    tray = QSystemTrayIcon(QIcon(":bookmark"))
    tray.setVisible(True)

    menu = QMenu()

    ac = QAction(QIcon(":close"), "Quit")
    ac.triggered.connect(app.quit)
    menu.addAction(ac)

    tray.setContextMenu(menu)

    # Create first window

    app_windows = AppWindows(app, app_data)
    app_windows._new_sutta_search_window()

    logger.info("Exiting.")
    sys.exit(app.exec_())
