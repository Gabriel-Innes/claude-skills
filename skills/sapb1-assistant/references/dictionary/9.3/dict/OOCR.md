<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOCR - Distribution Rule
Module: Sales Opportunities | 14 columns | ObjType: 62
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code
  OcrName nVarChar(30) Factor Description
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  AbsEntry Int(11) Numerator
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  IsFixedAmt VarChar(1) Distribute by Fixed Amount default=N [Y=Yes, N=No]
