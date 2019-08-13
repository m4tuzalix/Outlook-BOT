import xlrd
import os
import glob
from database import total_score, del_repeated
from tkinter import messagebox


class Cleaner:
        def clearing_db_from_resolved(path):
        
                files_path = os.path.join(path, '*') ##// path join to all files in provided dir
                files = sorted(glob.iglob(files_path), key=os.path.getctime) ##// sorting files by date of creatin
                try:
                        wb = xlrd.open_workbook(files[-1])
                        sheet = wb.sheet_by_index(0)
                        sheet.cell_value(0,0)
                        raw_data = []
                        clean_data = []
                        for x in range(sheet.nrows):
                                for y in range(sheet.ncols):
                                        cell = sheet.cell_value(x,y)
                                        if cell != "":
                                                raw_data.append(str(cell))
                        for item in raw_data:
                                if item[:3] == "INC":
                                        clean_data.append(item)

                        for rows in total_score(): #/// looping thru db records and excel cells. If match, then delete in db
                                for item in clean_data:
                                        if rows[2] == item:
                                                del_repeated(rows[2])
                except IndexError:
                      messagebox.showerror("WRONG PATH","No excel files found")  

                


        


    
    
     
    
        
