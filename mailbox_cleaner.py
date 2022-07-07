#!/usr/bin/env python3
"""mailbox-cleaner script to delete messages from IMAP folders.
"""

import datetime
from argparse import ArgumentParser

from imap_tools import A, MailBox, MailBoxTls, MailBoxUnencrypted
from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except (DistributionNotFound, ValueError):
    # package is not installed
    __version__ = "0.0.0.dev0-unknown"


def get_parser() -> ArgumentParser:
    """Create the argument parser for the program CLI"""
    parser = ArgumentParser(prog="mailbox-cleaner")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-c",
        "--connection",
        help="the connection method to connect with the IMAP server (default: %(default)s)",
        choices=["SSL", "STARTTLS", "PLAIN"],
        default="SSL",
    )
    parser.add_argument(
        "-f",
        "--folder",
        help="the IMAP folder to clean (default: %(default)s)",
        default="INBOX",
    )
    parser.add_argument(
        "-d",
        "--days",
        help=(
            "the minimum number of days old an email must be to be removed,"
            " if not provided ALL emails will be removed"
        ),
        type=int,
        default=0,
    )
    parser.add_argument(
        "host", help="the IMAP server's address (ex. imap.example.com:993)"
    )
    parser.add_argument("username", help="the username to login")
    parser.add_argument("password", help="the password to login")
    return parser


def clean(
    host: str, method: str, username: str, password: str, folder: str, days: int
) -> int:
    """Clean an IMAP folder"""
    if method == "PLAIN":
        cls = MailBoxUnencrypted
        port = "143"
    elif method == "STARTTLS":
        cls = MailBoxTls
        port = "143"
    else:
        cls = MailBox
        port = "993"
    if ":" in host:
        host, port = host.split(":")
    with cls(host, port=int(port)).login(username, password, folder) as mailbox:
        result = mailbox.delete(
            mailbox.uids(
                A(date_lt=datetime.date.today() - datetime.timedelta(days=days))
            )
        )
        return len(result[1][1]) if result else 0


def main() -> None:
    """Program's main entry point"""
    args = get_parser().parse_args()
    count = clean(
        args.host, args.connection, args.username, args.password, args.folder, args.days
    )
    print(f"{count} message(s) deleted")


if __name__ == "__main__":
    main()
