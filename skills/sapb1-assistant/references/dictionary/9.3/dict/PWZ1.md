<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ1 - Payment Wizard - Rows 1
Module: Banking | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  CardType VarChar(1) BP Type
  Checked VarChar(1) Checked
  BPCurrency nVarChar(3) BP Currency
  BPSingleP VarChar(1) BP Single Payment default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
