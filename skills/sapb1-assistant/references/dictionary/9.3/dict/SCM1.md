<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCM1 - Special Ledger - Analytical Accounting Configuration Rule Conditions: Material
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CondNum, RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCM
  CondNum Int(6) Condition Number
  Value1 nVarChar(200) Static Value
  Table1 nVarChar(20) Table Name
  Field1 nVarChar(200) Table Field Name
  Cond1 nVarChar(200) Value Selection Condition
  Group1 nVarChar(100) Group by Clause
  Relation nVarChar(50) Comparison Operator
  Value2 nVarChar(200) Static Value
  Table2 nVarChar(20) Table Name
  Field2 nVarChar(200) Table Field Name
  Cond2 nVarChar(200) Comparison Operator
  Group2 nVarChar(100) Group by Clause
  ExtCond1 nVarChar(200) Extended Special Data
  ExtCond2 nVarChar(200) Extended Special Data
