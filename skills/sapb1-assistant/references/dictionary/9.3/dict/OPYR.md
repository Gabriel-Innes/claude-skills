<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPYR - Payment Reason
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Payment Reason Description
  Default VarChar(1) Default Value default=N [Y=Yes, N=No]
