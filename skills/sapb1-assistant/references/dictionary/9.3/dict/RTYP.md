<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RTYP - Document Type List
Module: Reports | 9 columns | ObjType: 10000196
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CODE
Fields (name type(len) description [values] ->parent table):
  CODE nVarChar(4) Report Type
  NAME nVarChar(250) Type Name
  DEFLT_REP nVarChar(8) Standard Report
  ADD_NAME nVarChar(250) Addon Name
  FRM_TYPE nVarChar(250) Add-On Form Type
  MNU_ID nVarChar(250) Menu Id
  IS_SYS VarChar(1) Is sytem type or not default=Y [Y=Yes, N=No]
  DEFLT_SEQ Int(11) Standard Sequence
  TYPE VarChar(1) Type default=L [L=Layout, P=Print Sequence]
