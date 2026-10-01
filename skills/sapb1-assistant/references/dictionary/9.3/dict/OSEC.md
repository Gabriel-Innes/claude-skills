<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSEC - Sections
Module: Administration | 4 columns | ObjType: 10000074
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  CODE U: Code
  ECODE U: eCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(15) Code
  Descr nVarChar(30) Description
  eCode nVarChar(3) eCode
