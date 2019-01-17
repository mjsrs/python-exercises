import click
import datetime
from globals import *
from utils import TextParser


def newFileName(file_name):
    # isolate file extension
    # reverse string name and split only one occurrency
    arr = file_name[::-1].split('.' ,1)
    #re-reverse file name; add time; add file extension
    return '%s_%s.%s' % (arr[1][::-1], datetime.datetime.now().strftime('%H%M%S'), arr[0])

@click.command()
@click.argument('fname', type=click.Path(exists=True))
def cli(fname):
    with open(fname, 'r') as article:
        new_file_name = newFileName(fname)
        with open(new_file_name, 'w') as new_article:
            text = TextParser(article, REPLACEMENTS)
            for line in text:
                new_article.write(line)

