<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCFG - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: B1iEnabled
Fields (name type(len) description [values] ->parent table):
  PFlags Text(16) Protect settings flags
  B1iEnabled VarChar(1) Is B1i enabled? default=Y [Y=Yes, N=No]
  LstBckupTo Int(11) Last backup Timeout default=60
  SkinStyle VarChar(1) Skin Style default=H
  IsPALInit VarChar(1) Is PAL Initialize or Not default=N
  PANAVer Int(11) Pervasive Version default=0
