<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# INV15 - A/R Inv. - Drawn Dpm Applied
Module: Marketing Documents | 84 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]
