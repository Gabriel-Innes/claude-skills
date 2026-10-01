<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCSN - Certificate Series
Module: Administration | 5 columns | ObjType: 10000075
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  SECTION: Section
  LOCATION: Location
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(4) Code
  Section Int(11) Section ->OSEC
  Location Int(11) Location ->OLCT
  DfltSeries Int(6) Default Series default=0
