<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SRT1 - Korean Summary Report - Rows1
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqNo, SumRptId
Fields (name type(len) description [values] ->parent table):
  SumRptId nVarChar(100) Summary Rpt ID
  SeqNo Int(11) Sequence Number
  CardNum Int(11) Business Partner Total Numbers
  TransNum Int(11) Total Trans Number Under BP
  BaseAmt Num(19,6) Total Base Amount Under BPs
  TaxAmt Num(19,6) Total Tax Amount Under BPs
