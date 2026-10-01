<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ALR1 - Queue of messages to be sent
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, Code
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  LineId Int(11) Row Number
  NameFrom nVarChar(155) From
  AddrFrom nVarChar(100) Reply Address
  NameTo nVarChar(155) To
  IsSMS VarChar(1) SMS default=N [Y=Yes, N=No, F=Fax]
  Address nVarChar(100) Address
  Status VarChar(1) Status default=U [U=Not Sent, P=In Process, S=Sent]
  ObjType nVarChar(20) Object
  ObjCode nVarChar(50) Object Code
