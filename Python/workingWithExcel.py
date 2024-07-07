import pandas as pd


def inputFile():
    excelPath = 'Input.xlsx'
    df = pd.read_excel(excelPath, sheet_name='Students')

    df['Dob'] = df['Dob'].dt.strftime('%d-%m-%Y')
    return df


