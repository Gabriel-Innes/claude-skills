<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPRO - Property Object
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE_NAME U: Name, Code, MapID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Property ID
  MapID Int(11) Mapping ID ->OMAP
  Code Int(11) Input/Output Code
  Type nVarChar(6) Property Type default=Strin [Strin=String, XML=XML, String=]
  Name nVarChar(50) Property Name
  IsBlob VarChar(1) Is BLOB Type [Y=, N=]
  TValue nVarChar(250) Text Value
  BValue Text(16) BLOB Value
  Encoding nVarChar(20) Encoding [base64=, =]
