<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XROBJ - XLR Company Report Objects
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, RepObjId
Fields (name type(len) description [values] ->parent table):
  RepObjId nVarChar(38) RepObjId
  Name nVarChar(50) Name
  Descriptio Text(16) Description
  Creator nVarChar(50) Creator
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) ModifyDate
  ObjType Int(11) ObjType
  XmlId nVarChar(38) XmlId
  XlsId nVarChar(38) XlsID
  VariablesI nVarChar(38) VariablesID
  Reference Text(16) Reference
  RefType Int(11) RefType default=0
  Global Int(11) Global default=0
