import xlsxwriter
from parser import get_data
from userdata import FILENAME


def write_ex(func):
    book = xlsxwriter.Workbook(FILENAME)
    page = book.add_worksheet('Goods')

    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 12)
    page.set_column('C:C', 70)
    page.set_column('D:D', 50)

    for item in func():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()

write_ex(get_data)
