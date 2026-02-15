import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    try:
        pattern_labels = r'[a-zA-Z_]+'
        for column in df.columns:
            if not re.fullmatch(pattern_labels, column):
                return pandas.DataFrame([])

        if not re.fullmatch(pattern_labels, new_column):
            return pandas.DataFrame([])

        if '+' in role:
            roles_parts = role.split('+')
            if len(roles_parts) != 2:
                return pandas.DataFrame([])

            first_column_role = roles_parts[0].strip()
            second_column_role = roles_parts[1].strip()
            if not (re.fullmatch(pattern_labels, first_column_role) and re.fullmatch(pattern_labels, second_column_role)):
                return pandas.DataFrame([])

            if first_column_role in df.columns and second_column_role in df.columns:
                new_df = df.copy()
                new_df[new_column] = pandas.to_numeric(new_df[first_column_role]) + pandas.to_numeric(
                    new_df[second_column_role])
                return new_df
        elif '-' in role:
            roles_parts = role.split('-')
            if len(roles_parts) != 2:
                return pandas.DataFrame([])

            first_column_role = roles_parts[0].strip()
            second_column_role = roles_parts[1].strip()
            if not (re.fullmatch(pattern_labels, first_column_role) and re.fullmatch(pattern_labels, second_column_role)):
                return pandas.DataFrame([])

            if first_column_role in df.columns and second_column_role in df.columns:
                new_df = df.copy()
                new_df[new_column] = pandas.to_numeric(new_df[first_column_role]) - pandas.to_numeric(
                    new_df[second_column_role])
                return new_df
        elif '*' in role:
            roles_parts = role.split('*')
            if len(roles_parts) != 2:
                return pandas.DataFrame([])

            first_column_role = roles_parts[0].strip()
            second_column_role = roles_parts[1].strip()
            if not (re.fullmatch(pattern_labels, first_column_role) and re.fullmatch(pattern_labels, second_column_role)):
                return pandas.DataFrame([])

            if first_column_role in df.columns and second_column_role in df.columns:
                new_df = df.copy()
                new_df[new_column] = pandas.to_numeric(new_df[first_column_role]) * pandas.to_numeric(new_df[second_column_role])
                return new_df

        return pandas.DataFrame([])

    except Exception:
        return pandas.DataFrame([])