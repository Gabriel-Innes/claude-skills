<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EPASM - EPASM
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AsmName
Fields (name type(len) description [values] ->parent table):
  AsmName nVarChar(100) plugin assembly name
  PkgName nVarChar(50) FK to the EPPKG table
  AsmType nVarChar(20) Ttypes contained in assembly default=All [Messages=Only IMessage contained in the assembly, Processors=Only IMessageProcessor contained in the assembly, All=All types are in the assembly]
