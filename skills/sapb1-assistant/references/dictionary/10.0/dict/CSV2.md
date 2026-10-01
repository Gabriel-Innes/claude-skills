<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CSV2 - A/R Correction Invoice Reversal - Freight - Rows
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, GroupNum
  LINE: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCSV
  LineNum Int(11) Row Number
  GroupNum Int(11) Expense Group
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  PaidSys Num(19,6) Paid in SC
  ObjType nVarChar(20) Object Type default=166 ->ADP1
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
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
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
  ExtTaxRate Num(19,6) External Tax Rate
  ExtTaxSum Num(19,6) External Tax Amount
  TaxAmtSrc VarChar(1) Tax Amount Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtTaxSumF Num(19,6) External Tax Amount (FC)
  ExtTaxSumS Num(19,6) External Tax Amount (SC)
  CUSplit VarChar(1) CU Split default=N [Y=Yes, N=No]
