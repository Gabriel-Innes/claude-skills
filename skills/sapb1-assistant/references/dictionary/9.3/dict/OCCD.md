<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCCD - Cargo Customs Declaration Numbers
Module: Administration | 9 columns | ObjType: 283
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CCDNum
Fields (name type(len) description [values] ->parent table):
  CCDNum nVarChar(40) CCD Number
  Date Date(8) Date
  CustBroker nVarChar(15) Customs Broker
  DocNum nVarChar(20) Imp./Exp. Document Number
  DocDate Date(8) Imp./Exp. Document Date
  SupNum nVarChar(20) Supply Agreement Number
  SupDate Date(8) Supply Agreement Date
  CustTerm nVarChar(15) Customs Terminal
  PayKey nVarChar(4) Payment Internal ID
