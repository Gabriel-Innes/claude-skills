<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TXD1 - Tax Invoice Drafts - Rows
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BaseEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  BaseEntry Int(11) Base Document Internal ID
  LineNum Int(11) Row Number
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocType VarChar(1) Document Type default=I [I=Invoice, P=Payment, J=Journal Entry, C=Correction Invoice, R=Payment Request, L=Landed Cost]
  RefEntry1 Int(11) Ref.1 Document Key
  RefEntry2 Int(11) Ref. 2 Document Key
  ObjType Int(6) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  RefType Int(11) Ref. Object Type default=-1 [-1=, 13=A/R Invoice, 18=A/P Invoice, 30=Journal Entry, 24=Incoming Payment, 204=A/P Down Payment, 165=A/R Correction Invoice, 163=A/P Correction Invoice, 69=Landed Cost]
  EncryptIV nVarChar(100) Encrypt IV
