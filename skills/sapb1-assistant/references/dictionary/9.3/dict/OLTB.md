<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OLTB - Location-based Tax Bal Table
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  index: STACode, STAType, LocCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  LocCode Int(11) Location Code ->OLCT
  STAType Int(11) Tax Type ->OSTT
  STACode nVarChar(8) STA Code ->OSTA
  BalaType VarChar(1) Balance Type [P=, R=, C=, F=]
  Balance Num(19,6) Balance
