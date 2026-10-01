<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OQUE - Queue
Module: Service | 5 columns | ObjType: 194
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID
  descript nVarChar(200) Description
  manager Int(11) Queue Manager default=0 ->OUSR
  email nVarChar(200) Queue E-Mail
  inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
