<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSHS - User-Defined Values
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndexID
  DETAILS U: ColID, ItemID, FormID
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  ItemID nVarChar(52) Field
  ColID nVarChar(20) Column ID default=-1
  ActionT Int(6) Action default=0 [0=, 1=Valid Values, 2=Query]
  QueryId Int(11) Query ID ->OUQR
  IndexID Int(11) Index
  Refresh VarChar(1) Refresh default=N [Y=Yes, N=No]
  FieldID nVarChar(60) Field
  FrceRfrsh VarChar(1) Force Refresh default=N [Y=Yes, N=No]
  ByField VarChar(1) By Field default=N [Y=When Field Changes, N=When Exiting Altered Column, C=When Column Value Changes]
