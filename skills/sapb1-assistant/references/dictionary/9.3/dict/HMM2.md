<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HMM2 - Child Table of OHHM
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Child No.
  VerType VarChar(1) Version Type [H=SAP HANA Version, A=SAP Business One Analytics Powered by HANA Version, B=SAP Business One Version]
  Ver nVarChar(100) Version
