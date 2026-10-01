<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ABTC - Internal Bank Operation Codes - Log
Module: Banking | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  InOpCode nVarChar(15) Internal Bank Operation Code Name
  PstTrans VarChar(1) Posting Transaction default=1 [1=Incoming Bank Transfer, 2=Outgoing Bank Transfer, 3=Incoming Bill of Exchange, 4=Outgoing Bill of Exchange, 5=Outgoing Checks, 6=Deposit]
  BPorAct VarChar(1) BP or Account default=C [C=BP, A=Account]
  PstMethod VarChar(1) BP Posting Method default=1 [0=, 1=Business Partner from/to Bank Account, 2=Bank Interim Account or Bank Account, 3=External Reconciliation]
  ActFee nVarChar(15) Account Fee ->OACT
  ProjFee nVarChar(20) Project Fee ->OPRJ
  PrftCntFee nVarChar(8) Fee Distribution Rule ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Descript nVarChar(40) Operation Description
  PrftCntFe2 nVarChar(8) Fee Distribution Rule2 ->OOCR
  PrftCntFe3 nVarChar(8) Fee Distribution Rule3 ->OOCR
  PrftCntFe4 nVarChar(8) Fee Distribution Rule4 ->OOCR
  PrftCntFe5 nVarChar(8) Fee Distribution Rule5 ->OOCR
  UserSign2 Int(6) Updating User ->OUSR
