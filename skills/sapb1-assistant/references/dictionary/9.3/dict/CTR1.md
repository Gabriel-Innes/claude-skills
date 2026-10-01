<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CTR1 - Service Contract - Items
Module: Service | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, ContractID
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  Line Int(11) Row
  ManufSN nVarChar(36) Mfr Serial No.
  InternalSN nVarChar(36) Serial Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemGroup Int(6) Item Group ->OITB
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ItmGrpName nVarChar(20) Item Group Name
  InsID Int(11) Customer Equipment Card ID ->OINS
  TermDate Date(8) Termination Date
  LogInstanc Int(11) Log Instance - History
