<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTD3 - WTax Codes Details for BP
Module: Business Partners | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
  BP U: WTCode, KeyPart1, KeyPart2, DateFrom, DetailType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  KeyPart1 nVarChar(15) BP Key Part 1
  KeyPart2 nVarChar(15) BP Key Part 2
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  Rate Num(19,6) Currency Rate
  DetailType nVarChar(2) Type of Detailed Information [A=Allowed, S=Special Rate, E=Exemption]
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, S=Service Layer, W=Web Client, P=Partner Implementation, U=UI Reproweb Autocomplete]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
