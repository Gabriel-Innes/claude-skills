<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSI11 - A/R Corr. Inv. - Drawn Dpm Det
Module: Marketing Documents | 70 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSI
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=165 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Liable for Acquisition Tax default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]
