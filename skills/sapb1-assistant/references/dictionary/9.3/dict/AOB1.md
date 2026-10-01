<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AOB1 - Sent Messages - User History
Module: Administration | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode, ObjType, AlertCode
  SEND_EM: SendEMail
  CONFIRMED2: Confirmed2
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  ObjType nVarChar(20) Object default=12 [-1=Random, 12=User, 11=Contact Person]
  ObjCode nVarChar(50) Object Code
  ObjName nVarChar(155) Name
  SendIntrnl VarChar(1) Sent Internally default=N [Y=Yes, N=No]
  Confirmed1 VarChar(1) Confirmation 1 default=N [Y=Yes, N=No]
  ConfDate1 Date(8) Approval Time 1
  ConfTime1 Int(6) Approval Time 1
  SendEMail VarChar(1) Sent E-mail default=N [Y=Yes, N=No]
  E_Mail nVarChar(100) E-Mail
  Confirmed2 VarChar(1) Confirmation 2 default=N [Y=Yes, N=No, E=Error]
  ConfDate2 Date(8) Authorization Period 2
  ConfTime2 Int(6) Authorization Period 2
  SendSMS VarChar(1) Sent SMS default=N [Y=Yes, N=No]
  PortNum nVarChar(50) Mobile Phone Number
  Confirmed3 VarChar(1) Confirmation 3 default=N [Y=Yes, N=No, E=Error]
  ConfDate3 Date(8) Approval Time 3
  ConfTime3 Int(6) Approval Time 3
  SendFax VarChar(1) Sent Fax default=N [Y=Yes, N=No]
  Fax nVarChar(20) Fax Number
  Confirmed4 VarChar(1) Confirmation 4 default=N [Y=Yes, N=No, E=Error]
  ConfDate4 Date(8) Confirmation Date 4
  ConfTime4 Int(6) Confirmation Time 4
