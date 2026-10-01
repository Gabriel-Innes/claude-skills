<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ALR2 - Dynamic message data row
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Location, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  Location Int(11) The order of columns in message
  ColName nVarChar(30) The column name in message
  Link VarChar(1) Link Indication default=N [N=No, Y=Yes]
