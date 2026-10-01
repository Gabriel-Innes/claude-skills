<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
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
  GroupCode Int(6) Group No. default=1 [1=Price List - Group No. 1, 2=Price List - Group No. 2, 3=Price List - Group No. 3, 4=Price List - Group No. 4, 5=Price List - Group No. 5, 6=Price List - Group No. 6, 7=Price List - Group No. 7, 8=Price List - Group No. 8, 9=Price List - Group No. 9, 10=Price List - Group No. 10, 11=Price List - Group No. 11, 12=Price List - Group No. 12, 13=Price List - Group No. 13, 14=Price List - Group No. 14, 15=Price List - Group No. 15, 16=Price List - Group No. 16, 17=Price List - Group No. 17, 18=Price List - Group No. 18, 19=Price List - Group No. 19, 20=Price List - Group No. 20, 21=Price List - Group No. 21, 22=Price List - Group No. 22, 23=Price List - Group No. 23, 24=Price List - Group No. 24, 25=Price List - Group No. 25, 26=Price List - Group No. 26, 27=Price List - Group No. 27, 28=Price List - Group No. 28, 29=Price List - Group No. 29, 30=Price List - Group No. 30]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
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
