<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TYPR - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CODE, Local, ResCode, RevCode
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
