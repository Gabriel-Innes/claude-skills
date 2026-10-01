<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD6 - BP's Payer Name
Module: Business Partners | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, CardPyName
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CardPyName nVarChar(48) Payer Name in Bank Statement
