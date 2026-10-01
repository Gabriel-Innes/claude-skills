<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOND - Industries
Module: Sales Opportunities | 3 columns | ObjType: 201
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IndCode
  IND_NAME U: IndName
Fields (name type(len) description [values] ->parent table):
  IndCode Int(11) Industry Code
  IndName nVarChar(15) Industry Name
  IndDesc nVarChar(30) Industry Description
