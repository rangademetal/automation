import json
from openpyxl import load_workbook

from config_class.excel_class import Excel
from config_class.data_encode import DateTimeEncoder
from config_class.database import Database



datatime_encoder = DateTimeEncoder()
excel = Excel('sampledatainsurance.xlsx')
database = Database('localhost', 'root', 'Sad1996.', 'insurance')

connection = database.connection()
print(connection)

field = database.get_column(connection=connection, table_name='insurance_main')
print(field)
print(database.set_values(len(field)))



# workbook = excel.open_file()
# sheet = excel.select_sheet(workbook=workbook, sheet='PolicyData')

# max_row = excel.get_max_row(sheet=sheet)
# max_col = excel.get_max_col(sheet=sheet)

# header = excel.get_headers(sheet, 1, max_col)
# datas = excel.get_data(sheet=sheet, row=max_row, column=max_col)

# dictionary_data = excel.dictionary_data(header=header, data=datas, counter=10)


# with open('extract.json', 'w') as wfile:
#     json.dump(dictionary_data, wfile, cls=DateTimeEncoder)

# with open('extract.json') as rfile:
#     data = json.load(rfile)
