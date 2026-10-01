<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBGS - Budget Scenario
Module: Finance | 16 columns | ObjType: 91
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: Name, FinancYear
  INTER_KEY: BaseId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(100) Name
  BaseId Int(11) Basic Budget
  InitRate Num(19,6) Initial Ratio Percentage
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  FinancYear Date(8) Start of Fiscal Year
  IsMain VarChar(1) Main default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  RoundSys Int(6) Rounding Method default=0 [0=No Rounding, 1=Round to Full Decimal Amount, 2=Round to Full Amount, 3=Round to Full Tens Amount]
  UserSign Int(6) User Signature ->OUSR
  OcrCode nVarChar(8) Dimension 1 ->OOCR
  OcrCode2 nVarChar(8) Dimension 2 ->OOCR
  OcrCode3 nVarChar(8) Dimension 3 ->OOCR
  OcrCode4 nVarChar(8) Dimension 4 ->OOCR
  OcrCode5 nVarChar(8) Dimension 5 ->OOCR
  PrjCode nVarChar(20) Project Code ->OPRJ
