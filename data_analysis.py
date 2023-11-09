import pandas as pd
import numpy as np
from ta import add_all_ta_features

def analyze_data(data):
    data = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")
    return data