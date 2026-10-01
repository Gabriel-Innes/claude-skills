<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEFDW - EFD Wizard
Module: Reports | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  RunTime Int(6) Wizard Run Time
  Status VarChar(1) Status [S=Saved, E=Executed]
  UserSign Int(11) User Signature ->OUSR
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  Branch Int(11) Branch default=-2 ->OUBR
  ProfType nVarChar(2) Profile Type
  BlockC VarChar(1) Block C default=Y [Y=Yes, N=No]
  BlockD VarChar(1) Block D default=Y [Y=Yes, N=No]
  BlockE VarChar(1) Block E default=Y [Y=Yes, N=No]
  BlockH VarChar(1) Block H default=Y [Y=Yes, N=No]
  BlockG VarChar(1) Block G default=Y [Y=Yes, N=No]
  BlockI VarChar(1) Block I default=Y [Y=Yes, N=No]
  FlPurCode VarChar(1) File Purpose Code [0=Remessa do arquivo original, 1=Remessa do arquivo substituto]
  AccEmploye Int(11) Accountant Employee ->OCRD
  AccExtern nVarChar(15) Accountant External ->OHEM
  ItmFrom nVarChar(50) From Item
  ItmTo nVarChar(50) To Item
  ItmGroup Int(6) Item Group
  ItQryGroup nVarChar(250) Item Properties
  RptReason nVarChar(2) Reporting Reason default=01 [01=No final no período, 02=Na mudança de forma de tributação da mercadoria (ICMS), 03=Na solicitação da baixa cadastral, paralisação temporária e outras situações, 04=Na alteração de regime de pagamento – condição do contribuinte, 05=Por determinação dos fiscos]
