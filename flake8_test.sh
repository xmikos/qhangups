#!/bin/bash
flake8 --exclude="qrc_*,ui_*" --ignore=E401 --max-line-length 119 --max-complexity 6 --show-source "$@"
