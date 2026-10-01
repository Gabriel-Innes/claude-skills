<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OOST - Opportunity Stage
Module: Sales Opportunities | 8 columns | ObjType: 101
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
  STEP U: StepId
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Name
  StepId Int(6) Stage No.
  CloPrcnt Num(19,6) Closing Percentage
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  SalesStage VarChar(1) Sales default=Y [Y=Yes, N=No]
  PurStage VarChar(1) Purchasing default=Y [Y=Yes, N=No]
