<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OULA - EULA
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  Signed VarChar(1) Signed default=N [Y=Yes, N=No]
  Checked VarChar(1) Checked default=N [Y=Yes, N=No]
  EULAType VarChar(1) EULA Type default=P [E=Evaluation, P=Productive]
  Licensor nVarChar(100) Licensor
  Licensee nVarChar(100) Licensee
  InstallNo nVarChar(30) Installation Number
  Signer nVarChar(155) Signer
  UFunction nVarChar(100) Signer Function
  Username nVarChar(155) B1 User Name
  SignDate Date(8) Signing Date
  DocVer nVarChar(50) EULA Document Version
  EULADoc Text(16) EULA Document
  EULAFormat nVarChar(50) EULA Format default=TXT [PDF=PDF, TXT=TXT]
  Checksum nVarChar(150) EULA Record Checksum
