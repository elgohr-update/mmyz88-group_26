# authors: Yuanzhe Marco Ma, Arash Shamseddini, Kaicheng Tan, Zhenrui Yu
# date: 2020-11-28

"""Creates EDA visualizations and tables

Usage: eda_imdb.py <data> <out>

Options:
<data>     Path to the data to visualize
<out>      Path to directory for outputting results
"""

import os
from pathlib import Path

import altair as alt
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)


def main(data, out):
    train_df = pd.read_csv(data)

    # Create output directories in not exist
    Path(out).mkdir(parents=True, exist_ok=True)

    alt.Chart(train_df, title='Rating Distribution').mark_bar().encode(
        x=alt.X('Rating', bin=True, title='Rating'),
        y=alt.Y('count()', title="Counts")).configure_mark(
        color='steelblue'
    ) \
        .properties(width=500, height=450) \
        .save(os.path.join(out, 'histogram_rating_distribution.svg'))

    alt.Chart(train_df, title='Rating of Critics').mark_boxplot().encode(
        x='Rating',
        y='Author',
        color='Author'
    ) \
        .properties(width=500, height=450) \
        .save(os.path.join(out, 'boxplot_rating_critics.svg'))

    train_df.loc[:, 'TextLength'] = train_df['Text'].str.len()
    alt.Chart(train_df, title='Text length vs ratings').mark_bar().encode(
        x=alt.X('Rating', bin=True, title='Rating'),
        y=alt.Y('mean(TextLength):Q', title='Mean of the text length')
    ) \
        .properties(width=500, height=450) \
        .save(os.path.join(out, 'histogram_rating_vs_text_length.svg'))


if __name__ == '__main__':
    main(opt['<data>'], opt['<out>'])
