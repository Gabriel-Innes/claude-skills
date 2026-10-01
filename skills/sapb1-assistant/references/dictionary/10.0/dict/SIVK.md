<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SIVK - IVL Vs OINM Keys
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: INMTransSe
  TRANSSEQ U: TransSeq, LayerID
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  RootID Int(11) Root ID
  TransNum Int(11) Transaction Number
  Instance Int(11) Instance default=0
  INMTransSe Int(11) INM_Transaction Sequence No.
