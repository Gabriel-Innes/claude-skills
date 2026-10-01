<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CASE - Internal Recon. Upgrade 2007A
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Intl ID for Inconsistent Amt
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  UserSign Int(6) User Signature ->OUSR
  Message VarChar(1) Show Message? default=N [Y=, N=, S=]
