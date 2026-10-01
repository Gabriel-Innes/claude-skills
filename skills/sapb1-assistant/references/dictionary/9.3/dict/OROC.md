<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OROC - Retorno Operation Codes
Module: Banking | 8 columns | ObjType: 1320000028
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OccurCode Int(11) Occurrence Code
  MovemnCode Int(6) Movement Code
  BoeStatus VarChar(1) BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  Descript nVarChar(254) Description
  Color Int(11) Color
  FileFormat nVarChar(100) File Format
  BankCode nVarChar(30) Bank Code
