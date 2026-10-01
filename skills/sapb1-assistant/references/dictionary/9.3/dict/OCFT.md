<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCFT - Cash Flow Transactions - Rows
Module: Finance | 20 columns | ObjType: 241
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFTId
Fields (name type(len) description [values] ->parent table):
  CFTId Int(11) Cash Flow Transaction ID
  CFWId Int(11) Cash Flow Line Item ID ->OCFW
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SysCredit Num(19,6) System Credit Amount
  SysDebit Num(19,6) System Debit Amount
  FCDebit Num(19,6) FC Debit Amount
  FCCredit Num(19,6) FC Credit Amount
  FCCurrency nVarChar(3) Foreign Currency
  Account nVarChar(15) Account Code ->OACT
  BatchNum Int(11) Batch No.
  JDTId Int(11) Journal Entry ID
  JDTLineId Int(11) Journal Entry Line ID
  TransType nVarChar(20) Source Object [24=Incoming Payment, 46=Vendor Payment, 30=Journal Entry, 140=Payment Draft, 29=Journal Vouchers List, 25=Deposit, 76=Postdated Check Deposit, 182=Bill of Exchange Transaction, 42=Bank Statement, 157=Payment Wizard]
  BaseRef nVarChar(11) Base Reference
  PaymentMen nVarChar(11) Payment Means
  PaymentRef nVarChar(11) Payment Reference
  PostDate Date(8) Posting Date
  ValueDate Date(8) Value Date
  Status VarChar(1) Status
