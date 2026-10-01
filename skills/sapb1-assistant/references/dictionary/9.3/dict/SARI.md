<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SARI - add-ons table
Module: General | 41 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AddPlat, AddOnId, AName, NameSpace
Fields (name type(len) description [values] ->parent table):
  AddOnId Int(11) AddOn ID default=-1
  NameSpace nVarChar(20) Partner Name Space
  PName nVarChar(40) Partner Name
  AName nVarChar(40) AddOn Name
  EName nVarChar(128) AddOn Exe name
  CData nVarChar(80) Partner Contact Data
  AddOnChk nVarChar(32) AddOn Exe Check Sum
  InstName nVarChar(128) AddOn Installer Name
  InstChkSum nVarChar(32) AddOn Installer Check Sum
  ABinary Text(16) AddOn Installer Binary
  InstTime Int(11) Installation estimation time
  AddOnVer nVarChar(13) AddOn Version
  ForceFlag VarChar(1) AddOn Install force flag default=Y [Y=Yes, N=No]
  UnInstName nVarChar(128) AddOn Uninstaller Name
  UnInstChk nVarChar(32) AddOn UnInstaller Check Sum
  UnInstPar nVarChar(200) UnInstaller params
  InstIsUn VarChar(1) Is Installer is UnInstaller
  AGroup VarChar(1) AddOn Group
  IParams nVarChar(200) Installer Params
  UnInstTime Int(11) Uninstallation estimation time default=0
  AutoAssign VarChar(1) Automatic Company Assignment default=N
  Visible VarChar(1) AddOn is visible in AddOnAdmin default=Y [Y=Yes, visible, N=]
  SelfUpgrd VarChar(1) Don`t install/uninstal default=N [Y=Yes, don`t install/uninstall, N=No, perform install/uninstall]
  InstSil VarChar(1) Use silent mode in install default=N [Y=Silent mode supported, N=Silent mode not supported]
  UnInstSil VarChar(1) Use silent mode in uninstall default=N [Y=Silent mode supported, N=Silent mode not supported]
  UpgSil VarChar(1) Use silent mode in upgrade default=N [Y=Silent mode supported, N=Silent mode not supported]
  InstParF Text(16) Parameter files in install
  UnInstParF Text(16) Parameter files in uninstall
  UpgParF Text(16) Parameter files in upgrade
  InstPFChk nVarChar(32) Checksum of install param file
  UnInstPFCh nVarChar(32) Checksum of uninstall par file
  UpgPFChk nVarChar(32) Checksum of upgrade param file
  UpgName nVarChar(128) Addon upgrader name
  UpgTime Int(11) Estimated upgrade time default=0
  UpgParams nVarChar(200) Upgrader params
  AUpgrader Text(16) Addon upgrader binary
  UpgChkSum nVarChar(32) Addon upgrader checksum
  ABinary64 Text(16) AddOn Installer Binary (64bit)
  IsAdd64 VarChar(1) Is Addon Installer 64bit default=N
  AddPlat VarChar(1) Platform of addon installer default=N [N=x86, X=x64]
  ClientType VarChar(1) Client type supported by the addon default=W [W=Windows desktop, B=Browser access, A=All]
