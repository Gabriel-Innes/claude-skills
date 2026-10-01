<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWD3 - WTax Codes Details for BP
Module: Business Partners | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
  BP U: LogInstanc, DetailType, DateFrom, KeyPart2, KeyPart1, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  KeyPart1 nVarChar(15) BP key part 1
  KeyPart2 nVarChar(15) BP key part 2
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  Rate Num(19,6) Currency Rate
  DetailType nVarChar(2) Type of Detailed Information [A=Allowed, S=Special Rate, E=Exemption]
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
