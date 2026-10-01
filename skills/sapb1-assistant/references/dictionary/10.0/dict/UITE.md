<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UITE - 
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, itemOrder
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  itemOrder Int(11) Item Order
  itemLabel nVarChar(254) Item Label
  itemType VarChar(1) Item Type
  columnId nVarChar(36) Column Id
  sonFormId nVarChar(36) Son Form Id
  note nVarChar(254) Note
  groupId nVarChar(36) Group Id
  locale nVarChar(254) Localization Flag
  locVisible nVarChar(254) Visible Settings
  labelSid Int(11) Item Name String Id
  groupIcon Int(11) Group Icon Index
  groupType VarChar(1) Group Type
  actionId nVarChar(36) ->MACT
  linkButton VarChar(1) Show Link Button default=N
  mVisible VarChar(1) Mobile Visibility
