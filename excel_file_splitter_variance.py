import xlwings as xw

### For use when data is stored in an excel table
### Create list of cost centers for loop, to be replaced with readxl of dynamic list.  Consider nested list with official name and short name 
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
'Writing Studies'
]

## Create list of sheets with data that needs to be split out.  Should be one column that contains information of 
sheetList = [
['DATA','A13:M16000']
]

## This must be updated to the table name on your Data sheet
tblName = 'Datatbl'

folder = r'C:\Users\kxs1147\Box\CAS-BOT FILES\BUDGET VARIANCES\FY23\Q2\File Prep'
filename = 'WIP FY2023 Q2 Master Variance File'

### When updating Field:=n must equal to index of column filtering on tblName, i.e. Column A is 1, Column M is 13

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
				
        exec(f'''sheet.range('{tblName}').api.AutoFilter(Field:=13, Criteria1:= "<>{costCenter}")''')
        wb.sheets[sheetList[j][0]].range(delRng).delete()       
        ##sheet.range(tblName).api.AutoFilter(Field:=13, Criteria1:= "*")
        exec(f'''sheet.range('{tblName}').api.AutoFilter(Field:=13, Criteria1:= "{costCenter}")''')
        sheet['A:C'].api.EntireColumn.Hidden = True
        wb.api.RefreshAll()
      
   
    wb.save(folder+'\\'+filename+' - '+ i +'.xlsx')
    wb.app.kill()

