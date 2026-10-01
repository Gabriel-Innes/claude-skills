<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HET1 - Employee Transfer Details
Module: Human Resources | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: empID, TransferID
Fields (name type(len) description [values] ->parent table):
  TransferID Int(11) Foreign Key to OHET ->OHET
  empID Int(11) Foreign Key to OHEM ->OHEM
  Transfered Date(8) Timestamp: Status "Sent"
  Status VarChar(1) Processing Status default=N [N=New, S=Sent, A=Accepted, E=Error]
  Comment Text(16) Any comments
  TransTime Int(6) Time When Status Is "Sent"
