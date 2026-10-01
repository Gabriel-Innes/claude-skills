<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# STRI - String list item resource
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RevCode, ResCode, Num, Name
  UNIQUE_ID U: UniqueID, Name
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) STRL name
  Num Int(11) String number
  StrIndex Int(11) String Index default=0
  ItemString nVarChar(254) Item string
  UniqueID nVarChar(10) Unique ID
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
