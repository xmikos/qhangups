#!/usr/bin/env python

import sys

from setuptools import setup
from qhangups.version import __version__

install_requires = [
    "hangups>=0.4.1",
    "appdirs",
    "Quamash"
]

if sys.version_info < (3, 4):
    install_requires.append("asyncio")

setup(
    name="QHangups",
    version=__version__,
    description="Alternative client for Google Hangouts written in PyQt",
    author="Michal Krenek (Mikos)",
    author_email="m.krenek@gmail.com",
    url="https://github.com/xmikos/qhangups",
    license="GNU GPLv3",
    packages=["qhangups"],
    package_data={
        "qhangups": [
            "qhangups.svg",
            "qhangups_disabled.svg",
            "*.ui",
            "languages/*.qm",
            "languages/*.ts"
        ]
    },
    data_files=[
        ("share/applications", ["qhangups.desktop"]),
        ("share/pixmaps", ["qhangups.png"])
    ],
    entry_points={
        "gui_scripts": [
            "qhangups=qhangups.__main__:main"
        ],
    },
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications :: Chat"
    ]
)
