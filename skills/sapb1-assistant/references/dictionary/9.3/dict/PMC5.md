<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PMC5 - Project Management Configuration - Activity Type
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ActTypeID
Fields (name type(len) description [values] ->parent table):
  ActTypeID Int(11) Activity Type No.
  ActType nVarChar(100) Activity Type
  LaborItem nVarChar(50) Labor Item No. ->OITM
  Chargeable VarChar(1) Chargeable default=Y [Y=Yes, N=No]
  Absence VarChar(1) Absence default=Y [Y=Yes, N=No]
  AbsenceID Int(11) Absence No.
