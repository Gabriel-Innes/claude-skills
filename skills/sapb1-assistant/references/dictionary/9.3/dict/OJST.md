<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OJST - TDS Adjustment
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  DocDate Date(8) Posting Date
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(11) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Generation Time
  DepositNum Int(11) Deposit Number ->OVPM
  CertNum nVarChar(31) Certificate Number
