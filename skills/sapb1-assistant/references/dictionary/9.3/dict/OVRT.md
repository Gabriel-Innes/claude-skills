<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OVRT - Tax Invoice Report
Module: Marketing Documents | 22 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TxInvRptNo
Fields (name type(len) description [values] ->parent table):
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Create Date
  SupBPLId Int(11) Supplier BPL ID
  CardCode nVarChar(15) Receipt BP Code
  BaseAmt Num(19,6) Total Base Amount(LC)
  BlankNo Int(11) Blank Before Total Base Amount
  TaxAmt Num(19,6) Total Tax Amount(LC)
  Total Num(19,6) Total Base + Total Tax
  BPAddress nVarChar(254) Customer Pay to Address
  version nVarChar(50) Report Generation Version
  ReportType Int(11) VAT: Tax Report Type ID ->OKRT
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site default=-1 ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  Remarks nVarChar(254) Remarks
  OriNTSAppr nVarChar(50) Original NTS Approval Number
  CardName nVarChar(100) Receipt BP Code
  RptStatus VarChar(1) Tax Invoice Report Status default=S [S=Saved, C=Canceled, R=Reversed]
  OriTaxInvN nVarChar(10) Original Tax Invoice Number
  TxInvPrint VarChar(1) Tax Invoice Report Print Type default=I [A=Aggregated, I=Individual]
  Canceled VarChar(1) Tax Invoice Report is Canceled or Not default=N [Y=Yes, N=No]
