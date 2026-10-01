<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODWZ - Dunning Wizard
Module: Marketing Documents | 44 columns | ObjType: 197
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId
  SECONDARY: WizardName
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  WizardName nVarChar(100) Wizard Name
  ToPayDate Date(8) To be paid by
  CreateDate Date(8) Creation Date
  Status VarChar(1) Wizard Status default=S [S=Saved Parameters, R=Saved Recommendations, E=Executed and Printed or Sent by E-Mail, O=Executed, Not Yet Printed or Sent by E-Mail, P=Partially Executed and Printed, T=Partially Executed, Not Yet Printed or Sent by E-Mail]
  DunLevel nVarChar(3) Dunning Level default=0 [0=All, 1=Level 1, 2=Level 2, 3=Level 3, 4=Level 4, 5=Level 5, 6=Level 6, 7=Level 7, 8=Level 8, 9=Level 9, 10=Level 10] ->ODUN
  CreditZero VarChar(1) Include BP with Credit default=N [Y=Yes, N=No]
  PayNoBased VarChar(1) Payment on Account default=Y [Y=Yes, N=No]
  CrdtNBased VarChar(1) Include Credit Not Based default=Y [Y=Yes, N=No]
  DunTime nVarChar(6) Dunning Time
  UserSign Int(6) User Signature ->OUSR
  FromDate Date(8) From Date Filter
  ToDate Date(8) Date To Filter
  ManualJEs VarChar(1) Include Manual JEs default=N [N=No, Y=Yes]
  DspOpnItms VarChar(1) Display Open Items default=N [Y=Yes, N=No]
  AllowNegLt VarChar(1) Allow Negative Dunning Letter default=N [Y=Yes, N=No]
  DunTerm nVarChar(25) Dunning Term default=-1 ->ODUT
  FrmDueDate Date(8) From Due Date Filter
  ToDueDate Date(8) To Due Date Filter
  UpToDate Date(8) Include Payments Up To
  InvPostDat Date(8) Invc. Posting Date
  InvDueDate Date(8) Invc. Due Date
  InvDocDate Date(8) Invc. Doc. Date
  Project nVarChar(20) Project
  OcrCode nVarChar(8) Costing Code
  OcrCode2 nVarChar(8) Costing Code 2
  OcrCode3 nVarChar(8) Costing Code 3
  OcrCode4 nVarChar(8) Costing Code 4
  OcrCode5 nVarChar(8) Costing Code 5
  InVatGroup nVarChar(8) Interest VAT Group
  InTaxCode nVarChar(8) Interest Tax Code
  FeVatGroup nVarChar(8) Fee VAT Group
  FeTaxCode nVarChar(8) Fee Tax Code
  VatPrcnt Num(19,6) VAT Percent
  AutoRmk VarChar(1) Auto Remark default=Y
  Remarks nVarChar(254) Remarks
  Series Int(11) Series default=0 ->NNM1
  BPLId Int(11) BPL ID Assigned to Invoice
  LocCode Int(11) Location Code
  VersionNum nVarChar(11) Version Number
  OvrDueOnly VarChar(1) BPs with Overdue Item Only default=N [Y=Yes, N=No]
  QuickDisp VarChar(1) Quick Display default=N [Y=Yes, N=No]
  OPNoBased VarChar(1) Include Outgoing Payments default=N [Y=Yes, N=No]
  CnsdVendor VarChar(1) Consider Connected Vendor default=N [Y=Yes, N=No]
