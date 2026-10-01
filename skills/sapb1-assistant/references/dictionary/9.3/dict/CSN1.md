<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSN1 - Certificate Series - Series
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series, AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OCSN
  Series Int(6) Series
  BeginStr nVarChar(20) Prefix
  InitialNum Int(11) First No. default=1
  NextNum Int(11) Next No. default=1
  LastNum Int(11) Last No.
