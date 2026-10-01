<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATHL - Thresholds
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RecType VarChar(1) Report Type default=A [A=Annual Invoice Declaration, B=Blacklist Country]
  EffecFrom Date(8) Effective From
  Company nVarChar(20) Company
  PrivInv nVarChar(20) Private - Invoice
  PrivJE nVarChar(20) Private - Journal Entry
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Tourism nVarChar(20) Tourism
