<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWU1 - SEWU1
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TblId, CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  TblId nVarChar(20) Table Id
  UDFNum Int(11) number of UDFs
  TotUdfSz Int(11) Total UDFs size per table
