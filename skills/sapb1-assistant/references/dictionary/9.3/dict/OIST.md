<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIST - BoE Instruction
Module: Banking | 4 columns | ObjType: 269
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: IsCancel, InstrCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  InstrCode nVarChar(2) Instruction
  InstrDespt nVarChar(128) Description
  IsCancel VarChar(1) Is Cancellation default=N [Y=Yes, N=No]
