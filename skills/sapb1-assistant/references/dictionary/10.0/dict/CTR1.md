<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CTR1 - Service Contract - Items
Module: Service | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, Line
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  Line Int(11) Row
  ManufSN nVarChar(36) Mfr Serial No.
  InternalSN nVarChar(36) Serial Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  ItemGroup Int(6) Item Group ->OITB
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ItmGrpName nVarChar(20) Item Group Name
  InsID Int(11) Customer Equipment Card ID ->OINS
  TermDate Date(8) Termination Date
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV
