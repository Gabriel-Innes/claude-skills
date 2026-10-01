<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACK - Acknowledge Number
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  LOC_QUART U: Location, Quarter, FinYear
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  FinYear Int(11) Financial Year ->OFYM
  Quarter VarChar(1) Quarter [1=Quarter 1, 2=Quarter 2, 3=Quarter 3, 4=Quarter 4]
  AckNum nVarChar(100) Acknowledgment No.
  Location Int(11) Location ->OLCT
