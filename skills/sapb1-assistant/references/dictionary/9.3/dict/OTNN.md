<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTNN - 1099 Forms
Module: Administration | 4 columns | ObjType: 145
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FormCode
  NAME U: Form1099
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code
  Form1099 nVarChar(100) 1099 Form
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
