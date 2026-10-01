<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBST - BoE Stamp Tax
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  AMOUNT U: Amount
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Amount Num(19,6) BoE Amount
  StampTax Num(19,6) BoE Stamp Tax
