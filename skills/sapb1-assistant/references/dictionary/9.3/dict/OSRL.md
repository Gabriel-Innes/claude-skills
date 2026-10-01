<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSRL - Serial Numbers
Module: Administration | 5 columns | ObjType: 47
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SerialNum, ItemCode
  INV_NUM: ItemCode, DocNum
  CARD_KEY: CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SerialNum nVarChar(17) Serial Number
  CardCode nVarChar(15) Customer Code ->OCRD
  DocNum Int(11) Invoice Number
  UserSign Int(6) User Signature ->OUSR
