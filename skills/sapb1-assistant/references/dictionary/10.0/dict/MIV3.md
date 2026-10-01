<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MIV3 - Grouped Tax Rows of MI
Module: Marketing Documents | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Entry, LnDataNum
Fields (name type(len) description [values] ->parent table):
  Entry Int(11) Monthly Invoice Entry ->OMIV
  TaxCode nVarChar(8) Tax Code
  VatPercent Num(19,6) VAT Percent
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  BaseSum Num(19,6) Base Sum
  BaseSumSc Num(19,6) Base Sum (SC)
  BaseSumFc Num(19,6) Base Sum (FC)
  VatSum Num(19,6) VAT Sum
  VatSumSc Num(19,6) VAT Sum (SC)
  VatSumFc Num(19,6) VAT Sum (FC)
  TODedBaseS Num(19,6) Tax Only Deducted Base Sum
  TODedBaSSC Num(19,6) Tax Only Deducted Base Sum (SC)
  TODedBaSFC Num(19,6) Tax Only Deducted Base Sum (FC)
  LnDataNum Int(11) Row Number in Tax Data default=-1
