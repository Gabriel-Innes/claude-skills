<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EFDW1 - EFD Wizard - Rows 1
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WhCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WhCode nVarChar(8) Warehouse Code ->OWHS
