<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WTM2 - Confirmation Templates - Stages
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WstCode, WtmCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  WstCode Int(11) Stage ->OWST
  SortId Int(6) Sort Code default=1
  Remarks nVarChar(100) Description
