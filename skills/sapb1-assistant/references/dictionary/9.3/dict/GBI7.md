<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI7 - GBI Row 7 - Accounting Vouchers
Module: Finance | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  DocDate nVarChar(8) Document Date
  DocType nVarChar(12) Document Type
  JrnEntryNo nVarChar(20) Journal Entry Number
  LnNo Int(11) Line Number
  Remark nVarChar(50) Details of Each Line
  AcctNo nVarChar(15) G/L Account Number
  Currency nVarChar(3) Transaction Currency
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  FCDebit Num(19,6) Debit Foreign Currency Amount
  FCCredit Num(19,6) Credit Foreign Currency Amount
  Rate Num(19,6) Exchange Rate
  Quantity Num(19,6) Quantity
  UnitPrice Num(19,6) Unit Price
  EvaGrp nVarChar(254) Evaluation Group
  SettMeth nVarChar(20) Settlement Method
  BillType nVarChar(20) Bill Type
  BillNo nVarChar(30) Bill Number
  BillDate nVarChar(8) Bill Date
  AttmtNum Int(6) Number of Attachments
  Creator nVarChar(155) Creator of the Voucher
  Approver nVarChar(155) Approver of the Voucher
  Bookkeeper nVarChar(155) Bookkeeper
  Cashier nVarChar(155) Cashier
  Posted VarChar(1) Posted Sign default=1 [1=, 0=]
  Reversed VarChar(1) Reversed Sign default=0 [1=, 0=]
  DocNum nVarChar(20) Document Number
