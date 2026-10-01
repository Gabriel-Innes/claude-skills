<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OHLD - Holiday Table
Module: Human Resources | 6 columns | ObjType: 186
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HldCode
Fields (name type(len) description [values] ->parent table):
  HldCode nVarChar(20) Holidays Name
  WndFrm VarChar(1) Weekend From default=6 [1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  WndTo VarChar(1) To default=1 [1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  isCurYear VarChar(1) Current Year default=Y [Y=Yes, N=No]
  ignrWnd VarChar(1) Ignore Weekend default=N
  WeekNoRule VarChar(1) Rule to Calculate Week Number default=J [J=First week starts on January 1, D=First week starts in first 4-day week, F=First week starts in first full week]
