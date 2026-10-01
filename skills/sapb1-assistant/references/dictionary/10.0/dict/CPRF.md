<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CPRF - Column Preferences
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, FormID, ItemID, ColID, TPLId
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  ItemID nVarChar(50) Item Number
  ColID nVarChar(60) Column
  Width Int(11) Width
  VisInForm VarChar(1) Visible in Form default=N [Y=Yes, N=No]
  VisualIndx Int(11) Tabs Layout
  EditInForm VarChar(1) Editable in Form default=N [Y=Yes, N=No]
  VisInExpnd VarChar(1) Visible in Expanded default=N [Y=Yes, N=No]
  ExpandIndx Int(11) Expanded Index
  EditInEXP VarChar(1) Editable in Expanded default=N [Y=Yes, N=No]
  Folded VarChar(1) Folder default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ExtDisable VarChar(1) Externally Disabled default=N [N=No, Y=Yes]
  ExtInvsbl VarChar(1) Externally Invisible default=N [N=No, Y=Yes]
  TPLId Int(6) Template ID default=0 ->UICU
  TableName nVarChar(20) Table Name
  ItemUID nVarChar(32) ItemUID
