<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HMM1 - Child Table of OHMM
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  UNIQUEVIEW U: ViewName
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Child No.
  ViewType VarChar(1) View Type [A=Attribute View, C=Calculation View, Y=Analytic View, P=Procedure]
  ViewName nVarChar(100) View Name
  MenuDesc nVarChar(254) Menu Description
  MenuEnable VarChar(1) Menu Enable [Y=Yes, N=No]
  IAEnable VarChar(1) Interactive Analysis Enable default=Y [Y=Yes, N=No]
  SLEnable VarChar(1) Enable Service Layer [Y=Yes, N=No]
  SLExpose VarChar(1) Expose Service Layer [Y=Yes, N=No]
