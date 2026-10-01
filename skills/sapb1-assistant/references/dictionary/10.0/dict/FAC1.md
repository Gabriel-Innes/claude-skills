<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# FAC1 - Fixed Asset Parameter Change - Rows
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFAC
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  TransType nVarChar(4) Transaction Type [0=Unknown, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value, 560=Change of Period Control]
  OldDprType nVarChar(15) Old Depreciation Type ->ODTP
  NewDprType nVarChar(15) New Depreciation Type ->ODTP
  OldUsfLife Int(11) Old Useful Life
  NewUsfLife Int(11) New Useful Life
  OldDprDate Date(8) Old Depreciation Start Date
  NewDprDate Date(8) New Depreciation Start Date
  OldSalVal Num(19,6) Old Salvage Value
  NewSalVal Num(19,6) New Salvage Value
  OldTtlUnit Int(11) Old Total Units
  NewTtlUnit Int(11) New Total Units
