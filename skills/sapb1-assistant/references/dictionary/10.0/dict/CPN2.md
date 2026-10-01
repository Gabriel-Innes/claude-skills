<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CPN2 - Campaign - Items
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CpnNo, CpnLineNum
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  ItemType VarChar(1) Item Type [I=Items, L=Labor, T=Travel]
  ItemGrp nVarChar(100) Item Group
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
