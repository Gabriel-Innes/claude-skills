<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# CRM activities module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## CALLATTEMP (CTT) - Call attempt
Keys (first = PK; D = duplicates allowed): CTT0 CTTNUM; CTT1 CTTCMP (D); CTT2 CTTCCN (D)
Fields:
  AUUID AUUID Single identifier
  CLLNUM VCR Short code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CTT]CREUSR (AUTILIS) !Other
  CTTCCN AIN Contact (relationship) -> [AIN]AIN0 =[CTT]CTTCCN (CONTACTCRM) !Block
  CTTCMP BPR Company -> [BPR]BPR0 =[CTT]CTTCMP (BPARTNER) !Block
  CTTDAT D Attempt date
  CTTNUM VCR Attempt code
  CTTREP REP Sales rep -> [REP]REP0 =[CTT]CTTREP (SALESREP) !Block
  HOUCRE HM Creation time
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CTT]UPDUSR (AUTILIS) !Other

## CMARKETING (CMG) - Marketing campaign
Keys (first = PK; D = duplicates allowed): CMG0 NUM; CMG1 DATSTR (D)
Fields:
  AUUID AUUID Single identifier
  BUD MD1 Budget
  CLO M*4 Closed [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[CMG]CUR (TABCUR) !Block
  DATEND D End date
  DATSTR D Start date
  DES CLX Description
  FCY FCY Site -> [FCY]FCY0 =[CMG]FCY (FACILITY) !Block
  NUM VCR Code
  NUMFULOBJ CLC Chrono txt file
  OBJFLG C*2 Flag text file
  TTR DCO Description
  TYPFULOBJ CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CORREP (COP) - Representative in charge
Keys (first = PK; D = duplicates allowed): COP0 COPREP+COPNUM
Fields:
  AUUID AUUID Single identifier
  COPNUM VCR Correspondant code
  COPREP REP Sales rep code -> [REP]REP0 =[COP]COPREP (SALESREP) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CORRESPOND (COR) - Outlook contact
Keys (first = PK; D = duplicates allowed): COR0 CORNUM
Fields:
  AUUID AUUID Single identifier
  BIR D Date of birth
  BPRLIB CLX Company description
  BPRNUM BPR BP -> [BPR]BPR0 =[COR]BPRNUM (BPARTNER) !Other
  CNTNUM AIN Code -> [AIN]AIN0 =[COR]CNTNUM (CONTACTCRM) !Delete
  CORNUM VCR Sequence no.
  CORTYP AOB Type -> [AOB]ABREV =[COR]CORTYP (AOBJET) !Block
  CPYADD ADL(3) Address
  CPYBPADES DES Description
  CPYBPANUM ADR Code
  CPYBPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CPYCRY CRY Country -> [TCY]TCY0 =[COR]CPYCRY (TABCOUNTRY) !Block
  CPYCRYNAM NCY Country name
  CPYCTY CTY City
  CPYEML MAI Email
  CPYFAX TEL Fax
  CPYMOB TEL Mobile phone
  CPYSAT SAT County
  CPYTEL TEL Telephone
  CPYZIP POS Postal code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSP ADI Category -> [ADI]CODE =907;CSP (ATABDIV) !Block
  FNA FNA First name
  FNC M*15 Function [menu 233: 1=Managing Director,2=Sales Manager,3=Technical Manager,4=Financial and Legal Manager,5=Site Manager,6=Company manager,7=Manager,8=Staff manager,9=Accountant,10=Other,11=Liquidator,12=Official receiver]
  FNCLIB A*50 Function description
  HOMADD ADL(3) Address
  HOMCRY CRY Country -> [TCY]TCY0 =[COR]HOMCRY (TABCOUNTRY) !Block
  HOMCRYNAM NCY Country name
  HOMCTY CTY City
  HOMEML MAI Email
  HOMFAX TEL Fax
  HOMMOB TEL Mobile phone
  HOMSAT SAT County
  HOMTEL TEL Telephone
  HOMZIP POS Postal code
  LAN LAN Language -> [TLA]TLA0 =[COR]LAN (TABLAN) !Block
  LNA NAM Last name
  MSS ADI Role -> [ADI]CODE =414;MSS (ATABDIV) !Block
  SRV DES Department
  TTL M*15 Title [menu 941: 1=Mr,2=Mrs,3=Ms]
  TTR DES Title
  UPDBPRNUM C*1 Change BP code
  UPDCNTNUM C*1 Change inter code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CRMCLOB (CRC) - CRM text file
Keys (first = PK; D = duplicates allowed): CRC0 CRCNUM
Fields:
  AUUID AUUID Single identifier
  CRCAINNUM AIN Contact (rel.) code -> [AIN]AIN0 =[CRC]CRCAINNUM (CONTACTCRM) !Block
  CRCBPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CRCBPRNUM BPR BP code -> [BPR]BPR0 =[CRC]CRCBPRNUM (BPARTNER) !Block
  CRCCLOB HDC Text file (clob)
  CRCCORNUM VCR Correspondant code
  CRCNUM VCR Sequence no.
  CRCREP BPR Sales rep -> [BPR]BPR0 =[CRC]CRCREP (BPARTNER) !Block
  CRCTYP ABR Type
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CRMTRS (CTR) - Entry transaction CRM
Keys (first = PK; D = duplicates allowed): CTR0 CTRTYP+CTRNUM; CTR1 CTRNUM+CTRTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[CTR]ACSCOD (ACCCOD) !Block
  AUUID AUUID Single identifier
  BLOCINVI A*15(15) Hidden block
  CLELIS ANX(8) Index
  COLFIXNAM A*25(10) Fixed column grid
  COLFIXVAL C*1(10) Fix.col. grid value
  COULIS M*4(8) Numbering active [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRDES DES Description
  CTRNUM TRS Transaction
  CTRTYP M*15 Transaction type [menu 3050: 1=CRM activities planning calendar]
  CTRTYPCAR A*2 Alpha no.
  DERLU M*4 Last read [menu 1: 1=No,2=Yes]
  DESAXX AX3 Description
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[CTR]DOCNAM (AREPORT) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FIRLIS M*4 In first position [menu 1: 1=No,2=Yes]
  FLTLIS A*215(8) Filter
  GFY AGF Group -> [AGF]AGF0 =[CTR]GFY (AGRPFCY) !Block
  NPRFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  NPRNAM ARP Document -> [ARP]ARP0 =[CTR]NPRNAM (AREPORT) !Block
  OBJLIS AOB(8) Object -> [AOB]ABREV =[CTR]OBJLIS (AOBJET) !Block
  ONGINVISI A*15(10) Hidden tab
  ONGLETACT AMK Active tab -> [AMK]CODMSK =[CTR]ONGLETACT (AMSK) !Block
  ORDLIS M*10(8) Sign [menu 90: 1=Ascending,2=Descending]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CRMTRSVAL (CTV) - CRM values entry transaction
Keys (first = PK; D = duplicates allowed): CTV0 CTRTYP+CTRNUM; CTV1 CTRNUM+CTRTYP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM TRS Transaction
  CTRTYP M*15 Transaction type [menu 3050: 1=CRM activities planning calendar]
  FIENAM A*24(90) Fields
  FIEVAL A*10(90) Values
  ININAM A*24(20) Field name to assign
  INIVAL A*10(20) Value to assign
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FIEDIC (FID) - Criteria of target
Keys (first = PK; D = duplicates allowed): FID0 CRITAB+CAT
Fields:
  AUUID AUUID Single identifier
  CAT ADI Category -> [ADI]CODE =452;CAT (ATABDIV) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FID]CREUSR (AUTILIS) !Other
  CRITAB ATB Table -> [ATB]CODFIC =[FID]CRITAB (ATABLE) !Block
  CRITABAXX AXX Table title
  STD C*4 Standard
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FID]UPDUSR (AUTILIS) !Other

## FIEDICFIE (FDF) - Target criteria fields
Keys (first = PK; D = duplicates allowed): FDF0 CRITAB+SELCRIFIE+CAT
Fields:
  AUUID AUUID Single identifier
  CAT ADI Category -> [ADI]CODE =452;CAT (ATABDIV) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FDF]CREUSR (AUTILIS) !Other
  CRITAB ATB Table -> [ATB]CODFIC =[FDF]CRITAB (ATABLE) !Block
  SELCRIAXX AXX Description
  SELCRIFIE A*17 Field
  SELCRIFLG M*4 Status [menu 1: 1=No,2=Yes]
  SELCRISRT L*8 Order no.
  STD C*4 Standard
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FDF]UPDUSR (AUTILIS) !Other

## HD8CLOB (HD8) - Clobs lead
Keys (first = PK; D = duplicates allowed): HD80 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD8 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD8]CREUSR (AUTILIS) !Other
  NUM CLC Sequence no.
  TYP CLT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD8]UPDUSR (AUTILIS) !Other

## LEAD (LDS) - Leads
Keys (first = PK; D = duplicates allowed): LDS0 PSTNUM; LDS2 PSTTYP+PSTNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Default address
  BUS ADI Business -> [ADI]CODE =425;BUS (ATABDIV) !Block
  CPYCAF MD1 Business result
  CPYCRN CRT Site registration number
  CPYCRY CRY Country -> [TCY]TCY0 =[LDS]CPYCRY (TABCOUNTRY) !Block
  CPYEFF A*4 Headcount
  CPYNAF NAF SIC code
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[LDS]CUR (TABCUR) !Block
  DATFIRCNT D First contact date
  FNC M*15 Function [menu 233: 1=Managing Director,2=Sales Manager,3=Technical Manager,4=Financial and Legal Manager,5=Site Manager,6=Company manager,7=Manager,8=Staff manager,9=Accountant,10=Other,11=Liquidator,12=Official receiver]
  FNCLIB A*50 Function description
  MSS ADI Role -> [ADI]CODE =414;MSS (ATABDIV) !Block
  NUMCLOB CLC Chrono txt file
  ORIPPT ADI Source -> [ADI]CODE =413;ORIPPT (ATABDIV) !Block
  PSTITR M*15 Interest [menu 3041: 1=Low,2=Medium,3=Strong]
  PSTNUM LDS Code -> [LDS]LDS0 =[LDS]PSTNUM (LEAD) !Delete
  PSTORI M*15 Source [menu 3042: 1=None,2=Mass mailing,3=Call campaign,4=Trade show,5=Media campaign,6=Marketing campaign]
  PSTORITYP M*15 Source type [menu 3037: 1=Manual,2=Generated,3=Synchronization,4=Import]
  PSTORIVCR VCR Original document no.
  PSTORIVCRL L*8 Original line no.
  PSTREP REP Supervisor -> [REP]REP0 =[LDS]PSTREP (SALESREP) !Block
  PSTSTA M*15 Status [menu 3040: 1=Disqualified,2=On hold,3=Qualified,4=Contacted]
  PSTTYP M*15 Type [menu 7811: 1=Standard,2=Lead]
  SRV A*30 Department
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MARASSDEF (MAD) - Content of sectors
Keys (first = PK; D = duplicates allowed): MAD0 RECORDNUM+RECORDADD+RECORDTYP; MAD1 RECORDNUM+RECORDTYP (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MAD]CREUSR (AUTILIS) !Other
  MANASS C*4 Manually allocated
  MARSCTNUM VCR Sector code
  RECORDADD ADR Address code
  RECORDNUM VCR Record key
  RECORDTYP ABR Record type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MAD]UPDUSR (AUTILIS) !Other

## MARASSREP (MAR) - Representative portfolio
Keys (first = PK; D = duplicates allowed): MAR0 RECORDNUM+RECORDADD+RECORDTYP (D); MAR1 RECORDNUM+RECORDTYP (D); MAR2 RECORDNUM+RECORDADD+RECORDTYP+REPTYP (D); MAR3 RECORDNUM+RECORDTYP+REPTYP (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MAR]CREUSR (AUTILIS) !Other
  MANASS C*4 Manually allocated
  RECORDADD ADR Address code
  RECORDNUM VCR Record key
  RECORDTYP ABR Record type
  REPITM ADI Product group -> [ADI]CODE =1+GFAMCIA;REPITM (ATABDIV) !Block
  REPMSS ADI Role -> [ADI]CODE =414;REPMSS (ATABDIV) !Block
  REPNUM REP Sales rep -> [REP]REP0 =[MAR]REPNUM (SALESREP) !Block
  REPTYP C*4 Representative type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MAR]UPDUSR (AUTILIS) !Other

## MARDEF (MDF) - Definitions of sectors
Keys (first = PK; D = duplicates allowed): MDF0 MARSCTNUM (D); MDF1 MARSCTNUM+CRINUM; MDF2 MARSCTNUM+CRINUM+MARSCTTAB+MARSCTFIE (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRINUM L*8 No. of criteria
  MARSCTCND M*15 Condition [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  MARSCTFIE AVA Criteria field
  MARSCTNUM VCR Sector code
  MARSCTOPD M*15 Operator [menu 2955: 1=.,2=And,3=Or]
  MARSCTTAB M*15 Table of criteria [menu 2958: 1=BPs,2=Prospects/Customers,3=Addresses,4=Contacts]
  MDFABRFIC A*10 Table abbreviation
  MDFFIETYP M*15 Data type [menu 3049: 1=Alphanumeric,2=Numeric,3=Date]
  MDFINDNUM C*2 Index
  MDFINDOK C*1 Possible index
  MDFTAB ATB Table -> [ATB]CODFIC =[MDF]MDFTAB (ATABLE) !Block
  MDFVAL A*50 Value
  NBPARDEB C*4 No. opening brackets
  NBPARFIN C*4 No. closing brackets.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MARDEFVAL (MDV) - Criteria details
Keys (first = PK; D = duplicates allowed): MDV0 MARSCTNUM+CRINUM (D); MDV1 MARSCTNUM+CRINUM+SCTVALNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MDV]CREUSR (AUTILIS) !Other
  CRINUM L*8 No. of criteria
  MARSCTNUM VCR Sector code
  MARSCTVAL A*35 Value
  MARVALDAT D Internal date value
  SCTVALNUM C*4 No. of value
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MDV]UPDUSR (AUTILIS) !Other

## MARREPSEC (MRS) - Allocation of sectors
Keys (first = PK; D = duplicates allowed): MRS0 MARSCTNUM (D); MRS1 MARSCTNUM+SCTREPSEC
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MRS]CREUSR (AUTILIS) !Other
  MARSCTNUM VCR Sector code
  SCTREPITM ADI Product group -> [ADI]CODE =1+GFAMCIA;SCTREPITM (ATABDIV) !Block
  SCTREPMSS ADI Role -> [ADI]CODE =414;SCTREPMSS (ATABDIV) !Block
  SCTREPSEC REP Sales rep -> [REP]REP0 =[MRS]SCTREPSEC (SALESREP) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MRS]UPDUSR (AUTILIS) !Other

## MARSCT (MST) - Market sectors
Keys (first = PK; D = duplicates allowed): MST0 MARSCTNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GRUDEF A*100 Criteria groups
  MARSCTAXX AXX Description
  MARSCTDES CLX Description
  MARSCTNUM VCR Sector code
  MARSCTREP REP Sales rep -> [REP]REP0 =[MST]MARSCTREP (SALESREP) !Block act:REC
  MSTCRI M*15 Selection [menu 3051: 1=Criteria,2=Formula,3=Criteria and formula]
  MSTENA M*4 Active [menu 1: 1=No,2=Yes]
  MSTFOR CLX Formula
  MSTFOROPD M*15 Formula operator [menu 2955: 1=.,2=And,3=Or]
  MSTORD C*4 Order number
  NUMFULDES CLC Chrono txt file
  TYPFULDES CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MKGLEVEL (MKL) - Level
Keys (first = PK; D = duplicates allowed): MKL0 OPGNUM+KEYTYPE+DATAKEY
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MKL]CREUSR (AUTILIS) !Other
  DATAKEY VCR Key
  KEYTYPE ABR Type
  LEVEL L*8 Level
  OPGNUM VCR Operation code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MKL]UPDUSR (AUTILIS) !Other

## MKGOPG (MOG) - Target/operations relations
Keys (first = PK; D = duplicates allowed): MOG0 MKGQUR+OPGNUM+TGR; MOG1 MKGQUR+TGR (D); MOG2 OPGNUM+TGR (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MOG]CREUSR (AUTILIS) !Other
  MKGQUR VCR Target
  OPGNUM VCR Operation code
  TGR TGL Target -> [TGL]TGL0 =[MOG]TGR (TGRLIS) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MOG]UPDUSR (AUTILIS) !Other

## MKGQUR (MQR) - Marketing targets
Keys (first = PK; D = duplicates allowed): MQR0 QURNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FGVCAH C*4 Cancel cache
  FINPPL L*8 Final population
  PPLGRUDIO A*110 Regroup pop.
  QURCAT ADI Category -> [ADI]CODE =438;QURCAT (ATABDIV) !Block
  QURNAM DCO Description
  QURNUM VCR Target code
  QURTOTREC L*8 Number of entries
  TGPNUM TGP Presentation support -> [TGP]TGP0 =[MQR]TGPNUM (TGRSSP) !Block
  TGR TGL Target -> [TGL]TGL0 =[MQR]TGR (TGRLIS) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MQR]UPDUSR (AUTILIS) !Other
  WIZCRE M*4 Created by the wizard [menu 1: 1=No,2=Yes]

## MKGQURPPL (MQP) - Intermediate populations
Keys (first = PK; D = duplicates allowed): MQP0 QURNUM (D); MQP1 QURNUM+PPLORD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MQP]CREUSR (AUTILIS) !Other
  CRIGRUDIO A*110 Regrouping cri.
  FGVCAH C*4 Cancel cache
  PPLDES CLX Description
  PPLDESCRLF CLX Description
  PPLOPD M*15 Operator [menu 2959: 1=.,2=and,3=or,4=and not,5=or not]
  PPLORD L*8 Population code
  PPLSELSPT VCR Selection help
  QURNUM VCR Target code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MQP]UPDUSR (AUTILIS) !Other

## OMMRESULT (MRE) - Merge data
Keys (first = PK; D = duplicates allowed): MRE0 OPGNUM+MRENUM
Fields:
  ADD1 A*50 Address
  ADD2 A*50 Address
  ADD3 A*50 Address
  AUUID AUUID Single identifier
  BPRNAM A*50 BP name
  BPRNUM A*50 BP code
  CCNNUM A*50 Contact (rel.) code
  CLSNUM L*8 Order no.
  CNTNAM A*85 Contact name
  CNTTTL A*50 Title
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MRE]CREUSR (AUTILIS) !Other
  CRY A*50 Country
  CTY A*50 City
  F501 A*10 F501
  F599 A*10 F599
  FAX A*50 Fax
  MRENUM VCR Sequence no.
  OPGNUM VCR Mail code
  REPFNC A*50 Function
  REPNAM A*50 Sales rep name
  SAT A*50 County
  TEL A*50 Telephone
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MRE]UPDUSR (AUTILIS) !Other
  WEB A*50 Email
  ZIP A*50 Postal code

## OMMRPT (OMR) - Mailing report
Keys (first = PK; D = duplicates allowed): OMR0 LAN+MAGTPL
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[OMR]CREUSR (AUTILIS) !Other
  LAN LAN Language -> [TLA]TLA0 =[OMR]LAN (TABLAN) !Block
  MAGTPL A*50 Report code
  MAGTPLRPT A*50 Mailing report
  OMRDESAX3 AX3 Long title
  OMRSHOAX1 AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[OMR]UPDUSR (AUTILIS) !Other

## PLGMKG (PLG) - Marketing schedule management
Keys (first = PK; D = duplicates allowed): PLG0 CMGNUM (D); PLG1 CLSNUM (D); PLG2 CLSNUM+SSS (D)
Fields:
  AUUID AUUID Single identifier
  CLSNUM L*8 Order no.
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[PLG]CMGNUM (CMARKETING) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PLG]CREUSR (AUTILIS) !Other
  DAT D Date created
  MOR A*1 Tree structure test
  SSS A*30 Session
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PLG]UPDUSR (AUTILIS) !Other

## PLGOPG (PLO) - Marketing schedule management
Keys (first = PK; D = duplicates allowed): PLO0 OPGNUM (D); PLO1 CLSNUM (D); PLO2 CMGNUM+OPGNUM+SSS (D)
Fields:
  AUUID AUUID Single identifier
  CLSNUM L*8 Order no.
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[PLO]CMGNUM (CMARKETING) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PLO]CREUSR (AUTILIS) !Other
  DAT D Date created
  DATOPG D Operation date
  OPGNUM VCR Operation code
  SSS A*30 Session
  TYPOPG M*15 Operation type [menu 969: 1=Mass mailing,2=Call campaign,3=Trade show,4=Media Campaign,5=.]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PLO]UPDUSR (AUTILIS) !Other

## QURCRI (QCR) - Criteria of target
Keys (first = PK; D = duplicates allowed): QCR0 QURNUM+PPLORD (D); QCR1 QURNUM+PPLORD+CRINUM; QCR2 QURNUM+CRICND (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[QCR]CREUSR (AUTILIS) !Other
  CRICND M*15 Condition [menu 2960: 1=Equal,2=Different,3=Starting with,4=Containing,5=Ending with,6=Greater than,7=Greater than or equal to,8=Less than,9=Less than or equal to,10=Included between]
  CRIFIE AVA Field
  CRINUM L*8 Criteria code
  CRIOPD M*15 Operator [menu 2959: 1=.,2=and,3=or,4=and not,5=or not]
  CRITAB ATB Table -> [ATB]CODFIC =[QCR]CRITAB (ATABLE) !Block
  FGVCAH C*4 Cancel cache
  PPLORD L*8 Population code
  QURNUM VCR Target code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QCR]UPDUSR (AUTILIS) !Other

## QURCRIVAL (QCV) - Criteria values
Keys (first = PK; D = duplicates allowed): QCV0 QURNUM+PPLORD+CRINUM (D); QCV1 QURNUM+PPLORD+CRINUM+CRIVALNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[QCV]CREUSR (AUTILIS) !Other
  CRINUM L*8 Criteria code
  CRIVAL A*35 Value
  CRIVALDAT D Internal date value
  CRIVALNUM C*4 Value code
  FGVCAH C*4 Cancel cache
  PPLORD L*8 Population code
  QURNUM VCR Target code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QCV]UPDUSR (AUTILIS) !Other

## QUREXTRACT (QTX) - Extraction of targets
Keys (first = PK; D = duplicates allowed): QTX0 QURNUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[QTX]CREUSR (AUTILIS) !Other
  MGCCOL1 A*35 Column 1
  MGCCOL10 A*35 Column 10
  MGCCOL11 A*35 Column 11
  MGCCOL12 A*35 Column 12
  MGCCOL13 A*35 Column 13
  MGCCOL14 A*35 Column 14
  MGCCOL15 A*35 Column 15
  MGCCOL16 A*35 Column 16
  MGCCOL17 A*35 Column 17
  MGCCOL18 A*35 Column 18
  MGCCOL19 A*35 Column 19
  MGCCOL2 A*35 Column 2
  MGCCOL20 A*35 Column 20
  MGCCOL21 A*35 Column 21
  MGCCOL22 A*35 Column 22
  MGCCOL23 A*35 Column 23
  MGCCOL24 A*35 Column 24
  MGCCOL25 A*35 Column 25
  MGCCOL26 A*35 Column 26
  MGCCOL27 A*35 Column 27
  MGCCOL28 A*35 Column 28
  MGCCOL29 A*35 Column 29
  MGCCOL3 A*35 Column 3
  MGCCOL30 A*35 Column 30
  MGCCOL31 A*35 Column 31
  MGCCOL32 A*35 Column 32
  MGCCOL33 A*35 Column 33
  MGCCOL34 A*35 Column 34
  MGCCOL35 A*35 Column 35
  MGCCOL36 A*35 Column 36
  MGCCOL37 A*35 Column 37
  MGCCOL38 A*35 Column 38
  MGCCOL39 A*35 Column 39
  MGCCOL4 A*35 Column 4
  MGCCOL40 A*35 Column 40
  MGCCOL41 A*35 Column 41
  MGCCOL42 A*35 Column 42
  MGCCOL43 A*35 Column 43
  MGCCOL44 A*35 Column 44
  MGCCOL45 A*35 Column 45
  MGCCOL46 A*35 Column 46
  MGCCOL47 A*35 Column 47
  MGCCOL48 A*35 Column 48
  MGCCOL49 A*35 Column 49
  MGCCOL5 A*35 Column 5
  MGCCOL50 A*35 Column 50
  MGCCOL51 A*35 Column 51
  MGCCOL52 A*35 Column 52
  MGCCOL53 A*35 Column 53
  MGCCOL54 A*35 Column 54
  MGCCOL55 A*35 Column 55
  MGCCOL56 A*35 Column 56
  MGCCOL57 A*35 Column 57
  MGCCOL58 A*35 Column 58
  MGCCOL59 A*35 Column 59
  MGCCOL6 A*35 Column 6
  MGCCOL60 A*35 Column 60
  MGCCOL61 A*35 Column 61
  MGCCOL62 A*35 Column 62
  MGCCOL63 A*35 Column 63
  MGCCOL64 A*35 Column 64
  MGCCOL65 A*35 Column 65
  MGCCOL66 A*35 Column 66
  MGCCOL67 A*35 Column 67
  MGCCOL68 A*35 Column 68
  MGCCOL69 A*35 Column 69
  MGCCOL7 A*35 Column 7
  MGCCOL70 A*35 Column 70
  MGCCOL71 A*35 Column 71
  MGCCOL72 A*35 Column 72
  MGCCOL73 A*35 Column 73
  MGCCOL74 A*35 Column 74
  MGCCOL75 A*35 Column 75
  MGCCOL76 A*35 Column 76
  MGCCOL77 A*35 Column 77
  MGCCOL78 A*35 Column 78
  MGCCOL79 A*35 Column 79
  MGCCOL8 A*35 Column 8
  MGCCOL80 A*35 Column 80
  MGCCOL81 A*35 Column 81
  MGCCOL82 A*35 Column 82
  MGCCOL83 A*35 Column 83
  MGCCOL84 A*35 Column 84
  MGCCOL85 A*35 Column 85
  MGCCOL86 A*35 Column 86
  MGCCOL87 A*35 Column 87
  MGCCOL88 A*35 Column 88
  MGCCOL89 A*35 Column 89
  MGCCOL9 A*35 Column 9
  MGCCOL90 A*35 Column 90
  MGCCOL91 A*35 Column 91
  MGCCOL92 A*35 Column 92
  MGCCOL93 A*35 Column 93
  MGCCOL94 A*35 Column 94
  MGCCOL95 A*35 Column 95
  MGCCOL96 A*35 Column 96
  MGCCOL97 A*35 Column 97
  MGCCOL98 A*35 Column 98
  MGCCOL99 A*35 Column 99
  MGCCOLSRTA A*35 Sort field
  MGCCOLSRTD D Sort field
  MGCCOLSRTK A*30 Key
  MGCCOLSRTL DCB*24.2 Sort field
  MGCTIT1 A*50 Column 1
  MGCTIT10 A*50 Column 10
  MGCTIT11 A*50 Column 11
  MGCTIT12 A*50 Column 12
  MGCTIT13 A*50 Column 13
  MGCTIT14 A*50 Column 14
  MGCTIT15 A*50 Column 15
  MGCTIT16 A*50 Column 16
  MGCTIT17 A*50 Column 17
  MGCTIT18 A*50 Column 18
  MGCTIT19 A*50 Column 19
  MGCTIT2 A*50 Column 2
  MGCTIT20 A*50 Column 20
  MGCTIT21 A*50 Column 21
  MGCTIT22 A*50 Column 22
  MGCTIT23 A*50 Column 23
  MGCTIT24 A*50 Column 24
  MGCTIT25 A*50 Column 25
  MGCTIT26 A*50 Column 26
  MGCTIT27 A*50 Column 27
  MGCTIT28 A*50 Column 28
  MGCTIT29 A*50 Column 29
  MGCTIT3 A*50 Column 3
  MGCTIT30 A*50 Column 30
  MGCTIT31 A*50 Column 31
  MGCTIT32 A*50 Column 32
  MGCTIT33 A*50 Column 33
  MGCTIT34 A*50 Column 34
  MGCTIT35 A*50 Column 35
  MGCTIT36 A*50 Column 36
  MGCTIT37 A*50 Column 37
  MGCTIT38 A*50 Column 38
  MGCTIT39 A*50 Column 39
  MGCTIT4 A*50 Column 4
  MGCTIT40 A*50 Column 40
  MGCTIT41 A*50 Column 41
  MGCTIT42 A*50 Column 42
  MGCTIT43 A*50 Column 43
  MGCTIT44 A*50 Column 44
  MGCTIT45 A*50 Column 45
  MGCTIT46 A*50 Column 46
  MGCTIT47 A*50 Column 47
  MGCTIT48 A*50 Column 48
  MGCTIT49 A*50 Column 49
  MGCTIT5 A*50 Column 5
  MGCTIT50 A*50 Column 50
  MGCTIT51 A*50 Column 51
  MGCTIT52 A*50 Column 52
  MGCTIT53 A*50 Column 53
  MGCTIT54 A*50 Column 54
  MGCTIT55 A*50 Column 55
  MGCTIT56 A*50 Column 56
  MGCTIT57 A*50 Column 57
  MGCTIT58 A*50 Column 58
  MGCTIT59 A*50 Column 59
  MGCTIT6 A*50 Column 6
  MGCTIT60 A*50 Column 60
  MGCTIT61 A*50 Column 61
  MGCTIT62 A*50 Column 62
  MGCTIT63 A*50 Column 63
  MGCTIT64 A*50 Column 64
  MGCTIT65 A*50 Column 65
  MGCTIT66 A*50 Column 66
  MGCTIT67 A*50 Column 67
  MGCTIT68 A*50 Column 68
  MGCTIT69 A*50 Column 69
  MGCTIT7 A*50 Column 7
  MGCTIT70 A*50 Column 70
  MGCTIT71 A*50 Column 71
  MGCTIT72 A*50 Column 72
  MGCTIT73 A*50 Column 73
  MGCTIT74 A*50 Column 74
  MGCTIT75 A*50 Column 75
  MGCTIT76 A*50 Column 76
  MGCTIT77 A*50 Column 77
  MGCTIT78 A*50 Column 78
  MGCTIT79 A*50 Column 79
  MGCTIT8 A*50 Column 8
  MGCTIT80 A*50 Column 80
  MGCTIT81 A*50 Column 81
  MGCTIT82 A*50 Column 82
  MGCTIT83 A*50 Column 83
  MGCTIT84 A*50 Column 84
  MGCTIT85 A*50 Column 85
  MGCTIT86 A*50 Column 86
  MGCTIT87 A*50 Column 87
  MGCTIT88 A*50 Column 88
  MGCTIT89 A*50 Column 89
  MGCTIT9 A*50 Column 9
  MGCTIT90 A*50 Column 90
  MGCTIT91 A*50 Column 91
  MGCTIT92 A*50 Column 92
  MGCTIT93 A*50 Column 93
  MGCTIT94 A*50 Column 94
  MGCTIT95 A*50 Column 95
  MGCTIT96 A*50 Column 96
  MGCTIT97 A*50 Column 97
  MGCTIT98 A*50 Column 98
  MGCTIT99 A*50 Column 99
  QURNUM VCR Target code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QTX]UPDUSR (AUTILIS) !Other

## QURTMP (QTP) - Target process
Keys (first = PK; D = duplicates allowed): QTP0 QURNUM+PPLORD+CRINUM+KEYTGR (D); QTP1 QURNUM+PPLORD+KEYTGR (D); QTP2 KEYTGR (D); QTP3 QURNUM+PPLORD+CRINUM+WKGTAB+KEYREC (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[QTP]CREUSR (AUTILIS) !Other
  CRINUM L*8 Criteria code
  CRIVALNUM C*4 Value code
  KEYREC A*30 Record key
  KEYTGR A*30 Target key
  PPLORD L*8 Population code
  QURNUM VCR Target code
  SPTLEV C*4 Level
  SPTTYP M*15 Type of support [menu 2965: 1=Regrouping of tables,2=Process,3=All records,4=First level link]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QTP]UPDUSR (AUTILIS) !Other
  WKGTAB ATB Table processed -> [ATB]CODFIC =[QTP]WKGTAB (ATABLE) !Block

## RESOURCES (RSS) - Resources
Keys (first = PK; D = duplicates allowed): RSS0 NUM
Fields:
  AUUID AUUID Single identifier
  CAT ADI Category -> [ADI]CODE =411;CAT (ATABDIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  NUM VCR Code
  NUMFULDES CLC Chrono txt file
  RSSDESAXX AXX Description
  SALFCY FCY Sales site -> [FCY]FCY0 =[RSS]SALFCY (FACILITY) !Block
  TTR DCO Description
  TYPFULDES CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## RESRES (RRS) - Resource reservations
Keys (first = PK; D = duplicates allowed): RRS0 NUM; RRS1 RRSORI+RRSORIVCR (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CRESNC D Reserved since the
  CREUSR A*5 Creation user
  HOUEND HM End time
  HOUSTR HM Start time
  NUM VCR Code
  RERDAT D Reserved for the
  RERDATEND D End date
  RERREP REP Reserved by -> [REP]REP0 =[RRS]RERREP (SALESREP) !Block
  RRSORI M*15 Source [menu 2997: 1=Manual creation,2=Appointment,3=After-sales service action]
  RRSORIVCR VCR Document no.
  RRSORIVCRL L*8 Line no.
  RSSNUM RSS Resource code -> [RSS]RSS0 =[RRS]RSSNUM (RESOURCES) !Block
  SALFCY FCY Sales site -> [FCY]FCY0 =[RRS]SALFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SCPASW (SCA) - Call script responses
Keys (first = PK; D = duplicates allowed): SCA0 CLL+SCP+QST
Fields:
  ASWALH DCO Answer
  ASWBOL M*4 Answer [menu 1: 1=No,2=Yes]
  ASWDAT D Answer
  ASWNUM DCB*9.2 Answer
  ASWTYP M*15 Response type [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  AUUID AUUID Single identifier
  CLL VCR Short code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SCA]CREUSR (AUTILIS) !Other
  QST QSS Question code
  SCP VCR Script code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SCA]UPDUSR (AUTILIS) !Other

## SCPQST (SCQ) - Call script questions
Keys (first = PK; D = duplicates allowed): SCQ0 SCPNUM+QSTNUM
Fields:
  ASWFIE A*10 Field code
  ASWKEY A*100 Key
  ASWTAB M*10 Table code [menu 959: 1=Business Partners,2=Prospects/Customers,3=Contacts]
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SCQ]CREUSR (AUTILIS) !Other
  QST DCO Question
  QSTNUM QSS Question code
  QSTTYP M*15 Response type [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  SCPNUM VCR Script code
  STRQST M*4 First question [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SCQ]UPDUSR (AUTILIS) !Other

## SCPQSTCND (SQC) - Routing conditions
Keys (first = PK; D = duplicates allowed): SQC0 SCPNUM+QSTNUM+CNDNUM (D); SQC1 SCPNUM+NEXQST (D); SQC2 SCPNUM+QSTNUM+CND (D)
Fields:
  ALHCND DCO Alphanumeric condition
  AUUID AUUID Single identifier
  CND MM*15 Condition [menu 962: 1=Next,2=Exit,3=Starting with,4=Containing,5=Ending with,6=Greater than,7=Greater than or equal to,8=Less than,9=Less than or equal to,10=Between,11=True,12=False,13=Before the,14=After the,15=Other]
  CNDNUM VCR Condition code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SQC]CREUSR (AUTILIS) !Other
  DATCNDMAX D Max date conditions
  DATCNDMIN D Min date condition
  NEXQST QSS Next question
  NUMCNDMAX DCB*9.2 Max numeric condition
  NUMCNDMIN DCB*9.2 Min numeric condition
  QSTNUM QSS Question code
  SCPNUM VCR Script code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SQC]UPDUSR (AUTILIS) !Other

## SCRIPT (SCP) - Call script
Keys (first = PK; D = duplicates allowed): SCP0 SCPNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SALFCY FCY Site -> [FCY]FCY0 =[SCP]SALFCY (FACILITY) !Block
  SCPFLG M*4 Inactive [menu 1: 1=No,2=Yes]
  SCPNAM DCO Description
  SCPNUM VCR Script code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SCP]UPDUSR (AUTILIS) !Other

## SECPST (SPT) - Lead sector
Keys (first = PK; D = duplicates allowed): SPT0 SPTNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SECPSTAXX AXX Description
  SPTCRI M*15 Selection [menu 3051: 1=Criteria,2=Formula,3=Criteria and formula]
  SPTENA M*4 Active [menu 1: 1=No,2=Yes]
  SPTFOR CLX Formula
  SPTFOROPD M*15 Formula operator [menu 2955: 1=.,2=And,3=Or]
  SPTNUM VCR Sector code
  SPTORD C*4 Order number
  SPTREP REP Sales rep -> [REP]REP0 =[SPT]SPTREP (SALESREP) !Block
  SPTRES A*100 Grouping
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SECPSTSEL (SPS) - Lead sector selection
Keys (first = PK; D = duplicates allowed): SPS0 SPSNUM+SPSLIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  NBPARDEB C*4 No. opening brackets
  NBPARFIN C*4 No. closing brackets.
  SPSABRFIC A*10 Table abbreviation
  SPSCND M*15 Condition [menu 2960: 1=Equal,2=Different,3=Starting with,4=Containing,5=Ending with,6=Greater than,7=Greater than or equal to,8=Less than,9=Less than or equal to,10=Included between]
  SPSFIE AVA Fields
  SPSFIETYP M*15 Data type [menu 3049: 1=Alphanumeric,2=Numeric,3=Date]
  SPSINDNUM C*2 Index
  SPSINDOK C*1 Possible index
  SPSLIN C*4 Line number
  SPSNUM VCR Sector code
  SPSOPD MM*15 Operator [menu 2955: 1=.,2=And,3=Or]
  SPSTAB ATB Table -> [ATB]CODFIC =[SPS]SPSTAB (ATABLE) !Block
  SPSVAL A*50 Value
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SELCMG (SEC) - List of marketing selections
Keys (first = PK; D = duplicates allowed): SEC0 OPGNUM+SELTBL (D)
Fields:
  AUUID AUUID Single identifier
  CNTTTR A*75 Generic title
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SEC]CREUSR (AUTILIS) !Other
  DEFADD M*15 Address assignment [menu 965: 1=By Business Partner,2=By Contact]
  HIEBPR M*4 BP/contact empty [menu 1: 1=No,2=Yes]
  OPGNUM VCR Operation code
  OPGTYP ABR Operation type
  SELCRI CLX Criteria
  SELDAT D Selection date
  SELREC L*8 No. of records
  SELTBL ABR File
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SEC]UPDUSR (AUTILIS) !Other
  USEQUR M*4 Use target [menu 1: 1=No,2=Yes]

## SELCMGLIS (SCL) - Marketing selection guide
Keys (first = PK; D = duplicates allowed): SCL0 OPGNUM+RECTYP (D); SCL1 OPGNUM+RECTYP+RECNUM (D); SCL2 OPGNUM+RECTYP+RECNUM+BPRNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address code
  BPRNUM BPR BP code -> [BPR]BPR0 =[SCL]BPRNUM (BPARTNER) !Block
  CLSNUM L*8 Order no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SCL]CREUSR (AUTILIS) !Other
  OPGNUM VCR Operation code
  RECNUM VCR Code
  RECTYP ABR Type
  REPNUM REP Sales rep code -> [REP]REP0 =[SCL]REPNUM (SALESREP) !Block
  SCLCRY CRY Country -> [TCY]TCY0 =[SCL]SCLCRY (TABCOUNTRY) !Block
  SCLCTY CTY City
  SCLSAT SAT County
  SCLZIP POS Postal code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SCL]UPDUSR (AUTILIS) !Other

## SELSSP (SSP) - Support of selections
Keys (first = PK; D = duplicates allowed): SSP0 SPTNUM; SSP1 SPTTGR+SPTNUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SSP]CREUSR (AUTILIS) !Other
  SPTDES CLX Description
  SPTNAMAXX AXX Description
  SPTNUM VCR Support code
  SPTPRO A*10 Processing
  SPTSTD C*4 Standard support
  SPTTGR TGL Target -> [TGL]TGL0 =[SSP]SPTTGR (TGRLIS) !Delete
  SPTTYP M*15 Type [menu 2965: 1=Regrouping of tables,2=Process,3=All records,4=First level link]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SSP]UPDUSR (AUTILIS) !Other

## SELSSPCPN (SSC) - Selection support components
Keys (first = PK; D = duplicates allowed): SSC0 SPTNUM+SPTLEV (D); SSC1 SPTNUM+SPTTAB
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SSC]CREUSR (AUTILIS) !Other
  SPTCPNSTD C*4 Standard support
  SPTFLT A*215 Filter
  SPTIDX ANX Index
  SPTKEY AVA Key
  SPTKEYPAE AVA Parent key
  SPTLEV C*4 Level
  SPTNUM VCR Support code
  SPTTAB ATB Table -> [ATB]CODFIC =[SSC]SPTTAB (ATABLE) !Block
  SPTTABPAE ATB Parent table -> [ATB]CODFIC =[SSC]SPTTABPAE (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SSC]UPDUSR (AUTILIS) !Other

## SYNCDATA (SYD) - Synchronization data
Keys (first = PK; D = duplicates allowed): SYD0 SYDNUM; SYD1 SYDUSR (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SYDATTTYP A*1 Action type
  SYDDAT D Date
  SYDGEN C*1 Generate synchro
  SYDHOU HS Time
  SYDKEY VCR Key
  SYDNUM VCR Sequence no.
  SYDOTKSTA C*1 Outlook status
  SYDTYP ABR Type
  SYDUPD C*1 Update synchro
  SYDUSR AUS User -> [AUS]CODUSR =[SYD]SYDUSR (AUTILIS) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SYNCLINK (SYL) - Synchronise cross reference
Keys (first = PK; D = duplicates allowed): SYL0 SYLNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SYLFIE ATB Heading -> [ATB]CODFIC =[SYL]SYLFIE (ATABLE) !Block
  SYLFLGDPT C*1 To process
  SYLKEY VCR Key
  SYLNIV C*4 Level
  SYLNUM VCR Sequence no.
  SYLTYP AOB Type -> [AOB]ABREV =[SYL]SYLTYP (AOBJET) !Block
  SYLUSR AUS User -> [AUS]CODUSR =[SYL]SYLUSR (AUTILIS) !Block
  SYLVALADX CLX X3 value
  SYLVALOTK CLX Outlook value
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SYNCPAR (SYP) - Synchronization setup
Keys (first = PK; D = duplicates allowed): SYP0 SYPUSR
Fields:
  AUUID AUUID Single identifier
  BAPADXCRE M*4 Create X3 appt. [menu 1: 1=No,2=Yes]
  BAPADXDLT M*4 Delete X3 appt. [menu 1: 1=No,2=Yes]
  BAPADXUPD M*4 Update X3 appt. [menu 1: 1=No,2=Yes]
  BAPOTKCRE M*4 Create Outlook appt. [menu 1: 1=No,2=Yes]
  BAPOTKDLT M*4 Delete Outlook appt. [menu 1: 1=No,2=Yes]
  BAPOTKUPD M*4 Update Outlook appt. [menu 1: 1=No,2=Yes]
  CLLADXCRE M*4 Create adonix call [menu 1: 1=No,2=Yes]
  CLLADXDLT M*4 Delete X3 call [menu 1: 1=No,2=Yes]
  CLLADXUPD M*4 Update X3 call [menu 1: 1=No,2=Yes]
  CLLOTKCRE M*4 Create Outlook call [menu 1: 1=No,2=Yes]
  CLLOTKDLT M*4 Delete Outlook call [menu 1: 1=No,2=Yes]
  CLLOTKUPD M*4 Update Outlook call [menu 1: 1=No,2=Yes]
  CORADXCRE M*4 Create X3 contact [menu 1: 1=No,2=Yes]
  CORADXDLT M*4 Delete X3 contact [menu 1: 1=No,2=Yes]
  CORADXUPD M*4 Update X3 contact [menu 1: 1=No,2=Yes]
  COROTKCRE M*4 Create Outlook contact [menu 1: 1=No,2=Yes]
  COROTKDLT M*4 Delete Outlook contact [menu 1: 1=No,2=Yes]
  COROTKUPD M*4 Update Outlook contact [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  OTKUSR A*10 Outlook user
  SYPUSR AUS User -> [AUS]CODUSR =[SYP]SYPUSR (AUTILIS) !Block
  TSKADXCRE M*4 Create X3 task [menu 1: 1=No,2=Yes]
  TSKADXDLT M*4 Delete X3 task [menu 1: 1=No,2=Yes]
  TSKADXUPD M*4 Update X3 task [menu 1: 1=No,2=Yes]
  TSKOTKCRE M*4 Create Outlook task [menu 1: 1=No,2=Yes]
  TSKOTKDLT M*4 Delete Outlook task [menu 1: 1=No,2=Yes]
  TSKOTKUPD M*4 Update Outlook task [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TGRLIS (TGL) - Dictionary of targets
Keys (first = PK; D = duplicates allowed): TGL0 TGRTAB
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TGL]CREUSR (AUTILIS) !Other
  TGRAOB ABR Management object
  TGRDES CLX Description
  TGRLISSTD C*4 Standard
  TGRMAIKEY AVA Target primary key
  TGRNAMAXX AXX Description
  TGRSSPDEF TGP Default support -> [TGP]TGP0 =[TGL]TGRSSPDEF (TGRSSP) !Block
  TGRTAB ATB Table -> [ATB]CODFIC =[TGL]TGRTAB (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TGL]UPDUSR (AUTILIS) !Other

## TGRLISFIE (TLF) - Target inquiry
Keys (first = PK; D = duplicates allowed): TLF0 TGRTAB+TGRSSPNUM (D); TLF1 TGRTAB+TGRSSPNUM+TGRTABLNK+TGRFIE
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TLF]CREUSR (AUTILIS) !Other
  TGRFIE A*17 Field
  TGRFIEORD L*8 Order no.
  TGRFIESTD C*4 Standard
  TGRSSPNUM TGP Presentation support -> [TGP]TGP0 =[TLF]TGRSSPNUM (TGRSSP) !Delete
  TGRTAB ATB Table -> [ATB]CODFIC =[TLF]TGRTAB (ATABLE) !Block
  TGRTABLNK ATB Linked table -> [ATB]CODFIC =[TLF]TGRTABLNK (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TLF]UPDUSR (AUTILIS) !Other

## TGRLISLNK (TLL) - Linked tables
Keys (first = PK; D = duplicates allowed): TLL0 TGRTAB+TGRLNK; TLL1 TGRTAB+TGRLNK+TGRLNKIDX
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TLL]CREUSR (AUTILIS) !Other
  TGREXPLNK A*215 Link expression
  TGRLNK ATB Linked table -> [ATB]CODFIC =[TLL]TGRLNK (ATABLE) !Block
  TGRLNKIDX ANX Link key
  TGRLNKSTD C*4 Standard
  TGRTAB ATB Table -> [ATB]CODFIC =[TLL]TGRTAB (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TLL]UPDUSR (AUTILIS) !Other

## TGRSSP (TGP) - Presentation support
Keys (first = PK; D = duplicates allowed): TGP0 TGRSSPNUM; TGP1 TGR+TGRSSPNUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FIESRT A*17 Sort field
  FIESRTTYP M*10 Sort sequence [menu 90: 1=Ascending,2=Descending]
  SPTDEF C*4 Default support
  SPTSTD C*4 Standard support
  TABSRT ATB Sort table -> [ATB]CODFIC =[TGP]TABSRT (ATABLE) !Block
  TGR TGL Target -> [TGL]TGL0 =[TGP]TGR (TGRLIS) !Delete
  TGRAXX AXX Description
  TGRSSPNUM VCR Support code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TGP]UPDUSR (AUTILIS) !Other

