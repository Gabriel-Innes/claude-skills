<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CHO1 - Checks for Payment - Rows
Module: Banking | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CheckKey, LineId
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) SAP Business One Internal Key ->OCHO
  LineId Int(11) Row Number
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency
  LineAcct nVarChar(15) Row Account
  Line_A_C VarChar(1) Business Partner or Account default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  LineMnyLC Num(19,6) Row Total (LC)
  LineMnySC Num(19,6) Row Total (SC)
  LineMnyFC Num(19,6) Row Total (FC)
  TotLineLC Num(19,6) Row Total (LC)
  TotLineSC Num(19,6) Row Total (SC)
  TotLineFC Num(19,6) Row Total (FC)
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
