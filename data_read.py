import pandas as pd
import numpy as np
import sys

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 10)

class Summary:

  def __init__(self, df: pd.DataFrame, Y_colstr: str):
    self.df = df
    self.Y_colstr = Y_colstr
    self.collst = df.columns
    self.numeric_collst = self.df.select_dtypes(include=[np.number]).columns
    self.null_counts = df.isnull().sum()
    self.unique_counts = df.nunique()

  def _get_outliers_iqr(self, c):
    if not pd.api.types.is_numeric_dtype(c):
      return ""
    
    q1 = c.quantile(0.25)
    q3 = c.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 *iqr
    upper_bound = q3 + 1.5 *iqr

    outliers = c[(c < lower_bound) | (c > upper_bound)]
    return len(outliers)


  def small_summary(self):
    return pd.DataFrame({
      "feature": self.collst,
      "dtype": self.df.dtypes.values,
      "nulls": self.null_counts,
      "nonnuls %": [
        f"{round((self.null_counts[c] / self.df.shape[0]) * 100, 2)}%"
        for c in self.collst
      ],
      "uniques": self.df.nunique().values,
      "uniques %": [
        f"{round((self.unique_counts[c] / len(self.df)) * 100, 2)}%"
        for c in self.collst
      ]
    })

  def large_summary(self):

    corr_df = self.df[self.numeric_collst].corr() if self.Y_colstr in self.numeric_collst else None

    summary = pd.DataFrame({
      "BASE": ["|" for _ in self.collst],
      "feature": self.collst,
      "dtype": self.df.dtypes.values,
      "DESC. STATS": ["|" for _ in self.collst],
      "mean": [
        round(self.df[c].mean(), 2) 
        if c in self.numeric_collst
        else "" for c in self.collst
      ],
      "median": [
        round(self.df[c].median(), 2) 
        if c in self.numeric_collst
        else "" for c in self.collst
      ],
      "mode": [self.df[c].mode()[0] for c in self.collst],
      "min": [
        round(self.df[c].min(), 2)
        if c in self.numeric_collst 
        else "" for c in self.collst
      ],
      
      "25%": [
        round(self.df[c].quantile(0.25), 2)
        if c in self.numeric_collst 
        else "" for c in self.collst
      ],
      
      "50%": [
        round(self.df[c].quantile(0.5), 2)
        if c in self.numeric_collst 
        else "" for c in self.collst
      ],
      
      "75%": [
        round(self.df[c].quantile(0.75), 2) if
        c in self.numeric_collst
        else "" for c in self.collst
      ],
      
      "max": [
        round(self.df[c].max(), 2) if
        c in self.numeric_collst
        else "" for c in self.collst
      ],
      
      "skew": [
        "" if not pd.api.types.is_numeric_dtype(self.df[c])
        else "left" if (self.df[c].median() > self.df[c].mean()) 
        else "right" if (self.df[c].median() < self.df[c].mean())
        else "center" for c in self.collst
      ],

      "corr": [
        round(corr_df[self.Y_colstr].loc[c], 2) 
        if corr_df is not None and c in corr_df.index
        else ""
        for c in self.collst
      ],

      "COUNTS": ["|" for _ in self.collst],
      "outliers": [self._get_outliers_iqr(self.df[c]) for c in self.collst],
      "outliers %": [
        f"{round((self._get_outliers_iqr(self.df[c])/ self.df.shape[0]) * 100, 2)}%"
        if pd.api.types.is_numeric_dtype(self.df[c]) else ""
        for c in self.collst
      ],
      "uniques": self.unique_counts,
      "uniques %": [
        f"{round((self.unique_counts[c] / len(self.df)) * 100, 2)}%"
        if pd.api.types.is_numeric_dtype(self.df[c]) else ""
        for c in self.collst
      ],
      "nulls": self.null_counts,
      "nonnuls %": [
        f"{round((self.null_counts[c] / self.df.shape[0]) * 100, 2)}%"
        for c in self.collst
      ],
    })

    return summary

def main():

  path_str = get_path()
  df = read_in_csv(path_str)
  quick_peek(df)
  Y_colstr = input_dependent(df)
  summary = Summary(df, Y_colstr)
  run_summaries(summary)

  return summary

def get_path():
  return input("Path: ")

def read_in_csv(path):
  if path.split(".")[-1] == "csv":
    try:
      return pd.read_csv(path)
    except:
      sys.exit("Not a valid path")
  else:
    sys.exit("Not a csv file")

def quick_peek(df):
  print(f"shape of df is {df.shape}")
  print(f"dtypes of df is {df.dtypes}")
  print(f"head of df is {df.head(5)}")
  return

def input_dependent(df):
  Y_colstr = input("Dependent variable: ")
  if Y_colstr not in df.columns:
    sys.exit("Not a column in the df")
  return Y_colstr

def run_summaries(summary):
  print(summary.small_summary())
  print(summary.large_summary())

if __name__ == "__main__":
  main()