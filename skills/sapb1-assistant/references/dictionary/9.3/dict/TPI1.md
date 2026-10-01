<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TPI1 - Purchase Tax Invoice - Rows
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, BaseEntry
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID ->OTPI
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, D=Down Payment, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref.1 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
