<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEML - E-mail Log
Module: Reports | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  DocEntry Int(11) Doc Internal Number
  ObjType nVarChar(20) Object Type
  DocNum Int(11) Document Number
  EMailAddr nVarChar(100) E-Mail Address
  SendDate Date(8) Send Date
  SendTime Int(6) Time Sent
  USERID Int(6) User Signature ->OUSR
  U_NAME nVarChar(155) User Name
  Subject nVarChar(254) Subject
  Body Text(16) Body
  AtcEntry Int(11) Attachment Entry ->OATC
