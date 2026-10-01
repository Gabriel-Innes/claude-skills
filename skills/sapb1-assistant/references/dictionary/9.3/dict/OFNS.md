<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFNS - Folio Numbering - Series
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Series
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Series Int(11) Series ID
  Name nVarChar(100) Name
  PTICode nVarChar(5) POI Code ->OPTI
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number
  Letter VarChar(1) Letter [A=A, B=B, C=C, E=E, M=M, R=R]
  CAI nVarChar(14) CAI
  CAIDueDate Date(8) CAI Due Date
  Remarks nVarChar(100) Remarks
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
