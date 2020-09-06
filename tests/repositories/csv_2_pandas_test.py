# pytest読み込み
import pytest

import pandas as pd
from pandas.testing import assert_frame_equal

from repositories.csv_2_pandas import Csv2Pandas

SAMPLE_CSV_DATA_PATH = 'tests/data/Foo|Bar.csv'

def test_fetch():
    # Run
    node_csv = Csv2Pandas(SAMPLE_CSV_DATA_PATH)
    node_csv.fetch()

    # Expected data
    expected_df = pd.read_csv(SAMPLE_CSV_DATA_PATH)

    # Assert node_csv has proper pandas data frame as df
    assert_frame_equal(node_csv.df, expected_df)
    # Assert file_name
    assert node_csv.file_name == 'Foo|Bar'
