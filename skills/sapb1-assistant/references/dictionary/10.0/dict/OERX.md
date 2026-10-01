<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OERX - Excise Register Numbering Ext
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ErnId
  LOC_KEY U: Location
Fields (name type(len) description [values] ->parent table):
  ErnId Int(11) Excise Register Numbering ID
  Location Int(11) Loc. ->OLCT
  UserSign Int(6) User Signature ->OUSR
