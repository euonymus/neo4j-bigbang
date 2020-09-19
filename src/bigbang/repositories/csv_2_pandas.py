import pandas as pd
from pandas.api.types import is_numeric_dtype
from pathlib import Path
class Csv2Pandas(object):
    """
    Private Properties and Getters
    """
    @property
    def df(self):
        pass

    @df.getter
    def df(self):
        return self.__df

    @property
    def file_name(self):
        pass

    @df.getter
    def file_name(self):
        return self.__file_name

    """
    Constructor
    """
    def __init__(self, file_path = None):
        self.file_path = file_path

    def _fetch(self, file_path):
        if not self.file_path:
            raise AttributeError('file_path is not properly prepared.')
        file_name = Path(self.file_path)
        self.__file_name = file_name.stem
        self.__df = pd.read_csv(file_path ,header=0)

    def fetch(self):
        self._fetch(self.file_path)

    @staticmethod
    def property(prop):
        return None if pd.isnull(prop) else prop
