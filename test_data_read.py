from data_read import read_in_csv
import pandas as pd
import pytest

@pytest.mark.parametrize("path", [
    # "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Ad_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Sales_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Price_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Basic_table.csv"
])
def test_valid_csv_valid_path(path):
    result = read_in_csv(path)
    assert isinstance(result, pd.DataFrame)

@pytest.mark.parametrize("path", [
    # "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Ad_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Sales_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Price_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/data/Basic_table.pdf"
])
def test_invalid_csv_valid_path(path):
    with pytest.raises(SystemExit):
        read_in_csv(path)

@pytest.mark.parametrize("path", [
    # "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Ad_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Sales_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Price_table.csv",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Basic_table.csv"
])
def test_valid_csv_invalid_path(path):
    with pytest.raises(SystemExit):
        read_in_csv(path)

@pytest.mark.parametrize("path", [
    # "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Ad_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Sales_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Price_table.pdf",
    "https://raw.githubusercontent.com/ua-chjb/simple_data_read_function/refs/heads/main/Basic_table.pdf"
])
def test_invalid_csv_invalid_path(path):
    with pytest.raises(SystemExit):
        read_in_csv(path)