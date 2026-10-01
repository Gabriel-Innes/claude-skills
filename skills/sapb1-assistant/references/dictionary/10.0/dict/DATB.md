<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DATB - Data Archive Tax Balance
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  LocCode Int(11) Location Code ->OLCT
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
  TaxComId Int(11) Tax Component ID ->OSTT
  MatType Int(11) Material Type
  ArchBal Num(19,6) Data Archived Balance
  TaxAcct nVarChar(15) Tax Account ->OACT
  IsPLA VarChar(1) PLA Field
  IsTaxCred VarChar(1) Tax Credit Field
