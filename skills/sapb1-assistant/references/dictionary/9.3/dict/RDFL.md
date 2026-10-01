<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDFL - Document Standards
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, UserId, DoumntDode
  CODE: DoumntDode
Fields (name type(len) description [values] ->parent table):
  DoumntDode nVarChar(4) Code
  UserId Int(11) User Signature
  DfltReport nVarChar(8) Standard Report
  CardCode nVarChar(15) BP Code default=-1 ->OCRD
  DfltSeq Int(11) Standard Sequence
  TYPE VarChar(1) Type default=L [L=Layout, P=Print Sequence]
