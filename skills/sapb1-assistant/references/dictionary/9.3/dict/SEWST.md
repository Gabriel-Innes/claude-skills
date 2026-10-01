<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWST - SEWST
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(30) Name
  U_SentDate nVarChar(10) Sent Date
  U_SentTime nVarChar(8) Sent Time
  U_UserID nVarChar(8) User ID
  U_RCode nVarChar(3) Return Code
  U_RInfo nVarChar(254) Return info
  U_AutoSent VarChar(1) Is schedule sent or manual
