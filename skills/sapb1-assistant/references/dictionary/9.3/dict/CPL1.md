<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CPL1 - Quick Copy - Instance Log
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->OCPL
  LogId Int(11) Log ID
  ObjectID nVarChar(20) Object ID
  Instance nVarChar(254) Instance Key
  ErrCode nVarChar(20) Error Code
  MessageId nVarChar(20) Message ID
  MessageDes nVarChar(254) Message Description
  InstName nVarChar(254) Instance Name
