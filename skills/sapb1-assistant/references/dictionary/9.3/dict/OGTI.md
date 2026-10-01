<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OGTI - GTS Invoice
Module: Marketing Documents | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CreateDate Date(8) Create Date
  MappingNum nVarChar(20) GTS Mapping No.
  Voiding VarChar(1) Voiding Flag default=0 [0=Normal, 1=Voided]
  ItemList VarChar(1) Item List [0=Without Item List, 1=With Item List]
  CategNum nVarChar(20) GTS Cat. No.
  GtsInvNum nVarChar(8) GTS Invoice No.
  ItemRowNum Int(11) Item List Row Number
  DocDate Date(8) Document Date
  FiscaMonth Int(6) Fiscal Month
  DocAmount Num(19,6) Document Amount
  VatPercent Num(19,6) VAT Percent
  VatAmount Num(19,6) VAT Amount
  BpName nVarChar(100) BP Name
  BpTaxRgNum nVarChar(20) BP Tax Registration No.
  BpAddrTel nVarChar(80) BP Address and Telephone
  BpBankNum nVarChar(60) BP Bank Number
  SellerName nVarChar(80) Seller Name
  SelTaxReg nVarChar(80) Seller Tax Registration No.
  SelAddTel nVarChar(80) Seller Address and Tel.
  SelBankAct nVarChar(80) Seller Bank Account
  Remarks nVarChar(160) Remarks
  Issuer nVarChar(8) Issuer
  Checker nVarChar(8) Checker
  Payee nVarChar(8) Payee
  InBndFile nVarChar(254) Inbound File: Full Name
