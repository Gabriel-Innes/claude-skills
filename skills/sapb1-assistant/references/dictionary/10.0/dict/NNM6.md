<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NNM6 - Documents Numbering - Supplementary Code
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, PeriodType, StartDate, EndDate
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  PeriodType VarChar(1) Sequence Period Type [Y=Annually, M=Monthly, W=Weekly, P=Permanent]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Sequence Int(11) Current Sequence
  FormatStr nVarChar(254) Format String for Create Code
