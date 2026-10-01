<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RLD1 - Reference Links Definition
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, TargetType, TargetFld
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORLD
  TargetType VarChar(1) Target Type default=H [H=Header, B=BP Row, L=Row]
  TargetFld nVarChar(50) Target Field
  SourceFld nVarChar(50) Source Field
  OrderNum Int(11) Order Number
  SourceType VarChar(1) Source Type default=E [B=Base Document Reference, C=Column, D=Default, E=Not Defined, I=Installment Number, S=Reference Link Sources, T=Remarks Template]
