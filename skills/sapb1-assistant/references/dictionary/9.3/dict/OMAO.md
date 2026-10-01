<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMAO - Mobile Add-On Setting
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(200) Name
  URL Text(16) Entry URL
  Type VarChar(1) Type default=M [M=Module, H=Home]
  Provider nVarChar(200) Provider
  ViewStyle VarChar(1) View Style default=P [P=Page - Universal, F=Full Screen - iPad, L=Landscape only - iPad]
  LogonMethd VarChar(1) Logon Method default=B [B=B1i Framework, S=Standard Logon, N=No Control]
  LogonPyld nVarChar(254) Logon Payload default=user={value1}&pwd={value2}
  Enable VarChar(1) Enable default=Y [Y=Yes, N=No]
  System VarChar(1) System default=N [N=No, Y=Yes]
  B1MobileAp VarChar(1) SAP Business One default=N [Y=Yes, N=No]
  B1SalesApp VarChar(1) SAP Business One Sales default=N [Y=Yes, N=No]
