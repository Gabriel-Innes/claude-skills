<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MOBJ - MOBJ
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: guid
  TABLE_NAME U: tableName
  FA_OBJ_ID: fatheObjId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  tableName nVarChar(50) Table Name
  fatheObjId nVarChar(36) Father Object Id
  note nVarChar(254) Note
  popCol1 nVarChar(36) Popup Column 1
  objId Int(11) Internal Object Id
  objArrayId Int(11) Internal Object Array Number
  allowAdd VarChar(1) Allow Create
  allowUpd VarChar(1) Allow Update
  allowDel VarChar(1) Allow Remove
  noteSid Int(11)
  modeList VarChar(1) Listview Mode
  modeGet VarChar(1) Get by Key Mode
  isSystem VarChar(1) Is System Table
