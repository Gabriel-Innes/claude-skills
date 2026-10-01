<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OGPA - Gross Profit Adjustment
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Name nVarChar(100) Gross Profit Adjustment Name
  CreateDate Date(8) Create Date
  UserSign Int(6) User Signature
  Status VarChar(1) Status [R=Saved Recommendations, S=Simulation, E=Executed, P=Saved Parameters]
  Remarks nVarChar(254) Description
  WizType VarChar(1) Wizard Type default=A [A=Gross Profit Adjustment Wizard, R=Production Cost Recalculation Wizard]
  nGPAdj Int(11) Number of Gross Profits Recalculated
  nPCAdj Int(11) Number of Product Costs Recalculated
  nGPFail Int(11) Number of Gross Profit Recalculations Failed
  nPCFail Int(11) Number of Failed Product Cost Recalculations
  nJECreate Int(11) Number of Journal Entries Created
  nMRVCreate Int(11) Number of MRV Created
