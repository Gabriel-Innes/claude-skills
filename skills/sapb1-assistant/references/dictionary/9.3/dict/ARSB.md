<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARSB - Resource Groups - History
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInstanc, ResGrpCod
  GROUP_NAME U: logInstanc, ResGrpNam
Fields (name type(len) description [values] ->parent table):
  ResGrpCod Int(6) Number
  ResGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Object nVarChar(20) Object Type - History default=292
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History
  updateDate Date(8) Date of Update - History
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  CostName1 nVarChar(254) Resource Std Cost 1
  CostVal1 Num(19,6) Resource Std Cost 1
  CostName2 nVarChar(254) Resource Std Cost 2
  CostVal2 Num(19,6) Resource Std Cost 2
  CostName3 nVarChar(254) Resource Std Cost 3
  CostVal3 Num(19,6) Resource Std Cost 3
  CostName4 nVarChar(254) Resource Std Cost 4
  CostVal4 Num(19,6) Resource Std Cost 4
  CostName5 nVarChar(254) Resource Std Cost 5
  CostVal5 Num(19,6) Resource Std Cost 5
  CostName6 nVarChar(254) Resource Std Cost 2
  CostVal6 Num(19,6) Resource Std Cost 6
  CostName7 nVarChar(254) Resource Std Cost 7
  CostVal7 Num(19,6) Resource Std Cost 7
  CostName8 nVarChar(254) Resource Std Cost 8
  CostVal8 Num(19,6) Resource Std Cost 8
  CostName9 nVarChar(254) Resource Std Cost 9
  CostVal9 Num(19,6) Resource Std Cost 9
  CostName10 nVarChar(254) Resource Std Cost 10
  CostVal10 Num(19,6) Resource Std Cost 10
  ResUoM nVarChar(20) Resource Unit of Measurement
