<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FAM1 - Fixed Asset Data Migration - Rows
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OFAM
  LineNum Int(11) Line Number
  ObjectType nVarChar(20) Object Type [1470000002=Account Determination, 1470000003=Depreciation Areas, 1470000004=Depreciation Type Pools, 1470000000=Depreciation Types, 1470000032=Asset Classes, 4=Items, 35=Item Numbering]
  ObjectCode nVarChar(20) Object Code
  ObjectName nVarChar(100) Object Name
  Status VarChar(1) Status default=Y [Y=Successful, N=Failed]
  Message nVarChar(254) Message
