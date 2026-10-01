<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIST - BoE Instruction
Module: Banking | 4 columns | ObjType: 269
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: InstrCode, IsCancel
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  InstrCode nVarChar(2) Instruction
  InstrDespt nVarChar(128) Description
  IsCancel VarChar(1) Is Cancellation default=N [Y=Yes, N=No]
