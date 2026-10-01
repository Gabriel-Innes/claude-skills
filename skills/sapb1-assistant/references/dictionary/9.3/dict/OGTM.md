<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OGTM - GTS Mapping Object
Module: Marketing Documents | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CreateDate Date(8) Create Date
  GtsMapNum nVarChar(20) GTS Mapping No.
  InvMapEnty Int(11) Link to Invoice Mapping ID ->OIVM
  GtsInvNum Int(11) Link to GTS Invoice Object ->OGTI
  BpCode nVarChar(15) BP Code ->OCRD
  BpName nVarChar(100) BP Name
  BpTaxRegNo nVarChar(20) BP Tax Registration No.
  BpAddrTel nVarChar(80) BP Address and Telephone
  BpBankNum nVarChar(80) BP Bank Number
  Remark nVarChar(254) Remarks
  Checker nVarChar(80) Checker
  Payee nVarChar(80) Payee
  DocAmount Num(19,6) Document Net Amount
  AmtAftDsct Num(19,6) Amount After Discount
  TaxAmount Num(19,6) Tax Amount
  GtsStatus VarChar(1) GTS Status default=1 [1=Exported, 2=Voided, 3=Imported]
  ExportDate Date(8) Export Date
  VoidDate Date(8) Void Date
  ImportDate Date(8) Import Date
