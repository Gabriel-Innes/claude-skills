<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MAP2 - Mapping Input and Output Relation
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CodeOut, CodeIn, MapID
Fields (name type(len) description [values] ->parent table):
  MapID Int(11) Mapping ID ->OMAP
  CodeIn Int(11) Input Code
  CodeOut Int(11) Output Code
  Sequence Int(11) Run Sequence
  Name nVarChar(20) Parameter Name
