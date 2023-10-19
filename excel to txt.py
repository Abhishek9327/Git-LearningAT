import pandas as pd

excel_path = 'EXCEL_TIPS.xls'
df = pd.read_excel(excel_path)
txtfile = "txtfile.txt"
df.to_csv(txtfile, sep='\t', index=False)
print(f'Data has been transferred from Excel to {txtfile}')

