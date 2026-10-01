<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPR5 - Opportunity - Reasons
Module: Sales Opportunities | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, OpportId
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ReasondId Int(11) Reason ->OOFR
