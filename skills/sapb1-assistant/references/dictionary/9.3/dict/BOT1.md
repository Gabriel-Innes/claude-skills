<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BOT1 - Bill of Exchange Transactions
Module: Banking | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BoeType, BOENumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transaction No. ->OBOT
  BOENumber Int(11) Bill of Exchange No.
  BoeType VarChar(1) Bill of Exchange Type default=I [I=Incoming, O=Outgoing]
  DueDate Date(8) Bill of Exchange Due Date
  BPBankCtr nVarChar(3) BP Bank Country ->OCRY
  BPBankCod nVarChar(30) BP Bank Code
  BPBankAct nVarChar(50) BP Bank Account
  BPBankBrnc nVarChar(50) BP Bank Branch
  ExReconNum Int(11) Extra Reconciliation Number
  BOEAbs Int(11) Bill of Exchange Key ->OBOE
  BPLId Int(11) Branch ->OBPL
  EnBPBnkAct Text(16) Encryption of BP Bank Account
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
