<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWUA - SEWUA
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  NoUdfDb Int(11) number of UDFs
  NoTblUdf Int(11) UDFs per table
  NoAutoFMS Int(11) Auto Refresh in use
  NoRegFMS Int(11) No FMS with Refresh Regular
  NoCustTmpl Int(11) No of customised Document
