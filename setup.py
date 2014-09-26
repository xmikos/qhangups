#!/usr/bin/env python

from distutils.core import setup
from qhangups.qhangups import __version__

setup(name="QHangups",
      version=__version__,
      description="Alternative client for Google Hangouts written in PyQt",
      author="Michal Krenek (Mikos)",
      author_email="m.krenek@gmail.com",
      url="https://github.com/xmikos/qhangups",
      license="GNU GPLv3",
      packages=["qhangups"],
      package_data={"qhangups": ["qhangups.svg", "qhangups_disabled.svg"]},
      data_files=[("share/applications", ["qhangups.desktop"]),
                  ("share/pixmaps", ["qhangups.png"])],
      scripts=["scripts/qhangups"],
      requires=["hangups", "appdirs", "asyncio", "PyQt4", "Quamash"])
