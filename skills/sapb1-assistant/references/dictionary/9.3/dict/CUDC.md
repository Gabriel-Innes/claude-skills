<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUDC - User Display Cat.
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CodeID
  FORM: NameID
Fields (name type(len) description [values] ->parent table):
  CodeID Int(11) Code
  NameID nVarChar(20) Name
  FormID Int(11) Form ID
  UserSign Int(6) User Signature ->OUSR
