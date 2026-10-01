<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSPG - Special Prices for Groups
Module: Inventory and Production | 6 columns | ObjType: 85
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjKey, ObjType, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ObjType nVarChar(20) Object Type [52=Item Group, 8=Item Properties, 43=Companies]
  ObjKey nVarChar(50) Object Key
  Discount Num(19,6) Discount
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Form ->OUSR
