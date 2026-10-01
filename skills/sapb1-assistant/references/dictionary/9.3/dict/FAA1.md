<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FAA1 - Asset Attributes - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, Code
  UNIQUE U: AttrID, Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->OFAA
  LineNum Int(11) Row Number
  AttrID Int(11) Attribute ID
  AttrName nVarChar(100) Attribute Name
  FieldType VarChar(1) Field Type [A=Text, N=Numeric, D=Date, S=Amount, P=Price, Q=Quantity]
  DefaultVal nVarChar(100) Default Value
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0
