<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BTC1 - Internal Bank Operation Codes - Accounts
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(6) Row
  GLAct nVarChar(15) G/L Account ->OACT
  Project nVarChar(20) Project ->OPRJ
  PrftCenter nVarChar(8) Distribution Rule ->OOCR
  VatCode nVarChar(8) VAT Code ->OVTG
  LogInstanc Int(11) Log Instance default=0
  PrftCent2 nVarChar(8) Distribution Rule2 ->OOCR
  PrftCent3 nVarChar(8) Distribution Rule3 ->OOCR
  PrftCent4 nVarChar(8) Distribution Rule4 ->OOCR
  PrftCent5 nVarChar(8) Distribution Rule5 ->OOCR
