<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCD - Service Code Table
Module: Service | 5 columns | ObjType: 254
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: County, ServiceCD
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  County Int(11) County Code ->OCNT
  ServiceCD nVarChar(15) Service Code
  Descrip nVarChar(70) Description
  Incomimg VarChar(1) Is Incomimg(Y/N) default=Y [Y=Incoming, N=Outgoing]
