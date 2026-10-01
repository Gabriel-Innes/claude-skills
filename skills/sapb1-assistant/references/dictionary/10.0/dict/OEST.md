<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEST - EWB Sub-Type
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SUB_TYPE U: SubID
  SUPLY_TYPE: SuplyType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SubID Int(11) EWB Sub-Type Code
  SubType nVarChar(50) Sub supply type of e-way bill
  SuplyType VarChar(1) EWB Supply Type default=B [B=Both, I=Inward, O=Outward]
