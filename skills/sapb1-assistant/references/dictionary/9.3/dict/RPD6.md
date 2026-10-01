<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RPD6 - Goods Return - Installments
Module: Marketing Documents | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InstlmntID, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORPD
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=21 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)
