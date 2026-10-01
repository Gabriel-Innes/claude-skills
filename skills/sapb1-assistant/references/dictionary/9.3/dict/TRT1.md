<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRT1 - Posting Templates - Rows
Module: Finance | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Sequence, TrtCode
Fields (name type(len) description [values] ->parent table):
  TrtCode nVarChar(8) Template Code ->OTRT
  Sequence Int(11) Sequence Row No.
  AcctCode nVarChar(15) Account Code
  Line_Descr nVarChar(100) Account Description
  Debit Num(19,6) Debit
  Credit Num(19,6) Credit
  VatGroup nVarChar(8) Tax Group ->OVTG
  UserSign Int(6) User Signature ->OUSR
  VatLine VarChar(1) Vat Line default=N [Y=Yes, N=No]
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
  CemCode nVarChar(20) Cost Element Code ->OCEM
