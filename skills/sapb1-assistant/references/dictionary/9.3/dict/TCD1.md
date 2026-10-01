<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCD1 - Key Fields for Determination
Module: Administration | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD1_UNI U: Priority, TcdId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TcdId Int(11) Tax Determination Code ->OTCD
  KeyFld_1 Int(11) Key Fields 1 default=0
  KeyFld_2 Int(11) Key Fields 2 default=0
  KeyFld_3 Int(11) Key Fields 3 default=0
  Priority Int(11) Priority default=0
  Descr nVarChar(100) Description
  KeyFld_4 Int(11) Key Fields 4 default=0
  UDFTable_1 nVarChar(20) UDF Table Name 1
  UDFAlias_1 nVarChar(18) UDF Field Alias 1
  UDFTable_2 nVarChar(20) UDF Table Name 2
  UDFAlias_2 nVarChar(18) UDF Field Alias 2
  UDFTable_3 nVarChar(20) UDF Table Name 3
  UDFAlias_3 nVarChar(18) UDF Field Alias 3
  UDFTable_4 nVarChar(20) UDF Table Name 4
  UDFAlias_4 nVarChar(18) UDF Field Alias 4
  KeyFld_5 Int(11) Key Fields 5 default=0
  UDFTable_5 nVarChar(20) UDF Table Name 5
  UDFAlias_5 nVarChar(18) UDF Field Alias 5
