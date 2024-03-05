import pandas as pd
import seaborn as sns
import numpy as np
import os

import config

if __name__ == "__main__":
    ds = pd.read_csv(config.DSSRC)
    print(ds)