<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCST - States
Module: Administration | 9 columns | ObjType: 130
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Country
  GST_CODE: Country, GSTCode
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Country nVarChar(3) Country ->OCRY
  Name nVarChar(100) Name
  UserSign Int(6) User Signature ->OUSR
  eCode Int(6) eCode
  GNRECode nVarChar(4) GNRE Code
  GSTCode nVarChar(2) GST State Code
  GSTIsUT VarChar(1) Is Union Territory default=N [Y=Yes, N=No]
  GroupCode Int(6) Group Code ->OSTG
