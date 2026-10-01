<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD9 - OCRD Extension
Module: Business Partners | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  ISTransMod Int(11) Intrastat Transport Mode ->ODCI
  ISIncoterm Int(11) Intrastat Incoterms ->ODCI
  ISState Int(11) Intrastat State ->ODCI
  ISNatTrans Int(11) Intrastat Nature of Trans. ->ODCI
  ISStatProc Int(11) Intrastat Statistical Proc. ->ODCI
  ISCustProc Int(11) Intrastat Customs Proc. ->ODCI
  ISCRYOrig nVarChar(3) Intrastat Country Origin ->OCRY
  ISPort Int(11) Intrastat Port of Entry/Exit ->ODCI
  ISDomFrgld VarChar(1) Intrastat Domestic/Foreign ID
  ISRelevant VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
