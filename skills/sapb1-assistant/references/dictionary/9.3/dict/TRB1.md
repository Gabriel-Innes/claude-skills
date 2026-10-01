<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRB1 - Tax Report Wizard Selected States
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: State, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  State nVarChar(3) State Code ->OCST
