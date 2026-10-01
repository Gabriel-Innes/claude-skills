<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTCD - Tax Code Determination
Module: Administration | 4 columns | ObjType: 266
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD_TYPE U: TcdType
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TcdType nVarChar(2) Determination Type default=MI [MI=Material Item, SI=Service Item, SD=Service Document, WT=Withholding Tax]
  DftArCode nVarChar(8) Default Sales Tax Code
  DftApCode nVarChar(8) Default Purchase Tax Code
