<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MLS1 - Distribution Lists - Recipients
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->OMLS
  LineNum Int(11) Addressee Number
  ObjType nVarChar(20) Object
  ObjCode nVarChar(50) Object Code
  ObjName nVarChar(155) Name
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  Fax nVarChar(20) Fax Number
