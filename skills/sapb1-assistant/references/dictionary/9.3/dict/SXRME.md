<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRME - XLR Members
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MemberId
  second U: Domain, Name, DomainType, RoleId
Fields (name type(len) description [values] ->parent table):
  MemberId Identity(11) MemberId
  RoleId nVarChar(16) RoleId
  DomainType Int(11) DomainType default=0
  MemberType Int(11) MemberType default=0
  Name nVarChar(244) Name
  Domain nVarChar(244) Domain
  Descriptio nVarChar(254) Description
