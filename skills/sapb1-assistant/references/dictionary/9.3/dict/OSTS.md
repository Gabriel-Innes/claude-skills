<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSTS - Service App Technician settings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Technician Int(11) Technician ->OHEM
  Choice VarChar(1) Choice default=C [G=Group, C=Customize]
  GroupCode Int(11) Group Code ->OSSG
