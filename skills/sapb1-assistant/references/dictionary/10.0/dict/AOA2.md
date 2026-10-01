<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AOA2 - Blanket Agreement - Details
Module: Business Partners | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgrNo, AgrLnNum, AgrEfctNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective Row No.
  DatePeriod VarChar(1) Frequency default=M [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semi-Annually, A=Annually, O=One Time]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  CallUp nVarChar(100) Release Information
  WhsCode nVarChar(8) Warehouse Code default=-1 ->OWHS
  Quantity Num(19,6) Item Quantity
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  LogInstanc Int(11) Log Instance default=0
  AmountLC Num(19,6) Planned Amount (LC)
  AmountFC Num(19,6) Planned Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
