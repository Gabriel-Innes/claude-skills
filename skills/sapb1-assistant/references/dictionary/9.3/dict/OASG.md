<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OASG - Account Segmentation
Module: Finance | 5 columns | ObjType: 142
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(6) Numerator
  Name nVarChar(100) Name
  Size Int(6) Size
  Type VarChar(1) Type default=A [A=Alphanumeric, N=Numeric]
  UserSign Int(6) User Signature ->OUSR
