#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:52:42 2021

@author: atharvagurav
"""
from datetime import datetime
import re 

def main(log_file_path):
    # Open function to open the file "MyFile1.txt" 
    # (same directory) in append mode and
    expr = re.compile('([\d{2}]+:[\d{2}]+[pmPM]*?[\s]*?-[\s]*?[\d{2}]+:[\d{2}]+[pmPM])')
    parseData(log_file_path, expr)

def parseData(log_file_path, expr, read_line=True, reparse=False):
    found = False
    total_time = 0
    invalid_input = 'Lines having issues are -'
    cnt = 1
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                if line.strip() == "Time Log:":
                    found = True
                if found == True:
                    try:
                        match = expr.search(line, re.IGNORECASE)
                        if match:
                            lst_time = []
                            finalTimes=match.group(1).split('-');
                            lst_time.append(finalTimes[0].strip())
                            lst_time.append(finalTimes[1].strip())
    
                            st_time = lst_time[0].replace('P',"").replace('p',"").replace('a',"").replace('m',"").replace('A',"").replace('M',"")
                            stp_time = lst_time[1].replace('P',"").replace('p',"").replace('a',"").replace('m',"").replace('A',"").replace('M',"")
    
    
                            SsplitM = (st_time.split(":")) 
                            EsplitM = (stp_time.split(":"))                                         
    
                            totalMinM = int(EsplitM[1])-int(SsplitM[1])                          
                            totalHrsM = int(EsplitM[0])-int(SsplitM[0])
                            if totalHrsM < 0 and totalMinM < 0:
                                totalHrsM = totalHrsM + 11
                                totalMinM = totalMinM  + 60
                            elif totalHrsM < 0 and totalMinM == 0:
                                totalHrsM = totalHrsM + 12
                            elif totalHrsM > 0 and totalMinM < 0:
                                totalHrsM = totalHrsM - 1
                                totalMinM = totalMinM + 60
                            elif totalHrsM < 0 and totalMinM > 0:
                                totalHrsM = totalHrsM + 12
    
                            total_time += (totalHrsM *3600) + (totalMinM *60)                        
                        else:
                            continue
                    except:
                        error = True
                        invalid_input = f'{invalid_input}, {cnt}'
                else: 
                    invalid_input = f'{invalid_input}, {cnt}'
                    break
                cnt += 1

    if found == False:
        print(f'{invalid_input}')
    elif found == True:
        minutes, seconds = divmod(total_time, 60)
        hours, minutes = divmod(minutes, 60)
        invalid_input = f'{invalid_input} none'
        print(f'{str(hours)} Hours  {str(minutes)}  Minutes, {invalid_input}')
    
    file.close()
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1]) 