<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACP2 - Campaign - Items
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemType VarChar(1) Item Type [I=Items, L=Labor, T=Travel]
  ItemGrp nVarChar(20) Item Group
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
