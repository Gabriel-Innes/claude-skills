<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XRXML - XLR company XML
Module: Reports | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Global, XmlId
Fields (name type(len) description [values] ->parent table):
  XmlId nVarChar(40) XmlId
  Xml Text(16) Xml
  Global Int(11) Global default=0
