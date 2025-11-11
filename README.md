# simple_data_read_function
final project for Harvard EDX CS50 Python

Video: [youtube.com/watch?v=0aRj9Cpn-HY&feature=youtu.be]
Github: [https://github.com/ua-chjb/simple_data_read_function/tree/main]

This program reads in a csv and passes it through a class to summarize the dataframe. The class Summary has methods `small_summary()` and `large_summary()`, which can be called as reference points at any time during EDA.

The method `small_summary()` is similar to `df.dypes()`, but with the following improvements:
- nulls: the method computes both the raw count of null values and the percentage of nulls over the length of the dataframe.
- uniques: the method computes both the raw count of uniques and the percentage of uniques over the length of the dataframe. This is useful for identifying which variables should be transformed to categorical later on in the pipeline.

The method `large_summary()` is similar to `df.describe()`, but with the following improvements:
- inclusion of nulls, as above.
- inclusion of uniques, as above.
- descriptive statistics: mean, median and mode, compared side-by-side.
- quantile ranges: min, 25%, 50%, 75%, max. (50% is redundant with the median.)
- skew: returns "right", "left", or "center", based on the comparison between median and mean.
- corr: returns Pearson's correlation coefficient for each column in terms of the dependent variable.
- outliers: using an internal method, an interquartile range is computed on each column. A count of the dataframe with the iqr method applied then returns the number of outliers. The percentage of outliers is also included.

Other functions in the program:
- `get_path()`: user inputs the path of the csv file.
- `read_in_csv()`: python opens the file if it is both a legitimate path and a csv file, else the system exist.
- `input_dependent()`: user inputs the Y variable for analysis in `large_summary`'s correlation computation.
- `quick_peek()`: python prints the shape, dtypes, and head of the dataframe, primarily so that the user can ascertain which of the variables is the dependent.

Unit tests:
- the program runs unit tests to ensure that only valid paths of valid csv files are processed.

Sample data:
- the program does not use the `open` method, as this only works with local data.
- to avoid unnecessary cost and portability, the testing data files are hosted open-source in this repository.
- data files' lengths are between 700 and 285 000.
- to avoid large compute time, the large csv has been commented out in unit testing.