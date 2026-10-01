<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOST - Opportunity Stage
Module: Sales Opportunities | 8 columns | ObjType: 101
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
