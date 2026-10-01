<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCMF - Common Functions of Fiori-Style Cockpit
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemIndex, UserID
  INDEX: ItemIndex
Fields (name type(len) description [values] ->parent table):
  UserID Int(6) User ID ->OUSR
  ItemIndex Int(11) Common Function Item Index
  MenuUID nVarChar(50) Menu UID
  GroupID Int(6) Authorization Group ID ->OUGR
