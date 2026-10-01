<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SRT2 - Korean Summary Report - Rows2
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SumRptId, SeqNo
Fields (name type(len) description [values] ->parent table):
  SumRptId nVarChar(100) Summary Rpt ID
  SeqNo Int(11) Sequence Number
  VATRegNum nVarChar(12) VAT Reg. Number of BP
  CardCode nVarChar(15) BP Code on OCRD
  CardName nVarChar(100) BP Name
  TransNo Int(11) Total Trans Number under BP
  BaseAmt Num(19,6) Total Base Amount under BP
  TaxAmt Num(19,6) Total Tax Amount under BP
  Remark nVarChar(100) Line Item Remark, do not use
