<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCR - Special Ledger - Analytical Accounting Configuration Rules: Revenues & Expenses
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number
  RuleType Int(6) Rule Type Number default=1
  ParentID Int(6) Parent Rule ID ->OSCR
  Status VarChar(1) Rule Status
  Priority Int(6) Rule Priority default=100
  Name nVarChar(100) Rule Name
  CreateDate Date(8) Date of Rule Generation
  UpdateDate Date(8) Date of Rule Change
  UserSign Int(6) Rule Created By ->OUSR
  UserSign2 Int(6) Rule Changed By ->OUSR
  ExtCond nVarChar(200) Extended Special Data
