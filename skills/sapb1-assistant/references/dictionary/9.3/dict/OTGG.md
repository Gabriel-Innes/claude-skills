<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTGG - Target Group
Module: Business Partners | 3 columns | ObjType: 1320000002
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TargetCode
Fields (name type(len) description [values] ->parent table):
  TargetCode nVarChar(20) Target Group Code
  TargetName nVarChar(100) Target Group Name
  TargetType VarChar(1) Target Group Type default=C [C=Customer, S=Vendor]
