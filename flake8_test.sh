#!/bin/bash
flake8 --exclude="qrc_*,ui_*" --builtins="_" --ignore=E401,E402 --max-line-length 119 --max-complexity 8 --show-source "$@"
