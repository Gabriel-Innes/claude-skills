<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UIC2 - Customized Forms in Template
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, FormId, ItemId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  ItemId nVarChar(70) Item ID
  Visible VarChar(1) Visible
  VisibleCtl VarChar(1) Visible Control
  Editable VarChar(1) Editable
  EditbleCtl VarChar(1) Editable Control
  Left Int(6) Left
  Top Int(6) Top
  Right Int(6) Right
  Bottom Int(6) Bottom
  FromPane Int(6) From Pane
  ToPane Int(6) To Pane
  UDF VarChar(1) UDF default=N
  TableName nVarChar(20) TableName
