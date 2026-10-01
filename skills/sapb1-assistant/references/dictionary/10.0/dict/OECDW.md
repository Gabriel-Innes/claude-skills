<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OECDW - ECD Wizard
Module: Reports | 40 columns
Indexes (name: columns; first = primary key; U = unique):
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
  DecenInd VarChar(1) Decentralized Indicator [C=Relat�rio Consolidado, H=Matriz - Descentralizado, B=Filial - Descentralizado]
  Branch Int(11) Branch default=-2 ->OUBR
  InstCode nVarChar(2) Institution Code [00=Nenhuma inscri��o em outras entidades, 01=Banco Central do Brasil, 02=Superintend�ncia de Seguros Privados (Susep), 03=Comiss�o de Valores Mobili�rios (CVM), 04=Ag�ncia Nacional de Transportes Terrestres (ANTT), AC=Secretaria da Fazenda do Estado do Acre, ou equivalente, AL=Secretaria da Fazenda de Alagoas, ou equivalente, AM=Secretaria da Fazenda de Amazonas, ou equivalente, AP=Secretaria da Fazenda do Amap�, ou equivalente, BA=Secretaria da Fazenda da Bahia, ou equivalente, DF=Secretaria da Fazenda do Distrito Federal, ou equivalente, CE=Secretaria da Fazenda do Cear� , ou equivalente, ES=Secretaria da Fazenda do Esp�rito Santo, ou equivalente, GO=Secretaria da Fazenda de Goi�s, ou equivalente, MA=Secretaria da Fazenda do Maranh�o, ou equivalente, MT=Secretaria da Fazenda do Mato Grosso, ou equivalente, MS=Secretaria da Fazenda do Mato Grosso do Sul, ou equivalente, MG=Secretaria da Fazenda de Minas Gerais, ou equivalente, PA=Secretaria da Fazenda do Par�, ou equivalente, PB=Secretaria da Fazenda da Para�ba, ou equivalente, PE=Secretaria da Fazenda de Pernambuco, ou equivalente, PR=Secretaria da Fazenda do Paran�, ou equivalente, PI=Secretaria da Fazenda do Piau�, ou equivalente, RJ=Secretaria da Fazenda do Rio de Janeiro, ou equivalente, RN=Secretaria da Fazenda do Rio Grande do Norte, ou equivalente, RS=Secretaria da Fazenda do Rio Grande do Sul, ou equivalente, RR=Secretaria da Fazenda de Roraima, ou equivalente, RO=Secretaria da Fazenda de Rond�nia, ou equivalente, SC=Secretaria da Fazenda de Santa Catarina, ou equivalente, SP=Secretaria da Fazenda de S�o Paulo, ou equivalente, SE=Secretaria da Fazenda de Sergipe, ou equivalente, TO=Secretaria da Fazenda de Tocantins, ou equivalente]
  EntIdCode nVarChar(32) Entry Identification Code
  SituatInd VarChar(1) Situation Indicator [0=Opening (abertura), 1=Split-up/ Split-off (Cis�o parcial/ cis�o total), 2=Merger (Fus�o), 3=Downstream merger/ Upstream merger (Incorpora��o), 4=Extinction (Extin��o), 5=Transformation (Transforma��o)]
  ReportType VarChar(1) Report Type [G=Livro Di�rio, R=Livro Di�rio com Escritura��o Resumida, A=Livro Di�rio Auxiliar ao Di�rio com Escritura��o Resumida, B=Livro Balancetes Di�rios e Balan�os (matriz)]
  CmpName nVarChar(100) Company Name
  CmpState nVarChar(2) Company State
  CmpCntCode nVarChar(10) Company County Code
  CmpCNPJ nVarChar(32) Company CNPJ
  CmpIE nVarChar(32) Company IE
  CmpCity nVarChar(32) Company City
  BrnState nVarChar(2) Branch State
  BrnCntCode nVarChar(10) Branch County Code
  BrnCNPJ nVarChar(32) Branch CNPJ
  BrnIE nVarChar(32) Branch IE
  BrnCity nVarChar(32) Branch City
  AccStIden VarChar(1) Account Statement Identification [1=Relat�rio apenas da empresa, 2=Relat�rio consolidado da matriz e filiais, afiliadas e empresas associadas]
  AccStRem Text(16) Account Statement Remark
  BookPurp nVarChar(80) Book Purpose
  JrnlNum Int(11) Journal Number
  PeriodSitu VarChar(1) Indicator of Initial Period Situation [0=Normal (In�cio no primeiro dia do ano), 1=Abertura, 2=Resultante de cis�o/fus�o ou remanescente de cis�o, ou realizou incorpora��o, 3=In�cio de obrigatoriedade da entrega da ECD no curso do ano calend�rio]
  BkPrpsInd VarChar(1) Bookkeeping Purpose Indicator [0=Original, 1=Substituta com NIRE, 2=Substituta sem NIRE, 3=Substituta com troca de NIRE]
  NIREind VarChar(1) NIRE Indicator [0=Empresa n�o possui registro na Junta Comercial (n�o possui NIRE), 1=Empresa possui registro na Junta Comercial (possui NIRE)]
  SubBkNIRE nVarChar(11) Substitute Bookkeeping NIRE
  SubBkHash nVarChar(40) Substitute Bookkeeping Hash
  BalanTemp Int(11) Balance Sheet Template ->OFRT
  PrLosTemp Int(11) Profit and Loss Statement Template ->OFRT
  BalanRefF VarChar(1) Balance Sheet Reference Fields default=N [Y=Yes, N=No]
  BalanUdfF VarChar(1) Balance Sheet User-Defined Fields default=N [Y=Yes, N=No]
  PrLosRefF VarChar(1) Profit and Loss Statement Reference Fields default=N [Y=Yes, N=No]
  PrLosUdfF VarChar(1) Profit and Loss Statement User-Defined Fields default=N [Y=Yes, N=No]
