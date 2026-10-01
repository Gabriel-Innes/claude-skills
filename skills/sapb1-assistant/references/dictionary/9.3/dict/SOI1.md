<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SOI1 - Statement of Import - Business Partners
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OSOI
  CardCode nVarChar(15) BP Card Code ->OCRD
