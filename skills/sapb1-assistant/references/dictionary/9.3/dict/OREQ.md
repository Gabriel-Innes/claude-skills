<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OREQ - External System Call Request
Module: Service | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID
  Category Int(11) Request Category
  Status VarChar(1) Request Status default=N [N=New, P=In Process, S=Completed, C=Comfirmed, F=Failed]
  CreateDate Date(8) Request Creation Date
  CreateTime Int(11) Request Creation Time
  LstUpdDate Date(8) Latest Update Date
  LstUpdTime Int(11) Latest Update Time
  UserSign nVarChar(8) Latest Update User Code
  Port Int(11) Port
