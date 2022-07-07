"""Setup module installation."""

import os

from setuptools import setup


def load_requirements(path: str) -> list:
    """Load requirements from the given relative path."""
    with open(path, encoding="utf-8") as file:
        requirements = []
        for line in file.read().split("\n"):
            if line.startswith("-r"):
                dirname = os.path.dirname(path)
                filename = line.split(maxsplit=1)[1]
                requirements.extend(load_requirements(os.path.join(dirname, filename)))
            elif line and not line.startswith("#"):
                requirements.append(line)
        return requirements


if __name__ == "__main__":
    MODULE_NAME = "mailbox_cleaner"
    with open("README.md", encoding="utf-8") as readme:
        long_desc = readme.read()

    setup(
        name=MODULE_NAME,
        setup_requires=["setuptools_scm"],
        use_scm_version={
            "root": ".",
            "relative_to": __file__,
            "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
            "git_describe_command": "git describe --dirty --tags --long --match v*.*.*",
        },
        description="Command line utility to clean IMAP folders",
        long_description=long_desc,
        long_description_content_type="text/markdown",
        author="adbenitez",
        author_email="adbenitez@hispanilandia.net",
        url=f"https://github.com/adbenitez/{MODULE_NAME}",
        py_modules=[MODULE_NAME],
        keywords="cli email imap cleaner",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3",
        ],
        entry_points="""
            [console_scripts]
            mailbox-cleaner=mailbox_cleaner:main
        """,
        python_requires=">=3.7",
        install_requires=load_requirements("requirements/requirements.txt"),
        extras_require={
            "test": load_requirements("requirements/requirements-test.txt"),
            "dev": load_requirements("requirements/requirements-dev.txt"),
        },
    )
