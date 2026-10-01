<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODCI - Intrastat Configuration
Module: Administration | 14 columns
Indexes (name: columns; first = primary key; U = unique):
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
  TriangDeal nVarChar(2) Triangular Deal Type [11=Acquisitions intra-communautaires, 21=Livraison exon�r�e, 31=Facturations dans le cadre d�op�rations triangulaires]
