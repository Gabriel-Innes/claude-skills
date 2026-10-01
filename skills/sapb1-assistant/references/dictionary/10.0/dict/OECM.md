<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OECM - Electronic Communication Types or Protocols
Module: Reports | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Communication Type or Protocol
  Descr nVarChar(200) Description
  LogInstanc Int(6) Log Instance
  UIOrder Int(6) UI Order
  StrIndex Int(6) String Index
  IsActive VarChar(1) Activation of Communication Type or Protocol default=N [Y=Yes, N=No]
  LHost nVarChar(254) Background Process Client Machine Name
  LPID Int(11) Background Process Client Process ID
  LTimeout nVarChar(14) Validity Time Stamp of Background Process Client Session
  RHost nVarChar(254) Machine Name Requesting Control of Background eDoc Processing
  RPID Int(11) Process ID Requesting Control of Background eDoc Processing
  RTimeout nVarChar(14) Validity Time Stamp of Background Process Client Request
