<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XRDBV - XLR company DB version
Module: Reports | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DBObjVer
Fields (name type(len) description [values] ->parent table):
  DBObjVer nVarChar(20) IXDBObjectsVersion
  DBObjVerDe nVarChar(254) IXDBObjectsVersionDescr
  DBObjVerUp Date(8) IXDBObjectsVersionUpdated
  ParVer nVarChar(20) PartnerVersion
  ParVerDesc nVarChar(254) PartnerVersionDescr
  ParVerUpd Date(8) PartnerVersionUpdated
  Partner nVarChar(50) Partner
  PartnerDBV nVarChar(50) PartnerDBVersion
