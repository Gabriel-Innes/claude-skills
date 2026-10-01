<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPW4 - VAT Refund
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  RefundAcct nVarChar(15) Refund Account Code
  RefundAmnt Num(19,6) Refund Amount
  RfndAmntFC Num(19,6) Refund Amount FC
  RfndAmntSC Num(19,6) Refund Amount SC
