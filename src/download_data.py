"""Download file from an URL to a local path

Usage:
  download_data.py <url> <download_path>
  download_data.py (-h | --help)

Options:
  <url>             URL to the file to download
  <download_path>   Path (including filename) where the downloaded file should be stored
  -h, --help        Display help
"""
import os
import urllib.request
from pathlib import Path

from docopt import docopt


def main(url, out_file):
    # Create parent directories recursively if not exist
    Path(os.path.dirname(out_file)).mkdir(parents=True, exist_ok=True)

    # Download file from URL
    urllib.request.urlretrieve(url, out_file)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(f'Downloading {arguments["<url>"]} to {arguments["<download_path>"]}')
    main(arguments["<url>"], arguments["<download_path>"])
