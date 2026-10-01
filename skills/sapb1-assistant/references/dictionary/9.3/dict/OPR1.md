<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPR1 - Opportunity - Rows
Module: Sales Opportunities | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, OpprId
Fields (name type(len) description [values] ->parent table):
  OpprId Int(11) Sequence No. ->OOPR
  Line Int(6) Row No.
  SlpCode Int(11) Sales Employee ->OSLP
  CntctCode Int(11) Contact Person ->OCPR
  OpenDate Date(8) Start Date
  CloseDate Date(8) Closing Date
  Step_Id Int(11) Stage Key ->OOST
  ClosePrcnt Num(19,6) Percentage Rate
  MaxSumLoc Num(19,6) Max. Local Total
  MaxSumSys Num(19,6) Max. System Total
  Memo Text(16) Remarks
  DocId Int(11) Object Code
  ObjType nVarChar(9) Object Type default=-1 [-1=, 0=, 23=Sales Quotations, 17=Sales Orders, 15=Delivery Notes, 13=Sales Invoices, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=Purchase Invoices]
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Linked VarChar(1) Activity default=N [Y=Yes, N=No]
  WtSumLoc Num(19,6) Weighted Amount (LC) - Rows
  WtSumSys Num(19,6) Weighted Amount (SC)
  UserSign Int(6) User Signature ->OUSR
  ChnCrdCode nVarChar(15) BP Channel Code ->OCRD
  ChnCrdName nVarChar(100) BP Channel Name
  ChnCrdCon Int(11) BP Channel Contact ->OCPR
  DocChkbox VarChar(1) Document Checkbox [Y=Yes, N=No]
  Owner Int(11) Data Ownership Field ->OHEM
  DocNumber Int(11) Document Number
