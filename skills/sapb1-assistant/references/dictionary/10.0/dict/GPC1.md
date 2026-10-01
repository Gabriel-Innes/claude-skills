<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPC1 - Authority Assignment
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, BPLId, State
  CARD_CODE U: CardCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OGPC
  BPLId Int(11) Branch ->OBPL
  State nVarChar(3) State ->OCST
  CardCode nVarChar(15) Vendor Code ->OCRD
