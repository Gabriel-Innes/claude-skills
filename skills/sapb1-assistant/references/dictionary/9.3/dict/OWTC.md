<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWTC - WTax Certificates
Module: Inventory and Production | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RctType nVarChar(20) Object Type [24=Incoming Payment, 46=Outgoing Payment]
  RctAbs Int(11) Receipt No.
  Jurisdict nVarChar(2) Jurisdiction
  WtaxType nVarChar(2) WTax Type [--=WTax Certificate, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate]
  WtAbsEntry Int(11) Internal Number
  DueDate Date(8) Due Date
  CerSeries Int(11) WTax Certificate Series
  Number Int(11) Number
  RefNumber nVarChar(20) Reference Number
  SumVatAmnt Num(19,6) Sum of VAT Amount
  SumDocTot Num(19,6) Sum of Doc. Total Amount
  SumBaseAmn Num(19,6) Sum of Base Amount
  SumAccumAm Num(19,6) Sum of Accumulated Amount
  SumPercpAm Num(19,6) Sum of Perception Amount
  PTICode nVarChar(5) POI Code
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator
  PTICodeRef nVarChar(20) POI Code Reference
