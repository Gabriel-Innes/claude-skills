<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACL1 - Activity Check-ins
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ClgCode, LineNum, LogInstanc
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
