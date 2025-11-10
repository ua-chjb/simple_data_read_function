from data_read import read_in_csv, quick_peek
import pandas as pd
import pytest

def test_valid_csv_valid_path():
    result = read_in_csv("C:/Users/benno/OneDrive/Data/DVM-CAR/price_table.csv")
    assert isinstance(result, pd.DataFrame)

def test_invalid_csv_valid_path():
    with pytest.raises(SystemExit):
        read_in_csv("C:/Users/benno/OneDrive/Data/DVM-CAR/price_table.pdf")

def test_valid_csv_invalid_path():
    with pytest.raises(SystemExit):
        read_in_csv("price_table.csv")

def test_invalid_csv_invalid_path():
    with pytest.raises(SystemExit):
        read_in_csv("price_table.pdf")