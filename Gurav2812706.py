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
    expr = re.compile('([\d{2}]+:[\d{2}]+[pmPM]*?[\s]*?-[\s]*?[\d{2}]+:[\d{2}]+[pmPM][pmPM])')
    parseData(log_file_path, expr)

def parseData(log_file_path, expr, read_line=True, reparse=False):
    skip_chars = [' ']
    totalTime=0
    found = False
    
    with open(log_file_path, "r") as file:
        if read_line == True:
            for line in file:
                if line.strip() == "Time Log:":
                    found = True
                if found == True:
                    match = expr.search(line, re.IGNORECASE)
                    if match:
                        lst_time = []
                        timeSlots=''.join(i for i in match.group(1) if not i in skip_chars)
                        finalTimes=timeSlots.split('-');
                        lst_time.append(finalTimes[0].strip())
                        lst_time.append(finalTimes[1].strip())

                        st_time = lst_time[0].replace('pm',"").replace('p',"").replace('a',"").replace('m',"").replace('PM',"").replace('AM',"")
                        stp_time = lst_time[1].replace('pm',"").replace('p',"").replace('a',"").replace('m',"").replace('PM',"").replace('AM',"")

                        SsplitM = (st_time.split(":")) 
                        EsplitM = (stp_time.split(":"))                                         
                                    

                        #get the difference between the start and end times
                        deltaMins = int(EsplitM[1])-int(SsplitM[1])                             
                        deltaHrs = int(EsplitM[0])-int(SsplitM[0])
                        if deltaHrs < 0 and deltaMins < 0:
                            deltaHrs = deltaHrs + 11
                            totalMinM = deltaMins  + 60
                        elif deltaHrs < 0 and deltaMins == 0:
                            deltaHrs = deltaHrs + 12
                        elif deltaHrs > 0 and deltaMins < 0:
                            deltaHrs = deltaHrs - 1
                            totalMinM = deltaMins + 60
                        elif deltaHrs < 0 and deltaMins > 0:
                            deltaHrs = deltaHrs + 12
                        
                        #keep adding hours and minues to totalHrs, totalMins
                        totalTime += (deltaHrs * 3600) + (deltaMins * 60)
                else:
                    print(f'File cannot be parsed')
                 
    #calculate total log time by computing on hours and minutes from totalTime
    minutes, seconds = divmod(totalTime, 60)
    hours, minutes = divmod(minutes, 60)
    print(f'{str(hours)} Hours  {str(minutes)}  Minutes')
    file.close()
    
if __name__ == '__main__':
    import sys
    #main(sys.argv[1]) 
    main("TimeLogEnergy.txt") 