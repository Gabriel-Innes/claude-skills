<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPOS - POS Master Data
Module: Administration | 5 columns | ObjType: 541
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EquipNo
Fields (name type(len) description [values] ->parent table):
  EquipNo nVarChar(20) Equipment No.
  Model nVarChar(20) Model
  ManufSN nVarChar(21) Manufacturer Serial No.
  RegNo Int(6) Register No.
  NFModel nVarChar(6) Fiscal Document Model ->ONFM
