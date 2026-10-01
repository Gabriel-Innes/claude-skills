<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DRF2 - Draft - Freight - Rows
Module: Marketing Documents | 58 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRF
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=112 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
