<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSYS - System Strings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
  STRING U: String
Fields (name type(len) description [values] ->parent table):
  Num Int(11) String number
  String nVarChar(250) String
  StringType Int(6) String Type default=0 [0=Free Text, 1=Form, 2=Table, 3=Resource]
  RefCounter Int(11) Reference Counter
