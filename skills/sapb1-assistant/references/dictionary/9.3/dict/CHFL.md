<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CHFL - Choose from List Format
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FldIndex, ObjName
Fields (name type(len) description [values] ->parent table):
  ObjName nVarChar(20) Object Name
  FldIndex Int(6) Field Index
  FldNum nVarChar(60) Field No.
  DispName nVarChar(30) Displayed Name
  GroupBy VarChar(1) Group By default=N [Y=Yes, N=No]
  Visible VarChar(1) Visible default=N [Y=Yes, N=No]
  DispDesc VarChar(1) Show Type default=Y [Y=Yes, N=No]
  SortOrder VarChar(1) Sort Order default=A [A=Ascending, D=Descending]
  VisIndex Int(6) Visual Index default=0
