<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OHET - Object: HR Employee Transfer
Module: Human Resources | 7 columns | ObjType: 480000001
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransferID
Fields (name type(len) description [values] ->parent table):
  TransferID Int(11) Unique ID for Transfer
  TransStart Date(8) Transfer Start Date
  TransEnd Date(8) Timestamp if Status is "Sent"
  Status VarChar(1) Processing Status default=N [N=New, P=Processing, S=Sent, R=Received, A=Accepted, E=Error]
  Comment Text(16) Any comments
  StartTime Int(6) Transfer Start Time
  EndTime Int(6) Time When Status Is "Sent"
