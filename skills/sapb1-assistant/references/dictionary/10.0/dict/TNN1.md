<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TNN1 - 1099 Boxes
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormCode, Box1099
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code ->OTNN
  Box1099 nVarChar(20) 1099 Box
  BoxDescr nVarChar(100) Box Description
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  Min1099Amt Num(19,6) Minimum 1099 Amount
