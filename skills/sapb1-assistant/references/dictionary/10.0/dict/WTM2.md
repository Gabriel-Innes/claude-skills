<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTM2 - Confirmation Templates - Stages
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, WstCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  WstCode Int(11) Stage ->OWST
  SortId Int(6) Sort Code default=1
  Remarks nVarChar(100) Description
