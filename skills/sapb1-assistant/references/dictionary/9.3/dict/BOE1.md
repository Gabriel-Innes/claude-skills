<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BOE1 - Bill of Exchange for Payment - Rows
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, BoeKey
Fields (name type(len) description [values] ->parent table):
  BoeKey Int(11) SBO Internal Key ->OBOE
  LineId Int(11) Row No.
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency ->OCRN
  LineAcct nVarChar(15) Row Account
  Line_A_C VarChar(1) BP/Account default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(11) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
