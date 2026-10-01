<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSTS - Service App Technician settings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Technician Int(11) Technician ->OHEM
  Choice VarChar(1) Choice default=C [G=Group, C=Customize]
  GroupCode Int(11) Group Code ->OSSG
