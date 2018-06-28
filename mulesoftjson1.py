#!/usr/bin/env python
import re
import json
import csv
import StringIO



csv_rows = []
date_var = ""
#with open('D:\TEST_GoogleSheets\Attendance\Attendance.csv', "rb") as shakes, open('D:\TEST_GoogleSheets\Modified_CSV\emp_Attendance.json', 'w') as newfile:
def shakes_json():
    shakes = StringIO.StringIO(u""",,,,,zxv,,,,,,,
    ,,,,,,,,,,,,
    ,,,,,xzv,,,,,,,
    ,,,,,,,,,,,,
    ,,,,,,,,,,,,
    ***   REPORT NO. 19,,,,,DAILY In And Out REPORT,,Run Date :,16-Mar-18,,,,
    Lexicon Networks,,,,,,,Run Time :,12:54:31 PM,,,,
    ,,,,,,,,,,,,
    ID,,Name,,,In Time,Out Time,MinsWork,HrsWork,Status,,,
    Date :,,01-Mar-18,,,,,,,,,,
    1003,,Vishal  Dubey,,,,,,0,0,:,0,A
    ,,,,,,,,,,,,
    1010,,Muralidar  Remane,,,10:47 AM,07:16 PM,,509,8,:,29,P
    ,,,,,,,,,,,,
    1012,,Fexcy  Francis,,,09:12 AM,05:37 PM,,505,8,:,25,P
    ,,,,,,,,,,,,
    1013,,Sanket  Kulkarni,,,10:47 AM,06:19 PM,,452,7,:,32,P
    ,,,,,,,,,,,,
    1017,,Richa  Gohiley,,,,,,0,0,:,0,A""")
    for line in shakes:
        if re.match("|".join(["(.*)ID(.*)", "(.*)10(.*)", "Date :(.*)"]), line):
            if re.match("Date :(.*)", line):
                date_var = line[8:19]

            if re.match("|".join(["(.*)ID(.*)", "10(.*)"]), line):
                line = line.replace('ID', 'Emp_ID')
                line = line.replace('Status,', 'Status,Date')
                line = line.replace(',:,', ':')
                line = line.replace(',,', ',')
                line = line.replace(',,', ',')
                line = line.replace(',,', ',,,')
                line = line.replace(',,,', ',0,0,')
                if re.match("(.*)10(.*)", line):
                    line = line.rstrip('\n')+ date_var +'\n'
                    line = line.replace('\r', ',')
                line = line.replace('Date,', 'Date')
                line = line.replace('\r', '')
                json_line = StringIO.StringIO(line)
                reader = csv.DictReader( json_line, fieldnames = ( "Emp_ID","Name","In Time","Out Time","MinsWork","HrsWork","Status","Date" ))
                out = json.dumps( [ row for row in reader ])
                print out
try {shakes_json;
     return out;
     } catch(exception e)



            #reader = csv.DictReader(StringIO.StringIO(line))
            #out = json.dumps( [ row for row in reader ])
            #print out


            #reader_list = csv.DictReader(io.StringIO(unicode(line.splitlines())))
                #print reader_list.fieldnames
                ##################################
#                reader = csv.DictReader(f)
#                title = reader.fieldnames
#                for row in reader:
#                    csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
#
#                a = (json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '), encoding="utf-8",
#                                ensure_ascii=False))
#                result = a
                ##################################



                #newfile.write(line, )
