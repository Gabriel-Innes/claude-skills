<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTRX - Transformation Documents
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(250) Description
  Type nVarChar(8) Type default=XSLT [XSLT=XSLT Document]
  Data Text(16) Data
