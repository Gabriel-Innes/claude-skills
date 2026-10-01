<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCMF - Common Functions of Fiori-Style Cockpit
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, ItemIndex
  INDEX: ItemIndex
Fields (name type(len) description [values] ->parent table):
  UserID Int(6) User ID ->OUSR
  ItemIndex Int(11) Common Function Item Index
  MenuUID nVarChar(50) Menu UID
  GroupID Int(6) Authorization Group ID ->OUGR
  MenuType VarChar(1) Menu Type default=S [S=System Menu, O=Menu of User Defined Object, Q=Menu of User Defined Query, A=Menu added by UI API, N=Menu added by Unknown Source]
  CmfMenuId nVarChar(50) Common Function Menu ID
