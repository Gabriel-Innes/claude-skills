<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ALR3 - Dynamic message data cells
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, Location, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  Location Int(11) Number of Column in Message
  Line Int(11) Number of Column in Message
  Value nVarChar(254) The column/row value
  ObjType nVarChar(20) The linked object
  KeyStr nVarChar(254) Key string in linked object
