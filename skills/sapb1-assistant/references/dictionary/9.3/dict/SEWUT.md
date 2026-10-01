<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWUT - SEWUT
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: transid, CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  transid nVarChar(10) transid
  transtype nVarChar(3) transtype
  installmen nVarChar(10) installments
