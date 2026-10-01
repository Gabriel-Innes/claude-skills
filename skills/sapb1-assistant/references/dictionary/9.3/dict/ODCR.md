<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODCR - Checking Rule
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RuleCode
Fields (name type(len) description [values] ->parent table):
  RuleCode nVarChar(2) Checking Rule Code
  RuleDesc nVarChar(100) Checking Rule Description
  PastRcp VarChar(1) Include Past Plan Receipts default=Y [Y=Yes, N=No]
  AutoATP VarChar(1) ATP Check Automatically default=Y [Y=Yes, N=No]
  SLDUncfm VarChar(1) Schedule for Unconfirmed Qty default=Y [Y=Yes, N=No]
  AllowUncfm VarChar(1) Allow Unconfirmed Quantity default=N [Y=Yes, N=No]
  CmltStrtg VarChar(1) Cumulation Strategy default=R [R=Required Qty on Creation; Confirmed Qty on Change, C=Confirmed Qty on Creation and Change]
  DeliStrtg VarChar(1) Delivery Strategy default=D [D=Delivery Proposal, O=One-Time Delivery, C=Complete Delivery]
  MaxPrpsls Int(11) Max. No. of Proposals default=9
  validFor VarChar(1) Active default=N
  validFrom nVarChar(8) Active From
  validTo nVarChar(8) Active To
  frozenFor VarChar(1) Inactive default=N
  frozenFrom nVarChar(8) Inactive From
  frozenTo nVarChar(8) Inactive To
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
