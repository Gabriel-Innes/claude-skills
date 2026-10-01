<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MCOL - MCOL
Module: General | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lineNum, fatherId
  GUID U: guid
  COL_NAME: colName, fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Object Id
  lineNum Int(11) Line Number
  colName nVarChar(50) Column Name
  colType VarChar(1) Column Type
  colSize Int(11) Column Size
  linkObjId nVarChar(36) Link to Object Id
  note nVarChar(254) Note
  defaultVal nVarChar(254) Default Value
  editSize Int(11) Edit Size
  mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  editType VarChar(1) Edit Type
  rdOnlyAdd VarChar(1) Read Only for Add Mode
  rdOnlyUpd VarChar(1) Read Only for Update Mode
  supresZero VarChar(1) Supress Zero
  locale nVarChar(254) Localization
  onListEvt VarChar(1) On List Event
  onChgEvt VarChar(1) On Change Event
  noteSid Int(11) String Id
  width Int(11) Width
  noteList nVarChar(254) Listview Note
  noteLstSid Int(11) String id of list view note
  fieldType Int(11) Field Type
  diType VarChar(1) DI API Fields
  diBatType VarChar(1) DI Batch Mode Type
