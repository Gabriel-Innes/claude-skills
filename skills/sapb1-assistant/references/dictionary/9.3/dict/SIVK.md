<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SIVK - IVL Vs OINM Keys
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: INMTransSe
  TRANSSEQ U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  RootID Int(11) Root ID
  TransNum Int(11) Transaction Number
  Instance Int(11) Instance default=0
  INMTransSe Int(11) INM_Transaction Sequence No.
