<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODCI - Intrastat Configuration
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CONF_ID: ConfID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Configuration Entry ID
  ConfType VarChar(1) Configuration Type [M=Additional Measurement Unit, C=Commodity Codes, P=Custom Procedures, I=Incoterms, N=Nature of Transactions, E=Ports of Entry and Exit, R=Service Codes, S=Statistical Procedures, T=Transport Modes, G=Regions]
  Code nVarChar(50) Code
  Descr nVarChar(254) Description
  PrcstVal Num(19,6) Percentage Value
  SuppUnit Int(11) Supplementary Unit ->ODCI
  Export VarChar(1) Valid for Export default=Y [Y=Yes, N=No]
  Import VarChar(1) Valid for Import default=Y [Y=Yes, N=No]
  StatCode nVarChar(2) Statistical Code
  DateFrom Date(8) Valid From
  DateTo Date(8) Valid To
  TextVal nVarChar(12) Text Value
  ConfID nVarChar(254) Configuration ID
