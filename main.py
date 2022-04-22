import pandas as pd


excel_workbook = 'FT DS Learner Tracker.xlsx'

sheet1 = pd.read_excel(excel_workbook, sheet_name='sheet1')
print(sheet1.head(10))

fake_name_list = []
surname_list = []

excel_names = sheet1['Fake_Name, Surname']
print(excel_names)

for name in excel_names:
    Fake_Name, Surname = name.split(' ',1)
    fake_name_list.append(Fake_Name)
    surname_list.append(Surname)
print(fake_name_list)

sheet1.insert(0, 'Fake_Name', fake_name_list)
sheet1.insert(1,'Surname', surname_list)

del sheet1['Fake_Name, Surname']
print(sheet1.head(10))


















