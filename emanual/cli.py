# -*- coding: utf-8 -*-
import click

from emanual import make


@click.group()
def main():
    """
    Welecome to EManual!
    """
    pass


@main.command()
def create():
    """
    Create the info.json File
    """
    make.create_info()


@main.command()
@click.option('--port', default=8000, help='port to listen')
def server(port):
    """
    Server to preview the markdown files
    """
    import os
    os.system('python -m SimpleHTTPServer %s' % port)
