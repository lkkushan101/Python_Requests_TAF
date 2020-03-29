import openpyxl


def readExcel(file, sheet_name, coloumn_row):
    book = openpyxl.load_workbook(file)
    sheet = book.get_sheet_by_name(sheet_name)
    data = sheet[coloumn_row]
    return  data.value