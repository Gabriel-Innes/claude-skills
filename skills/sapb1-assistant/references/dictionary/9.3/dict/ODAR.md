<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODAR - Data Archiving
Module: Administration | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  PeriodDate Date(8) Period Date
  UserSign Int(6) User Signature
  CreateDate Date(8) Archive Date
  CreateTime Int(6) Archive Time
  VersionNum Int(11) Version Number
  JEPerLen VarChar(1) Journal Entry Period Length default=A [A=Period, S=Sub-period, M=Month]
  JERef1 nVarChar(100) Journal Entry Reference 1
  JERef2 nVarChar(100) Journal Entry Reference 2
  JEMemo nVarChar(50) Journal Entry Remarks
  JEByProj VarChar(1) Journal Entry By Project default=N [Y=Yes, N=No]
  JEByProf VarChar(1) Journal Entry By Dist. Rule default=N [Y=Yes, N=No]
  INPerLen VarChar(1) Inventory Period Length default=A [A=Period, S=Sub-period, M=Month]
  INPriceSrc Int(6) Inventory Price Source ->OPLN
  INRef1 nVarChar(11) Inventory Reference 1
  INRef2 nVarChar(11) Inventory Reference 2
  INMemo nVarChar(254) Inventory Remarks
  JEByCurr VarChar(1) Journal Entry by Currency default=N [Y=Yes, N=No]
  JEByDIM2 VarChar(1) Journal Entry by Dimension 2 default=N [Y=Yes, N=No]
  JEByDIM3 VarChar(1) Journal Entry by Dimension 3 default=N [Y=Yes, N=No]
  JEByDIM4 VarChar(1) Journal Entry by Dimension 4 default=N [Y=Yes, N=No]
  JEByDIM5 VarChar(1) Journal Entry by Dimension 5 default=N [Y=Yes, N=No]
  DBReduc Num(19,6) DB Reduction (MB)
  DBReducPer Num(19,6) DB Reduction (%)
  TrandReduc Int(11) Transaction Reduction
  TranReducP Num(19,6) Transaction Reduction (%)
  INZeroPrc VarChar(1) Inventory Zero Price default=N [Y=Yes, N=No]
  TranRedArP Num(19,6) Trans. Reduc. Archived (%)
  DelNonReco VarChar(1) Delete nonreconciled OBNK lns default=N [Y=Yes, N=No]
  RunName nVarChar(50) Data Archive Run Name
  RODBGUID nVarChar(32) Readonly DB GUID for Archiving
  ArchMethod VarChar(1) Archive Method default=F [F=By Financial Period, B=By Business Partner]
