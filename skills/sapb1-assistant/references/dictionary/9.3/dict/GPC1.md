<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GPC1 - Authority Assignment
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: State, BPLId, AbsId
  CARD_CODE U: CardCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OGPC
  BPLId Int(11) Branch ->OBPL
  State nVarChar(3) State ->OCST
  CardCode nVarChar(15) Vendor Code ->OCRD
