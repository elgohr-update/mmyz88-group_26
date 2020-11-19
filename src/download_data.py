"""Download file from an URL to a local path
Usage:
  download_data.py <url> <download_path>
  download_data.py (-h | --help)
Options:
  -h, --help
"""
from docopt import docopt
import urllib.request


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(f'Downloading {arguments["<url>"]} to {arguments["<download_path>"]}...')
    urllib.request.urlretrieve(arguments['<url>'], arguments['<download_path>'])
