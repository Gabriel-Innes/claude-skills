<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHE7 - Savings Payments
Module: Human Resources | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Row
  ConName nVarChar(50) Contract Name
  PmntNotes nVarChar(50) Payment Details
  AN Num(19,6) Employee
  AG Num(19,6) Employer
  BankName nVarChar(50) Bank Name
  BankCode nVarChar(20) Bank Code
  BankAcct nVarChar(20) Bank Account
  LogInstanc Int(11) Log Instance default=0
  ANCurrency nVarChar(3) Employee Currency
  AGCurrency nVarChar(3) Employer Currency
  Sequence VarChar(1) Frequency default=M [B=, M=Monthly, Q=Quarterly, S=Semi-annually, Y=Yearly]
  EnBnkAcct Text(16) Encryption of Bank Account
  EncryptIV nVarChar(100) Encrypt IV
