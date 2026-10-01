<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODOR - Doubtful Debts
Module: Sales Opportunities | 3 columns | ObjType: 185
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NUMOFDAYS U: NumOfDays
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NumOfDays Int(11) No. of Days
  Percentage Num(19,6) Doubtful Debt %
