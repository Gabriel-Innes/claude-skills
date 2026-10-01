<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BTC1 - Internal Bank Operation Codes - Accounts
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
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
