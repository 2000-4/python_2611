from openpyxl import *
from openpyxl.styles import PatternFill

# == 셀 배경 색 바꾸기 ==
wb = Workbook()
ws = wb.active

# 헤더
ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'
ws['D1'] = '사회'
ws['E1'] = '과학'

color = PatternFill(fill_type='solid', fgColor='b2e018')

# 반복문을 통해 셀의 배경색 바꾸기
for cell in ws[1]: # 1행 전체
    cell.fill = color

wb.save('bg_color.xlsx')