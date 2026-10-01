<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CTNS - Transaction Notification Setting
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  OBJECT_ID U: ObjectId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal No.
  ObjectId nVarChar(30) Business Object ID
  EnableAsyN VarChar(1) Enable async notification default=N [Y=Yes, N=No]
  EnableTn VarChar(1) Transaction Notification default=Y [Y=Yes, N=No]
  EnablePTn VarChar(1) Post Transaction Notification default=Y [Y=Yes, N=No]
