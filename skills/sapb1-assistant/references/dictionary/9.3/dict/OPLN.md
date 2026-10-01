<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPLN - Price Lists
Module: Inventory and Production | 24 columns | ObjType: 6
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ListNum
  LIST_NAME U: ListName
Fields (name type(len) description [values] ->parent table):
  ListNum Int(6) Price List No.
  ListName nVarChar(32) Price List Name
  BASE_NUM Int(6) Base Price List ->OPLN
  Factor Num(19,6) Factor
  RoundSys Int(6) Rounding Method default=0 [0=No Rounding, 1=Round to Full Decimal Amount, 2=Round to Full Amount, 3=Round to Full Tens Amount, 4=Fixed Ending, 5=Fixed Interval]
  GroupCode Int(6) Group No. default=1 [1=Group 1, 2=Group 2, 3=Group 3, 4=Group 4]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SPPCounter Int(11) SPP Counter
  UserSign Int(6) User Signature ->OUSR
  IsGrossPrc VarChar(1) Gross Price? default=N [Y=Gross, N=Net]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
  CreateDate Date(8) Creation Date
  PrimCurr nVarChar(3) Primary Default Currency
  AddCurr1 nVarChar(3) Additional Default Currency 1
  AddCurr2 nVarChar(3) Additional Default Currency 2
  RoundRule VarChar(1) Rounding Rule default=R [R=Round to Closest, C=Round Up, F=Round Down]
  ExtAmount Num(19,6) Fixed Amount (Ending/Interval)
  RndFrmtInt nVarChar(10) Ending/Interval - Integer Part
  RndFrmtDec nVarChar(10) Ending/Interval - Decimal Part
