<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ILM2 - Inventory Account Substitute
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DebitCredi, AccountId, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  AccountId Int(6) Account ID default=-1
  AcctCode nVarChar(15) Account Code ->OACT
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=Debit, C=Credit]
