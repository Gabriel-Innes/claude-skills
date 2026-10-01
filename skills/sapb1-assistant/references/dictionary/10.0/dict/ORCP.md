<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ORCP - Recurring Transaction Template
Module: Marketing Documents | 20 columns | ObjType: 540000040
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(8) Template Code
  Dscription nVarChar(50) Description
  IsRemoved VarChar(1) Is Removed default=N [Y=Yes, N=No]
  DocObjType nVarChar(20) Linked Document Type default=-1 [-1=, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Returns Request, 16=Return, -203=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, -13=A/R Reserve Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Returns Request, 21=Goods Return, -204=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, -18=A/P Reserve Invoice, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer]
  DraftEntry Int(11) Linked Draft Entry ->ODRF
  Frequency VarChar(1) Frequency default=M [D=Daily, W=Weekly, X=Every 2 Weeks, M=Monthly, P=Every 2 Months, Q=Quarterly, S=Semiannually, A=Annually, O=One Time]
  Remind Int(6) Sub-Frequency default=1001 [-1=, 1=On Sunday, 2=On Monday, 3=On Tuesday, 4=On Wednesday, 5=On Thursday, 6=On Friday, 7=On Saturday, 101=Every 1, 102=Every 2, 103=Every 3, 104=Every 4, 105=Every 5, 106=Every 6, 107=Every 7, 108=Every 8, 109=Every 9, 110=Every 10, 111=Every 11, 112=Every 12, 113=Every 13, 114=Every 14, 115=Every 15, 116=Every 16, 117=Every 17, 118=Every 18, 119=Every 19, 120=Every 20, 121=Every 21, 122=Every 22, 123=Every 23, 124=Every 24, 125=Every 25, 126=Every 26, 127=Every 27, 128=Every 28, 129=Every 29, 130=Every 30, 131=Every 31, 145=Every 45, 160=Every 60, 1001=On 1, 1002=On 2, 1003=On 3, 1004=On 4, 1005=On 5, 1006=On 6, 1007=On 7, 1008=On 8, 1009=On 9, 1010=On 10, 1011=On 11, 1012=On 12, 1013=On 13, 1014=On 14, 1015=On 15, 1016=On 16, 1017=On 17, 1018=On 18, 1019=On 19, 1020=On 20, 1021=On 21, 1022=On 22, 1023=On 23, 1024=On 24, 1025=On 25, 1026=On 26, 1027=On 27, 1028=On 28, 1029=On 29, 1030=On 30, 1031=On 31]
  StartDate Date(8) Execution Start Date
  EndDate Date(8) Execution End Date
  LogInstanc Int(11) Log Instance default=0
  CreateUser Int(6) Created by User ->OUSR
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  UpdateUser nVarChar(6) Updated by User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  PriceUpdat VarChar(1) Prices Update default=N [Y=Yes, N=No]
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
