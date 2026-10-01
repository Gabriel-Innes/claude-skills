<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACRB - Business Partner Bank Accounts - History
Module: Business Partners | 46 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  ACCOUNT U: LogInstanc, CardCode, Account, BankCode, Country
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CardCode nVarChar(15) BP Code ->OCRD
  BankCode nVarChar(30) Bank Code
  Country nVarChar(3) Country ->OCRY
  Account nVarChar(50) Account No.
  Branch nVarChar(50) Branch
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  State nVarChar(3) State
  ControlKey nVarChar(2) Control Key
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  LogInstanc Int(11) Log Instance default=0
  Building Text(16) Building/Floor/Room
  AliasName nVarChar(50) Alias Name
  AcctType VarChar(1) Account Type
  BankKey Int(11) Bank Internal ID ->ODSC
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Phone
  Fax nVarChar(25) Fax
  ISRType Int(6) ISR Type
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(6) Customer ID Number default=0
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  SwiftNum nVarChar(50) BIC/SWIFT Code
  ABARoutNum nVarChar(25) ABA Routing Number
  MandateID nVarChar(35) Mandate ID
  SignDate Date(8) Date of Signature
  PWZAbsEntr Int(11) PWZ ABS Entry ->OPWZ
  BranchChk nVarChar(5) Branch Check Digit
  MandatDate Date(8) Date Of Mandate Expiration
  SeqType nVarChar(4) SEPA Seq. Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  ActType VarChar(1) Account Type [C=Checking Account, S=Savings Account]
  IsPrenot VarChar(1) Is Prenotification default=N [Y=Yes, N=No]
  EnAccount Text(16) Encryption of Account
  EnIBAN Text(16) Encryption of IBAN
  EncryptIV nVarChar(100) Encrypt IV
