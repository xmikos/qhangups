QHangups
========

Alternative client for Google Hangouts written in PyQt

Requirements
------------

- Python >= 3.3
- PyQt >= 4.5
- Quamash (https://github.com/harvimt/quamash) - *latest Git revision*
- hangups (https://github.com/tdryer/hangups) - *latest Git revision*
- appdirs (https://github.com/ActiveState/appdirs)
- asyncio (https://pypi.python.org/pypi/asyncio) for Python < 3.4

Usage
-----

Run ``qhangups --help`` to see all available options.
Start QHangups by running ``qhangups``.

The first time you start QHangups, you will be prompted to log into your
Google account. Your credentials will only be sent to Google, and only
session cookies will be stored locally. If you have trouble logging in,
try logging in through a browser first.

Help
----
::

    usage: qhangups [-h] [-d] [--log LOG] [--cookies COOKIES]
    
    optional arguments:
      -h, --help         show this help message and exit
      -d, --debug        log detailed debugging messages (default: False)
      --log LOG          log file path (default:
                         ~/.local/share/QHangups/hangups.log)
      --cookies COOKIES  cookie storage path (default:
                         ~/.local/share/QHangups/cookies.json)
