#!/bin/bash

# Synchronize local copy of QHangups Python dependencies
# to their latest revisions from git/hg/bzr

PY_LIBS_DIR="libs"

create_link() {
    rm -f "$1"
    ln -s "$PY_LIBS_DIR/$1/$1" "$1"
}

sync_git() {
    if [ ! -d "$PY_LIBS_DIR/$2" ]; then
        git clone --recursive "$1" "$PY_LIBS_DIR/$2"
    else
        pushd "$PY_LIBS_DIR/$2" &>/dev/null
        git pull
        git submodule update --init --recursive
        popd &>/dev/null
    fi
    create_link "$2"
}

sync_hg() {
    if [ ! -d "$PY_LIBS_DIR/$2" ]; then
        hg clone "$1" "$PY_LIBS_DIR/$2"
    else
        pushd "$PY_LIBS_DIR/$2" &>/dev/null
        hg pull -u
        popd &>/dev/null
    fi
    create_link "$2"
}

sync_bzr() {
    if [ ! -d "$PY_LIBS_DIR/$2" ]; then
        bzr branch "$1" "$PY_LIBS_DIR/$2"
    else
        pushd "$PY_LIBS_DIR/$2" &>/dev/null
        bzr pull
        popd &>/dev/null
    fi
    create_link "$2"
}

if [ ! -d "$PY_LIBS_DIR" ]; then
    mkdir -p "$PY_LIBS_DIR"
fi

sync_git https://github.com/harvimt/quamash quamash
sync_git https://github.com/tdryer/hangups.git hangups
sync_git https://github.com/mtomwing/purplex purplex
sync_git https://github.com/zorro3/ConfigArgParse configargparse.py
sync_git https://github.com/ActiveState/appdirs appdirs.py
sync_git https://github.com/KeepSafe/aiohttp aiohttp
sync_git https://github.com/wardi/urwid.git urwid
sync_git https://github.com/jmcarp/robobrowser robobrowser
sync_git https://github.com/xmikos/reparser.git reparser.py
sync_git https://github.com/mitsuhiko/werkzeug werkzeug
sync_git https://github.com/kennethreitz/requests requests
sync_bzr lp:beautifulsoup bs4
sync_hg https://bitbucket.org/gutworth/six six.py
