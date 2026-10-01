<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWTT - Withholding Tax Type
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTTypeId
  WT_TYPE U: WTType
Fields (name type(len) description [values] ->parent table):
  WTTypeId Int(11) Internal Number
  WTType nVarChar(10) Type
  WTThresh Num(19,6) Min. WTax Amount
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
