<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CLG1 - Activity CheckIns
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, ClgCode
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number ->OCLG
  LineNum Int(11) Line Number
  Date Date(8) Date
  Location nVarChar(254) Location
  Latitude nVarChar(13) Latitude
  Longitude nVarChar(14) Longitude
  Time Int(11) Time
  OwnerUser Int(6) Owner User ->OUSR
  OwnerEmp Int(11) Owner Employee ->OHEM
  LogInstanc Int(11) Log Instance default=0
