<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSTC - Sales Tax Codes
Module: Administration | 18 columns | ObjType: 128
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(100) Name
  Rate Num(19,6) Rate
  Freight VarChar(1) Freight default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidForAR VarChar(1) Valid for A/R default=Y [Y=Yes, N=No]
  ValidForAP VarChar(1) Valid for A/P default=Y [Y=Yes, N=No]
  TfcId Int(11) Formula Combination ID ->OTFC
  Lock VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxIcms nVarChar(2) Taxation For ICMS
  IsItmLevel VarChar(1) Single Item Level Tax default=N [Y=Yes, N=No]
  CfopIn nVarChar(6) CFOP Incoming Code ->OCFP
  CfopOut nVarChar(6) CFOP Outgoing Code ->OCFP
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FADebit VarChar(1) FA Debit default=N [Y=Yes, N=No]
  IsSystem VarChar(1) Is System Tax Code default=N [Y=Yes, N=No]
