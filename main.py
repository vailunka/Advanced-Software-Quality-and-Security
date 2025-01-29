import pandas as pd

def excel_to_csv(excel_file, sheet_name=0, exclude_columns=None, output_csv="output.csv"):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    #print("Columns in Excel: ", df.columns.tolist())
    df.columns = df.columns.str.strip()

    # Exclude specified columns if specified
    if exclude_columns:
        df = df.drop(columns=exclude_columns, errors="ignore")

    df.to_csv(output_csv, index=False)
    print(f"CSV file saved as {output_csv}")

if __name__ == "__main__":
    excel_to_csv("Scenarios.xlsx", sheet_name=0, output_csv="scenarios.csv")
    #excel_to_csv("Scenarios.xlsx", sheet_name=0, exclude_columns=["User"], output_csv="scenarios.csv")

