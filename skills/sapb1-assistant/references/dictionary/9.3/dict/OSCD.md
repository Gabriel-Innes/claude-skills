<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCD - Service Code Table
Module: Service | 5 columns | ObjType: 254
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: ServiceCD, County
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  County Int(11) County Code ->OCNT
  ServiceCD nVarChar(15) Service Code
  Descrip nVarChar(70) Description
  Incomimg VarChar(1) Is Incomimg(Y/N) default=Y [Y=Incoming, N=Outgoing]
