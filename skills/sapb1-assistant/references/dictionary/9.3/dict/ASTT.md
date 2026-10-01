<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASTT - Sales Tax Authorities Type
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsId
  NAME U: LogInstanc, Name
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  Name nVarChar(40) Type Name
  UserSign Int(6) User Signature ->OUSR
  IsVat VarChar(1) VAT default=N [Y=Yes, N=No]
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
  TpsId Int(11) ID of Tax Parameter Set ->OTPS
  PLABalance Num(19,6) PLA Current Balance
  Locked VarChar(1) Locked default=N
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]
