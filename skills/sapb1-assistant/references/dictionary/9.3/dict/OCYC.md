<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCYC - Cycle
Module: Inventory and Production | 24 columns | ObjType: 146
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Cycle Code
  Name nVarChar(20) Cycle Name
  Frequency VarChar(1) Frequency [0=Daily, 1=Weekly, 2=Every Four Weeks, 3=Monthly, 4=Quarterly, 5=Semiannually, 6=Annually, 7=None, 8=Every "X" Days:]
  Day Int(11) Day
  Hour Int(11) Hour
  UserSign Int(6) User Signature ->OUSR
  NextDate Date(8) Next Counting Date
  Type VarChar(1) Cycle Type default=C [C=Cycle, M=MRP]
  SubOption VarChar(1) Suboption default=1 [1=Option 1, 2=Option 2]
  Interval Int(11) Interval default=1
  EndType VarChar(1) Recurrence End Type default=N [N=No End Date, C=By Counter, D=By Date]
  MaxOccur Int(11) Max. Occurrences
  SeEndDat Date(8) Series End Date
  Sunday VarChar(1) Sunday default=N [N=No, Y=Yes]
  Monday VarChar(1) Monday default=N [N=No, Y=Yes]
  Tuesday VarChar(1) Tuesday default=N [N=No, Y=Yes]
  Wednesday VarChar(1) Wednesday default=N [N=No, Y=Yes]
  Thursday VarChar(1) Thursday default=N [N=No, Y=Yes]
  Friday VarChar(1) Friday default=N [N=No, Y=Yes]
  Saturday VarChar(1) Saturday default=N [N=No, Y=Yes]
  DayInMonth Int(11) Repeat Day in Month
  Week Int(11) Repeat Week in Month [1=First, 2=Second, 3=Third, 4=Fourth, 5=Last]
  DayOfWeek Int(11) Repeat Day of Week [8=Day, 9=Weekday, 0=Weekend Day, 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  Month Int(11) Repeat Month
