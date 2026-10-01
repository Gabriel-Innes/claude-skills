<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TNN1 - 1099 Boxes
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Box1099, FormCode
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code ->OTNN
  Box1099 nVarChar(20) 1099 Box
  BoxDescr nVarChar(100) Box Description
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  Min1099Amt Num(19,6) Minimum 1099 Amount
