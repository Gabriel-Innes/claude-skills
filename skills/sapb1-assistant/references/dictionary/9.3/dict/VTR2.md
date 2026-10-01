<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VTR2 - Doc. Type Filter
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(15) Object Code [13=A/R Invoices, 14=A/R Credit Memos, 18=A/P Invoices, 19=A/P Credit Memos, 24=Incoming Payments, 30=Journal Entries, 46=Outgoing Payments, 57=Checks for Payment, 67=Inventory Transfers, 203=A/R Down Payment, 204=A/P Down Payment]
  FromDocNo Int(11) Doc. Number From
  ToDocNo Int(11) To Doc Number
  Selected VarChar(1) Is Selected Object. default=N [N=No, Y=Yes]
