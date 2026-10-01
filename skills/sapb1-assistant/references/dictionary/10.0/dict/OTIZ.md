<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTIZ - Company Time Zone
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Index
  ChangeDate nVarChar(50) Date of Change
  TimeZone Int(11) Index of Time Zone
  ActiveDst VarChar(1) Indicator: DST Active or Not default=U [Y=, N=, U=]
  offset Int(11) Offset
