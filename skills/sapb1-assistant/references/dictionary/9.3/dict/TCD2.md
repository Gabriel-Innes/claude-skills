<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCD2 - Key Field Values
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD2_UNI U: DispOrder, Tcd1Id
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd1Id Int(11) Tax Determination ID ->TCD1
  DispOrder Int(11) Display Order
  KeyFld_1_V nVarChar(50) Key Fields 1 Value
  KeyFld_2_V nVarChar(50) Key Fields 2 Value
  KeyFld_3_V nVarChar(50) Key Fields 3 Value
  KeyFld_4_V nVarChar(50) Key Fields 4 Value
  KeyFld_5_V nVarChar(50) Key Fields 5 Value
