<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MLS1 - Distribution Lists - Recipients
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->OMLS
  LineNum Int(11) Addressee Number
  ObjType nVarChar(20) Object
  ObjCode nVarChar(50) Object Code
  ObjName nVarChar(155) Name
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  Fax nVarChar(50) Fax Number
