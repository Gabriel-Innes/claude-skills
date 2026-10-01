<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPR3 - Opportunity - Competitors
Module: Sales Opportunities | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, OpportId
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  CompetId Int(11) Competitors ->OCMT
  Memo nVarChar(50) Details
  Won VarChar(1) Won or Lost default=N [Y=Yes, N=No]
  ThreatLevl Int(6) Threat Level [1=Low, 2=Medium, 3=High]
