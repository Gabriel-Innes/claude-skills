<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TPW4 - VAT Refund
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  RefundAcct nVarChar(15) Refund Account Code
  RefundAmnt Num(19,6) Refund Amount
  RfndAmntFC Num(19,6) Refund Amount FC
  RfndAmntSC Num(19,6) Refund Amount SC
