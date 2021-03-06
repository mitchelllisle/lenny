import pandas as pd
import numpy as np
import warnings
try:
    from sklearn.preprocessing import LabelEncoder
except ImportError:
    warnings.warn("LabelEncoder function won't work as you seem to be missing sklearn")

def negabs(x):
    '''
    Inverse of ABS

    This is a simple functions for turning a positive number
    into a negative numbers.
    ----------
    PARAMS
    ----------
    x : Number to turn into a negative number

    ----------
    EXAMPLE
    ----------
    df.assign(negativeY = df.y.apply(lambda x: negabs(x)))
    '''
    return x * -1

def medianFrequency(value, frequency):
    computedMedian = np.median(value.repeat(frequency))
    return computedMedian

def normalise(data):
    '''
    Normalise a list of values to a number between 0 and 1

    This is a simple functions for turning a sequence of numbers
    into a value between 0 and 1. Useful for machine learning
    algorithms that require all features being on the same scale.
    ----------
    PARAMS
    ----------
    data : Column to apply normalise function over
    ----------
    EXAMPLE
    ----------
    data.assign(score = normalise(data, 'ProductionBudget'))
    '''
    minVal = data.min()
    maxVal = data.max()
    normalisedVals = (data - minVal) / (maxVal - minVal)
    return normalisedVals

def gini(data):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq:
    # http://www.statsdirect.com/help/generatedimages/equations/equation154.svg
    # from:
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    # All values are treated equally, arrays must be 1d:
    array = data.values
    array = array.astype(float)

    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))

def labelEncoder(data, column):
    '''
    labelEncoder
    Simple function for making Sklearn LabelEncoder easier to use in
    data science workflow. Given a string column, it will return integer
    encoded values for use in a machine learning algorithm that expects
    numeric values.
    ------
    PARAMS
    ------
    data : that contains the column you're interested in encoding
    column : Column that is to be encoded

    -------
    EXAMPLE
    -------
    fifaAbilities.assign(preferred_foot = mh.labelEncoder(fifaAbilities, "preferred_foot"))
    '''
    values = list(data[column])
    encodedLabels = LabelEncoder()
    encodedLabels = encodedLabels.fit_transform(values)
    return encodedLabels


def cleanUpString(text, strip_chars=[], replace_extras={}):
    # Credit for this code goes to: https://codereview.stackexchange.com/users/114734/double-j
    # Taken from this URL: https://codereview.stackexchange.com/questions/139549/python-string-clean-up-function-with-optional-args
    clean_up_items = {'\n': ' ', '\r': ' ', '\t': ' ', '  ': ' '}
    clean_up_items.update(replace_extras)

    text = text.strip()

    change_made = True
    while change_made:
        text_old = text
        for x in strip_chars:
            while text.startswith(x) or text.endswith(x):
                text = text.strip(x).strip()

        for key, val in clean_up_items.items():
            while key in text:
                text = text.replace(key, val)

        change_made = False if text_old == text else True

    return text.strip()
