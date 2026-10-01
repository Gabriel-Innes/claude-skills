<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBST - BoE Stamp Tax
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  AMOUNT U: Amount
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Amount Num(19,6) BoE Amount
  StampTax Num(19,6) BoE Stamp Tax
