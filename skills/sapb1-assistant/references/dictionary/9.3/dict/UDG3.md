<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDG3 - User Defaults - POS/Cash Register
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PosCashReg, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  PosCashReg Int(11) POS/Cash Register ->OPCM
