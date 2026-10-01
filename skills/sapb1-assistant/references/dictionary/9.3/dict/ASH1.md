<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASH1 - Project Management Time Sheet - Rows - History
Module: General | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  Date Date(8) Date
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Workorder Int(11) Workorder Doc. Entry ->OWOR
  WorAbs Int(11) Workorder Abs. Entry
  ServCall Int(11) Service Call ID ->OSCL
  CostCenter nVarChar(8) Cost Center
  FiProject nVarChar(20) Financial Project
  Location Int(11) Location
  GPSData nVarChar(50) GPS Data
  Branch Int(11) Branch ID ->OBPL
  Break Int(11) Break
  NonBillTm Int(11) Nonbillable Time
  EffectTm Int(11) Effective Time
  BillableTm Int(11) Billable Time
  FullDay VarChar(1) Full Day default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ProjectID Int(11) Project or Subproject ID
  Subproject Int(11) Subproject ID
  StageID Int(11) Stage ID
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
