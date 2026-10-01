<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OKRT - Tax Report Type
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TAX_REP_TY U: TaxRepType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Tax Report Type ID
  TaxRepType nVarChar(254) Tax Report Type Name
  Descrip nVarChar(254) Tax Report Type Description
  SumRepType Int(11) Summary VAT Report Type ->OSVT
  NameDesc nVarChar(254) Tax Report Type Name + Desc
