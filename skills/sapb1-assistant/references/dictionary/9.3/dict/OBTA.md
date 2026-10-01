<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBTA - Brazil - Tax Adjustment
Module: General | 48 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NUM U: DocNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Status VarChar(1) Status default=O [O=Open, C=Canceled]
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocNum Int(11) Document Number
  DocRate Num(19,6) Document Rate
  TaxCat Int(11) Tax Category
  Type Int(6) Type default=1 [1=Referred Collection Document, 2=Other Obligations, Adjustments, and Information Originating from Fiscal Documents, 3=Adjustment of ICMS Appraisal, 4=Adjustment and Additional Information of ICMS Appraisal, 5=Adjustment of ICMS and Identification of Fiscal Documents, 6=ICMS Obligations to Pay or Paid - Own Operations, 7=Adjustment of ICMS-ST Appraisal, 8=Adjustment and Additional Information of ICMS-ST Appraisal, 9=Adjustment of ICMS-ST and Identification of Fiscal Documents, 10=ICMS-ST Obligations to Pay or Paid - Own Operations, 11=Adjustment of IPI Appraisal, 12=Adjustment of PIS Appraisal, 13=Adjustment of COFINS appraisal]
  Oper Int(6) Operation default=1 [1=Other Debits, 2=Chargeback of Debits, 3=Other Credits, 4=Credit Chargeback, 5=Tax Deductions Calculated]
  RefVisType Int(11) Referenced Document ID default=1 [1=A/R Invoices, 2=A/P Invoices, 3=A/R Credit Memos, 4=A/P Credit Memos, 5=Deliveries, 6=Goods Receipt PO, 7=A/R Reserve Invoices, 8=A/P Reserve Invoices, 9=External Document]
  RefObjType Int(11) Referenced Document Type [13=A/R Invoices, 18=A/P Invoices, 14=A/R Credit Memos, 19=A/P Credit Memos, 15=Deliveries, 20=Goods Receipt PO, -1=External Document]
  RefDocEnt Int(11) Referenced Document Entry
  RefDocNum Int(11) Referenced Document Number
  StateUf nVarChar(2) State - UF
  PostDate Date(8) Posting Date
  CodDa VarChar(1) Collection Document default=1 [1=GNRE, 2=Other Document]
  NumDa nVarChar(20) Document Number
  CodAut nVarChar(30) Bank Authentication
  VlDa Num(19,6) Total Value
  VlDaSc Num(19,6) Total Value SC
  DtVcto Date(8) Due Date
  DtPgto Date(8) Payment Date
  CodAj nVarChar(10) ICMS Code
  DescCompAj nVarChar(120) Remarks
  BcIcms Num(19,6) ICMS Base Amount
  BcIcmsSc Num(19,6) ICMS Base Amount SC
  AliqIcms Num(19,6) ICMS Rate
  VlIcms Num(19,6) ICMS Value
  VlIcmsSc Num(19,6) ICMS Value SC
  VlOutros Num(19,6) Other Values
  CodAjApur nVarChar(10) Adjustment Code
  NumProc nVarChar(10) Procedure Docket Number
  IndProc VarChar(1) Procedure Docket Indicator
  Ser nVarChar(3) Fiscal Document Serial
  Sub nVarChar(3) Fiscal Document Subserial
  NumDoc Int(11) Fiscal Document Number
  DtDoc Date(8) Fiscal Document Issue Date
  CodMod nVarChar(6) Model Document Number
  CodPart nVarChar(15) BP Code ->OCRD
  CodRec nVarChar(15) Revenue Code
  GLAcct nVarChar(15) G/L Account Code ->OACT
  ItemCode nVarChar(50) Item Code ->OITM
  BPLId Int(11) Branch ID ->OBPL
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
  TransId Int(11) Transaction Number ->OJDT
