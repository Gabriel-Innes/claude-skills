<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RCR1 - Recurring Postings - Rows
Module: Finance | 29 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, Instance, RcurCode
Fields (name type(len) description [values] ->parent table):
  RcurCode nVarChar(8) Recurring Postings Code ->ORCR
  LineId Int(11) Row Number default=0
  AcctCode nVarChar(15) Account Code
  AcctDesc nVarChar(100) Account Description
  Debit Num(19,6) Debit
  Credit Num(19,6) Credit
  Currency nVarChar(3) Currency
  Instance Int(6) Instance
  VatGroup nVarChar(8) Tax Group ->OVTG
  UserSign Int(6) User Signature ->OUSR
  VatLine VarChar(1) VAT Row default=N [Y=Yes, N=No]
  CtrlAcct nVarChar(15) Control Account
  OcrCode nVarChar(8) Distr. Rule ->OOCR
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  OcrCode1 nVarChar(8) Costing Code 1 ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  WtLiable VarChar(1) WTax-Liable [Y=Yes, N=No]
  WTaxLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  GrossValue Num(19,6) Gross Value
  Project nVarChar(20) Project Code ->OPRJ
  BPLId Int(11) Branch ->OBPL
  CemCode nVarChar(20) Cost Element Code ->OCEM
