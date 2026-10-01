<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWHW - SEWHW
Module: General | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam, MachineNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(254) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber nVarChar(100) Customer Number
  OsType nVarChar(64) OS Type
  OsVersion nVarChar(32) OS Version
  VendorIden nVarChar(254) Vendor Identity
  CpuType nVarChar(32) CPU TYPE
  NumOfCPUs Int(11) Number Of CPUs
  PhysMemory Int(11) Physical Memory
  ServerFlag VarChar(1) Server Flag (Is Server?) [0=No, 1=Yes]
  TotDskSpac nVarChar(16) Total Disk Space
  FreDskSpac nVarChar(16) Free Disk Space
  UseDskSpac nVarChar(16) Used Disk Space
  CRRntmVer nVarChar(100) CR Runtime Version
  BOBIPltVer nVarChar(100) BO BI Platform Version
  CRDsgnrVer nVarChar(100) CR Designer Version
  CRIntPgVer nVarChar(100) CR Integration Package Version
  NETFrmVer nVarChar(254) .NET Framework Version
  NETFrmSDKV nVarChar(254) .NET Framework SDK Version
  MmrMngSett nVarChar(254) Memory Management Settings
  B1ClntPltf nVarChar(10) BusinessOne Client Platform
