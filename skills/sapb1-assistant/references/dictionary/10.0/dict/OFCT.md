<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFCT - Sales Forecast
Module: MRP | 7 columns | ObjType: 198
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsID
  FCT_CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Internal Number
  Code nVarChar(16) Forecast Code
  Name nVarChar(100) Forecast Name
  UserSign Int(6) User Signature ->OUSR
  StartDate Date(8) Forecast Start Date
  EndDate Date(8) Forecast End Date
  FormView VarChar(1) Forecast Form View default=D [D=Daily, W=Weekly, M=Monthly]
