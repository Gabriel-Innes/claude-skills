<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRB3 - Tax Report Wizard - Selected Tax Categories
Module: Reports | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NfTaxId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRB
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
