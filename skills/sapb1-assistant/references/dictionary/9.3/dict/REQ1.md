<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# REQ1 - External System Call Request - Message List
Module: Service | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID
  MsgType VarChar(1) Message Type default=I [I=Information, W=Warning, E=Error]
  ErrCode nVarChar(3) Error Code
  MsgBody Text(16) Message Body
  Status VarChar(1) Message Status default=U [U=Unread, R=Read]
  MsgDate Date(8) Message Log Date
  MsgTime Int(11) Message Log Time
