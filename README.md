# mailbox-cleaner

a simple CLI tool to clean IMAP folders

[![Latest Release](https://img.shields.io/pypi/v/mailbox-cleaner.svg)](https://pypi.org/project/mailbox-cleaner)
[![Supported Versions](https://img.shields.io/pypi/pyversions/mailbox-cleaner.svg)](https://pypi.org/project/mailbox-cleaner)
[![Downloads](https://pepy.tech/badge/mailbox-cleaner)](https://pepy.tech/project/mailbox-cleaner)
[![License](https://img.shields.io/pypi/l/mailbox-cleaner.svg)](https://pypi.org/project/mailbox-cleaner)
[![CI](https://github.com/adbenitez/mailbox-cleaner/actions/workflows/python-ci.yml/badge.svg)](https://github.com/adbenitez/mailbox-cleaner/actions/workflows/python-ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation

To install with pip:

```
$ pip install -U mailbox-cleaner
```

After installation the command `mailbox-cleaner` should be available.
You can also just download the `mailbox_cleaner.py` file and execute it directly.

## Usage

To delete emails older than 15 days in the INBOX folder:
```
mailbox-cleaner imap.example.com me@example.com myPassword -d 15
```

To delete emails older than 30 days in the Trash folder using a STARTTLS connection to a host with non-standard port:
```
mailbox-cleaner imap.example.com:9999 me@example.com myPassword -c STARTTLS -f Trash -d 30
```

To see all available options and more information use:
```
mailbox-cleaner --help
```

## License

Licensed GPLv3+, see the LICENSE file for details.

Copyright © 2022 Asiel Díaz Benítez.
