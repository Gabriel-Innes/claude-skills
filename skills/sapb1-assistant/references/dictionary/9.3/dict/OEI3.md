<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEI3 - OEI - Freight
Module: Marketing Documents | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOCUMENT: BaseAbsEnt, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OOEI
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=140000009 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
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
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)
