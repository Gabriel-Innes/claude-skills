<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XRREL - XLR Company Report Objects
Module: Reports | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, ChildId, ParentId
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(38) ParentId
  ChildId nVarChar(38) ChildId
  RelType Int(11) RelType default=1
  SeqNo Int(11) SeqNo default=0
  Global Int(11) Global default=0
