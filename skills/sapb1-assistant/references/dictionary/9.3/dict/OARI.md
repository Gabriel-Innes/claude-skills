<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OARI - Add-On - Company Definitions
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AddOnID
Fields (name type(len) description [values] ->parent table):
  AddOnID Int(11) Add-On ID
  EGroup VarChar(1) Execution Group [A=Automatic, M=Manual, C=Critical]
  AStatus VarChar(1) Is add-on active? default=Y [Y=Yes, N=No]
  EventOrder Int(11) Add-on Event Order
  IsAdd64 VarChar(1) Add-On is 64 Bit default=N
  AddPlat VarChar(1) Add-On Installer Platform default=N [N=x86, X=x64, A=ARM]
