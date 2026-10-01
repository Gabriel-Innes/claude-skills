<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AOA4 - Blanket Agreement - Recurring Transactions
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, RcpEntry, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance default=0
