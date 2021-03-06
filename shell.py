#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse

from flask import Flask

import scripts  # Do not remove this line
from utils.command import Command


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    for command in Command.__subclasses__():
        command.register(subparsers)
    args = parser.parse_args()
    args.run(**args.__dict__)

