import xlwings as xw
import pandas as pd

### Create list of cost centers for loop, to be replaced with readxl 
### Saveas will fail if the filename is too long, need to shorten filename / path 

costCenters = [
'Aerospace Studies', 
'Africana Studies', 
'American Studies', 
'Anthropology', 
'Art & Art History', 
'Biology', 
'Center for the Humanities', 
'Chemistry', 
'Classics', 
'Composition Program', 
'Computer Science', 
"College of Arts and Sciences - Dean's Office", 
'Ecosystem Science and Policies', 
'English', 
'Geography', 
'Geological Sciences', 
'History', 
'College of Arts and Sciences - International Studies', 
'Judaic Studies', 
'Latin American Studies', 
'Lowe Art Museum', 
'Masters of Arts in  International Administration', 
'Program in International Studies', 
'Masters of Arts in Liberal Studies', 
'Mathematics', 
'Modern Languages & Literatures', 
'Neuroscience', 
'College of Arts and Sciences - Strategic Initiatives', 
'Philosophy', 
'Physics', 
'Political Science', 
'Psychology', 
'Religious Studies', 
'Sociology', 
'Theatre Arts', 
'Women & Gender Studies', 
'College of Arts and Sciences - Information Technology', 
'College of Arts and Sciences - Office of Communications and Marketing', 
'College of Arts and Sciences - Research Support Services', 
##'College of Arts and Sciences - Office of Enrollment Management and Graduate Student Services', 
'College of Arts and Sciences - Office of Academic Advising', 
'Advanced Program For Integrated Science And Math (PRISM)', 
'Miami Institute For The Americas', 
'Online Bachelors General Studies (BGS)', 
'Online Masters in Public Adminstration (MPA)', 
'Interdisciplinary Administration', 
'Creative Writing Program', 
'Social Sciences Operations', 
'Global Health Studies', 
'Directed Independent Language Study (DILS)', 
'College of Arts and Sciences - Fiscal Affairs and Facilities', 
'Hemispheric and Global Affairs', 
'Psychology - SCCC Sponsored Programs', 
'Writing Studies']

## Create list of sheets with data that needs to be split out.  Should be one column that contains information of 
sheetList = [
['GeneralFund','A3:A4000'],
['DesignatedFund','A3:A7000'],
['SponsoredFund','A3:A4100'],
['Endowments','A3:A1100']
]

folder = r'C:\Users\kxs1147\Box\CAS-BOT FILES\BUDGET AND PLANNING\FY2024 BUDGET\DEPT BUDGETS\File Prep'
filename = 'WIP FY2024 Budget Request Master Worksheet 20211101 NO MACRO - Copy'


for i in costCenters:
    app = xw.App(visible=False)
    ## Open Master Workbook
    wb = xw.Book(folder+'\\'+filename+'.xlsx')
    ## Save File with cost center name
    costCenter = i
    
    
    for j in range(0, len(sheetList)):
    
        sheet = wb.sheets[sheetList[j][0]]
        rng = sheet.range(sheetList[j][1])
        delRng = ''.join(c if not(c.isalpha()) else '' for c in sheetList[j][1])
				
        exec(f'sheet.used_range.api.AutoFilter(Field:=1, Criteria1 = "<>{costCenter}")')
        wb.sheets[sheetList[j][0]].range(delRng).delete()       
        wb.sheets[sheetList[j][0]].api.AutoFilter.ShowAllData()
        
        sheet.api.Protect(Password:="cas", DrawingObjects:=True, Contents:=True, Scenarios:=True, 
        UserInterfaceOnly:=True, AllowFormattingCells:=False, AllowFormattingColumns:=True, 
        AllowFormattingRows:=True, AllowInsertingColumns:=False, AllowInsertingRows:=False, 
        AllowInsertingHyperlinks:=False, AllowDeletingColumns:=False, AllowDeletingRows:=False, 
        AllowSorting:=False, AllowFiltering:=True, AllowUsingPivotTables:=True)
    
    wb.save(folder+'\\'+filename+' - '+ i +'.xlsx')
    wb.app.kill()

