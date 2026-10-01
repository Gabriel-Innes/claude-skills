<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SLSC - Local Settings Components CABs
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code, LocCode
Fields (name type(len) description [values] ->parent table):
  LocCode nVarChar(3) LocalCode
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  Type VarChar(1) Type [C=Chart of accounts, R=Reports, O=Objects, P=CR Report, L=CR Layout, H=HANA Content]
  DataCab Text(16) Data CAB
  System VarChar(1) System package default=N [Y=Yes, N=No]
