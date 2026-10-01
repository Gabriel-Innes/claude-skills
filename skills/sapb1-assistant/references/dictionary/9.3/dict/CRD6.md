<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CRD6 - BP's Payer Name
Module: Business Partners | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardPyName, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CardPyName nVarChar(48) Payer Name in Bank Statement
