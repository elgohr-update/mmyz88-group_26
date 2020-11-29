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
        y=alt.Y('count()', title="Counts")).configure_axis(
        grid=False).configure_view(
        strokeOpacity=0
    ).configure_mark(
        opacity=0.2,
        color='steelblue'
    ).save(os.path.join(out, 'histogram_rating_distribution.html'))

    alt.Chart(train_df, title='Rating of Critics').mark_boxplot().encode(
        x='Rating',
        y='Author',
        color='Author'
    ).save(os.path.join(out, 'boxplot_rating_critics.html'))

    alt.Chart(train_df,
              title='Relationship between Rating and Number of Words in the review').mark_line().encode(
        x=alt.X('n_words', bin=True, title='Number of Words'),
        y=alt.Y('mean(Rating)', title="Rating")
    ).save(os.path.join(out, 'line_rating_vs_num_words.html'))


if __name__ == '__main__':
    main(opt['<data>'], opt['<out>'])
