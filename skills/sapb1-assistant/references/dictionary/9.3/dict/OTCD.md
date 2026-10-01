<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTCD - Tax Code Determination
Module: Administration | 4 columns | ObjType: 266
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  TCD_TYPE U: TcdType
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TcdType nVarChar(2) Determination Type default=MI [MI=Material Item, SI=Service Item, SD=Service Document, WT=Withholding Tax]
  DftArCode nVarChar(8) Default Sales Tax Code
  DftApCode nVarChar(8) Default Purchase Tax Code
