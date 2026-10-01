<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTGG - Target Group
Module: Business Partners | 3 columns | ObjType: 1320000002
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TargetCode
Fields (name type(len) description [values] ->parent table):
  TargetCode nVarChar(20) Target Group Code
  TargetName nVarChar(100) Target Group Name
  TargetType VarChar(1) Target Group Type default=C [C=Customer, S=Vendor]
