<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# STRL - String List resource
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RevCode, ResCode, Name
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) STRL name
  Num Int(11) STRL number
  MaxUnique Int(11) Max Unique
  RobjCode Int(11) Imp Exp Obj Code default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
