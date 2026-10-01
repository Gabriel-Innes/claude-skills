<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BTA2 - Brazil Tax Adujstment - Taxes Paid in Advance
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  TAX U: AbsEntry, TaxEntry, TaxLine
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBTA
  LineNum Int(11) Row Number
  TaxEntry Int(11) Tax Entry ->TAX1
  TaxLine Int(11) Tax Line ->TAX1
