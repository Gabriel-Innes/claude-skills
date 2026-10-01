<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PHA8 - Project Management - Summary
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  PhBudget Num(19,6) Subproject Budget
  OpenAmtAP Num(19,6) Open Amount (A/P)
  InvoicedAP Num(19,6) Invoiced (A/P)
  TotalAP Num(19,6) Total (A/P)
  TotVarAP Num(19,6) Total Variance (A/P)
  VarPercAP Num(19,6) Variance Percentage (A/P)
  AccPhBudg Num(19,6) Accumulated Subproject Budget
  AccOpAmAP Num(19,6) Accumulated Open Amount (A/P)
  AccInvAP Num(19,6) Accumulated Invoiced (A/P)
  AccTotAP Num(19,6) Accumulated Total (A/P)
  AccTVarAP Num(19,6) Accumulated Total Variance (A/P)
  AccVPercAP Num(19,6) Accumulated Variance Percentage (A/P)
  PoPhAmt Num(19,6) Potential Subproject Amount
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvoicedAR Num(19,6) Invoiced (A/R)
  TotalAR Num(19,6) Total (A/R)
  TotVarAR Num(19,6) Total Variance (A/R)
  VarPercAR Num(19,6) Variance Percentage (A/R)
  AccPoPhAmt Num(19,6) Accumulated Potential Subproject Amount
  AccOpAmAR Num(19,6) Accumulated Open Amount (A/R)
  AccInvAR Num(19,6) Accumulated Invoiced (A/R)
  AccTotAR Num(19,6) Accumulated Total (A/R)
  AccTVarAR Num(19,6) Accumulated Total Variance (A/R)
  AccVPercAR Num(19,6) Accumulated Variance Percentage (A/R)
  ActICCost Num(19,6) Actual Item Component Cost
  ActRCCost Num(19,6) Actual Resource Component Cost
  ActAddCost Num(19,6) Actual Additional Cost
  ActPrCost Num(19,6) Actual Product Cost
  ActBPrCost Num(19,6) Actual By-Product Cost
  TotalVar Num(19,6) Total Variance
  DueDate Date(8) Due Date
  CloseDate Date(8) Actual Closing Date
  Overdue Int(11) Overdue default=0
  Valid VarChar(1) If the calculated data is valid default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
