<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWUA - SEWUA
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  NoUdfDb Int(11) number of UDFs
  NoTblUdf Int(11) UDFs per table
  NoAutoFMS Int(11) Auto Refresh in use
  NoRegFMS Int(11) No FMS with Refresh Regular
  NoCustTmpl Int(11) No of customised Document
