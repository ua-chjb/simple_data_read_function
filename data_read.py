import pandas as pd
import numpy as np
import sys

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 10)

class Summary:

  def __init__(self, df, Y_colstr):
    self.df = df
    self.Y_colstr = Y_colstr

  def small_summary(self):
    return pd.DataFrame({
      "feature": self.df.columns,
      "dtype": self.df.dtypes.values,
      "nulls": self.df.isnull().sum().values,
      "nonnuls %": [
        f"{round((self.df[c].isnull().sum() / self.df.shape[0]) * 100, 2)}%"
        for c in self.df.columns
      ],
      "uniques": self.df.nunique().values,
      "uniques %": [
        f"{round((self.df[c].nunique() / len(self.df)) * 100, 2)}%"
        for c in self.df.columns
      ]
    })

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


  def large_summary(self):

    cols = self.df.columns
    numeric_collst = self.df.select_dtypes(include=[np.number]).columns
    corr_df = self.df[numeric_collst].corr() if self.Y_colstr in numeric_collst else None

    summary = pd.DataFrame({
      "BASE": ["|" for _ in cols],
      "feature": cols,
      "dtype": self.df.dtypes.values,
      "DESC. STATS": ["|" for _ in cols],
      "mean": [
        round(self.df[c].mean(), 2) 
        if c in numeric_collst
        else "" for c in cols
      ],
      "median": [
        round(self.df[c].median(), 2) 
        if c in numeric_collst
        else "" for c in cols
      ],
      "mode": [self.df[c].mode()[0] for c in cols],
      "min": [
        round(self.df[c].min(), 2)
        if c in numeric_collst 
        else "" for c in cols
      ],
      
      "25%": [
        round(self.df[c].quantile(0.25), 2)
        if c in numeric_collst 
        else "" for c in cols
      ],
      
      "50%": [
        round(self.df[c].quantile(0.5), 2)
        if c in numeric_collst 
        else "" for c in cols
      ],
      
      "75%": [
        round(self.df[c].quantile(0.75), 2) if
        c in numeric_collst
        else "" for c in cols
      ],
      
      "max": [
        round(self.df[c].max(), 2) if
        c in numeric_collst
        else "" for c in cols
      ],
      
      "skew": [
        "" if not pd.api.types.is_numeric_dtype(self.df[c])
        else "left" if (self.df[c].median() > self.df[c].mean()) 
        else "right" if (self.df[c].median() < self.df[c].mean())
        else "center" for c in cols
      ],

      "corr": [
        round(corr_df[self.Y_colstr].loc[c], 2) 
        if corr_df is not None and c in corr_df.index
        else ""
        for c in cols
      ],

      "COUNTS": ["|" for _ in cols],
      "outliers": [self._get_outliers_iqr(self.df[c]) for c in cols],
      "outliers %": [
        f"{round((self._get_outliers_iqr(self.df[c])/ self.df.shape[0]) * 100, 2)}%"
        if pd.api.types.is_numeric_dtype(self.df[c]) else ""
        for c in cols
      ],
      "uniques": self.df.nunique().values,
      "uniques %": [
        f"{round((self.df[c].nunique() / len(self.df)) * 100, 2)}%"
        if pd.api.types.is_numeric_dtype(self.df[c]) else ""
        for c in cols
      ],
      "nulls": self.df.isnull().sum().values,
      "nonnuls %": [
        f"{round((self.df[c].isnull().sum() / self.df.shape[0]) * 100, 2)}%"
        for c in cols
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