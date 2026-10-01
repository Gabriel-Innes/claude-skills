<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RLD1 - Reference Links Definition
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TargetFld, TargetType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORLD
  TargetType VarChar(1) Target Type default=H [H=Header, B=BP Row, L=Row]
  TargetFld nVarChar(50) Target Field
  SourceFld nVarChar(50) Source Field
  OrderNum Int(11) Order Number
  SourceType VarChar(1) Source Type default=E [B=Base Document Reference, C=Column, D=Default, E=Not Defined, I=Installment Number, S=Reference Link Sources, T=Remarks Template]
