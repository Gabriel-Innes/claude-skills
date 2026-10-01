<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FLT1 - 856 Report - Selection Criteria
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FilterName, Code, UserSign, FormNo
Fields (name type(len) description [values] ->parent table):
  FormNo nVarChar(20) Form No.
  Code nVarChar(50) Code
  UserSign Int(6) User Signature ->OUSR
  ExNumData1 Int(11) Extra Numeric Data 1
  ExNumData2 Int(11) Extra Numeric Data 2
  ExNumData3 Int(11) Extra Numeric Data 3
  ExStrData1 nVarChar(254) Extra String Data 1
  ExStrData2 nVarChar(254) Extra String Data 2
  ExStrData3 nVarChar(254) Extra String Data 3
  FilterName nVarChar(30) Filter Name default=_
