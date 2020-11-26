# authors: Yuanzhe Marco Ma, Arash Shamseddini, Kaicheng Tan, Zhenrui Yu
# date: 2020-11-25
"""Splits and pre-processes the  IMDB review data (from https://github.com/nproellochs/SentimentDictionaries).

Usage: pre_process.py --input_file=<input_file> --out_dir=<out_dir> 

Options:
<input_file>       Raw csv file path (downloaded from the website, csv format)
<out_dir>          Path to directory where the processed data should be written (in csv format)
"""

import os
import urllib.request
import pandas as pd
from pathlib import Path
from sklearn.model_selection import (
    train_test_split,
)
from docopt import docopt

opt = docopt(__doc__)
def main(input_file, out_dir):
    data = pd.read_csv(input_file)

    # split trainig and test data
    train_df, test_df = train_test_split(data, test_size=0.2, random_state=123)
    out_dir_train = out_dir + '/train.csv'
    out_dir_test = out_dir + '/test.csv'

    try:
        train_df.to_csv(out_dir_train, index=False)
        test_df.to_csv(out_dir_test, index=False)
    except:
        os.makedirs(os.path.dirname(out_dir_train))
        train_df.to_csv(out_dir_train, index=False)
        os.makedirs(os.path.dirname(out_dir_test))
        test_df.to_csv(out_dir_test, index=False)
if __name__ == "__main__":
    main(opt["--input_file"], opt["--out_dir"])
    
