<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MAB1 - Menu Abbreviation
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MenuID, absEntry
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Key
  MenuID Int(11) Menu ID
  Alias nVarChar(20) Menu Alias
