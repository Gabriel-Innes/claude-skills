<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OHTM - Employee Teams
Module: Human Resources | 3 columns | ObjType: 211
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: teamID
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID
  name nVarChar(20) Team Name
  descriptio Text(16) Description
