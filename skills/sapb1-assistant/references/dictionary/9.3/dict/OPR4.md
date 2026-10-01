<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPR4 - Opportunity - Interests
Module: Sales Opportunities | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, OprId
Fields (name type(len) description [values] ->parent table):
  OprId Int(11) Sequence No.
  Line Int(6) Row No.
  IntId Int(11) Interest ID ->OOIN
  Prmry VarChar(1) Primary Interest default=N [Y=Yes, N=No]
