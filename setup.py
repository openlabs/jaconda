# -*- coding: utf-8 -*-
"""
    setup

    Jaconda Python API - Unofficial

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) LTD
    :license: BSD, see LICENSE for more details.
"""
from setuptools import setup

setup(
    name = "jaconda",
    version = "0.1",
    description = "Python client to Jaconda API v2",
    author = "Sharoon Thomas, Openlabs Technologies & Consulting (P) Limited",
    author_email = "sales@openlabs.co.in",
    url = "http://openlabs.co.in",
    license = "BSD",

    install_requires = [
        "requests",
    ],
    packages = ["jaconda"],
    package_dir = {
        "jaconda": ".",
    },
    classifiers = [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Topic :: Communications :: Chat",
    ],

)
