<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RLS1 - Reference Links Sources Definition
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
  OBJARRFLD U: SrcFld, SrcArr, SrcObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORLS
  LineID Int(11) Line Id
  SrcObjType nVarChar(20) Source Object Type
  SrcArr Int(6) Source of Posting
  SrcFld nVarChar(21) Source Field
