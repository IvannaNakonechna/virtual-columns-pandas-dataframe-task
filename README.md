# Virtual Column in Pandas DataFrame

> *This project contains a function `add_virtual_column` that creates a new DataFrame with a calculated column based on a string expression.*

### How it works:
The function parses the `role` string to identify the operation (+, -, or *) and the columns involved. It then calculates the values for the `new_column` while keeping all original data.

### Key logic included:
- **Validation:** Uses regex to ensure all column labels (including the new one) consist only of letters and underscores.
- **Operations:** Supports basic math: addition, subtraction, and multiplication.
- **Error Handling:** If any column name is invalid, the operation isn't supported, or columns are missing, the function returns an empty DataFrame instead of crashing.
- **Data Stability:** Includes numeric conversion to ensure calculations work even if the source data is stored as strings.
