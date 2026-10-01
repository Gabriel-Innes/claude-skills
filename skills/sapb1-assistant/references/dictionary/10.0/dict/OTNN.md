<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTNN - 1099 Forms
Module: Administration | 4 columns | ObjType: 145
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormCode
  NAME U: Form1099
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code
  Form1099 nVarChar(100) 1099 Form
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
