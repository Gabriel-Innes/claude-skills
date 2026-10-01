<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODUT - Dunning Terms
Module: Marketing Documents | 20 columns | ObjType: 196
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TermCode
Fields (name type(len) description [values] ->parent table):
  TermCode nVarChar(25) Dunning Term Code
  TermName nVarChar(100) Dunning Term Name
  GrpMethod VarChar(1) Grouping Method default=B [I=One Letter per Invoice, L=One Letter per Dunning Level, B=One Letter per BP]
  YearDays Int(6) Days in Year default=360
  MonthDays Int(6) Days in Month default=30
  RemIntrst VarChar(1) Calc. Interest Rem/Orig Sum default=Y [Y=Yes, N=No]
  XchgOrig VarChar(1) Exchange Rate Orig/Current default=Y [Y=Yes, N=No]
  YearlyRate Num(19,6) Yearly Interest Rate
  MaxLevel Int(6) Max Dunning Level default=0
  TotalFee Num(19,6) All Total Fee
  FeeCurr nVarChar(3) All Fee Currency
  MinBalance Num(19,6) All Min. Balance
  BalCurr nVarChar(3) All Balance Currency
  CalcIntr VarChar(1) All Calc. Interest default=Y [Y=Yes, N=No]
  LetterFrmt nVarChar(8) All Letter Format
  HiLtrFrmt VarChar(1) Apply Highest Letter Template default=N [Y=Yes, N=No]
  DateCalInt VarChar(1) Base Date for Interest Calc. default=Y [Y=From Due Date, N=From Last Dunning Run]
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  IntrAcc nVarChar(15) Interest Account ->OACT
  FeeAcc nVarChar(15) Fee Account ->OACT
