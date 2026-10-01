<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TYPR - TYPR
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, Local, CODE
  TYPE: CODE
Fields (name type(len) description [values] ->parent table):
  CODE nVarChar(4) Report Type
  NAME nVarChar(250) Type Name
  DEFLT_REP nVarChar(8) Standard Report
  Local nVarChar(2) Localization
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
