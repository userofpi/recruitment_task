import pandas as pd
from solution import add_virtual_column

def test_sum_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), f"The function should sum the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"

def test_multiplication_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns = ["label_one",
    "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one * label_two", "label_three")
    assert df_result.equals(df_expected), f"The function should multiply the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"

def test_subtraction_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 0]] * 2, columns = ["label_one",
    "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one - label_two", "label_three")
    assert df_result.equals(df_expected), f"The function should subtract the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"

def test_empty_result_when_invalid_labels():
    df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label3")
    assert df_result.empty, f"Should return an empty df when the \"new_column\" is invalid.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df = pd.DataFrame([[1, 2]] * 3, columns=["label-one", "label_two"])
    df_result = add_virtual_column(df, "label-one + label_two", "label")
    assert df_result.empty, f"Should return an empty df when both df columns and roles are invalid.\n\nResult:\n\n {df_result}\n\nExpected:\n\nEmpty df "
    df = pd.DataFrame([[1, 2]] * 3, columns=["label-one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label")
    assert df_result.empty, f"Should return an empty df when a df column is invalid.\n\nResult:\n\n {df_result}\n\nExpected:\n\nEmpty df"

def test_empty_result_when_invalid_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one \\ label_two", "label_three")
    assert df_result.empty, f"Should return an empty df when the role have invalid character: '\\'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df_result = add_virtual_column(df, "label&one + label_two", "label_three")
    assert df_result.empty, f"Should return an empty df when the role have invalid character: '&'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df_result = add_virtual_column(df, "label_five + label_two","label_three")
    assert df_result.empty, f"Should return an empty df when the role have a column which isn't in the df: 'label_five'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"

def test_when_extra_spaces_in_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns = ["label_one","label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), f"Should work when the role haven't spaces between the operation and the column.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    df_result = add_virtual_column(df, "label_one + label_two ","label_three")
    assert df_result.equals(df_expected), f"Should work when the role have spaces between the operation and the column.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    df_result = add_virtual_column(df, " label_one + label_two ","label_three")
    assert df_result.equals(df_expected), f"Should work when the role have extra spaces in the start/end.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"


if __name__ == "__main__":
    # Test 1: add
    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(add_virtual_column(df1, "a + b", "sum"))

    # Test 2: subtraction
    df2 = pd.DataFrame({"revenue": [100, 200], "cost": [30, 50]})
    print(add_virtual_column(df2, "revenue - cost", "profit"))

    # Test 3: Complex expression
    df3 = pd.DataFrame({"x": [10, 20], "y": [5, 10], "z": [2, 3]})
    print(add_virtual_column(df3, "x * y + z", "result"))

    # Test 4: Error - non-existent column
    df4 = pd.DataFrame({"a": [1, 2]})
    print(add_virtual_column(df4, "a + b", "c"))  # pusty DataFrame

    # Test 5: Error - invalid name
    df5 = pd.DataFrame({"a": [1, 2]})
    print(add_virtual_column(df5, "a + a", "new-column"))  # pusty DataFrame

    test_sum_of_two_columns()
    test_multiplication_of_two_columns()
    test_subtraction_of_two_columns()
    test_empty_result_when_invalid_labels()
    test_empty_result_when_invalid_rules()
    test_when_extra_spaces_in_rules()
    print("All tests passed!")


