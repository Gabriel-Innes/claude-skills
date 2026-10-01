<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTOB - 1099 Opening Balance
Module: Administration | 6 columns | ObjType: 148
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Box1099, Form1099, VendCode
Fields (name type(len) description [values] ->parent table):
  VendCode nVarChar(15) Vendor Code ->OCRD
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  PostDate Date(8) Posting Date
  AmountLC Num(19,6) Amount (LC)
  Submitted VarChar(1) Submitted default=N [Y=Yes, N=New]
