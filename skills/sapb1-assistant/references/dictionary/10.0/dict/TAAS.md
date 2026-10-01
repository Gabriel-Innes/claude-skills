<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TAAS - Result of TaaS Tax Code Check
Module: Reports | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  DUMMY U: Internal
Fields (name type(len) description [values] ->parent table):
  Internal Int(11) Internal Number
  TaxObjType nVarChar(20) Tax Object Type
  TaxAbsEntr Int(11) Tax Abs Entry
  LineSeq Int(11) Row Sequence
  DocObjType nVarChar(20) Doc. Object Type
  InvDocEntr Int(11) InvDocEntry
  DocDate Date(8) Doc. Date
  SrcArrType Int(11) Source Array Type
  SrcLineNum Int(11) Source Row Number default=-1
  TaxCode nVarChar(8) Tax Code
  StaCode nVarChar(8) Tax Authorities Code
  StaType Int(11) Tax Authorities Type
  IsOK VarChar(1) Is OK
  ErrorType VarChar(1) Error Type
  ErrorDescr nVarChar(254) Error Description
  IsLiable VarChar(1) Is Tax Liable
  BaseSum Num(19,6) Base Sum
  Tax1Rate Num(19,6) TAX1 Rate
  TaasRate Num(19,6) TaaS Rate
  Tax1VatSum Num(19,6) Tax1 VAT Sum
  TaasVatSum Num(19,6) TaaS VAT Sum
