<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AEC5 - List of Canceled Reconciliations for Actions in Electronic Communication
Module: Reports | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LogNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->ECM2
  LogNum Int(11) Log Number
  DocType Int(11) Document Type
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  UUID nVarChar(50) UUID
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Sec.
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Sec.
  LogInstanc Int(6) Log Instance
