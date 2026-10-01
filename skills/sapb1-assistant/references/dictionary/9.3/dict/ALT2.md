<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ALT2 - Alerts - Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupId, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  GroupId Int(6) Group Id ->OUGR
  SendIntrnl VarChar(1) Send Internally default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]
