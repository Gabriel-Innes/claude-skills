<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UIC5 - Customized Folders in Template
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemId, FormId, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  ItemId nVarChar(20) Item ID
  Left Int(6) Left
  Right Int(6) Right
  Top Int(6) Top
  Bottom Int(6) Bottom
  CurPan Int(6) Current Pane
  Caption nVarChar(50) Caption
  GroupItem nVarChar(20) Group Item
