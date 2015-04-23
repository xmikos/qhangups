#!/usr/bin/env python

from distutils.core import setup
from qhangups.version import __version__

setup(name="QHangups",
      version=__version__,
      description="Alternative client for Google Hangouts written in PyQt",
      author="Michal Krenek (Mikos)",
      author_email="m.krenek@gmail.com",
      url="https://github.com/xmikos/qhangups",
      license="GNU GPLv3",
      packages=["qhangups"],
      package_data={"qhangups": ["qhangups.svg",
                                 "qhangups_disabled.svg",
                                 "languages/*.qm"]},
      data_files=[("share/applications", ["qhangups.desktop"]),
                  ("share/pixmaps", ["qhangups.png"])],
      scripts=["scripts/qhangups"],
      requires=["hangups", "appdirs", "asyncio", "PyQt4", "Quamash"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: MacOS X',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications :: Qt',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Communications :: Chat'
      ])
