<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UFRM - UFRM
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  FATHER_ID: fatherId
  OBJECT_ID U: objId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  formName nVarChar(254) Form Name
  objId nVarChar(36) Object Id
  frmNameSid Int(11) Form Name String Index
