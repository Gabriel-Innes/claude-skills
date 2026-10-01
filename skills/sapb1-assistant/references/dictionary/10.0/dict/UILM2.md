<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UILM2 - Inventory Account Substitute
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID, AccountId, DebitCredi
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  AccountId Int(6) Account ID default=-1
  AcctCode nVarChar(15) Account Code ->OACT
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=Debit, C=Credit]
