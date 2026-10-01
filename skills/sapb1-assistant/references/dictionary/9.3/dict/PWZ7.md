<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PWZ7 - Payment Wizard 7-Selected Branches
Module: Marketing Documents | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, IdNumber
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) ID Number ->OPWZ
  BPLId Int(11) Assigned Branch ->OBPL
