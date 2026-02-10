#Autor Maciej Klimiuk

import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Creates a new DataFrame with an additional calculated column based on the role expression.
    Returns an empty DataFrame if validation fails.
    """

    # 1. Define Regex for strict name validation
    name_pattern = re.compile(r'^[a-zA-Z_]+$')

    # 2. Validate the 'new_column' name
    if not name_pattern.match(new_column):
        return pd.DataFrame([])

    # 3. Validate existing DataFrame column names
    for col in df.columns:
        if not name_pattern.match(str(col)):
            return pd.DataFrame([])

    # 4. Validate the 'role' string content
    allowed_role_chars = re.compile(r'^[a-zA-Z_\s\+\-\*]+$')
    if not allowed_role_chars.match(role):
        return pd.DataFrame([])

    # 5. Validate that columns mentioned in 'role' actually exist in the DataFrame
    role_columns = re.findall(r'[a-zA-Z_]+', role)
    for col in role_columns:
        if col not in df.columns:
            return pd.DataFrame([])

    # 6. Compute the new column
    try:
        # Create a copy to prevent modifying the original dataframe
        result_df = df.copy()

        result_df[new_column] = result_df.eval(role)

        return result_df

    except Exception:
        # Catches syntax errors or other issues during evaluation
        return pd.DataFrame([])