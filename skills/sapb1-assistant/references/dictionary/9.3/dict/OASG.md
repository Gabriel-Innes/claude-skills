<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OASG - Account Segmentation
Module: Finance | 5 columns | ObjType: 142
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(6) Numerator
  Name nVarChar(100) Name
  Size Int(6) Size
  Type VarChar(1) Type default=A [A=Alphanumeric, N=Numeric]
  UserSign Int(6) User Signature ->OUSR
