<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARC1 - Incoming Payment - Checks - History
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ObjType, LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineID Int(11) Row Number
  DueDate Date(8) Check Date
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Account Number default=-1
  Branch nVarChar(50) Branch Number
  AcctNum nVarChar(50) Account Number
  Details nVarChar(254) Details
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  CheckSum Num(19,6) Check Amount
  Currency nVarChar(3) Check Currency
  Flags Int(11) Flags default=0 ->OCRN
  ObjType nVarChar(20) ObjType ->ADP1
  LogInstanc Int(11) Log Instance default=0
  CountryCod nVarChar(3) Country Code ->OCRY
  CheckAct nVarChar(15) Check Account ->OACT
  CheckAbs Int(11) Check ID Entry ->OCHO
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  Endorse VarChar(1) Endorse default=N [Y=Yes, N=No]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV
