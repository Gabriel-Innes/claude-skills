<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SRA1 - Scheduled Report Parameters
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ParamCode, ActionCode
  SECONDARY U: KeyNumber, KeyString, ActionCode
Fields (name type(len) description [values] ->parent table):
  ActionCode Int(11) Action Code
  ParamCode Int(11) Parameter Code
  KeyString nVarChar(32) Parameter Key String
  KeyNumber Int(11) Parameter Key Numerator
  ValString Text(16) Parameter Value String
  ValNumber Int(11) Parameter Value Number
  ValMoney Num(19,6) Parameter Value Money
