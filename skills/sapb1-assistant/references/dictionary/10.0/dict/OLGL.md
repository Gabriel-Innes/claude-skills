<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OLGL - Legal Data
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SRC_DOC U: SrcObjType, SrcObjAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  ObjType nVarChar(20) Object Type default=540000073 ->ADP1
  UserSign Int(6) User Signature ->OUSR
  PrintDate Date(8) Date of Printing
  PrintTime Int(6) Time of Printing
  PrBrand nVarChar(30) Printer Brand
  PrType nVarChar(30) Printer Type
  PrModel nVarChar(30) Printer Model
  PrFwVer nVarChar(30) Printer Firmware Version
  PrDllVer nVarChar(30) Printer DLL Version
  FisSeries nVarChar(30) Fiscal Series
  FisNumber nVarChar(30) Fiscal Number
  DocNumber nVarChar(30) Document Number
  FisUser Int(6) Fiscal User ID ->OUSR
