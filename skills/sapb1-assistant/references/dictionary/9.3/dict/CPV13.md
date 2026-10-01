<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CPV13 - A/P Correction Invoice Reversal Rows - Distributed Expenses
Module: Marketing Documents | 59 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCPV
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=164 ->ADP1
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
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
