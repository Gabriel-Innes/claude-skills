<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCN2 - Tracking Note - Brokers
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  CardCode nVarChar(15) BP Code ->OCRD
  AgrNo Int(11) Blanket Agreement Number ->OOAT
