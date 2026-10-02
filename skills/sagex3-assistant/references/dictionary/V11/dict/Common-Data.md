<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Common Data module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## AYTPRFX3 (AYR) - Website user
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYR0 USR+FCYXTDCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AYR]CREUSR (AUTILIS) !Other
  FCYXTDCOD AYS Website -> [AYS]AYS0 =[AYR]FCYXTDCOD (AYTFCY) !Delete
  PRFXTDCOD AYD Website profile -> [AYD]AYD0 =FCYXTDCOD;PRFXTDCOD (AYTPRF) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AYR]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AYR]USR (AUTILIS) !Delete

## BAPPOINT (BAP) - Appointment
Notes: differs in V9.0 P12 (diff: AT3_BAPPOINT.htm); differs in V10 P1 (diff: ATD_BAPPOINT.htm)
Keys (first = PK; D = duplicates allowed): APP0 APTNUM; APP1 APTWEE (D); APP2 APTDAT+APTHOU+APTNUM; APP3 APTWEE+APTDAT+APTHOU (D); APP4 APTDATX (D); APP5 APTCMP (D); APP6 APTORIADI+APTORIVCR+APTORIVCRL (D)
Fields:
  APTADD CAD(3) Address
  APTCCNNUM AIN(10) Contact to visit -> [AIN]AIN0 =[BAP]APTCCNNUM (CONTACTCRM) !Block
  APTCMGNUM CMG Campaign code -> [CMG]CMG0 =[BAP]APTCMGNUM (CMARKETING) !Block
  APTCMP BPR BP -> [BPR]BPR0 =[BAP]APTCMP (BPARTNER) !Block
  APTCODADD ADR Address code
  APTCOR COR(10) Outlook contact -> [COR]COR0 =[BAP]APTCOR (CORRESPOND) !Block
  APTCRY CRY Country -> [TCY]TCY0 =[BAP]APTCRY (TABCOUNTRY) !Block
  APTCTY CTY City
  APTDAT D Appointment date
  APTDATEND D Last appointment
  APTDATX D Week conversion
  APTDON M*4 Completed [menu 1: 1=No,2=Yes]
  APTDUR HM Appointment duration
  APTEML MAI Email address
  APTHOU HM Appointment time
  APTHOUEND HM End time
  APTMOB TEL Mobile phone
  APTNUM VCR Appointment chrono
  APTOBJ CLX Summary objective
  APTOPGNUM VCR Operation code
  APTOPGTYP AOB Operation type -> [AOB]ABREV =[BAP]APTOPGTYP (AOBJET) !Block
  APTORI M*15 Source [menu 2994: 1=Manual creation,2=Mass mail,3=Call campaign,4=Trade show,5=Media campaign,6=Marketing campaign]
  APTORIADI ADI Source -> [ADI]CODE =439;APTORIADI (ATABDIV) !Block
  APTORIAOB AOB Object code -> [AOB]ABREV =[BAP]APTORIAOB (AOBJET) !Block
  APTORITYP M*15 Source type [menu 3037: 1=Manual,2=Generated,3=Synchronization,4=Import]
  APTORIVCR VCR Document no.
  APTORIVCRL L*8 Line no.
  APTPJT PJT Project -> [PIM]PIM0 =[BAP]APTPJT (PIMPL) !Block
  APTPLC M Location [menu 955: 1=At customer's site,2=On our premises,3=Other]
  APTRECADD AIN Recording -> [AIN]AIN0 =[BAP]APTRECADD (CONTACTCRM) !Block
  APTREPNUM REP(10) Sales rep -> [REP]REP0 =[BAP]APTREPNUM (SALESREP) !Block
  APTRER RRS(15) Reservation -> [RRS]RRS0 =[BAP]APTRER (RESRES) !Block
  APTRPO CLX Overview
  APTSAO ADI Satisfaction -> [ADI]CODE =437;APTSAO (ATABDIV) !Block
  APTSAT SAT County
  APTTEL TEL Telephone
  APTTYP ADI Category -> [ADI]CODE =433;APTTYP (ATABDIV) !Block
  APTTYPADD M*15 Type [menu 954: 1=Contact,2=BP,3=Company,4=Site]
  APTWEE C*4 Appointment week
  APTZIP POS Postal code
  ATPADDCMT CLX Address description
  ATPREPMNA REP Organizer -> [REP]REP0 =[BAP]ATPREPMNA (SALESREP) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  FULDAY M*4 Entire day [menu 1: 1=No,2=Yes]
  NUMFULOBJ CLC Chrono txt file
  NUMFULRPO CLC Chrono txt file
  OBJFLG C*2 Flag text file
  RPOFLG C*2 Flag text file
  SALFCY FCY Sales site -> [FCY]FCY0 =[BAP]SALFCY (FACILITY) !Block
  TYPFULOBJ CLT Type text file
  TYPFULRPO CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BBLOB (BBB) - Special folders
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## BCKITOREN (BREN) - Backup integration reason
Notes: activity code KPO; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): BREN0 SEQID; BREN1 FICHIER+CREDAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BREN]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[BREN]DOSSIER (ADOSSIER) !Other
  FICHIER A*15 Tables to import
  INTMOT M*15 Reason [menu 8330: 1=Backup of production environment,2=Backup of test environment,3=Other not affecting document sequence numbers]
  SEQID L*8 Sequence no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BREN]UPDUSR (AUTILIS) !Other

## BCLOB (BCB) - Special folders
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## BETCPY (BCH) - Intercompany parameters
Keys (first = PK; D = duplicates allowed): BCH0 CLE
Fields:
  AUUID AUUID Single identifier
  CLE A*3 Key
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GRPCPYTPV AGF(25) Purchase co./group -> [AGF]AGF0 =[BCH]GRPCPYTPV (AGRPFCY) !Block
  GRPCPYTSO AGF(20) Sales co./group -> [AGF]AGF0 =[BCH]GRPCPYTSO (AGRPFCY) !Block
  GRPCPYTSV AGF(25) Sales co./group -> [AGF]AGF0 =[BCH]GRPCPYTSV (AGRPFCY) !Block
  PFIDEFNEG PFI Elt var. - -> [PFI]PFI0 =[BCH]PFIDEFNEG (PFOOTINV) !Block
  PFIDEFPOS PFI Elt var. + -> [PFI]PFI0 =[BCH]PFIDEFPOS (PFOOTINV) !Block
  PFINUM PFI(90) Purchase invoice element -> [PFI]PFI0 =[BCH]PFINUM (PFOOTINV) !Block
  PIVTYP TPV(25) Supp invoice type -> [TPV]TPV0 =PIVTYP;[V]GSUPCLE (TABPIVTYP) !Block
  SFINUM SFI(90) Sales invoice element -> [SFI]SFI0 =[BCH]SFINUM (SFOOTINV) !Block
  SIVTYP TSV(25) Customer invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Block
  SOHCAT M*15(20) Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHTYP TSO(20) Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BETCPYL (BCL) - Intercompany parameters
Keys (first = PK; D = duplicates allowed): BCL0 NUMERO; BCL1 FLG1234+NUMERO; BCL2 CRIBETCPY
Fields:
  AUUID AUUID Single identifier
  AUZBETFLG M*4 Authorization [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BCL]CREUSR (AUTILIS) !Other
  CRIBETCPY A*30 Criteria
  FLG1234 C*4 Flag
  FLG1CPYORI C*1 Flag
  FLG2FCYORI C*1 Flag
  FLG3CPYDES C*1 Flag
  FLG4FCYDES C*1 Flag
  GRPCPYDES AGF Ship-to cy/grp -> [AGF]AGF0 =[BCL]GRPCPYDES (AGRPFCY) !Block
  GRPCPYORI AGF Source comp/Group -> [AGF]AGF0 =[BCL]GRPCPYORI (AGRPFCY) !Block
  GRPFCYDES AGF Dest site/grp -> [AGF]AGF0 =[BCL]GRPFCYDES (AGRPFCY) !Block
  GRPFCYORI AGF Source site/Group -> [AGF]AGF0 =[BCL]GRPFCYORI (AGRPFCY) !Block
  NUMERO L*8 Number
  TRFPRI M*4 Price transfer [menu 1: 1=No,2=Yes]
  TYPBET M*15 Type [menu 2203: 1=Intersite,2=Intercompany]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BCL]UPDUSR (AUTILIS) !Other
  VCRTYP M*15 Document [menu 701: 40 values, see local-menus.md]
  VCRTYPDES M*15 Document [menu 701: 40 values, see local-menus.md]
  VLTFOOINV M*15 Valuation [menu 298: 1=Purchasing,2=Sales,3=Stock,4=Production,5=MPS,6=MRP,7=Projet]

## BILLLADC (BOLC) - Bill of lading contents
Keys (first = PK; D = duplicates allowed): BOLC0 BOLNUM+BOLLIN; BOLC1 BOLNUM+DOCNUMCON
Fields:
  AUUID AUUID Single identifier
  BOLLIN L*8 BOL line
  BOLNUM VCR BOL number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BOLC]CREUSR (AUTILIS) !Other
  DOCNUMCON A*20 Document number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOLC]UPDUSR (AUTILIS) !Other

## BILLLADD (BOLD) - Bill of lading detail
Keys (first = PK; D = duplicates allowed): BOLD0 BOLNUM+BOLLIN; BOLD1 BOLNUM+FRTCLS+PCK+NMFC (D)
Fields:
  AUUID AUUID Single identifier
  BOLLIN L*8 BOL line
  BOLNUM VCR BOL number
  COMMENT A*50 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BOLD]CREUSR (AUTILIS) !Other
  FRTCLS FRT Freight class -> [FRT]FRT0 =FRTCLS;[V]GSUPCLE (FRTCLS) !Block
  GROWEI WEI Gross weight
  NBRPCK QTY No. of packages
  NETWEI WEI Net weight
  NMFC FCC NMFC -> [FCC]FCC0 =1;NMFC (FRTCOMCOD) !Block
  PACWEI WEI Package weight
  PCK PCK Packaging -> [TPA]TPA0 =[BOLD]PCK (TABPACKAGE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOLD]UPDUSR (AUTILIS) !Other
  VOL VOL Volume
  VOU UOM Volume unit -> [TUN]TUN0 =[BOLD]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[BOLD]WEU (TABUNIT) !Block

## BILLLADH (BOLH) - Bill of lading header
Keys (first = PK; D = duplicates allowed): BOLH0 BOLNUM
Fields:
  ADJFLG M*4 Manual adjustment [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BLFTEX TXC BOL footer text
  BLHTEX TXC BOL header text
  BOLDAT D BOL date
  BOLNUM VCR BOL number
  BOLTYP M*15 BOL type [menu 2085: 1=Customer,2=Supplier,3=Miscellaneous]
  BPAADDLIG ADL(3) Ship-to address
  BPR BPR BP -> [BPR]BPR0 =[BOLH]BPR (BPARTNER) !Block
  BPRADD ADR Address code
  BPRNAM NAM(2) Ship-to customer
  BPTNUM BPT Carrier -> [BPT]BPT0 =[BOLH]BPTNUM (BPCARRIER) !Block
  CPY CPY Company -> [CPY]CPY0 =[BOLH]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BOLH]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[BOLH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  DOCNUM A*20 Reference document
  FCY FCY Site -> [FCY]FCY0 =[BOLH]FCY (FACILITY) !Block
  MDL MDL Delivery mode -> [TMD]TMD0 =[BOLH]MDL (TABMODELIV) !Block
  POSCOD POS Postal code
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRONUM A*20 PRO number act:KUS
  SAT SAT County
  SCAC A*4 SCAC code act:KUS
  TRAILER A*20 Trailer/Seal number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOLH]UPDUSR (AUTILIS) !Other

## BILLLADWRK (BOLW) - Bill of lading report
Notes: differs in V9.0 P12 (diff: AT3_BILLLADWRK.htm); differs in V10 P1 (diff: ATD_BILLLADWRK.htm)
Keys (first = PK; D = duplicates allowed): BOLW0 REQNUM+USER+BOLNUM+BOLLIN
Fields:
  AUUID AUUID Single identifier
  BOLLIN L*8 BOL line
  BOLNUM VCR BOL number
  COMMENT A*50 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BOLW]CREUSR (AUTILIS) !Other
  FRTCLS FRT Freight class -> [FRT]FRT0 =FRTCLS;[V]GSUPCLE (FRTCLS) !Block
  GROWEI WEI Gross weight
  KUSFLG C*4
  LAN LAN Language -> [TLA]TLA0 =[BOLW]LAN (TABLAN) !Block
  NBRPCK QTY No. of packages
  NMFC FCC NMFC -> [FCC]FCC0 =1;NMFC (FRTCOMCOD) !Block
  OVRFLOW C*4
  PCK PCK Packaging -> [TPA]TPA0 =[BOLW]PCK (TABPACKAGE) !Block
  REQNUM L*8 Request no.
  TEXTE A*80 Text
  TEXTE2 A*250 Text
  TOTNBRPCK QTY Total
  TXTNUM1 C*4
  TXTNUM2 C*4
  TXTNUM3 C*4
  TXTNUM4 C*4
  TXTNUM5 C*4
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOLW]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[BOLW]USER (AUTILIS) !Other
  WEU UOM Weight unit -> [TUN]TUN0 =[BOLW]WEU (TABUNIT) !Block

## BOM (BOH) - Header BOMS
Keys (first = PK; D = duplicates allowed): BOH0 ITMREF+BOMALT+BOMALTTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[BOH]ACSCOD (ACCCOD) !Block
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BOHENDDAT D Valid to
  BOHSTRDAT D Valid from
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMDESAXX AX3 Header title
  BOMRLE A*10 Review level
  CFGVCRNUM VCR Journal number config act:CFG
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  HEATEX TXC Header text
  IDENT1 ID1 Identifier 1
  ITMREF ITM Parent product -> [ITM]ITM0 =[BOH]ITMREF (ITMMASTER) !Block
  PLMATTURL A*250 Linked documents
  QTYCOD M*15 Management unit [menu 225: 1=One,2=Per hundred,3=Per thousand,4=Percentage,5=By lot]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USESTA M*15 Use status [menu 240: 1=In development,2=Available to use]

## BOMD (BOD) - Detail BOMs
Keys (first = PK; D = duplicates allowed): BOD0 ITMREF+BOMALT+BOMSEQ+CPNITMREF+BOMALTTYP; BOD1 CPNITMREF+ITMREF+BOMALT+BOMSEQ+BOMALTTYP; BOD2 ITMREF+BOMALT+BOMSEQ+BOMSEQNUM+CPNITMREF+BOMALTTYP; BOD3 BOMALT+CPNITMREF+BOMALTTYP+ITMREF+BOMSEQ; BOD4 BOMALT+ITMREF+BOMALTTYP+CPNITMREF+BOMSEQ
Fields:
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMENDDAT D Valid to
  BOMENDLOT LOT Last valid lot
  BOMOFS C*4 Operation lead time
  BOMQTY QTY UOM link quantity
  BOMSEQ C*4 Sequence
  BOMSEQNUM C*2 Sequence remainder
  BOMSHO DES Link description
  BOMSTRDAT D Valid from
  BOMSTRLOT LOT First valid lot
  BOMSTUCOE COE UOM-STK factor
  BOMTEXNUM TXC Link text
  BOMUOM UOM UOM -> [TUN]TUN0 =[BOD]BOMUOM (TABUNIT) !Block
  CPNITMREF ITM Component -> [ITM]ITM0 =[BOD]CPNITMREF (ITMMASTER) !Block
  CPNOPE OPE Routing operation
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTFLG M*4 Valuation [menu 1: 1=No,2=Yes]
  ECCRLEGRP C*4 Revision group act:ECC
  ECCVALMAJ ICVVAL Major version act:ECC
  ECCVALMIN ICVVAL Minor version act:ECC
  EXPNUM L*8 Export number
  FORQTY FOR Qty formula -> [TFO]TFO0 =54;FORQTY (TABFOR) !Block
  FORSEL FOR Selection formula -> [TFO]TFO0 =53;FORSEL (TABFOR) !Block
  INVPRN M*4 Print invoice [menu 1: 1=No,2=Yes]
  ITMREF ITM Parent product -> [ITM]ITM0 =[BOD]ITMREF (ITMMASTER) !Block
  ITMTOLNEG COE Weighing tolerance -(%) act:MWM
  ITMTOLPOS COE Weighing tolerance +(%) act:MWM
  LEVSET M*15 Setup level [menu 2394: 1=,2=SHI record,3=Product-site,4=BOM] act:MWM
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LIKRLE A*10 Link review index
  NDEPRN M*4 Print packing slip [menu 1: 1=No,2=Yes]
  OCNPRN M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  OPENUMLEV C*1 Routing operation suffix
  PICPRN M*4 Materials requisition printing [menu 1: 1=No,2=Yes]
  PKC M*15 Pick list code [menu 2328: 10 values, see local-menus.md] act:MWM
  QTYRND M*15 Quantity rounding [menu 293: 1=Round to the nearest,2=Greater than,3=Less than]
  SCA DCB*3.3 Scrap factor %
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BOMPRN (BOP) - Print BOMs
Notes: differs in V9.0 P12 (diff: AT3_BOMPRN.htm)
Keys (first = PK; D = duplicates allowed): BOP0 BOPUID+BOMALTTYP+BOMALT+ITMREF+LIG
Fields:
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BOMALT C*2 BOM code
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMENDDAT D Valid to
  BOMENDLOT LOT Last valid lot
  BOMOFS C*4 Operation lead time
  BOMSEQ C*4 Sequence
  BOMSEQNUM C*2 Sequence remainder
  BOMSHO DES Link description
  BOMSTRDAT D Valid from
  BOMSTRLOT LOT First valid lot
  BOMTEXNUM TXC Link text
  BOPUID L*8 Process no.
  CPNITMREF ITM Component -> [ITM]ITM0 =[BOP]CPNITMREF (ITMMASTER) !BSRA
  CPNOPE OPE Routing operation
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GROQTY QTY Gross quantity
  INVPRN M*4 Print invoice [menu 1: 1=No,2=Yes]
  ITMREF ITM Parent product -> [ITM]ITM0 =[BOP]ITMREF (ITMMASTER) !BSRA
  LIG C*4 Line number
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LIKRLE A*10 Link review index
  NDEPRN M*4 Print packing slip [menu 1: 1=No,2=Yes]
  NETQTY QTY Net quantity
  NIV C*2 Level
  OCNPRN M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  OPENUMLEV C*1 Routing operation suffix
  PICPRN M*4 Materials requisition printing [menu 1: 1=No,2=Yes]
  PKC M*15 Pick list code [menu 2328: 10 values, see local-menus.md] act:MWM
  QTYRND A*10 Quantity rounding
  SCA DCB*3.3 Scrap factor %
  STOFCY FCY Storage site -> [FCY]FCY0 =[BOP]STOFCY (FACILITY) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOP]UPDUSR (AUTILIS) !Other

## BOMRET (BMR) - Component requirements
Keys (first = PK; D = duplicates allowed): BMR0 BMRUID+ITMREF+NIV
Fields:
  AUUID AUUID Single identifier
  AVAQTY QTY Available quantity
  BMRUID L*8 Process no.
  BOMALT C*2 BOM code
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATREF D Reference date
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  FLG A*1 Total
  GENFLG M*4 Generic [menu 1: 1=No,2=Yes]
  IMULT C*4
  INTFLG M*4 Intermediary [menu 1: 1=No,2=Yes]
  ITMCMP ITM Parent product -> [ITM]ITM0 =[BMR]ITMCMP (ITMMASTER) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[BMR]ITMREF (ITMMASTER) !Block
  ITMSTA M*15 Product status [menu 246: 1=Active,2=In development,3=On shortage,4=Not renewed,5=Obsolete,6=Not usable]
  LTI LTI Lead time
  LTIUOM M*15 Time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  MFGFLG M*4 Manufactured [menu 1: 1=No,2=Yes]
  NIV C*2 Level
  PHAFLG M*4 Phantom [menu 1: 1=No,2=Yes]
  PURFLG M*4 Bought [menu 1: 1=No,2=Yes]
  RETQTY QTY Requirement quantity
  SALFLG M*4 Sold [menu 1: 1=No,2=Yes]
  SCPFLG M*4 Subcontracted [menu 1: 1=No,2=Yes]
  SCSFLG M*4 Subcontract [menu 1: 1=No,2=Yes]
  SHTQTY QTY Quantity shortage
  STOFCY FCY Storage site -> [FCY]FCY0 =[BMR]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[BMR]STU (TABUNIT) !Block
  TCLCOD ITG Category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Block
  TOOFLG M*4 Tools [menu 1: 1=No,2=Yes]
  TRTCOD C*4 Processing
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BMR]UPDUSR (AUTILIS) !Other
  USESTA M*15 Use status [menu 240: 1=In development,2=Available to use]

## BOMWUS (BOW) - Where-used BOM
Keys (first = PK; D = duplicates allowed): BOW0 BOWUID+ITMREF+BOMALT+BOMSEQ+CPNITMREF+BOMALTTYP; BOW1 BOWUID+BOMALT+BOMALTTYP+ITMREF+BOMSEQ+CPNITMREF
Fields:
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMENDDAT D Valid to
  BOMENDLOT LOT Last valid lot
  BOMOFS C*4 Operation lead time
  BOMQTY QTY UOM link quantity
  BOMSEQ C*4 Sequence
  BOMSEQNUM C*2 Sequence remainder
  BOMSHO DES Link description
  BOMSTRDAT D Valid from
  BOMSTRLOT LOT First valid lot
  BOMSTUCOE COE UOM-STK factor
  BOMTEXNUM TXC Link text
  BOMUOM UOM UOM -> [TUN]TUN0 =[BOW]BOMUOM (TABUNIT) !Block
  BOWUID L*8 Process no.
  CPNDES DES Description
  CPNITMREF ITM Component -> [ITM]ITM0 =[BOW]CPNITMREF (ITMMASTER) !Block
  CPNOPE OPE Routing operation
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GROQTY QTY Gross quantity
  IMULT C*4
  INVPRN M*4 Print invoice [menu 1: 1=No,2=Yes]
  ITMREF ITM Parent product -> [ITM]ITM0 =[BOW]ITMREF (ITMMASTER) !Block
  JMULT C*4
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LIKRLE A*10 Link review index
  NDEPRN M*4 Print packing slip [menu 1: 1=No,2=Yes]
  NETQTY QTY Net quantity
  NIV C*2 Level
  OCNPRN M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  OPENUMLEV C*1 Routing operation suffix
  PICPRN M*4 Materials requisition printing [menu 1: 1=No,2=Yes]
  PKC M*15 Pick list code [menu 2328: 10 values, see local-menus.md] act:MWM
  QTYRND A*10 Quantity rounding
  SCA DCB*3.3 Scrap factor %
  TRTCOD C*4 Processing
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOW]UPDUSR (AUTILIS) !Other

## BPADDRESSSA (BPASA) - Addresses
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## BPARTNER (BPR) - Business partner
Notes: differs in V9.0 P12 (diff: AT3_BPARTNER.htm); differs in V10 P1 (diff: ATD_BPARTNER.htm)
Keys (first = PK; D = duplicates allowed): BPR0 BPRNUM; BPR1 BPRSHO (D); BPR2 BETFCY+FCY+BPRNUM
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =17;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACCNONREI ADR Non resident account
  ACS ACS Report access code -> [ACS]ACS0 =[BPR]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[BPR]BIDCRY (TABCOUNTRY) !Block
  BIDNUM BID Dft. bank details
  BPAADD ADR Default address
  BPCFLG M*4 Customer [menu 1: 1=No,2=Yes]
  BPPFLG M*4 Public sector [menu 1: 1=No,2=Yes] act:MAXPD
  BPRACC M*4 Miscellaneous BP [menu 1: 1=No,2=Yes]
  BPRFBDMAG M*4 Mailing prohibited [menu 1: 1=No,2=Yes]
  BPRFLG M*4(4) Miscellaneous [menu 1: 1=No,2=Yes]
  BPRGTETYP GTE Entry type -> [GTE]GTE0 =BPRGTETYP;[V]GSUPCLE (GTYPACCENT) !Block
  BPRLOG A*10 Acronym
  BPRNAM NAM(2) Company name
  BPRNUM BPR BP -> [BPR]BPR0 =[BPR]BPRNUM (BPARTNER) !Other
  BPRSHO SHO Short description
  BPSFLG M*4 Supplier [menu 1: 1=No,2=Yes]
  BPTFLG M*4 Carrier [menu 1: 1=No,2=Yes]
  BRGCOD BCG Category -> [BCG]BCG0 =[BPR]BRGCOD (BPCCATEG) !BSRA
  BRGOBJ A*3 Cust/suppl cat
  CCNFLG M*4 Grantor [menu 1: 1=No,2=Yes] act:CCN
  CFOEXD M*4 Cash excluded [menu 1: 1=No,2=Yes] act:CFOM
  CNTNAM NAM Default contact
  CPYREL M*15 Related company [menu 3664: 1=Not related,2=Voting rights >= 10%,3=Voting rights < 10%] act:PBDPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRN CRT Site tax ID no.
  CRY CRY Country -> [TCY]TCY0 =[BPR]CRY (TABCOUNTRY) !Block
  CSLBPR BPR Partner -> [BPR]BPR0 =[BPR]CSLBPR (BPARTNER) !Block act:PRCSL
  CUR CUR Currency -> [TCU]TCU0 =[BPR]CUR (TABCUR) !Block
  DOCTYP M*4 Document type [menu 2004: 1=Site tax ID number,2=Intracommunity tax ID number,3=Passport,4=Official document,5=Fiscal residence certificate,6=Others] act:KSP
  DOOFLG M*4 Service caller [menu 1: 1=No,2=Yes]
  EECNUM A*20 EU VAT no. act:DEB
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCTFLG M*4 Factor [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[BPR]FCY (FACILITY) !Block
  FISCOD A*20 Fiscal code act:KIT
  GRUCOD A*10 Consolidation act:CSL
  GRUGPY A*10 Consolidation group act:CSL
  LAN LAN Language -> [TLA]TLA0 =[BPR]LAN (TABLAN) !Block
  LEGETT M*4 Natural person [menu 1: 1=No,2=Yes]
  MODPAM ADI CFONB payment -> [ADI]CODE =311;MODPAM (ATABDIV) !Block
  NAF NAF SIC code act:KFR
  PPTFLG M*4 Prospect [menu 1: 1=No,2=Yes]
  PRVFLG M*4 Service supplier [menu 1: 1=No,2=Yes]
  PTHFLG C*4 Ship-to act:KAG
  REPFLG M*4 Sales rep [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VATNUM A*15 IVA partita act:KIT

## BPCARRIER (BPT) - Carriers
Keys (first = PK; D = duplicates allowed): BPT0 BPTNUM; BPT1 BPTNAM (D)
Fields:
  ADL MD1 Proport amount
  AUUID AUUID Single identifier
  BKT WEI Bracket value
  BPAADD ADR Default address
  BPTFOR FOR Formula -> [TFO]TFO0 =4;BPTFOR (TABFOR) !Block
  BPTNAM NAM Company name
  BPTNUM BPR Carrier -> [BPR]BPR0 =[BPT]BPTNUM (BPARTNER) !Block
  BPTPLITYP M*6 Amount - tax/+ tax [menu 243: 1=Exclude tax,2=Include tax]
  BPTSHO SHO Short description
  CFY CPY(20) Company -> [CPY]CPY0 =[BPT]CFY (COMPANY) !Other act:MUL
  CNTNAM NAM Default contact
  COEWEIVOL COE Coefficient
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[BPT]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  FXDAMT MD1 Fixed amount
  NBPLI C*2 No. of price columns
  NTRFLG M*4 Print BOL [menu 1: 1=No,2=Yes]
  PLIBKT WEI Bracket value act:BPW
  PLIFLG M*4 Price list management [menu 1: 1=No,2=Yes]
  PLIMAX WEI End date act:BPW
  PLIUOMRND WEI Rounding act:BPW
  SCAC A*4 SCAC code act:KUS
  TSDFRE MD1(5) Freight thresholds
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VOU UOM Volume unit -> [TUN]TUN0 =[BPT]VOU (TABUNIT) !Block
  WEIRND M*4 Round the weight [menu 238: 1=Band <,2=Band >,3=Nearest band]
  WEU UOM Weight unit -> [TUN]TUN0 =[BPT]WEU (TABUNIT) !Block

## BPCCATEG (BCG) - Customer category
Notes: differs in V9.0 P12 (diff: AT3_BPCCATEG.htm); differs in V10 P1 (diff: ATD_BPCCATEG.htm)
Keys (first = PK; D = duplicates allowed): BCG0 BCGCOD
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =2;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BCGCOD BCG Category -> [BCG]BCG0 =[BCG]BCGCOD (BPCCATEG) !Delete
  BCGDES DES Description
  BCGSHO SHO Short description
  BPCTYP M*15 Customer type [menu 401: 1=Normal,2=Miscellaneous,3=Intra-company,4=Prospect]
  BPTNUM BPT Carrier -> [BPT]BPT0 =[BCG]BPTNUM (BPCARRIER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  COMCAT M*15 Commission category [menu 403: 1=Category 1,2=Category 2,3=Category 3]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMOD M*15 Creation method [menu 223: 1=Direct,2=With validation]
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[BCG]CRY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[BCG]CUR (TABCUR) !Block
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DESAXX AX3 Description
  DIA GDA Account structure -> [GDA]GDA0 =DIA (GDIAACC) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[BCG]DIE (GDIE) !Block act:ANA
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DUDCLC M*15 Due date origin [menu 407: 1=Invoice date,2=Shipment date]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[BCG]EECICT (INCOTERM) !Block
  EECINCRAT RAT Intras. incr. act:DEB
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXPNUM L*8 Export number
  FCTNUM FCT Factor -> [FCT]FCT0 =[BCG]FCTNUM (FACTOR) !Block act:FCT
  FREINV M*15 Freight invoicing [menu 402: 1=Invoiced,2=Not invoiced,3=Up to threshold 1,4=Up to threshold 2,5=Up to threshold 3,6=Up to threshold 4,7=Up to threshold 5]
  FUPMINAMT MD1 Minimum reminder act:FUP
  FUPTYP M*15 Reminder type [menu 235: 1=No reminder,2=By invoice,3=Global,4=Global by level,5=Global by date] act:FUP
  GRP A*5 Group act:FUP
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVDTAAMT DCB*11.4 Invoicing element act:SFI
  INVPER M*15 Invoice period [menu 406: 1=Per request,2=Daily,3=Weekly,4=10-day period,5=2-week period,6=Monthly]
  LAN LAN Language -> [TLA]TLA0 =[BCG]LAN (TABLAN) !Block
  LNDAUZ M*4 Loan authorized [menu 1: 1=No,2=Yes] act:LND
  MDL MDL Delivery mode -> [TMD]TMD0 =[BCG]MDL (TABMODELIV) !Block
  NDEFLG M*4 Print packing slip [menu 1: 1=No,2=Yes]
  NPRFLG M*4 Print picking ticket [menu 1: 1=No,2=Yes]
  OCNFLG M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  ORDCLE M*4 Close unfilled lines [menu 1: 1=No,2=Yes]
  ORDMINAMT MD1 Min order amt
  OSTAUZ MD1 Authorized credit
  OSTCTL M*15 Credit control [menu 234: 1=Check,2=No check,3=Hold]
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[BCG]PAYBAN (BANK) !Block
  PRITYP M*6 Price type [menu 243: 1=Exclude tax,2=Include tax]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REFCOU ANM Customer sequence -> [ANM]ANM0 =[BCG]REFCOU (ACODNUM) !Block
  REP REP Sales rep -> [REP]REP0 =[BCG]REP (SALESREP) !Block act:REC
  REPDLV REP Sales rep -> [REP]REP0 =[BCG]REPDLV (SALESREP) !Block act:RED
  SHOAXX AX1 Short description
  SOIPER M*15 Note type [menu 404: 1=Per request,2=Weekly,3=10-day period,4=2-week period,5=Monthly]
  STOFCY FCY Shipment site -> [FCY]FCY0 =[BCG]STOFCY (FACILITY) !Block
  TPMCOD TPM Template code -> [TPM]TPM0 =TPMCOD (TABPRTMOD) !RTZ
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Block act:STC
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD UVY Unavailable period -> [TUV]UVY0 =[BCG]UVYCOD (TABUNAVAIL) !Block
  UVYDAY1 M*4 Monday [menu 1: 1=No,2=Yes]
  UVYDAY2 M*4 Tuesday [menu 1: 1=No,2=Yes]
  UVYDAY3 M*4 Wednesday [menu 1: 1=No,2=Yes]
  UVYDAY4 M*4 Thursday [menu 1: 1=No,2=Yes]
  UVYDAY5 M*4 Friday [menu 1: 1=No,2=Yes]
  UVYDAY6 M*4 Saturday [menu 1: 1=No,2=Yes]
  UVYDAY7 M*4 Sunday [menu 1: 1=No,2=Yes]
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block

## BPCUSTMVT (MVC) - Customer transactions
Keys (first = PK; D = duplicates allowed): MVC0 BPCRSK+CPY+BPCNUM+CUR; MVC1 BPCNUM+CPY (D)
Fields:
  ACCCUR CUR Accounting currency -> [TCU]TCU0 =[MVC]ACCCUR (TABCUR) !Block
  AUUID AUUID Single identifier
  BLCC MD1 Accounting balance
  BLCL MD1 Accounting balance
  BLCR MD1 Accounting balance
  BPCNUM BPR Customer -> [BPR]BPR0 =[MVC]BPCNUM (BPARTNER) !Delete
  BPCRSK BPR Risk BP -> [BPR]BPR0 =[MVC]BPCRSK (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[MVC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[MVC]CUR (TABCUR) !Block
  DLVOSTC MD1 Delivery in progress
  DLVOSTL MD1 Delivery in progress
  DLVOSTR MD1 Delivery in progress
  EXPNUM L*8 Export number
  FCTOST MD1 In progress factor act:FCT
  FUPDAT D Last reminder date act:FUP
  FUPLEV C*2 Reminder level act:FUP
  LNDBPCATIC MD1 Sold-to on loan act:LND
  LNDBPCATIL MD1 Sold-to on loan act:LND
  LNDBPCATIR MD1 Sold-to on loan act:LND
  LNDBPCNOTC MD1 On loan -tax act:LND
  LNDBPCNOTL MD1 On loan -tax act:LND
  LNDBPCNOTR MD1 On loan -tax act:LND
  LNDBPIATIC MD1 On loan act:LND
  LNDBPIATIL MD1 On loan act:LND
  LNDBPIATIR MD1 On loan act:LND
  LNDBPINOTC MD1 On loan excl tax act:LND
  LNDBPINOTL MD1 On loan excl tax act:LND
  LNDBPINOTR MD1 On loan excl tax act:LND
  LNDDLVC MD1 Delivered on loan act:LND
  LNDDLVL MD1 Delivered on loan act:LND
  LNDDLVR MD1 Delivered on loan act:LND
  MAXFUPLEV C*2 Max reminder level act:FUP
  NIVDLVC MD1 Delivered not invoiced
  NIVDLVL MD1 Delivered not invoiced
  NIVDLVR MD1 Delivered not invoiced
  NPTINVC MD1 Unposted invoices
  NPTINVL MD1 Unposted invoices
  NPTINVR MD1 Unposted invoices
  NYTBILC MD1(3) Drafts
  NYTBILL MD1(3) Drafts
  NYTBILR MD1(3) Drafts
  ORDBPCATIC MD1 Sold-to on order
  ORDBPCATIL MD1 Sold-to on order
  ORDBPCATIR MD1 Sold-to on order
  ORDBPCNOTC MD1 On order excl tax sold-to cus
  ORDBPCNOTL MD1 On order excl tax sold-to cus
  ORDBPCNOTR MD1 On order excl tax sold-to cus
  ORDBPIATIC MD1 On order
  ORDBPIATIL MD1 On order
  ORDBPIATIR MD1 On order
  ORDBPINOTC MD1 On order ex-tax
  ORDBPINOTL MD1 On order ex-tax
  ORDBPINOTR MD1 On order ex-tax
  QUOATIC MD1 In curr tax inc
  QUOATIL MD1 In curr tax inc
  QUOATIR MD1 Line amt. + tax
  QUONOTC MD1 In curr tax exc
  QUONOTL MD1 In curr tax exc
  QUONOTR MD1 Line amt. - tax
  UNPDAT D Last late payment date act:FUP
  UNPNBR C*2 Late payments act:FUP
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BPCUSTOMER (BPC) - Customers
Notes: differs in V9.0 P12 (diff: AT3_BPCUSTOMER.htm); differs in V10 P1 (diff: ATD_BPCUSTOMER.htm)
Keys (first = PK; D = duplicates allowed): BPC0 BPCNUM; BPC1 BPCNAM (D)
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =2;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AEIFLG C*4 Electronic invoice act:ELINV
  AGTPCP C*4 VAT collection agent act:KAG
  AGTSATTAX C*4 Regional taxes act:KAG
  AUUID AUUID Single identifier
  BCGCOD BCG Category -> [BCG]BCG0 =[BPC]BCGCOD (BPCCATEG) !Block
  BELVATSUB M*4 Subject to tax [menu 1: 1=No,2=Yes] act:KBE
  BPAADD ADR Default address
  BPAINV ADR Address
  BPAPYR ADR Address
  BPCBPSNUM A*15 Our supplier no.
  BPCCDTISR BPR Insurance company -> [BPR]BPR0 =[BPC]BPCCDTISR (BPARTNER) !Block
  BPCGRU BPR Group customer -> [BPR]BPR0 =[BPC]BPCGRU (BPARTNER) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[BPC]BPCINV (BPARTNER) !Block
  BPCNAM NAM Company name
  BPCNUM BPR Customer -> [BPR]BPR0 =[BPC]BPCNUM (BPARTNER) !Delete
  BPCPYR BPR Pay-by customer -> [BPR]BPR0 =[BPC]BPCPYR (BPARTNER) !Block
  BPCREM A*250 Notes
  BPCRSK BPR Risk customer -> [BPR]BPR0 =[BPC]BPCRSK (BPARTNER) !Block
  BPCSHO SHO Short description
  BPCSNCDAT D Customer since
  BPCSTA M*4 Active customer [menu 1: 1=No,2=Yes]
  BPCTYP M*15 Type [menu 401: 1=Normal,2=Miscellaneous,3=Intra-company,4=Prospect]
  BPDADD ADR Ship-to customer address
  BUS ADI Business -> [ADI]CODE =425;BUS (ATABDIV) !RTZ
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CDTISR MD1 Credit insurance
  CDTISRDAT D Insurance date
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CNTEFAT AIN Contact -> [AIN]AIN0 =[BPC]CNTEFAT (CONTACTCRM) !Block act:EFAT
  CNTFIRDAT D First contact date
  CNTLASDAT D Last contact date act:PPT
  CNTLASTYP M*10 Last contact type [menu 431: 1=No type,2=Telephone,3=Visit,4=Courier,5=Mail,6=Mass mailing] act:PPT
  CNTNAM NAM Default contact
  CNTNEXDAT D Next contact date act:PPT
  CNTNEXTYP M*10 Next contact type [menu 431: 1=No type,2=Telephone,3=Visit,4=Courier,5=Mail,6=Mass mailing] act:PPT
  COMCAT M*15 Commission category [menu 403: 1=Category 1,2=Category 2,3=Category 3]
  COTCHX COT Service contract -> [COT]COT0 =COTCHX (CONTTEMPL) !RTZ
  COTPITRQD L*8 Tokens necessary
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSHVATRGM M*4(9) Tax rule [menu 1: 1=No,2=Yes] act:KPO
  CUR CUR Currency -> [TCU]TCU0 =[BPC]CUR (TABCUR) !Block
  DAYMON C*2(6) Day of the month
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIA GDA Account structure -> [GDA]GDA0 =[BPC]DIA (GDIAACC) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[BPC]DIE (GDIE) !Block act:ANA
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DUDCLC M*15 Due date origin [menu 407: 1=Invoice date,2=Shipment date]
  ELECTINV M*4 Electronic invoice [menu 1: 1=No,2=Yes] act:EFAT
  EXPNUM L*8 Export number
  FCTNUM FCT Factor -> [FCT]FCT0 =[BPC]FCTNUM (FACTOR) !Block act:FCT
  FLGSATTAX C*4 Collection agent act:KAG
  FREINV M*15 Freight invoicing [menu 402: 1=Invoiced,2=Not invoiced,3=Up to threshold 1,4=Up to threshold 2,5=Up to threshold 3,6=Up to threshold 4,7=Up to threshold 5]
  FUPMINAMT MD1 Minimum reminder act:FUP
  FUPTYP M*15 Reminder type [menu 235: 1=No reminder,2=By invoice,3=Global,4=Global by level,5=Global by date] act:FUP
  GRP FGP Group -> [FGP]FGP0 =[BPC]GRP (FUPGRP) !Block act:FUP
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[BPC]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVPER M*15 Invoice period [menu 406: 1=Per request,2=Daily,3=Weekly,4=10-day period,5=2-week period,6=Monthly]
  INVTEX TXC Invoice header text
  LNDAUZ M*4 Loan authorized [menu 1: 1=No,2=Yes] act:LND
  MTCFLG M*4 Matchable [menu 1: 1=No,2=Yes]
  OCNFLG M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  ORDCLE M*4 Close unfilled lines [menu 1: 1=No,2=Yes]
  ORDFIRDAT D First order date
  ORDMINAMT MD1 Min order amt
  ORDTEX TXC Ord header text
  ORIPPT ADI Source -> [ADI]CODE =413;ORIPPT (ATABDIV) !RTZ
  OSTAUZ MD1 Authorized credit
  OSTCTL M*15 Credit control [menu 234: 1=Check,2=No check,3=Hold]
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[BPC]PAYBAN (BANK) !BSRA
  PITCDT L*8 Token credits
  PITCPT L*8 Additional info
  PPTFLG M*4 Prospect [menu 1: 1=No,2=Yes] act:PPT
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  QUOLASDAT D Last quote date act:PPT
  REP REP Sales rep -> [REP]REP0 =[BPC]REP (SALESREP) !Block act:REC
  SATTAX A*1 Provinces act:KAG
  SOIPER M*15 Note type [menu 404: 1=Per request,2=Weekly,3=10-day period,4=2-week period,5=Monthly]
  STRDATEFAT D Start date act:EFAT
  TOTPIT L*8 Total credit
  TPMCOD TPM Template code -> [TPM]TPM0 =TPMCOD (TABPRTMOD) !RTZ
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Block act:STC
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD2 UVY Unavailable period -> [TUV]UVY0 =[BPC]UVYCOD2 (TABUNAVAIL) !Block
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VATENDDAT D(9) VAT end date act:KPO
  VATEXN A*15 Exemption no.
  VATSTRDAT D(9) VAT start date act:KPO

## BPDLVCUST (BPD) - Ship-to customer
Keys (first = PK; D = duplicates allowed): BPD0 BPCNUM+BPAADD; BPD1 RCPFCY+BPCNUM+BPAADD
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Delivery address
  BPCLOC LOC Loan location -> [STC]STC0 =STOFCY;BPCLOC (STOLOC) !Block
  BPCNUM BPR Customer -> [BPR]BPR0 =[BPD]BPCNUM (BPARTNER) !Delete
  BPDEXNFLG A*1 Exemption flag act:KUS
  BPDNAM NAM(2) Company name
  BPTNUM BPT Carrier -> [BPT]BPT0 =[BPD]BPTNUM (BPCARRIER) !Block
  CPY CPY Company -> [CPY]CPY0 =[BPD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYLTI C*3 Delivery LT in days
  DLVPIO M*15 Delivery priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  DLVTEX TXC Deliv header text
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[BPD]EECICT (INCOTERM) !Block
  EECINCRAT RAT Intrastat increase act:DEB
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM A*20 EU identification act:DEB
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[BPD]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  ICTCTY CTY Incoterm town
  INSCTYFLG A*1 City interior flag act:KUS
  LAN LAN Language -> [TLA]TLA0 =[BPD]LAN (TABLAN) !Block
  MDL MDL Delivery mode -> [TMD]TMD0 =[BPD]MDL (TABMODELIV) !Block
  NDEFLG M*4 Print packing slip [menu 1: 1=No,2=Yes]
  NPRFLG M*4 Print pick ticket [menu 1: 1=No,2=Yes]
  PRPTEX TXC Picking header text
  RCPFCY FCY Receiving site -> [FCY]FCY0 =[BPD]RCPFCY (FACILITY) !Block
  REP REP Sales rep -> [REP]REP0 =[BPD]REP (SALESREP) !Block act:RED
  SCOLOC LOC Subcontract loc. -> [STC]STC0 =STOFCY;SCOLOC (STOLOC) !Block
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[BPD]STOFCY (FACILITY) !Block
  TAXEXN A*15 Tax exemption no. act:KUS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[BPD]UVYCOD (TABUNAVAIL) !Block
  UVYDAY1 M*4 Monday [menu 1: 1=No,2=Yes]
  UVYDAY2 M*4 Tuesday [menu 1: 1=No,2=Yes]
  UVYDAY3 M*4 Wednesday [menu 1: 1=No,2=Yes]
  UVYDAY4 M*4 Thursday [menu 1: 1=No,2=Yes]
  UVYDAY5 M*4 Friday [menu 1: 1=No,2=Yes]
  UVYDAY6 M*4 Saturday [menu 1: 1=No,2=Yes]
  UVYDAY7 M*4 Sunday [menu 1: 1=No,2=Yes]
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block

## BPEXCEPT (BPE) - BP-Company exception
Notes: activity code MUL; differs in V9.0 P12 (diff: AT3_BPEXCEPT.htm)
Keys (first = PK; D = duplicates allowed): BPE0 BPRNUM+CPY
Fields:
  ACCBPC CAC Cust accounting code -> [CAC]CAC0 =2;ACCBPC;[V]GSUPCLE (GACCCODE) !Block
  ACCBPS CAC Supplier acc code -> [CAC]CAC0 =3;ACCBPS;[V]GSUPCLE (GACCCODE) !Block
  ACEAUZ M*4 Authorization [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[BPE]BPRNUM (BPARTNER) !Delete
  CFOEXDCPY M*4 Cash excluded [menu 1: 1=No,2=Yes] act:CFOM
  CPY CPY Company -> [CPY]CPY0 =[BPE]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BPE]CREUSR (AUTILIS) !Other
  DEPBPC TDA Customer early disc -> [TDA]TDA0 =DEPBPC;[V]GSUPCLE (TABDEPAGIO) !Block
  DEPBPS TDA Supplier early disc -> [TDA]TDA0 =DEPBPS;[V]GSUPCLE (TABDEPAGIO) !Block
  PAYBANBVR BAN Payment bank ISR -> [BAN]BAN0 =[BPE]PAYBANBVR (BANK) !Block act:KSW
  PAYDAY C*2 Contractual period act:MAXPD
  PTEBPC PTE Customer payment -> [TPT]TPT0 =PTEBPC;[V]GCURLEG;1 (TABPAYTERM) !Block
  PTEBPS PTE Supplier payment -> [TPT]TPT0 =PTEBPS;[V]GCURLEG;1 (TABPAYTERM) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BPE]UPDUSR (AUTILIS) !Other
  VACBPC TVB Cust tax rule -> [TVB]TVB0 =VACBPC;[V]GSUPCLE (TABVACBPR) !Block
  VACBPR TVB BP tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACBPS TVB Supplier tax rule -> [TVB]TVB0 =VACBPS;[V]GSUPCLE (TABVACBPR) !Block

## BPMISC (BPM) - Order-giver/miscellaneous BP
Keys (first = PK; D = duplicates allowed): BPM0 BPRTYP+BPRNUM
Fields:
  ALHX A*30(5) Alphanumeric fields
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[BPM]BPRNUM (BPARTNER) !Delete
  BPRTYP ABR BP type
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATX D(5) Date fields
  DCBX DCB*9.2(5) Decimal field
  INTX L*8(5) Integer field
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BPMISCCGF (BPG) - Miscellaneous BP configuration
Keys (first = PK; D = duplicates allowed): BPG0 BPRTYP+LAN (D)
Fields:
  AUUID AUUID Single identifier
  BPRTYP A*10 BP type
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BPG]CREUSR (AUTILIS) !Other
  LAN A*10 Language
  TTRALH A*30(5) Alpha field title
  TTRBLC A*30(4) Block title
  TTRDAT A*30(5) Date field title
  TTRDCB A*30(5) Decimal field title
  TTRINT A*30(5) Integer field title
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BPG]UPDUSR (AUTILIS) !Other

## BPSCATEG (BSG) - Supplier category
Keys (first = PK; D = duplicates allowed): BSG0 BSGCOD
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =3;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount] act:PFI
  AUUID AUUID Single identifier
  BOX1099 A*4 1099 box act:S1099
  BPSTYP M*15 Supplier type [menu 501: 1=Normal,2=Prospect,3=Miscellaneous]
  BPTNUM BPT Carrier -> [BPT]BPT0 =[BSG]BPTNUM (BPCARRIER) !Block
  BSGCOD BSG Category -> [BSG]BSG0 =[BSG]BSGCOD (BPSCATEG) !Delete
  BSGDES DES Description
  BSGSHO SHO Short description
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMOD M*15 Creation method [menu 223: 1=Direct,2=With validation]
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[BSG]CRY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[BSG]CUR (TABCUR) !Delete
  DADFLG M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DESAXX AX3 Description
  DIA GDA Account structure -> [GDA]GDA0 =DIA (GDIAACC) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[BSG]DIE (GDIE) !Block act:ANA
  DUDCLC M*15 Due date origin [menu 502: 1=Receipt date,2=Invoice date]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[BSG]EECICT (INCOTERM) !Block
  EECICT2 ICT Incoterm -> [ICTH]ICT0 =[BSG]EECICT2 (INCOTERM) !Block
  EECINCRAT RAT Intrastat increase act:DEB
  EECINCRAT2 RAT Intras. incr. act:DEB
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECLOC2 M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXPNUM L*8 Export number
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[BSG]FFWNUM (BPCARRIER) !Block
  FLG281 M*4 281.5 [menu 1: 1=No,2=Yes] act:BE281
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC] act:S1099
  FUPFLG M*4 Delivery reminders [menu 1: 1=No,2=Yes]
  INVDTA PFI Invoicing element -> [PFI]PFI0 =[BSG]INVDTA (PFOOTINV) !Block act:PFI
  INVDTAAMT DCB*11.4 % or amount act:PFI
  LAN LAN Language -> [TLA]TLA0 =[BSG]LAN (TABLAN) !Block
  LTIMRKCOE COE Lead time coefficient
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[BSG]MATTOL (MATCHTOL) !Block
  MDL MDL Delivery mode -> [TMD]TMD0 =[BSG]MDL (TABMODELIV) !Block
  NORPRNFLG M*4 Order form [menu 1: 1=No,2=Yes]
  NREPRNFLG M*4 Receipt note [menu 1: 1=No,2=Yes]
  NRTPRNFLG M*4 Return slip [menu 1: 1=No,2=Yes]
  OCNFLG M*4 Ack. reminder [menu 1: 1=No,2=Yes]
  ORDFREFRT MD1 Free freight threshold
  ORDMINAMT MD1 Minimum order
  OSTAUZAMT MD1 Authorized credit
  OSTCTL M*15 Credit control [menu 234: 1=Check,2=No check,3=Hold]
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[BSG]PAYBAN (BANK) !BSRA
  PLISTC PRS Price list structure -> [PRS]PRS0 =2;PLISTC (PRICSTRUCT) !Block
  PRIMRKCOE COE Price coefficient
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  PURPRITYP M*10 Amount type [menu 243: 1=Exclude tax,2=Include tax]
  QLYMRKCOE COE Quality coefficient
  QTYMRKCOE COE Quantity coefficient
  REFCOU ANM Customer sequence -> [ANM]ANM0 =[BSG]REFCOU (ACODNUM) !Block
  RITCOD RTZ(30) Withholding code -> [RTZ]RTZ0 =[BSG]RITCOD (RITENZIONE) !Block act:KIT
  RITNBR C*4 Number of codes act:KIT
  RITRAT DCB*9.2 Withholding tax allowance act:KIT
  RSKMRKCOE COE Free coefficient
  SEVLIN M*4 Multi-line order [menu 1: 1=No,2=Yes]
  SHOAXX AX1 Short description
  TPMCOD TPM Template code -> [TPM]TPM0 =TPMCOD (TABPRTMOD) !RTZ
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Block act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[BSG]UVYCOD (TABUNAVAIL) !Block
  UVYCOD2 UVY Unavailable -> [TUV]UVY0 =[BSG]UVYCOD2 (TABUNAVAIL) !Block
  UVYDAY1 M*4 Monday [menu 1: 1=No,2=Yes]
  UVYDAY2 M*4 Tuesday [menu 1: 1=No,2=Yes]
  UVYDAY3 M*4 Wednesday [menu 1: 1=No,2=Yes]
  UVYDAY4 M*4 Thursday [menu 1: 1=No,2=Yes]
  UVYDAY5 M*4 Friday [menu 1: 1=No,2=Yes]
  UVYDAY6 M*4 Saturday [menu 1: 1=No,2=Yes]
  UVYDAY7 M*4 Sunday [menu 1: 1=No,2=Yes]
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block

## BPSHISUPLN (BSL) - Ship-to addresses
Keys (first = PK; D = duplicates allowed): BSL0 BPSNUM+CPY+BPSSHI+BPSADD; BSL1 BPSSHI+BPSADD (D)
Fields:
  AUUID AUUID Single identifier
  BPSADD A*3 Ship-from address
  BPSNUM BPR Supplier -> [BPR]BPR0 =[BSL]BPSNUM (BPARTNER) !Delete
  BPSSHI BPR Ship-from supplier -> [BPR]BPR0 =[BSL]BPSSHI (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BSL]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BPSHISUPP (BSS) - Shipping site suppliers
Keys (first = PK; D = duplicates allowed): BSS0 BPSSHI+BPSADD
Fields:
  AUUID AUUID Single identifier
  BPSADD ADR Ship-from address
  BPSNAM NAM(2) Company name
  BPSSHI BPR Ship-from supplier -> [BPR]BPR0 =[BSS]BPSSHI (BPARTNER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYLTI C*3 Ship. deadline in dys
  EECICT ICT Incoterm -> [ICTH]ICT0 =[BSS]EECICT (INCOTERM) !Block
  EECINCRAT RAT Intrastat increase act:DEB
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM A*20 EU identification act:DEB
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[BSS]FFWNUM (BPCARRIER) !Block
  ICTCTY CTY Incoterm town
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[BSS]UVYCOD (TABUNAVAIL) !Block
  UVYDAY1 M*4 Monday [menu 1: 1=No,2=Yes]
  UVYDAY2 M*4 Tuesday [menu 1: 1=No,2=Yes]
  UVYDAY3 M*4 Wednesday [menu 1: 1=No,2=Yes]
  UVYDAY4 M*4 Thursday [menu 1: 1=No,2=Yes]
  UVYDAY5 M*4 Friday [menu 1: 1=No,2=Yes]
  UVYDAY6 M*4 Saturday [menu 1: 1=No,2=Yes]
  UVYDAY7 M*4 Sunday [menu 1: 1=No,2=Yes]

## BPSUPPLIER (BPS) - Suppliers
Notes: differs in V9.0 P12 (diff: AT3_BPSUPPLIER.htm); differs in V10 P1 (diff: ATD_BPSUPPLIER.htm)
Keys (first = PK; D = duplicates allowed): BPS0 BPSNUM; BPS1 BPSNAM (D); BPS2 BPSSHO (D)
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =3;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AGTPCP C*4 VAT collection agent act:KAG
  AGTSATTAX C*4 Regional taxes act:KAG
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount] act:PFI
  AUTINVCOD A*5 Auto invoice code act:KPO
  AUUID AUUID Single identifier
  BOX1099 A*4 1099 box act:S1099
  BPAADD ADR Default address
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPCNUM BPN Customer number act:KDE
  BPCNUMBPS A*15 Our customer no.
  BPRDSP DSP Payroll interface distribution -> [DSP]DSP0 =BPRDSP;1 (CADSP) !Block act:MURAN
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[BPS]BPRPAY (BPARTNER) !Block
  BPSGRU BPR Supplier group -> [BPR]BPR0 =[BPS]BPSGRU (BPARTNER) !Block
  BPSINV BPR Supplier invoice -> [BPR]BPR0 =[BPS]BPSINV (BPARTNER) !Block
  BPSNAM NAM Company name
  BPSNUM BPR Supplier -> [BPR]BPR0 =[BPS]BPSNUM (BPARTNER) !Delete
  BPSREM A*250 Notes
  BPSRSK BPR Risk BP -> [BPR]BPR0 =[BPS]BPSRSK (BPARTNER) !Block
  BPSSHO SHO Short description
  BPSTYP M*15 Supplier type [menu 501: 1=Normal,2=Prospect,3=Miscellaneous]
  BPTNUM BPT Carrier -> [BPT]BPT0 =[BPS]BPTNUM (BPCARRIER) !Block
  BSGCOD BSG Category -> [BSG]BSG0 =[BPS]BSGCOD (BPSCATEG) !Block
  CAI A*10 CAI number act:KAG
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CNTNAM NAM Default contact
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSHDAT D Cash VAT limit date act:KSP
  CSHVAT M*4 Cash VAT tax rule [menu 1: 1=No,2=Yes] act:KSP
  CUR CUR Currency -> [TCU]TCU0 =[BPS]CUR (TABCUR) !Block
  CURCLC M*15 Rate determination [menu 503: 1=Order date,2=Receipt date,3=Invoice date]
  DADFLG M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  DATVLYCAI D*1 CAI validity date act:KAG
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIA GDA Account structure -> [GDA]GDA0 =[BPS]DIA (GDIAACC) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[BPS]DIE (GDIE) !Block act:ANA
  DOUFLG M*15 Dispute [menu 516: 1=No,2=Warning,3=Hold]
  DUDCLC M*15 Due date origin [menu 502: 1=Receipt date,2=Invoice date]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[BPS]EECICT (INCOTERM) !Block
  EECINCRAT RAT Intrastat increase act:DEB
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FLG281 M*4 281.5 [menu 1: 1=No,2=Yes] act:BE281
  FLGSATTAX C*4 Collection agent act:KAG
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC] act:S1099
  FUPFLG M*4 Delivery reminder [menu 1: 1=No,2=Yes]
  GENMRK DCB*3.2 Total rank
  INVDTA PFI Invoicing element -> [PFI]PFI0 =[BPS]INVDTA (PFOOTINV) !Block act:PFI
  INVDTAAMT DCB*11.4 % or amount act:PFI
  IPTEXS ADI Expense allocation -> [ADI]CODE =312;IPTEXS (ATABDIV) !Block
  LOC EMP Location
  LTIMRK DCB*2.2 LT rank
  LTIMRKCOE COE Lead time coefficient
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[BPS]MATTOL (MATCHTOL) !Block
  MDL MDL Delivery mode -> [TMD]TMD0 =[BPS]MDL (TABMODELIV) !Block
  NORPRNFLG M*4 Order form [menu 1: 1=No,2=Yes]
  NREPRNFLG M*4 Receipt note [menu 1: 1=No,2=Yes]
  NRTPRNFLG M*4 Return slip [menu 1: 1=No,2=Yes]
  OCNFLG M*4 Ack. reminder [menu 1: 1=No,2=Yes]
  ORDFREFRT MD1 Free freight threshold
  ORDMINAMT MD1 Minimum order
  ORDTEX TXC Order acknowledgement
  OSTAUZAMT MD1 Authorized credit
  OSTCTL M*15 Credit control [menu 234: 1=Check,2=No check,3=Hold]
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[BPS]PAYBAN (BANK) !BSRA
  PAYLOKFLG M*4 Payment hold [menu 1: 1=No,2=Yes]
  PLISTC PRS Price list structure -> [PRS]PRS0 =2;PLISTC (PRICSTRUCT) !Block
  PRIMRK DCB*2.2 Price rank
  PRIMRKCOE COE Price coefficient
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[BPS]PRVNUM (HONPRV) !Block act:FEE2
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  PURPRITYP M*10 Amount type [menu 243: 1=Exclude tax,2=Include tax]
  QLYMRK DCB*2.2 Quality rank
  QLYMRKCOE COE Quality coefficient
  QTYMRK DCB*2.2 Quantity rank
  QTYMRKCOE COE Quantity coefficient
  RITCOD RTZ(30) Withholding code -> [RTZ]RTZ0 =[BPS]RITCOD (RITENZIONE) !Block act:KIT
  RITNBR C*4 Number of codes act:KIT
  RITPARCOE DCB*9.2(10) Partner held act:KIT
  RITPARNAM DES(10) Name of partner act:KIT
  RITPARNBR C*4 No. of partners act:KIT
  RITRAT DCB*9.2 Withholding tax allowance act:KIT
  RSKMRK DCB*2.2 Free rank
  RSKMRKCOE COE Free coefficient
  RTNTEX TXC Return order
  SATTAX A*10 Provinces act:KAG
  SEVLIN M*4 Multi-line order [menu 1: 1=No,2=Yes]
  TPMCOD TPM Template code -> [TPM]TPM0 =TPMCOD (TABPRTMOD) !RTZ
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Block act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[BPS]UVYCOD (TABUNAVAIL) !Block
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  WLFLG M*4 No WL verification [menu 1: 1=No,2=Yes] act:KPL

## BPSUPPMVT (MVS) - Supplier transactions
Keys (first = PK; D = duplicates allowed): MVS0 BPSRSK+CPY+BPSNUM+CUR; MVS1 BPSNUM+CPY (D)
Fields:
  ACCCUR CUR Accounting currency -> [TCU]TCU0 =[MVS]ACCCUR (TABCUR) !Block
  AUUID AUUID Single identifier
  BILAMTC MD1(3) Drafts
  BILAMTL MD1(3) Drafts
  BILAMTR MD1(3) Drafts
  BLCAMTC MD1 Accounting balance
  BLCAMTL MD1 Accounting balance
  BLCAMTR MD1 Accounting balance
  BPSNUM BPR Supplier -> [BPR]BPR0 =[MVS]BPSNUM (BPARTNER) !Delete
  BPSRSK BPR Risk BP -> [BPR]BPR0 =[MVS]BPSRSK (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[MVS]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Transaction currency -> [TCU]TCU0 =[MVS]CUR (TABCUR) !Block
  INVAMTC MD1 Unposted invoices
  INVAMTL MD1 Unposted invoices
  INVAMTR MD1 Unposted invoices
  ORDATIC MD1 On order
  ORDATIL MD1 On order
  ORDATIR MD1 On order
  ORDNOTC MD1 On order
  ORDNOTL MD1 On order
  ORDNOTR MD1 On order
  RCPATIC MD1 Delivered not invoiced
  RCPATIL MD1 Delivered not invoiced
  RCPATIR MD1 Delivered not invoiced
  RCPNOTC MD1 Delivered not invoiced
  RCPNOTL MD1 Delivered not invoiced
  RCPNOTR MD1 Delivered not invoiced
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CAAUZ (CAZ) - Restriction table
Keys (first = PK; D = duplicates allowed): CAZ0 TYP+AUZ1+AUZ2
Fields:
  AUUID AUUID Single identifier
  AUZ1 A*5 Restriction code
  AUZ2 A*5 Restriction code
  COBIVS M*4 Inverse combination [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  TYP M*15 Restriction type [menu 620: 1=Dimension/dimension restriction,2=Account/dimension restriction,3=Account/account restriction]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CACCE (CCE) - Dimensions
Keys (first = PK; D = duplicates allowed): CCE0 DIE+CCE
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[CCE]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  AUZ ADI Restriction code -> [ADI]CODE =322;AUZ (ATABDIV) !Block
  BUDTRK M*4 Budget tracking [menu 1: 1=No,2=Yes]
  CCE CCE Dimension -> [CCE]CCE0 =DIE;CCE (CACCE) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  DEFCCE CCE Default dimension -> [CCE]CCE0 =OTHDIE(indice);DEFCCE(indice) (CACCE) !Block act:ANA
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[CCE]DIE (GDIE) !Block
  DIENBR C*1 No. dim.
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCY CFY Company/site
  FRW M*4 Carryforward [menu 1: 1=No,2=Yes]
  IPT M*4 Chargeable [menu 1: 1=No,2=Yes]
  OTHDIE DIE Other dimension -> [DIE]DIE0 =[CCE]OTHDIE (GDIE) !Block act:ANA
  QTY QTY(20) Quantity
  SHOTRA AX1 Short description
  UOM UOM(20) Nonfinancial unit -> [TUN]TUN0 =[CCE]UOM (TABUNIT) !Block
  UOMNBR C*4 Number of units
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author
  VLYEND D Validity end date
  VLYSTR D Validity start date

## CACCEDEF (CDE) - Default dimensions
Notes: differs in V9.0 P12 (diff: AT3_CACCEDEF.htm); differs in V10 P1 (diff: ATD_CACCEDEF.htm)
Keys (first = PK; D = duplicates allowed): CDE0 COD+CPY
Fields:
  AUUID AUUID Single identifier
  CCE1 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE10 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE11 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE12 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE13 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE14 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE15 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE16 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE17 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE18 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE19 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE2 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE20 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE3 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE4 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE5 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE6 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE7 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE8 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  CCE9 M*15(5) Dimension [menu 693: 26 values, see local-menus.md]
  COD CDE Code -> [CDE]CDE0 =COD;CPY (CACCEDEF) !Other
  CPY CPY Company -> [CPY]CPY0 =[CDE]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CDE]CREUSR (AUTILIS) !Other
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE(20) Dimension codes -> [DIE]DIE0 =[CDE]DIE (GDIE) !Block
  FLD AFR*128(26) Identifiers
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBLIG C*2 Number of lines
  NBRDIE C*2 No. dim.
  SHOTRA AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CDE]UPDUSR (AUTILIS) !Other

## CADIEDEF (CDI) - Default dimension types
Keys (first = PK; D = duplicates allowed): CDI0 OBJ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CDI]CREUSR (AUTILIS) !Other
  DIE DIE Dimension codes -> [DIE]DIE0 =[CDI]DIE (GDIE) !Block act:ANA
  NBRDIE C*2 No. dim.
  OBJ M*20 Object [menu 2230: 17 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CDI]UPDUSR (AUTILIS) !Other

## CADSP (DSP) - Analytical allocations
Keys (first = PK; D = duplicates allowed): DSP0 DSP+NBRDSP
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[DSP]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Delete
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE(9);CCE10 (CACCE) !Delete
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE(10);CCE11 (CACCE) !Delete
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE(11);CCE12 (CACCE) !Delete
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE(12);CCE13 (CACCE) !Delete
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE(13);CCE14 (CACCE) !Delete
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE(14);CCE15 (CACCE) !Delete
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE(15);CCE16 (CACCE) !Delete
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE(16);CCE17 (CACCE) !Delete
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE(17);CCE18 (CACCE) !Delete
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE(18);CCE19 (CACCE) !Delete
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Delete
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE(19);CCE20 (CACCE) !Delete
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Delete
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Delete
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Delete
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Delete
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Delete
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Delete
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Delete
  COE DCB*9 Coefficients
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE(20) Dimension type -> [DIE]DIE0 =[DSP]DIE (GDIE) !Delete
  DSP DSP Key -> [DSP]DSP0 =DSP;NBRDSP (CADSP) !Other
  EXPNUM L*8 Export number
  FCY CFY Company/site
  NBRDIE C*1 No. dim.
  NBRDSP C*2 Number of lines
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VLYEND D Validity end date
  VLYSTR D Validity start date

## CAECOD (CAEC) - CAE code
Notes: activity code FPOPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## CARAREA (CAA) - Carrier regions
Keys (first = PK; D = duplicates allowed): CAA0 BPTNUM+LINNUM; CAA1 BPTNUM+STOFCY+CRY+POSCOD (D)
Fields:
  AUUID AUUID Single identifier
  BPTARE A*5 Region
  BPTNUM BPT Carrier -> [BPT]BPT0 =[CAA]BPTNUM (BPCARRIER) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[CAA]CRY (TABCOUNTRY) !Block
  EXPNUM L*8 Export number
  LINNUM L*8 Line number
  POSCOD POS Postal code
  STOFCY FCY Shipment site -> [FCY]FCY0 =[CAA]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CARPRICE (CAP) - Carrier price lists
Keys (first = PK; D = duplicates allowed): CAP0 BPTNUM+BPTARE+RANG; CAP1 BPTNUM+RANG+BPTARE; CAP2 BPTNUM+BPTARE+MAXQTY
Fields:
  ADL MD2 Proport amount
  AUUID AUUID Single identifier
  BKT WEI Bracket value
  BPTARE A*5 Region
  BPTNUM BPT Carrier -> [BPT]BPT0 =[CAP]BPTNUM (BPCARRIER) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  MAXQTY WEI Maximum quantity included
  MINQTY WEI Min qty excluded
  PRI MD2 List price
  RANG C*3 Sequence
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEIRND M*4 Round the weight [menu 238: 1=Band <,2=Band >,3=Nearest band]

## CBLOB (CBB) - Special folders
Keys (first = PK; D = duplicates allowed): CBB0 CODBLB+IDENT1+IDENT2
Fields:
  AUUID AUUID Single identifier
  BLOB ABB Image file
  CODBLB A*10 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM HM Time
  CREUSR A*5 Creation user
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  NAMBLB DES File name
  TYPBLB AT Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM HM Time
  UPDUSR A*5 Change user

## CCMACTION (CCMACT) - Actions
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMACTION.htm)
Keys (first = PK; D = duplicates allowed): CCMACT_0 ACTIONID
Fields:
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMACT]CREUSR (AUTILIS) !Other
  TRANACTION M*15 Action [menu 2032: 24 values, see local-menus.md]
  TRANTYPE M*15 Entity [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMACT]UPDUSR (AUTILIS) !Other

## CCMAPPROVER (CCMAPPR) - Change request approvers
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMAPPROVER.htm)
Keys (first = PK; D = duplicates allowed): CCMAPPR0 CRID+APPRLN; CCMAPPR1 CRID+APPRUSER (D); CCMAPPR2 CRID+SORTSEQ (D)
Fields:
  APPRLN C*4 Line no.
  APPRREASON A*50 Reason
  APPRSTAT M*20 Approval status [menu 2041: 1=Pending,2=Approved,3=Rejected]
  APPRUSER CCMAUSAP User code -> [AUS]CODUSR =[CCMAPPR]APPRUSER (AUTILIS) !Block
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMAPPR]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  NCSAPPUSR NCSAUSAP User -> [AUS]CODUSR =[CCMAPPR]NCSAPPUSR (AUTILIS) !Block
  SORTSEQ C*4 Sort sequence
  TRANSTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMAPPR]UPDUSR (AUTILIS) !Other

## CCMCHGREQ (CCMCR) - Change request
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCHGREQ.htm)
Keys (first = PK; D = duplicates allowed): CCMCR0 CRID
Fields:
  AUUID AUUID Single identifier
  CCMUSRID CCMAUSCM Change manager -> [AUS]CODUSR =[CCMCR]CCMUSRID (AUTILIS) !Block
  CHGMANDAT D Reassigned on
  CHGMANUSR CCMAUS Reassigned by -> [AUS]CODUSR =[CCMCR]CHGMANUSR (AUTILIS) !Block
  CLOSEDATE D Closed on
  CLOSEDST M*15 Closed state [menu 2042: 1=-Select-,2=Rejected,3=Completed]
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMCR]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  CRSTATUS M*20 Status [menu 2033: 1=New,2=In review,3=Rejected,4=In planning,5=Being implemented,6=Completed,7=Closed]
  DATEREQ D Required date
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  IMPACT M*20 Change impact [menu 2031: 1=- Select -,2=Major,3=Minor,4=Unknown]
  IMPACTANAL C*4 Impact analysis
  NCSCATEGORY M*15 Category [menu 3715: 1=- Select -,2=Customer,3=Supplier,4=Internal,5=External]
  NCSCCMID CCMCRID Request ID
  NCSMANAGER NCSAUSQA QA manager -> [AUS]CODUSR =[CCMCR]NCSMANAGER (AUTILIS) !Block
  NCSPLANNER NCSAUSPL Planner -> [AUS]CODUSR =[CCMCR]NCSPLANNER (AUTILIS) !Block
  NCSPROCAU M*15 Probable cause [menu 3717: 1=- Select -,2=Supplier issue,3=Transport issue,4=Production issue,5=Inventory issue,6=Sales issue,7=Design issue,8=Other]
  NCSREASON M*35 Reason [menu 3703: 1=- Select -,2=Nonfulfillment of requirement,3=Potential Nonconformity,4=Customer feedback,5=Observation during internal audit]
  NCSREC M*4 Non-conformance [menu 1: 1=No,2=Yes]
  NCSROOCAU M*15 Root cause [menu 3716: 19 values, see local-menus.md]
  PLANNER CCMAUSPL Planner -> [AUS]CODUSR =[CCMCR]PLANNER (AUTILIS) !Block
  PRODDESC A*50 Description
  PRODUCT ITM Product -> [ITM]ITM0 =[CCMCR]PRODUCT (ITMMASTER) !Block
  REASON M*20 Reason for change [menu 2034: 1=- Select -,2=New requirement,3=Enhancement,4=Defect,5=Other]
  REJECTCOD M*50 Reason for rejection [menu 2035: 1=- Select -,2=Not enough evidence,3=Not cost-effective,4=Change is out of scope / budget,5=Request conflicts with other scheduled change,6=Implementation date is in a freeze period,7=Other,8=Not selected]
  REJECTDAT D Rejected on
  REJECTUSR CCMAUS Rejected by -> [AUS]CODUSR =[CCMCR]REJECTUSR (AUTILIS) !Block
  SEVERITY M*20 Severity [menu 2030: 1=- Select -,2=Critical,3=Major,4=Moderate,5=Minor (Cosmetic)]
  SITE FCY Site -> [FCY]FCY0 =[CCMCR]SITE (FACILITY) !Block
  TITLE DES Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCR]UPDUSR (AUTILIS) !Other

## CCMCRDESC (CCMCRD) - Change request description
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRDESC.htm)
Keys (first = PK; D = duplicates allowed): CCMCR0 CRID
Fields:
  AUUID AUUID Single identifier
  CRDESC ACRTF*1 Additional information
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMCRD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCRD]UPDUSR (AUTILIS) !Other

## CCMCRNOTES (CCMCRN) - Change request attachments
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRNOTES.htm)
Keys (first = PK; D = duplicates allowed): CCMCRN0 CRID+FILENAM+NOTELINE
Fields:
  AUUID AUUID Single identifier
  CATEGORY M*15 Category [menu 2043: 1=- Select -,2=Request detail,3=Approval,4=Recommendation,5=Planning,6=Implementation,7=Rejection,8=Other]
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMCRN]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  CRNOTES AB0*1 Notes
  DES A*50 Description
  DOCTYPE ATYP Document type -> [ATYP]ATYP0 =[CCMCRN]DOCTYPE (ATYPEPRO) !Block
  FILENAM A*30 File name
  NOTELINE C*4 Line number
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMCRN]UPDUSR (AUTILIS) !Other

## CCMCRORIGC (CCMCROC) - Customer originators
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRORIGC.htm)
Keys (first = PK; D = duplicates allowed): CCMCROC0 CRID+ORIGCLN; CCMCROC1 CRID+BPCNUM; CCMCROC2 CRID+SORTSEQ (D)
Fields:
  AUUID AUUID Single identifier
  BPCNUM BPC Customer -> [BPC]BPC0 =[CCMCROC]BPCNUM (BPCUSTOMER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMCROC]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  CUSTCONTACT AIN Contact -> [AIN]AIN0 =[CCMCROC]CUSTCONTACT (CONTACTCRM) !BSRA
  ORIGCLN C*4 Line number
  SORTSEQ C*4 Sort sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCROC]UPDUSR (AUTILIS) !Other

## CCMCRORIGE (CCMCROE) - External originators
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRORIGE.htm)
Keys (first = PK; D = duplicates allowed): CCMCROE0 CRID+ORIGELN; CCMCROE1 CRID+EXTCONTACT; CCMCROE2 CRID+SORTSEQ (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMCROE]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  EXTCONTACT AIN Contact -> [AIN]AIN0 =[CCMCROE]EXTCONTACT (CONTACTCRM) !Block
  ORIGELN C*4 Line number
  SORTSEQ C*4 Sort sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCROE]UPDUSR (AUTILIS) !Other

## CCMCRORIGI (CCMCROI) - Internal originators
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRORIGI.htm)
Keys (first = PK; D = duplicates allowed): CCMCROI0 CRID+ORIGILN; CCMCROI1 CRID+USER; CCMCROI2 CRID+SORTSEQ (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMCROI]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ORIGILN C*4 Line number
  SORTSEQ C*4 Sort sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCROI]UPDUSR (AUTILIS) !Other
  USER CCMAUS User code -> [AUS]CODUSR =[CCMCROI]USER (AUTILIS) !Block

## CCMCRORIGS (CCMCROS) - Supplier originators
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMCRORIGS.htm)
Keys (first = PK; D = duplicates allowed): CCMCROS0 CRID+ORIGSLN; CCMCROS1 CRID+BPSNUM; CCMCROS2 CRID+SORTSEQ (D)
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPS Supplier -> [BPS]BPS0 =[CCMCROS]BPSNUM (BPSUPPLIER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMCROS]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ORIGSLN C*4 Line number
  SORTSEQ C*4 Sort sequence
  SUPPCONTACT AIN Contact -> [AIN]AIN0 =[CCMCROS]SUPPCONTACT (CONTACTCRM) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMCROS]UPDUSR (AUTILIS) !Other

## CCMIMPBOD (CCMIBOD) - Impact analysis-BOM lines
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPBOD.htm)
Keys (first = PK; D = duplicates allowed): CCMBOD0 CRID+LINENO; CCMBOD1 CRID+SORTSEQ
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMIBOD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BLOCK M*4 Block [menu 1: 1=No,2=Yes]
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Delete
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMSEQ C*4 Sequence
  BOMSHO DES Link description
  BOMUOM UOM UOM -> [TUN]TUN0 =[CCMIBOD]BOMUOM (TABUNIT) !Block
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Creation user -> [AUS]CODUSR =[CCMIBOD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  ITMREF ITM Parent product -> [ITM]ITM0 =[CCMIBOD]ITMREF (ITMMASTER) !Block
  LIKQTY QTY Link quantity
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  NIV C*2 Level
  QTYRND A*10 Quantity rounding
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIBOD]UPDUSR (AUTILIS) !Other

## CCMIMPBOH (CCMIBOH) - Impact analysis-BOMs
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPBOH.htm)
Keys (first = PK; D = duplicates allowed): CCMBOH0 CRID
Fields:
  AUUID AUUID Single identifier
  BOHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIBOH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  NUMBOM L*8 Number of BOMs
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIBOH]UPDUSR (AUTILIS) !Other

## CCMIMPFOD (CCMIFOD) - Impact analysis-Forecasts
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPFOD.htm)
Keys (first = PK; D = duplicates allowed): CCMIFOD0 CRID+LINENO; CCMIFOD1 CRID+SORTSEQ
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMIFOD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  COMMENT A*240 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIFOD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  ITMREF ITM Product -> [ITM]ITM0 =[CCMIFOD]ITMREF (ITMMASTER) !Block
  LINENO C*4 Line no.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  MONTHEND D End of month
  MONTHNAME A*10 Month (january, february, ...)
  MONTHSTART D Beginning of month
  ORDSTATUS A*10 Order status
  SITE FCY Site -> [FCY]FCY0 =[CCMIFOD]SITE (FACILITY) !Block
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TOTQTY QTY Monthly total
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIFOD]UPDUSR (AUTILIS) !Other
  WEEQTY1 QTY Qty week 1
  WEEQTY2 QTY Qty week 2
  WEEQTY3 QTY Qty week 3
  WEEQTY4 QTY Qty week 4
  WEEQTY5 QTY Qty week 5
  YEA A*4 Year

## CCMIMPFOH (CCMIFOH) - Impact analysis-Forecasts
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPFOH.htm)
Keys (first = PK; D = duplicates allowed): CCMIFOH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIFOH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOHMONTHS L*8 Number of months
  FOHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  FOHQTY QTY Total quantity
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIFOH]UPDUSR (AUTILIS) !Other

## CCMIMPITM (CCMIITM) - Impact analysis-Stock
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPITM.htm)
Keys (first = PK; D = duplicates allowed): CCMITM0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIITM]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  ITMFCY L*8 Number of sites
  ITMPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  ORDSTO QTY On reorder
  PHYALL QTY Total allocated
  PHYSTO QTY Available stock
  SALSTO QTY On sales orders
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIITM]UPDUSR (AUTILIS) !Other

## CCMIMPITMDET (CCMITMD) - Impact analysis-Stock sites
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPITMDET.htm)
Keys (first = PK; D = duplicates allowed): CCMITD0 CRID+LINENO; CCMITD1 CRID+SORTSEQ
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMITMD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BLOCK M*4 Block [menu 1: 1=No,2=Yes]
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Creation user -> [AUS]CODUSR =[CCMITMD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  FCYORDSTO QTY On reorder
  FCYPHYALL QTY Total allocated
  FCYPHYSTO QTY Available stock
  FCYSALSTO QTY On sales orders
  ITMREF ITM Product -> [ITM]ITM0 =[CCMITMD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  STOFCY FCY Storage site -> [FCY]FCY0 =[CCMITMD]STOFCY (FACILITY) !Delete
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMITMD]UPDUSR (AUTILIS) !Other

## CCMIMPMFGD (CCMMFGD) - Impact analysis-Work orders
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPMFGD.htm)
Keys (first = PK; D = duplicates allowed): CCMMFGD0 CRID+LINENO; CCMMFGD1 CRID+SORTSEQ (D)
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMMFGD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BLOCK M*4 Block [menu 1: 1=No,2=Yes]
  BOMALT TBO BOM code -> [TBO]TBO0 =2;BOMALT (TABBOMALT) !Block
  BPCNUM BPR Ship-to customer -> [BPR]BPR0 =BPCNUM (BPARTNER) !Block
  BPCTYPDEN M*15 Ship-to type [menu 722: 1=Site,2=Customer,3=Supplier]
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMMFGD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  EXTQTY QTY Planned quantity
  ITMREF ITM Product -> [ITM]ITM0 =[CCMMFGD]ITMREF (ITMMASTER) !Block
  ITMSTA M*15 Line status [menu 363: 1=Pending,2=In process,3=Completed,4=Cancelled]
  LINENO C*4 Line no.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  MFGFCY FCY Production site -> [FCY]FCY0 =[CCMMFGD]MFGFCY (FACILITY) !Block
  MFGLIN L*8 Line no.
  MFGNUM MFG Order no. -> [MFG]MFG0 =MFGNUM (MFGHEAD) !Other
  MFGSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  PLNFCY FCY Planning site -> [FCY]FCY0 =[CCMMFGD]PLNFCY (FACILITY) !Block
  SHIPTOSITE FCY Ship-to site -> [FCY]FCY0 =[CCMMFGD]SHIPTOSITE (FACILITY) !Block
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UOMEXTQTY QTY Rel quantity
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMMFGD]UPDUSR (AUTILIS) !Other

## CCMIMPMFGH (CCMMFGH) - Impact analysis-Work orders
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPMFGH.htm)
Keys (first = PK; D = duplicates allowed): CCMMFGH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMMFGH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMMFGH]UPDUSR (AUTILIS) !Other
  WOHORDERS L*8 Number of orders
  WOHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  WOHQTY QTY Total quantity

## CCMIMPPOD (CCMIPOD) - Impact analysis-Purchases
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPPOD.htm)
Keys (first = PK; D = duplicates allowed): CCMPOD0 CRID+LINENO; CCMPOD1 CRID+SORTSEQ; CCMPOD2 CRID+BPSNUM+POHNUM (D)
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMIPOD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BPSNUM BPR Supplier -> [BPR]BPR0 =[CCMIPOD]BPSNUM (BPARTNER) !Other
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CONAMNT MD8 Base calculation
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMIPOD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  FOLDCUR CUR Currency -> [TCU]TCU0 =[CCMIPOD]FOLDCUR (TABCUR) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[CCMIPOD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  LINSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  NETPRIATI MD8 Amount + tax
  NETPRINOT MD8 Amount - tax
  POHCUR CUR Currency -> [TCU]TCU0 =[CCMIPOD]POHCUR (TABCUR) !Block
  POHNUM POH Order number -> [POH]POH0 =[CCMIPOD]POHNUM (PORDER) !Other
  POPLIN L*8 Line no.
  POQSEQ L*8 Sequence number
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[CCMIPOD]PRHFCY (FACILITY) !Block
  QTY QTY Ordered qty.
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMIPOD]UPDUSR (AUTILIS) !Other
  WIPSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]

## CCMIMPPOH (CCMIPOH) - Impact analysis-Purchases
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPPOH.htm)
Keys (first = PK; D = duplicates allowed): CCMPOH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMIPOH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMIPOH]FOLDCUR (TABCUR) !Block
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  POHAMT MD8 Total amount +tax
  POHAMTEX MD8 Total amount -tax
  POHORDERS L*8 Number of orders
  POHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  POHQTY QTY Total quantity
  POHSUP L*8 Number of suppliers
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMIPOH]UPDUSR (AUTILIS) !Other

## CCMIMPPRD (CCMIPRD) - Impact analysis-Purchase req
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPPRD.htm)
Keys (first = PK; D = duplicates allowed): CCMPRD0 CRID+LINENO; CCMPRD2 CRID+SORTSEQ
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMIPRD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BPSNUM BPR Supplier -> [BPR]BPR0 =[CCMIPRD]BPSNUM (BPARTNER) !Block
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CONAMNT MD8 Base calculation
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIPRD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  FOLDCUR CUR Currency -> [TCU]TCU0 =[CCMIPRD]FOLDCUR (TABCUR) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[CCMIPRD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINEPRICE MD8 Amount + tax
  LINEPRIEX MD8 Amount - tax
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  PRHCUR CUR Currency -> [TCU]TCU0 =[CCMIPRD]PRHCUR (TABCUR) !Block
  PSDLIN L*8 Line
  PSHFCY FCY Request site -> [FCY]FCY0 =[CCMIPRD]PSHFCY (FACILITY) !Block
  PSHNUM PSH Request no. -> [PSH]PSH0 =[CCMIPRD]PSHNUM (PREQUIS) !Block
  PSHSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  QTYPUU QTY Purchase quantity
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIPRD]UPDUSR (AUTILIS) !Other

## CCMIMPROD (CCMROD) - Impact analysis-Routing lines
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPROD.htm)
Keys (first = PK; D = duplicates allowed): CCMROD0 CRID+LINENO; CCMROD1 CRID+SORTSEQ
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMROD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BLOCK M*4 Block [menu 1: 1=No,2=Yes]
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Creation user -> [AUS]CODUSR =[CCMROD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ ICVVAL Major version act:ECC
  ECCVALMIN ICVVAL Minor version act:ECC
  ENDDATE D End date
  FCY FCY Site -> [FCY]FCY0 =[CCMROD]FCY (FACILITY) !Delete
  IDENT1 ID1 Identifier 1
  ITMREF ITM Routing -> [ITM]ITM0 =[CCMROD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  ROUALT TRO Routing code -> [TRO]TRO0 =[CCMROD]ROUALT (TABROUALT) !Block
  ROUDESAXX AX3 Header title
  ROUENDDAT D Valid to
  ROUSTRDAT D Valid from
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMROD]UPDUSR (AUTILIS) !Other

## CCMIMPROH (CCMROH) - Impact analysis-Routing
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPROH.htm)
Keys (first = PK; D = duplicates allowed): CCMROH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMROH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  NUMROU L*8 Number of lines
  ROHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMROH]UPDUSR (AUTILIS) !Other

## CCMIMPSCD (CCMSCD) - Impact analysis-Subcontract
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSCD.htm)
Keys (first = PK; D = duplicates allowed): CCMSCD CRID+LINENO
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMSCD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BPRNUM BPR Supplier -> [BPR]BPR0 =[CCMSCD]BPRNUM (BPARTNER) !RTZ
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMSCD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  ITMREF ITM Product -> [ITM]ITM0 =[CCMSCD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  POHFCY FCY Order site -> [FCY]FCY0 =[CCMSCD]POHFCY (FACILITY) !Block
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[CCMSCD]PRHFCY (FACILITY) !Block
  QTYPUU QTY Purchase quantity
  RETDAT D Receipt date
  SCHNUM SCO Subcontract order -> [SCO]SCO0 =[CCMSCD]SCHNUM (SCOHEAD) !Block
  SCOSTA M*10 Status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  STARTDATE D Start date
  TOTVAL MD8 Total value
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMSCD]UPDUSR (AUTILIS) !Other

## CCMIMPSCH (CCMSCH) - Impact analysis-Subcontract
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSCH.htm)
Keys (first = PK; D = duplicates allowed): CCMSCH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMSCH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMSCH]FOLDCUR (TABCUR) !Block
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  SCHAMT MD8 Total value
  SCHORDERS L*8 Number of orders
  SCHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  SCHQTY QTY Total quantity
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMSCH]UPDUSR (AUTILIS) !Other

## CCMIMPSOD (CCMSOD) - Impact analysis-Sales orders
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSOD.htm)
Keys (first = PK; D = duplicates allowed): CCMSOD0 CRID+LINENO; CCMSOD1 CRID+SORTSEQ; CCMSOD2 CRID+BPCORD+SOHNUM (D)
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMSOD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BLOCK M*4 Block [menu 1: 1=No,2=Yes]
  BPCORD BPC Sold-to -> [BPC]BPC0 =[CCMSOD]BPCORD (BPCUSTOMER) !Other
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CONAMNT MD8 Base calculation
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMSOD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  DEMSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  DLVQTY QTY Delivered qty.
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMSOD]FOLDCUR (TABCUR) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[CCMSOD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  NETPRIATI MD8 Amount + tax
  NETPRINOT MD8 Amount - tax
  ODLQTYSTU QTY STK qty. in process
  OPRQTYSTU QTY Qty being prep STU
  PREQTYSTU QTY Qty prepared STU
  QTY QTY Ordered qty.
  SALFCY FCY Sales site -> [FCY]FCY0 =[CCMSOD]SALFCY (FACILITY) !Block
  SOHCUR CUR Currency -> [TCU]TCU0 =[CCMSOD]SOHCUR (TABCUR) !Block
  SOHNUM SOH Order number -> [SOH]SOH0 =[CCMSOD]SOHNUM (SORDER) !Other
  SOPLIN L*8 Line no.
  SOQSEQ L*8 Sequence number
  SOQSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  SORTSEQ C*4 Sort sequence
  STAGE M*15 Stage [menu 2050: 1=Order,2=Preparation,3=Delivery]
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMSOD]UPDUSR (AUTILIS) !Other

## CCMIMPSOH (CCMSOH) - Impact analysis-Sales orders
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSOH.htm)
Keys (first = PK; D = duplicates allowed): CCMSOH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMSOH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMSOH]FOLDCUR (TABCUR) !Block
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  SOHAMT MD8 Total amount +tax
  SOHAMTEX MD8 Total amount -tax
  SOHCUST L*8 Number of customers
  SOHORDERS L*8 Number of orders
  SOHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  SOHQTY QTY Total quantity
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMSOH]UPDUSR (AUTILIS) !Other

## CCMIMPSQD (CCMISQD) - Impact analysis-Sales quotes
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSQD.htm)
Keys (first = PK; D = duplicates allowed): CCMSQD0 CRID+LINENO; CCMSQD1 CRID+SORTSEQ; CCMSQD2 CRID+BPCORD+SQHNUM (D)
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMISQD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  BPCORD BPC Sold-to -> [BPC]BPC0 =[CCMISQD]BPCORD (BPCUSTOMER) !Other
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CONAMNT MD8 Base calculation
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMISQD]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  ECCVALMAJ CCMECS Major version act:ECC
  ECCVALMIN CCMEVL Minor version act:ECC
  ENDDATE D End date
  FOLDCUR CUR Currency -> [TCU]TCU0 =[CCMISQD]FOLDCUR (TABCUR) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[CCMISQD]ITMREF (ITMMASTER) !Block
  LINENO C*4 No.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  NETPRIATI MD8 Amount + tax
  NETPRINOT MD8 Amount - tax
  QTY QTY Quote quantity
  SALFCY FCY Sales site -> [FCY]FCY0 =[CCMISQD]SALFCY (FACILITY) !Block
  SORTSEQ C*4 Sort sequence
  SQDLIN L*8 Quote line
  SQHCUR CUR Currency -> [TCU]TCU0 =[CCMISQD]SQHCUR (TABCUR) !Block
  SQHNUM VCR Quote no.
  STARTDATE D Start date
  TRANTYPE M*15 Transaction type [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMISQD]UPDUSR (AUTILIS) !Other
  VLYDAT D Validity date

## CCMIMPSQH (CCMISQH) - Impact analysis-Sales quotes
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPSQH.htm)
Keys (first = PK; D = duplicates allowed): CCMSQH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMISQH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMISQH]FOLDCUR (TABCUR) !Block
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  SQHAMT MD8 Total amount +tax
  SQHAMTEX MD8 Total amount -tax
  SQHCUST L*8 Number of customers
  SQHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  SQHQTY QTY Total quantity
  SQHQUOTES L*8 Number of quotes
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMISQH]UPDUSR (AUTILIS) !Other

## CCMPLAND (CCMPD) - Change request plan detail
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMPLAND.htm)
Keys (first = PK; D = duplicates allowed): CCMPD_0 CRID+LINENO; CCMPD_1 CRID+SORTSEQ (D)
Fields:
  ACTIONER CCMAUS Actioner -> [AUS]CODUSR =[CCMPD]ACTIONER (AUTILIS) !Block
  ACTIONID CCMACT Action ID
  AUUID AUUID Single identifier
  COMMENT A*50 Comment
  COMPLETEDATE D Complete by
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMPD]CREUSR (AUTILIS) !Other
  CRID CCMPLAN Request ID
  ENDDATE D End date
  LINENO C*4 Line no.
  LINESTATUS M*15 Status [menu 2040: 1=Pending,2=In progress,3=Completed]
  SORTSEQ C*4 Sort sequence
  STARTDATE D Start date
  TRANTYPE M*15 Entity [menu 2039: 1=-Select-,2=ALL,3=BOMs,4=Customer,5=Demand forecasts,6=Purchase requests,7=Purchase orders,8=Sales quote,9=Routing,10=Sales order,11=Stock,12=Subcontract orders,13=Supplier,14=Work order,15=Other]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMPD]UPDUSR (AUTILIS) !Other

## CCMPLANH (CCMPH) - Change request plan header
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMPLANH.htm)
Keys (first = PK; D = duplicates allowed): CCMPH_0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMPH]CREUSR (AUTILIS) !Other
  CRID CCMPLAN Request ID
  HIGHLEVEL M*15 Status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  PLANSTATUS M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCMPH]UPDUSR (AUTILIS) !Other

## CCMREJDSC (CCMREJ) - Rejection description
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMREJDSC.htm)
Keys (first = PK; D = duplicates allowed): CCMCR0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCMREJ]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  REJDESC ACRTF*1 Additional information
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[CCMREJ]UPDUSR (AUTILIS) !Other

## CERTIFCCS (CCS) - Entertainment fund certificate
Notes: activity code FINTM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## CFGDEF (CDF) - Config. default values
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CDF0 RECCOD+CODFIC+CODFLD+SCENUM; CDF1 RECCOD+CODFIC+SCENUM+CODFLD
Fields:
  AUUID AUUID Single identifier
  CODFIC M Table code [menu 752: 30 values, see local-menus.md]
  CODFLD AVA Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFTYP C*4 Value type
  DEFVAL A*80 Default value
  EXPNUM L*8 Export number
  RECCOD C*4 Code
  SCENUM CFG Scenario -> [CSC]CSC0 =[CDF]SCENUM (CFGSCE) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CDF]UPDUSR (AUTILIS) !Other

## CHEFWRK (CEW) - Signature management
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## CLACTR (HRCLC) - Document clause
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## CLASSCONV (HRCCV) - Collective agreement classification
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## COMPETENCE (CPC) - Skills
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## COMPETENCED (CPD) - Skills
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## COMREP (COM) - Sales rep commissions
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): COM0 REP+CPY+YEA+MON
Fields:
  AMTCOM MD1 Amount
  AMTINV MD1 Invoiced with taxes
  AMTINVREP MD1 Invoiced by the agent
  AMTPAY MD1 Payments
  AMTPAYREP MD1 Payments to the agent
  AUUID AUUID Single identifier
  BASCOM MD1 Basis
  CPY CPY Company -> [CPY]CPY0 =[COM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[COM]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[COM]CUR (TABCUR) !Block
  DAT D Date
  ENASARCO MD1 Enasarco
  FIRR MD1 Firr
  INPS MD1 Inps
  MON C*2 Months
  REP REP Sales rep -> [REP]REP0 =[COM]REP (SALESREP) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[COM]UPDUSR (AUTILIS) !Other
  YEA C*4 Year

## CONTACTSA (CNTSA) - Additional RSA fields
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## CONTAMT (CAM) - Annual databases
Keys (first = PK; D = duplicates allowed): CAM1 CONNUM+AMTRECNUMX
Fields:
  AMT MD1 Amount
  AMTEND D End date
  AMTRECNUMX L*8 Number
  AMTSTR D Start date
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[CAM]CONNUM (CONTSERV) !RTZ
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CAM]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice no.
  PRONUMINV L*8 Process number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CAM]UPDUSR (AUTILIS) !Other

## CONTAMTX (CAX) - Annual databases
Keys (first = PK; D = duplicates allowed): CAX0 CONNUM+AMTRECNUMX+PRONUM
Fields:
  AMT MD1 Amount
  AMTEND D End date
  AMTRECNUMX L*8 Number
  AMTSTR D Start date
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[CAX]CONNUM (CONTSERV) !RTZ
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CAX]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice no.
  PRONUM L*8 Process number
  PRONUMINV L*8 Process number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CAX]UPDUSR (AUTILIS) !Other

## CONTCARE (CCA) - Maintenance plan
Keys (first = PK; D = duplicates allowed): CCA0 CONNUM+TPL+CCANUM
Fields:
  APE ADI Entry points -> [ADI]CODE =430;APE (ATABDIV) !Block
  AUUID AUUID Single identifier
  CCANUM VCR Plan chrono
  CND CLX Condition
  CNDFLT CLX Condition filter
  CNDTAB A*10 Condition table
  CONNUM VCR Contract/templ. code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FRY L*8 Recurrence
  FRYBAS M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  FRYTYP M*15 Periodicity type [menu 2990: 1=Recurrance,2=Value check,3=Entry point]
  INVTYP M*15 Supp invoicing [menu 2991: 1=According to contract due dates,2=On closing of the service request]
  LASSREDAT D Last meeting
  SET A*15 Required model
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CONTCOV (CCV) - Service contracts coverage
Keys (first = PK; D = duplicates allowed): CCV0 CONNUM+TPL+RECTYP+SBBRECTYP+RECNUM (D); CCV1 BPC+RECTYP+SBBRECTYP (D); CCV2 TPL+RECTYP+SBBRECTYP+CMT (D)
Fields:
  AUUID AUUID Single identifier
  BPC BPR Customer -> [BPR]BPR0 =[CCV]BPC (BPARTNER) !Delete
  CMT DES Comments
  CONNUM CON Contract code -> [CON]CON0 =[CCV]CONNUM (CONTSERV) !Delete
  CPNICDFLG M*15 Included components [menu 2999: 1=Exclude non-listed components,2=Include non-listed components]
  CPNSRT A*15 Sort for components
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCV]CREUSR (AUTILIS) !Other
  EXSICDFLG M*15 Included charges [menu 3002: 1=Exclude the expenses not listed,2=Include the expenses not listed]
  HEIPRC C*3(5) Up to (%)
  ICDFLG M*15 Included/excluded [menu 2981: 1=Exclude,2=Include]
  ITMICDFLG M*15 Item inclusion [menu 3000: 1=Exclude non-listed products,2=Include non-listed products]
  LABICDFLG M*15 Include labor [menu 3001: 1=Exclude non-listed labor,2=Include non-listed labor]
  LNDAUZ M*4 Authorized loan [menu 1: 1=No,2=Yes]
  MAXCOV MD1(5) Max threshold
  MINCOV MD1(5) Min threshold
  PAEKEY A*30(5) Parent key
  PAEKEYTYP A*3(5) Parent key type
  RECNUM A*30 Covered element
  RECTYP A*3 Record type
  SBBRECTYP A*3 Sub-type
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCV]UPDUSR (AUTILIS) !Other

## CONTIDX (CIX) - Index values
Keys (first = PK; D = duplicates allowed): CIX0 IND (D); CIX1 IND+INDDAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CIX]CREUSR (AUTILIS) !Other
  IND ADI Index -> [ADI]CODE =410;IND (ATABDIV) !Block
  INDDAT D Date
  INDVAL DCB*9.2 Value
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CIX]UPDUSR (AUTILIS) !Other

## CONTITM (CIT) - Covered product
Keys (first = PK; D = duplicates allowed): CIT0 CONNUM+TPL+CONMACNUM; CIT1 CONMACCOD (D)
Fields:
  AUUID AUUID Single identifier
  CONMACCOD A*20 Group/product/base
  CONMACNUM A*15 Base number
  CONNUM CON Contract code -> [CON]CON0 =[CIT]CONNUM (CONTSERV) !Delete
  COVTYP M*15 Coverage type [menu 983: 1=According to base,2=According to product reference,3=According to commercial group]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CIT]CREUSR (AUTILIS) !Other
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CIT]UPDUSR (AUTILIS) !Other

## CONTPBL (CPL) - Skills covered
Keys (first = PK; D = duplicates allowed): CPL0 CONNUM+TPL+PBLGRPCOV
Fields:
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[CPL]CONNUM (CONTSERV) !RTZ
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CPL]CREUSR (AUTILIS) !Other
  PBLGRPCOV PBL Skill groups -> [PBL]PBL0 =[CPL]PBLGRPCOV (FAMPB) !RTZ
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CPL]UPDUSR (AUTILIS) !Other

## CONTQUAL (CQL) - Quality constraints
Keys (first = PK; D = duplicates allowed): CQL0 CONNUM+TPL+GRALEV
Fields:
  AMTPLY MD1 Penalty amount
  AUUID AUUID Single identifier
  BASEXXAMT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOL M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  CONNUM VCR Contract/templ. code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CQL]CREUSR (AUTILIS) !Other
  GRALEV ADI Severity level -> [ADI]CODE =428;GRALEV (ATABDIV) !RTZ
  ITTDATEND D Intervention end
  ITTDUR C*4 Duration
  ITTDURBAS M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTFCY M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTLTIMAX C*4 Max intrvn LT
  OTHCNI CLX Other constraints
  SOLLTIMAX C*4 Max rsltn LT
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CQL]UPDUSR (AUTILIS) !Other

## CONTREW (CRE) - Contract renewals
Keys (first = PK; D = duplicates allowed): CRE1 CONNUM+REWRECNUMX
Fields:
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[CRE]CONNUM (CONTSERV) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CRE]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice no.
  PRONUMINV L*8 Process number
  REWEND D End
  REWMAN C*2 Manual renew.
  REWRECNUMX L*8 Number
  REWSTR D Start
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CRE]UPDUSR (AUTILIS) !Other

## CONTREWX (CRX) - Contract renewals
Keys (first = PK; D = duplicates allowed): CRX0 CONNUM+REWRECNUMX+PRONUM
Fields:
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[CRX]CONNUM (CONTSERV) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CRX]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice no.
  PRONUM L*8 Process number
  PRONUMINV L*8 Process number
  REWEND D End
  REWMAN C*2 Manual renew.
  REWRECNUMX L*8 Number
  REWSTR D Start
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CRX]UPDUSR (AUTILIS) !Other

## CONTSERV (CON) - Service contract
Notes: differs in V9.0 P12 (diff: AT3_CONTSERV.htm); differs in V10 P1 (diff: ATD_CONTSERV.htm)
Keys (first = PK; D = duplicates allowed): CON0 CONNUM; CON1 CONENDDAT (D); CON2 CONBPC (D); CON3 CONCCN (D); CON4 CONBPC+RSIFLG+FDDFLG (D); CON5 CONORI+CONORIVCR+CONORIVCRL (D)
Fields:
  ACPDPTCOD ADI(25) Litigation accepted -> [ADI]CODE =315;ACPDPTCOD (ATABDIV) !Block
  AMTPLY MD1 Penalty amount
  AMTPLYX MD1 Penalty amount
  AUUID AUUID Single identifier
  BASEXXAMT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXAMTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOL M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOLX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CONAMT MD1 Amount
  CONBASFOR ADI Revaluation formula -> [ADI]CODE =427;CONBASFOR (ATABDIV) !Block
  CONBASIDX ADI Indexing database -> [ADI]CODE =410;CONBASIDX (ATABDIV) !Block
  CONBPC BPR Sold-to -> [BPR]BPR0 =[CON]CONBPC (BPARTNER) !Block
  CONBPCGRU BPR Group customer -> [BPR]BPR0 =[CON]CONBPCGRU (BPARTNER) !Block
  CONBPCINV BPR Bill-to customer -> [BPR]BPR0 =[CON]CONBPCINV (BPARTNER) !Block
  CONBPCPYR BPR Pay-by -> [BPR]BPR0 =[CON]CONBPCPYR (BPARTNER) !Block
  CONCAT M*15 Category [menu 2976: 1=Warranty,2=Meeting,3=Maintenance,4=By points]
  CONCCN AIN Contact (relationship) -> [AIN]AIN0 =[CON]CONCCN (CONTACTCRM) !Block
  CONCHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CONCOT VCR Contract template
  CONENDDAT D End date
  CONNAM A*85 Description
  CONNUM VCR Code
  CONORI M*15 Source [menu 2977: 1=Manual creation,2=Sales order,3=Sales shipment,4=Sales invoice,5=Warranty request,6=Service contract duplication,7=Points credit]
  CONORIVCR VCR Original document no.
  CONORIVCRL L*8 Source document line
  CONPJT PJT Project -> [PIM]PIM0 =[CON]CONPJT (PIMPL) !Block
  CONPRITYP M*6 Price type [menu 243: 1=Exclude tax,2=Include tax]
  CONREW M*4 Renewable [menu 1: 1=No,2=Yes]
  CONSTRDAT D Start date
  CONTYP ADI Statistical group -> [ADI]CODE =indice+440;CONTYP(indice) (ATABDIV) !Block act:STO
  CONTYPCLA DES Category
  CONVACBPR TVB Tax rule -> [TVB]TVB0 =CONVACBPR;[V]GSUPCLE (TABVACBPR) !Block
  CPY CPY Company -> [CPY]CPY0 =[CON]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRSCOVSAM M*4 Coverage viewed [menu 1: 1=No,2=Yes]
  CUR CUR Currency -> [TCU]TCU0 =[CON]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[CON]DIE (GDIE) !Block act:ANA
  DSYWND C*2 Display left list
  EVRMAC M*4 All products [menu 1: 1=No,2=Yes]
  EVRPBL M*4 All skills [menu 1: 1=No,2=Yes]
  FDDFLG M*4 Archived [menu 1: 1=No,2=Yes]
  FDDUSR A*5 Archived by
  GUA M*4 Warranty [menu 1: 1=No,2=Yes]
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[CON]INVDTA (SFOOTINV) !Block act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVFRY C*4 Invoicing freq
  INVFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVFRYCOE DCB*3.2 Coefficient
  INVLTI C*4 Invoicing advance notice
  INVLTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVMET M*15 Invoicing method [menu 2978: 1=Pre-invoicing (term to mature),2=Post-invoicing (over due term)]
  ITMREF ITM Product code -> [ITM]ITM0 =[CON]ITMREF (ITMMASTER) !Block
  ITTDATEND D Intervention end
  ITTDATENDX D Intervention end
  ITTDUR C*4 Duration
  ITTDURBAS M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURBASX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURX C*4 B duration
  ITTFCY M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTFCYX M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTLTIMAX C*4 Max intrvn LT
  ITTLTIMAXX C*4 Max intrvn LT
  LASIDXDAT D Last value date
  LASINVDAT D Last invoice
  LASVALIDX MD1 Last index value
  MANCONENDDAT D End date
  MANCONREW M*4 Renewable [menu 1: 1=No,2=Yes]
  MANCONSTRDAT D Start date
  MANREWAMT MD1 Renewal amount
  MANREWFLG M*4 To renew [menu 1: 1=No,2=Yes]
  MANREWFRY C*4 Renew frequency
  MANREWFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  NEXINVAMT MD1 Next invoice amount
  NEXINVDAT D Next invoice
  NEXSHIINV D Next invoice sending
  OCONAMT MD1 Amount
  OCONENDDAT D End date
  OCONSTRDAT D Start date
  ODSYWND C*2 Old left list
  OINV SIH Invoice -> [SIV]SIV0 =[CON]OINV (SINVOICEV) !Other
  OLASIDXDAT D Last value date
  OLASINVDAT D Prev last invoice
  OLASVALIDX MD1 Last index value
  ONEXINVAMT MD1 Old amount
  ONEXINVDAT D Former next invoice
  ONEXSHIINV D Former next mailing
  ORDLINNUM L*8 Order line no.
  ORDNUM SOH Order number -> [SOH]SOH0 =[CON]ORDNUM (SORDER) !Block
  ORDUPDFLG M*4 Order no. modification [menu 1: 1=No,2=Yes]
  OREWINV SIH Invoice -> [SIV]SIV0 =[CON]OREWINV (SINVOICEV) !Other
  ORVADAT D Revaluation date
  ORVAINV SIH Invoice -> [SIV]SIV0 =[CON]ORVAINV (SINVOICEV) !Other
  OTHCNI CLX Other constraints
  PITBLC L*8 Remaining points
  PITCDT L*8 Points credit
  PITCSM L*8 Points consumed
  PITRER L*8 Points available
  PITTOL C*3 Points tolerance
  PTE PTE Payment terms -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REWFRY C*4 Renew frequency
  REWFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RSIDAT D Termination date
  RSIFLG M*4 Cancelled contract [menu 1: 1=No,2=Yes]
  RSILTI C*4 Advance notice of cancellation
  RSILTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RSIREN ADI Termination reason -> [ADI]CODE =429;RSIREN (ATABDIV) !Block
  RVADAT D Revaluation date
  RVAFRY C*4 Revaluation freq
  RVAFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RVAMET M*15 Revaluation method [menu 2979: 1=Post re-evaluation,2=Pre re-evaluation]
  RVASSP M*15 Revaluation support [menu 2974: 1=Index development,2=Mathematical formula]
  SALFCY FCY Sales site -> [FCY]FCY0 =[CON]SALFCY (FACILITY) !Block
  SALREP REP Sales rep -> [REP]REP0 =[CON]SALREP (SALESREP) !Block act:REC
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SIUDAT D Subscription date
  SOLLTIMAX C*4 Max rsltn LT
  SOLLTIMAXX C*4 Max rsltn LT
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CONTSERVX (COX) - Service contract
Keys (first = PK; D = duplicates allowed): COX0 CONNUM
Fields:
  ACPDPTCOD ADI(25) Litigation accepted -> [ADI]CODE =315;ACPDPTCOD (ATABDIV) !Block
  AMTPLY MD1 Penalty amount
  AMTPLYX MD1 Penalty amount
  AUUID AUUID Single identifier
  BASEXXAMT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXAMTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOL M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOLX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CONAMT MD1 Amount
  CONBASFOR ADI Revaluation formula -> [ADI]CODE =427;CONBASFOR (ATABDIV) !Block
  CONBASIDX ADI Indexing database -> [ADI]CODE =410;CONBASIDX (ATABDIV) !Block
  CONBPC BPR Sold-to -> [BPR]BPR0 =[COX]CONBPC (BPARTNER) !Block
  CONBPCGRU BPR Group customer -> [BPR]BPR0 =[COX]CONBPCGRU (BPARTNER) !Block
  CONBPCINV BPR Bill-to customer -> [BPR]BPR0 =[COX]CONBPCINV (BPARTNER) !Block
  CONBPCPYR BPR Pay-by -> [BPR]BPR0 =[COX]CONBPCPYR (BPARTNER) !Block
  CONCAT M*15 Category [menu 2976: 1=Warranty,2=Meeting,3=Maintenance,4=By points]
  CONCCN AIN Contact (relationship) -> [AIN]AIN0 =[COX]CONCCN (CONTACTCRM) !Block
  CONCHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CONCOT VCR Contract template
  CONENDDAT D End date
  CONNAM A*85 Description
  CONNUM VCR Code
  CONORI M*15 Source [menu 2977: 1=Manual creation,2=Sales order,3=Sales shipment,4=Sales invoice,5=Warranty request,6=Service contract duplication,7=Points credit]
  CONORIVCR VCR Document no.
  CONORIVCRL L*8 Journal line
  CONPJT OPP Project -> [OPP]OPP0 =[COX]CONPJT (OPPOR) !Block
  CONPRITYP M*6 Price type [menu 243: 1=Exclude tax,2=Include tax]
  CONREW M*4 Renewable [menu 1: 1=No,2=Yes]
  CONSTRDAT D Start date
  CONTYP ADI Statistical group -> [ADI]CODE =indice+440;CONTYP(indice) (ATABDIV) !Block act:STO
  CONTYPCLA DES Category
  CONVACBPR TVB Tax rule -> [TVB]TVB0 =CONVACBPR;[V]GSUPCLE (TABVACBPR) !Block
  CPY CPY Company -> [CPY]CPY0 =[COX]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRSCOVSAM M*4 Coverage viewed [menu 1: 1=No,2=Yes]
  CUR CUR Currency -> [TCU]TCU0 =[COX]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[COX]DIE (GDIE) !Block act:ANA
  DSYWND C*2 Display left list
  EVRMAC M*4 All products [menu 1: 1=No,2=Yes]
  EVRPBL M*4 All skills [menu 1: 1=No,2=Yes]
  FDDFLG M*4 Archived [menu 1: 1=No,2=Yes]
  FDDUSR A*5 Archived by
  GUA M*4 Warranty [menu 1: 1=No,2=Yes]
  INVDTA C*2 Invoicing element act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVFRY C*4 Invoicing freq
  INVFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVFRYCOE DCB*3.2 Coefficient
  INVLTI C*4 Invoicing advance notice
  INVLTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVMET M*15 Invoicing method [menu 2978: 1=Pre-invoicing (term to mature),2=Post-invoicing (over due term)]
  ITMREF ITM Product code -> [ITM]ITM0 =[COX]ITMREF (ITMMASTER) !Block
  ITTDATEND D Intervention end
  ITTDATENDX D Intervention end
  ITTDUR C*4 Duration
  ITTDURBAS M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURBASX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURX C*4 B duration
  ITTFCY M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTFCYX M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTLTIMAX C*4 Max intrvn LT
  ITTLTIMAXX C*4 Max intrvn LT
  LASIDXDAT D Last value date
  LASINVDAT D Last invoice
  LASVALIDX MD1 Last index value
  MANREWAMT MD1 Renewal amount
  MANREWFLG M*4 To renew [menu 1: 1=No,2=Yes]
  NEXINVAMT MD1 Next invoice amount
  NEXINVDAT D Next invoice
  NEXSHIINV D Next invoice sending
  OCONAMT MD1 Amount
  OCONENDDAT D End date
  OCONSTRDAT D Start date
  ODSYWND C*2 Old left list
  OINV SIH Invoice -> [SIV]SIV0 =[COX]OINV (SINVOICEV) !Block
  OLASIDXDAT D Last value date
  OLASINVDAT D Prev last invoice
  OLASVALIDX MD1 Last index value
  ONEXINVAMT MD1 Old amount
  ONEXINVDAT D Former next invoice
  ONEXSHIINV D Former next mailing
  ORDLINNUM L*8 Order line no.
  ORDNUM SOH Order number -> [SOH]SOH0 =[COX]ORDNUM (SORDER) !Block
  ORDUPDFLG M*4 Order no. modification [menu 1: 1=No,2=Yes]
  OREWINV SIH Invoice -> [SIV]SIV0 =[COX]OREWINV (SINVOICEV) !Block
  ORVADAT D Revaluation date
  ORVAINV SIH Invoice -> [SIV]SIV0 =[COX]ORVAINV (SINVOICEV) !Block
  OTHCNI CLX Other constraints
  PITBLC L*8 Remaining points
  PITCDT L*8 Points credit
  PITCSM L*8 Points consumed
  PITRER L*8 Points available
  PITTOL C*3 Points tolerance
  PRONUM L*8 Process number
  PTE PTE Payment terms -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REWFRY C*4 Renew frequency
  REWFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RSIDAT D Termination date
  RSIFLG M*4 Cancelled contract [menu 1: 1=No,2=Yes]
  RSILTI C*4 Advance notice of cancellation
  RSILTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RSIREN ADI Termination reason -> [ADI]CODE =429;RSIREN (ATABDIV) !Block
  RVADAT D Revaluation date
  RVAFRY C*4 Revaluation freq
  RVAFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RVAMET M*15 Revaluation method [menu 2979: 1=Post re-evaluation,2=Pre re-evaluation]
  RVASSP M*15 Revaluation support [menu 2974: 1=Index development,2=Mathematical formula]
  SALFCY FCY Sales site -> [FCY]FCY0 =[COX]SALFCY (FACILITY) !Block
  SALREP REP Sales rep -> [REP]REP0 =[COX]SALREP (SALESREP) !Block act:REC
  SIUDAT D Subscription date
  SOLLTIMAX C*4 Max rsltn LT
  SOLLTIMAXX C*4 Max rsltn LT
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CONTTEMPL (COT) - Service contract template
Keys (first = PK; D = duplicates allowed): COT0 CONNUM
Fields:
  ACPDPTCOD ADI(25) Litigation accepted -> [ADI]CODE =315;ACPDPTCOD (ATABDIV) !Block
  AMTPLY MD1 Penalty amount
  AMTPLYX MD1 Penalty amount
  AUUID AUUID Single identifier
  BASEXXAMT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXAMTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITT M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXITTX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOL M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  BASEXXSOLX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  CONBASFOR ADI Revaluation formula -> [ADI]CODE =427;CONBASFOR (ATABDIV) !Block
  CONBASIDX ADI Indexing database -> [ADI]CODE =410;CONBASIDX (ATABDIV) !Block
  CONCAT M*15 Category [menu 2976: 1=Warranty,2=Meeting,3=Maintenance,4=By points]
  CONNUM VCR Code
  CONREW M*4 Renewable [menu 1: 1=No,2=Yes]
  CONTYP ADI Statistical group -> [ADI]CODE =indice+440;CONTYP(indice) (ATABDIV) !Block act:STO
  CONTYPCLA DES Category
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRSCOVSAM M*4 Coverage viewed [menu 1: 1=No,2=Yes]
  CUR CUR Currency -> [TCU]TCU0 =[COT]CUR (TABCUR) !Block
  EVRMAC M*4 All products [menu 1: 1=No,2=Yes]
  EVRPBL M*4 All skills [menu 1: 1=No,2=Yes]
  GUA M*4 Warranty [menu 1: 1=No,2=Yes]
  INVFRY C*4 Invoicing freq
  INVFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVFRYCOE DCB*3.2 Coefficient
  INVLTI C*4 Invoicing advance notice
  INVLTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  INVMET M*15 Invoicing method [menu 2978: 1=Pre-invoicing (term to mature),2=Post-invoicing (over due term)]
  ITTDATEND D Intervention end
  ITTDATENDX D Intervention end
  ITTDUR C*4 Duration
  ITTDURBAS M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURBASX M*15 Expression database [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  ITTDURX C*4 B duration
  ITTFCY M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTFCYX M*4 Intervention / site [menu 1: 1=No,2=Yes]
  ITTLTIMAX C*4 Max intrvn LT
  ITTLTIMAXX C*4 Max intrvn LT
  LASIDXDAT D Last value date
  LASVALIDX L*8 Last index value
  MRK CLX Notes
  OTHCNI CLX Other constraints
  PITCDT L*8 Points credit
  PITRQD L*8 Tokens necessary
  PITTOL C*3 Points tolerance
  PTE PTE Payment terms -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REWFRY C*4 Renew frequency
  REWFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RSILTI C*4 Advance notice of cancellation
  RSILTIBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RVAFRY C*4 Revaluation freq
  RVAFRYBAS M*15 Basis [menu 976: 1=hours,2=days,3=weeks,4=months,5=years,6=]
  RVAMET M*15 Revaluation method [menu 2979: 1=Post re-evaluation,2=Pre re-evaluation]
  RVASSP M*15 Revaluation support [menu 2974: 1=Index development,2=Mathematical formula]
  SOLLTIMAX C*4 Max rsltn LT
  SOLLTIMAXX C*4 Max rsltn LT
  TPLNAM DCO Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## COSTSTCB (STCB) - Cost structure - schedules
Keys (first = PK; D = duplicates allowed): STCB0 STCNUM+STCLIN+STCLIM; STCB1 STCNUM+STCLIN+MINLIM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Creation date
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[STCB]CUR (TABCUR) !Block
  MAXLIM MD6 Upper range
  MINLIM MD6 Lower range
  STCLIM L*8 Range line
  STCLIN L*8 Structure line
  STCNUM VCR Cost structure
  UNTPRI MD6 Unit price
  UOM UOM Unit -> [TUN]TUN0 =[STCB]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## COSTSTCF (STCF) - Cost structure - site
Keys (first = PK; D = duplicates allowed): STCF0 ITMREF+BPSNUM+STOFCY
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPN Supplier
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[STCF]CREUSR (AUTILIS) !Other
  ITMDESBPS DES Supplier description
  ITMREF ITM Product -> [ITM]ITM0 =[STCF]ITMREF (ITMMASTER) !Delete
  ITMREFBPS A*20 Supplier product
  STCNUM VCR Cost structure
  STOFCY A*5 Storage site
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[STCF]UPDUSR (AUTILIS) !Other

## COSTSTCH (STCH) - Cost structure
Keys (first = PK; D = duplicates allowed): STCH0 STCNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  STCNUM VCR Cost structure
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## COSTSTCL (STCL) - Cost structure - lines
Keys (first = PK; D = duplicates allowed): STCL0 STCNUM+STCLIN
Fields:
  AUUID AUUID Single identifier
  BAS M*25 Basis [menu 2091: 1=Quantity,2=Volume,3=Weight]
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[STCL]CUR (TABCUR) !Block
  DIRCLCMOD M*25 Calculation mode [menu 2089: 1=Percentage per net price,2=Fixed amount,3=Amount per unit,4=Amount by fixed bracket,5=Schedule,6=Weighted amount,7=Formula]
  DOCCHGTYP M*4 Doc rate type [menu 1: 1=No,2=Yes]
  FCSCOD FCS Cost -> [FCS]FCS0 =[STCL]FCSCOD (FRECST) !Block
  FCSDES AX3 Description
  FCSNAT M*40 Cost nature [menu 2276: 1=Packaging,2=Loading,3=Pre-transport,4=Export customs formality,5=Main transport loading,6=Main transport,7=Main transport unloading,8=Import customs formalities,9=Post-transport,10=Unloading,11=Insurance,12=Others]
  FORFCS FOR Formula -> [TFO]TFO0 ="C";FORFCS (TABFOR) !Block
  HGHBKT M*4 Higher fixed bracket [menu 1: 1=No,2=Yes]
  LIM M*4 Range [menu 1: 1=No,2=Yes]
  LIMTYP M*25 Schedule [menu 2094: 1=Per unit,2=Amount]
  PRINETPRC DCB*5.4 Percentage per net price
  QTY QTY Quantity
  STCLIN L*8 Structure line
  STCNUM VCR Cost structure
  STKVLT M*4 Stock valuation [menu 1: 1=No,2=Yes]
  UNTPRI MD6 Unit price
  UOM UOM Unit -> [TUN]TUN0 =[STCL]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEIPRC DCB*5.4 Weighting percentage:

## CPTANALIN (CAL) - Analytical accounting lines
Keys (first = PK; D = duplicates allowed): CAL0 ABRFIC+VCRTYP+VCRNUM+VCRLIN+VCRSEQ+CPLCLE+ANALIG
Fields:
  ABRFIC ABR Table abbreviation
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !RTZ
  AMT MD1 Amount
  ANALIG C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !RTZ act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[CAL]COA (GCOA) !RTZ
  CPLCLE A*30 Key complement
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CAL]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[CAL]CUR (TABCUR) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[CAL]DIE (GDIE) !RTZ act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !RTZ
  GLU UOM Non-financial unit -> [TUN]TUN0 =[CAL]GLU (TABUNIT) !RTZ
  LED LED(10) Ledger -> [LED]LED0 =[CAL]LED (GLED) !RTZ
  QTY QTY Quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CAL]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## CPTFOOTLNK (CFL) - Analytical accounting lines
Keys (first = PK; D = duplicates allowed): CAL0 ABRFIC+VCRTYP+VCRNUM+VCRLIN+VCRSEQ+CPLCLE+ANALIG
Fields:
  ABRFIC ABR Table abbreviation
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !RTZ
  AMT MD1 Amount
  ANALIG C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !RTZ act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[CFL]COA (GCOA) !RTZ
  CPLCLE A*30 Key complement
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CFL]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[CFL]CUR (TABCUR) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[CFL]DIE (GDIE) !RTZ act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !RTZ
  GLU UOM Non-financial unit -> [TUN]TUN0 =[CFL]GLU (TABUNIT) !RTZ
  LED LED(10) Ledger -> [LED]LED0 =[CFL]LED (GLED) !RTZ
  QTY QTY Quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFL]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## CTRLNIVW (CNW) - Lev. control workbench
Keys (first = PK; D = duplicates allowed): CNW0 ITMREF+BOMALT+BOMALTTYP
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CNW]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[CNW]ITMREF (ITMMASTER) !Delete
  NIV C*4 Level
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CNW]UPDUSR (AUTILIS) !Other

## CTSWSP (CTSW) - Control system
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): CTSW0 CPY+NUM; CTSW1 CPY+CREDATTIM
Fields:
  AUUID AUUID Single identifier
  BASCOS DCB*10.2 Taxable amount
  BPCNAM NAM(2) Customer name
  BPCNUM BPR Customer -> [BPR]BPR0 =[CTSW]BPCNUM (BPARTNER) !Delete
  CODOPE ADI Operation code -> [ADI]CODE =393;CODOPE (ATABDIV) !Block
  CPY CPY Company -> [CPY]CPY0 =[CTSW]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CRETYP A*1 Credit memo type
  CREUSR AUS User -> [AUS]CODUSR =[CTSW]CREUSR (AUTILIS) !Other
  CRN CRN Site tax ID no.
  CRY CRY Country -> [TCY]TCY0 =[CTSW]CRY (TABCOUNTRY) !Delete
  CSV A*16 CSV export
  DOCTYP M*4 Document type [menu 2004: 1=Site tax ID number,2=Intracommunity tax ID number,3=Passport,4=Official document,5=Fiscal residence certificate,6=Others]
  ERRDES A*250 Description
  ERRINT M*4 Error [menu 1: 1=No,2=Yes]
  ERRINTDES A*250 Error message
  EXTREF A*60 External reference
  FCY FCY Site -> [FCY]FCY0 =[CTSW]FCY (FACILITY) !Delete
  INVDAT D Invoice date
  INVHOU HMM Time
  INVNUM A*60 Document number
  NIFREP A*9 Representative TIN
  NUM VCR Document no.
  NUMFAC A*60 Invoice number
  PREINVDAT D Date
  PRESTA A*100 Status
  QRFLG M*4 QR image [menu 1: 1=No,2=Yes]
  QRTEXT A*250 QR-data
  RESCOD A*250 Code
  RESSTA A*100 Status code
  RETSOP M*4 Withholdings [menu 1: 1=No,2=Yes]
  SENDDAT D Send date
  SENDHOU HMM Time
  SIGNATURE AC0*3 Signature
  STA M*15 Status [menu 2107: 1=Accepted,2=In error,3=Canceled]
  TBAI A*30 Number
  TBAIFILE AC0*1 File
  TERDEC M*15 Territory of declaration [menu 2108: 1=Common territory,2=Navarre,3=Biscay,4=Gipuzkoa,5=Álava,6=Canary Islands]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CTSW]UPDUSR (AUTILIS) !Other

## DEB (DEB) - EU exchange declaration
Notes: activity code DEB; differs in V9.0 P12 (diff: AT3_DEB.htm)
Keys (first = PK; D = duplicates allowed): DEB0 CPY+DEBDAT+FLO+VCRTYP+VCRNUM+VCRLIN; DEB1 CPY+VCRTYP+VCRNUM+VCRLIN+FLO (D); DEB2 CPY+DEBDAT+FLO+DEBLIN
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[DEB]BPRNUM (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[DEB]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DEB]CREUSR (AUTILIS) !Other
  CRYFCY CRY Site country -> [TCY]TCY0 =[DEB]CRYFCY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[DEB]CUR (TABCUR) !Block
  CUSREF A*12 Customs reference
  DAT D Document date
  DEBDAT D Intrastat date
  DEBLIN L*8 Line no.
  DESCRY A*3 Receiving/issuing country
  DESPRO A*2 Destination province act:KIT
  EECICT ICT Incoterm -> [ICTH]ICT0 =[DEB]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU]
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block
  EECNUM A*20 EU identification
  EECNUMDEB C*4 EU Intrastat
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled]
  EECUNT DCB*13 Intrastat additional units
  EECUSU A*12 Additional unit act:KIT
  EXPNUM L*8 Export number
  FISAMT DCB*10.2 EU fiscal value
  FLO M*15 Automatic flows [menu 205: 1=Arrivals,2=Dispatches,3=Arrivals and Dispatches,4=]
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[DEB]ITMREF (ITMMASTER) !Block
  LINVALOFLG M*4 Valuated line [menu 1: 1=No,2=Yes]
  MON C*2 Months act:KIT
  NETMAS DCB*12.3 EU net weight
  NIV C*1 EU declaration level
  ORICRY A*3 Country of origin
  PORT ADI Port -> [ADI]CODE =951;PORT (ATABDIV) !Block act:DEBP
  REG A*2 Department
  REGION ADI Region -> [ADI]CODE =950;REGION (ATABDIV) !Block act:KPO
  SIGN A*1 Sign act:KIT
  STAAMT DCB*10.2 Statistic value
  STAFED A*40 Region/State act:DEBR
  STOFCY FCY Storage site -> [FCY]FCY0 =[DEB]STOFCY (FACILITY) !Block
  TRIM C*2 Quarter act:KIT
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DEB]UPDUSR (AUTILIS) !Other
  VALAMT DCB*10.2 Value in currency act:KIT
  VCRLIN L*8 Entry line no.
  VCRLINVALO L*8(15) Journal line
  VCRNUM VCR Order no.
  VCRNUMVALO VCR(15) Inv/credits
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  YEA C*4 Year act:KIT

## DEBPAR (DER) - Intrastat computation parameters
Notes: activity code DEB
Keys (first = PK; D = duplicates allowed): DER0 EECNUMDEB
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[DER]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DER]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DER]CUR (TABCUR) !Block
  DEBDAT D Intrastat date
  EECNUMDEB C*4 EU Intrastat
  FLO M*15 Automatic flows [menu 205: 1=Arrivals,2=Dispatches,3=Arrivals and Dispatches,4=]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DER]UPDUSR (AUTILIS) !Other

## DEBREGNAT (DRN) - Movement rule and nature
Notes: activity code DEB
Keys (first = PK; D = duplicates allowed): DRN0 LEG+CRY+GRP+MVT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DRN]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[DRN]CRY (TABCOUNTRY) !Delete
  EECNAT TEC Type -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block
  EECNATR TEC Adjust nature -> [TEC]TEC0 =EECNATR;[V]GSUPCLE (TABEECNAT) !Block
  EECSCH TSC Rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block
  EECSCHR TSC Adjust rule -> [TSC]TSC0 =EECSCHR;[V]GSUPCLE (TABEECSCH) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLUX M Physical flow [menu 205: 1=Arrivals,2=Dispatches,3=Arrivals and Dispatches,4=]
  FLUXREGUL M Adjustment flow [menu 205: 1=Arrivals,2=Dispatches,3=Arrivals and Dispatches,4=]
  GRP AGF Group -> [AGF]AGF0 =[DRN]GRP (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MVT M Movement [menu 2236: 24 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DRN]UPDUSR (AUTILIS) !Other
  VALSTO M*4 Value stock [menu 1: 1=No,2=Yes]

## DECAT (DLA) - WI declaration
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## DEFVAL (DVA) - Complex default values
Keys (first = PK; D = duplicates allowed): DVA0 OBC+PARAM
Fields:
  ALHX A*100(20) Alphanumeric fields
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DVA]CREUSR (AUTILIS) !Other
  DATX D(20) Date fields
  DCBX DCB*9.2(20) Decimal field
  INTX L*8(50) Numeric fields
  OBC A*3 Object
  PARAM A*100 Parameter
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DVA]UPDUSR (AUTILIS) !Other

## DIAHOU (DIH) - Time table schemas
Keys (first = PK; D = duplicates allowed): DIH0 NUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DIANAM A*70 Description
  DIANAMAXX AXX Description
  DIASHO SHO Short description
  DIASHOAXX AX1 Short description
  ENDHOU HM(5) End
  NUM A*10 Time table schema
  STRHOU HM(5) Start
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## DICOEMP (DIC) - Employee field dictionary
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## DIETRS (DTR) - Analytical entry transaction
Notes: differs in V9.0 P12 (diff: AT3_DIETRS.htm); differs in V10 P1 (diff: ATD_DIETRS.htm)
Keys (first = PK; D = duplicates allowed): DTR0 ABRFIC+DTRTYP+DTRNUM+DTRTNU+DTRLIN; DTR1 ABRFIC+DTRTYP+DTRNUM+DTRTNU+DIE
Fields:
  ABRFIC ABR Table abbreviation
  AUUID AUUID Single identifier
  CCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CCESCR2 M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CCESCR3 M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTR]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[DTR]DIE (GDIE) !Block
  DSPCOD M*15 Distribution [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DSPSCR M*18 Distribution [menu 99: 1=Form and table,2=Form,3=Table]
  DTRLIN L*8 Line number
  DTRNUM TRS Transaction
  DTRTNU C*1 Grid number
  DTRTYP C*2 Transaction type
  HEACCECOD M*15 Dimension header [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOCCECOD M*15 Analyt.dimension.mvts [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTR]UPDUSR (AUTILIS) !Other

## DIETRSXX (DTX) - Analytical entry transaction
Keys (first = PK; D = duplicates allowed): DTR0 ABRFIC+DTRTYP+DTRNUM+DTRTNU+DTRLIN
Fields:
  ABRFIC ABR Table abbreviation
  AUUID AUUID Single identifier
  CCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CCESCR2 M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CCESCR3 M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTX]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[DTX]DIE (GDIE) !Other
  DSPCOD M*15 Distribution [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DSPSCR M*18 Distribution [menu 99: 1=Form and table,2=Form,3=Table]
  DTRLIN L*8 Line number
  DTRNUM TRS Transaction
  DTRTNU C*1 Grid number
  DTRTYP C*2 Transaction type
  HEACCECOD M*15 Dimension header [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOCCECOD M*15 Analyt.dimension.mvts [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTX]UPDUSR (AUTILIS) !Other

## DKSDATA (DKD) - Electronic signatures
Notes: activity code DKS; differs in V9.0 P12 (diff: AT3_DKSDATA.htm); differs in V10 P1 (diff: ATD_DKSDATA.htm)
Keys (first = PK; D = duplicates allowed): DKD0 KEYCODE+DOCTYP+DOCNUM; DKD1 KEYCODE+DKSDOCNUM (D)
Fields:
  ACCESSDATE D Read date act:EFAT
  ACCESSIP A*40 IP address act:EFAT
  ACCESSTIME A*8 Read time act:EFAT
  ANMCODE ANM Sequence number -> [ANM]ANM0 =[DKD]ANMCODE (ACODNUM) !Block
  ATDTCOD A*200 AT code act:KPO
  ATDTCOMKEY A*24 Symmetric key act:KPO
  ATDTCOMSTA A*200 Communication status act:KPO
  ATDTDATTIM A*24 Send date act:KPO
  ATDTINPTYP M*4 Record type [menu 2049: 1=Manual,2=SAFT-T,3=Web service] act:KPO
  ATDTRECDAT D AT code reception act:KPO
  ATDTRECTIM HS AT code reception act:KPO
  ATDTREQDAT D AT code request act:KPO
  ATDTREQTIM HS AT code request act:KPO
  ATDTTESMOD M*10 Test mode [menu 1: 1=No,2=Yes] act:KPO
  ATEI M*20 Tax authority EI [menu 2426: 1=Not sent,2=Sent with error,3=Pending response from EFAT,4=Pending response from business partner,5=Communication successful] act:EFAT
  AUUID AUUID Single identifier
  BPEI M*20 Customer EI [menu 2426: 1=Not sent,2=Sent with error,3=Pending response from EFAT,4=Pending response from business partner,5=Communication successful] act:EFAT
  CERNUM C*4 Certificate number
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DKD]CREUSR (AUTILIS) !Other
  DIGSIGN A*173 Electronic signature
  DKSDOCNUM A*60 Document number
  DOCBASTYP A*3 Type
  DOCLINK A*200 Document link EFAT act:EFAT
  DOCNUM VCR Document number
  DOCSTA M*4 Document status [menu 1: 1=No,2=Yes]
  DOCTYP A*5 Entry type
  EFATMESS A*200 EFAT TA message act:EFAT
  EFATSENT A*20 Date act:EFAT
  EXPDATE D Expiration date act:EFAT
  GROSSTOT DCB*13.4 Gross total
  GROSSTOTFLG M*4 Gross total [menu 1: 1=No,2=Yes]
  KEYCODE A*20 Code
  KEYVER C*4 Key version
  OLDDOCTYP VCR Document type act:KPO
  PDKSDOCNUM A*60 Previous doc no.
  PRNCHAR A*4 Car. to print
  RATCUR RCU Currency rate act:KPO
  RECTYP M*4 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document]
  SAFTINVTYP M*15 SAF-T document type [menu 2028: 1=Invoice,2=Simplified invoice,3=Debit note,4=Credit note,5=Fixed assets sale,6=Fixed assets return,7=Invoice-Receipt,8=Proforma,9=Consignment invoice] act:KPO
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)] act:KPO
  SYSENTDAT A*19 System entry date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DKD]UPDUSR (AUTILIS) !Other
  VALIDDAT D Validation date
  VALIDTIM HS Validation time
  VCRTYP M*15 Entry type [menu 2047: 1=All types,2=Deliveries,3=Customer returns,4=Loan returns,5=Sub-cont material returns,6=Inter-site transfers,7=Sub-contract transfers,8=Sub-contract returns,9=Purchase returns,10=Transport note,11=Orders,12=Quotes,13=Proforma]
  WITHOLTAX DCB*13.4 Withholding tax

## DKSDATAFRA (DKF) - Electronic signatures
Notes: activity code DSFR
Keys (first = PK; D = duplicates allowed): DKF0 KEYCODE+ORIDOC+DOCTYP+DOCNUM+LIN
Fields:
  ACC GAC Account -> [GAC]GAC0 =[DKF]ACC (GACCOUNT) !BSRA
  ACCDAT D Accounting date
  AMTATI MD1 Amount + tax
  AMTCUR MD1 Amount in currency
  AMTLED MD1 Ledger amount
  AMTTAX MD1(10) Tax amount
  AUUID AUUID Single identifier
  BASTAX MD1(10) Tax basis
  BPR BPR BP -> [BPR]BPR0 =[DKF]BPR (BPARTNER) !BSRA
  BPREECNUM EEC EU identif.
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[DKF]CPY (COMPANY) !BSRA
  CPYEECNUM EEC EU identif.
  CPYNAM NAM Company name
  CPYPOSCOD POS Postal code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DKF]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DKF]CUR (TABCUR) !BSRA
  DES DES Description
  DIGSIGN A*250(2) Electronic signature
  DOCNUM VCR Document number
  DOCTYP A*5 Entry type
  DSIDATTIM A*14 Date time
  FCY FCY Site -> [FCY]FCY0 =[DKF]FCY (FACILITY) !BSRA
  FNLPSTDAT D Final date
  FNLPSTNUM VCR Final number
  JOU JOU Journal -> [JOU]JOU0 =[DKF]JOU (GJOURNAL) !BSRA
  JOUDES DES Description
  KEYCODE A*20 Code
  KEYVER C*4 Key version
  LIN C*3 Line number
  MES A*250(3) Message
  ORIDOC C*1 Origin
  POSCOD POS Postal code
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DKF]UPDUSR (AUTILIS) !Other

## DKSDATAPOR (DKP) - Electronic signatures
Notes: activity code KPO; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): DKP0 KEYCODE+ORIDOC+DOCTYP+DOCNUM+LIN
Fields:
  ACC GAC Account -> [GAC]GAC0 =[DKP]ACC (GACCOUNT) !BSRA
  ACCDAT D Accounting date
  AMTCUR MD1 Amount in currency
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DKP]BPR (BPARTNER) !BSRA
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[DKP]CPY (COMPANY) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DKP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DKP]CUR (TABCUR) !BSRA
  DES DES Description
  DIGSIGN A*250(2) Electronic signature
  DOCCREDAT D Date created
  DOCNUM VCR Document number
  DOCTYP A*5 Entry type
  DOCUPDDAT D Change date
  DSIDATTIM A*14 Date time
  FCY FCY Site -> [FCY]FCY0 =[DKP]FCY (FACILITY) !BSRA
  JOU JOU Journal -> [JOU]JOU0 =[DKP]JOU (GJOURNAL) !BSRA
  JOUDES DES Description
  KEYCODE A*20 Code
  KEYVER C*4 Key version
  LIN L*8 Line no.
  MES A*250(3) Message
  ORIDOC C*1 Origin
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DKP]UPDUSR (AUTILIS) !Other

## DKSJAV (DKJ) - Connection parameters
Notes: activity code DKS
Keys (first = PK; D = duplicates allowed): DKJ0 KEYCODE
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DKJ]CREUSR (AUTILIS) !Other
  KEYCODE A*20 Code
  SRVJAVA AMC Java server
  TYPDBA M*15 Database type [menu 57: 1=Oracle,2=SQL Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DKJ]UPDUSR (AUTILIS) !Other

## DKSKEY (DKK) - Key management
Notes: differs in V10 P1 (diff: ATD_DKSKEY.htm)
Keys (first = PK; D = duplicates allowed): DKK0 KEYCODE+KEYVER
Fields:
  ANMCODE ANM(10) Sequence number definition -> [ANM]ANM0 =[DKK]ANMCODE (ACODNUM) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DKK]CREUSR (AUTILIS) !Other
  KEYCODE A*20 Code
  KEYDES AX3 Description
  KEYVER C*4 Key version
  PRIVATEKEY ABB Private key
  PUBLICKEY A*217 Public key
  STRDAT D Start date
  STRDATPAY D Start date
  STRDATWD D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DKK]UPDUSR (AUTILIS) !Other

## DKSLOG (DKL) - Signature log
Notes: activity code DKS
Keys (first = PK; D = duplicates allowed): DKL0 KEYCODE+DOCTYP+DOCNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DKL]CREUSR (AUTILIS) !Other
  DKSORIMES A*117 Original message
  DOCNUM VCR Document number
  DOCTYP A*5 Entry type
  ENCRORIMES ABB Encrypted message
  KEYCODE A*20 Code
  KEYVER C*4 Key version
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DKL]UPDUSR (AUTILIS) !Other

## DMWBPREXC (DMWBPE) - Waste disposal exceptions
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWBPE0 BPR+SCMCOD
Fields:
  AUUID AUUID Single identifier
  BPR BPR Business partner -> [BPR]BPR0 =[DMWBPE]BPR (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWBPE]CREUSR (AUTILIS) !Other
  ENDDAT D Valid to
  NOTE ACB Note
  SCMCOD DMWSC Scheme -> [DMWSC]DMWSC0 =[DMWBPE]SCMCOD (DMWSCHEME) !Block
  STRDAT D Valid from
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWBPE]UPDUSR (AUTILIS) !Other

## DMWPAORD (DMWPAOR) - Waste disposal management
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWPAORD0 COD+TYP+TYPID; DMWPAORD1 COD+TYP (D)
Fields:
  AUUID AUUID Single identifier
  COD DMWSC Code -> [DMWSC]DMWSC0 =[DMWPAOR]COD (DMWSCHEME) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWPAOR]CREUSR (AUTILIS) !Other
  DES AX3 Description
  TYP M*10 Data type [menu 3687: 1=Product group,2=Packing material,3=Pack size,4=Tariff type,5=Tariff category]
  TYPID A*30 ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWPAOR]UPDUSR (AUTILIS) !Other

## DMWPRODPACKD (DMWPPAD) - Product packaging assignment
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWPPAH0 PKGNUM+LIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWPPAD]CREUSR (AUTILIS) !Other
  FLGPKG M*4 Packing [menu 1: 1=No,2=Yes]
  ITMGRP A*30 Product group
  ITMWEI WEI Item weight
  LIN L*8 Line number
  PKGIFF A*60 Packing
  PKGMAT A*30 Packing material
  PKGNUM DMWPPNUM Internal reference act:DMW
  PKGSIZ A*30 Pack size
  STU UOM Stock unit -> [TUN]TUN0 =[DMWPPAD]STU (TABUNIT) !Block
  TAFCAT A*30 Tariff category
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWPPAD]UPDUSR (AUTILIS) !Other
  VER C*4 Version

## DMWPRODPACKH (DMWPPAH) - Product packaging assignment
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWPPAH0 PKGNUM+SCMCOD+ITMREF; DMWPPAH1 SCMCOD+ITMREF
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWPPAH]CREUSR (AUTILIS) !Other
  ENDDAT D Valid to
  ITMREF ITM Product -> [ITM]ITM0 =[DMWPPAH]ITMREF (ITMMASTER) !Delete
  PKGNUM DMWPPNUM Internal reference act:DMW
  SCMCOD DMWSC Scheme -> [DMWSC]DMWSC0 =[DMWPPAH]SCMCOD (DMWSCHEME) !Block
  STRDAT D Valid from
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWPPAH]UPDUSR (AUTILIS) !Other
  VER DMWPPVER Version

## DMWQTY (DMWQTY) - Waste disposal quantity
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWQTY0 SCMCOD+STOFCY+ITMREF+IPTDAT+MVTSEQ+MVTIND; DMWQTY1 SCMCOD+VCRNUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWQTY]CREUSR (AUTILIS) !Other
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[DMWQTY]ITMREF (ITMMASTER) !Delete
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  QTYSTU QTY STK quantity
  SCMCOD DMWSC Scheme -> [DMWSC]DMWSC0 =[DMWQTY]SCMCOD (DMWSCHEME) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[DMWQTY]STOFCY (FACILITY) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWQTY]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Document no.
  VCRNUMRET VCR Document ref

## DMWQUOTAD (DMWQUOD) - Waste management quota
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWQUOD0 QUOTANUM (D); DMWQUOD01 QUOTANUM+PKGMAT+PKGSIZ+TAFTYP
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWQUOD]CREUSR (AUTILIS) !Other
  LIN L*8 Line number
  PKGMAT A*30 Packing material
  PKGSIZ A*30 Pack size
  QUOTA RAT Quota
  QUOTANUM DMWPPNUM Internal reference act:DMW
  TAFTYP A*30 Tariff type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWQUOD]UPDUSR (AUTILIS) !Other
  VER C*4 Version

## DMWQUOTAH (DMWQUOH) - Waste management quota
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWQUOH0 QUOTANUM+SCMCOD+ITMGRP; DMWQUOH1 SCMCOD+ITMGRP
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWQUOH]CREUSR (AUTILIS) !Other
  ENDDAT D Valid to
  ITMGRP A*30 Product group
  QUOTANUM DMWPPNUM Internal reference act:DMW
  SCMCOD DMWSC Scheme -> [DMWSC]DMWSC0 =[DMWQUOH]SCMCOD (DMWSCHEME) !Block
  STRDAT D Valid from
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWQUOH]UPDUSR (AUTILIS) !Other
  VER DMWPPVER Version

## DMWSCHEME (DMWSC) - Waste disposal scheme
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWSC0 COD
Fields:
  AUUID AUUID Single identifier
  BPR BPR Business partner -> [BPR]BPR0 =[DMWSC]BPR (BPARTNER) !Block
  COD A*15 Code
  CPY CPY Company -> [CPY]CPY0 =[DMWSC]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWSC]CREUSR (AUTILIS) !Other
  CRY M*4 Country [menu 3686: 1=Germany,2=Austria]
  DES AX3 Description
  ENDDAT D Valid to
  LICCOD A*30 License number
  NOTE ACB Note
  STRDAT D Valid from
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWSC]UPDUSR (AUTILIS) !Other

## DMWWEIGHT (DMWWEI) - Waste disposal weight
Notes: activity code DMW; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): DMWWEI0 SCMCOD+ITMREF+VCRNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DMWWEI]BPR (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMWWEI]CREUSR (AUTILIS) !Other
  IPTDAT D Allocation date
  ITMGRP A*30 Product group
  ITMREF ITM Product -> [ITM]ITM0 =[DMWWEI]ITMREF (ITMMASTER) !Delete
  ITMWEI WEI Weight
  PKGMAT A*30 Packing material
  PKGSIZ A*30 Pack size
  SCMCOD DMWSC Scheme -> [DMWSC]DMWSC0 =[DMWWEI]SCMCOD (DMWSCHEME) !Block
  TAFCAT A*30 Tariff category
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMWWEI]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Document no.
  VCRNUMRET VCR Document ref
  WEU UOM Weight unit -> [TUN]TUN0 =[DMWWEI]WEU (TABUNIT) !Block

## DOOBPCINT (DBI) - Internal customers
Keys (first = PK; D = duplicates allowed): DBI0 BPCNUM
Fields:
  AUUID AUUID Single identifier
  BPCNAM NAM Customer
  BPCNUM BPR Customer code -> [BPR]BPR0 =[DBI]BPCNUM (BPARTNER) !Delete
  BPCSHO SHO Short description
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DBI]CREUSR (AUTILIS) !Other
  INTBPC M*4 Internal customer [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DBI]UPDUSR (AUTILIS) !Other

## DROITVOTE (DVT) - Voting rights
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## DUEEMP (DUE) - DUE extraction
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## ECCSTA (ECS) - Major version statuses
Keys (first = PK; D = duplicates allowed): ECS0 ITMREF+ECCVALMAJ; ECS1 ITMREF+ECCSTA-ECCVALMAJ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ECCDESAXX AX3 Description
  ECCSHOAXX AX1 Short description
  ECCSTA M*4 Status [menu 2776: 1=Prototype,2=Active,3=Stopped,4=To activate]
  ECCVALMAJ ECS Major version
  ENDDAT D End date
  EXNDAT D Exception date
  EXNFLG M*4 Derogation [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =ITMREF (ITMMASTER) !Block
  SPSFLG M*4 On hold [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  TEX TXC Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ECCVAL (EVL) - Versions
Notes: differs in V10 P1 (diff: ATD_ECCVAL.htm)
Keys (first = PK; D = duplicates allowed): EVL1 ITMREF+ECCVALMAJ+ECCVALMIN+ECCTYP; EVL0 ITMREF+ECCSEQ+ECCTYP
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =ECCTYP;BOMALT (TABBOMALT) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EVL]CREUSR (AUTILIS) !Other
  ECCSEQ C*4 Sequence
  ECCTYP M*30 Flow [menu 2059: 1=Kit,2=Manufacturing BOM,3=Sub-contract BOM,4=Stock]
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  ENDDAT D End date
  EXNDAT D Excp. date
  EXNFLG M*4 Derogation [menu 1: 1=No,2=Yes]
  ITMREF ITM Product -> [ITM]ITM0 =[EVL]ITMREF (ITMMASTER) !Delete
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EVL]UPDUSR (AUTILIS) !Other
  USESTA M*15 Use status [menu 240: 1=In development,2=Available to use]

## EDIBPRCPY (EBC) - EDI flows by BP/company
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDIBPRCPY.htm)
Keys (first = PK; D = duplicates allowed): EBC0 BPRNUM+CPY+PARCOD
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[EBC]BPRNUM (BPARTNER) !Other
  CPY CPY Company -> [CPY]CPY0 =[EBC]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EBC]CREUSR (AUTILIS) !Other
  EXCEDICOD A*20 EDI code
  PARCOD EPR EDI partner -> [EPR]EPR0 =[EBC]PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EBC]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIBPRCPYD (EBCD) - EDI flows by BP/company
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EBCD0 BPRNUM+CPY+PARCOD+NUMLIN; EBCD1 BPRNUM+CPY+PARCOD+SORT; EBCD2 BPRNUM+CPY+PARCOD+CATTYP+CATACT; EBCD3 BPRNUM+CPY+PARCOD+CATCOD+CATACT
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[EBCD]BPRNUM (BPARTNER) !Other
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =[EBCD]CATCOD (EDICAT) !BSRA
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CPY CPY Company -> [CPY]CPY0 =[EBCD]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EBCD]CREUSR (AUTILIS) !Other
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  NUMLIN C*4 Line number
  PARCOD EPR EDI partner -> [EPR]EPR0 =[EBCD]PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EBCD]UPDUSR (AUTILIS) !Other

## EDIBPRPAR (EBP) - EDI partners by BP
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDIBPRPAR.htm); differs in V10 P1 (diff: ATD_EDIBPRPAR.htm)
Keys (first = PK; D = duplicates allowed): EBP0 BPATYP+BPANUM+BPAADD+PARCOD; EBP1 PARCOD+BPATYP+BPANUM+BPAADD
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPANUM BPR BP -> [BPR]BPR0 =[EBP]BPANUM (BPARTNER) !Block
  BPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CENROL M*20(4) Center role [menu 2071: 1=Accounting office,2=Management organ,3=Processing unit,4=Proposing organ] act:KSP
  CHBPCSERCOD A*100 Code act:KFR
  CHBPCSERNAM A*100 Description act:KFR
  CHENGNUMENG A*50 Commitment act:KFR
  CODE A*10(4) Code act:KSP
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EBP]CREUSR (AUTILIS) !Other
  DES A*40(4) Description act:KSP
  DUNS A*20 DUNS
  EDIINVCOD A*20 Bill-to BP code
  EDIORDCOD A*20 Order-to BP code
  EDIPAYCOD A*20 Pay-by BP code
  EDISDHCOD A*20 Ship-to BP code
  EXCEDICOD A*20 EDI code
  GLN A*20 GLN
  IDTYPE M*10 Identification type [menu 2002: 1=Fiscal code,2=Local code,3=GLN,4=DUNS,5=VAT Number,6=Free]
  LOCODE A*20 Local code
  PARCOD EPR EDI partner -> [EPR]EPR0 =[EBP]PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  PUBENT M*4 FACe public entity [menu 1: 1=No,2=Yes] act:KSP
  PUBENTCH M*4 Chorus public entity [menu 1: 1=No,2=Yes] act:KFR
  STA M*20 Status [menu 2000: 1=Disabled,2=Accepted,3=Closed,4=In progress,5=Rejected,6=In process]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EBP]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDICAT (ECA) - EDI category
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDICAT.htm)
Keys (first = PK; D = duplicates allowed): ECA0 CATCOD
Fields:
  AUUID AUUID Single identifier
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =[ECA]CATCOD (EDICAT) !BSRA
  CATDES A*35 Description
  CATTRGTAB ATB Triggering table -> [ATB]CODFIC =[ECA]CATTRGTAB (ATABLE) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CODIND ANX Index code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECA]CREUSR (AUTILIS) !Other
  DESCRIPT A*120 Index descriptor
  DUPLICATE M*30 Duplicate [menu 2010: 1=Authorized,2=Not authorized]
  FNC EFN Function act:EDIX3
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECA]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDICATD (ECAD) - EDI category (filters)
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ECAD0 CATCOD+NUMLIN; ECAD1 CATCOD+SORT
Fields:
  AUUID AUUID Single identifier
  CATCOD CAT Category code -> [ECA]ECA0 =[ECAD]CATCOD (EDICAT) !BSRA
  CODFIC ATB Table code -> [ATB]CODFIC =[ECAD]CODFIC (ATABLE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECAD]CREUSR (AUTILIS) !Other
  FLD A*30 Field
  FLDNAM A*30 Field
  FLDVAL1 A*100 Start
  FLDVAL2 A*100 End
  MANDATORY M*4 Mandatory [menu 1: 1=No,2=Yes]
  NUMLIN C*4 Line number
  OPERATOR M*20 Operator [menu 2023: 1=Value range,2=Equal to,3=Greater than or equal to,4=Less than or equal to]
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDFLG M*4 Enterable [menu 1: 1=No,2=Yes]
  UPDUSR AUS User -> [AUS]CODUSR =[ECAD]UPDUSR (AUTILIS) !Other

## EDICATK (ECAK) - EDI category (authorizations)
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ECAK0 CATCOD+NUMLIN; ECAK1 CATCOD+SORT; ECAK2 CATCOD+CODE
Fields:
  AUUID AUUID Single identifier
  CATCOD CAT Category code -> [ECA]ECA0 =[ECAK]CATCOD (EDICAT) !BSRA
  CODE A*30 Code
  CODFIC ATB Table code -> [ATB]CODFIC =[ECAK]CODFIC (ATABLE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECAK]CREUSR (AUTILIS) !Other
  FLD AVA Field
  NUMLIN C*4 Line number
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECAK]UPDUSR (AUTILIS) !Other

## EDICATL (ECAL) - EDI category (legislations)
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDICATL.htm); differs in V10 P1 (diff: ATD_EDICATL.htm)
Keys (first = PK; D = duplicates allowed): ECAL0 CATCOD+NUMLIN; ECAL1 CATCOD+SORT; ECAL2 CATCOD+CODE
Fields:
  AUUID AUUID Single identifier
  CATCOD CAT Category code -> [ECA]ECA0 =[ECAL]CATCOD (EDICAT) !BSRA
  CODE EDO Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECAL]CREUSR (AUTILIS) !Other
  DOSSIER A*10 Folder
  DUPLICATE M*30 Duplicate [menu 2010: 1=Authorized,2=Not authorized]
  NUMLIN C*4 Line number
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECAL]UPDUSR (AUTILIS) !Other

## EDICATREF (ECR) - Category authorization ref.
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): ECR0 CATTYP+CATTRGTAB
Fields:
  AUTCOD1 A*20 Authorization code
  AUTCOD2 A*20 Authorization code
  AUTCOD3 A*20 Authorization code
  AUTCOD4 A*20 Authorization code
  AUTCOD5 A*20 Authorization code
  AUUID AUUID Single identifier
  CATTRGTAB ATB Triggering table -> [ATB]CODFIC =[ECR]CATTRGTAB (ATABLE) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECR]CREUSR (AUTILIS) !Other
  CTRLGRP A*3 Control group
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECR]UPDUSR (AUTILIS) !Other

## EDICPYPAR (ECP) - EDI partners by company
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDICPYPAR.htm); differs in V10 P1 (diff: ATD_EDICPYPAR.htm)
Keys (first = PK; D = duplicates allowed): ECP0 CPY+PARCOD
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[ECP]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECP]CREUSR (AUTILIS) !Other
  DUNS A*20 DUNS
  EXCEDICOD A*20 EDI code
  EXCEDISTA M*20 Paperless document exchange [menu 2000: 1=Disabled,2=Accepted,3=Closed,4=In progress,5=Rejected,6=In process]
  IDTYPE M*10 Identification type [menu 2002: 1=Fiscal code,2=Local code,3=GLN,4=DUNS,5=VAT Number,6=Free]
  PARCOD EPR EDI partner -> [EPR]EPR0 =[ECP]PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  SAGCERTIF FIC*250 Certificate
  SAGEDICOD A*12 EDI SAGE code
  SAGEDISTA M*20 Paperless document exchange [menu 2000: 1=Disabled,2=Accepted,3=Closed,4=In progress,5=Rejected,6=In process]
  SAGGEDFLG M*4 EDM [menu 1: 1=No,2=Yes]
  SAGPLTURL A*250 URL
  SAGREMFLG M*4 Rematerialization [menu 1: 1=No,2=Yes]
  SIGNATURE M*4 Signature [menu 1: 1=No,2=Yes]
  STA M*20 Status [menu 2000: 1=Disabled,2=Accepted,3=Closed,4=In progress,5=Rejected,6=In process]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECP]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDICPYPARD (ECPD) - EDI partners by company
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): ECPD0 CPY+PARCOD+LIG; ECPD1 CPY+PARCOD+SORT
Fields:
  AUUID AUUID Single identifier
  CERTIFICATE A*60 Certificate
  CPY CPY Company -> [CPY]CPY0 =[ECPD]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ECPD]CREUSR (AUTILIS) !Other
  LIG C*4 Line
  PARCOD EPR EDI partner -> [EPR]EPR0 =[ECPD]PARCOD (EDIPARTNER) !Block
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ECPD]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[ECPD]USER (AUTILIS) !Block

## EDIFCYPAR (EFP) - EDI partner by site
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDIFCYPAR.htm)
Keys (first = PK; D = duplicates allowed): EFP0 FCY+PARCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EFP]CREUSR (AUTILIS) !Other
  EXCEDICOD A*20 EDI code
  FCY FCY Site -> [FCY]FCY0 =[EFP]FCY (FACILITY) !Delete
  GLN A*20 GLN
  IDTYPE M*10 Identification type [menu 2002: 1=Fiscal code,2=Local code,3=GLN,4=DUNS,5=VAT Number,6=Free]
  PARCOD EPR EDI partner -> [EPR]EPR0 =[EFP]PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  STA M*1 Status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EFP]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIFLO (EFL) - Flow
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EFL0 FLOCOD+FLOREL
Fields:
  AUUID AUUID Single identifier
  CACHEUUID AUUID Single identifier
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CODACT ACV Activity code -> [ACV]CODACT =[EFL]CODACT (ACTIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EFL]CREUSR (AUTILIS) !Other
  FLGACT M*4 Active [menu 1: 1=No,2=Yes]
  FLOCOD EFC Flow ID
  FLODES A*50 Description
  FLOREL EFR Version
  PARCOD EPR EDI partner -> [EPR]EPR0 =PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  PTCCOD PTC Protocol
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EFL]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIFLOA (EFLA) - Attachment
Notes: activity code EDIX3; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): EFLA0 FLOCOD+FLOREL+NUMLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EFLA]CREUSR (AUTILIS) !Other
  CRUSED ARP Crystal report -> [ARP]ARP0 =[EFLA]CRUSED (AREPORT) !Block
  DESTIN AIM Destination -> [AIM]AIM0 =[EFLA]DESTIN (APRINTER) !Block
  EXCMSG M*4 Exclude message [menu 1: 1=No,2=Yes]
  FICNAM FIC*50 File name
  FICVOL AVL Volume -> [AVL]CODE =[EFLA]FICVOL (AVOLUME) !Block
  FIXNAM M*4 Fixed name [menu 1: 1=No,2=Yes]
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  GENFLG M*4 Generated [menu 1: 1=No,2=Yes]
  NUMLIN L*8 Line
  PATH A*250 Directory
  SGNFLG M*4 Signed [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EFLA]UPDUSR (AUTILIS) !Other

## EDIFLOAP (EFLAP) - Parameters
Notes: activity code EDIX3; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): EFLP0 FLOCOD+FLOREL+NUMSEQ
Fields:
  ALIAS EVB Alias
  AUUID AUUID Single identifier
  CODREP ASW Representation code -> [ASW]ASW0 =[EFLAP]CODREP (ASHW) !Delete
  CONSTANT A*20 Constant value
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EFLAP]CREUSR (AUTILIS) !Other
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  NUMSEQ L*8 Sequence number
  PARDES A*250 Description
  PARNAM A*80 Parameter
  PROPERTY A*250 Property
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EFLAP]UPDUSR (AUTILIS) !Other
  VALTYPE M*30 Value type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]

## EDIFLOD (EFLD) - Flow detail
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDIFLOD.htm); differs in V10 P1 (diff: ATD_EDIFLOD.htm)
Keys (first = PK; D = duplicates allowed): EFLD0 FLOCOD+FLOREL+NUMLIN; EFLD1 FLOCOD+FLOREL+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EFLD]CREUSR (AUTILIS) !Other
  FLGMUX M*4 Merge [menu 1: 1=No,2=Yes]
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  MSGCOD EDC Message mapping ID
  MSGDIR M*10 Direction [menu 2005: 1=Outbound,2=Inbound]
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Other
  MSGFOR M*20 Message file format [menu 2013: 1=Sequential,2=XML]
  MSGOPE M*1 Operation [menu 2025: 1=Read,2=Create]
  MSGREL EDR Version
  MSGTYP M*15 Type [menu 2024: 1=Query,2=Attachment,3=SDATA]
  NUMLIN L*8 Line
  PTCCOD PTC Protocol
  SIGNAEXT A*10 Extension
  SIGNATURE M*15 Signature [menu 2026: 1=Without Signature,2=XAdES]
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EFLD]UPDUSR (AUTILIS) !Other
  VALXML M*4 XML validation [menu 1: 1=No,2=Yes]

## EDIMSG (EMS) - Message mapping
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EMS0 MSGCOD+MSGREL
Fields:
  ABRCLA ABR Instance
  AUUID AUUID Single identifier
  CACHEUUID AUUID Single identifier
  CATCOD CAT Category code -> [ECA]ECA0 =[EMS]CATCOD (EDICAT) !BSRA
  CODACT ACV Activity code -> [ACV]CODACT =[EMS]CODACT (ACTIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EMS]CREUSR (AUTILIS) !Other
  DRTPDF FIC*120 Attachment volume
  FILPDF AFF*60 File
  MSGCOD EDC Message mapping ID
  MSGDES A*35 Description
  MSGDIR M*10 Direction [menu 2005: 1=Outbound,2=Inbound]
  MSGOPE M*1 Operation [menu 2025: 1=Read,2=Create]
  MSGREL EDR Version
  MSGTPL AOE Template -> [AOE]AOE0 =[EMS]MSGTPL (AOBJEXT) !Block
  MSGTRGTAB ATB Triggering table -> [ATB]CODFIC =[EMS]MSGTRGTAB (ATABLE) !Block
  MSGTYP M*15 Type [menu 2024: 1=Query,2=Attachment,3=SDATA]
  REPCOD ASW Representation -> [ASW]ASW0 =[EMS]REPCOD (ASHW) !Block
  RPTPDF ARP Report code -> [ARP]ARP0 =[EMS]RPTPDF (AREPORT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EMS]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIMSGA (EMSA) - Inbound authorizations
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EMSA0 MSGCOD+MSGREL+NUMLIN; EMSA1 MSGCOD+MSGREL+SORT; EMSA2 MSGCOD+MSGREL+CODE
Fields:
  ALIAS AVB Alias
  AUUID AUUID Single identifier
  CODE A*30 Code
  CODPRO AVC Property
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EMSA]CREUSR (AUTILIS) !Other
  MANDATORY M*10 Mandatory [menu 2018: 1=Optional,2=Mandatory,3=Warning]
  MSGCOD EDC Message mapping ID
  MSGREL EDR Version
  NUMLIN L*8 Line
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EMSA]UPDUSR (AUTILIS) !Other

## EDIMSGD (EMSD) - Message mapping detail
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EMSD0 MSGCOD+MSGREL+NUMLIN; EMSD1 MSGCOD+MSGREL+SORT (D)
Fields:
  ALIAS AVB Alias
  AUUID AUUID Single identifier
  CODPRO AVC Property
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EMSD]CREUSR (AUTILIS) !Other
  EXPRESSION AFF*250 Expression
  FLDTYP M*15 Type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  FLGREC AOI Indicator
  MANDATORY M*10 Mandatory [menu 2018: 1=Optional,2=Mandatory,3=Warning]
  MSGCOD EDC Message mapping ID
  MSGREL EDR Version
  NUMLIN L*8 Line
  NUMTAB AOR Transcoding -> [AOR]AOR0 =NUMTAB;1 (AOBJEXTR) !RTZ
  PROTOPATH A*250 Prototype
  SASVAR A*20 SAS variable
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EMSD]UPDUSR (AUTILIS) !Other

## EDIPARTNER (EPR) - EDI partners
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EPR0 PARCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EPR]CREUSR (AUTILIS) !Other
  FLGACT M*4 Active [menu 1: 1=No,2=Yes]
  PARCOD EPR Code -> [EPR]EPR0 =[EPR]PARCOD (EDIPARTNER) !BSRA
  PARDES A*80 Description
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  PTCCOD PTC Protocol
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EPR]UPDUSR (AUTILIS) !Other

## EDIPARTNERD (EPRD) - EDI partners
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EPRD0 PARCOD+NUMLIN; EPRD1 PARCOD+SORT; EPRD2 PARCOD+CATCOD+CATACT; EPRD3 PARCOD+CATTYP (D)
Fields:
  AUUID AUUID Single identifier
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EPRD]CREUSR (AUTILIS) !Other
  NUMLIN C*4 Line number
  PARCOD EPR Code -> [EPR]EPR0 =[EPRD]PARCOD (EDIPARTNER) !BSRA
  PTCCOD PTC Protocol
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EPRD]UPDUSR (AUTILIS) !Other

## EDIPTC (EPT) - Protocol
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EPT0 PTCCOD
Fields:
  AUUID AUUID Single identifier
  CACHEUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[EPT]CODACT (ACTIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EPT]CREUSR (AUTILIS) !Other
  FLGACT M*4 Active [menu 1: 1=No,2=Yes]
  PTCCOD PTC Protocol
  PTCDES A*50 Description
  PTCTYP M*30 Protocol type [menu 2008: 1=Emails,2=Directories]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EPT]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIPTCD (EPTD) - Protocol detail
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EPTD0 PTCCOD+NUMLIN; EPTD1 PTCCOD+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EPTD]CREUSR (AUTILIS) !Other
  NUMLIN C*4 Line number
  PTCCOD PTC Protocol
  PTCLINCOD A*20 Code
  PTCLINVAL A*250 Value
  PTCLINVALDIR AVL Value -> [AVL]CODE =[EPTD]PTCLINVALDIR (AVOLUME) !Other
  PTCLINVALTYP A*10 Data type
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EPTD]UPDUSR (AUTILIS) !Other

## EDIPTCM (EPTM) - Protocol detail
Notes: activity code EDIX3; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): EPTM0 PTCCOD+NUMLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EPTM]CREUSR (AUTILIS) !Other
  NUMLIN C*4 Line number
  PTCCOD PTC Protocol
  PTCMLINCOD A*20 Code
  PTCMLINVAL A*250 Value
  PTCMLVALTYP A*10 Data type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EPTM]UPDUSR (AUTILIS) !Other

## EDIRUN (EDR) - Process launch
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDIRUN.htm)
Keys (first = PK; D = duplicates allowed): EDR0 NUM
Fields:
  ALLFLO M*10 All flows [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDR]CREUSR (AUTILIS) !Other
  DIRECTFLG M*4 Direct [menu 1: 1=No,2=Yes]
  DUPLICATEFLG M*10 Duplicate [menu 1: 1=No,2=Yes]
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  LASRUNDAT ADATIM Execution date
  NUM C*4 Process number
  PARCOD EPR EDI partner -> [EPR]EPR0 =PARCOD (EDIPARTNER) !Block
  PARTYP M*30 EDI partner type [menu 2009: 1=Sage eFacture,2=Miscellaneous exchanges]
  RUNDES A*35 Description
  TESTFLG M*10 Test [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDR]UPDUSR (AUTILIS) !Other

## EDIRUND (EDRD) - Process launch
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EDRD0 NUM+NUMLIN; EDRD1 NUM+SORT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDRD]CREUSR (AUTILIS) !Other
  FLD A*30 Field
  FLDCODTYP A*10 Data type
  FLDNAM A*30 Field
  FLDNOLIB C*4 Local menu no.
  FLDTYPTYP M*15 Type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  FLDVAL1 A*250 Start
  FLDVAL2 A*250 End
  MANDATORY M*10 Mandatory [menu 2018: 1=Optional,2=Mandatory,3=Warning]
  NUM C*4 Process number
  NUMLIN C*4 Line number
  OPERATOR M*20 Operator [menu 2023: 1=Value range,2=Equal to,3=Greater than or equal to,4=Less than or equal to]
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDFLG M*4 Enterable [menu 1: 1=No,2=Yes]
  UPDUSR AUS User -> [AUS]CODUSR =[EDRD]UPDUSR (AUTILIS) !Other

## EDISEQFIL (ESF) - Sequential file
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESF0 MSGCOD+MSGREL+MSGFILNOR
Fields:
  ABRCLA ABR Instance
  AUUID AUUID Single identifier
  CACHEUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ESF]CODACT (ACTIV) !Block
  CODDBA M*10 File format [menu 945: 1=ascii,2=utf-8,3=ucs-2]
  COMTYP M*15(20) Component type [menu 2019: 1=File name,2=Main key,3=Merge key,4=Date,5=Time,6=Constant,7=Batch number,8=Extension]
  COMVAL A*20(20) Value
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESF]CREUSR (AUTILIS) !Other
  FILDES A*50 Description
  FLDLIM A*1 Field delimiter
  FLGMUX M*4 Merge [menu 1: 1=No,2=Yes]
  KEYALIAS EVB Key
  KEYDES A*50 Description
  KEYPROPERTY A*250 Property
  KEYPROTOPATH A*250 Path
  MSGCOD EDC Message mapping ID
  MSGDIR M*10 Direction [menu 2005: 1=Outbound,2=Inbound]
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGFOR M*20 Message file format [menu 2013: 1=Sequential,2=XML]
  MSGREL EDR Version
  OPTCHA M*15 Character set [menu 9: 1=ISO 8859,2=IBM PC,3=7 bits US,4=7 bits France,5=MacIntosh,6=HP Roman 8]
  OPTDAT C*1 Date format
  OPTMNL C*1 Local menu format
  REPCOD A*20 Representation
  SEPDEC A*1 Decimal separator
  SEPFLD A*8 Field separator
  SEPREC A*8 Record separator
  TYPFIL M*15 File type [menu 94: 1=ASCII (1),2=ASCII (2),3=Delimited,4=Fixed length,5=XML,6=Flat,7=With header]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESF]UPDUSR (AUTILIS) !Other
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDISEQFILD (ESFD) - Sequential file detail
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESFD0 MSGCOD+MSGREL+MSGFILNOR+NUMLIN; ESFD1 MSGCOD+MSGREL+MSGFILNOR+SORT (D)
Fields:
  ALIAS EVB Alias
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESFD]CREUSR (AUTILIS) !Other
  ENDREG M*4 End of record [menu 1: 1=No,2=Yes]
  EXPRESSION A*250 Property
  FILCOD A*10 File code
  FLGREC AOI Indicator
  LEVEL C*2 Level
  LNG C*3 Length
  LOC C*4 Position
  MANDATORY M*10 Mandatory [menu 2018: 1=Optional,2=Mandatory,3=Warning]
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  NUMLIN L*8 Line
  PROTOPATH A*250 Prototype
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESFD]UPDUSR (AUTILIS) !Other

## EDISEQFILF (ESFF) - Sequential files
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESFF0 MSGCOD+MSGREL+MSGFILNOR+NUMLIN; ESFF1 MSGCOD+MSGREL+MSGFILNOR+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESFF]CREUSR (AUTILIS) !Other
  DESCRIPTION A*30 Description
  FILCOD A*10 File code
  FILNAM A*250 File name
  LINKFIELD A*100 Link code
  MAINFIELD A*100 Main field
  MANDATORY M*4 Mandatory [menu 1: 1=No,2=Yes]
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  NUMLIN L*8 Line
  PARFILE A*10 Parent identifier
  PROTOLINK A*100 Link code
  PROTOMAIN A*100 Main field
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESFF]UPDUSR (AUTILIS) !Other

## EDISTO (EST) - Temp storage space
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EST0 NUMBATCH+KEYDOC
Fields:
  AUUID AUUID Single identifier
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[EST]CREUSR (AUTILIS) !Other
  EXTKEYDOC A*60 External identifier
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  KEYDOC A*60 Key
  NUMBATCH A*20 Batch no.
  PARCOD EPR EDI partner -> [EPR]EPR0 =PARCOD (EDIPARTNER) !Block
  PTCCOD PTC Protocol
  STA M*15 Status [menu 2003: 1=Pending,2=In progress,3=Completed,4=Error]
  TESTFLG M*10 Test [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[EST]UPDUSR (AUTILIS) !Other

## EDISTOC (ESTC) - Text file (clob)
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESTC0 NUMBATCH+KEYDOC+NUMLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESTC]CREUSR (AUTILIS) !Other
  KEYDOC A*60 Key
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Line
  STACKTRACE ACPLAIN*1 Error log file
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESTC]UPDUSR (AUTILIS) !Other

## EDISTOE (ESTE) - Events
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESTE0 NUMBATCH+KEYDOC+NUMLIN; ESTE1 NUMBATCH+KEYDOC+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESTE]CREUSR (AUTILIS) !Other
  ERR A*100 Action
  ERRSTA M*4 Error status [menu 1: 1=No,2=Yes]
  FLOSTP M*20 Steps [menu 2014]
  INFO A*250 Information
  KEYDOC A*60 Key
  MSGNUM M Message [menu 2017: 36 values, see local-menus.md]
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Line
  ORI M Source [menu 2022: 1=Internal,2=External]
  SEV M Severity [menu 2020: 1=Information,2=Warning,3=Error]
  SORT L*8 Sort
  TIMESTAMP ADATIM Timestamp
  TYP M*15 Type [menu 2021: 1=Functional,2=Technical,3=Transfer]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESTE]UPDUSR (AUTILIS) !Other

## EDISTOF (ESTF) - Flow detail
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESTF0 NUMBATCH+KEYDOC+FLOCOD+FLOREL+NUMLIN; ESTF1 NUMBATCH+KEYDOC+FLOCOD+FLOREL+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESTF]CREUSR (AUTILIS) !Other
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  KEYDOC A*60 Key
  MSGCOD EDC Message mapping ID
  MSGDIR M*10 Direction [menu 2005: 1=Outbound,2=Inbound]
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Other
  MSGFOR M*20 Message file format [menu 2013: 1=Sequential,2=XML]
  MSGREL EDR Version
  MSGTYP M*15 Type [menu 2024: 1=Query,2=Attachment,3=SDATA]
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Line
  PTCCOD PTC Protocol
  REPCOD A*20 Representation
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESTF]UPDUSR (AUTILIS) !Other

## EDISTOJ (ESTJ) - Error
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESTJ0 NUMBATCH+KEYDOC+NUMLIN; ESTJ1 NUMBATCH+KEYDOC+SORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESTJ]CREUSR (AUTILIS) !Other
  INSUUID AUUID Uuid
  KEYDOC A*60 Key
  MESSAGE A*250 Message
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Line
  SEVERITY A*100 Action
  SORT L*8 Sort
  TIMESTAMP ADATIM Timestamp
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESTJ]UPDUSR (AUTILIS) !Other

## EDISTOU (ESTU) - Storage
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): ESTU0 NUMBATCH+KEYDOC+NUMLIN; ESTU1 NUMBATCH+KEYDOC+SORT (D); ESTU2 NUMBATCH+KEYDOC+CODE
Fields:
  AUUID AUUID Single identifier
  CODE A*10 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESTU]CREUSR (AUTILIS) !Other
  DOCCLASS ACLA Class -> [ACLA]ACLA0 =[ESTU]DOCCLASS (ACLASSE) !Other
  DOCDES A*50 Description
  DOCKEY A*100 Key
  DOCUUID AUUID Single identifier
  KEYDOC A*60 Key
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Line
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESTU]UPDUSR (AUTILIS) !Other

## EDITMPDOC (ETC) - Documents
Notes: activity code EDIX3; differs in V9.0 P12 (diff: AT3_EDITMPDOC.htm); differs in V10 P1 (diff: ATD_EDITMPDOC.htm)
Keys (first = PK; D = duplicates allowed): ETC0 NUMBATCH+DOCID; ETC1 NUMBATCH+FLOCOD+FLOREL (D); ETC2 DOCID
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPRNUM A*50 BP code
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATTRGTAB ATB Triggering table -> [ATB]CODFIC =[ETC]CATTRGTAB (ATABLE) !BSRA
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CPY CPY Company -> [CPY]CPY0 =[ETC]CPY (COMPANY) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ETC]CREUSR (AUTILIS) !Other
  DOCDAT D Document date
  DOCID A*100 Identifier
  EXTDOCID A*100 Identifier
  FCY FCY Site -> [FCY]FCY0 =[ETC]FCY (FACILITY) !BSRA
  FLGEDIBPR C*4 BP
  FLGEDIBPRCPY C*4 BP
  FLGEDICPY C*4 Company
  FLGEDIFCY C*4 Site
  FLGMUX M*4 Merge [menu 1: 1=No,2=Yes]
  FLGMUXIMP C*4 Merge
  FLGVALIDDOC C*4 Process
  FLGVALIDFLO C*4 Valid
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  FOLDERX3 A*30 Folder
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =[ETC]MSGFILNOR (ATABDIV) !BSRA
  MSGREL EDR Version
  NUMBATCH A*20 Batch no.
  PATH A*250 Directory
  PTCCOD PTC Protocol
  REP_ID A*50 Representation
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ETC]UPDUSR (AUTILIS) !Other
  UUID_FLO A*36 Flow
  UUID_INSJSON A*36 Instance
  UUID_JSON A*36 Uuid
  UUID_MSG A*36 Message mapping
  UUID_PTC A*36 Protocol
  UUID_SEQ A*36 Sequential file

## EDITMPLOG (EDL) - Log
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EDL0 NUMBATCH+DOCID+CATTYP+SORT; EDL1 NUMBATCH (D); EDL2 DOCID (D); EDL3 NUMBATCH+DOCID+CATTYP+FLOSTP+SORT
Fields:
  AUUID AUUID Single identifier
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDL]CREUSR (AUTILIS) !Other
  DOCID A*50 Identifier
  ERR A*100 Action
  ERRCOD A*6 Error code
  ERRSTA C*4 Status
  FLOSTP C*4 Flow step
  INFO A*250 Information
  KEY1 A*50 Key
  KEY2 A*50 Key
  MSGNUM M Message [menu 2017: 36 values, see local-menus.md]
  NUMBATCH A*50 Batch no.
  SEV M Severity [menu 2020: 1=Information,2=Warning,3=Error]
  SORT L*8 Sort
  STA C*4 Status
  TIMESTAMP ADATIM Timestamp
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDL]UPDUSR (AUTILIS) !Other

## EDITRKDOC (EDK) - Documents
Notes: activity code EDIX3
Keys (first = PK; D = duplicates allowed): EDK0 DOCID+CATTYP+NUMLIN; EDK1 FLOCOD+FLOREL+CPY+FCY+BPRNUM+BPAADD (D); EDK2 DOCID+CATTYP+FLOCOD+FLOREL (D); EDK3 FLOCOD+FLOREL+DOCID (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[EDK]BPRNUM (BPARTNER) !Block
  CATACT M*20 Action [menu 2011: 1=Send,2=Receive]
  CATCOD CAT Category code -> [ECA]ECA0 =CATCOD (EDICAT) !Block
  CATTYP M*50 Category type [menu 2012: 1=Purchase invoice,2=Sales invoice,3=Purchase order,4=Sales order,5=Sales delivery]
  CNTFLODOC C*4 Counter by flow
  CPY CPY Company -> [CPY]CPY0 =[EDK]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDK]CREUSR (AUTILIS) !Other
  DOCID A*100 Identifier
  DUPLICATE M*4 Duplicate [menu 1: 1=No,2=Yes]
  DUPLICATEAUT M*4 Duplicate auth. [menu 1: 1=No,2=Yes]
  DUPLICATEERR C*4 Duplicate message
  EXTID A*100 External identifier
  FCY FCY Site -> [FCY]FCY0 =[EDK]FCY (FACILITY) !Delete
  FLGMUX M*4 Merge [menu 1: 1=No,2=Yes]
  FLGMUXIMP M*4 Merge [menu 1: 1=No,2=Yes]
  FLGUPD M*4 Updated [menu 1: 1=No,2=Yes]
  FLOCOD EFC Flow ID
  FLOREL EFR Version
  NUM C*4 Process number
  NUMBATCH A*20 Batch no.
  NUMLIN L*8 Sequence number
  PTCCOD PTC Protocol
  RUNDATE ADATIM Date
  TESTFLG M*10 Test [menu 1: 1=No,2=Yes]
  TRKSTA M*15 Status [menu 2003: 1=Pending,2=In progress,3=Completed,4=Error]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDK]UPDUSR (AUTILIS) !Other

## EDIXMLFIL (EXF) - XML file
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXF0 MSGCOD+MSGREL+MSGFILNOR
Fields:
  ABRCLA ABR Instance
  AUUID AUUID Single identifier
  CACHEUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[EXF]CODACT (ACTIV) !Block
  COMTYP M*15(20) Component type [menu 2019: 1=File name,2=Main key,3=Merge key,4=Date,5=Time,6=Constant,7=Batch number,8=Extension]
  COMVAL A*20(20) Value
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXF]CREUSR (AUTILIS) !Other
  FILDES A*50 Description
  FILEUUID AUUID Single identifier
  FLGMUX M*4 Merge [menu 1: 1=No,2=Yes]
  KEYALIAS EVB Key
  KEYDES A*50 Description
  KEYPROPERTY A*250 Property
  KEYPROTOPATH A*250 Path
  MSGCOD EDC Message mapping ID
  MSGDIR M*10 Direction [menu 2005: 1=Outbound,2=Inbound]
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGFOR M*20 Message file format [menu 2013: 1=Sequential,2=XML]
  MSGREL EDR Version
  REPCOD A*20 Representation
  TYPFIL M*15 File type [menu 94: 1=ASCII (1),2=ASCII (2),3=Delimited,4=Fixed length,5=XML,6=Flat,7=With header]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXF]UPDUSR (AUTILIS) !Other
  UUIDXMLTYP AUUID Uuid
  VALID M*4 Valid [menu 1: 1=No,2=Yes]

## EDIXMLFILD (EXFD) - XML file detail
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXFD0 MSGCOD+MSGREL+MSGFILNOR+NUMLIN; EXFD1 MSGCOD+MSGREL+MSGFILNOR+SORT (D)
Fields:
  ALIAS EVB Alias
  AUUID AUUID Single identifier
  CONDITIONPAT A*250 Condition
  CONDITIONSTR A*250 Condition
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXFD]CREUSR (AUTILIS) !Other
  DESCRIPTION A*250 Description
  EXPRESSION A*250 Property
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  NUMLIN L*8 Line
  PATHID EPH Identifier
  PATHPARENTTY A*250 Identify
  PATHREST A*250 Restriction
  PATHSTR A*250 Path
  PATHTYPE A*100 Type
  PROTOPATH A*250 Prototype
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXFD]UPDUSR (AUTILIS) !Other

## EDIXMLFILF (EXFF) - XML files
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXFF0 MSGCOD+MSGREL+MSGFILNOR+NUMLIN; EXFF1 MSGCOD+MSGREL+MSGFILNOR+SORT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXFF]CREUSR (AUTILIS) !Other
  DESCRIPTION A*30 Description
  FILNAM A*250 File name
  MANDATORY M*4 Mandatory [menu 1: 1=No,2=Yes]
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  NUMLIN L*8 Line
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXFF]UPDUSR (AUTILIS) !Other

## EDIXMLFILP (EXFP) - XML file detail
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXFP0 MSGCOD+MSGREL+MSGFILNOR+PATHID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXFP]CREUSR (AUTILIS) !Other
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  PATHCLB ACPLAIN*1 Path
  PATHID EPH Identifier
  PATHPARENTTY A*250 Identify
  PATHREST A*250 Restriction
  PATHSTR A*250 Path
  PATHTYPE A*100 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXFP]UPDUSR (AUTILIS) !Other

## EDIXMLFILXSD (EXSD) - XSD files
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXSD0 MSGCOD+MSGREL+MSGFILNOR+NUMLIN; EXSD1 MSGCOD+MSGREL+MSGFILNOR+SORT
Fields:
  AUUID AUUID Single identifier
  CODE EXD Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXSD]CREUSR (AUTILIS) !Other
  MSGCOD EDC Message mapping ID
  MSGFILNOR ADI File standard -> [ADI]CODE =2002;MSGFILNOR (ATABDIV) !Block
  MSGREL EDR Version
  NUMLIN L*8 Line
  SORT L*8 Sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXSD]UPDUSR (AUTILIS) !Other
  UUIDXSD AUUID Uuid

## EDIXSDUPL (EXU) - EDI upload XSD file
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXU0 CODE
Fields:
  AUUID AUUID Single identifier
  CODE EXD Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXU]CREUSR (AUTILIS) !Other
  FILDES A*250 Description
  FILNAM A*50 File name
  NAM A*50 Name
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXU]UPDUSR (AUTILIS) !Other
  UUIDXSD AUUID Uuid

## EDIXSDUPLFIL (EXUF) - File
Notes: activity code FAL; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EDIXSDUPLLOB (EXUL) - Lob field
Notes: activity code EDIX3; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EXUL0 CODE
Fields:
  AUUID AUUID Single identifier
  CODE EXD Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EXUL]CREUSR (AUTILIS) !Other
  TXT ACPLAIN*9 File
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EXUL]UPDUSR (AUTILIS) !Other

## EECBIDWL (EWL) - WL
Notes: activity code KPL; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): EWL0 EECNUM+BIDNUM+CREDAT
Fields:
  AUUID AUUID Single identifier
  BIDNUM BID Bank account number
  CODE A*10 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EWL]CREUSR (AUTILIS) !Other
  EECNUM A*20 EU VAT no.
  REQID A*36 Request ID
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EWL]UPDUSR (AUTILIS) !Other
  WLISTA M*4 Status [menu 1: 1=No,2=Yes]

## EMPCTR (ECT) - Current contract
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOAD (AD) - Administrative information
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCHD (CHD) - Children
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCPT (CPT) - Accounting information
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTR (HRCTR) - Contract
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRAFR (CTRAFR) - Additional Africa fields
Notes: activity code FAFPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRAUS (CTRAUS) - Additional Australia fields
Notes: activity code FAUPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRCPT (CPR) - Contract accounting information
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRFRA (CTRFRA) - Additional France fields
Notes: activity code FFRPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRMID (CTRMID) - Additional Middle east fields
Notes: activity code KMIEA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRPEN (CPN) - Position hazardous cond in cont
Notes: activity code FFRPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRPOR (CTRPO) - Contract
Notes: activity code FPAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCTRSA (CTRSA) - Additional RSA fields
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOCUM (EPC) - Totals
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOELC (ELC) - Electoral lists
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOEXM (HREXM) - Degrees
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOHAB (HAB) - Authorizations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOID (ID) - Civil status
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOIDAFR (EAF) - Additional Africa fields
Notes: activity code FAFPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOIDAUS (EAUS) - Additional Australia fields
Notes: activity code FAUPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOIDMID (EMID) - Additional Middle east fields
Notes: activity code KSA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOIDPOR (IDPOR) - Civil status
Notes: activity code FPAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOIDSA (ESA) - Additional RSA fields
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOJNT (JNT) - Spouses (>1)
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOMED (MED) - Medical examinations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOPAR (PAR) - Deferred-based
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOPOT (EPO) - Position
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLORIB (RIB) - Bank ID statement
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOSAL (SAL) - Salary gains
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOTAXREC (ETR) - Tax info
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPLOTRY (TRY) - Professional experience
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## EMPSBD (ESB) - Subordinate
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## ESCSRE (ECE) - Escalation history
Keys (first = PK; D = duplicates allowed): ECE0 ESCCOD; ECE1 SRENUM+ESCDAT (D); ECE2 SREASS+SREDET (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ESCACTNAM A*100(10) Description
  ESCACTNUM ADI(10) Action -> [ADI]CODE =455;ESCACTNUM (ATABDIV) !RTZ
  ESCCAT ADI Category -> [ADI]CODE =453;ESCCAT (ATABDIV) !RTZ
  ESCCND ADI Condition -> [ADI]CODE =454;ESCCND (ATABDIV) !RTZ
  ESCCOD VCR Sequence no.
  ESCDAT D Date escalated
  ESCHOU HM Escalation time
  ESCNAM A*100 Description
  ESCNUM VCR Code
  ESCTYP M*15 Type [menu 3028: 1=Hidden,2=Archived,3=Incremental]
  SREASS M*15 Request assignment [menu 975: 1=Dispatching,2=Employee,3=Queue,4=Commercial,5=Closed]
  SREDET VCR Assignment detail
  SRENUM SRE Service request -> [SRE]SRE0 =[ECE]SRENUM (SERREQUEST) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## EVCRESULT (EVCR) - EU VAT ID check result
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): EVCRESULT0 EVCTARGET+BPR+CODADR+EVCORIGIN
Fields:
  AUUID AUUID Single identifier
  BPAADDLIG ADL Address line
  BPR BPR BP number -> [BPR]BPR0 =[EVCR]BPR (BPARTNER) !Block
  BPRNAM NAM BP name
  CHKDAT D Date
  CODADR ADR Address code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EVCR]CREUSR (AUTILIS) !Other
  CTY CTY City
  EVCCONREQ D Confirmation
  EVCCOUNT C*4 Chronological number
  EVCORIGIN M*20 Origin [menu 2207: 1=Business partner,2=Customer / Prospect,3=Ship-to customer,4=Supplier,5=Product,6=Product-sales,7=Product-customer,8=Product-supplier,9=Sales invoicing elements,10=Purchase invoicing elements,11=Secondary representatives,12=Prospect]
  EVCQUALIFIED M*4 Qualified [menu 1: 1=No,2=Yes]
  EVCRESPONSE AC0*1 Response
  EVCSERVICE M*12 Service [menu 3685: 1=None,2=EU,3=Germany]
  EVCTARGET EEC EU VAT number
  POSCOD POS Postal code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EVCR]UPDUSR (AUTILIS) !Other

## FACTOR (FCT) - Factors
Notes: differs in V9.0 P12 (diff: AT3_FACTOR.htm)
Keys (first = PK; D = duplicates allowed): FCT0 FCTCOD; FCT1 FCTNAM (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =21;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ADDFCT A*30(3) Factor address
  AUUID AUUID Single identifier
  BANACC GAC Account -> [GAC]GAC0 =COA;BANACC (GACCOUNT) !Block
  BANBPR BPR BP code -> [BPR]BPR0 =[FCT]BANBPR (BPARTNER) !Block
  BANCPY CPY Company -> [CPY]CPY0 =[FCT]BANCPY (COMPANY) !Block
  BANCUR CUR Currency -> [TCU]TCU0 =[FCT]BANCUR (TABCUR) !Block
  BANFCY FCY Site -> [FCY]FCY0 =[FCT]BANFCY (FACILITY) !Block
  BID BID Bank account number
  COA COA Chart code -> [COA]COA0 =[FCT]COA (GCOA) !Block
  COLBPC A*10 To be deleted
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[FCT]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  FAX A*20 Fax
  FCTBAN BAN Payment bank -> [BAN]BAN0 =[FCT]FCTBAN (BANK) !Block
  FCTBPCACC A*15 To be deleted
  FCTCOD FCT Factor code -> [FCT]FCT0 =[FCT]FCTCOD (FACTOR) !Delete
  FCTCPTNUM A*15 To be deleted
  FCTNAM A*30 Factor name
  FCTQTCVCR ANM Receipt sequence no. -> [ANM]ANM0 =[FCT]FCTQTCVCR (ACODNUM) !Block
  FCTRES DCB*3.2 Reserve %
  FCTTYP M*12 Factoring type [menu 3626: 1=Standard,2=Recourse,3=No recourse]
  FILEXT A*3 File extension
  FILNAM TFB File name -> [TFB]TFB0 =FILNAM;"";1;0;"";1 (TABFILBAN) !Block
  PAB1 A*30 Paying bank 1
  PAB2 A*30 Paying bank 2
  POSCOD POS Postal code
  SALCOD A*10 Vendor code
  SAT SAT State
  TEL TEL Telephone
  TXTSBRGT A*77(6) Text
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEB A*50 Internet address

## FAMPB (PBL) - Skill group
Keys (first = PK; D = duplicates allowed): PBL0 NUM; PBL1 NUM+PAEGRPNUM; PBL2 SUT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBL]CREUSR (AUTILIS) !Other
  GRPPBLDES DCO Description
  GRPPBLDESAXX AXX Description
  NUM VCR Code
  PAEGRPNUM PBL Parent group code -> [PBL]PBL0 =[PBL]PAEGRPNUM (FAMPB) !Block
  PBLBPC BPR Customer -> [BPR]BPR0 =[PBL]PBLBPC (BPARTNER) !Delete
  SUT A*10 Shortcut
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBL]UPDUSR (AUTILIS) !Other

## FILEDIH (FEH) - EDI file structure
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## FILEDIL (FEL) - List of EDI values
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## FISCALYEAR (FIY) - Fiscal years
Keys (first = PK; D = duplicates allowed): FIY0 CPY+LEDTYP+FIYNUM; FIY1 CPY+LEDTYP (D)
Fields:
  AUUID AUUID Single identifier
  CLODAT D Closing date
  CPY CPY Company -> [CPY]CPY0 =[FIY]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  EXPNUM L*8 Export number
  FIYEND D Fiscal year end
  FIYNUM C*2 Fiscal year
  FIYSTA M*15 Fiscal year status [menu 2618: 1=Not open,2=Open,3=Closed]
  FIYSTR D Fiscal year start
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEDTYPAUT M*4 Auto ledger [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FLXJOB (FJH) - Business process
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## FLXJOBRSP (FJR) - Workflow - Managers
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## FORCTR (FOC) - Arrival document formula
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## FRECST (FCS) - Cost
Keys (first = PK; D = duplicates allowed): FCS0 FCSCOD
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GCACCUR;ACCCOD;[V]GSUPCLE (GACCCODE) !Block act:CPT
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Creation date
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[FCS]DIE (GDIE) !Block act:ANA
  DIRCLCMOD M*25 Calculation mode [menu 2089: 1=Percentage per net price,2=Fixed amount,3=Amount per unit,4=Amount by fixed bracket,5=Schedule,6=Weighted amount,7=Formula]
  DIRFLG M*4 Product [menu 1: 1=No,2=Yes]
  DOCCHGTYP M*4 Doc rate type [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FCSCOD VCR Cost
  FCSNAT M*40 Cost nature [menu 2276: 1=Packaging,2=Loading,3=Pre-transport,4=Export customs formality,5=Main transport loading,6=Main transport,7=Main transport unloading,8=Import customs formalities,9=Post-transport,10=Unloading,11=Insurance,12=Others]
  HGHBKT M*4 Higher fixed bracket [menu 1: 1=No,2=Yes]
  INVFLG M*4 Billable [menu 1: 1=No,2=Yes]
  LIMTYP M*25 Schedule [menu 2094: 1=Per unit,2=Amount]
  NODIRBRD M*25 Breakdown [menu 2090: 1=No,2=Net amount pro rata,3=Net weight pro rata,4=Gross weight pro rata,5=Volume pro rata,6=Cost amount pro rata]
  STKVLT M*4 Stock valuation [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FRTCLS (FRT) - Freight class
Keys (first = PK; D = duplicates allowed): FRT0 FRTCLS+LEG; FRT1 LEG+FRTCLS
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FRT]CREUSR (AUTILIS) !Other
  DESAXX AXX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FRTCLS FRT Freight class -> [FRT]FRT0 =FRTCLS;LEG (FRTCLS) !Delete
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SHOAXX AX1 Short description
  SOC AGF Group -> [AGF]AGF0 =[FRT]SOC (AGRPFCY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FRT]UPDUSR (AUTILIS) !Other

## FRTCOMCOD (FCC) - Freight commodity code
Keys (first = PK; D = duplicates allowed): FCC0 COMTYP+COMCOD; FCC1 COMCOD+COMTYP; FCC3 COMCOD (D)
Fields:
  AUUID AUUID Single identifier
  COMCOD FCC Commodity code -> [FCC]FCC0 =[FCC]COMCOD (FRTCOMCOD) !BSRA
  COMTYP M*15 Commodity type [menu 2084: 1=NMFC number,2=HS code]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FCC]CREUSR (AUTILIS) !Block
  DESAXX AXX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  SHOAXX AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FCC]UPDUSR (AUTILIS) !Block

## GACCAUZ (GCA) - Compatible accounts
Notes: activity code KRU
Keys (first = PK; D = duplicates allowed): GCA0 COA+ACCDEB+ACCCDT
Fields:
  ACCCDT GAC Credited account -> [GAC]GAC0 =COA;ACCCDT (GACCOUNT) !Block
  ACCDEB GAC Debited account -> [GAC]GAC0 =COA;ACCDEB (GACCOUNT) !Block
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[GCA]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GCA]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GCA]UPDUSR (AUTILIS) !Other

## GACCCLS (CLS) - Account classes
Keys (first = PK; D = duplicates allowed): CLS0 LEG+CLSCOD
Fields:
  AUUID AUUID Single identifier
  CLSCOD CLA Code -> [CLS]CLS0 =[CLS]CLSCOD (GACCCLS) !BSRA
  CLSNAM A*50 Description
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CLS]CREUSR (AUTILIS) !Other
  DEFSNS M*15 Default sign [menu 610: 1=Debit,2=Credit,3=Unspecified]
  DESTRA AX3 Description
  ERA M*4 RTZ [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SNSANA M*15 Analytical sign [menu 2664: 1=Expense,2=Revenue]
  TYP M*15 Type [menu 690: 1=Normal,2=Off-balance-sheet,3=Unused]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CLS]UPDUSR (AUTILIS) !Other

## GACCCODE (CAC) - Accounting codes
Keys (first = PK; D = duplicates allowed): CAC0 TYP+ACCCOD+COA; CAC1 TYP+ACCCOD (D); CAC2 COA+TYP+ACCCOD
Fields:
  ACC A*20(99) General accounts
  ACCCOD CAC Accounting code -> [CAC]CAC0 =TYP;ACCCOD;[V]GSUPCLE (GACCCODE) !Delete
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[CAC]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  SHOTRA AX1 Short description
  TYP M*15 Code type [menu 602: 26 values, see local-menus.md]
  TYPCAR A*4 Code type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GACCCODLIG (CCL) - Accounting code lines
Notes: differs in V9.0 P12 (diff: AT3_GACCCODLIG.htm)
Keys (first = PK; D = duplicates allowed): CCL0 TYP+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CCL]CREUSR (AUTILIS) !Other
  NUMLIG C*2 Line no.
  OBL M*4 Mandatory [menu 1: 1=No,2=Yes]
  OTHPPU M*4 Local menu [menu 1: 1=No,2=Yes]
  TXT C*4 Text
  TYP M*15 Accounting code type [menu 602: 26 values, see local-menus.md]
  TYPCPT M*15 Account type [menu 604: 1=Account,2=Modifier,3=Control]
  TYPDES M*15 Description [menu 602: 26 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CCL]UPDUSR (AUTILIS) !Other

## GACCDEF (GCF) - Default accounts
Keys (first = PK; D = duplicates allowed): GCF0 COAORI+COADEN+COASTR
Fields:
  ACC GAC Account -> [GAC]GAC0 =COADEN;ACC (GACCOUNT) !Delete
  AUUID AUUID Single identifier
  COADEN COA Destination COA -> [COA]COA0 =COADEN (GCOA) !Delete
  COAORI COA Source acct plan -> [COA]COA0 =COAORI (GCOA) !Delete
  COASTR A*10 Account root
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GCF]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GCF]UPDUSR (AUTILIS) !Other

## GACCDIM (GCD) - Default dimension types
Keys (first = PK; D = duplicates allowed): GCD0 COA+LIN
Fields:
  ACCSTR A*15 Account root
  AUUID AUUID Single identifier
  CCE CCE Default dimension -> [CCE]CCE0 =DIE;CCE (CACCE) !Block
  COA COA Chart code -> [COA]COA0 =[GCD]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GCD]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type -> [DIE]DIE0 =[GCD]DIE (GDIE) !Block
  LIN C*3 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GCD]UPDUSR (AUTILIS) !Other

## GACCDUDATE (DUD) - Open items
Keys (first = PK; D = duplicates allowed): DUD0 TYP+NUM+LIG+DUDLIG; DUD1 ACCNUM+DUDLIG; DUD2 SOINUM+ACCNUM+DUDLIG; DUD3 FLGCLE+FCY+BPRPAY+DUDDAT (D); DUD4 BPR+SOINUM+ACCNUM+DUDLIG; DUD5 BPRPAY+SOINUM+ACCNUM+DUDLIG; DUD6 FLGCLE+ACCNUM+DUDLIG; DUD7 BPRPAY+BPR+NUMDUD; DUD8 NUMDUD; DUD9 BPR+BPAPAY+NUMDUD
Fields:
  ACCNUM L*8 Internal number
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ref. amt. curr.
  AUUID AUUID Single identifier
  BPAPAY ADR Business partner address
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[DUD]BPR (BPARTNER) !Block
  BPRFCT FCT Factor -> [FCT]FCT0 =[DUD]BPRFCT (FACTOR) !Block act:FCT
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[DUD]BPRPAY (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CPY CPY Company -> [CPY]CPY0 =[DUD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[DUD]CUR (TABCUR) !Block
  DATFUP D Reminder date
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DINAMT MD1 Prepayment deducted
  DPTCOD ADI Dispute code -> [ADI]CODE =315;DPTCOD (ATABDIV) !Block
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  DUDSTA C*1 Status
  EXPSENDAT D Expected issue date
  FCTVCR VCR Receipt act:FCT
  FCY FCY Site -> [FCY]FCY0 =[DUD]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGCLE C*1 Closed
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  IBDAMT MD1 Prepayment to deduct
  LEVFUP C*2 Reminder level
  LIG C*3 Line number
  NUM VCR Document no.
  NUMDUD A*15 Unique number
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAMTYP M*15 Payment type [menu 292: 1=Open item,2=Prepayment,3=Holdback]
  PAYCUR MD1 Paid
  PAYDAT D Payment date
  PAYLOC MD1 Paid ref. currency
  PER C*2 Period
  SAC SAC Control
  SENDAT D Issue date
  SENINS M*4 Prepayment issued [menu 1: 1=No,2=Yes]
  SNS C*2 Sign
  SOI M*4 Statement [menu 1: 1=No,2=Yes]
  SOINUM VCR Statement number
  TMPCUR MD1 Provisional payment
  TMPLOC MD1 Provisional payment
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPDUD M*15 Type of open item [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DUD]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## GACCGRUPYM (GRY) - Account groups
Keys (first = PK; D = duplicates allowed): GRY0 PYM+GRU+LIN; GRY1 PYM+LEV+GRU+LIN; GRY2 PYM+SBBGRU (D); GRY4 PYM+GRU (D); GRY5 PYM+ACC (D)
Fields:
  ACC A*15 Account
  AUUID AUUID Single identifier
  BUDTRK M*4 Budget tracking [menu 1: 1=No,2=Yes]
  CLSCOD CLA Classification -> [CLS]CLS0 ="";CLSCOD (GACCCLS) !Other
  COA COA Chart of accounts -> [COA]COA0 =[GRY]COA (GCOA) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DEFVAL MD1 Default value
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  GRU GRY Group code -> [GRY]GRY0 =PYM;GRU;1 (GACCGRUPYM) !Delete
  LEV C*2 Definition level
  LIN C*2 Line number
  PRNROW C*4 Print row
  PYM GYM Pyramid code -> [GYM]GYM0 =[GRY]PYM (GACCPYM) !Delete
  SBBGRU GRY Subgroup -> [GRY]GRY0 =PYM;SBBGRU;1 (GACCGRUPYM) !Delete
  SHOTRA AX1 Short description
  TIMDSP DTP Temp distribution -> [DTP]DTP0 =[GRY]TIMDSP (CADISTMP) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[GRY]UOM (TABUNIT) !Block
  UOMDAC M*4 Nonfinancial unit entry [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GACCOUNT (GAC) - Accounts
Notes: differs in V9.0 P12 (diff: AT3_GACCOUNT.htm); differs in V10 P1 (diff: ATD_GACCOUNT.htm)
Keys (first = PK; D = duplicates allowed): GAC0 COA+ACC; GAC1 COA+ACCSHO (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCSHO SAC Short code
  ACS ACS Access code -> [ACS]ACS0 =[GAC]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  AUZ ADI Restriction code -> [ADI]CODE =321;AUZ (ATABDIV) !Block
  AUZBPR M*4(10) BP authorization [menu 1: 1=No,2=Yes]
  BIDNUM BID Dft. bank details
  BPAADD ADR Default address
  BUDTRK M*4 Budget tracking [menu 1: 1=No,2=Yes]
  CCEDEF CCE Default dimension -> [CCE]CCE0 =DIE(indice);CCEDEF(indice) (CACCE) !Block act:ANA
  CEN M*4 Summary reporting [menu 1: 1=No,2=Yes]
  CLSCOD CLA Classification -> [CLS]CLS0 ="";CLSCOD (GACCCLS) !Other
  CNVACC1 GAC Debit balance decr. -> [GAC]GAC0 =COA;CNVACC1 (GACCOUNT) !Block
  CNVACC10 GAC Cred. rnd. variance -> [GAC]GAC0 =COA;CNVACC10 (GACCOUNT) !Block
  CNVACC2 GAC Debit balance incr. -> [GAC]GAC0 =COA;CNVACC2 (GACCOUNT) !Block
  CNVACC3 GAC Credit balance decr. -> [GAC]GAC0 =COA;CNVACC3 (GACCOUNT) !Block
  CNVACC4 GAC Credit balance incr. -> [GAC]GAC0 =COA;CNVACC4 (GACCOUNT) !Block
  CNVACC5 GAC Exchange gain -> [GAC]GAC0 =COA;CNVACC5 (GACCOUNT) !Block
  CNVACC6 GAC Exchange loss -> [GAC]GAC0 =COA;CNVACC6 (GACCOUNT) !Block
  CNVACC7 GAC Rnd. gain matching -> [GAC]GAC0 =COA;CNVACC7 (GACCOUNT) !Block
  CNVACC8 GAC Rnd. loss matching -> [GAC]GAC0 =COA;CNVACC8 (GACCOUNT) !Block
  CNVACC9 GAC Debtor rnd. variance -> [GAC]GAC0 =COA;CNVACC9 (GACCOUNT) !Block
  COA COA Chart code -> [COA]COA0 =[GAC]COA (GCOA) !Block
  COANBR C*2 Plan no.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CSLBPRACE M*4 Entry partner [menu 1: 1=No,2=Yes] act:PRCSL
  CSLCDT A*10 Consolidation act:CSL
  CSLDEB A*10 Consolidation act:CSL
  CSLFLG C*4 Conso analysis act:CSL
  CSLFLGBPR M*15 Partner [menu 2637: 1=Not entered,2=Optional,3=Mandatory] act:PRCSL
  CSLFLGFLW M*15 Flow management [menu 2637: 1=Not entered,2=Optional,3=Mandatory] act:CSL1
  CUR CUR Currency -> [TCU]TCU0 =[GAC]CUR (TABCUR) !Block
  DACDIENBR C*2 No. of dimensions entered
  DAS M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  DASTYP M*25 DAS2 nature [menu 615: 1=Fees and vacations,2=Commissions,3=Brokerages,4=Rebates,5=Attendance tokens,6=Royalties,7=Inventor rights,8=Other payments,9=Indemnities and reimbursements,10=Perquisites,11=Withholding tax on income,12=Net tax on royalties] act:DAS
  DEFACC GAC Default account -> [GAC]GAC0 =OTHCOA(indice);DEFACC(indice) (GACCOUNT) !RTZ act:NBCOA
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[GAC]DIE (GDIE) !Block act:ANA
  DIF M*15 Assessment method [menu 3666: 1=None,2=By journal entry,3=By account balance]
  DIFFLG M*4 Automatic variances [menu 1: 1=No,2=Yes]
  DSP DSP Key -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ESDTRK M*4 Service provisions [menu 1: 1=No,2=Yes] act:ESD
  EXPNUM L*8 Export number
  FCY CFY Company/site
  FLG281 M*4 281.5 account [menu 1: 1=No,2=Yes] act:BE281
  FLGABL M*4 Fixed asset tracking [menu 1: 1=No,2=Yes] act:FAS
  FLGDEP M*4 Discnt/charges [menu 1: 1=No,2=Yes] act:KDE
  FLGEXPCRE M*4 Expense creation [menu 1: 1=No,2=Yes] act:FAS
  FLGUOM M*4 Unit of work flag [menu 1: 1=No,2=Yes]
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  FLOCDT ADI Flow if credit -> [ADI]CODE =324;FLOCDT (ATABDIV) !Block act:CSL1
  FLODEB ADI Flow if debit -> [ADI]CODE =324;FLODEB (ATABDIV) !Block act:CSL1
  FRWCUR M*4 Carryforwards [menu 1: 1=No,2=Yes]
  GACACN M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:FAS
  GACPVS GAC Provision nature -> [GAC]GAC0 =COA;ACC (GACCOUNT) !RTZ act:KIT
  LOSGAIGNR M*4 Profit and loss [menu 1: 1=No,2=Yes]
  LVATYP M*15 LVA management [menu 3297: 1=None,2=LVA,3=Pool] act:FAS
  MTC M*4 Matchable [menu 1: 1=No,2=Yes]
  OBYIPT M*4 Mandatory allocation [menu 1: 1=No,2=Yes] act:NBCOA
  OTHCOA COA Other - CoA -> [COA]COA0 =[GAC]OTHCOA (GCOA) !Block act:NBCOA
  RITTYP M*15 Charge type [menu 953: 1=Exempt,2=Benefits,3=Charges,4=Commission,5=INPS,6=VAT,7=Other] act:KIT
  RPTCODCDT A*10(10) Credit report codes
  RPTCODDEB A*10(10) Debit report codes
  SAC M*4 Control [menu 1: 1=No,2=Yes]
  SCRACC A*15 Account screening act:NBCOA
  SHOTRA AX1 Short description
  SNSBLC M*15 Balance sign [menu 610: 1=Debit,2=Credit,3=Unspecified]
  SNSDEF M*15 Default sign [menu 610: 1=Debit,2=Credit,3=Unspecified]
  SUBACC GAC Recurring account -> [GAC]GAC0 =COA;SUBACC (GACCOUNT) !RTZ
  SUBBPR BPR Recurring BP -> [BPR]BPR0 =[GAC]SUBBPR (BPARTNER) !Block
  TIMDSP DTP Temp distribution -> [DTP]DTP0 =[GAC]TIMDSP (CADISTMP) !Block
  TYP281 M*8 281.5 category [menu 3623: 1=Commission brokerage rebate,2=Fees or sessional payments,3=Benefits in kind,4=Expenses incurred on behalf of the beneficiary] act:BE281
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  TYPRATFLG M*4 Rate type mgmt. [menu 1: 1=No,2=Yes]
  TYPVATCTL M*15 Tax code control [menu 3684: 1=Inactive,2=Authorization,3=Restriction]
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[GAC]UOM (TABUNIT) !Block
  UPDBLC M*15 Balance update [menu 679: 1=No,2=Customer,3=Supplier]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VALUOM MD4 Default value
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VLYEND D Validity end date
  VLYSTR D Validity start date

## GACCOUNTA (GAA) - Accounts (additional table)
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GAA0 COA+ACC
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[GAA]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VATCTL VAT(99) Tax codes -> [TVT]TVT0 =VATCTL(indice);[V]GSUPCLE (TABVAT) !Block

## GACCPYM (GYM) - Account pyramids
Keys (first = PK; D = duplicates allowed): GYM0 PYM; GYM1 COA+PYM
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GYM]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[GYM]COA (GCOA) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  PYM GYM Pyramid code -> [GYM]GYM0 =[GYM]PYM (GACCPYM) !Delete
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GACCTMP (HAT) - Accounting entries
Keys (first = PK; D = duplicates allowed): HAT0 TYP+NUM; HAT1 NUMPCE (D)
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  BANCIB ADI Interbank code -> [ADI]CODE =306;BANCIB (ATABDIV) !Block
  BANDAT D Bank date act:KIT
  BOLLATO VCR Bollato sequence number act:KIT
  BPRDATVCR D Source document date
  BPRVCR A*20 Original document
  CAT M*15 Category [menu 618: 1=Actual,2=Active simulation,3=Inactive simulation,4=Off-balance-sheet,5=Template]
  CPY CPY Company -> [CPY]CPY0 =[HAT]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[HAT]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[HAT]CURLED (TABCUR) !Block
  DACDIA A*5 Transaction
  DESVCR DES Description
  DUDDAT D Due date
  ENTDAT D Entry date
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[HAT]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLG C*3 Valid flag
  FLGDAS M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGGEN M*4 Auto generation [menu 1: 1=No,2=Yes]
  FLGPAZ M*4 Pay approval [menu 1: 1=No,2=Yes]
  FLGREP M*4 Carryforward [menu 1: 1=No,2=Yes]
  FNLPSTDAT D Final date
  FNLPSTNUM VCR(10) Final number
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LED LED(10) Ledger -> [LED]LED0 =[HAT]LED (GLED) !Block
  NUM VCR Document no.
  NUMDCL L*8 Declaration number
  NUMPCE L*8 Chronological number
  ORIGIN M*15 Source [menu 2801: 1=Direct entry,2=Automatic loading,3=Import]
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  PER C*2 Period
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  REF REF Reference
  REFINT A*25 Internal reference
  REFSIM A*25 Simulation reference
  RVS M*15 Reversal [menu 619: 1=No,2=Yes,3=Reversed]
  RVSDAT D Reversal date
  RVSORINUM VCR Original number
  RVSORITYP GTE Source type -> [GTE]GTE0 =RVSORITYP;[V]GSUPCLE (GTYPACCENT) !Block
  STA M*15 Status [menu 617: 1=Temporary,2=Final]
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPDUD M*15 Type of open item [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VALDAT D Value date

## GACCTMPA (AAT) - Analytical accounting line
Keys (first = PK; D = duplicates allowed): AAT0 TYP+NUM+LIN+LEDTYP+ANALIN
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM L*8 Unique number
  ACCNUMDOE UNQ Counterpart number act:KRU
  AMTCUR MD1 Entry amount
  AMTLED MD1 Ledger amount
  ANALIN C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA Chart code -> [COA]COA0 =[AAT]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[AAT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AAT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[AAT]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[AAT]CURLED (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[AAT]DIE (GDIE) !Block act:ANA
  FCYLIN FCY Site -> [FCY]FCY0 =[AAT]FCYLIN (FACILITY) !Block
  IDTLIN A*5 Identifier
  LED LED Ledger -> [LED]LED0 =[AAT]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  SNS C*2 Sign
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[AAT]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AAT]UPDUSR (AUTILIS) !Other

## GACCTMPD (DAT) - Accounting entry lines
Notes: differs in V9.0 P12 (diff: AT3_GACCTMPD.htm); differs in V10 P1 (diff: ATD_GACCTMPD.htm)
Keys (first = PK; D = duplicates allowed): DAT0 TYP+NUM+LIN+LEDTYP; DAT1 ACCNUM; DAT2 CODAUTACE+LEDTYP+CRIMTC+ACCNUM; DAT3 TYP+NUM+IDTLIN+LEDTYP+LIN
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM L*8 Internal number
  ACCNUMDOE UNQ Counterpart number act:KRU
  ACCNUMORI L*8 Source number
  AMTCUR MD1 Entry amount
  AMTFLG M*4 Forced amount [menu 1: 1=No,2=Yes]
  AMTLED MD1 Ledger amount
  AMTLED1 MD1 Forced amount
  AMTVAT MD1 Declared tax
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DAT]BPR (BPARTNER) !Block
  CHK A*5 Reconciliation
  CHKDAT D Reconciliation date
  CHRNUM VCR Chronological number
  COA COA Chart code -> [COA]COA0 =[DAT]COA (GCOA) !Delete
  CODAUTACE A*10 Auto journal code
  CPY CPY Company -> [CPY]CPY0 =[DAT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DAT]CREUSR (AUTILIS) !Other
  CRIMTC A*80 Matching criteria
  CSLBPR BPR Partner -> [BPR]BPR0 =[DAT]CSLBPR (BPARTNER) !Block act:PRCSL
  CSLCOD A*10 Partner act:CSL
  CSLFLO ADI Flow -> [ADI]CODE =324;CSLFLO (ATABDIV) !Block act:CSL1
  CUR CUR Currency -> [TCU]TCU0 =[DAT]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[DAT]CURLED (TABCUR) !Block
  DES DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[DAT]FCYLIN (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGMTC C*1 Flag
  FREREF REF Free reference
  IDTLIN A*5 Identifier
  INDEDVAT MD1 Non-deductible tax act:KIT
  LED LED Ledger -> [LED]LED0 =[DAT]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  MRK A*20 Marking
  MTC A*5 Matching
  MTCDAT D Matching date
  MTCDATMAX D Maximum group date
  MTCDATMIN D Minimum group date
  NUM VCR Document no.
  OFFACC A*15 Offset
  OLDLIG C*3 Line number
  PER C*2 Period
  QTY QTY Quantity
  REFINTLIN A*25 Internal reference
  SAC SAC Control
  SNS C*2 Sign
  STT1 ADI Statistics -> [ADI]CODE =351;STT1 (ATABDIV) !Block
  STT2 ADI Statistics -> [ADI]CODE =352;STT2 (ATABDIV) !Block
  STT3 ADI Statistics -> [ADI]CODE =353;STT3 (ATABDIV) !Block
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Block act:KDE
  TAX3 VAT Tax 3 -> [TVT]TVT0 =TAX3;[V]GSUPCLE (TABVAT) !Block act:KDE
  TRCLIG C*4 Line number
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[DAT]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DAT]UPDUSR (AUTILIS) !Other
  VATDEDRAT DCB*3.6 Deductib pro rata
  VATRAT DCB*3.6 Applied VAT rate

## GACM (GCM) - Account core model
Keys (first = PK; D = duplicates allowed): GCM0 GCM
Fields:
  ANALEDTYP M*10 Main analytical ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  AUUID AUUID Single identifier
  CFMAUT M*15(10) Auto ledger [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CTLTYP A*5(10) Control type
  CUR CUR(10) Management currency -> [TCU]TCU0 =[GCM]CUR (TABCUR) !Block
  DACRAT M*3(10) Rate entry [menu 2645: 1=Multiplier,2=Divisor,3=Both]
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DOELED M*4(10) Double entry [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FLGIAS M*4 IAS management [menu 1: 1=No,2=Yes] act:IAS
  FLGVCRRAT M*15(10) Doc rate type [menu 1: 1=No,2=Yes]
  GCM GCM Account core model -> [GCM]GCM0 =[GCM]GCM (GACM) !Delete
  GENLEDTYP M*10 Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  IASLEDTYP M*10 Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency] act:IAS
  LED LED(10) Ledger -> [LED]LED0 =[GCM]LED (GLED) !Block
  LED1 LED(10) Ledger 1 -> [LED]LED0 =[GCM]LED1 (GLED) !Block
  LED2 LED(10) Ledger 2 -> [LED]LED0 =[GCM]LED2 (GLED) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBRCTL C*2 No. of controls
  ORILEDTYP M*10(10) Source general ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  RNDOPTBAL M*15(10) Balancing option [menu 2648: 1=Allocation,2=Rounding variance]
  SHOTRA AX1 Short description
  TYPRAT M*15(10) Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GAUTACE (GAU) - Automatic journals
Keys (first = PK; D = duplicates allowed): GAU0 COD
Fields:
  ACTAFTVCR A*10 End item action
  ACTLEG ADI(99) Active legislations -> [ADI]CODE =909;ACTLEG(indice) (ATABDIV) !Block
  ACTLIK A*10 Action
  AUUID AUUID Single identifier
  COD GAU Entry code -> [GAU]GAU0 =[GAU]COD (GAUTACE) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[GAU]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATFLG M*4 First date [menu 1: 1=No,2=Yes]
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  FORCND AFR*120(2) Condition
  FORCND2 AFR*120 Condition
  GRPFLG M*15 Grouping [menu 669: 1=1 Journal per line,2=Grouped journal]
  JOU M*15 Journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  KEYTBL A*10 Key
  LIKFLD A*15(10) Linked fields
  LIKTBL ATB(10) Linked tables -> [ATB]CODFIC =[GAU]LIKTBL (ATABLE) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRLEG C*2 Active legislations
  NBRTBL C*2 Number of tables
  NEGAMT M*4 Negative amounts [menu 1: 1=No,2=Yes]
  PRGAFTVCR A*10 Program
  PRGLIK A*10 Program
  REIFLD A*10 Field code
  REITBL ATB Repetitive table -> [ATB]CODFIC =[GAU]REITBL (ATABLE) !Block
  SHOTRA AX1 Short description
  TBL ATB Table -> [ATB]CODFIC =[GAU]TBL (ATABLE) !Block
  TRCACT ACT Action -> [ACT]ACTION =[GAU]TRCACT (ACTION) !Block
  TRCCODPAR AAR(20) Parameter code -> [AAR]CODPAR =[GAU]TRCCODPAR (ACTCODPAR) !Block
  TRCFLG M*4 Traceability [menu 1: 1=No,2=Yes]
  TRCKEY ANX Index
  TRCTBL ATB Table -> [ATB]CODFIC =[GAU]TRCTBL (ATABLE) !Block
  TRCVALPAR A*30(20) Parameter value
  TYP M*15 Type [menu 665: 1=General,2=Payments]
  TYPVCR M*20 Entry reference [menu 2626: 1=Main account,2=Account journal - business partner,3=Bank journal > account,4=Treasury currency MO,5=Currency MO,6=Business partner MO,7=Account transfer,8=Discounted drafts,9=Draft transfer,10=Tax stamp]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GAUTACED (GAD) - Automatic journals (lines)
Keys (first = PK; D = duplicates allowed): GAD0 COD+LINNUM
Fields:
  ACCCND AFR*100(10) Condition
  ACCKEY AFR*80(10) Identification key
  ACCNUM C*2(10) Index
  ACTAFTLIK A*10 Action
  ACTAFTLIN A*10 Action
  ACTBEFLIN A*10 Action
  ACTLEG ADI(99) Active legislations -> [ADI]CODE =909;ACTLEG(indice) (ATABDIV) !Block
  AUUID AUUID Single identifier
  CCEDEF CDE Default dimensions -> [CDE]CDE0 =CCEDEF;[V]GSUPCLE (CACCEDEF) !Block
  COD GAU Code -> [GAU]GAU0 =[GAD]COD (GAUTACE) !Delete
  CPALIN C*4 Double entry act:KRU
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GAD]CREUSR (AUTILIS) !Other
  DEBCDT M*4 Debit-credit compensation [menu 1: 1=No,2=Yes]
  DES DES Description
  DESTRA AX3 Description
  DETCND AFR*80(10) Condition
  FLGDUD M*4 Open item management [menu 1: 1=No,2=Yes]
  FLGMTC M*4 Matching flag [menu 1: 1=No,2=Yes]
  FORCND AFR*200(4) Condition
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIKFLD A*15(5) Linked fields
  LIKTBL ATB(5) Linked tables -> [ATB]CODFIC =[GAD]LIKTBL (ATABLE) !Block
  LIKTBL2 A*200 Link expression
  LINGRP C*4 Group of lines
  LINNUM C*4 Line number
  LINNUMCAR A*4 Line number
  LINTBL1 ATB Table -> [ATB]CODFIC =[GAD]LINTBL1 (ATABLE) !Block
  LINTBL2 ATB Table 2 -> [ATB]CODFIC =[GAD]LINTBL2 (ATABLE) !Block
  LINTYP M*15 Line type [menu 625: 1=Unique,2=Repetitive,3=Linked table]
  NBRLED C*2 No. of ledgers
  NBRLEG C*2 Active legislations
  NBRTBL C*2 Number of tables
  NBRTYP C*2 Number
  PRGAFTLIK A*10 Program
  PRGAFTLIN A*10 Program
  PRGBEFLIN A*10 Program
  TRCFLG M*4 Traceability [menu 1: 1=No,2=Yes]
  TYPACCCOD M*15(10) Accounting code [menu 602: 26 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GAD]UPDUSR (AUTILIS) !Other

## GAUTACEF (GAG) - Automatic journal formulas
Keys (first = PK; D = duplicates allowed): GAG0 COD+LINNUM+FLD
Fields:
  AUUID AUUID Single identifier
  COD GAU Code -> [GAU]GAU0 =[GAG]COD (GAUTACE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GAG]CREUSR (AUTILIS) !Other
  FLD AVA Field
  FORCLC AFR*250 Formulas
  LINNUM C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GAG]UPDUSR (AUTILIS) !Other

## GAUTRCTMP (GTT) - Temporary traceability table
Keys (first = PK; D = duplicates allowed): GTT0 VCRNUM+LIN+LINCODACE+NUMORD; GTT1 CODACE+VCRNUM+UIDUSR+LIN+SUMKEY+NUMORD; GTT2 UIDUSR (D)
Fields:
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  CODACE GAU Entry code -> [GAU]GAU0 =[GTT]CODACE (GAUTACE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GTT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[GTT]CUR (TABCUR) !Other
  KEY1 A*20 Key
  KEY10 A*20 Key
  KEY11 A*20 Key
  KEY12 A*20 Key
  KEY13 A*20 Key
  KEY2 A*20 Key
  KEY3 A*20 Key
  KEY4 A*20 Key
  KEY5 A*20 Key
  KEY6 A*20 Key
  KEY7 A*20 Key
  KEY8 A*20 Key
  KEY9 A*20 Key
  LIN C*3 Line number
  LINCODACE C*4 Line number
  NUMORD L*8 Order no.
  SNS C*2 Sign
  SUMKEY A*200 Sum
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GTT]UPDUSR (AUTILIS) !Other
  VCRNUM C*2 Document no.

## GAUTRCVCR (GAT) - Automatic journal traceability
Notes: differs in V9.0 P12 (diff: AT3_GAUTRCVCR.htm); differs in V10 P1 (diff: ATD_GAUTRCVCR.htm)
Keys (first = PK; D = duplicates allowed): GAT0 ACCNUM+NUMORD; GAT1 VCRTYP+VCRNUM (D); GAT2 ACCNUM (D)
Fields:
  ACCNUM UNQ Unique number
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GAT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[GAT]CUR (TABCUR) !Other
  GAU GAU Automatic journal -> [GAU]GAU0 =[GAT]GAU (GAUTACE) !Other
  IDX ANX Index
  KEY1 A*20 Key
  KEY10 A*20 Key
  KEY11 A*20 Key
  KEY12 A*20 Key
  KEY13 A*20 Key
  KEY2 A*20 Key
  KEY3 A*20 Key
  KEY4 A*20 Key
  KEY5 A*20 Key
  KEY6 A*20 Key
  KEY7 A*20 Key
  KEY8 A*20 Key
  KEY9 A*20 Key
  LIK A*250 Link
  NUMORD L*8 Order no.
  SNS C*2 Sign
  TBL ATB Table -> [ATB]CODFIC =[GAT]TBL (ATABLE) !Other
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GAT]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Other

## GCACCOA (GCO) - Acct. code entry transactions
Keys (first = PK; D = duplicates allowed): GCO0 COD
Fields:
  AUUID AUUID Single identifier
  COA COA(9) Chart of accounts -> [COA]COA0 =[GCO]COA (GCOA) !Block
  COD GCO Transaction code -> [GCO]GCO0 =[GCO]COD (GCACCOA) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GCO]CREUSR (AUTILIS) !Other
  DESTRA AX3 Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBRCOA C*1 No. charts of accounts
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GCO]UPDUSR (AUTILIS) !Other

## GCCEGRUPYM (CRY) - Group pyramid analysis
Keys (first = PK; D = duplicates allowed): CRY0 PYM+GRU+LIN; CRY1 PYM+LEV+GRU+LIN; CRY2 PYM+SBBGRU (D); CRY4 PYM+GRU (D); CRY5 PYM+CCE (D)
Fields:
  AUUID AUUID Single identifier
  BUDTRK M*4 Budget tracking [menu 1: 1=No,2=Yes]
  CCE A*15 Dimension
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  GRU CYR Group -> [CRY]CRY0 =PYM;GRU;1 (GCCEGRUPYM) !Delete
  LEV C*2 Definition level
  LIN C*2 Line number
  PRNROW C*4 Print row
  PYM CYM Pyramid -> [CYM]CYM0 =PYM (GCCEPYM) !Delete
  SBBGRU CYR Subgroups -> [CRY]CRY0 =PYM;SBBGRU;1 (GCCEGRUPYM) !Delete
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GCCEPYM (CYM) - Dimension pyramids
Keys (first = PK; D = duplicates allowed): CYM0 PYM; CYM1 DIE+PYM
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[CYM]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[CYM]DIE (GDIE) !Block
  EXPNUM L*8 Export number
  PYM CYM Pyramid -> [CYM]CYM0 =[CYM]PYM (GCCEPYM) !Delete
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GCOA (COA) - Chart of accounts
Keys (first = PK; D = duplicates allowed): COA0 COA
Fields:
  ACCFMT A*15 Account format
  ACCLEN C*2 Length
  ACCMIS GAC(50) Miscellaneous accounts -> [GAC]GAC0 =COA;ACCMIS(indice) (GACCOUNT) !Block
  ACS ACS Access code -> [ACS]ACS0 =[COA]ACS (ACCCOD) !Block
  ANATRK M*4 Analytical tracking [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  AUX M*4 Ctrl account [menu 1: 1=No,2=Yes]
  CLSCOD CLA(30) Classification -> [CLS]CLS0 =LEGCLS;CLSCOD (GACCCLS) !Block
  COA COA Chart code -> [COA]COA0 =[COA]COA (GCOA) !Delete
  COLHEA AX1 Column header
  CREAUT M*4 Automatic creation [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  FXDLEN M*4 Fixed length [menu 1: 1=No,2=Yes]
  GENTRK M*4 General tracking [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LEGCLS ADI Legislation class -> [ADI]CODE =909;LEGCLS (ATABDIV) !Block
  PFX A*10(30) Prefix
  PFXNBR C*2 Number of prefixes
  PYR GYM BI pyramid -> [GYM]GYM0 =[COA]PYR (GACCPYM) !Block
  PYRREF GYM Reference pyramid -> [GYM]GYM0 =[COA]PYRREF (GACCPYM) !Block
  SHOTRA AX1 Short description
  TAXMGT M*4 Tax management [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GDIE (DIE) - Dimension types
Notes: differs in V9.0 P12 (diff: AT3_GDIE.htm); differs in V10 P1 (diff: ATD_GDIE.htm)
Keys (first = PK; D = duplicates allowed): DIE0 DIE
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[DIE]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CCECRE ADI Automatic creation -> [ADI]CODE =326;CCECRE (ATABDIV) !Block
  CCEFMT A*15 Dimension format
  CCEMIS CCE(10) Miscellaneous dimensions -> [CCE]CCE0 =DIE;CCEMIS (CACCE) !Block
  COLHEA AX1 Column header
  CREAUT M*4 Automatic creation [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Dimension type -> [DIE]DIE0 =[DIE]DIE (GDIE) !Delete
  ENT M*4 Entity [menu 1: 1=No,2=Yes] act:GDD
  ENV M*4 Envelope [menu 1: 1=No,2=Yes] act:GDD
  EXPNUM L*8 Export number
  FLGMODACE M*4 Change final entries [menu 1: 1=No,2=Yes]
  PCCFLG M*4 Cost type [menu 1: 1=No,2=Yes] act:PJM
  PJMFLG M*4 Project management [menu 1: 1=No,2=Yes] act:PJM
  PRJMGT M*4 No c/fwd. [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GDPDUDUD (GDPDUD) - Open items
Notes: activity code KDE; not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GDPDUD0 USERID+TYP+NUM+LIG+DUDLIG
Fields:
  ACCNUM L*8 Internal number
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ref. amt. curr.
  AUUID AUUID Single identifier
  BPAPAY ADR Business partner address
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[GDPDUD]BPR (BPARTNER) !Block
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[GDPDUD]BPRPAY (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CPY CPY Company -> [CPY]CPY0 =[GDPDUD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[GDPDUD]CUR (TABCUR) !Block
  DUDLIG C*3 Due date number
  FCTVCR VCR Receipt act:FCT
  FCY FCY Site -> [FCY]FCY0 =[GDPDUD]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGCLE C*1 Closed
  LIG C*3 Line number
  NUM VCR Document no.
  NUMDUD A*15 Unique number
  PAYCUR MD1 Paid
  PAYDAT D Payment date
  PAYLOC MD1 Paid ref. currency
  PER C*2 Period
  SAC SAC Control
  SNS C*2 Sign
  TMPCUR MD1 Provisional payment
  TMPLOC MD1 Provisional payment
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GDPDUD]UPDUSR (AUTILIS) !Other
  USERID ID User identity+ adxuid
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## GLED (LED) - Ledger
Notes: differs in V9.0 P12 (diff: AT3_GLED.htm); differs in V10 P1 (diff: ATD_GLED.htm)
Keys (first = PK; D = duplicates allowed): LED0 LED
Fields:
  ACCVCR M*4 One document per account (Italy) [menu 1: 1=No,2=Yes]
  ANA M*4 Analytical [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BAL M*4 Balance [menu 1: 1=No,2=Yes]
  BUD M*4 Budget [menu 1: 1=No,2=Yes]
  CMM M*4 Commitment [menu 1: 1=No,2=Yes]
  COA COA Chart code -> [COA]COA0 =[LED]COA (GCOA) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CSL M*4 Consolidation [menu 1: 1=No,2=Yes] act:PRCSL
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =DIE(indice) (GDIE) !Block
  DIEDACOBY M*4 Mandat. dim entry [menu 1: 1=No,2=Yes]
  DIEIPT M*4 Allocation [menu 1: 1=No,2=Yes]
  DIENBR C*1 No. of dim. types
  ENDVCR M*4 Closing document [menu 1: 1=No,2=Yes]
  EQLRANANA M*4 Balanced carryforward [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCYBAL M*4 Balance by site [menu 1: 1=No,2=Yes]
  GDD M*4 Expenses management [menu 1: 1=No,2=Yes] act:GDD
  GEN M*4 General [menu 1: 1=No,2=Yes]
  GENTYP M*15 Generation type [menu 807: 1=Site,2=Company]
  LED LED Ledger -> [LED]LED0 =[LED]LED (GLED) !Delete
  LEDTYPE M*15 Ledger type [menu 2653: 1=Not applicable,2=SNC base,3=IAS/IFRS standards,4=SNS micro entities,5=Others] act:KPO
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MTCFLG M*4 Matchable [menu 1: 1=No,2=Yes]
  PJMFLG M*4 Project management [menu 1: 1=No,2=Yes] act:PJM
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GRPACEMTC (GRM) - Matching group entries
Keys (first = PK; D = duplicates allowed): GRM0 COD+NUMORD+CODACE1+LIG1
Fields:
  AUUID AUUID Single identifier
  COD GRA Group entry -> [GRA]GRA0 =COD (GRPAUTACE) !Delete
  CODACE1 GAU Entry code -> [GAU]GAU0 =CODACE1 (GAUTACE) !Block
  CODACE2 GAU Entry code -> [GAU]GAU0 =CODACE2 (GAUTACE) !Block
  CODACE3 GAU Entry code -> [GAU]GAU0 =CODACE3 (GAUTACE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GRM]CREUSR (AUTILIS) !Other
  INVMTC M*4 Invoice matching [menu 1: 1=No,2=Yes]
  LIG1 C*4 Line number
  LIG2 C*4 Line number
  LIG3 C*4 Line number
  NUMORD C*2 Order no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GRM]UPDUSR (AUTILIS) !Other

## GRPAUTACE (GRA) - Automatic journal group
Keys (first = PK; D = duplicates allowed): GRA0 COD
Fields:
  AUUID AUUID Single identifier
  COD GRA Group entry -> [GRA]GRA0 =[GRA]COD (GRPAUTACE) !Delete
  CODACE GAU(10) Entry code -> [GAU]GAU0 =CODACE(indice) (GAUTACE) !Block
  CODACT ACV Activity code -> [ACV]CODACT =[GRA]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GRPCPC (GCP) - Group of skills
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## GRPCPCD (HRGCD) - Skill set detail
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## GTYPACCENT (GTE) - Document types
Keys (first = PK; D = duplicates allowed): GTE0 TYP+LEG
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GTE]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  AUZJOU M*4(10) Authorization [menu 1: 1=No,2=Yes]
  AUZLED M*4(10) Authorized ledger [menu 2647: 1=None,2=Authorized,3=Mandatory]
  COU ANM Sequence number -> [ANM]ANM0 =[GTE]COU (ACODNUM) !Block
  COUVATCEE ANM EU tax sequence no. -> [ANM]ANM0 =[GTE]COUVATCEE (ACODNUM) !Block act:KIT
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DAS2 M*4 Fee declaration [menu 1: 1=No,2=Yes] act:FEE2
  DEFJOU JOU Default journal -> [JOU]JOU0 =DEFJOU;[V]GSUPCLE (GJOURNAL) !Block
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DUDCASFLG M*4 Open item schedule [menu 1: 1=No,2=Yes] act:CASIN
  DUDDATFLG M*4 Open item management [menu 1: 1=No,2=Yes]
  DUDTYP M*15 Open item type [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ESDTRK M*4 Service provisions [menu 1: 1=No,2=Yes] act:ESD
  EXPNUM L*8 Export number
  FLGEXPCRE M*4 Expense creation [menu 1: 1=No,2=Yes]
  FUP M*4 Reminders [menu 1: 1=No,2=Yes]
  GFY AGF Group -> [AGF]AGF0 =[GTE]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANNUM M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PER M*15 Period [menu 621: 1=Normal,2=Carryforward,3=Closing]
  PREACC M*4 Temporary fiscal year [menu 1: 1=No,2=Yes] act:KIT
  RATDAT M*15 Rate date [menu 917: 1=Journal entry date,2=Source document date]
  SHOTRA AX1 Short description
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Delete
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VAT M*4 VAT on debit [menu 1: 1=No,2=Yes]
  VATPAI M*4 VAT on payment [menu 1: 1=No,2=Yes]
  VCRMOD M*4 Template journals [menu 1: 1=No,2=Yes]
  VCROUTBSE M*4 Off-balance-sheet entries [menu 1: 1=No,2=Yes]
  VCRREA M*4 Actual journals [menu 1: 1=No,2=Yes]
  VCRSIM M*4 Simulation journals [menu 1: 1=No,2=Yes]
  VLYEND D Validity end date
  VLYSTR D Validity start date

## GVARCODPAR (GVA) - Parameters of variables
Keys (first = PK; D = duplicates allowed): GVA0 CODPAR
Fields:
  AUUID AUUID Single identifier
  CODPAR A*10 Parameter code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  INTITPAR ATX Description
  TYPPAR M*15 Parameter type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GVARGAU (GVG) - Automatic journal variables
Keys (first = PK; D = duplicates allowed): GVG0 CODVAR
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[GVG]CODACT (ACTIV) !Block
  CODTRT ADC Processing
  CODVAR A*10 Variable code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  INFO ATX(5) Description
  INTITA ATX Description
  SHOTRA AX1 Short description
  SUBPRG A*20 Subprograms
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GVARPARGAU (GVP) - Variables parameters
Keys (first = PK; D = duplicates allowed): GVP0 CODVAR+NOPAR
Fields:
  ADRVAL M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AUUID AUUID Single identifier
  CODPAR A*10 Parameter code
  CODVAR A*10 Variable code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GVP]CREUSR (AUTILIS) !Other
  INTITPAR ATX Parameter title
  NOPAR C*2 Parameter no.
  TYPPAR M*15 Parameter type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GVP]UPDUSR (AUTILIS) !Other

## GVARPARVAL (GVV) - Parameter values
Keys (first = PK; D = duplicates allowed): GVV0 COD+LINNUM+FLD+CODVAR+CODPAR
Fields:
  AUUID AUUID Single identifier
  COD GAU Code -> [GAU]GAU0 =[GVV]COD (GAUTACE) !Delete
  CODPAR A*10 Parameter code
  CODVAR A*10 Variable code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GVV]CREUSR (AUTILIS) !Other
  FLD A*10 Field
  LINNUM C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GVV]UPDUSR (AUTILIS) !Other
  VALPAR A*80 Parameter value

## HD1CLOB (HD1) - Service reqts text files
Keys (first = PK; D = duplicates allowed): HD10 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD1 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD1]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD1]UPDUSR (AUTILIS) !Other

## HD2CLOB (HD2) - Actions text files
Keys (first = PK; D = duplicates allowed): HD20 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD2 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD2]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD2]UPDUSR (AUTILIS) !Other

## HD3CLOB (HD3) - Solutions text files
Keys (first = PK; D = duplicates allowed): HD30 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD3 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD3]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD3]UPDUSR (AUTILIS) !Other

## HD4CLOB (HD4) - Commerl reports text files
Keys (first = PK; D = duplicates allowed): HD40 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD4 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD4]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD4]UPDUSR (AUTILIS) !Other

## HD5CLOB (HD5) - Marketing text files
Keys (first = PK; D = duplicates allowed): HD50 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD5 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD5]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD5]UPDUSR (AUTILIS) !Other

## HD6CLOB (HD6) - CRM mini text files
Keys (first = PK; D = duplicates allowed): HD60 NUM+TYP
Fields:
  AUUID AUUID Single identifier
  CLOB HD6 Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD6]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD6]UPDUSR (AUTILIS) !Other

## HD7CLOB (HD7) - Aft-ss srv cons txt files
Keys (first = PK; D = duplicates allowed): HD70 NUM+TYP+PRONUM; HD71 PRONUM (D)
Fields:
  AUUID AUUID Single identifier
  CLOB ACB Text file (clob)
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HD7]CREUSR (AUTILIS) !Other
  NUM A*30 Sequence no.
  PRONUM L*8 Process number
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HD7]UPDUSR (AUTILIS) !Other

## HISTOCRM (HST) - History
Keys (first = PK; D = duplicates allowed): HST0 RECNUM+RECTYP (D); HST1 CLSNUM (D); HST2 SSS+CLSNUM (D)
Fields:
  AUUID AUUID Single identifier
  CLSNUM L*8 Order no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HST]CREUSR (AUTILIS) !Other
  DON M*4 Completed [menu 1: 1=No,2=Yes]
  RECDAT D Date
  RECHOU HM Time
  RECNUM VCR Code
  RECTYP AOB Record type -> [AOB]ABREV =[HST]RECTYP (AOBJET) !Block
  SSS A*30 Session
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HST]UPDUSR (AUTILIS) !Other

## HISTOMDT (HMDT) - Payments made
Notes: activity code SDD
Keys (first = PK; D = duplicates allowed): HMDT0 CPY+UMRNUM+PAYDAT+PAYNUM; HMDT1 PAYNUM
Fields:
  AMT MD1 Amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[HMDT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HMDT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[HMDT]CUR (TABCUR) !Block
  DPT M*15 Dispute reason [menu 3632: 1=Revocation,2=Reject,3=Return]
  FRMNUM VCR Slip no.
  PAYDAT D Direct debit date
  PAYNUM VCR Payment number
  SEQTYP ADI Sequence type -> [ADI]CODE =330;SEQTYP (ATABDIV) !Block
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HMDT]UPDUSR (AUTILIS) !Other

## HISTOOMM (HIM) - Mailing history
Keys (first = PK; D = duplicates allowed): HIM0 HIMNUM; HIM1 OMMNUM+CCNNUM (D); HIM2 OMMNUM+BPRNUM+CCNNUM (D); HIM3 OMMNUM+BPRNUM (D); HIM4 BPRNUM (D); HIM5 CCNNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =BPRNUM (BPARTNER) !RTZ
  CCNNUM AIN Contact (rel.) code -> [AIN]AIN0 =[HIM]CCNNUM (CONTACTCRM) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HIM]CREUSR (AUTILIS) !Other
  DATSND D Send date
  HIMNUM VCR History code
  OMMNUM VCR Mail code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HIM]UPDUSR (AUTILIS) !Other

## HOROITM (HOI) - Time stamped articles
Keys (first = PK; D = duplicates allowed): HOI0 MACNUM+PBLNUM+AUSNUM; HOI1 PBLNUM+MACNUM+AUSNUM (D); HOI2 AUSNUM+PBLNUM+MACNUM (D)
Fields:
  AUSNUM AUS User -> [AUS]CODUSR =[HOI]AUSNUM (AUTILIS) !Delete
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HOI]CREUSR (AUTILIS) !Other
  ITMREF ITM Time stamped article -> [ITM]ITM0 =[HOI]ITMREF (ITMMASTER) !Delete
  MACNUM ITM Product base -> [ITM]ITM0 =[HOI]MACNUM (ITMMASTER) !Delete
  PBLNUM PBL Skill group -> [PBL]PBL0 =[HOI]PBLNUM (FAMPB) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HOI]UPDUSR (AUTILIS) !Other

## HRCATCSP (HRCSP) - Socio-professional category
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCLLCVT (HRCLV) - Collective agreement
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCOMPANYAFR (CPYAFR) - Company
Notes: activity code KAFR; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCOMPANYKSA (CPYKSA) - Company
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCOMPANYPO (CPYPO) - Company
Notes: activity code FPOPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCTRDOC (HRDOC) - Documents to generate
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRCTRGRD (HRCGD) - Arrival reason
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACT (HREXT) - Extract template
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTDAT (HREXD) - Source
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTDEF (HREXL) - Definition
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTFIL (HREXF) - Filters
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTGRP (HREXG) - Groups
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTPAR (HREXP) - Parameters
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTRES (HREXR) - Results
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HREXTRACTVAL (HREXV) - Validations
Notes: activity code KGZA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRFACILITYPO (FCYPO) - Sites
Notes: activity code FPOPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRFACILITYSA (FCYSA) - South African site fields
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRLICAUT (HRLIC) - Permits and authorizations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRMEDAPT (HRMDP) - Ability
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRMEDTYP (HRMDT) - Visit type
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRNATCON (HRNCT) - Nature of contract
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRPOTPEN (HRPEN) - Position hazardous conditions
Notes: activity code FFRPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRRPLREN (HRRPL) - Replacement reason
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRSTDINDCLS (HRSIC) - Std. industrial classification
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRTRADECLASS (HRTCC) - Trade classification
Notes: activity code FZAPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HRXITGRD (HRXGD) - Disposal reason
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## HTMMAITXT (HTMMAI) - CRM email text
Keys (first = PK; D = duplicates allowed): HTMMAI0 FNC+LAN+AUS; HTMMAI1 FNC+AUS+LAN
Fields:
  AUS AUS User -> [AUS]CODUSR =[HTMMAI]AUS (AUTILIS) !Block
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HTMMAI]CREUSR (AUTILIS) !Other
  FNC M*20 Function [menu 2073: 1=Service request,2=Intervention]
  LAN LAN Language -> [TLA]TLA0 =[HTMMAI]LAN (TABLAN) !Block
  TXT1 AC0*4 E-mail text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HTMMAI]UPDUSR (AUTILIS) !Other

## IMCDETPRT (IMP) - Cost comparison
Keys (first = PK; D = duplicates allowed): IMP0 PRONUM+ITMREF+TYPCST+BRDCOD; IMP1 CURUID (D)
Fields:
  AUUID AUUID Single identifier
  BRDCOD C*4 Cost group
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[IMP]CREUSR (AUTILIS) !Other
  CST MD8 Cost
  CST2 MD8 Cost
  CURUID L*8 Process
  ITMREF ITM Product -> [ITM]ITM0 =ITMREF (ITMMASTER) !Delete
  PRONUM L*8 Process number
  TYPCST M*15 Cost type [menu 319: 1=Material,2=Machine,3=Labor,4=Subcontracting,5=Overhead costs,6=Calculated cost]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[IMP]UPDUSR (AUTILIS) !Other

## INCOTERM (ICTH) - Incoterms
Keys (first = PK; D = duplicates allowed): ICT0 ICTCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ICTH]CREUSR (AUTILIS) !Other
  DES AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ICTCOD A*5 Incoterm
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ICTH]UPDUSR (AUTILIS) !Other

## INCOTERMD (ICTD) - Incoterms Detail
Keys (first = PK; D = duplicates allowed): ICTD0 ICTCOD+CSTNAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ICTD]CREUSR (AUTILIS) !Other
  CSTNAT C*5 Cost nature
  CSTPYR M*15 Charges payable by [menu 2277: 1=Neither the buyer, nor the seller,2=Buyer,3=Seller,4=Buyer and seller]
  ICTCOD A*5 Incoterm
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ICTD]UPDUSR (AUTILIS) !Other

## INTCOFLO (ICF) - Intercompany transactions
Notes: activity code INTCO
Keys (first = PK; D = duplicates allowed): ICF0 ABRFIC+NUM+CPYSRC+CPYTGR+FCYTGR; ICF1 TYPVCR+NUMVCR+CPYTGR+FCYTGR+CPYSRC+ABRFIC+NUM
Fields:
  ABRFIC A*3 Table abbreviation
  ACCDAT D Accounting date
  ACCSRC GAC(10) Source account -> [GAC]GAC0 =COASRC;ACCSRC (GACCOUNT) !Block
  ACCTGR GAC(10) Target account -> [GAC]GAC0 =COATGR;ACCTGR (GACCOUNT) !Block
  AUUID AUUID Single identifier
  BPRSRC BPR Source BP -> [BPR]BPR0 =[ICF]BPRSRC (BPARTNER) !Block
  BPRTGR BPR Target BP -> [BPR]BPR0 =[ICF]BPRTGR (BPARTNER) !Block
  COASRC COA(10) Chart of acc. -> [COA]COA0 =[ICF]COASRC (GCOA) !Block
  COATGR COA(10) Target main chart -> [COA]COA0 =[ICF]COATGR (GCOA) !Block
  CPYSRC CPY Source company -> [CPY]CPY0 =[ICF]CPYSRC (COMPANY) !Block
  CPYTGR CPY Target company -> [CPY]CPY0 =[ICF]CPYTGR (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[ICF]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[ICF]CURLED (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[ICF]FCY (FACILITY) !Block
  FCYTGR FCY Target site -> [FCY]FCY0 =[ICF]FCYTGR (FACILITY) !Block
  JOUVCR JOU Journal -> [JOU]JOU0 =JOUVCR;[V]GSUPCLE (GJOURNAL) !Block
  LED LED(10) Ledger -> [LED]LED0 =[ICF]LED (GLED) !Block
  NUM VCR Document no.
  NUMVCR VCR Accounting document
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  TYPVCR GTE Entry type -> [GTE]GTE0 =TYPVCR;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## INTERVEN (ITN) - Service response
Notes: differs in V9.0 P12 (diff: AT3_INTERVEN.htm)
Keys (first = PK; D = duplicates allowed): ITN0 NUM; ITN1 DATX (D); ITN2 BPC (D); ITN3 CCN (D); ITN4 REP+DATX (D); ITN5 REP+DAT (D); ITN6 DAT (D); ITN7 ITNORI+ITNORIVCR+ITNORIVCRL (D)
Fields:
  ADD ADL(3) Address
  AUUID AUUID Single identifier
  BPC BPR Customer -> [BPR]BPR0 =[ITN]BPC (BPARTNER) !Block
  CCN AIN Contact (relationship) -> [AIN]AIN0 =[ITN]CCN (CONTACTCRM) !Block
  CONNUM CON Contract number -> [CON]CON0 =[ITN]CONNUM (CONTSERV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[ITN]CRY (TABCOUNTRY) !Block
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[ITN]CUR (TABCUR) !Block
  DAT D Start
  DATEND D End
  DATX D Week conversion
  DON M*4 Completed [menu 1: 1=No,2=Yes]
  DTCKIL L*8 Distance (miles)
  DUR HMD Duration
  EML MAI Email address
  FULDAY M*4 Entire day [menu 1: 1=No,2=Yes]
  HOU HM Time
  HOUEND HM End time
  HTOTTIMSPG L*8 Time passed (hours)
  IFFADD CLX Indications
  ITNCODADD ADR Address
  ITNORI M*15 Source [menu 2996: 1=Manual creation,2=Agenda]
  ITNORIVCR VCR Original document no.
  ITNORIVCRL L*8 Original line no.
  ITNRECADD A*15 Recording
  ITNTYPADD M*15 Type [menu 954: 1=Contact,2=BP,3=Company,4=Site]
  MAC MAC Base -> [MAC]MAC0 =[ITN]MAC (MACHINES) !Block
  MACGRU MAC Base regroupment -> [MAC]MAC0 =[ITN]MACGRU (MACHINES) !Block
  MANTIMFLG C*2 Manual entry flag
  MOB TEL Mobile phone
  MTOTTIMSPG C*2 Time passed (min.)
  NUM VCR Sequence no.
  NUMFULOBJ CLC Chrono txt file
  NUMFULRPO CLC Report chrono
  OBJ CLX Overview
  OBJFLG C*2 Flag text file
  ORDNUM SOH Order number -> [SOH]SOH0 =[ITN]ORDNUM (SORDER) !Block
  PBLSOL M*4 Problem resolved [menu 1: 1=No,2=Yes]
  REP AUS Provider -> [AUS]CODUSR =[ITN]REP (AUTILIS) !Block
  RER RRS(15) Reservations -> [RRS]RRS0 =[ITN]RER (RESRES) !Block
  RPO CLX Overview
  RPOFLG C*2 Overview written
  SALFCY FCY Site -> [FCY]FCY0 =[ITN]SALFCY (FACILITY) !Block
  SAT SAT County
  SCO M*4 Subcontracted [menu 1: 1=No,2=Yes]
  SCOAMT MD1 Negotiated amount
  SCONUM BPR Subcontractor -> [BPR]BPR0 =[ITN]SCONUM (BPARTNER) !Block
  SRVCONCOV M*4 Coverage [menu 1: 1=No,2=Yes]
  SRVDEMNUM SRE Serv. req. No. -> [SRE]SRE0 =[ITN]SRVDEMNUM (SERREQUEST) !Block
  TEL TEL Telephone
  TRITIM C*4 Estimated travel time
  TYP ADI Category -> [ADI]CODE =407;TYP (ATABDIV) !Block
  TYPFULOBJ CLT Type text file
  TYPFULRPO CLT Report type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEE C*4 Week
  ZIP POS Postal code

## ITCDET (ICD) - Detail cost for printing
Keys (first = PK; D = duplicates allowed): ICD1 UID+CODFIC+CLE+BRDCOD; ICD2 ITMREF+STOFCY (D)
Fields:
  AUUID AUUID Single identifier
  BRDCOD C*4 Cost group
  CLE A*100 Key
  CODFIC ATB Table code -> [ATB]CODFIC =[ICD]CODFIC (ATABLE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ICD]CREUSR (AUTILIS) !Other
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LABCST MD8 Labor cost
  MACCST MD8 Machine cost
  MATCST MD8 Material cost
  STOFCY FCY Storage site -> [FCY]FCY0 =[ICD]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ICD]UPDUSR (AUTILIS) !Other

## ITCDETPRT (ICP) - Temporary products - cost
Keys (first = PK; D = duplicates allowed): ICP0 STOFCY+ITMREF+CSTTYP-ITCSEQ+MATREF+CPNTYP+UID+BRDCOD; ICP1 CURUID (D)
Fields:
  AUUID AUUID Single identifier
  BRDCOD C*4 Cost group
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ICP]CREUSR (AUTILIS) !Other
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  CURUID L*8 Process
  ITCSEQ L*8 Sequence no.
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LABCST MD8 Labor cost
  MACCST MD8 Machine cost
  MATCST MD8 Material cost
  MATREF ITM Component -> [ITM]ITM0 =[ICP]MATREF (ITMMASTER) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[ICP]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ICP]UPDUSR (AUTILIS) !Other

## ITCMAT (ICC) - Temporary products - cost
Keys (first = PK; D = duplicates allowed): ICC0 STOFCY+ITMREF+CSTTYP-ITCSEQ+MATREF+ECCVALMAJ+ECCVALMIN+CPNTYP+UID; ICC1 UID+STOFCY+ITMREF+CSTTYP (D)
Fields:
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Costing mode [menu 480: 1=Standard cost,2=Updated standard price,3=Last cost,4=Moving average cost,5=FIFO cost,6=Average lot cost,7=Order cost,8=LIFO cost,9=Primary issue method,10=Secondary issue method,11=Simulated cost,12=Simulated price]
  CSTSEQ C*4 Sequence
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  EXPNUM L*8 Export number
  INVDTACST MD8 Invoicing element act:SPD
  ITCSEQ L*8 Sequence no.
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LABCST MD8 Labor cost act:LAB
  MACCST MD8 Machine cost act:MAC
  MATCST MD8 Material cost act:MAT
  MATFLG M*4 Material [menu 1: 1=No,2=Yes]
  MATREF ITM Component -> [ITM]ITM0 =[ICC]MATREF (ITMMASTER) !Block
  OVELABCST MD8 Labor overh
  OVEMACCST MD8 Machine OH cost
  OVEMATCST MD8 Material overhead cost
  OVESCOCST MD8 Subcontract
  QTYSTU QTY STK quantity
  QTYTOP QTY Level 1 quantity
  SCOCST MD8 Subcontract cost
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  STOFCY FCY Storage site -> [FCY]FCY0 =[ICC]STOFCY (FACILITY) !Delete
  STU UOM Stock unit -> [TUN]TUN0 =[ICC]STU (TABUNIT) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  YEA C*4 Year

## ITCMATCH (IMC) - Cost comparison
Keys (first = PK; D = duplicates allowed): ITC0 PRONUM+ITMREF
Fields:
  AFFUNI M*4 Unit display [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CLCQTY QTY Calculation quantity
  CLCQTY2 QTY Calculation quantity
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTTOT MD8 Total cost
  CSTTOT2 MD8 Total cost
  CSTTYP1 M*15 Cost type [menu 347: 1=Standard,2=Revised,3=Budget,4=Simulated,5=Estimated theoretical,6=Estimated release,7=Estimated production,8=Estimated cost price]
  CSTTYP2 M*15 Cost type [menu 347: 1=Standard,2=Revised,3=Budget,4=Simulated,5=Estimated theoretical,6=Estimated release,7=Estimated production,8=Estimated cost price]
  DESCEND M*4 Multilevel [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  INVDTA MD8 Invoice element
  INVDTA2 MD8 Invoice element
  ITCDAT1 D Date calculated
  ITCDAT2 D Date calculated
  ITCENDDAT1 D Validity
  ITCENDDAT2 D Validity
  ITCSEQ1 C*4 Sequence
  ITCSEQ2 C*4 Sequence
  ITCSTRDAT1 D Valid from
  ITCSTRDAT2 D Valid from
  ITMREF ITM Product -> [ITM]ITM0 =ITMREF (ITMMASTER) !Delete
  LABCST MD8 Labor cost act:LAB
  LABCST2 MD8 Labor cost act:LAB
  LABTOT MD8 Total labor cost
  LABTOT2 MD8 Total labor cost
  MACCST MD8 Machine cost act:MAC
  MACCST2 MD8 Machine cost act:MAC
  MACTOT MD8 Total machine
  MACTOT2 MD8 Total machine
  MATCST MD8 Material cost act:MAT
  MATCST2 MD8 Material cost act:MAT
  MATTOT MD8 Total material
  MATTOT2 MD8 Total material
  OVELABCST MD8 Labor overh
  OVELABCST2 MD8 Labor overh
  OVEMACCST MD8 Machine OH cost
  OVEMACCST2 MD8 Machine OH cost
  OVEMATCST MD8 Material overhead cost
  OVEMATCST2 MD8 Material overhead cost
  OVESCOCST MD8 Subcontract
  OVESCOCST2 MD8 Subcontract
  OVETOT MD8 Total overhead
  OVETOT2 MD8 Total overhead
  PRONUM L*8 Process number
  SCOCST MD8 Subcontract cost
  SCOCST2 MD8 Subcontract cost
  SCOTOT MD8 Total subcontracted
  SCOTOT2 MD8 Total subcontracted
  STOFCY1 FCY Storage site -> [FCY]FCY0 =[IMC]STOFCY1 (FACILITY) !Delete
  STOFCY2 FCY Storage site -> [FCY]FCY0 =[IMC]STOFCY2 (FACILITY) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN1 L*8 WO line
  VCRLIN2 L*8 WO line
  VCRNUM1 VCR Work order
  VCRNUM2 VCR Work order
  VLTTOT MD8 Valuation cost
  VLTTOT2 MD8 Valuation cost

## ITCNAT (ICN) - Nature detail - costs
Keys (first = PK; D = duplicates allowed): ICN0 STOFCY+ITMREF+CSTTYP-ITCSEQ+OVENAT+UID
Fields:
  AUUID AUUID Single identifier
  CLCQTY QTY Calculation quantity
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTSEQ C*4 Sequence
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  EXPNUM L*8 Export number
  FXDAMTLEV MD8(7) Fixed level amt
  FXDAMTSSE MD8(7) Fixed sub-level amount
  ITCDAT D Date calculated
  ITCSEQ L*8 Sequence no.
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  NATAMTLEV MD8(7) Level amount
  NATAMTSSE MD8(7) Sub-level amount
  OVENAT ONA Overhead cat. -> [ONA]ONA0 =[ICN]OVENAT (OVENAT) !Delete
  SLTOVECOL M*15 Overhead column choice [menu 320: 1=Formula A,2=Formula B,3=Formula C,4=Formula D]
  STOFCY FCY Storage site -> [FCY]FCY0 =[ICN]STOFCY (FACILITY) !Delete
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  YEA C*4 Year

## ITCWST (IWC) - Temporary products - cost
Keys (first = PK; D = duplicates allowed): IWC0 STOFCY+ITMREF+CSTTYP-ITCSEQ+WST+SCOITMREF+UID
Fields:
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Costing mode [menu 480: 1=Standard cost,2=Updated standard price,3=Last cost,4=Moving average cost,5=FIFO cost,6=Average lot cost,7=Order cost,8=LIFO cost,9=Primary issue method,10=Secondary issue method,11=Simulated cost,12=Simulated price]
  CSTSEQ C*4 Sequence
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  EXPNUM L*8 Export number
  ITCENDDAT D Validity
  ITCSEQ L*8 Sequence no.
  ITCSTRDAT D Validity
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  OPEAMT MS1 Operation amount
  OPECST DCB*9.2 Hourly rate
  OPETIM TIH Run time
  OPETIMTOP TIH Run time (PF)
  OVEAMT MS1 Overhead
  OVEAMTTOP MS1 Overhead
  PRISCO MD8 Price
  QTYSCOITM QTY Quantity
  QTYSCOTOP QTY Quantity
  RATCOD M*15 Dimension rate selection [menu 324: 1=Standard,2=Revised standard,3=Budget,4=Simulation]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[IWC]SCOITMREF (ITMMASTER) !Block
  SETAMT MS1 Adjustment amount
  SETCST DCB*9.2 Hourly rate
  SETTIM TIH Setup time
  SETTIMTOP TIH Setup time (PF)
  STOFCY FCY Storage site -> [FCY]FCY0 =[IWC]STOFCY (FACILITY) !Delete
  UID L*8 Process
  UOMSCOITM UOM Unit -> [TUN]TUN0 =[IWC]UOMSCOITM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCSTTYP M*15 Rate type [menu 314: 1=Unit,2=Fixed]
  WST WST Work center
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]
  YEA C*4 Year

## ITCWSTW (IWW) - Temporary products - cost
Keys (first = PK; D = duplicates allowed): IWW0 UID+STOFCY+ITMREF+CSTTYP+YEA+WST
Fields:
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Costing mode [menu 480: 1=Standard cost,2=Updated standard price,3=Last cost,4=Moving average cost,5=FIFO cost,6=Average lot cost,7=Order cost,8=LIFO cost,9=Primary issue method,10=Secondary issue method,11=Simulated cost,12=Simulated price]
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  EXPNUM L*8 Export number
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  OPEAMT MS1 Operation amount
  OPECST DCB*9.2 Hourly rate
  OPETIM TIH Run time
  PRISCO MD8 Price
  RATCOD M*15 Dimension rate selection [menu 324: 1=Standard,2=Revised standard,3=Budget,4=Simulation]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[IWW]SCOITMREF (ITMMASTER) !Block
  SETAMT MS1 Adjustment amount
  SETCST DCB*9.2 Hourly rate
  SETTIM TIH Setup time
  STOFCY FCY Storage site -> [FCY]FCY0 =[IWW]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCSTTYP M*15 Rate type [menu 314: 1=Unit,2=Fixed]
  WST WST Work center
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]
  YEA C*4 Year

## ITMBOM (ITB) - Products - BOMs
Keys (first = PK; D = duplicates allowed): ITB0 ITMREF+BOMALT+LLCTYP; ITB1 BOMALT+LLCTYP+LLC+ITMREF
Fields:
  AUUID AUUID Single identifier
  BOHITM ITM The lowest header -> [ITM]ITM0 =[ITB]BOHITM (ITMMASTER) !Block
  BOMALT C*2 BOM code
  BOMEXIFLG M*4 BOM existence [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[ITB]ITMREF (ITMMASTER) !Delete
  LLC C*2 Lowest level code
  LLCTYP M*4 Code type [menu 2224: 1=Business,2=Manufacturing/Subcontracting]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WUSEXIFLG M*4 Where-used existence [menu 1: 1=No,2=Yes]

## ITMBOMCFG (CFB) - Products - BOMs
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): ITB0 ITMREF+BOMALT+LLCTYP; ITB1 BOMALT+LLCTYP+LLC+ITMREF
Fields:
  AUUID AUUID Single identifier
  BOHITM ITM The lowest header -> [ITM]ITM0 =[CFB]BOHITM (ITMMASTER) !RTZ
  BOMALT TBO BOM code -> [TBO]TBO0 =[CFB]BOMALT (TABBOMALT) !Delete
  BOMEXIFLG M*4 BOM existence [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[CFB]ITMREF (ITMMASTER) !Delete
  LLC C*2 Lowest level code
  LLCTYP M*4 Code type [menu 2224: 1=Business,2=Manufacturing/Subcontracting]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WUSEXIFLG M*4 Where-used existence [menu 1: 1=No,2=Yes]

## ITMBPC (ITU) - Customer product
Keys (first = PK; D = duplicates allowed): ITU0 ITMREF+BPCNUM; ITU1 BPCNUM+ITMREFBPC; ITU2 BPCNUM+ITMDESBPC (D)
Fields:
  AUUID AUUID Single identifier
  BPCNUM BPR Customer -> [BPR]BPR0 =[ITU]BPCNUM (BPARTNER) !Block
  CFGVCRNUM VCR Journal number config act:CFG
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLUBPC COE UBD coef
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  ITMDESBPC DES Customer description
  ITMREF ITM Product -> [ITM]ITM0 =[ITU]ITMREF (ITMMASTER) !Block
  ITMREFBPC A*20 Customer product
  ITPTEX TXC Picking text
  ITSTEX TXC Sales text
  LOAECCFLG M*4 Version preload [menu 1: 1=No,2=Yes] act:ECC
  PCK PCK Packaging -> [TPA]TPA0 =[ITU]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCU1 UOM Packing 1 -> [TUN]TUN0 =[ITU]PCU1 (TABUNIT) !Block
  PCU2 UOM Packing 2 -> [TUN]TUN0 =[ITU]PCU2 (TABUNIT) !Block
  PCUSAUCOE1 COE PAC1-SAL conv.
  PCUSAUCOE2 COE PAC2-SAL conv.
  SAU UOM Sales unit -> [TUN]TUN0 =[ITU]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ITMBPS (ITP) - Supplier product
Keys (first = PK; D = duplicates allowed): ITP0 ITMREF+BPSNUM; ITP1 ITMREF+PIO+BPSNUM; ITP2 BPSNUM+ITMREFBPS; ITP3 BPSNUM+ITMDESBPS (D); ITP4 ITMREF+BOMALT (D)
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO Subcontract BOM -> [TBO]TBO0 =1;BOMALT (TABBOMALT) !Other
  BPSNUM BPR Supplier -> [BPR]BPR0 =[ITP]BPSNUM (BPARTNER) !Block
  CFGVCRNUM VCR Journal number config act:CFG
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*8 Creation user
  CTMBPSFLG M*4 Back-to-back order [menu 1: 1=No,2=Yes]
  DOUFLG M*15 Blocking [menu 516: 1=No,2=Warning,3=Hold]
  EANCODBPS A*20 Supplier UPC code
  EECINCRAT RAT Intrastat increase act:DEB
  EXPNUM L*8 Export number
  ITMDESBPS DES Supplier description
  ITMREF ITM Product -> [ITM]ITM0 =[ITP]ITMREF (ITMMASTER) !Block
  ITMREFBPS A*20 Supplier product
  LOAECCFLG M*4 Version preload [menu 1: 1=No,2=Yes] act:ECC
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[ITP]MATTOL (MATCHTOL) !Block
  PCU UOM Packing unit -> [TUN]TUN0 =[ITP]PCU (TABUNIT) !Block
  PCUPUUCOE COE PAC-PUR conv.
  PIO C*2 Priority
  PURMINQTY QTY Minimum PO qty.
  PUU UOM Purchase unit -> [TUN]TUN0 =[ITP]PUU (TABUNIT) !Block
  PUUSTUCOE COE PUR-STK conv.
  QLYCRD QLC Quality record -> [QLC]QLC0 =QLYCRD;1 (QLYCRD) !Block
  QLYMRK C*2 Quality rank
  QUAADXUID L*8 Process frequency
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUAFRY L*4 Frequency
  QUANUM L*4 Control number
  QUANUMUID L*4 Entries process
  SCOLTI C*4 Subcontract LT
  STCNUM VCR Cost structure
  TEX TXC Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*8 Change user

## ITMCATEG (ITG) - Product category
Notes: differs in V9.0 P12 (diff: AT3_ITMCATEG.htm); differs in V10 P1 (diff: ATD_ITMCATEG.htm)
Keys (first = PK; D = duplicates allowed): ITG0 STOFCY+TCLCOD; ITG1 TCLCOD+STOFCY
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =1;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ALLRULMAT TRU WO alloc rule -> [TRU]TRU0 =[ITG]ALLRULMAT (TABALLRUL) !Block
  ALLRULMFG TRU Mfg alloc rule -> [TRU]TRU0 =[ITG]ALLRULMFG (TABALLRUL) !Block
  ALLRULORD TRU Order alloc rule -> [TRU]TRU0 =[ITG]ALLRULORD (TABALLRUL) !Block
  ALLRULSCC TRU Sub-con alloc rule -> [TRU]TRU0 =[ITG]ALLRULSCC (TABALLRUL) !Block
  ALLRULSCO TRU Sub-con alloc rule -> [TRU]TRU0 =[ITG]ALLRULSCO (TABALLRUL) !Block
  ALLRULSHI TRU Shipment alloc rule -> [TRU]TRU0 =[ITG]ALLRULSHI (TABALLRUL) !Block
  ALLRULSRE TRU Aftr Sales alloc rule -> [TRU]TRU0 =[ITG]ALLRULSRE (TABALLRUL) !Block
  ALLRULTRF TRU Transf alloc rule -> [TRU]TRU0 =[ITG]ALLRULTRF (TABALLRUL) !Block
  AUUID AUUID Single identifier
  BASPRIORI M*15 Price origin [menu 2271: 1=Entered,2=Purchase price %]
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  BUDCSTUPD M*15 Budgeted std cost [menu 220: 1=Calculated,2=Entered]
  BUY AUS Buyer -> [AUS]CODUSR =[ITG]BUY (AUTILIS) !Block
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFGLIN TLP Product line -> [TLP]TLP0 =[ITG]CFGLIN (TABLINCFG) !Block
  CLEPCTAUT DCB*3.3 Automatic closing %
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTMFLG M*4 Back-to-back order [menu 1: 1=No,2=Yes]
  CTMQTY QTY Direct bk-to-bk qty
  CUNCOD M*15 Count mode [menu 216: 1=Cycle count,2=Annual count,3=No count]
  CUTCSTUPD M*15 Revised std cost [menu 220: 1=Calculated,2=Entered]
  DACPCUCOE M*4 Factor authorized [menu 1: 1=No,2=Yes] act:NUC
  DACPUUCOE M*4 Purchase factor entry [menu 1: 1=No,2=Yes]
  DACSAUCOE M*4 Sales factor entry [menu 1: 1=No,2=Yes]
  DAYCOV COV Coverage
  DIE DIE Dimension type code -> [DIE]DIE0 =[ITG]DIE (GDIE) !Block act:ANA
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  ECCFLG M*4 Version management [menu 1: 1=No,2=Yes] act:ECC
  ECCMAJ ICV Major sequence -> [ICV]ICV0 =[ITG]ECCMAJ (ITMCPTVER) !Block act:ECC
  ECCMIN ICV Minor sequence -> [ICV]ICV0 =[ITG]ECCMIN (ITMCPTVER) !Block act:ECC
  ECCSTO M*20 Stock version [menu 2777: 1=No,2=Major,3=Major and minor] act:ECC
  EEU UOM Intrastat additional unit -> [TUN]TUN0 =[ITG]EEU (TABUNIT) !Block
  EEUSTUCOE COE EU-STK conv.
  EXPNUM L*8 Export number
  EXYMGTCOD M*15 Expiration management [menu 211: 1=Not managed,2=Without rounding,3=Rounding month end,4=Rounding beginning month+1,5=Mandatory entry,6=Manual entry]
  EXYSTA A*1 Expiration status
  FIMHOR C*4 Firm horizon
  FIMHORUOM M*15 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  FLGFAS M*4 Capitalizable [menu 1: 1=No,2=Yes] act:FAS
  FOH C*4 Demand horizon
  FOHUOT M*10 Time unit outside of dem. [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  FRTCLS FRT Freight class -> [FRT]FRT0 =FRTCLS;[V]GSUPCLE (FRTCLS) !Block
  FRTHOR C*4 Planning horizon
  FRTHORUOM M*15 Planning horizon time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  GENFLG M*4 Generic [menu 1: 1=No,2=Yes]
  GLOAAAFLG M*4 Allow A [menu 1: 1=No,2=Yes]
  GLOQQQFLG M*4 Allow Q [menu 1: 1=No,2=Yes]
  GLORRRFLG M*4 Allow R [menu 1: 1=No,2=Yes]
  INTFLG M*4 Maintenance [menu 1: 1=No,2=Yes]
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVPRODTYP M*25 Product type [menu 2051: 1=Goods,2=Raw materials, subsidiaries and consumables,3=Finished and intermediate goods,4=By-products, waste and scrap,5=Products and works in progress,6=Not applicable] act:KPO
  ITMCREMOD M*15 Creation method [menu 223: 1=Direct,2=With validation]
  ITMREFCOU ANM Product sequence -> [ANM]ANM0 =[ITG]ITMREFCOU (ACODNUM) !Block
  ITMSFTTYP M*15 SAF-T product type [menu 2273: 1=None,2=Product,3=Service,4=Other] act:SAFT
  ITMTYP M*20 Type [menu 436: 1=Normal,2=Flexible kit,3=Fixed kit]
  ITMVOU VOL STK volume
  ITMWEI WEI STK weight
  LBEFMT ARP Label format -> [ARP]ARP0 =[ITG]LBEFMT (AREPORT) !Block act:NUC
  LNDFLG M*4 Loan authorized [menu 1: 1=No,2=Yes]
  LOAECCFLG M*4 Version preload [menu 1: 1=No,2=Yes] act:ECC
  LOCDES M*15 Location category [menu 2707: 1=Receipt,2=Stock,3=Picking,4=Workstation,5=Delivery,6=Store,7=Customer return,8=Return from return,9=To be defined,10=To be defined,11=To be defined] act:NDL
  LOCMGTCOD M*4 Location management [menu 1: 1=No,2=Yes]
  LOTCOU ANM Lot sequence number -> [ANM]ANM0 =[ITG]LOTCOU (ACODNUM) !Block
  LOTMGTCOD M*15 Lot management [menu 2711: 1=Not managed,2=Optional lot,3=Mandatory lot,4=Lot and sublot]
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[ITG]MATTOL (MATCHTOL) !Block
  MATWRH DEP WO warehouse act:WRH
  MAXQTY QTY Maximum quantity
  MAXSTO QTY Maximum stock
  MCEFLG M*4 Maintenance [menu 1: 1=No,2=Yes]
  MFGFLG M*4 Manufactured [menu 1: 1=No,2=Yes]
  MFGLOTQTY QTY Technical lot
  MFGSHTCOD M*4 Release if shortage [menu 1: 1=No,2=Yes]
  MFGWRH DEP Cons wareh act:WRH
  MINQTY QTY Minimum quantity
  MINRMNPRC RAT Delivery tolerance %
  NEGSTO M*4 Stock < 0 authorized [menu 1: 1=No,2=Yes]
  NMFC FCC NMFC -> [FCC]FCC0 =1;NMFC (FRTCOMCOD) !Block act:KUS
  OFS LTI Reorder LT
  ORDWRH DEP Order warehouse act:WRH
  OTRSTYP M*15(5) Movement type [menu 704: 35 values, see local-menus.md]
  OVECOD OVE(5) Overhead -> [OVE]OVE0 =[ITG]OVECOD (OVERHEAD) !Block
  OVECPNFLG M*4(5) Include lower level ovrh. [menu 1: 1=No,2=Yes]
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[ITG]PCCCOD (PJMCOSTCTR) !Block act:PJM
  PCK PCK Packaging -> [TPA]TPA0 =[ITG]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCKFLG M*4 Packing [menu 1: 1=No,2=Yes]
  PCKSTKFLG M*4 Stock detail [menu 1: 1=No,2=Yes]
  PCU UOM Packing unit -> [TUN]TUN0 =[ITG]PCU (TABUNIT) !Block act:NUC
  PCURUL M*30 Issuing PAC [menu 2706: 1=Unpack,2=Adjust coefficient (recalc PAC coeff),3=Fraction (calculate decimal PAC)] act:NUC
  PCUSTUCOE COE PAC-STK conv. act:NUC
  PHAFLG M*4 Phantom [menu 1: 1=No,2=Yes]
  PLAACS A*10 Access code
  PLANNER AUS Planner -> [AUS]CODUSR =[ITG]PLANNER (AUTILIS) !Block
  PLH C*4 Firm horizon
  PLHUOT M*10 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  PRQFLG M*4 Mandatory PO request [menu 1: 1=No,2=Yes]
  PTOCOD PTO Rule -> [PTO]PTO0 =[ITG]PTOCOD (PARMTO) !Block
  PURFLG M*4 Bought [menu 1: 1=No,2=Yes]
  PURPRIPRC RAT % applied
  PUU UOM Purchase unit -> [TUN]TUN0 =[ITG]PUU (TABUNIT) !Block
  PUUSTUCOE COE PUR-STK conv.
  QLYCRD QLC Technical sheet -> [QLC]QLC0 =QLYCRD;1 (QLYCRD) !Block
  QUAACS A*10 Access code
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  RCPFLG M*4 Receipt code [menu 1: 1=No,2=Yes]
  REOCOD M*15 Suggestion type [menu 250: 1=No suggestion,2=Purchase,3=Manufacturing,4=Intersite,5=Subcontracting]
  REOFCY FCY Reorder site -> [FCY]FCY0 =[ITG]REOFCY (FACILITY) !Block
  REOMGTCOD M*15 Reorder mode [menu 727: 1=Not managed,2=By MRP,3=By MPS,4=By ROP,5=By period]
  REOMINQTY QTY EOQ
  REOPER C*3 Reorder frequency
  REOPOL RPO Reorder policy -> [TRP]TRP0 =[ITG]REOPOL (TABREOPOL) !Block
  REOTSD QTY Reorder threshold
  SAFSTO QTY Safety stock
  SALFLG M*4 Sold [menu 1: 1=No,2=Yes]
  SALRMNPRC RAT Delivery tolerance %
  SAU UOM Sales unit -> [TUN]TUN0 =[ITG]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SCCWRH DEP Sb-c cons warehouse act:WRH
  SCOWRH DEP Sub-ctrt ship wareh act:WRH
  SCPFLG M*4 Subcontracted [menu 1: 1=No,2=Yes]
  SCSFLG M*4 Subcontract [menu 1: 1=No,2=Yes]
  SERCOU ANM Serial sequence -> [ANM]ANM0 =[ITG]SERCOU (ACODNUM) !Block
  SERMGTCOD M*15 Serial no. management [menu 210: 1=Not managed,2=Issued,3=Received/Issued]
  SESCOD SES Trend profile -> [SES]SES0 =[ITG]SESCOD (SEASON) !Block
  SHIWRH DEP Shipping warehouse act:WRH
  SHR DCB*3.3 Shrinkage percent
  SIMCSTUPD M*15 Simulated cost update [menu 220: 1=Calculated,2=Entered]
  SREWRH DEP Aftr Sales warehouse act:WRH
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  SSU UOM Statistical unit -> [TUN]TUN0 =[ITG]SSU (TABUNIT) !Block
  SSUSTUCOE COE STA-STK conv.
  STCNUM VCR Cost structure
  STDCSTUPD M*15 Standard cost update [menu 220: 1=Calculated,2=Entered]
  STDFLG M*15 Management mode [menu 297: 1=Not managed,2=By project,3=Available stock,4=By order]
  STOCOD M*15 Stock withdrawal mode [menu 217: 1=Immediate,2=Backflush,3=Not managed]
  STOFCY FCY Stock site -> [FCY]FCY0 =[ITG]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[ITG]STU (TABUNIT) !Block
  STULBEFMT ARP Label format -> [ARP]ARP0 =[ITG]STULBEFMT (AREPORT) !Block
  TCLAXX AX3 Description
  TCLCOD A*5 Category
  TCLDES DES Description
  TCLSHO SHO Short description
  TCLSHOAXX AX2 Short description
  TOOFLG M*4 Tools [menu 1: 1=No,2=Yes]
  TRFWRH DEP Internal mvt wareh act:WRH
  TRKCOD M*15 Traceability [menu 754: 1=No traceability,2=Detailed traceability,3=Summary traceability]
  TRKLEV M*15 Traceability level [menu 2778: 1=By default,2=Lot,3=Sub-lot,4=Serial number]
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Block act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VLTCOD TCM Valuation method -> [TCM]TCM0 =[ITG]VLTCOD (TABCOSTMET) !Block
  VOU UOM Volume unit -> [TUN]TUN0 =[ITG]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[ITG]WEU (TABUNIT) !Block

## ITMCOMP (ICM) - Competitor products
Keys (first = PK; D = duplicates allowed): ICM0 NUM
Fields:
  ASE CLX Strengths
  AUUID AUUID Single identifier
  BRA ADI Brand -> [ADI]CODE =415;BRA (ATABDIV) !RTZ
  CPPITMDESAXX AX3 Description
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[ICM]CUR (TABCUR) !RTZ
  DES CLX Description
  NUM VCR Code
  NUMFULASE CLC Chrono txt file
  NUMFULDES CLC Chrono txt file
  NUMFULSHC CLC Chrono txt file
  REF REF Reference
  SALFCY FCY Site -> [FCY]FCY0 =[ICM]SALFCY (FACILITY) !RTZ
  SALPRI MD1 Reported average cost
  SHC CLX Weaknesses
  TTR DES Description
  TYPFULASE CLT Type text file
  TYPFULDES CLT Type text file
  TYPFULSHC CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ITMCOST (ITC) - Products-costs
Keys (first = PK; D = duplicates allowed): ITC0 STOFCY+ITMREF+CSTTYP-ITCSEQ+UID; ITC1 STOFCY+ITMREF+CSTTYP+ITCSTRDAT+ITCSEQ (D); ITC2 STOFCY+ITMREF+CSTTYP+ITCENDDAT+ITCSEQ (D); ITC3 UID+STOFCY+ITMREF+CSTTYP+ITCSTRDAT+ITCENDDAT (D)
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CFGVCRNUM VCR Journal number config act:CFG
  CLCQTY QTY Calculation quantity
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTSEQ C*4 Sequence
  CSTTOT MD8 Total cost
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  DESCEND M*4 Multilevel [menu 1: 1=No,2=Yes]
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  EXPNUM L*8 Export number
  FIYNUM C*2 Fiscal year
  FXDCSTDSP M*15 Fixed costs distribution [menu 323: 1=Pro rata,2=Total]
  FXDLABCST MD8 Fixed labor cost act:LAB
  FXDLABLEV MD8 Fixed labor level C act:LAB
  FXDMACCST MD8 Fixed machine cost act:MAC
  FXDMACLEV MD8 Fixed machine level cost act:MAC
  FXDMATCST MD8 Fixed materials cost act:MAT
  FXDMATLEV MD8 Fixed material level cost act:MAT
  FXDMATLEV0 MD8 Fixed material level cost
  FXDOVELAB MD8 Fixed labor o/head
  FXDOVELABL MD8 Lab fixed OH level
  FXDOVELEV MD8 Fixed overhead level cost
  FXDOVEMAC MD8 Fixed machine overhead cost
  FXDOVEMACL MD8 Mach fixed ohs level
  FXDOVEMAT MD8 Fixed material overhead cost
  FXDOVEMATL MD8 Matl fixed OH level
  FXDOVESCO MD8 Fixed sub-con o/head
  FXDOVESCOL MD8 Sub-con fix OH level
  FXDSCOCST MD8 Fixed subcon cost
  FXDSCOLEV MD8 Fixed subcontract level cost
  ITCDAT D Date calculated
  ITCENDDAT D Validity
  ITCSEQ L*8 Sequence no.
  ITCSTRDAT D Validity
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LABCST MD8 Labor cost act:LAB
  LABLEVCST MD8 Labor level cost act:LAB
  LABTOT MD8 Total labor cost
  MACCST MD8 Machine cost act:MAC
  MACLEVCST MD8 Machine cost level act:MAC
  MACTOT MD8 Total machine
  MATCST MD8 Material cost act:MAT
  MATLEV0 MD8 Material cost level
  MATLEVCST MD8 Material cost level act:MAT
  MATTOT MD8 Total material
  OLDCST MD8 Previous updated std
  OLDDAT D Old date
  OVELABCST MD8 Labor overh
  OVELABLEV MD8 Labor OH level
  OVELEVCST MD8 Overhead cost level
  OVEMACCST MD8 Machine OH cost
  OVEMACLEV MD8 Mach overheads level
  OVEMATCST MD8 Material overhead cost
  OVEMATLEV MD8 Material ohs level
  OVEPRD MD8 OH lev. entry
  OVESCOCST MD8 Subcontract
  OVESCOLEV MD8 Sub-con OH level
  OVETOT MD8 Total overhead
  PHYSTO QTY Physical stock
  PRNUID L*8 Identifier
  ROUALT TRO Routing code -> [TRO]TRO0 =[ITC]ROUALT (TABROUALT) !Block
  SCOCST MD8 Subcontract cost
  SCOLEVCST MD8 Sub-con cost level
  SCOTOT MD8 Total subcontracted
  SLTMATCST M*15 Material cost [menu 328: 1=Standard cost,2=Revised standard cost,3=Budget cost,4=Simulated cost,5=Last cost,6=Average cost,7=Last purchase price,8=List price]
  SLTOVECOL M*15 Overhead column [menu 320: 1=Formula A,2=Formula B,3=Formula C,4=Formula D]
  STOFCY FCY Storage site -> [FCY]FCY0 =[ITC]STOFCY (FACILITY) !Delete
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*4 Update [menu 385: 1=No,2=Deferred,3=Immediate]
  UPDUSR A*5 Change user
  VLTCCERAT M*15 Dimension rate selection [menu 324: 1=Standard,2=Revised standard,3=Budget,4=Simulation]
  VLTTOT MD8 Valuation cost
  YEA C*4 Year

## ITMCPPLNK (ILK) - Competitor/product link
Keys (first = PK; D = duplicates allowed): ILK0 ITMNUM (D); ILK1 ITMCPPNUM (D); ILK2 ITMNUM+ITMCPPNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ILK]CREUSR (AUTILIS) !Other
  ITMCPPNUM CCC Competitor product -> [ICM]ICM0 =[ILK]ITMCPPNUM (ITMCOMP) !Block
  ITMNUM ITM Product code -> [ITM]ITM0 =[ILK]ITMNUM (ITMMASTER) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ILK]UPDUSR (AUTILIS) !Other

## ITMCPTVER (ICV) - Version counter setup
Notes: activity code ECC
Keys (first = PK; D = duplicates allowed): ICV0 ICVCOD
Fields:
  AUUID AUUID Single identifier
  CNS M*4 Constant management [menu 1: 1=No,2=Yes]
  CNSVAL A*9 Constant value
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ICVCOD A*5 Sequence number
  SEQ M*4 Sequence number [menu 1: 1=No,2=Yes]
  SEQBEG A*1 Sequence start
  SEQEND A*1 Sequence end
  SEQLNG C*2 Sequence length
  SEQTYP M*15 Sequence number type [menu 2779: 1=0 to 9,2=a to z,3=A to Z,4=0 to 9 then a to z,5=0 to 9 then A to Z]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ITMCUSNOM (INO) - NC8 product BOM
Keys (first = PK; D = duplicates allowed): INO0 ITMNOM; INO1 ITMCUSSHO (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AXX Description
  EXPNUM L*8 Export number
  ITMCUSDES A*250 Description
  ITMCUSSHO A*30 Alpha sort
  ITMCUSUOM A*12 Additional unit
  ITMNOM INO Code -> [INO]INO0 =[INO]ITMNOM (ITMCUSNOM) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ITMFACILIT (ITF) - Products-sites
Notes: differs in V9.0 P12 (diff: AT3_ITMFACILIT.htm); differs in V10 P1 (diff: ATD_ITMFACILIT.htm)
Keys (first = PK; D = duplicates allowed): ITF0 ITMREF+STOFCY; ITF1 STOFCY+ITMREF
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  AUUID AUUID Single identifier
  BUDCSTUPD M*15 Budgeted std. cost update [menu 220: 1=Calculated,2=Entered]
  BUY AUS Buyer -> [AUS]CODUSR =[ITF]BUY (AUTILIS) !Block
  CFGVCRNUM VCR Journal number config act:CFG
  CLEPCTAUT DCB*3.3 Automatic closing %
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTROU A*20 Cost
  CSTROUALT TRO Code -> [TRO]TRO0 =[ITF]CSTROUALT (TABROUALT) !Block
  CUNCOD M*15 Count mode [menu 216: 1=Cycle count,2=Annual count,3=No count]
  CUNFLG M*4 Blocked for count [menu 1: 1=No,2=Yes]
  CUNLISNUM VCR Count in progress
  CUTCSTUPD M*15 Revised std. cost update [menu 220: 1=Calculated,2=Entered]
  DAYCOV COV Coverage
  DEFLOC EMP Default locations act:NDL
  DEFLOCTYP TEM Default icon type act:NDL
  DLU COE UBD coefficient
  EXCFDMA M*4 FDMA not applicable [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FOH C*4 Demand horizon
  FOHUOT M*10 Time unit outside of dem. [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  FRTCLS FRT Freight class -> [FRT]FRT0 =FRTCLS;[V]GSUPCLE (FRTCLS) !Block
  GENLEVINS M*15 General level [menu 2757: 1=I,2=II,3=III]
  ISM A*8 Storage/Handling act:MWM
  ITMREF ITM Product -> [ITM]ITM0 =[ITF]ITMREF (ITMMASTER) !Block
  ITMTOLNEG COE Weighing tolerance -(%) act:MWM
  ITMTOLPOS COE Weighing tolerance +(%) act:MWM
  LOCMGTCOD M*4 Location management [menu 1: 1=No,2=Yes]
  LOCNUM M*15 Location no. [menu 2707: 1=Receipt,2=Stock,3=Picking,4=Workstation,5=Delivery,6=Store,7=Customer return,8=Return from return,9=To be defined,10=To be defined,11=To be defined] act:NDL
  LTIQLYCRD QLC Recontrol record -> [QLC]QLC0 =LTIQLYCRD;1 (QLYCRD) !Block
  MATWRH DEP WO warehouse act:WRH
  MAXSTO QTY Maximum stock
  MAXSTOCLC QTY Calculated max stock
  MFGLOTQTY QTY Technical lot
  MFGLTI LTI Production lead time
  MFGROU A*20 Production routing
  MFGROUALT TRO Code -> [TRO]TRO0 =[ITF]MFGROUALT (TABROUALT) !Block
  MFGSHTCOD M*4 Release if shortage [menu 1: 1=No,2=Yes]
  MFGWRH DEP Cons wareh act:WRH
  MIC C*3 Reduction factor
  MONPROMON C*2 Last monthly close
  MONPROYEA C*4 Last monthly close
  NEWLTISTA A*1 Recontrol status
  NMFC FCC NMFC -> [FCC]FCC0 =1;NMFC (FRTCOMCOD) !Block act:KUS
  NQA M*15 AQL [menu 2758: 1=1.0,2=1.5,3=2.5,4=4.0,5=6.5,6=10,7=15,8=25,9=40,10=65,11=100,12=0.0]
  OFS LTI Reorder LT
  ORDWRH DEP Order warehouse act:WRH
  OTRSTYP M*15(5) Movement type [menu 704: 35 values, see local-menus.md]
  OVECOD OVE(5) Overhead -> [OVE]OVE0 =[ITF]OVECOD (OVERHEAD) !Block
  OVECPNFLG M*4(5) Include lower level ovrh. [menu 1: 1=No,2=Yes]
  PCK PCK Packaging -> [TPA]TPA0 =[ITF]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCKFLG M*4 Packing [menu 1: 1=No,2=Yes]
  PCKSTKFLG M*4 Stock detail [menu 1: 1=No,2=Yes]
  PJMSTRSTK M*4 Stock for project [menu 1: 1=No,2=Yes] act:PJM
  PLANNER AUS Planner -> [AUS]CODUSR =[ITF]PLANNER (AUTILIS) !Block
  PLH C*4 Firm horizon
  PLHUOT M*10 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  PROPER RAT Prorata qty. adjust.
  PRPLTI LTI Picking
  PTOCOD A*5 Rule
  QLYCRD QLC Technical sheet -> [QLC]QLC0 =QLYCRD;1 (QLYCRD) !Block
  QUAACS A*10 Access code
  QUAADXUID L*8 Process frequency
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUAFRY L*4 Frequency
  QUALTI LTI Quality control
  QUANUM L*4 Number entries
  QUANUMUID L*4 Entries process
  RCCROU A*20 RCCP
  RCCROUALT TRO Code -> [TRO]TRO0 =[ITF]RCCROUALT (TABROUALT) !Block
  REDMODFLG M*15 Method of correction [menu 2377: 1=Lot,2=Allocation] act:MWM
  RELSCATIA M*4 Shrink with release [menu 1: 1=No,2=Yes]
  REOCOD M*15 Suggestion type [menu 250: 1=No suggestion,2=Purchase,3=Manufacturing,4=Intersite,5=Subcontracting]
  REOFCY FCY Reorder site -> [FCY]FCY0 =[ITF]REOFCY (FACILITY) !Block
  REOMGTCOD M*15 Reorder mode [menu 727: 1=Not managed,2=By MRP,3=By MPS,4=By ROP,5=By period]
  REOMINCLC QTY Calculated EOQ
  REOMINQTY QTY EOQ
  REOPER C*3 Reorder frequency
  REOPOL RPO Reorder policy -> [TRP]TRP0 =[ITF]REOPOL (TABREOPOL) !Block
  REOTSD QTY Reorder threshold
  REOTSDCLC QTY Calculated ROP
  SAFSTO QTY Safety stock
  SAFSTOCLC QTY Calculated safety stock
  SCCWRH DEP Sb-c cons warehouse act:WRH
  SCOWRH DEP Sub-ctrt ship wareh act:WRH
  SESCOD SES Trend profile -> [SES]SES0 =[ITF]SESCOD (SEASON) !Block
  SHIWRH DEP Shipping warehouse act:WRH
  SHLLTI C*4 Recontrol lead time
  SHLLTIUOM M*15 Rectrl time unit [menu 2759: 1=Calendar days,2=Month]
  SHR DCB*3.3 Shrinkage percent
  SIMCSTUPD M*15 Simulated cost update [menu 220: 1=Calculated,2=Entered]
  SMPMOD M*15 Sampling mode [menu 2756: 1=Global,2=Lot,3=No management]
  SMPTYP M*15 Sampling [menu 2755: 1=None,2=Single]
  STAFED ADI Region/State -> [ADI]CODE =80;STAFED (ATABDIV) !Block act:DEBR
  STDCSTUPD M*15 Standard cost update [menu 220: 1=Calculated,2=Entered]
  STOCOD M*15 Stock withdrawal mode [menu 217: 1=Immediate,2=Backflush,3=Not managed]
  STOFCY FCY Stock site -> [FCY]FCY0 =[ITF]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  TOTLTI LTI Multilevel
  TRFWRH DEP Internal mvt wareh act:WRH
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VLTCOD TCM Valuation method -> [TCM]TCM0 =[ITF]VLTCOD (TABCOSTMET) !Block
  WGRACS A*10 Access code act:MWM
  WIPPRO M*4 WIP protect. [menu 1: 1=No,2=Yes]
  YEAPROYEA C*4 Last annual close

## ITMMASTER (ITM) - Products
Notes: differs in V9.0 P12 (diff: AT3_ITMMASTER.htm); differs in V10 P1 (diff: ATD_ITMMASTER.htm)
Keys (first = PK; D = duplicates allowed): ITM0 ITMREF; ITM1 ITMDES1 (D); ITM2 SEAKEY+ITMREF; ITM3 CFGLIN+ITMREF; ITM4 CFGVCRNUM+ITMREF; ITM5 PLMITMREF+ITMREF
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =1;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ALG A*20 Allergens act:FOA
  ALGBOM C*2 Allergen BOM code act:FOA
  ALGDAT D Allergen change date act:FOA
  ALTBOMHDK TBO Code -> [TBO]TBO0 =1;ALTBOMHDK (TABBOMALT) !RTZ
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  BUY AUS Buyer -> [AUS]CODUSR =[ITM]BUY (AUTILIS) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFGBPRNUM BPR BP -> [BPR]BPR0 =[ITM]CFGBPRNUM (BPARTNER) !RTZ act:CFG
  CFGBPRREF A*20 BP reference act:CFG
  CFGDELDAT D Config purge date act:CFG
  CFGFLDALP1 A*20 Alpha field 1
  CFGFLDALP2 A*20 Alpha field 2
  CFGFLDALP3 A*20 Alpha field 3
  CFGFLDALP4 A*20 Alpha field 4
  CFGFLDALP5 A*20 Alpha field 5
  CFGFLDALP6 A*20 Alpha field 6
  CFGFLDNUM1 DCB*15 Numeric field 1
  CFGFLDNUM2 DCB*15 Numeric field 2
  CFGFLDNUM3 DCB*15 Numeric field 3
  CFGFLDNUM4 DCB*15 Numeric field 4
  CFGFLDNUM5 DCB*15 Numeric field 5
  CFGFLDNUM6 DCB*15 Numeric field 6
  CFGITMREF ITM Reference product -> [ITM]ITM0 =[ITM]CFGITMREF (ITMMASTER) !Delete act:CFG
  CFGLIN TLP Product line -> [TLP]TLP0 =[ITM]CFGLIN (TABLINCFG) !Block
  CFGVCRNUM VCR Journal number config act:CFG
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CPY CPY Company -> [CPY]CPY0 =[ITM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMAC M*4 Creation of base [menu 1: 1=No,2=Yes]
  CREUSR A*5 Creation user
  CSTGRP A*10 Cost group
  CUSREF INO Customs reference -> [INO]INO0 =[ITM]CUSREF (ITMCUSNOM) !Block act:DEB
  DACPCUCOE M*4 Factor authorized [menu 1: 1=No,2=Yes] act:NUC
  DACPUUCOE M*4 Purchase factor entry [menu 1: 1=No,2=Yes]
  DACSAUCOE M*4 Sales factor entry [menu 1: 1=No,2=Yes]
  DAYUOM UOM Unit for days -> [TUN]TUN0 =[ITM]DAYUOM (TABUNIT) !RTZ
  DEFACT DCB*5.4 Default title
  DEFPOT DCB*5.4 Default potency %
  DES1AXX AX3 Description 1
  DES2AXX AX3 Description 2
  DES3AXX AX3 Description 3
  DIE DIE Dimension type code -> [DIE]DIE0 =[ITM]DIE (GDIE) !Block act:ANA
  DLU COE UBD coefficient
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  DTY COE Density
  EANCOD A*20 UPC code
  ECCBOMALT2 TBO(2) Code -> [TBO]TBO0 =2;ECCBOMALT2(indice) (TABBOMALT) !Block act:ECC
  ECCBOMALT3 TBO(2) Code -> [TBO]TBO0 =3;ECCBOMALT3(indice) (TABBOMALT) !Block act:ECC
  ECCFLG M*4 Version management [menu 1: 1=No,2=Yes] act:ECC
  ECCMAJ ICV Major sequence -> [ICV]ICV0 =[ITM]ECCMAJ (ITMCPTVER) !Block act:ECC
  ECCMIN ICV Minor sequence -> [ICV]ICV0 =[ITM]ECCMIN (ITMCPTVER) !Block act:ECC
  ECCROUALT TRO(2) Routing code -> [TRO]TRO0 =[ITM]ECCROUALT (TABROUALT) !Block act:RVM
  ECCROUFLG M*4 Routing version [menu 1: 1=No,2=Yes] act:RVM
  ECCSTO M*20 Stock version [menu 2777: 1=No,2=Major,3=Major and minor] act:ECC
  EECGES M*4 Sub Intrastat [menu 1: 1=No,2=Yes] act:DEB
  EEU UOM Intrastat additional unit -> [TUN]TUN0 =[ITM]EEU (TABUNIT) !Block
  EEUSTUCOE COE EU-STK conv.
  EXPNUM L*8 Export number
  EXYMGTCOD M*15 Expiration management [menu 211: 1=Not managed,2=Without rounding,3=Rounding month end,4=Rounding beginning month+1,5=Mandatory entry,6=Manual entry]
  EXYSTA A*1 Expiration status
  FIMHOR C*4 Firm horizon
  FIMHORUOM M*15 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  FLGFAS M*4 Capitalizable [menu 1: 1=No,2=Yes] act:FAS
  FLYCAT ADI Voucher category -> [ADI]CODE =450;FLYCAT (ATABDIV) !RTZ
  FRTHOR C*4 Planning horizon
  FRTHORUOM M*15 Planning horizon time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  GENFLG M*4 Generic [menu 1: 1=No,2=Yes]
  HDKITMTYP M*15 Product type [menu 2984: 1=Other,2=Part,3=Labor,4=Expenses,5=Service contract]
  HOUUOM UOM Unit for hour -> [TUN]TUN0 =[ITM]HOUUOM (TABUNIT) !RTZ
  INTFLG M*4 Intermediary [menu 1: 1=No,2=Yes]
  INVPRODTYP M*25 Product type [menu 2051: 1=Goods,2=Raw materials, subsidiaries and consumables,3=Finished and intermediate goods,4=By-products, waste and scrap,5=Products and works in progress,6=Not applicable] act:KPO
  ITMDES1 DES Description 1
  ITMDES2 DES Description 2
  ITMDES3 DES Description 3
  ITMEXNFLG A*1 Exemption flag
  ITMREF ITM Product -> [ITM]ITM0 =[ITM]ITMREF (ITMMASTER) !Delete
  ITMSFTTYP M*15 SAF-T product type [menu 2273: 1=None,2=Product,3=Service,4=Other] act:SAFT
  ITMSTA M*15 Product status [menu 246: 1=Active,2=In development,3=On shortage,4=Not renewed,5=Obsolete,6=Not usable]
  ITMSTD A*20 Standard
  ITMVOU VOL STK volume
  ITMWEI WEI Item weight
  LBEFMT ARP Label format -> [ARP]ARP0 =[ITM]LBEFMT (AREPORT) !Block act:NUC
  LIFENDDAT D Service life end
  LIFSTRDAT D Service life start
  LOAECCFLG M*4 Version preload [menu 1: 1=No,2=Yes] act:ECC
  LOTCOU ANM Lot sequence number -> [ANM]ANM0 =[ITM]LOTCOU (ACODNUM) !Block
  LOTMGTCOD M*15 Lot management [menu 2711: 1=Not managed,2=Optional lot,3=Mandatory lot,4=Lot and sublot]
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[ITM]MATTOL (MATCHTOL) !Block
  MFGFLG M*4 Manufactured [menu 1: 1=No,2=Yes]
  MFGTEX TXC Production text
  MINRMNPRC RAT Delivery tolerance %
  MNTUOM UOM Unit for minutes -> [TUN]TUN0 =[ITM]MNTUOM (TABUNIT) !RTZ
  NEGSTO M*4 Stock < 0 authorized [menu 1: 1=No,2=Yes]
  NEWLTISTA A*1 Recontrol status
  OFS C*4 Reorder LT
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[ITM]PCCCOD (PJMCOSTCTR) !Block act:PJM
  PCU UOM Packing unit -> [TUN]TUN0 =[ITM]PCU (TABUNIT) !Block act:NUC
  PCURUL M*30 Issuing PAC [menu 2706: 1=Unpack,2=Adjust coefficient (recalc PAC coeff),3=Fraction (calculate decimal PAC)] act:NUC
  PCUSTUCOE COE PAC-STK conv. act:NUC
  PHAFLG M*4 Phantom [menu 1: 1=No,2=Yes]
  PITCDT L*8 Tokens to be credited
  PITCDTUOM UOM Credit unit -> [TUN]TUN0 =[ITM]PITCDTUOM (TABUNIT) !RTZ
  PLAACS ACS User access -> [ACS]ACS0 =[ITM]PLAACS (ACCCOD) !Block
  PLANNER AUS Planner -> [AUS]CODUSR =[ITM]PLANNER (AUTILIS) !Block
  PLMATTURL A*250 Linked documents
  PLMHISURL A*250 PLM history
  PLMITMREF PLM PLM product
  PRQFLG M*4 Mandatory PO request [menu 1: 1=No,2=Yes]
  PURBASPRI MD5 Base price
  PURFLG M*4 Bought [menu 1: 1=No,2=Yes]
  PURTEX TXC Purchase text
  PUU UOM Purchase unit -> [TUN]TUN0 =[ITM]PUU (TABUNIT) !Block
  PUUSTUCOE COE PUR-STK conv.
  RCPFLG M*4 Receipt code [menu 1: 1=No,2=Yes]
  RPLITM ITM Alternate product -> [ITM]ITM0 =[ITM]RPLITM (ITMMASTER) !Block
  SALFLG M*4 Sold [menu 1: 1=No,2=Yes]
  SAU UOM Sales unit -> [TUN]TUN0 =[ITM]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SCPFLG M*4 Subcontracted [menu 1: 1=No,2=Yes]
  SCSFLG M*4 Subcontract [menu 1: 1=No,2=Yes]
  SEAKEY A*20 Search key
  SERCOU ANM Serial sequence -> [ANM]ANM0 =[ITM]SERCOU (ACODNUM) !Block
  SERMGTCOD M*15 Serial no. management [menu 210: 1=Not managed,2=Issued,3=Received/Issued]
  SHL C*4 Shelf life
  SHLLTI C*4 Recontrol lead time
  SHLLTIUOM M*15 Rectrl time unit [menu 2759: 1=Calendar days,2=Month]
  SHLUOM M*15 Expir t unit [menu 2759: 1=Calendar days,2=Month]
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  SSU UOM Statistical unit -> [TUN]TUN0 =[ITM]SSU (TABUNIT) !Block
  SSUSTUCOE COE STA-STK conv.
  STAFED ADI Region/State -> [ADI]CODE =80;STAFED (ATABDIV) !Block act:DEBR
  STATAXFLG A*1 Tax flag
  STCNUM VCR Cost structure
  STDFLG M*15 Management mode [menu 297: 1=Not managed,2=By project,3=Available stock,4=By order]
  STOCRD A*8 Storage sheet
  STOISSDEF M*4 Stock issue [menu 1: 1=No,2=Yes]
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[ITM]STU (TABUNIT) !Block
  STULBEFMT ARP Label format -> [ARP]ARP0 =[ITM]STULBEFMT (AREPORT) !Block
  TCLCOD ITG Category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Block
  TOOFLG M*4 Tools [menu 1: 1=No,2=Yes]
  TPLCONGUA COT Warranty contract -> [COT]COT0 =[ITM]TPLCONGUA (CONTTEMPL) !RTZ
  TPLCONLND COT Loan contract -> [COT]COT0 =[ITM]TPLCONLND (CONTTEMPL) !RTZ
  TPLCONSRV COT Service contract -> [COT]COT0 =[ITM]TPLCONSRV (CONTTEMPL) !RTZ
  TRKCOD M*15 Traceability [menu 754: 1=No traceability,2=Detailed traceability,3=Summary traceability]
  TRKLEV M*15 Traceability level [menu 2778: 1=By default,2=Lot,3=Sub-lot,4=Serial number]
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Block act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VOU UOM Volume unit -> [TUN]TUN0 =[ITM]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[ITM]WEU (TABUNIT) !Block

## ITMMVT (ITV) - Product-site totals
Keys (first = PK; D = duplicates allowed): ITV0 ITMREF+STOFCY; ITV1 STOFCY+ITMREF
Fields:
  AINVDTAAVC MD7 Invoicing element act:SPD
  AINVDTACST MD7 Invoicing element act:SPD
  ALABAVC MD7 MAP labor cost act:LABD
  ALABCST MD7 MAP labor cost act:LABD
  AMACAVC MD7 MAP machine cost act:MACD
  AMACCST MD7 MAP machine cost act:MACD
  AMATAVC MD7 MAP material cost act:MATD
  AMATCST MD7 MAP material cost act:MATD
  AOVELABAVC MD7 MAP labor OH act:SPD
  AOVELABCST MD7 MAP labor OH act:SPD
  AOVEMACAVC MD7 MAP machine OH act:SPD
  AOVEMACCST MD7 MAP machine OH act:SPD
  AOVEMATAVC MD7 MAP material OH act:SPD
  AOVEMATCST MD7 MAP material OH act:SPD
  AOVESCOAVC MD7 MAP sub-con OH act:SPD
  AOVESCOCST MD7 MAP sub-con OH act:SPD
  ASCOAVC MD7 MAP sub-con cost act:SPD
  ASCOCST MD7 MAP sub-con cost act:SPD
  AUUID AUUID Single identifier
  AVC MD7 Average cost
  AVCBASAMT MD7 AUC base amount
  AVCBASQTY QTY AUC base quantity
  BPRCTLSTO QTY Loan stock 'Q'
  BPRPHYSTO QTY Loan stock 'A'
  BPRREJSTO QTY Loan stock 'R'
  CFGVCRNUM VCR Journal number config act:CFG
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTLALL QTY Int. allocated 'Q'
  CTLSTO QTY Internal 'Q'
  CUNDAT D(12) Count date
  CUNDIM C*3 Number of lines
  CUNISSMVT L*7 Issues since count
  CUNNBR L*8 No. of counts
  CUNNBREQU L*8 No. of accurate counts
  CUNQTYCLC QTY(12) Expected count quantities
  CUNQTYNEW QTY(12) Actual count quantities
  CUNRCPMVT L*7 Receipts since count
  CUNSTO QTY Stock last count
  DETSHT QTY Detail shortage
  EXPNUM L*8 Export number
  GLOALL QTY Global allocated
  GLOSHT QTY Global shortage
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LASCUNDAT D Last count
  LASCUNLIS VCR Last global list
  LASISSDAT D Last issue date
  LASPURDAT D Last purchase date
  LASPURPRI MD6 Last purchase price
  LASRCPDAT D Last receipt date
  LASRCPPRI MD6 Last receipt cost
  LASREODAT D Last reorder date
  LINVDTACST MD6 Invoicing element act:SPD
  LLABCST MD6 Last price lab cost act:LABD
  LMACCST MD6 Last price mch cost act:MACD
  LMATCST MD6 Last price mat cost act:MATD
  LOVELABCST MD6 Last price lab OH act:SPD
  LOVEMACCST MD6 Last price mch OH act:SPD
  LOVEMATCST MD6 Last price mat OH act:SPD
  LOVESCOCST MD6 Last price sub-con OH act:SPD
  LSCOCST MD6 Last price sub-c cost act:SPD
  NEXCUNDAT D Next count
  ORDSTO QTY On reorder
  PHYALL QTY Int. allocated 'A'
  PHYSTO QTY Internal 'A'
  PLFCTLSTO QTY Dock 'Q'
  PLFPHYSTO QTY Dock 'A'
  PLFREJSTO QTY Dock 'R'
  REJALL QTY Int. allocated 'R'
  REJSTO QTY Internal 'R'
  SALSTO QTY On sales orders
  SCCALL QTY Allocated
  SCCLNDSTO QTY Stock
  SCOCTLALL QTY Alloc. subcon. 'Q'
  SCOCTLSTO QTY Subcon. 'Q'
  SCOPHYALL QTY Alloc. subcon. 'A'
  SCOPHYSTO QTY Subcon. 'A'
  SCOREJALL QTY Alloc. subcon. 'R'
  SCOREJSTO QTY Sub-con stock 'R'
  STOFCY FCY Storage site -> [FCY]FCY0 =[ITV]STOFCY (FACILITY) !Block
  TRAAMT MD7 Amount transfer
  TRASTO QTY Transferred stock
  TRFSTO QTY In-transit stock
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WAISTO QTY Pending issues

## ITMMVTHIS (ITH) - Total product - site history
Keys (first = PK; D = duplicates allowed): ITH0 ITMREF+STOFCY+PERSTR; ITH1 STOFCY+ITMREF+PERSTR
Fields:
  AMTDEV MD1 Variance not absorbed
  AMTDEV2 MD1 Variance not absorbed act:VLT
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FIYNUM C*2 Fiscal year
  ITMREF ITM Product -> [ITM]ITM0 =[ITH]ITMREF (ITMMASTER) !Block
  LASISSDAT D Last issue date
  LASPURDAT D Last purchase date
  LASPURPRI MD6 Last purchase price
  LASRCPDAT D Last receipt date
  LASRCPPRI MD8 Last receipt cost
  LASREODAT D Last reorder date
  MONISSAMT MD1 Period issue amount
  MONISSMVT L*7 Number period issues
  MONISSQTY QTY Period issue quantity
  MONRCPAMT MD1 Period receipts amount
  MONRCPMVT L*7 Number period receipts
  MONRCPQTY QTY Period receipt quantity
  PEREND D Period end
  PERNUM C*2 Period number
  PERSTR D Period start
  STOFCY FCY Storage site -> [FCY]FCY0 =[ITH]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  YEAISSAMT MD1 Annual amt. issued
  YEAISSMVT L*7 No. annual issues
  YEAISSQTY QTY Annual qty. issued
  YEARCPAMT MD1 Annual amt. received
  YEARCPMVT L*7 No. annual receipts
  YEARCPQTY QTY Annual qty. received

## ITMSALES (ITS) - Products - sales
Notes: differs in V9.0 P12 (diff: AT3_ITMSALES.htm); differs in V10 P1 (diff: ATD_ITMSALES.htm)
Keys (first = PK; D = duplicates allowed): ITS0 ITMREF; ITS1 ITMDES1 (D)
Fields:
  AUUID AUUID Single identifier
  BASPRI MD5 Base price
  BASPRIORI M*15 Price origin [menu 2271: 1=Entered,2=Purchase price %]
  CFGVCRNUM VCR Journal number config act:CFG
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTMFLG M*4 Back-to-back order [menu 1: 1=No,2=Yes]
  CTMQTY QTY Direct bk-to-bk qty
  DES1AXX AX3 Description 1
  EXPNUM L*8 Export number
  GUAMON C*2 Warranty (month)
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[ITS]ITMREF (ITMMASTER) !Delete
  ITMTYP M*20 Type [menu 436: 1=Normal,2=Flexible kit,3=Fixed kit]
  ITPTEX TXC Picking text
  ITSTEX TXC Sales text
  LNDFLG M*4 Loan authorized [menu 1: 1=No,2=Yes]
  LOAECCFLG M*4 Version preload [menu 1: 1=No,2=Yes] act:ECC
  MAXQTY QTY Maximum quantity
  MINPFM RAT Minimum margin
  MINPRI MD5 Minimum price
  MINQTY QTY Minimum quantity
  MINRMNPRC RAT Delivery tolerance %
  PCK PCK Packaging -> [TPA]TPA0 =[ITS]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PURPRIPRC RAT % applied
  QTYFOR A*3 Quantity formula
  SBSDAT D Substitution date
  SBSITM ITM Substitution product -> [ITM]ITM0 =[ITS]SBSITM (ITMMASTER) !Block
  THEPRI MD5 Theoretical price
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ITMWRH (ITW) - Products-warehouses
Notes: activity code WRH
Keys (first = PK; D = duplicates allowed): ITW0 ITMREF+WRH; ITW1 WRH+ITMREF
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUNCOD M*15 Count mode [menu 216: 1=Cycle count,2=Annual count,3=No count]
  CUNWRHFLG M*4 Warehouse control [menu 1: 1=No,2=Yes]
  DEFLOC EMP Default locations act:NDL
  DEFLOCTYP TEM Default icon type act:NDL
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[ITW]ITMREF (ITMMASTER) !Block
  LASCUNDAT D Last count
  LASCUNLIS VCR Last global list
  LOCDEFFLG M*4 Default locations [menu 1: 1=No,2=Yes]
  LOCNUM M*15 Location no. [menu 2707: 1=Receipt,2=Stock,3=Picking,4=Workstation,5=Delivery,6=Store,7=Customer return,8=Return from return,9=To be defined,10=To be defined,11=To be defined] act:NDL
  NEXCUNDAT D Next count
  REOTSD QTY Reorder threshold
  REOWRH WRH Warehouse for reorder -> [WRH]WRH0 =[ITW]REOWRH (WAREHOUSE) !Other
  STOFCY FCY Stock site -> [FCY]FCY0 =[ITW]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =[ITW]WRH (WAREHOUSE) !Other

## JOBTYP (JOT) - Standard jobs
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## JOBTYPDEF (JOD) - Job type default values
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## JOBTYPKSA (JSA) - Additional RSA fields
Notes: activity code FKGPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## JSNX3DET (JXD) - JSON-X3 transform map detail
Notes: activity code POCOM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): JXD0 MAPCOD+MAPCODLIN; JXD1 MAPCOD (D); JXD2 JSNPATH (D)
Fields:
  AUUID AUUID Single identifier
  CONFIG A*30 Configure fields
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[JXD]CREUSR (AUTILIS) !Other
  JSNPATH A*200 JSON class path
  JSNPROP A*30 JSON property name
  JSNPROPFMT A*30 JSON property format
  MAPCOD A*20 Mapping code
  MAPCODLIN C*4 Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[JXD]UPDUSR (AUTILIS) !Other
  X3PROPFMT A*30 X3 property format
  X3REPALIAS A*30 X3 alias
  X3REPPATH A*200 X3 rep. class path

## JSNX3HEAD (JXH) - JSON-X3 transformation mapper
Notes: activity code POCOM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): JXH0 MAPCOD; JXH1 JSNCLANAM (D); JXH2 X3REPNAM (D); JXH3 X3REPNAM+X3FACET
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[JXH]CREUSR (AUTILIS) !Other
  DSC A*60 Description
  JSNCLANAM A*50 JSON class name
  JSNKEYFMT A*200 JSON key format
  MAPCOD A*20 Mapping code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[JXH]UPDUSR (AUTILIS) !Other
  X3FACET A*10 X3 facet
  X3KEYFMT A*200 X3 key format
  X3REPNAM A*50 X3 representation

## JSNX3TRAN (JXT) - JSON-X3 transport
Notes: activity code POCOM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): JXT0 MAPCOD; JXT1 JSNCLANAM (D); JXT2 X3REPNAM (D); JXT3 X3REPNAM+X3FACET
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[JXT]CREUSR (AUTILIS) !Other
  DSC A*60 Description
  JSNCLANAM A*50 JSON class name
  JSNCLASIZ L*8(10) JSON class size
  JSNCLASPT A*200(10) JSON class split
  MAPCOD A*20 Mapping code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[JXT]UPDUSR (AUTILIS) !Other
  X3FACET A*10 X3 facet
  X3KEYFMT A*200 X3 key format
  X3MAXREC A*6 Maximum records
  X3REPNAM A*50 X3 representation

## LASTCUSMVT (LCM) - Last customer movements
Keys (first = PK; D = duplicates allowed): LCM0 BPCNUM+IFFTYP+CPY
Fields:
  AMT MD1 Amount
  AUUID AUUID Single identifier
  BPCNUM BPR BP of movement -> [BPR]BPR0 =[LCM]BPCNUM (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[LCM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[LCM]CUR (TABCUR) !Block
  IFFFCY FCY Site information -> [FCY]FCY0 =[LCM]IFFFCY (FACILITY) !Block
  IFFTYP M*20 Innformation type [menu 2213: 20 values, see local-menus.md]
  MVTDAT D Movement date
  MVTTYP M*20 Movement type [menu 2214: 1=Quote,2=Order,3=Delivery,4=Return,5=Invoice,6=Service contract,7=Service request,8=Service response,9=Project,10=Payment,11=Payment due,12=Reminder,13=Without type (task),14=Telephone,15=Visit]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Order no.

## LASTSUPMVT (LSM) - Last supplier movements
Keys (first = PK; D = duplicates allowed): LSM0 BPSNUM+IFFTYP+CPY
Fields:
  AMT MD1 Amount
  AUUID AUUID Single identifier
  BPSNUM BPR BP of movement -> [BPR]BPR0 =[LSM]BPSNUM (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[LSM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[LSM]CUR (TABCUR) !Block
  IFFFCY FCY Site information -> [FCY]FCY0 =[LSM]IFFFCY (FACILITY) !Block
  IFFTYP M*20 Innformation type [menu 565: 1=Last call for tenders,2=Last purchase request,3=Last order,4=Last receipt,5=Last return,6=Last invoice,7=Last credit memo,8=Last payment]
  MVTDAT D Movement date
  MVTTYP M*20 Movement type [menu 566: 1=Call for tenders,2=Purchase request,3=Order,4=Receipt,5=Return,6=Invoice,7=Payment]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Order no.

## MACHINES (MAC) - Installed base
Notes: differs in V9.0 P12 (diff: AT3_MACHINES.htm); differs in V10 P1 (diff: ATD_MACHINES.htm)
Keys (first = PK; D = duplicates allowed): MAC0 MACNUM; MAC1 BPCNUM+CCNNUM (D); MAC2 BPCNUM (D); MAC3 CCNNUM (D); MAC5 MACPDTCOD+MACSERNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPCNUM BPR BP code -> [BPR]BPR0 =[MAC]BPCNUM (BPARTNER) !Block
  CCNNUM AIN Contact (rel.) code -> [AIN]AIN0 =[MAC]CCNNUM (CONTACTCRM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Sales currency -> [TCU]TCU0 =[MAC]CUR (TABCUR) !Block
  FCYITN ADR Installation site
  MACBPCCUR CUR Purchase currency -> [TCU]TCU0 =[MAC]MACBPCCUR (TABCUR) !Block
  MACBPCDAT D Purchase date
  MACBPCPRI MD1 Purchase price
  MACBRA ADI Brand -> [ADI]CODE =408;MACBRA (ATABDIV) !Block
  MACBRACLA DES Mark clearly
  MACCUTBPC BPR End user -> [BPR]BPR0 =[MAC]MACCUTBPC (BPARTNER) !Block
  MACDES DES Description
  MACITNDAT D Installation date
  MACITNLND M*4 Installed as a loan [menu 1: 1=No,2=Yes]
  MACITNTYP M*15 Installation type [menu 2972: 1=End user,2=Reseller,3=Wholesaler,4=In stock,5=Rejected]
  MACITSDAT D In service date
  MACNUM VCR Sequence no.
  MACORI M*15 Source [menu 2971: 1=Manual creation,2=Split,3=Shipment validation,4=Invoice validation,5=Warranty request,6=Manual modification of the installation,7=Sales return,8=Loan return]
  MACORIVCR VCR Original document no.
  MACORIVCRL L*8 Source document line
  MACPDTCOD ITM Product code -> [ITM]ITM0 =[MAC]MACPDTCOD (ITMMASTER) !Block
  MACPURDAT D Sales date
  MACQTY L*8 Quantity
  MACRSL BPR Reseller -> [BPR]BPR0 =[MAC]MACRSL (BPARTNER) !Block
  MACSALPRI MD1 Sale price
  MACSERNUM SE1 Serial number
  PLE CLX Location
  PREORI M*15 Source [menu 2971: 1=Manual creation,2=Split,3=Shipment validation,4=Invoice validation,5=Warranty request,6=Manual modification of the installation,7=Sales return,8=Loan return]
  PREORIVCR VCR Original document no.
  PREORIVCRL L*8 Source document line
  SALFCY FCY Sales site -> [FCY]FCY0 =[MAC]SALFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MACITN (MAI) - Machine installations
Keys (first = PK; D = duplicates allowed): MAI0 MACNUM (D); MAI1 MACNUM+CLSNUM (D); MAI2 BPCTYP+BPC (D)
Fields:
  AUUID AUUID Single identifier
  BPC BPR End user -> [BPR]BPR0 =[MAI]BPC (BPARTNER) !Block
  BPCCUR CUR Purchase currency -> [TCU]TCU0 =[MAI]BPCCUR (TABCUR) !Block
  BPCDAT D Purchase date
  BPCPRI MD1 Purchase price
  BPCTYP A*3 EU type
  CLSNUM L*8 Sequence no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MAI]CREUSR (AUTILIS) !Other
  CUR CUR Sales currency -> [TCU]TCU0 =[MAI]CUR (TABCUR) !Block
  ENDITN D Date of recovery
  ITNDAT D Installation date
  ITNFCY ADR Installation site
  ITNTYP M*15 Installation type [menu 2972: 1=End user,2=Reseller,3=Wholesaler,4=In stock,5=Rejected]
  LND M*4 Loan [menu 1: 1=No,2=Yes]
  MACNUM MAC Machine code -> [MAC]MAC0 =[MAI]MACNUM (MACHINES) !RTZ
  ORI M*15 Source [menu 2971: 1=Manual creation,2=Split,3=Shipment validation,4=Invoice validation,5=Warranty request,6=Manual modification of the installation,7=Sales return,8=Loan return]
  ORIVCR VCR Original document
  ORIVCRL L*8 Origin line
  PLE A*230 Location
  PURDAT D Sales date
  RSL BPR Reseller -> [BPR]BPR0 =[MAI]RSL (BPARTNER) !Block
  SALPRI MD1 Sale price
  SECCUR CUR Currency of recovery -> [TCU]TCU0 =[MAI]SECCUR (TABCUR) !Block
  SECPRI MD1 Recovery price
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MAI]UPDUSR (AUTILIS) !Other

## MACWARREQ (MWR) - Warranty request archive
Keys (first = PK; D = duplicates allowed): MWR0 MACNUM (D)
Fields:
  AUUID AUUID Single identifier
  CONNUM CON Warranty contract -> [CON]CON0 =[MWR]CONNUM (CONTSERV) !Block
  CREDAT D Create request
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MWR]CREUSR (AUTILIS) !Other
  MACNUM MAC Base number -> [MAC]MAC0 =[MWR]MACNUM (MACHINES) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MWR]UPDUSR (AUTILIS) !Other
  WRENUM RQW Warranty request -> [RQW]RQW0 =[MWR]WRENUM (WARREQUEST) !Block

## MAILING (OMM) - Mass mailing
Keys (first = PK; D = duplicates allowed): OMM0 OMMNUM; OMM1 CMGNUM (D); OMM2 CREDAT (D)
Fields:
  AUUID AUUID Single identifier
  BUD MD1 Established budget
  CLO M*4 Closed [menu 1: 1=No,2=Yes]
  CLODAT D Closing date
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[OMM]CMGNUM (CMARKETING) !Block
  CNTTTR A*75 Generic title
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHIS M*4 Create history [menu 1: 1=No,2=Yes]
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OMM]CUR (TABCUR) !Block
  DEFADD M*15 Address assignment [menu 965: 1=By Business Partner,2=By Contact]
  DES DCO Description
  EMAOBC A*90 E-mail object
  EMATEX CLX E-mail text
  FCY FCY Site -> [FCY]FCY0 =[OMM]FCY (FACILITY) !Block
  HIEBPR M*4 BP/contact empty [menu 1: 1=No,2=Yes]
  NBQSND L*8 Number of mailings
  NUMFULOBJ CLC Chrono txt file
  OBJ CLX Objective
  OBJFLG C*2 Flag text file
  OMMNUM VCR Mail code
  SHIDAT D Ship date
  SHIMOD M*15 Shipment method [menu 963: 1=Post,2=E-Mail,3=Fax,4=XML]
  SHISTA M*15 Shipment status [menu 968: 1=Successful termination,2=Waiting Dispatch]
  TPL A*50 Template
  TYPFULOBJ CLT Type text file
  TYPMRG M*15 Merging [menu 2967: 1=Use Seagate Crystal Report,2=Use Microsoft Word,3=Generated on the client machine,4=Generated on the server]
  TYPSEA AOB Sample type -> [AOB]ABREV =[OMM]TYPSEA (AOBJET) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MAILXML (MXL) - Mass mailing XML
Keys (first = PK; D = duplicates allowed): MXL0 NUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  MXLDESAX3 AX3 Long title
  MXLSHOAX1 AX1 Short description
  NUM VCR Name
  REPFNCFLG M*4 Extraction function [menu 1: 1=No,2=Yes]
  ROT A*10 Object XML
  SRT A*15 Order attribute
  TTR A*15 Generic title
  TYP M*15 Type [menu 3021: 1=BPs,2=Contacts]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MAILXMLD (MXD) - Mass mailing lines XML
Keys (first = PK; D = duplicates allowed): MXD0 NUM+TAB+FIE
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MXD]CREUSR (AUTILIS) !Other
  FIE AVA Field
  LBEXML DES XML tag
  NUM VCR Name
  TAB ATB Table -> [ATB]CODFIC =[MXD]TAB (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MXD]UPDUSR (AUTILIS) !Other

## MANDATE (MDT) - Mandates
Notes: activity code SDD
Keys (first = PK; D = duplicates allowed): MDT0 CPY+UMRNUM; MDT1 CPY+BPCNUM+UMRNUM
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[MDT]ACS (ACCCOD) !RTZ
  AMDFLG M*4 Amendment flag [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BICCOD A*11 BIC code act:VII
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[MDT]BIDCRY (TABCOUNTRY) !Block
  BIDNUM BID Bank acct. number
  BPCADD ADR Customer address code
  BPCNUM BPR Customer code -> [BPR]BPR0 =[MDT]BPCNUM (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[MDT]CPY (COMPANY) !Delete
  CPYADD ADR Company address code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[MDT]CREUSR (AUTILIS) !Other
  DES DES Description
  ENDDAT D Mandate end date
  FNLDBT A*35 Final debtor
  FNLFLG M*4 Final [menu 1: 1=No,2=Yes]
  IBACOD A*34 IBAN code
  IBAN A*4 IBAN pref
  MAIMDTFLG M*4 Main mandate [menu 1: 1=No,2=Yes]
  MDTCOP AC0*1 Copy of the mandate
  MIGFLG M*4 Migration [menu 1: 1=No,2=Yes]
  NBRSDDPAY C*4 Number of payments
  NDAIMPFLG M*4 SMNDA or IBAN [menu 1: 1=No,2=Yes]
  NTLMIGIDT A*28 Migration national ID
  PAYNBR C*4 No. of direct debits
  PAYTYP M*15 Payment type [menu 3630: 1=Recurring,2=One-off]
  SIGCTY CTY Signature place
  SIGDAT D Signature date
  SITFNC A*35 Signatory function
  SITNAM A*35 Signatory name
  STA M*1 Status [menu 3631: 1=Initial,2=Approved,3=Adjourned,4=Revoked,5=Expired,6=Closed]
  TOTSDDPAY MD1 Total direct debits
  TYP M*15 Type [menu 3629: 1=CORE,2=B2B,3=COR1]
  UDLCON A*35 Underlying contract
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[MDT]UPDUSR (AUTILIS) !Other
  WIOFIRSEQ M*4 Without first seq [menu 1: 1=No,2=Yes]

## MATCSTW (MAW) - Material calculation
Keys (first = PK; D = duplicates allowed): MAW0 MAWUID+STOFCY+ITMREF+ECCVALMAJ+ECCVALMIN+CPNTYP
Fields:
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTUPD M*15 Update code [menu 220: 1=Calculated,2=Entered]
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  FXDMATOVE MS1 Fix mat o/h
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  LLC C*2 Lowest level code
  MATOVE MS1 Overhead
  MATPRI MS1 Price
  MATQTYSSE QTY Quantity sub-group
  MATQTYTOP QTY Quantity under FP
  MAWUID L*8 Process no.
  OVECOD A*3 Overhead
  ROUOPE OPE Operation
  STOFCY FCY Storage site -> [FCY]FCY0 =[MAW]STOFCY (FACILITY) !Delete
  STU UOM Stock unit -> [TUN]TUN0 =[MAW]STU (TABUNIT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MAW]UPDUSR (AUTILIS) !Other

## MEAEMP (MEA) - Monthly employer certificate
Notes: activity code FINTM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## MEDIA (OMN) - Media campaign
Keys (first = PK; D = duplicates allowed): OMN0 OMNNUM; OMN1 CMGNUM (D)
Fields:
  AUUID AUUID Single identifier
  BUD MD1 Budget
  CLO M*4 Closed [menu 1: 1=No,2=Yes]
  CLODAT D Closing date
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[OMN]CMGNUM (CMARKETING) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OMN]CUR (TABCUR) !Block
  DES DCO Description
  DTB L*8 Circulation
  FCY FCY Site -> [FCY]FCY0 =[OMN]FCY (FACILITY) !Block
  MED ADI Media -> [ADI]CODE =426;MED (ATABDIV) !Block
  NUMFULOBJ CLC Chrono txt file
  OBJ CLX Objective
  OBJFLG C*2 Flag text file
  OMNEND D End
  OMNNUM VCR Code
  OMNSTR D Start
  TYPFULOBJ CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MEDWRK (MEW) - Occupational health
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## MEMFOR (FOG) - Memos
Keys (first = PK; D = duplicates allowed): FOG0 CODMSK+CODZON+USR+FORCOD
Fields:
  AUUID AUUID Single identifier
  CODMSK AMK Screen code -> [AMK]CODMSK =[FOG]CODMSK (AMSK) !Delete
  CODZON AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FOG]CREUSR (AUTILIS) !Other
  FORCOD FOR Formula code -> [TFO]TFO0 =FORTYP;FORCOD (TABFOR) !Delete
  FORTYP M*15 Formula type [menu 213: 56 values, see local-menus.md]
  GLOB M*4 Global [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FOG]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[FOG]USR (AUTILIS) !Delete
  VALDEF M*4 Default value [menu 1: 1=No,2=Yes]

## MFCDETPRT (MCP) - Material detail
Keys (first = PK; D = duplicates allowed): MCP0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP1+MFCTYP2+UID+CURUID+BRDCOD+TYPCST
Fields:
  AUUID AUUID Single identifier
  BRDCOD C*4 Cost group
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MCP]CREUSR (AUTILIS) !Other
  CST MD8 Cost
  CST2 MD8 Cost
  CURUID L*8 Process
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  MATREF ITM Component -> [ITM]ITM0 =[MCP]MATREF (ITMMASTER) !Block
  MFCTYP1 M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  MFCTYP2 M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  SCOFLG M*30 Sub-con to deliver [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SCPCST MD8 Reject
  STOFCY FCY Storage site -> [FCY]FCY0 =[MCP]STOFCY (FACILITY) !Block
  TYPCST M*15 Cost type [menu 319: 1=Material,2=Machine,3=Labor,4=Subcontracting,5=Overhead costs,6=Calculated cost]
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MCP]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## MFCMAT (MCC) - Material detail
Keys (first = PK; D = duplicates allowed): MCC0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP+MATREF+ECCVALMAJ+ECCVALMIN+UID
Fields:
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Costing mode [menu 480: 1=Standard cost,2=Updated standard price,3=Last cost,4=Moving average cost,5=FIFO cost,6=Average lot cost,7=Order cost,8=LIFO cost,9=Primary issue method,10=Secondary issue method,11=Simulated cost,12=Simulated price]
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  EXPNUM L*8 Export number
  INVDTACST MD8 Invoicing element act:SPD
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LABCST MD8 Labor cost act:LAB
  MACCST MD8 Machine cost act:MAC
  MATCST MD8 Material cost act:MAT
  MATREF ITM Component -> [ITM]ITM0 =[MCC]MATREF (ITMMASTER) !Block
  MFCTYP M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  OVELABCST MD8 Labor overh
  OVEMACCST MD8 Machine OH cost
  OVEMATCST MD8 Material overhead cost
  OVESCOCST MD8 Subcontract
  QTYSTU QTY STK quantity
  SCOCST MD8 Subcontract cost
  SCOFLG M*30 Sub-con to deliver [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  STOFCY FCY Storage site -> [FCY]FCY0 =[MCC]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[MCC]STU (TABUNIT) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VLTTOT MD8 Total cost
  YEA C*4 Year

## MFCNAT (MCN) - Nature detail - PC
Keys (first = PK; D = duplicates allowed): MCN0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP+OVENAT+UID
Fields:
  AUUID AUUID Single identifier
  CPLQTY QTY Total completed qty.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LEV M*4 Parent product level [menu 1: 1=No,2=Yes]
  MFCDAT D Date calculated
  MFCTYP M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  NATAMTLEV MD8(7) Level amount
  NATAMTSSE MD8(7) Sub-level amount
  OVENAT ONA Overhead cat. -> [ONA]ONA0 =[MCN]OVENAT (OVENAT) !Block
  SLTOVECOL M*15 Overhead column choice [menu 320: 1=Formula A,2=Formula B,3=Formula C,4=Formula D]
  STOFCY FCY Storage site -> [FCY]FCY0 =[MCN]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  YEA C*4 Year

## MFCTYPREL (MTR) - Cost comparison
Keys (first = PK; D = duplicates allowed): MTR0 UID+MFCTYP
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MTR]CREUSR (AUTILIS) !Other
  MFCTYP M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  MFCTYP1 M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  MFCTYP2 M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MTR]UPDUSR (AUTILIS) !Other

## MFCWST (MCW) - Operation detail
Notes: differs in V9.0 P12 (diff: AT3_MFCWST.htm)
Keys (first = PK; D = duplicates allowed): MCW0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP+WST+SCOITMREF+UID
Fields:
  AMTSCO MS1 Amount
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 325: 20 values, see local-menus.md]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Costing mode [menu 480: 1=Standard cost,2=Updated standard price,3=Last cost,4=Moving average cost,5=FIFO cost,6=Average lot cost,7=Order cost,8=LIFO cost,9=Primary issue method,10=Secondary issue method,11=Simulated cost,12=Simulated price]
  EXPNUM L*8 Export number
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  MFCTYP M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  OPEAMT MS1 Operation amount
  OPECST DCB*9.2 Hourly rate
  OPETIM TIH Run time
  OVEAMT MS1 Overhead
  PRISCO MD8 Price
  QTY QTY Quantity
  RATCOD M*15 Dimension rate selection [menu 324: 1=Standard,2=Revised standard,3=Budget,4=Simulation]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[MCW]SCOITMREF (ITMMASTER) !Block
  SETAMT MS1 Adjustment amount
  SETCST DCB*9.2 Hourly rate
  SETTIM TIH Setup time
  STOFCY FCY Storage site -> [FCY]FCY0 =[MCW]STOFCY (FACILITY) !Block
  UID L*8 Process
  UOM UOM Unit -> [TUN]TUN0 =[MCW]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WCSTTYP M*15 Rate type [menu 314: 1=Unit,2=Fixed]
  WST WST Work center
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]
  YEA C*4 Year

## MFGCOST (MFC) - Cost price
Notes: differs in V9.0 P12 (diff: AT3_MFGCOST.htm); differs in V10 P1 (diff: ATD_MFGCOST.htm)
Keys (first = PK; D = duplicates allowed): MFC0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP+UID; MFC1 VCRTYP+VCRNUM+VCRLIN (D)
Fields:
  ANAFLG M*4 IAA update [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BPSMATCST MD8 Supp material cost act:MAT
  CPLRIO DCB*5.2 Ratio
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTTOT MD8 Total cost
  EXPNUM L*8 Export number
  INVDTACPN MD8 Invoicing element
  INVDTACST MD8 Invoicing element act:SPD
  INVDTATOT MD8 Invoicing element
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LABCPNCST MD8 Component labor cst act:LAB
  LABCST MD8 Labor cost act:LAB
  LABTOT MD8 Total labor cost
  MACCPNCST MD8 Component machine cost act:MAC
  MACCST MD8 Machine cost act:MAC
  MACTOT MD8 Total machine
  MATCPNCST MD8 Component material costs act:MAT
  MATCST MD8 Material cost act:MAT
  MATLEV0 MD8 Material cost level
  MATTOT MD8 Total material
  MFCDAT D Date calculated
  MFCSEMBRD M*4 SF/PC breakdown [menu 1: 1=No,2=Yes]
  MFCTYP M*20 Expected cost [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  OVECPNCST MD8 Component overhead cost
  OVELABCPN MD8 Cost level OH lab
  OVELABCST MD8 Labor overh
  OVEMACCPN MD8 Cost level OH mch
  OVEMACCST MD8 Machine OH cost
  OVEMATCPN MD8 Cost level OH mat
  OVEMATCST MD8 Material overhead cost
  OVESCOCPN MD8 Cost level OH sub-con
  OVESCOCST MD8 Subcontract
  OVETOT MD8 Total overhead
  PJT PJT Project -> [PIM]PIM0 =[MFC]PJT (PIMPL) !Block
  PRNUID L*8 Identifier
  QTYSTU QTY STK quantity
  ROUALT TRO Routing code -> [TRO]TRO0 =[MFC]ROUALT (TABROUALT) !Block
  SCOCPNCST MD8 Component sub-contract cost
  SCOCST MD8 Subcontract cost
  SCOTOT MD8 Total subcontracted
  SLTMATCST M*15 Material cost selection [menu 329: 1=Standard cost,2=Revised standard cost,3=Last cost,4=Average cost,5=Transaction cost]
  SLTOVECOL M*15 Overhead column [menu 320: 1=Formula A,2=Formula B,3=Formula C,4=Formula D]
  SLTSEMCST M*15 Semifinished cost selection [menu 329: 1=Standard cost,2=Revised standard cost,3=Last cost,4=Average cost,5=Transaction cost]
  STOFCY FCY Storage site -> [FCY]FCY0 =[MFC]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VLTCCERAT M*15 Dimension rate selection [menu 324: 1=Standard,2=Revised standard,3=Budget,4=Simulation]
  WIPCLE MS1 WIP balance
  YEA C*4 Year

## MFGWIP (MWH) - WIP valuation - header
Keys (first = PK; D = duplicates allowed): MWH0 VCRTYP+VCRNUM; MWH1 TRKTYP+STRDAT (D)
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CPLQTY QTY Total completed qty.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D End date
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[MWH]ITMREF (ITMMASTER) !Block
  MATLEVFLG M*4 Material cost level [menu 1: 1=No,2=Yes]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MWH]MFGFCY (FACILITY) !Block
  MFGTRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  QUACPLQTY QTY Actual QC quantity
  REJCPLQTY QTY Actual rejected qty.
  ROUALT TRO Routing code -> [TRO]TRO0 =[MWH]ROUALT (TABROUALT) !Block
  ROUNUM ROH Released routing -> [ROH]ROH0 =ROUNUM;ROUALT;MFGFCY (ROUTING) !Block
  STRDAT D Start date
  STU UOM Stock unit -> [TUN]TUN0 =[MWH]STU (TABUNIT) !Block
  TRKFIRST D First tracking date
  TRKLAST D Last tracking date
  TRKTYP M*20 Tracking type [menu 399: 1=Work order,2=Product,3=Miscellaneous]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WST WST Work center

## MGTATCUD (ATCUD) - ATCUD management
Notes: activity code KPO; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): ATCUD0 CPY+CODNUM+SEQ
Fields:
  ATCUD A*100 ATCUD
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[ATCUD]CODNUM (ACODNUM) !Block
  CPY CPY Company -> [CPY]CPY0 =[ATCUD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATCUD]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  SAFTINVTYP A*4 SAF-T document type
  SEQ A*20 Series
  TYP A*5 Document type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATCUD]UPDUSR (AUTILIS) !Other
  USED M*4 Used [menu 1: 1=No,2=Yes]
  VAL1 DCB*12 Next value

## MGTWASTE (MGTW) - Waste management
Notes: activity code KPO; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): MGTW1 COD
Fields:
  AUUID AUUID Single identifier
  COD MGTW Code -> [MGTW]MGTW1 =[MGTW]COD (MGTWASTE) !Block
  CPYNAM A*250 Company
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MGTW]CREUSR (AUTILIS) !Other
  TYPWAS A*250 Type of waste
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MGTW]UPDUSR (AUTILIS) !Other
  WEBSITE A*250 Website

## MISSION (MIS) - Role
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## MMSDEFVAL (MMV) - MMS default values
Keys (first = PK; D = duplicates allowed): MMV0 ID+CODFIC+CODZONE
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[MMV]CODFIC (ATABLE) !Delete
  CODZONE AVA Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  ID A*10 Identifier
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VALDEF A*80 Default value

## MMSPAR (MMS) - MMS setup
Keys (first = PK; D = duplicates allowed): MMS0 ID
Fields:
  AUUID AUUID Single identifier
  BPSFOR FOR Selection formula -> [TFO]TFO0 =41;ITMFOR (TABFOR) !Block
  BPSPIT PIT Suppliers -> [PIT]PIT0 =BPSPIT (PIVOTS) !Block
  CCEPIT PIT Analytical dimensions -> [PIT]PIT0 =CCEPIT (PIVOTS) !Block
  CLSBPSPIT PIT Supp. classification -> [PIT]PIT0 =CLSBPSPIT (PIVOTS) !Block
  CNTBPSPIT PIT Supplier contact -> [PIT]PIT0 =CNTBPSPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DIE DIE Dimension type -> [DIE]DIE0 =DIE (GDIE) !Block
  DIEIMP DIE Dimension type -> [DIE]DIE0 =DIE (GDIE) !Block
  DRTSTO A*250 Storage directory
  DRTWRK A*250 Work directory
  FCYPIT PIT Storage site -> [PIT]PIT0 =FCYPIT (PIVOTS) !Block
  ID A*10 Identifier
  INTIT DES Description
  ITMBPSPIT PIT Supplier product -> [PIT]PIT0 =ITMBPSPIT (PIVOTS) !Block
  ITMFOR FOR Selection formula -> [TFO]TFO0 =41;ITMFOR (TABFOR) !Block
  ITMPIT PIT Products -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  ITVPIT PIT Product-site stock -> [PIT]PIT0 =ITVPIT (PIVOTS) !Block
  MVTPIT PIT Movements -> [PIT]PIT0 =MVTPIT (PIVOTS) !Block
  PJTPIT PIT Projects -> [PIT]PIT0 =PJTPIT (PIVOTS) !Block
  PSHPIT PIT Purchase requests -> [PIT]PIT0 =PSHPIT (PIVOTS) !Block
  STAPSHPIT PIT Status of requests -> [PIT]PIT0 =STAPSHPIT (PIVOTS) !Block
  STJMMSFLG M*4 With MMS movement [menu 1: 1=No,2=Yes]
  STJPIT PIT Stock journal -> [PIT]PIT0 =STJPIT (PIVOTS) !Block
  STUPIT PIT Units of measure -> [PIT]PIT0 =STUPIT (PIVOTS) !Block
  TCOPIT PIT UOM conversion -> [PIT]PIT0 =TCOPIT (PIVOTS) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRPIT PIT Users -> [PIT]PIT0 =USRPIT (PIVOTS) !Block
  VOLFILSTO ASTO*250 Storage directory
  VOLFILWRK ASTO*250 Work directory

## MOTENT (MOE) - Arrival reason
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## MTOHEAD (MTO) - MTO network
Notes: differs in V9.0 P12 (diff: AT3_MTOHEAD.htm)
Keys (first = PK; D = duplicates allowed): MTO0 MTOREF
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D End date
  EXPNUM L*8 Export number
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  MTODES DES Description
  MTOREF VCR MTO network
  MTOSHO SHO Short description
  PJT PJT Project -> [PIM]PIM0 =PJT (PIMPL) !RTZ
  STRDAT D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## MTOLINK (MLK) - Demand/resource assignments
Keys (first = PK; D = duplicates allowed): MLK0 STOFCY+ITMREF+DEMTYP+DEMNUM+DEMLIN+DEMSEQ (D); MLK1 STOFCY+ITMREF+RESSTYP+RESSNUM+RESSLIN+RESSSEQ (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEMLIN L*8 Demand line
  DEMNUM VCR Demand journal
  DEMSEQ L*8 Demand sequence
  DEMTYP M*15 Request type [menu 701: 40 values, see local-menus.md]
  DWIPSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  DWIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]
  EXPNUM L*8 Export number
  FMIFLG M*4 Back-to-back order [menu 1: 1=No,2=Yes]
  FRCFLG M*4 Forced [menu 1: 1=No,2=Yes]
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LIKQTY QTY Quantity assigned
  MTOREF MTO MTO network -> [MTO]MTO0 =MTOREF (MTOHEAD) !RTZ
  RESSLIN L*8 Resouce line
  RESSNUM VCR Resource document
  RESSSEQ L*8 Resource sequence
  RESSTYP M*15 Resource type [menu 701: 40 values, see local-menus.md]
  RWIPSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  RWIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]
  STOFCY FCY Storage site -> [FCY]FCY0 =[MLK]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## NOTCATEG (NTG) - Note category
Keys (first = PK; D = duplicates allowed): NTG0 NTGTYP+NTGCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FIE M*3(20) Include [menu 1: 1=No,2=Yes]
  NTGCOD NTG Category -> [NTG]NTG0 =[NTG]NTGCOD (NOTCATEG) !BSRA
  NTGDESAXX AX3 Description
  NTGSHOAXX AX1 Short description
  NTGTYP M*15 Note type [menu 2087: 1=Product,2=Customer,3=Supplier]
  PLAACS A*10 User access
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRTYP M*15(20) Function [menu 2088: 26 values, see local-menus.md]

## NOTE (NTS) - Notes
Keys (first = PK; D = duplicates allowed): NTS0 CODE+NTSCOD2
Fields:
  AUTODISP M*4 Auto display [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPCNUM BPR Customer -> [BPR]BPR0 =[NTS]BPCNUM (BPARTNER) !Delete
  BPSNUM BPR Supplier -> [BPR]BPR0 =[NTS]BPSNUM (BPARTNER) !Delete
  CODE VCR Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EFFDAT D Effective date
  ENDDAT D Expiration date
  ITMREF ITM Product -> [ITM]ITM0 =[NTS]ITMREF (ITMMASTER) !Delete
  NOTE ACB Note
  NTGCOD NTG Category -> [NTG]NTG0 =NTGTYP;NTGCOD (NOTCATEG) !Block
  NTGTYP M*15 Note type [menu 2087: 1=Product,2=Customer,3=Supplier]
  NTSCOD A*10 Note
  NTSCOD2 A*100 Key
  NTSDESAXX AX3 Description
  NTSSHOAXX AX1 Short description
  PRIORITY M*4 Priority [menu 1: 1=No,2=Yes]
  STOFCY FCY Site -> [FCY]FCY0 =[NTS]STOFCY (FACILITY) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## NUMCAI (NCA) - CAI assignment
Notes: activity code KAG; differs in V9.0 P12 (diff: AT3_NUMCAI.htm); differs in V10 P1 (diff: ATD_NUMCAI.htm)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## OBJECTIFBI (OBI) - BI objectives
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## OPPOR (OPP) - Project
Notes: differs in V9.0 P12 (diff: AT3_OPPOR.htm); differs in V10 P1 (diff: ATD_OPPOR.htm)
Keys (first = PK; D = duplicates allowed): OPP0 OPPNUM; OPP1 OPPCDA (D); OPP2 OPPCMGNUM (D); OPP3 OPPOPGNUM (D); OPP4 OPPCMP (D); OPP5 OPPMCN (D); OPP6 OPPREP+OPPCDA (D); OPP7 OPPORI+OPPORIVCR+OPPORIVCRL (D)
Fields:
  ASE DCO(15) Strengths
  AUUID AUUID Single identifier
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CPP ADI(15) Competitor -> [ADI]CODE =418;CPP (ATABDIV) !Block
  CPPAMT MD1(15) Competitor amount
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OPP]CUR (TABCUR) !Block
  DAM MD1 Double weighting
  DAMAVE M*4 By average [menu 1: 1=No,2=Yes]
  DAMCUM M*4 Cumulated [menu 1: 1=No,2=Yes]
  DON M*4(15) Phase end [menu 1: 1=No,2=Yes]
  DONX M*4(15) Phase end [menu 1: 1=No,2=Yes]
  ENDDAT D(15) Date
  ENDDATX D(15) Date
  OPPAAM MD1 Weighted amount
  OPPAMT MD1 Amount
  OPPCDA D Desired conclusion
  OPPCLO M*4 Closed project [menu 1: 1=No,2=Yes]
  OPPCMGNUM CMG Campaign code -> [CMG]CMG0 =[OPP]OPPCMGNUM (CMARKETING) !Block
  OPPCMP BPR BP -> [BPR]BPR0 =[OPP]OPPCMP (BPARTNER) !Block
  OPPDATOPN D Opening date
  OPPDES DCO Project description
  OPPEXTNUM A*20 External identifier
  OPPMCN AIN Contact (relationship) -> [AIN]AIN0 =OPPMCN (CONTACTCRM) !Block
  OPPNBQ L*4 Number of quotes
  OPPNUM VCR Project chrono
  OPPOPGNUM VCR Operation code
  OPPOPGTYP AOB Operation type -> [AOB]ABREV =[OPP]OPPOPGTYP (AOBJET) !Block
  OPPORI M*15 Source [menu 2995: 1=Manual creation,2=Mass mail,3=Call campaign,4=Trade show,5=Media campaign,6=Service Request,7=Marketing campaign]
  OPPORITYP M*15 Source type [menu 3037: 1=Manual,2=Generated,3=Synchronization,4=Import]
  OPPORIVCR VCR Document no.
  OPPORIVCRL L*8 Line no.
  OPPREACDA D Actual conclusion
  OPPREP REP Sales rep -> [REP]REP0 =[OPP]OPPREP (SALESREP) !Block
  OPPSRENUM SRE Service request -> [SRE]SRE0 =[OPP]OPPSRENUM (SERREQUEST) !Block
  OPPSTE ADI Step -> [ADI]CODE =OPPSTEADI;OPPSTE (ATABDIV) !Block
  OPPSTEA2 A*10 Fixed stage code
  OPPSTEADI ADV Miscellaneous table -> [ADV]CODE =[OPP]OPPSTEADI (ATABTAB) !Block
  OPPSUC L*3 Success probability
  OPPTYP ADI Category -> [ADI]CODE =434;OPPTYP (ATABDIV) !Block
  PBYPRJ L*3 Project probability
  PBYPRJAAM MD1 Weighted project
  REN DES(15) Reason
  RENX DES(15) Reason
  SALFCY FCY Sales site -> [FCY]FCY0 =[OPP]SALFCY (FACILITY) !Block
  SBBPJT OPP(15) Sub-project -> [OPP]OPP0 =[OPP]SBBPJT (OPPOR) !Block
  SHC DCO(15) Weaknesses
  STE ADI(15) Step -> [ADI]CODE =400;STE (ATABDIV) !Block
  STEX ADI(15) Step -> [ADI]CODE =421;STEX (ATABDIV) !Block
  STRSTE D Since
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPPORCPP (OCP) - Project competitor
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OCP0 OPPNUM+CPP
Fields:
  ASE DCO Strengths
  AUUID AUUID Single identifier
  CPP ADI Competitor -> [ADI]CODE =418;CPP (ATABDIV) !Block
  CPPAMT MD1 Competitor amount
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OCP]OPPNUM (OPPOR) !Delete
  SHC DCO Weaknesses
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPPORCRM (OPPCRM) - CRM project
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OPPCRM0 OPPNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  DAM MD1 Double weighting
  DAMAVE M*4 By average [menu 1: 1=No,2=Yes]
  DAMCUM M*4 Cumulated [menu 1: 1=No,2=Yes]
  OPPAAM MD1 Weighted amount
  OPPAMT MD1 Amount
  OPPCDA D Desired conclusion
  OPPNBQ L*4 Number of quotes
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OPPCRM]OPPNUM (OPPOR) !Delete
  OPPREACDA D Actual conclusion
  OPPSRENUM SRE Service request -> [SRE]SRE0 =[OPPCRM]OPPSRENUM (SERREQUEST) !Block
  OPPSTE ADI Step -> [ADI]CODE =OPPSTEADI;OPPSTE (ATABDIV) !Block
  OPPSTEA2 A*10 Fixed stage code
  OPPSTEADI ADV Miscellaneous table -> [ADV]CODE =[OPPCRM]OPPSTEADI (ATABTAB) !Block
  OPPSUC L*3 Success probability
  PBYPRJ L*3 Project probability
  PBYPRJAAM MD1 Weighted project
  STRSTE D Since
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPPORPJM (OPPPJM) - PJM project
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OPPPJM0 OPPNUM
Fields:
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[OPPPJM]CREUSR (AUTILIS) !Other
  CUROPP CUR Financial currency -> [TCU]TCU0 =[OPPPJM]CUROPP (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[OPPPJM]DIE (GDIE) !Block act:ANA
  OPEDEFFCY FCY Operating site -> [FCY]FCY0 =[OPPPJM]OPEDEFFCY (FACILITY) !BSRA
  OPPDATLA D Launch date
  OPPDATLV D Delivery date
  OPPDATS D Date closed
  OPPDATTH D Suspension date
  OPPFRT M*4 Projected [menu 1: 1=No,2=Yes]
  OPPIMPT M*4 Intermediate batch [menu 1: 1=No,2=Yes]
  OPPIMPTLOCK M*4 Lock [menu 1: 1=No,2=Yes]
  OPPINT M*4 Internal [menu 1: 1=No,2=Yes]
  OPPMOD M*4 Template [menu 1: 1=No,2=Yes]
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OPPPJM]OPPNUM (OPPOR) !Delete
  OPPPROACTIV M*4 Activation [menu 1: 1=No,2=Yes]
  OPPSTATE M*9 Status [menu 2249: 1=New,2=Launched,3=Delivered,4=Closed,5=,6=,7=,8=,9=Suspended]
  TASBUDAUT M*4 Task creates budget [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[OPPPJM]UPDUSR (AUTILIS) !Other

## OPPORSBB (OBB) - Sub-project
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OBB0 OPPNUM+SBBPJT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OBB]OPPNUM (OPPOR) !Delete
  SBBPJT OPP Sub-project -> [OPP]OPP0 =[OBB]SBBPJT (OPPOR) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPPORSTA (OSA) - Project after-sales steps
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OSA0 OPPNUM+STELINX; OSA1 OPPNUM+STRDATX+STELINX
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DONX M*4 Phase end [menu 1: 1=No,2=Yes]
  ENDDATX D End date
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OSA]OPPNUM (OPPOR) !Delete
  RENX DES Reason
  STELINX ISEQ Step line
  STEORIXAOB AOB Object code -> [AOB]ABREV =[OSA]STEORIXAOB (AOBJET) !Block
  STEORIXVCR VCR Document no.
  STEX ADI Step -> [ADI]CODE =421;STEX (ATABDIV) !Block
  STRDATX D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPPORSTB (OSB) - Project pre-sales steps
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): OSB0 OPPNUM+STELIN; OSB1 OPPNUM+STRDAT+STELIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DON M*4 Phase end [menu 1: 1=No,2=Yes]
  ENDDAT D End date
  OPPNUM OPP Project chrono -> [OPP]OPP0 =[OSB]OPPNUM (OPPOR) !Delete
  REN DES Reason
  STE ADI Step -> [ADI]CODE =400;STE (ATABDIV) !Block
  STELIN ISEQ Step line
  STEORIAOB AOB Object code -> [AOB]ABREV =[OSB]STEORIAOB (AOBJET) !Block
  STEORIVCR VCR Document no.
  STRDAT D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ORDCOMP (DOO) - Service caller
Keys (first = PK; D = duplicates allowed): DOO0 BPRNUM
Fields:
  ALH1 A*30 Alpha field 1
  ALH2 A*30 Alpha field 2
  ALH3 A*30 Alpha field 3
  ALH4 A*30 Alpha field 4
  ALH5 A*30 Alpha field 5
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[DOO]BPRNUM (BPARTNER) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DOO]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DOO]UPDUSR (AUTILIS) !Other

## ORDERS (ORD) - WIP
Keys (first = PK; D = duplicates allowed): ORD0 WIPTYP+WIPNUM+ITMREF; ORD1 STOFCY+ITMREF+ENDDAT (D); ORD2 ITMREF+ENDDAT (D); ORD3 STOFCY+VCRTYP+VCRNUM+VCRLIN+VCRSEQ (D); ORD4 ITMREF+STOFCY+WIPTYP (D)
Fields:
  ABBFIL A*3 File abbreviation
  ALLQTY QTY Allocated qty.
  ATECORI M*15 Source [menu 7885: 1=Classic pages,2=Classes]
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !RTZ
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMOFS C*4 Operation lead time
  BOMOPE OPE Operation number
  BPRNUM BPR BP -> [BPR]BPR0 =[ORD]BPRNUM (BPARTNER) !RTZ
  CCMRID CCMCRID Request ID act:CCM
  CCMSTA M*20 Request status [menu 2044: 1=Pending,2=Blocking,3=No action,4=Complete] act:CCM
  CPLQTY QTY Total completed qty.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ENDDAT D End date
  EXPNUM L*8 Export number
  EXTQTY QTY Planned qty.
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  ITMREF ITM Product -> [ITM]ITM0 =ITMREF (ITMMASTER) !Block
  ITMREFORI ITM Source product -> [ITM]ITM0 =[ORD]ITMREFORI (ITMMASTER) !Other
  MRPDAT D MRP date
  MRPMES M*15 MRP message [menu 318: 1=No action,2=Advance,3=Delay,4=Increase,5=Reduce,6=Cancel,7=Advance/Increase,8=Advance/Reduce,9=Delay/Increase,10=Delay/Reduce,11=Delay firm horizon,12=Obsolete product (end of life),13=Overstock,14=Invalid routing version]
  MRPQTY QTY MRP qty.
  MTOQTY QTY Assigned qty.
  MTOREF MTO MTO network -> [MTO]MTO0 =MTOREF (MTOHEAD) !RTZ
  OPTFLG M*4 Optimization flag [menu 1: 1=No,2=Yes]
  ORI M*15 Source [menu 298: 1=Purchasing,2=Sales,3=Stock,4=Production,5=MPS,6=MRP,7=Projet]
  ORIFCY FCY Original site -> [FCY]FCY0 =[ORD]ORIFCY (FACILITY) !Block
  PIO M*15 Priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  PJT PJT Project -> [PIM]PIM0 =[ORD]PJT (PIMPL) !BSRA
  RMNEXTQTY QTY Remaining qty.
  SHTQTY QTY Shortage
  STOFCY FCY Stock site -> [FCY]FCY0 =[ORD]STOFCY (FACILITY) !Block
  STRDAT D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRNUM VCR Subcon. req./order
  VCRNUMORI VCR Original document
  VCRSEQ L*8 Document sequence no.
  VCRSEQORI L*8 Source seq.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]

## ORGAFFIL (ORA) - Organization membership
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## ORGANISME (ORG) - Organizations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## ORGBAN (ORB) - Organization
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## OVENAT (ONA) - Overhead category
Keys (first = PK; D = duplicates allowed): ONA0 OVENAT
Fields:
  A1 A*10 Alpha 1
  A2 A*10 Alpha 2
  ACCCOD CAC Accounting code -> [CAC]CAC0 =19;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DIE DIE Dimension type code -> [DIE]DIE0 =[ONA]DIE (GDIE) !Block act:ANA
  EXPNUM L*8 Export number
  N1 DCB*11.2 Numeric 1
  N2 DCB*11.2 Numeric 2
  ONAAXX AX3 Description
  ONASHOAXX AX1 Short description
  OVENAT A*3 Nature
  TYPCST M*15 Cost type [menu 2384: 1=As per context,2=Material,3=Machine,4=Labor,5=Subcontracting]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OVERHEAD (OVE) - Overhead codes
Keys (first = PK; D = duplicates allowed): OVE0 OVECOD
Fields:
  AUUID AUUID Single identifier
  CLCLEV M*15 Overhead application [menu 331: 1=Stock receipt,2=Stock issue]
  CLCMOD M*15 Calculation method [menu 321: 1=Cumulated,2=Compound]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OVE]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  FORBASIS M*15 Formula base [menu 2360: 1=Amount,2=Hours (operations) or quantities]
  FORCODA FOR Formula code -> [TFO]TFO0 =5;FORCODA(indice) (TABFOR) !Block act:ONA
  FORCODB FOR Formula code -> [TFO]TFO0 =5;FORCODB(indice) (TABFOR) !Block act:ONA
  FORCODC FOR Formula code -> [TFO]TFO0 =5;FORCODC(indice) (TABFOR) !Block act:ONA
  FORCODD FOR Formula code -> [TFO]TFO0 =5;FORCODD(indice) (TABFOR) !Block act:ONA
  FXDOVEA DCB*8 Contract act:ONA
  FXDOVEB DCB*8 Contract act:ONA
  FXDOVEC DCB*8 Contract act:ONA
  FXDOVED DCB*8 Contract act:ONA
  OVEAXX AX3 Description
  OVECOD A*3 Overhead
  OVEDES DES Description
  OVENAT ONA Category -> [ONA]ONA0 =[OVE]OVENAT (OVENAT) !Block act:ONA
  OVESHO SHO Short description
  OVESHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRTRG M*20 Trigger [menu 2381: 1=Document,2=Source document] act:ONA

## PARESC (PEC) - Escalation parameter
Keys (first = PK; D = duplicates allowed): PEC0 ESCNUM; PEC1 ENAFLG+ESCCAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ESCACTNAM A*100(10) Description
  ESCACTNUM ADI(10) Action -> [ADI]CODE =455;ESCACTNUM (ATABDIV) !RTZ
  ESCCAT ADI Category -> [ADI]CODE =453;ESCCAT (ATABDIV) !RTZ
  ESCCND ADI Condition -> [ADI]CODE =454;ESCCND (ATABDIV) !RTZ
  ESCNAM A*100 Description
  ESCNUM VCR Code
  ESCTYP M*15 Type [menu 3028: 1=Hidden,2=Archived,3=Incremental]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PARMTO (PTO) - Assignment rules
Keys (first = PK; D = duplicates allowed): PTO0 PTOCOD
Fields:
  AUUID AUUID Single identifier
  BPSFLT M*4(5) Prio supplier [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATFLT M*4(5) Reference date [menu 1: 1=No,2=Yes]
  DATMARDOWN C*3(5) Margin - (d)
  DATMARUP C*3(5) Margin + (d)
  DEMCAT M*15 Order type [menu 790: 1=No,2=Sales,3=Production,4=Internal]
  DEMFCT C*4 Type factor
  DEMMOD M*4 Type mode [menu 1: 1=No,2=Yes]
  DIRALL M*4 Auto allocation [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FRCPRO M*4 Process the forced [menu 1: 1=No,2=Yes]
  PIOFCT C*4 Priority factor
  PIOMOD M*4 Priority method [menu 1: 1=No,2=Yes]
  PJTFLT M*4(5) Standardized project [menu 1: 1=No,2=Yes]
  PTOAUT M*4 Automatic [menu 1: 1=No,2=Yes]
  PTOCOD A*5 Rule
  PTODES DES Description
  PTODESAXX AX3 Description
  PTODIR M*4 Back-to-back [menu 1: 1=No,2=Yes]
  PTOHOR C*4 Horizon
  PTOHORFLG M*4 Horizon flag [menu 1: 1=No,2=Yes]
  PTOREAL M*4 Real time [menu 1: 1=No,2=Yes]
  PTOSHO SHO Short description
  PTOSHOAXX AX1 Short description
  QTYFLT M*4(5) Standardized quantity [menu 1: 1=No,2=Yes]
  QTYPCTDOWN DCB*3.3(5) Tolerance - (%)
  QTYPCTUP DCB*3.3(5) Tolerance + (%)
  REAL4DEM M*4 Real time requirements [menu 1: 1=No,2=Yes]
  REAL4RESS M*4 Real time supply [menu 1: 1=No,2=Yes]
  SHTFCT C*4 Shortage factor
  SHTMOD M*4 Shortage mode [menu 1: 1=No,2=Yes]
  UNTFLT M*4(5) Standardized unit [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PARTAXUSA (PTU) - American tax parameters
Keys (first = PK; D = duplicates allowed): PTU0 COD
Fields:
  AUUID AUUID Single identifier
  COD A*10 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PTU]CREUSR (AUTILIS) !Other
  DIRECTORY A*250 Directories
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PTU]UPDUSR (AUTILIS) !Other

## PAYORDER (PYO) - Prepayments
Keys (first = PK; D = duplicates allowed): PYO0 DUDNUM+DUDLIG+PAYNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PYO]CREUSR (AUTILIS) !Other
  DUDLIG C*3 Due date number
  DUDNUM L*8 Due date number
  DUDPAYAMT MD1 Paid amount
  INVNUM L*8 Entry number
  PAYNUM L*8 Entry number
  PAYVCR VCR Payment
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PYO]UPDUSR (AUTILIS) !Other

## PBDBPGRP (PBDBPG) - Economic reason/BP groups
Keys (first = PK; D = duplicates allowed): PBDBPG0 COD+LEG
Fields:
  AUUID AUUID Single identifier
  COD PBDBPG Group code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDBPG]CREUSR (AUTILIS) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDBPG]UPDUSR (AUTILIS) !Other

## PBDBPGRPD (PBDBPD) - Economic reason/BP groups
Keys (first = PK; D = duplicates allowed): PBDBPD0 COD+LEG+BPR
Fields:
  AUUID AUUID Single identifier
  BPR A*15 BP code
  COD PBDBPG Group code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDBPD]CREUSR (AUTILIS) !Other
  CRYADDCOD M*15 Address code [menu 3642: 1=BP address,2=Payment address]
  ECOCOD PBDECO Economic reason code -> [PBDECO]PBDECO0 =ECOCOD;LEG (PBDECOCOD) !Block
  FLGALL M*4 All BP types [menu 1: 1=No,2=Yes]
  FLGBPNINC M*4 Always include BP [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TYP M*20 Type [menu 277: 1=Customer,2=Supplier,3=Carrier,4=Factor,5=Sales rep,6=Miscellaneous BPs]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDBPD]UPDUSR (AUTILIS) !Other

## PBDECOCOD (PBDECO) - Economic reason code
Keys (first = PK; D = duplicates allowed): PBDECO0 COD+LEG; PBDECO1 LEG+COD
Fields:
  AUUID AUUID Single identifier
  COD PBDECO Code -> [PBDECO]PBDECO0 =COD;LEG (PBDECOCOD) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDECO]CREUSR (AUTILIS) !Other
  DES AXX Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TIT AX3 Description
  TYP M*15 Type [menu 3641: 1=Not used,2=Service,3=Capital flow,4=Transit trade]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDECO]UPDUSR (AUTILIS) !Other

## PERIOD (PER) - Periods
Keys (first = PK; D = duplicates allowed): PER0 CPY+LEDTYP+FIYNUM+PERNUM; PER1 LEDTYP (D)
Fields:
  AUUID AUUID Single identifier
  CLODAT D Closing date
  CPY CPY Company -> [CPY]CPY0 =[PER]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PER]CREUSR (AUTILIS) !Other
  FIYNUM C*2 Fiscal year
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEDTYPAUT M*4 Auto ledger [menu 1: 1=No,2=Yes]
  PEREND D Period end
  PERNUM C*2 Period number
  PERSTA M*15 Period status [menu 214: 1=Not open,2=Open,3=Closed]
  PERSTOSTA M*15 Stock transaction status [menu 228: 1=Open,2=Deferred,3=Balance adjustment,4=Closed]
  PERSTR D Period start
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PER]UPDUSR (AUTILIS) !Other

## PFOOTINV (PFI) - Purchase invoicing elements
Keys (first = PK; D = duplicates allowed): PFI0 PFINUM
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =16;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACTCLCBAS A*10 Action calcul.
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount]
  AUUID AUUID Single identifier
  BPSORI M*20 Original supplier [menu 577: 1=Order supplier,2=Invoice supplier]
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CLCBAS M*15 Calculation basis [menu 537: 1=None,2=Exclude tax amount,3=Include tax amount,4=Action]
  CLCDEB M*18 Intrastat taken into account [menu 2208: 1=No,2=Fiscal value,3=Statistical value] act:DEB
  CLCORD C*3 Calculation order
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PFI]CUR (TABCUR) !Block
  DACLIN M*4 Price line [menu 1: 1=No,2=Yes]
  DACORD M*4 Order footer [menu 1: 1=No,2=Yes]
  DEFVAL DCB*11.4 Default value
  DEPFLG M*4 Subject to discount [menu 1: 1=No,2=Yes]
  DESAXX AX2 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[PFI]DIE (GDIE) !Block act:ANA
  DISVATFLG M*4 Rebate on VAT [menu 1: 1=No,2=Yes]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  DSPLIN M*15 Distribution [menu 520: 1=No,2=Quantity pro rata,3=Amount pro rata,4=Weight pro rata,5=Volume pro rata]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  INCDCR M*10 Increase/Decrease [menu 254: 1=Increase,2=Decrease]
  ITMREF ITM Product -> [ITM]ITM0 =[PFI]ITMREF (ITMMASTER) !Block
  LANDESSHO A*50 Descriptions
  NPRVLT M*4 Net price increase [menu 1: 1=No,2=Yes]
  PFINUM PFI Invoicing element -> [PFI]PFI0 =[PFI]PFINUM (PFOOTINV) !Other
  PFINUMCAR A*3 Alpha no.
  PRGCLCBAS A*10 Program calcul.
  SHOAXX AX1 Short description
  TRFINV M*20 Include in ord-inv [menu 567: 1=Amount pro rata,2=Quantity pro rata,3=Weight pro rata,4=Volume pro rata,5=First document,6=All documents]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI Element tax level -> [TVI]TVI0 =VACITM;[V]GSUPCLE (TABVACITM) !Block
  VATRUL M*15 Tax rule [menu 538: 1=Product rate,2=Fixed rate]

## PHONECALL (CLL) - Call
Notes: differs in V9.0 P12 (diff: AT3_PHONECALL.htm); differs in V10 P1 (diff: ATD_PHONECALL.htm)
Keys (first = PK; D = duplicates allowed): CLL0 CLLNUM; CLL1 CLLDATX (D); CLL2 CLLCMP (D); CLL3 CLLCCN (D); CLL4 CLLREP+CLLDATX (D); CLL5 CLLCMGNUM (D); CLL6 CLLOPGTYP+CLLOPGNUM (D); CLL7 CLLORIADI+CLLORIVCR+CLLORIVCRL (D); CLL8 CLLDAT+CLLHOU+CLLNUM
Fields:
  AUUID AUUID Single identifier
  CLLCAT ADI Category -> [ADI]CODE =432;CLLCAT (ATABDIV) !Block
  CLLCCN AIN Contact (relationship) -> [AIN]AIN0 =[CLL]CLLCCN (CONTACTCRM) !Block
  CLLCCNCRY CRY Contact country -> [TCY]TCY0 =[CLL]CLLCCNCRY (TABCOUNTRY) !Block
  CLLCMGFLG C*2 Call campaign flag
  CLLCMGNUM CMG Campaign code -> [CMG]CMG0 =[CLL]CLLCMGNUM (CMARKETING) !Block
  CLLCMP BPR BP -> [BPR]BPR0 =[CLL]CLLCMP (BPARTNER) !Block
  CLLCOR COR Outlook contact -> [COR]COR0 =[CLL]CLLCOR (CORRESPOND) !Block
  CLLDAT D Date
  CLLDATX D Week conversion
  CLLDON M*4 Completed [menu 1: 1=No,2=Yes]
  CLLDUR C*4 Duration
  CLLEML MAI Email
  CLLETS TEL Direct line
  CLLHOU HM Time
  CLLMOB TEL Mobile phone
  CLLNUM VCR Call time
  CLLOBJ CLX Subject summary
  CLLOPGNUM VCR Operation code
  CLLOPGTYP AOB Operation type -> [AOB]ABREV =[CLL]CLLOPGTYP (AOBJET) !Block
  CLLOPP PJT Project -> [PIM]PIM0 =[CLL]CLLOPP (PIMPL) !Block
  CLLORI M*15 Source [menu 2993: 1=Manual creation,2=Mass mail,3=Call campaign,4=Trade show,5=Media campaign,6=Marketing campaign]
  CLLORIADI ADI Source -> [ADI]CODE =439;CLLORIADI (ATABDIV) !Block
  CLLORIAOB AOB Object code -> [AOB]ABREV =[CLL]CLLORIAOB (AOBJET) !Block
  CLLORITYP M*15 Source type [menu 3037: 1=Manual,2=Generated,3=Synchronization,4=Import]
  CLLORIVCR VCR Original document no.
  CLLORIVCRL L*8 Original line no.
  CLLPIOLEV ADI Priority level -> [ADI]CODE =405;CLLPIOLEV (ATABDIV) !Block
  CLLREP REP Sales rep -> [REP]REP0 =[CLL]CLLREP (SALESREP) !Block
  CLLRPO CLX Report
  CLLSAO ADI Satisfaction -> [ADI]CODE =436;CLLSAO (ATABDIV) !Block
  CLLSCP SCP Call script -> [SCP]SCP0 =[CLL]CLLSCP (SCRIPT) !Block
  CLLTNTPRE C*4 Prev attempts
  CLLTYP M Type [menu 956: 1=Incoming call,2=Outgoing call]
  CLLWEE C*4 Week
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  NUMFULOBJ CLC Chrono txt file
  NUMFULRPO CLC Chrono txt file
  OBJFLG C*2 Flag text file
  RPOFLG C*2 Flag text file
  SALFCY FCY Sales site -> [FCY]FCY0 =[CLL]SALFCY (FACILITY) !Block
  TYPFULOBJ CLT Type text file
  TYPFULRPO CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PHONING (OMP) - Phone campaign
Keys (first = PK; D = duplicates allowed): OMP0 OMPNUM; OMP1 CMGNUM (D); OMP2 OMPSTR (D)
Fields:
  AUUID AUUID Single identifier
  BUD MD1 Established budget
  CLO M*4 Closed [menu 1: 1=No,2=Yes]
  CLODAT D Closing date
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[OMP]CMGNUM (CMARKETING) !Block
  CNTTTR A*75 Generic title
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OMP]CUR (TABCUR) !Block
  DEFADD M*15 Address assignment [menu 965: 1=By Business Partner,2=By Contact]
  DES DCO Description
  FCY FCY Site -> [FCY]FCY0 =[OMP]FCY (FACILITY) !Block
  HIEBPR M*4 BP/contact empty [menu 1: 1=No,2=Yes]
  NBRCLLOMP L*8 Number of calls
  NBRCLLPCD L*8 No. of calls made
  NBRCLLPCDX L*8 Calls not made
  NUMFULOBJ CLC Chrono txt file
  OBJ CLX Objective
  OBJFLG C*2 Flag text file
  OMPEND D End
  OMPNUM VCR Code
  OMPSTR D Start
  SCPNUM SCP Call script -> [SCP]SCP0 =[OMP]SCPNUM (SCRIPT) !Block
  TYPFULOBJ CLT Type text file
  TYPSEA AOB Sample type -> [AOB]ABREV =[OMP]TYPSEA (AOBJET) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PIMPL (PIM) - Project link
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PIM0 PIMNUM; PIM1 OPPNUM+TASCOD (D); PIM2 OPPNUM+PBUCOD (D); PIM4 OPPNUM (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PIM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[PIM]FCY (FACILITY) !Block
  FINRSPFCY FCY Financial site -> [FCY]FCY0 =[PIM]FINRSPFCY (FACILITY) !Block
  OPPNUM OPP Project -> [OPP]OPP0 =[PIM]OPPNUM (OPPOR) !Other
  OPPSTATE M*9 Status [menu 2249: 1=New,2=Launched,3=Delivered,4=Closed,5=,6=,7=,8=,9=Suspended] act:PJM
  PBUCOD PBU Budget code act:PJM
  PBUSTATE M*8 Status [menu 2251: 1=New,2=Open,3=Delivered,4=Closed,5=,6=,7=,8=,9=Suspended] act:PJM
  PIMDESAX1 AX3 Short description
  PIMDESAXX AXX Description
  PIMNUM VPJ Project link
  PIMSTA M*4 Active [menu 1: 1=No,2=Yes]
  PIMTYP M*20 Type [menu 2254: 1=CRM,2=Project,3=Mixed project,4=Budget,5=Labor task,6=Material task,7=Mixed task,8=Miscellaneous]
  TASCOD TAC Task code act:PJM
  TASSTATE M*9 Status [menu 2250: 1=New,2=Launched,3=Started,4=Closed,5=Planned,6=,7=,8=,9=Suspended] act:PJM
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PIMPLSEL (PIS) - Temporary allocation lines
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PIS0 PIMSSS+SEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR A*10 Creation user
  OPPNUM OPP Project number -> [OPP]OPP0 =[PIS]OPPNUM (OPPOR) !BSRA
  PBUCOD PBU Budget code
  PIMNUM VPJ Project link
  PIMSSS L*8 Session
  PIMSTA M*4 Status [menu 1: 1=No,2=Yes]
  PIMTYP M*20 Type [menu 2254: 1=CRM,2=Project,3=Mixed project,4=Budget,5=Labor task,6=Material task,7=Mixed task,8=Miscellaneous]
  SEQ L*8 Sequence
  TASCOD TAC Task code
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## PINVOICE (PIH) - Purchase invoices
Notes: differs in V9.0 P12 (diff: AT3_PINVOICE.htm); differs in V10 P1 (diff: ATD_PINVOICE.htm)
Keys (first = PK; D = duplicates allowed): PIH0 NUM; PIH1 BPR+BPRVCR (D); PIH2 GTE+NUM; PIH3 ACCDAT+BPR (D); PIH4 CUR+BPR+NUM; PIH5 CPY+EECNUMDEB+ACCDAT (D); PIH6 RCRNUM+RCRDAT (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM L*8 Internal number
  AMTATI MD1 Amount + tax
  AMTATIL MD1 Invoice amt. + tax (co)
  AMTNOT MD1 Amount - tax
  AMTNOTL MD1 Amount - tax (co)
  AMTSUBJ1099 MD1 Amt. subject to 1099 act:S1099
  AMTTAX MD1(20) Tax amount
  AUUID AUUID Single identifier
  BASDEP MD1 Early disc/late charge calc basis
  BASTAX MD1(20) Tax basis
  BELVCS VCS VCS number act:KBE
  BOX1099 A*4 1099 box act:S1099
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Address
  BPAPAY ADR Pay-to BP address
  BPR BPR BP -> [BPR]BPR0 =[PIH]BPR (BPARTNER) !Block
  BPRDAT D Source date
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[PIH]BPRPAY (BPARTNER) !Block
  BPRSAC SAC Control
  BPRVCR A*20 Source document
  BPYADDLIG ADL(3) Address line
  BPYCRY CRY Country -> [TCY]TCY0 =[PIH]BPYCRY (TABCOUNTRY) !Block
  BPYCRYNAM NCY Country name
  BPYCTY CTY City
  BPYNAM NAM(2) Company name
  BPYPOSCOD POS Postal code
  BPYSAT SAT County
  BVRBID BID Bank account number act:KSW
  BVRREFLINE A*55 ISR reference line act:KSW
  CAI A*10 CAI number act:KAG
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CEEFLG M*4 EU invoice [menu 1: 1=No,2=Yes]
  CLSVCR A*10 Class act:KAG
  CPY CPY Company -> [CPY]CPY0 =[PIH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CRY CRY Country -> [TCY]TCY0 =[PIH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CSHVAT M*4 Cash VAT tax rule [menu 1: 1=No,2=Yes] act:KSP
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[PIH]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[PIH]CURLED (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DAS2 M*4 Fees declaration [menu 1: 1=No,2=Yes] act:FEE2
  DATVLYCAI D*1 CAI validity date act:KAG
  DEDTAX MD1(20) Deductible tax
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DEPRAT RAT Early discount rate
  DEPTYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  DES DES(5) Comments
  DIE DIE Dimension type code -> [DIE]DIE0 =[PIH]DIE (GDIE) !Block act:ANA
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PIH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNUM A*20 EU identification act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENDDATSVC D End service act:SVC
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[PIH]FCY (FACILITY) !Block
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[PIH]FFWNUM (BPCARRIER) !Block
  FIY C*2 Fiscal year
  FLD40REN ADI Field 40 - reason -> [ADI]CODE =8300;FLD40REN (ATABDIV) !Block act:KPO
  FLD41REN ADI Field 41 - reason -> [ADI]CODE =8301;FLD41REN (ATABDIV) !Block act:KPO
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC] act:S1099
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  ICTCTY CTY Incoterm town
  INVNUM VCR Invoice number
  INVREF REF Internal reference
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LASDATSVC D Accrued costs posted act:SVC
  LED LED(10) Ledger -> [LED]LED0 =[PIH]LED (GLED) !Block
  NBRCPY C*2 Number of companies
  NBRTAX C*2 Number of taxes
  NUM VCR Document no.
  ORIDOCNUM A*30 Original document no. act:KPO
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  PAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  PER C*2 Period
  PIHTYP M*20 Purchase invoice cat. [menu 533: 1=Invoice,2=Additional invoice,3=Credit memo,4=Credit memo/Return]
  PIVTYP TPV Invoice type -> [TPV]TPV0 =PIVTYP;[V]GSUPCLE (TABPIVTYP) !Block
  PJTH PJT Project -> [PIM]PIM0 =[PIH]PJTH (PIMPL) !Block
  PORIMPLIQNUM VCR Import tax pmt no act:KPO
  POSCOD POS Postal code
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  PURPRITYP M*10 Supplier amount type [menu 243: 1=Exclude tax,2=Include tax]
  PURTYP M*5(20) Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  RCRDAT D Recurrence date
  RCRNUM VCR Recurring number
  RITAMT DCB*9.2(10) Amount act:KIT
  RITAMTDED DCB*9.2(10) Amount deducted act:KIT
  RITBAS DCB*9.2(10) Bases act:KIT
  RITBASDED DCB*9.2(10) Deducted basis act:KIT
  RITCOD RTZ(10) Withholding code -> [RTZ]RTZ0 =[PIH]RITCOD (RITENZIONE) !Block act:KIT
  RITINV VCR Proforma act:KIT
  RITNBR C*4 No. of withholdings act:KIT
  RITPAY VCR Payment act:KIT
  SAT SAT County
  SCUVCR A*10 Branch act:KAG
  SEQVCR A*10 Sequence act:KAG
  SINUM A*10 Integrale part no. act:SMI
  SNS C*2 Sign
  SPACUS A*40 SCD reference act:KSP
  SPACUSBPR BPS SCD BP code -> [BPS]BPS0 =[PIH]SPACUSBPR (BPSUPPLIER) !Block act:KSP
  SPACUSDAT D SCD date act:KSP
  SPADERNUM A*60 DER code act:KSP
  STA M*15 Status [menu 509: 1=Pending,2=To validate,3=Validated]
  STRDATSVC D Start service act:SVC
  STRDUDDAT D Due date basis
  TAX VAT(20) Taxes -> [TVT]TVT0 =TAX(indice);[V]GSUPCLE (TABVAT) !Block
  TWMSTA M*15 Match status [menu 585: 1=Not applicable,2=Successful,3=Warning,4=Blocked,5=Unblocked]
  TYPVCR A*10 Document type act:KAG
  UBLAMT MD8 Unblock amount
  UBLDAT D Unblock date
  UBLUSR AUS Unblock user -> [AUS]CODUSR =[PIH]UBLUSR (AUTILIS) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VAC TVB Tax rule -> [TVB]TVB0 =VAC;[V]GSUPCLE (TABVACBPR) !Block
  VATDAT D Tax date on credit

## PITCOUNT (PCT) - Point counter
Keys (first = PK; D = duplicates allowed): PCT0 SRENUM+TPYFLG+FGVCAH+BPC+MAC+PBL+HDT+HDTSEQ; PCT1 CONNUM (D); PCT2 LOO
Fields:
  AUUID AUUID Single identifier
  BPC BPR Customer -> [BPR]BPR0 =[PCT]BPC (BPARTNER) !RTZ
  CONNUM CON Service contract -> [CON]CON0 =[PCT]CONNUM (CONTSERV) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FGVCAH C*1 Cancel cache
  HDT VCR Consumptions
  HDTSEQ VCR Consumptions
  LOO A*100 Loop
  MAC MAC Base -> [MAC]MAC0 =[PCT]MAC (MACHINES) !RTZ
  PBL PBL Skill -> [PBL]PBL0 =[PCT]PBL (FAMPB) !RTZ
  PIT L*8 Points
  PITTYP M*15 Point type [menu 3017: 1=Fixed,2=Supplementary]
  SAT M*15 Point status [menu 3013: 1=Mobilized,2=Consumed]
  SRENUM VCR Service request
  TPYFLG C*1 Temp record
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PCT]UPDUSR (AUTILIS) !Other

## PITDEB (PDB) - Points debit
Keys (first = PK; D = duplicates allowed): PDB0 BPR+ITMREF+PBL
Fields:
  AUUID AUUID Single identifier
  BPR BPR Customer -> [BPR]BPR0 =[PDB]BPR (BPARTNER) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMREF ITM Base -> [ITM]ITM0 =[PDB]ITMREF (ITMMASTER) !Delete
  NULPIO M*4 Null value [menu 1: 1=No,2=Yes]
  PBL PBL Skill group -> [PBL]PBL0 =[PDB]PBL (FAMPB) !Delete
  SGLNBRPIT L*8 Points debited
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PITDEBD (PBD) - Point debits (line)
Keys (first = PK; D = duplicates allowed): PBD0 BPR+ITMREF+PBL+PBDLIN
Fields:
  AUUID AUUID Single identifier
  BPR BPR Customer -> [BPR]BPR0 =[PBD]BPR (BPARTNER) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEBFRY QTY Quantity
  DEBFRYBAS UOM Unit -> [TUN]TUN0 =[PBD]DEBFRYBAS (TABUNIT) !RTZ
  ITM ITM Product consumed -> [ITM]ITM0 =[PBD]ITM (ITMMASTER) !RTZ
  ITMREF ITM Base -> [ITM]ITM0 =[PBD]ITMREF (ITMMASTER) !Delete
  NBRPIT L*8 Points debited
  NULPIOVAL M*4 Null value [menu 1: 1=No,2=Yes]
  PBDLIN L*8 Debit line
  PBL PBL Skill group -> [PBL]PBL0 =[PBD]PBL (FAMPB) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PIVOTS (PIT) - Pivots
Keys (first = PK; D = duplicates allowed): PIT0 ID
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  HEAMES A*250 Header text
  HEATYP M*20 Header [menu 2242: 1=No header,2=Standard header,3=Specific header,4=Header with titles]
  ID A*10 Identifier
  INTIT DES Description
  NORECFLG M*4 No rec. message [menu 1: 1=No,2=Yes]
  NORECMES A*50 Message text
  STDFLG M*4 Standard [menu 1: 1=No,2=Yes]
  TYP M*30 Type [menu 2240: 48 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## PIVZON (PIZ) - Pivot areas
Keys (first = PK; D = duplicates allowed): PIZ0 ID+LIN; PIZ1 ID+CODFIC+CODZONE
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[PIZ]CODFIC (ATABLE) !Block
  CODZONE AVA Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  FRM AFR*150 Formula
  ID A*10 Identifier
  LIN C*3 Line number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  WRKZON M*4 Non-managed field [menu 1: 1=No,2=Yes]

## PIWRK (PKW) - Temporary journal traceability
Keys (first = PK; D = duplicates allowed): SKW0 PRONUM+LEV; SKW1 CREUSR+CREDAT+PRONUM+LEV
Fields:
  ACCNUM L*8 Internal number
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[PKW]BPRNUM (BPARTNER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CURVCR CUR Currency -> [TCU]TCU0 =[PKW]CURVCR (TABCUR) !Other
  DUDLIG C*3 Due date number
  IPTDAT D Entry date
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Other
  LEV A*60 Level
  LEVALP A*20 Level
  LEVNUM C*2 Level
  ORDATI MD1 Line amt. + tax
  ORDATID MD1 Line amt. + tax (folder)
  ORDATIL MD1 Line amt. + tax (company)
  ORDNOT MD1 Line amt. - tax
  ORDNOTD MD1 Line amt. - tax (folder)
  ORDNOTL MD1 Line amt. - tax (company)
  PRONUM A*50 Search
  PROUID L*8 Process number
  REP1 REP Sales rep 1 -> [REP]REP0 =[PKW]REP1 (SALESREP) !BSRA act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[PKW]REP2 (SALESREP) !BSRA act:RE2
  SALFCY FCY Sales site -> [FCY]FCY0 =[PKW]SALFCY (FACILITY) !Other
  SEL A*20 Sign
  STOFCY FCY Shipment site -> [FCY]FCY0 =[PKW]STOFCY (FACILITY) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PKW]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRNUM A*40 Entry
  VCRNUMCALC A*40 Calculation journal
  VCRNUMORI A*40 Original document
  VCRSTAT1 DCO Part status
  VCRSTAT2 DCO Part status
  VCRSTAT3 DCO Part status
  VCRSTAT4 DCO Part status
  VCRTYP M*15 Entry type [menu 477: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 477: 40 values, see local-menus.md]

## PJMAFF (PAF) - Employee assignment
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PAF0 OPPNUM+PAFCLB
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PAF]CREUSR (AUTILIS) !Other
  OPPNUM PIM Project number -> [PIM]PIM0 =[PAF]OPPNUM (PIMPL) !Block
  PAFCLB PAUS Employee -> [PAUS]PAUS =[PAF]PAFCLB (PJMAUS) !Block
  PAFROL ADI Role -> [ADI]CODE =639;PAFROL (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PAF]UPDUSR (AUTILIS) !Other

## PJMAUS (PAUS) - Project users
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PAUS PAUS
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PAUS]CREUSR (AUTILIS) !Other
  ENAFLG M*1 Active employee [menu 1: 1=No,2=Yes]
  PAUS AUS Employee -> [AUS]CODUSR =[PAUS]PAUS (AUTILIS) !Delete
  PAUSCST MD2 Hourly rate
  PAUSCUR CUR Currency -> [TCU]TCU0 =[PAUS]PAUSCUR (TABCUR) !Block
  PAUSPA M*4 Time entry administrator [menu 1: 1=No,2=Yes]
  PAUSROL ADI Role -> [ADI]CODE =639;PAUSROL (ATABDIV) !Block
  PAUSTT M*4 Time entry [menu 1: 1=No,2=Yes]
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PAUS]PCCCOD (PJMCOSTCTR) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PAUS]UPDUSR (AUTILIS) !Other

## PJMBUD (PJBU) - Project budget
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJBU0 OPPNUM+PBUCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  KEYCONCAT A*40 Concatenation
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJBU]OPPNUM (PIMPL) !Delete
  PBUCOD PBU Budget code
  PBUDATH D Suspension date
  PBUDATO D WIP issue date
  PBUDATS D Date closed
  PBUELE M*4 Elementary [menu 1: 1=No,2=Yes]
  PBUENDDT D End date
  PBUFCY FCY Site or company -> [FCY]FCY0 =[PJBU]PBUFCY (FACILITY) !Block
  PBUIMP M*4 Chargeable [menu 1: 1=No,2=Yes]
  PBUNUM VCR Sequence no.
  PBUPAE PBU Parent code
  PBUSTARTDT D Start date
  PBUSTATE M*8 Status [menu 2251: 1=New,2=Open,3=Delivered,4=Closed,5=,6=,7=,8=,9=Suspended]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*10 Change user

## PJMBUDLIG (PJLB) - Budget line
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJLB0 OPPNUM+PBUCOD+PLBSEQ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PJLB]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJLB]OPPNUM (PIMPL) !Delete
  ORI M*20 Origin [menu 7713: 1=Manual,2=Operations,3=Product requirements,4=Budget lines,5=Project]
  PBUCOD PBU Budget code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJLB]PCCCOD (PJMCOSTCTR) !Block
  PLBAMT MD1 Budget amount
  PLBAMTEST MD1 Last estimated amount
  PLBAMTREC MD1 Recorded amount
  PLBAMTREM MD1 Remaining amount
  PLBDATBUD D Last budget date
  PLBDATREM D Last estimated date
  PLBDESAXX AXX Description
  PLBFCY FCY Site -> [FCY]FCY0 =[PJLB]PLBFCY (FACILITY) !Block
  PLBFLGREM M*4 Nothing to commit [menu 1: 1=No,2=Yes]
  PLBPRI MD2 Budget unit price
  PLBPRIFRC M*4 Forced [menu 1: 1=No,2=Yes]
  PLBPRIREM MD2 Unit price
  PLBQTY QTY Budget quantity
  PLBQTYEST QTY Last quantity
  PLBQTYREC QTY Recorded quantity
  PLBQTYREM QTY Remaining quantity
  PLBSEQ L*8 Sequence
  PLBU UOM Unit -> [TUN]TUN0 =[PJLB]PLBU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMBUDTRQ (PJQ) - Financial overview queries
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTQ0 PBTGRP+PBTCOD
Fields:
  ACTIVE M*4 Active [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CODDES AX3 Query name
  CONTXT M*15 Context [menu 2269: 1=Labor,2=Products,3=Expenses,4=Finance,5=Time entry]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJQ]CREUSR (AUTILIS) !Other
  CUMRTCO M*4 Remain. budget calc. [menu 1: 1=No,2=Yes]
  CUMSCOL M*4 Subcol1. calculation [menu 1: 1=No,2=Yes]
  DEFCTYPE PJCC Default cost type -> [PJCC]PCC0 =[PJQ]DEFCTYPE (PJMCOSTCTR) !Block
  FREECOL L*8 Free column
  LABEL AX3 Label
  PBTCOD BTQ Query no. -> [PJQ]PTQ0 =[PJQ]PBTCOD (PJMBUDTRQ) !BSRA
  PBTGRP ADI Financial view -> [ADI]CODE =388;PBTGRP (ATABDIV) !Block
  PBTOBJ AOB Object -> [AOB]ABREV =[PJQ]PBTOBJ (AOBJET) !Block
  PJMPBTCOD BTS Structure link -> [PJS]PTS0 =PBTGRP;PJMPBTCOD (PJMBUDTRS) !Block
  POSVAL M*4 Positive valuation [menu 1: 1=No,2=Yes]
  SQLQRY ALH SQL query -> [ALH]ALH0 =[PJQ]SQLQRY (ALISTEH) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJQ]UPDUSR (AUTILIS) !Other

## PJMBUDTRS (PJS) - Financial overview structure
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTS0 PBTGRP+PBTCOD
Fields:
  AUUID AUUID Single identifier
  CODDES AXX Column content
  COL1TYP M*15 [menu 2296: 1=Quantity,2=Amount]
  COL2TYP M*15 [menu 2296: 1=Quantity,2=Amount]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJS]CREUSR (AUTILIS) !Other
  DSPLY M*4 Display [menu 1: 1=No,2=Yes]
  PBTCOD BTS Column sequence -> [PJS]PTS0 =PBTCOD;PBTGRP (PJMBUDTRS) !Block
  PBTGRP ADI Financial view -> [ADI]CODE =388;PBTGRP (ATABDIV) !Block
  SCOL1 AX3 Subcolumn 1 title
  SCOL2 AX3 Subcolumn 2 title
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJS]UPDUSR (AUTILIS) !Other

## PJMCLOB (PJCB) - Special folders
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJCB0 CODBLB+IDENT1+IDENT2+IDENT3+IDENT4
Fields:
  AUUID AUUID Single identifier
  CLOB ACB Text file (clob)
  CODBLB ATB Code -> [ATB]CODFIC =[PJCB]CODBLB (ATABLE) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[PJCB]CREUSR (AUTILIS) !Other
  IDENT1 AVA Identifier 1
  IDENT2 A*40 Identifier 2
  IDENT3 A*40 Identifier 3
  IDENT4 A*40 Identifier 4
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJCB]UPDUSR (AUTILIS) !Other

## PJMCOSTCTR (PJCC) - Cost type
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PCC0 PCCCOD
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHX M*4 Create [menu 1: 1=No,2=Yes] act:ANA
  COA COA Chart code -> [COA]COA0 =[PJCC]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[PJCC]DIE (GDIE) !Block act:ANA
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  ITMREF ITM Service product -> [ITM]ITM0 =[PJCC]ITMREF (ITMMASTER) !Block
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJCC]PCCCOD (PJMCOSTCTR) !Delete
  PCCCOD2 PJCC Expenses -> [PJCC]PCC0 =[PJCC]PCCCOD2 (PJMCOSTCTR) !Other
  PCCCUR CUR Currency -> [TCU]TCU0 =[PJCC]PCCCUR (TABCUR) !Block
  PCCFCY FCY Site -> [FCY]FCY0 =[PJCC]PCCFCY (FACILITY) !Other
  PCCGRP ADI Group -> [ADI]CODE =386;PCCGRP (ATABDIV) !Other
  PCCHATA M*4 Accounting [menu 1: 1=No,2=Yes]
  PCCPOHA M*4 Purchasing [menu 1: 1=No,2=Yes]
  PCCPRCT DCB*9.2 Percentage
  PCCPROV M*4 Indirect cost [menu 1: 1=No,2=Yes]
  PCCSTOA M*4 Stock [menu 1: 1=No,2=Yes]
  PCCU UOM Unit -> [TUN]TUN0 =[PJCC]PCCU (TABUNIT) !Other
  PCCWKA M*4 Labor [menu 1: 1=No,2=Yes]
  PJMBDC M*20 Budget distribution [menu 2076: 1=Even Period Spread,2=User Defined Spread,3=Annual Even Spread]
  SHOAXX AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMCOSTDAT (PCD) - Rate at a given date
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): CSTD0 PCCCOD+PCCDATCST
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PCD]CREUSR (AUTILIS) !Other
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PCD]PCCCOD (PJMCOSTCTR) !Block
  PCCCST RAT Unit rate
  PCCDATCST D Rate activation date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PCD]UPDUSR (AUTILIS) !Other

## PJMDE (PJE) - Detailed expense
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJE0 PDESSS+PDESEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  OBJECT A*30
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJE]OPPNUM (PIMPL) !BSRA
  PBUCOD PBU Budget code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJE]PCCCOD (PJMCOSTCTR) !BSRA
  PDEAMT1 MD1 Amount
  PDEAMT2 MD1
  PDEAMT3 MD1
  PDEAMT4 MD1
  PDEAMT5 MD1
  PDEDAT D
  PDEDES A*80
  PDEFREEC10A QTY
  PDEFREEC10B MD1
  PDEFREEC6A QTY Quantity
  PDEFREEC6B MD1 Amount
  PDEFREEC7A QTY
  PDEFREEC7B MD1
  PDEFREEC8A QTY
  PDEFREEC8B MD1
  PDEFREEC9A QTY
  PDEFREEC9B MD1
  PDEGRPDAT D
  PDEGRPDES A*80 Group
  PDEGRPNUM A*30 Group
  PDEIMG DCB*14.2
  PDENUM A*30 Number
  PDEORICOD A*80
  PDEORIDES A*80
  PDEQTY1 QTY Quantity
  PDEQTY2 QTY
  PDEQTY3 QTY
  PDEQTY4 QTY
  PDEQTY5 QTY
  PDESEQ L*8 Sequence
  PDESSS L*8 Session
  PDETYP L*8 Data type
  PDEU UOM Unit -> [TUN]TUN0 =[PJE]PDEU (TABUNIT) !BSRA
  PDEUQTY1 QTY Quantity
  PDEUQTY2 QTY Quantity
  PDEUQTY3 QTY Quantity
  PDEUQTY4 QTY Quantity
  PDEUQTY5 QTY Quantity
  PDEWQA L*8 Quantity
  PDEWWIPA L*8 WIP
  PIMNUM PIM Project link -> [PIM]PIM0 =[PJE]PIMNUM (PIMPL) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMFINCTORPT (PJMCTO) - Cost type reporting
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJC0 SHOWGRP+OPPNUM+PSCSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJMCTO]CREUSR (AUTILIS) !Other
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJMCTO]OPPNUM (PIMPL) !Other
  PBUCOD PBU Budget code
  PBUPAE PBU Parent code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJMCTO]PCCCOD (PJMCOSTCTR) !Other
  PCCGRP ADI Group -> [ADI]CODE =386;PCCGRP (ATABDIV) !Other
  PCCGRPSOR L*8 Sort
  PSCAMT1 MD1 Amount 1
  PSCAMT2 MD1 Amount 2
  PSCAMT3 MD1 Amount 3
  PSCAMT4 MD1 Amount 4
  PSCAMT5 MD1 Amount 5
  PSCBUDAMT MD1 Budget amount
  PSCBUDQTY QTY Budget quantity
  PSCESTTOTAMT MD1 Total estimation
  PSCESTTOTQTY QTY Total estimation
  PSCFREEC10A QTY
  PSCFREEC10B MD1
  PSCFREEC6A QTY Quantity
  PSCFREEC6B MD1 Amount
  PSCFREEC7A QTY
  PSCFREEC7B MD1
  PSCFREEC8A QTY
  PSCFREEC8B MD1
  PSCFREEC9A QTY
  PSCFREEC9B MD1
  PSCIMG DCB*14.2
  PSCMARGAMT MD1 Margin amount
  PSCMARGBUD6 COE Ratio on budget
  PSCMARGQTY QTY Margin
  PSCMARGTOT6 COE Ratio on total
  PSCPCTMAMT MD1 Percentage
  PSCPCTMBUD6 COE Budget percentage
  PSCPCTMQTY QTY Percentage
  PSCPCTMTOT6 COE Total percentage
  PSCQTY1 QTY Quantity 1
  PSCQTY2 QTY Quantity 2
  PSCQTY3 QTY Quantity 3
  PSCQTY4 QTY Quantity 4
  PSCQTY5 QTY Quantity 5
  PSCREMAMT MD1 Remaining amount
  PSCREMQTY QTY Remaining quantity
  PSCSEQ L*8 Sequence
  PSCTOTAMT MD1 Total amount
  PSCTOTQTY QTY Total quantity
  PSCU UOM Unit -> [TUN]TUN0 =[PJMCTO]PSCU (TABUNIT) !Block
  PSCUR CUR Currency -> [TCU]TCU0 =[PJMCTO]PSCUR (TABCUR) !Block
  PSCWIPAMT MD1 WIP amount
  PSCWIPQTY QTY WIP quantity
  SHOWGRP ADI Financial view -> [ADI]CODE =388;SHOWGRP (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJMCTO]UPDUSR (AUTILIS) !Other

## PJMFINOVRRPT (PJMRPT) - Cost structure reporting
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJMR0 SHOWGRP+OPPNUM+PSCSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJMRPT]CREUSR (AUTILIS) !Other
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJMRPT]OPPNUM (PIMPL) !Other
  PBUCOD PBU Budget code
  PBUPAE PBU Parent code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJMRPT]PCCCOD (PJMCOSTCTR) !Other
  PCCGRP ADI Group -> [ADI]CODE =386;PCCGRP (ATABDIV) !Other
  PCCGRPSOR L*8 Sort
  PSCAMT1 MD1 Amount 1
  PSCAMT2 MD1 Amount 2
  PSCAMT3 MD1 Amount 3
  PSCAMT4 MD1 Amount 4
  PSCAMT5 MD1 Amount 5
  PSCBUDAMT MD1 Budget amount
  PSCBUDQTY QTY Budget quantity
  PSCESTTOTAMT MD1 Total estimation
  PSCESTTOTQTY QTY Total estimation
  PSCFREEC10A QTY
  PSCFREEC10B MD1
  PSCFREEC6A QTY Quantity
  PSCFREEC6B MD1 Amount
  PSCFREEC7A QTY
  PSCFREEC7B MD1
  PSCFREEC8A QTY
  PSCFREEC8B MD1
  PSCFREEC9A QTY
  PSCFREEC9B MD1
  PSCIMG DCB*14.2
  PSCMARGAMT MD1 Margin amount
  PSCMARGBUD6 COE Ratio on budget
  PSCMARGQTY QTY Margin
  PSCMARGTOT6 COE Ratio on total
  PSCPCTMAMT MD1 Percentage
  PSCPCTMBUD6 COE Budget percentage
  PSCPCTMQTY QTY Percentage
  PSCPCTMTOT6 COE Total percentage
  PSCQTY1 QTY Quantity 1
  PSCQTY2 QTY Quantity 2
  PSCQTY3 QTY Quantity 3
  PSCQTY4 QTY Quantity 4
  PSCQTY5 QTY Quantity 5
  PSCREMAMT MD1 Remaining amount
  PSCREMQTY QTY Remaining quantity
  PSCSEQ L*8 Sequence
  PSCTOTAMT MD1 Total amount
  PSCTOTQTY QTY Total quantity
  PSCU UOM Unit -> [TUN]TUN0 =[PJMRPT]PSCU (TABUNIT) !Block
  PSCUR CUR Currency -> [TCU]TCU0 =[PJMRPT]PSCUR (TABCUR) !Block
  PSCWIPAMT MD1 WIP amount
  PSCWIPQTY QTY WIP quantity
  SHOWGRP ADI Financial view -> [ADI]CODE =388;SHOWGRP (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJMRPT]UPDUSR (AUTILIS) !Other

## PJMOPEAFF (PJOA) - Employee assignment
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJOA0 OPPNUM+TASCOD+OPENUM+OPESPLNUM+POANUM; PJOA1 OPPNUM+TASCOD (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PJOA]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  KEYCONCAT A*40 Concatenation
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJOA]OPPNUM (PIMPL) !Block
  POACLB AUS Employee -> [AUS]CODUSR =[PJOA]POACLB (AUTILIS) !Block
  POACSMQTY QTY Consumed load
  POACST MD2 Hourly rate
  POACSTLAB MD2 Labor rate
  POADES AXX Description
  POAEND D End date
  POAENDHM HM End time
  POANUM ISEQ Sequence
  POARMNQTY QTY Remaining load
  POASTDQTY QTY Planned load
  POASTR D Start date
  POASTRHM HM Start time
  POUOM UOM Unit -> [TUN]TUN0 =[PJOA]POUOM (TABUNIT) !Block
  TASCOD TAC Task code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMSALITMD (PSPLD) - Saleable product list
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSPLD0 OPPNUM+PBUCOD+TASCOD+SEQNUM; PSPLD1 OPPNUM+TASCOD+PBUCOD+SEQNUM
Fields:
  AUUID AUUID Single identifier
  BASPRI MD5 Base price
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSPLD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PSPLD]CUR (TABCUR) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXTQTY QTY Planned quantity
  EXTUOM UOM Planned unit -> [TUN]TUN0 =[PSPLD]EXTUOM (TABUNIT) !Block
  ITMDES DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PSPLD]ITMREF (ITMMASTER) !Block
  ITTSEQ L*8 Sequence
  OPENUM OPE Operation
  OPPNUM PIM Project number -> [PIM]PIM0 =[PSPLD]OPPNUM (PIMPL) !Delete
  ORI M*20 Origin [menu 7713: 1=Manual,2=Operations,3=Product requirements,4=Budget lines,5=Project]
  PBUCOD PBU Budget code
  PLBSEQ L*8 Sequence
  PRODGRPLVL M*20 Product grp. level [menu 7715: 1=Not grouped,2=Project,3=Budget code,4=Task code]
  PSOLIN L*8 Project doc line
  PSONUM VCR Project doc number
  QTY QTY Document quantity
  QTYSTU QTY STK quantity
  SAU UOM Sales unit -> [TUN]TUN0 =[PSPLD]SAU (TABUNIT) !Block
  SEQNUM ISEQ Line number
  STU UOM Stock unit -> [TUN]TUN0 =[PSPLD]STU (TABUNIT) !Block
  TASCOD TAC Task code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSPLD]UPDUSR (AUTILIS) !Other

## PJMSC (PJC) - Consolidated expenses
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJC0 PSCSSS+PSCSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJC]CREUSR (AUTILIS) !Other
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJC]OPPNUM (PIMPL) !Other
  PBUCOD PBU Budget code
  PBUPAE PBU Parent code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJC]PCCCOD (PJMCOSTCTR) !Other
  PCCGRP ADI Group -> [ADI]CODE =386;PCCGRP (ATABDIV) !Other
  PCCGRPSOR L*8 Sort
  PSCAMT1 MD1 Amount 1
  PSCAMT2 MD1 Amount 2
  PSCAMT3 MD1 Amount 3
  PSCAMT4 MD1 Amount 4
  PSCAMT5 MD1 Amount 5
  PSCBUDAMT MD1 Budget amount
  PSCBUDQTY QTY Budget quantity
  PSCESTTOTAMT MD1 Total estimation
  PSCESTTOTQTY QTY Total estimation
  PSCFREEC10A QTY
  PSCFREEC10B MD1
  PSCFREEC6A QTY Quantity
  PSCFREEC6B MD1 Amount
  PSCFREEC7A QTY
  PSCFREEC7B MD1
  PSCFREEC8A QTY
  PSCFREEC8B MD1
  PSCFREEC9A QTY
  PSCFREEC9B MD1
  PSCIMG DCB*14.2
  PSCMARGAMT MD1 Margin amount
  PSCMARGBUD6 COE Ratio on budget
  PSCMARGQTY QTY Margin
  PSCMARGTOT6 COE Ratio on total
  PSCPCTMAMT MD1 Percentage
  PSCPCTMBUD6 COE Budget percentage
  PSCPCTMQTY QTY Percentage
  PSCPCTMTOT6 COE Total percentage
  PSCQTY1 QTY Quantity 1
  PSCQTY2 QTY Quantity 2
  PSCQTY3 QTY Quantity 3
  PSCQTY4 QTY Quantity 4
  PSCQTY5 QTY Quantity 5
  PSCREMAMT MD1 Remaining amount
  PSCREMQTY QTY Remaining quantity
  PSCSEQ L*8 Sequence
  PSCSSS L*8 Session
  PSCTOTAMT MD1 Total amount
  PSCTOTQTY QTY Total quantity
  PSCU UOM Unit -> [TUN]TUN0 =[PJC]PSCU (TABUNIT) !Block
  PSCWIPAMT MD1 WIP amount
  PSCWIPQTY QTY WIP quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJC]UPDUSR (AUTILIS) !Other

## PJMSCCT (PJCCT) - Consolidated expenses
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PJC0 PSCSSS+PSCSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJCCT]CREUSR (AUTILIS) !Other
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJCCT]OPPNUM (PIMPL) !Other
  PBUCOD PBU Budget code
  PBUPAE PBU Parent code
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PJCCT]PCCCOD (PJMCOSTCTR) !Other
  PCCGRP ADI Group -> [ADI]CODE =386;PCCGRP (ATABDIV) !Other
  PCCGRPSOR L*8 Sort
  PSCAMT1 MD1 Amount 1
  PSCAMT2 MD1 Amount 2
  PSCAMT3 MD1 Amount 3
  PSCAMT4 MD1 Amount 4
  PSCAMT5 MD1 Amount 5
  PSCBUDAMT MD1 Budget amount
  PSCBUDQTY QTY Budget quantity
  PSCESTTOTAMT MD1 Total estimation
  PSCESTTOTQTY QTY Total estimation
  PSCFREEC10A QTY
  PSCFREEC10B MD1
  PSCFREEC6A QTY Quantity
  PSCFREEC6B MD1 Amount
  PSCFREEC7A QTY
  PSCFREEC7B MD1
  PSCFREEC8A QTY
  PSCFREEC8B MD1
  PSCFREEC9A QTY
  PSCFREEC9B MD1
  PSCIMG DCB*14.2
  PSCMARGAMT MD1 Margin amount
  PSCMARGBUD6 COE Ratio on budget
  PSCMARGQTY QTY Margin
  PSCMARGTOT6 COE Ratio on total
  PSCPCTMAMT MD1 Percentage
  PSCPCTMBUD6 COE Budget percentage
  PSCPCTMQTY QTY Percentage
  PSCPCTMTOT6 COE Total percentage
  PSCQTY1 QTY Quantity 1
  PSCQTY2 QTY Quantity 2
  PSCQTY3 QTY Quantity 3
  PSCQTY4 QTY Quantity 4
  PSCQTY5 QTY Quantity 5
  PSCREMAMT MD1 Remaining amount
  PSCREMQTY QTY Remaining quantity
  PSCSEQ L*8 Sequence
  PSCSSS L*8 Session
  PSCTOTAMT MD1 Total amount
  PSCTOTQTY QTY Total quantity
  PSCU UOM Unit -> [TUN]TUN0 =[PJCCT]PSCU (TABUNIT) !Block
  PSCWIPAMT MD1 WIP amount
  PSCWIPQTY QTY WIP quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJCCT]UPDUSR (AUTILIS) !Other

## PJMSOLITMD (PSOD) - Sold product list
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSOD0 PSONUM+SEQNUM; PSOD1 PSONUM+OPPNUM (D)
Fields:
  APPLYBPRI M*4 Apply [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BASPRI MD5 Base price
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSOD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PSOD]CUR (TABCUR) !Block
  CUSTOMER BPR Customer -> [BPR]BPR0 =[PSOD]CUSTOMER (BPARTNER) !Block
  DOCNUM VCR Document number
  DOCTYP M*20 Document type [menu 7718: 1=Quote,2=Sales order,3=Direct invoice]
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXTQTY QTY Planned quantity
  EXTUOM UOM Planned unit -> [TUN]TUN0 =[PSOD]EXTUOM (TABUNIT) !Block
  ITMDES DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PSOD]ITMREF (ITMMASTER) !Block
  OPPNUM PIM Project number -> [PIM]PIM0 =[PSOD]OPPNUM (PIMPL) !Block
  PBUCOD PBU Budget code
  PRJLINK PIM Project link -> [PIM]PIM0 =[PSOD]PRJLINK (PIMPL) !Block
  PSOLIN L*8 Project doc line
  PSONUM VCR Project doc number
  QTY QTY Document quantity
  QTYSTU QTY STK quantity
  SAU UOM Sales unit -> [TUN]TUN0 =[PSOD]SAU (TABUNIT) !Block
  SEQNUM L*8 Line number
  STU UOM Stock unit -> [TUN]TUN0 =[PSOD]STU (TABUNIT) !Block
  TASCOD TAC Task code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSOD]UPDUSR (AUTILIS) !Other

## PJMSOLITMH (PSOH) - Sales document creation
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSOH0 PSONUM
Fields:
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AUUID AUUID Single identifier
  BPAADD ADR Delivery address
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[PSOH]BPCINV (BPARTNER) !Block
  BPCORD BPC Sold-to -> [BPC]BPC0 =[PSOH]BPCORD (BPCUSTOMER) !Block
  BPCPYR BPR Pay-by -> [BPR]BPR0 =[PSOH]BPCPYR (BPARTNER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSOH]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PSOH]CUR (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DEMDLVDAT D Required delivery
  DOCDAT D Document date
  DOCREF A*20 Customer reference
  DOCTYP M*20 Document type [menu 7718: 1=Quote,2=Sales order,3=Direct invoice]
  HDOCNUM VCR Document number
  OPPNUM PIM Project number -> [PIM]PIM0 =[PSOH]OPPNUM (PIMPL) !Block
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PSONUM VCR Project doc number
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  RAT1 RCU Reverse
  RAT2 RCU Divisor
  SALFCY FCY Sales site -> [FCY]FCY0 =[PSOH]SALFCY (FACILITY) !Block
  SHIDAT D Shipment date
  SIVTYP TSV Invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Block
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Block
  SQHTYP TSQ Quote type -> [TSQ]TSQ0 =SQHTYP;[V]GSUPCLE (TABSQHTYP) !Block
  STOFCY FCY Shipment site -> [FCY]FCY0 =[PSOH]STOFCY (FACILITY) !Block
  STRDUDDAT D Due date basis
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSOH]UPDUSR (AUTILIS) !Other
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VLYDAT D Validity date

## PJMSOLITMO (PSOO) - Sold product list
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSOO0 PSONUM+OPPNUM+PBUCOD+TASCOD+SEQNUM
Fields:
  AUUID AUUID Single identifier
  BASPRI MD5 Base price
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSOO]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PSOO]CUR (TABCUR) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[PSOO]ITMREF (ITMMASTER) !Block
  OPPNUM PIM Project number -> [PIM]PIM0 =[PSOO]OPPNUM (PIMPL) !Block
  PBUCOD PBU Budget code
  PRODGRPLVL M*20 Product grp. level [menu 7715: 1=Not grouped,2=Project,3=Budget code,4=Task code]
  PSOLIN L*8 Project doc line
  PSONUM VCR Project doc number
  QTY QTY Document quantity
  SAU UOM Sales unit -> [TUN]TUN0 =[PSOO]SAU (TABUNIT) !Block
  SEQNUM L*8 Line number
  TASCOD TAC Task code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSOO]UPDUSR (AUTILIS) !Other

## PJMTIMEMP (PTE) - Time summary
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTE0 CLB+OPPNUM+PTEDAT+PTESEQ; PTE1 PIMTASCOD (D); PTE2 PIMPBUCOD (D); PTE3 CLB-PTEDAT+OPPNUM+PTESEQ
Fields:
  AUUID AUUID Single identifier
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLB AUS Employee -> [AUS]CODUSR =[PTE]CLB (AUTILIS) !Block
  CLBCST MD2 Employee labor rate
  CLBPCC PJCC Employee cost type -> [PJCC]PCC0 =[PTE]CLBPCC (PJMCOSTCTR) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PTE]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PTE]CUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[PTE]FCY (FACILITY) !Block
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPPNUM PIM Project chrono -> [PIM]PIM0 =[PTE]OPPNUM (PIMPL) !Block
  PBUCOD PBU Budget code
  PIMPBUCOD PIM Budget -> [PIM]PIM0 =[PTE]PIMPBUCOD (PIMPL) !Block
  PIMTASCOD PIM Task -> [PIM]PIM0 =[PTE]PIMTASCOD (PIMPL) !Block
  PJMCST MD2 Project labor rate
  PJMPCC PJCC Project cost type -> [PJCC]PCC0 =[PTE]PJMPCC (PJMCOSTCTR) !Block
  POANUM L*8 Sequence
  PTEDAT D Date
  PTEDESAXX AXX Description
  PTEINV M*4 Invoicing flag [menu 1: 1=No,2=Yes]
  PTEORI M Origin [menu 2078: 1=Manual,2=Imported]
  PTEQTY QTY Time spent
  PTESEQ L*8 Sequence
  PTESTA M Status [menu 2074: 1=New,2=Validated,3=Invoiced,4=Posted]
  PTETYP ADI Time category -> [ADI]CODE =640;PTETYP (ATABDIV) !Block
  PTEUOM UOM Time unit -> [TUN]TUN0 =[PTE]PTEUOM (TABUNIT) !Block
  PTEVAL M*4 Validated [menu 1: 1=No,2=Yes]
  TASCOD TAC Task number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PTE]UPDUSR (AUTILIS) !Other

## PJMTIMEMPH (PTEH) - Time summary
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTEH0 CLB
Fields:
  AUUID AUUID Single identifier
  CLB AUS Employee -> [AUS]CODUSR =[PTEH]CLB (AUTILIS) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PTEH]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PTEH]UPDUSR (AUTILIS) !Other

## PJMTIMEMPI (PTI) - Time summary
Notes: activity code PJM; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PTE0 CLB+OPPNUM+PTEDAT+PTESEQ
Fields:
  AUUID AUUID Single identifier
  CLB AUS Employee -> [AUS]CODUSR =[PTI]CLB (AUTILIS) !Block
  CLBCST MD2 Employee labor rate
  CLBPCC PJCC Employee cost type -> [PJCC]PCC0 =[PTI]CLBPCC (PJMCOSTCTR) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PTI]CREUSR (AUTILIS) !Other
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPPNUM PIM Project chrono -> [PIM]PIM0 =[PTI]OPPNUM (PIMPL) !Block
  PBUCOD PBU Budget code
  PJMCST MD2 Project labor rate
  PJMPCC PJCC Project cost type -> [PJCC]PCC0 =[PTI]PJMPCC (PJMCOSTCTR) !Block
  PTEDAT D Date
  PTEQTY QTY Time spent
  PTESEQ L*8 Sequence
  PTETYP ADI Time category -> [ADI]CODE =640;PTETYP (ATABDIV) !Block
  PTEUOM UOM Time unit -> [TUN]TUN0 =[PTI]PTEUOM (TABUNIT) !Block
  PTEVAL M*4 Validated [menu 1: 1=No,2=Yes]
  TASCOD TAC Task number
  TEXTE A*80 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PTI]UPDUSR (AUTILIS) !Other

## PJMTSK (PJTA) - Project task
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTA0 OPPNUM+TASCOD; PTA1 KEYCONCAT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  KEYCONCAT A*40 Concatenation
  OPPNUM PIM Project number -> [PIM]PIM0 =[PJTA]OPPNUM (PIMPL) !Delete
  PBUCOD PBU Budget code
  TASCOD TAC Task code
  TASDATB D Beginning date
  TASDATH D Suspension date
  TASDATL D Launch date
  TASDATP D Planning date
  TASDATS D Closing date
  TASENDDT D End date
  TASFCY FCY Site -> [FCY]FCY0 =[PJTA]TASFCY (FACILITY) !Block
  TASNUM VCR Sequence no.
  TASPAE TAC Parent code
  TASRESP A*10 Supervisor
  TASSTARTDT D Start date
  TASSTATE M*9 Status [menu 2250: 1=New,2=Launched,3=Started,4=Closed,5=Planned,6=,7=,8=,9=Suspended]
  TASTLA M*4 To launch [menu 1: 1=No,2=Yes]
  TASTYP M*16 Task type [menu 2258: 1=Provisional,2=Operational]
  TCACOD CTA Category -> [PTC]CTA0 =[PJTA]TCACOD (PJMTSKCAT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMTSKCAT (PTC) - Project task category
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): CTA0 TCACOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[PTC]PCCCOD (PJMCOSTCTR) !Block
  TASTYP M*12 Task type [menu 2252: 1=Material,2=Labor,3=Mixed,4=Miscellaneous]
  TCACOD CTA Category -> [PTC]CTA0 =[PTC]TCACOD (PJMTSKCAT) !Delete
  TCADESAXX AX3 Description
  TCADESX AX1 Short description
  TCAMOD M*15 Planning [menu 2263: 1=Date of tasks,2=Manual date,3=Calculated date,4=No operation]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PJMTSKDEP (PKD) - Project dependencies
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PKD0 OPPNUM+TASCOD+OPENUM+ITTSEQ; PKD1 OPPNUM+TASCOD+OPENUM (D); PKD2 OPPNUM+TASCOD+ITTSEQ (D); PKD3 OPPNUM+TASCOD (D)
Fields:
  AUUID AUUID Single identifier
  BILL M*4 Billable task [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PKD]CREUSR (AUTILIS) !Other
  DEPITM L*8 Dependency item
  DEPOPE OPE Dependency operation
  ITTSEQ L*8 Sequence
  OPEEND D End date
  OPENUM OPE Operation code
  OPESTR D Start date
  OPPNDEP PIM Dependency project -> [PIM]PIM0 =[PKD]OPPNDEP (PIMPL) !Block
  OPPNUM PIM Project number -> [PIM]PIM0 =[PKD]OPPNUM (PIMPL) !Delete
  PRICE DCB*9.2 Price
  TASCOD TAC Task code
  TASDEP TAC Dependency task
  TASSTATE M*9 Status [menu 2250: 1=New,2=Launched,3=Started,4=Closed,5=Planned,6=,7=,8=,9=Suspended]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PKD]UPDUSR (AUTILIS) !Other

## PJMTSKITM (JTT) - Main product
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): JTT0 OPPNUM+TASCOD+ITTSEQ
Fields:
  ALLQTY QTY Allocated qty.
  ALLSTA M*15 Allocation status [menu 416: 1=Not allocated,2=Partly allocated,3=Allocated]
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSMTYP M*15 Consumption mode [menu 7729: 1=Direct delivery,2=Sales order]
  DLVQTY QTY Delivered quantity
  DLVSTA M*15 Delivery status [menu 7731: 1=Not delivered,2=Partially delivered,3=Delivered,4=No deliverable]
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  FRCDLTALLFLG M*4 Manual WIP closure [menu 1: 1=No,2=Yes]
  ITMDES1 AX3 Description
  ITMDLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  ITMPLANNUM A*30 Plan number
  ITMPLANVER A*30 Plan version
  ITMREF ITM Product -> [ITM]ITM0 =[JTT]ITMREF (ITMMASTER) !Block
  ITTQTY QTY Quantity
  ITTSEQ L*8 Sequence
  ODLQTY QTY Qty. in process
  OPPNUM PIM Project number -> [PIM]PIM0 =[JTT]OPPNUM (PIMPL) !Delete
  SALITM M*20 Sold product [menu 1: 1=No,2=Yes]
  SHTQTY QTY Shortage
  SOQQTY QTY Ordered quantity
  STOFCY FCY Shipment site -> [FCY]FCY0 =[JTT]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  TASCOD TAC Task code
  TASFCY FCY Site -> [FCY]FCY0 =[JTT]TASFCY (FACILITY) !Block
  UOM UOM Unit -> [TUN]TUN0 =[JTT]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WIPNUM VCR Order no.

## PJMTSKOPE (PTKO) - Tasks - Operations
Notes: activity code PJM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PTKO0 OPPNUM+TASCOD+OPENUM+OPESPLNUM; PTKO1 OPPNUM+TASCOD+OPENUM (D); PTKO2 OPPNUM+TASCOD (D)
Fields:
  ALTOPECOD M*4 Routing code ope. [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[PTKO]BPRNUM (BPARTNER) !Block
  CAD DCB*6.4 Rate
  CPLCRG MD8 Actual charge
  CPLLAB WST Actual labor W/C
  CPLLABNBR C*2 Act. no. labor
  CPLOPETIM TIH Actual run time
  CPLPRI MD8 Actual price
  CPLQTY QTY Total completed qty.
  CPLUNTTIM TIH Actual unit time
  CPLWST WST Actual work center
  CPLWSTNBR C*2 Actual resources
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSMQTY QTY Consumed load
  CUR CUR Currency -> [TCU]TCU0 =[PTKO]CUR (TABCUR) !Block
  EFF DCB*3.3 % efficiency
  EQUNUM ITM Tools -> [ITM]ITM0 =[PTKO]EQUNUM (ITMMASTER) !Block
  EXPNUM L*8 Export number
  EXTLAB WST Expected labor work center
  EXTLABNBR C*2 Exp. no. labor
  EXTOPETIM TIH Exp. run time
  EXTPRI MD8 Expected price
  EXTQTY QTY Planned quantity
  EXTSTRQTY QTY Sub-contract quantity
  EXTSTUQTY QTY Expected STK quantity
  EXTUNTTIM TIH Expected unit time
  EXTWST WST Expected W/C
  EXTWSTNBR C*2 Expected resources
  FITCAPEND D End finite capacity
  FITCAPSTR D Finite capacity start
  FRCSTRDAT D Sched forced scheduling
  FRCSTRHOU HM Forced scheduling time
  FXGNUM A*20 Fixture
  INFCAPEND D End date
  INFCAPSTR D Start date
  INVQTY QTY Invoiced qty.
  OPECST MS1 Hourly rate
  OPECST2 MD8 Labor rate
  OPEDATH D Suspension date
  OPEDATS D Date closed
  OPEEND D End date
  OPEENDDT D Actual end date
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPENUMLEV C*1 Operation suffix
  OPEPLNNUM A*20 Operation plan
  OPEROUPCT A*20 Operation image
  OPESPLNUM C*4 Operation split
  OPESTA M*15 Operation status [menu 308: 1=Pending,2=Previous operation in process,3=Previous operation closed,4=In process,5=Closed,6=Excluded,7=Ordered]
  OPESTARTDT D Actual start date
  OPESTR D Start date
  OPESTRCOE COE SUSCU/OU factor
  OPESTUCOE COE STK-OPE conversion
  OPEUOM UOM Operation UOM -> [TUN]TUN0 =[PTKO]OPEUOM (TABUNIT) !Block
  OPEUOM2 UOM Unit -> [TUN]TUN0 =[PTKO]OPEUOM2 (TABUNIT) !Block
  OPPNUM PIM Project number -> [PIM]PIM0 =[PTKO]OPPNUM (PIMPL) !Delete
  OPSNUM VCR Load no.
  PIO C*2 Priority
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PRGNUM A*20 Program
  QUACPLQTY QTY Actual QC quantity
  REFPRI MD8 Reference price
  REJCPLQTY QTY Actual rejected qty.
  RMNQTY QTY Remaining load
  ROODESAXX AXX Description
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  ROUOPENUM OPE Operation no.
  RPLIND C*3 Alternate index
  RSTMAC A*5 Machine restriction
  SCHGRP A*15 Grouping criterion
  SCHSBB A*15 Distinction criteria
  SCOCOD M*15 Subcontract [menu 311: 1=No,2=Normal,3=By exception]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[PTKO]SCOITMREF (ITMMASTER) !Block
  SCOLTI LTI Subcontract LT
  SCOPUU UOM Purchase unit -> [TUN]TUN0 =[PTKO]SCOPUU (TABUNIT) !Block
  SCOWST WST Subcontract work C
  SETLABCOE DCB*3.3 Labor time set fac
  SHR DCB*3.3 Shrinkage in %
  SPLCOD M*15 Splitting [menu 304: 1=None,2=Equal quantities,3=Equal run times,4=Equal run times / 1 rule,5=Equal quantities + efficiency]
  SPLMAXNBR C*4 Max splits
  STDLAB WST Standard labor
  STDLABNBR C*2 Std no. labor
  STDOPENUM ROT Standard operation
  STDOPETIM TIH Standard run time
  STDQTY QTY Standard quantity
  STDUNTTIM TIH Standard unit time
  STDWST WST Standard position
  STDWSTNBR C*2 Std no. workcenters
  TASCOD TAC Task code
  TASFCY FCY Site -> [FCY]FCY0 =[PTKO]TASFCY (FACILITY) !Block
  TECCRD A*8 Technical sheet
  TIMCOD M*15 Management unit [menu 303: 1=Time for 1,2=Time for 100,3=Time for 1000,4=Time per lot]
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WIPNUM VCR WIP no.
  WSTEFF DCB*3.3 Post efficiency
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]

## PLMDEFVAL (PDV) - PLM default values
Keys (first = PK; D = duplicates allowed): PDV0 ID+CODFIC+CODZONE
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[PDV]CODFIC (ATABLE) !Delete
  CODZONE AVA Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  ID A*10 Identifier
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VALDEF A*80 Default value

## PLMPAR (PPA) - PLM setup
Notes: differs in V10 P1 (diff: ATD_PLMPAR.htm)
Keys (first = PK; D = duplicates allowed): PPA0 ID
Fields:
  ADDEML1 MAI Email address
  ADDEML2 MAI Email address
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =2;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMPIT PIT BOM set (pivot) -> [PIT]PIT0 =BOMPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DRTISS A*250 Index destination
  DRTRCP A*250 Directory to be scanned
  DRTSTO A*250 Storage directory
  ID A*10 Identifier
  INTIT DES Description
  ITMPIT PIT Product set (pivot) -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILISS ASTO*250 Index destination
  VOLFILRCP ASTO*250 Directory to be scanned
  VOLFILSTO ASTO*250 Storage directory

## POPUL (HRPOP) - Employee populations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## POPULA (HRPOA) - Employee populations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## POPULB (POB) - Employee populations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PORQRC (PORQRC) - Portuguese QR-data
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PORQRC0 DOCTYP+DOCNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PORQRC]CREUSR (AUTILIS) !Other
  DOCNUM VCR Document number
  DOCTYP A*5 Entry type
  IMGQRC ABB QR image
  QRC_A A*9
  QRC_B A*30
  QRC_C A*12 Customer country
  QRC_D A*2 Document type
  QRC_E A*1 Document status
  QRC_F A*8 Document date
  QRC_G A*60 Document ID
  QRC_H A*70 ATCUD
  QRC_I1 A*5
  QRC_I2 A*16
  QRC_I3 A*16
  QRC_I4 A*16
  QRC_I5 A*16
  QRC_I6 A*16
  QRC_I7 A*16
  QRC_I8 A*16
  QRC_J1 A*5
  QRC_J2 A*16
  QRC_J3 A*16
  QRC_J4 A*16
  QRC_J5 A*16
  QRC_J6 A*16
  QRC_J7 A*16
  QRC_J8 A*16
  QRC_K1 A*5
  QRC_K2 A*16
  QRC_K3 A*16
  QRC_K4 A*16
  QRC_K5 A*16
  QRC_K6 A*16
  QRC_K7 A*16
  QRC_K8 A*16
  QRC_L A*16 Not subject to VAT
  QRC_M A*16
  QRC_N A*16
  QRC_O A*16 Document total
  QRC_P A*16 Withholding tax
  QRC_Q A*4 Hash code
  QRC_R A*4 Certificate number
  STAQRC M*4 QR image status [menu 1: 1=No,2=Yes]
  STRQRC A*250
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PORQRC]UPDUSR (AUTILIS) !Other

## POSTE (POT) - Position
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## POSTEDEF (POD) - Item default value
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## POSTEHAB (PHA) - Authorizations
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## POSTEKSA (PSS) - Additional RSA fields
Notes: activity code FKGPH; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PPREASON (PPR) - Purchase price reasons
Keys (first = PK; D = duplicates allowed): PPR0 PRIREN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACMAN M*4 Manual entry [menu 1: 1=No,2=Yes]
  DES DES Description
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  LANDESSHO A*60 Descriptions
  PRIREN C*2 Reason
  PRIRENCAR A*3 Alpha no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDPRI M*4 Price change [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user

## PPRICCONF (PPC) - Supplier pricing parameters
Keys (first = PK; D = duplicates allowed): PPC0 PLI; PPC1 PLIENAFLG+PLITYP+PIO+PLI
Fields:
  ABB A*3(5) Abbreviation
  ATICNVFLG M*4 Conversion - / +tax [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  COMPRO M*15 Comm factor [menu 244: 1=Yes,2=No,3=Initialization]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRIBPR C*1 BP criterion
  CRIBPSNUM C*1 Supplier criterion
  CRICURNUM C*1 Currency criterion
  CRIDES A*20(5) Criterion title
  CRIDIE DIE(5) Dimension type code -> [DIE]DIE0 =[PPC]CRIDIE (GDIE) !Block
  CRIIND C*4(5) Criterion index
  CRIITM C*1 Product criterion
  CRIITMNUM C*1 Product criterion
  CRILEN DCB*5(5) Field length
  CRINBR C*1 Numbers of criteria
  CRIUOMNUM C*1 Unit criterion
  CUR CUR Currency -> [TCU]TCU0 =[PPC]CUR (TABCUR) !Block
  CURCNVFLG M*4 Currency conversion [menu 1: 1=No,2=Yes]
  DESAXX AX3 Description
  DISCRGPRO M*15 Charge/Discount processing [menu 244: 1=Yes,2=No,3=Initialization] act:PPR
  EXPNUM L*8 Export number
  FIL AVA(5) Table
  FLD AVA(5) Field
  FLDTYP ATY(5) Field type -> [ATY]CODTYP =[PPC]FLDTYP (ATYPE) !Block
  FLDTYPCPL A*10(5) Supplement type
  FOCPRO M*15 Free products [menu 273: 1=No,2=Same product,3=Other products,4=Order total]
  FOCTYP M*15 Free type [menu 274: 1=Threshold,2=Multiple]
  LANDESSHO A*60 Descriptions
  LIEN M*5(5) Link [menu 49: 1=No,2=Long,3=Short]
  PIO C*3 Priority
  PLI PPC Price list code -> [PPC]PPC0 =[PPC]PLI (PPRICCONF) !Other
  PLIBPRCNR MM*15 BP concerns [menu 2210: 1=Outside group,2=Group,3=All]
  PLIENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  PLISEA C*1 Price search
  PLISTC PRS Structure code -> [PRS]PRS0 =2;PLISTC (PRICSTRUCT) !Block
  PLITYP M*10 Price list type [menu 241: 1=Normal,2=Grouped,3=Restricted,4=Component]
  PPUMNU C*3(5) Local menu
  PRIFLD A*250 Base price field
  PRIIND C*4 Base price index
  PRIPRO M*15 Price processing [menu 270: 1=No,2=Value,3=Value for N,4=Factor,5=Calculation]
  PRIQTYFLG M*15 Price/Quantity [menu 239: 1=No,2=Yes,3=Quantity bands,4=Gross price bands,5=Net price bands]
  PRIREN PPR Reason -> [PPR]PPR0 =[PPC]PRIREN (PPREASON) !Block
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  UOMCNVFLG M*4 Unit conversion [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDNULPRI M*4 Update zero price [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user

## PPRICFICH (PPF) - Supplier prices (records)
Keys (first = PK; D = duplicates allowed): PPF0 PLI+PLICRD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  LINNBR C*4 Number of lines
  PLI PPC Price list code -> [PPC]PPC0 =[PPF]PLI (PPRICCONF) !Delete
  PLICRD VCR Price list record
  PLICRDIDX A*10 Index
  PLIENDDAT D Validity end date
  PLISTRDAT D Validity start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## PPRICLIST (PPL) - Supplier price lists
Keys (first = PK; D = duplicates allowed): PPL0 PLI+PLICRD+PLILIN; PPL1 PLI+PLICRI+PLISTRDAT (D); PPL2 PLI+PLICRI1+PLISTRDAT (D); PPL3 PLI+PLICRI2+PLISTRDAT (D)
Fields:
  AUUID AUUID Single identifier
  COMCOE CCR Comm factor
  CPNITMREF ITM Component -> [ITM]ITM0 =[PPL]CPNITMREF (ITMMASTER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PPL]CUR (TABCUR) !Block
  DCGVAL MD8 Charge/discount value act:PPR
  EXPNUM L*8 Export number
  FOCAMTBKT MD1 Free Class
  FOCAMTMIN MD1 Free threshold
  FOCITMREF ITM Free product -> [ITM]ITM0 =[PPL]FOCITMREF (ITMMASTER) !Block
  FOCQTY QTY Free quantity
  FOCQTYBKT QTY Free Class
  FOCQTYMIN QTY Free threshold
  FOCUOM UOM Unit -> [TUN]TUN0 =[PPL]FOCUOM (TABUNIT) !Block
  IMPNUMLIG L*8 Import line
  LTI C*3 Lead time
  MAXAMT MD1 Maximum value
  MAXQTY QTY Maximum quantity
  MINAMT MD1 Minimum value
  MINQTY QTY Minimum quantity
  PLI PLI Price list code
  PLICRD VCR Price list record
  PLICRI PPX Criteria
  PLICRI1 PPU Criteria 1
  PLICRI2 PPU Criteria 2
  PLICRI3 PPU Criterion 3
  PLICRI4 PPU Criterion 4
  PLICRI5 PPU Criterion 5
  PLIENDDAT D Validity end date
  PLILIN L*8 Line
  PLISTRDAT D Validity start date
  PRI MD8 Price
  PRIDIV C*4 Price factor
  UOM UOM Unit -> [TUN]TUN0 =[PPL]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PREREPORT (PPP) - Calculate crystal report currency
Keys (first = PK; D = duplicates allowed): PPP0 NUM+TYPOBJ+CUR
Fields:
  AMT1 DCB*9.2 Amount
  AMT2 DCB*9.2 Amount
  AMT3 DCB*9.2 Amount
  AMT4 DCB*9.2 Amount
  AMT5 DCB*9.2 Amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PPP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PPP]CUR (TABCUR) !Block
  NUM A*15 Key
  TYPOBJ A*3 Object type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PPP]UPDUSR (AUTILIS) !Other

## PRESTATION (PSN) - Service provision
Notes: activity code FINTM; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PRESTCOV (PCO) - Covered services
Keys (first = PK; D = duplicates allowed): PCO0 CONNUM+TPL+MACNUM+TYPSVC (D)
Fields:
  AUUID AUUID Single identifier
  CONNUM CON Contract code -> [CON]CON0 =[PCO]CONNUM (CONTSERV) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PCO]CREUSR (AUTILIS) !Other
  LNDAUZ M*4 Authorized loan [menu 1: 1=No,2=Yes]
  MACNUM MAC Machine code -> [MAC]MAC0 =[PCO]MACNUM (MACHINES) !Block
  MAXCOV MD1 Maximum coverage
  MINCOV MD1 Minimum coverage
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  TYPSVC ADI Covered services -> [ADI]CODE =407;TYPSVC (ATABDIV) !RTZ
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PCO]UPDUSR (AUTILIS) !Other

## PRICSTRUCT (PRS) - Price structure (cust/supp)
Keys (first = PK; D = duplicates allowed): PRS0 BPCBPS+PLISTC
Fields:
  AUUID AUUID Single identifier
  BPCBPS M*15 Customer/Supplier [menu 242: 1=Customer,2=Supplier]
  BPCBPSCAR A*1 Alpha no.
  CLCRUL M*15(9) Calculation basis [menu 276: 1=By unit,2=By line,3=By document]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX2(9) Description
  EXPNUM L*8 Export number
  FMTCOL A*15(9) Column format
  INCDCR M*10(9) Increase/Decrease [menu 254: 1=Increase,2=Decrease]
  INVDTA SFI(9) Invoicing element -> [SFI]SFI0 =[PRS]INVDTA (SFOOTINV) !Other
  LANDESSHO A*50(9) Descriptions
  NPRNOTFLG M*4(9) Net price excl tax line [menu 1: 1=No,2=Yes]
  NPRVLTFLG M*4(9) Net price increase [menu 1: 1=No,2=Yes]
  PLISTC A*10 Structure code
  SHOAXX AX1(9) Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALTYP M*10(9) Value type [menu 255: 1=Amount,2=% combined,3=% series]

## PROFIL (PRF) - Employee profile
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PROFILDEF (HRPFD) - Employee profile Default values
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PYRAPAR (PYRA) - HRMS payroll NA setup
Notes: activity code PYRA
Keys (first = PK; D = duplicates allowed): PYRA0 ID
Fields:
  AUUID AUUID Single identifier
  CCETPL AOE Dimensions -> [AOE]AOE0 =[PYRA]CCETPL (AOBJEXT) !Block
  CREDATTIM ADATIM Date time
  CREUSR A*10 Creation user
  DACDIA GDE Transaction -> [GDE]DIA =[PYRA]DACDIA (GDIAENTRY) !Block
  DRTSTO A*250 Storage directory
  DRTWRK A*250 Work directory
  GACTPL AOE Accounts -> [AOE]AOE0 =[PYRA]GACTPL (AOBJEXT) !Block
  GASTPL AOE Journals -> [AOE]AOE0 =[PYRA]GASTPL (AOBJEXT) !Block
  ID A*10 Identifier
  INTIT DES Description
  JOU JOU Journal -> [JOU]JOU0 =JOU;LEG (GJOURNAL) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TYP GTE Payroll doc type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDATTIM ADATIM Date time
  UPDUSR A*10 Change author

## QLYCRD (QLC) - Technical sheets
Keys (first = PK; D = duplicates allowed): QLC0 QLYCRD+NUMLIN; QLC1 QLYCRDDES+NUMLIN (D); QLC2 SEQ+QLYCRD+NUMLIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  NUMLIN C*4 Line
  QLYCRD A*8 Technical sheet
  QLYCRDDES DES Record title
  QLYDESAXX AX3 Record title
  QSTNUM QST Question -> [QLQ]QLQ0 =[QLC]QSTNUM (QLYCRDQST) !Block
  QSTTEXAXX AXX Text
  RPLQLYCRD A*8 New record
  SEQ L*6 Sequence
  TEX A*50 Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## QLYCRDASW (QLA) - Quality records - responses
Keys (first = PK; D = duplicates allowed): QLA0 QLYCTLDEM+VCRLIN+CRDSEQ+QSTNUM
Fields:
  ALPASW A*50 Answer
  ASW A*50 Answer
  AUUID AUUID Single identifier
  CRDSEQ L*8 Seq no. analysis file
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATASW D Answer
  EXPNUM L*8 Export number
  FLGASW M*4 Answer [menu 1: 1=No,2=Yes]
  GPG ADI Grouping -> [ADI]CODE =102;GPG (ATABDIV) !Block
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[QLA]ITMREF (ITMMASTER) !Block
  NUMASW DCB*13 Answer
  OSDASW M*4 Non-standard response [menu 1: 1=No,2=Yes]
  PRNCOD M*4 Printing [menu 1: 1=No,2=Yes]
  QLYCRD A*8 Quality record
  QLYCTLDEM VCR Analysis request
  QSTNUM QST Question -> [QLQ]QLQ0 =[QLA]QSTNUM (QLYCRDQST) !Block
  RPLQLYCRD A*8 New record
  TRKTYP M*20 Tracking type [menu 285: 1=Quality control tracking,2=Work order tracking]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*5 Line no. analyzed

## QLYCRDNQA (NQA) - Sampling: AQL criteria
Keys (first = PK; D = duplicates allowed): NQA0 COD+NQA+CODSMP
Fields:
  AUUID AUUID Single identifier
  COD C*2 AQL criteria code
  CODSMP A*3 Sampling code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  NQA M*15 AQL [menu 2758: 1=1.0,2=1.5,3=2.5,4=4.0,5=6.5,6=10,7=15,8=25,9=40,10=65,11=100,12=0.0]
  QTYACP L*6 Acceptance
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## QLYCRDQST (QLQ) - Quality records - questions
Keys (first = PK; D = duplicates allowed): QLQ0 QSTNUM
Fields:
  ALPDEFASW A*20 Default response
  ALPENDVAL A*20 End date
  ALPNMNVAL A*20 Nominal value
  ALPSTRVAL A*20 Start range
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEMASWTYP M*15 Response type [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  DEMCTLTYP M*15 Control type [menu 253: 1=Value list,2=Ranges,3=No control]
  ENDVALFOR FOR End range formula -> [TFO]TFO0 =32;ENDVALFOR (TABFOR) !Block
  EXPNUM L*8 Export number
  GPG ADI Grouping -> [ADI]CODE =102;GPG (ATABDIV) !Block
  LOKTYP M*20 Blocking type [menu 266: 1=No block,2=Operation block,3=Status block,4=Next sheet]
  NUMDEFASW DCB*13 Default response
  NUMENDVAL DCB*13 End date
  NUMNMNVAL DCB*13 Nominal value
  NUMSTRVAL DCB*13 Start range
  OSDASW M*4 Non-standard response [menu 1: 1=No,2=Yes]
  PRNCOD M*4 Printing [menu 1: 1=No,2=Yes]
  QSTDES DES Question title
  QSTDESAXX AX3 Question title
  QSTNUM A*8 Question
  QSTSHO SHO Short description
  QSTSHOAXX AX1 Short description
  RPLQLYCRD A*8 New record
  STRVALFOR FOR Start range formula -> [TFO]TFO0 =32;STRVALFOR (TABFOR) !Block
  TCT TCT Control table -> [TCT]TCT0 =TCT;1 (TABCTL) !Block
  UOM UOM Unit -> [TUN]TUN0 =[QLQ]UOM (TABUNIT) !Other
  UOMDEC C*1 Decimals
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## QLYWRK (QLW) - Work file - responses
Keys (first = PK; D = duplicates allowed): QLW0 PRONUM+LINNUM+QSTNUM
Fields:
  ALPASW A*50 Answer
  ASW A*50 Answer
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATASW D Answer
  FLGASW M*4 Answer [menu 1: 1=No,2=Yes]
  GPG ADI Grouping -> [ADI]CODE =102;GPG (ATABDIV) !Block
  IPTDAT D Allocation date
  LINNUM L*8 Line number
  NUMASW DCB*13 Answer
  OPENUM OPE Operation
  OSDASW M*4 Non-standard response [menu 1: 1=No,2=Yes]
  PRNCOD M*4 Printing [menu 1: 1=No,2=Yes]
  PRONUM L*8 Process number
  QSTNUM QST Question -> [QLQ]QLQ0 =[QLW]QSTNUM (QLYCRDQST) !Block
  RPLQLYCRD A*8 New record
  TECCRD A*8 Technical sheet
  TRKTYP M*20 Tracking type [menu 285: 1=Quality control tracking,2=Work order tracking]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QLW]UPDUSR (AUTILIS) !Other
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## QUEUE (QUE) - Queue
Keys (first = PK; D = duplicates allowed): QUE0 NUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[QUE]CREUSR (AUTILIS) !Other
  DES CLX Description
  NUM VCR Code
  NUMFULDES CLC Chrono txt file
  QUEDESAXX AXX Description
  TTR DCO Description
  TYPFULDES CLT Type text file
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[QUE]UPDUSR (AUTILIS) !Other

## REACHPAR (RPA) - REACH setup
Keys (first = PK; D = duplicates allowed): RPA0 ID
Fields:
  AUUID AUUID Single identifier
  BPSFOR FOR Selection formula -> [TFO]TFO0 =50;ITMFOR (TABFOR) !Block
  BPSPIT PIT Suppliers -> [PIT]PIT0 =BPSPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DRTWRK A*250 Work directory
  ID A*10 Identifier
  INTIT DES Description
  ITMFOR FOR Selection formula -> [TFO]TFO0 =41;ITMFOR (TABFOR) !Block
  ITMPIT PIT Products -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  ITMSRT M*15 Sort [menu 2270: 1=Product,2=Supplier]
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILWRK ASTO*250 Work directory

## REPSEC (RSE) - Secondary marketing contacts
Keys (first = PK; D = duplicates allowed): RSE0 BPCNUM+REPNUM; RSE1 BPCNUM (D)
Fields:
  AUTASS C*4 Auto allocation
  AUUID AUUID Single identifier
  BPCNUM BPR Customer code -> [BPR]BPR0 =[RSE]BPCNUM (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RSE]CREUSR (AUTILIS) !Other
  GRPITM ADI Product group -> [ADI]CODE =19+GFAMCIA;GRPITM (ATABDIV) !Block
  MSS ADI Role -> [ADI]CODE =414;MSS (ATABDIV) !Block
  REPNUM REP Sales rep code -> [REP]REP0 =[RSE]REPNUM (SALESREP) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RSE]UPDUSR (AUTILIS) !Other

## RETROCTR (RCR) - Back-pay - Employees
Notes: activity code HRPAY; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## RITDUD (RIU) - Withholdings by open item
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## RITENZIONE (RTZ) - Table of withholding codes
Keys (first = PK; D = duplicates allowed): RTZ0 RITCOD
Fields:
  ACC1 GAC Cash account -> [GAC]GAC0 =COA;ACC1 (GACCOUNT) !Block
  ACC2 GAC Charge account -> [GAC]GAC0 =COA;ACC2 (GACCOUNT) !Block
  AMTFXD DCB*19.8 Fixed amount act:KAG
  AUUID AUUID Single identifier
  BAS M*4(30) Included in base [menu 1: 1=No,2=Yes]
  BASEXE DCB*19.8 Min not taxable act:KAG
  BASMIN DCB*19.8 Min base taxable act:KAG
  BASRAT DCB*9.2 Allowance rate
  BASRTZ C*4 Withholding calc. basis act:KAG
  BASTSD C*4 Base threshold act:KAG
  BKT MD0(9) Brackets
  CAT M*4 Withholding type [menu 950: 1=At source,2=INPS,3=ENASARCO,4=FIRR,5=Other,6=VAT,7=Gross income,8=Gains,9=SUSS,10=W3,11=W4]
  COA COA Chart code -> [COA]COA0 =[RTZ]COA (GCOA) !Block
  COE1 DCB*9.2 Supp charge coeff
  COE2 DCB*9.2 Enterprise coeff
  COU A*1 Sequence number act:KAG
  CREDAT D Creation date
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  ENDDAT D End of application
  EXPNUM L*8 Export no.
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LEGCOD A*20 Legal code
  MET M*4 Calculation method [menu 952: 1=Single rate,2=Rate per installment,3=Min./Max threshold]
  PAYPRT C*4 Partial payment act:KAG
  RAT DCB*9.2(10) Rate
  RITCOD RTZ Withholding code -> [RTZ]RTZ0 =[RTZ]RITCOD (RITENZIONE) !Other
  SAT A*1 Province act:KAG
  SHO SHO Short description
  STRDAT D Start of application
  TSDBKT DCB*19.8 Threshold act:KAG
  TYP M*4 Withholding type [menu 951: 1=On payment,2=On invoice]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## RITHIS (RTH) - History of paid withholdings
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): RTH0 PAYNUM+PIHNUM+RITCOD
Fields:
  AMT MD1 Amount
  AUUID AUUID Single identifier
  BAS MD1 Basis
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RTH]CREUSR (AUTILIS) !Other
  PAYNUM VCR Payment
  PIHNUM VCR Invoice
  RITCOD RTZ Withholding code -> [RTZ]RTZ0 =[RTH]RITCOD (RITENZIONE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RTH]UPDUSR (AUTILIS) !Other

## RITMVT (RTM) - Withholding movements
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): RTM0 BPR+RITCOD+CPY+ANN
Fields:
  AMTANN MD1 Amount
  ANN C*4 Civil year
  AUUID AUUID Single identifier
  BASANN MD1 Basis
  BPR BPR BP -> [BPR]BPR0 =[RTM]BPR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[RTM]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RTM]CREUSR (AUTILIS) !Other
  RITCOD RTZ Withholding code -> [RTZ]RTZ0 =[RTM]RITCOD (RITENZIONE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RTM]UPDUSR (AUTILIS) !Other

## RPTDS (RDS) - Report electronic signatures
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): RDS0 CRYCOD+LAN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RDS]CREUSR (AUTILIS) !Other
  CRYCOD ACR Crystal reports
  DIGSIGN ABB Electronic signature
  LAN LAN Language -> [TLA]TLA0 =[RDS]LAN (TABLAN) !Block
  LASDAT D Last date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RDS]UPDUSR (AUTILIS) !Other

## SAFTPTTMP1 (SAFTP) - SAF-T
Notes: activity code SAFT
Keys (first = PK; D = duplicates allowed): SAFTP0 COD+EECNUM
Fields:
  AUUID AUUID Single identifier
  COD A*30 Export no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SAFTP]CREUSR (AUTILIS) !Other
  EECNUM A*20 EU VAT no. act:DEB
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SAFTP]UPDUSR (AUTILIS) !Other

## SALESREP (REP) - Sales rep
Keys (first = PK; D = duplicates allowed): REP0 REPNUM; REP1 AUSNUM (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =4;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUSNUM AUS User code -> [AUS]CODUSR =[REP]AUSNUM (AUTILIS) !RTZ
  AUUID AUUID Single identifier
  BPAADD ADR Default address
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFY CPY Company -> [CPY]CPY0 =[REP]CFY (COMPANY) !Other act:MUL
  CLLDEL L*8 No. of late calls
  COMBAS M*15 Commission base [menu 405: 1=% on net price,2=% on margin,3=% on calculation formula]
  COMFOR1 FOR Commission formula 1 -> [TFO]TFO0 =3;COMFOR1 (TABFOR) !Block
  COMFOR2 FOR Commission formula 2 -> [TFO]TFO0 =3;COMFOR2 (TABFOR) !Block
  COMRAT1 RAT Commission rate 1 act:COM
  COMRAT2 RAT Commission rate 2 act:COM
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[REP]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[REP]DIE (GDIE) !Block act:ANA
  EXPNUM L*8 Export number
  FCY FCY Sales site -> [FCY]FCY0 =[REP]FCY (FACILITY) !Block
  NSE L*8 No. of reschedules
  OBJCLL L*8 Call objective
  REPNAM NAM Last name
  REPNUM BPR Sales rep -> [BPR]BPR0 =[REP]REPNUM (BPARTNER) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SCALE (HRSCA) - Level scale
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SCALED (HRSDD) - Detail level scale
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SCREMPD (HRSMD) - Employee screens
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SCREMPH (HRSMH) - Employee screens
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SEARESULT (LUP) - Search result
Keys (first = PK; D = duplicates allowed): LUP0 OBJNUM (D); LUP1 RESNUM (D); LUP2 SSS (D); LUP3 OBJNUM+SSS
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LUP]CREUSR (AUTILIS) !Other
  OBJNUM BPR Record code -> [BPR]BPR0 =[LUP]OBJNUM (BPARTNER) !Other
  RESNUM L*8 Result no.
  SSS A*30 Session
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LUP]UPDUSR (AUTILIS) !Other

## SEASON (SES) - Trend profiles
Keys (first = PK; D = duplicates allowed): SES0 SESCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D(53) End date
  SESAMT DCB*11.4(53) Distribution key
  SESCOD A*3 Trend profile
  SESDES DES Description
  SESDESAXX AX3 Description
  SESNBR C*4 Lines
  SESRND M*15 Lot rounding [menu 268: 1=None,2=Round up,3=Round down,4=One lot minimum]
  SESSHO SHO Short description
  SESSHOAXX AX1 Short description
  STRDAT D(53) Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SEAUTH (SEU) - Credit card authorizations
Notes: activity code SEPP
Keys (first = PK; D = duplicates allowed): SEU0 VCRTYP+VCRNUM+VCRSEQ; SEU1 TXNID (D); SEU2 SOHNUM (D); SEU3 SDHNUM (D); SEU4 SIHNUM (D); SEU5 BPCNUM+ACCNCKNAM (D)
Fields:
  ACCL4D A*4 Last four digits
  ACCNCKNAM A*15 Account nickname
  AUTAMT MD1 Authorization amount
  AUTDAT D Authorization date
  AUTID A*15 Authorization code
  AUTMSG A*32 Message
  AUUID AUUID Single identifier
  BPCNUM BPR Customer -> [BPR]BPR0 =[SEU]BPCNUM (BPARTNER) !Delete
  CRDTYP ADI Card type -> [ADI]CODE =398;CRDTYP (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SEU]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SEU]CUR (TABCUR) !Block
  EXPDAT D Expiration
  MANAUT M*4 Manual authorization [menu 1: 1=No,2=Yes]
  MANAUTUSR AUS User -> [AUS]CODUSR =[SEU]MANAUTUSR (AUTILIS) !Other
  ORIGAUTH MD1 Original auth amount
  ORIGAUTID A*15 Authorization ID
  ORIGTXNID A*50 Transaction ID
  ORIGVPSTXID A*38 Transaction ID
  PAYAMT MD1 Payment amount
  PAYDAT D Payment date
  PAYID A*15 Payment code
  PAYNUM VCR Payment number
  POSTAUT C*4 Post
  PRCCOD SEP Processing code -> [SER]SER0 =[SEU]PRCCOD (SEPRC) !Block
  SDHNUM VCR Delivery no.
  SIHNUM VCR Invoice no.
  SOHNUM VCR Order no.
  SPSECKEY A*10 Security key
  STAFLG M*15 Status [menu 2095: 1=Selected,2=Verified,3=Authorized,4=Rejected,5=Voided,6=Captured,7=Settled,8=Manual]
  TAXAMT MD1 Tax amount
  TXNID A*50 Transaction
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SEU]UPDUSR (AUTILIS) !Other
  VANREF A*20 VAN reference
  VCRNUM VCR Entry
  VCRSEQ L*8 Document sequence no.
  VCRTYP C*4 Entry type
  VCRTYPORI C*4 Source document type
  VPSTXID A*38 Transaction ID

## SEBPC (SEB) - Payment gateway customer data
Notes: activity code SEPP
Keys (first = PK; D = duplicates allowed): SEB0 BPCNUM+ACCNCKNAM
Fields:
  ACCL4D A*4 Last four digits
  ACCNAM NAM Name
  ACCNCKNAM A*15 Account nickname
  ADDLIG ADL(3) Address
  AUUID AUUID Single identifier
  BPCNUM BPR Customer -> [BPR]BPR0 =[SEB]BPCNUM (BPARTNER) !Delete
  CRDTYP ADI Card type -> [ADI]CODE =398;CRDTYP (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SEB]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[SEB]CRY (TABCOUNTRY) !Block
  CTY CTY City
  EMAIL MAI Email address
  EXPDAT D Expiration
  FLACT M*6 Active flag [menu 1: 1=No,2=Yes]
  FLDEF M*6 Default [menu 1: 1=No,2=Yes]
  FSTNAM A*20 First name
  LSTNAM A*20 Last name
  ONETIME M*4 One time use card [menu 1: 1=No,2=Yes]
  POSCOD POS Postal code
  PRCCOD SEP Processing code -> [SER]SER0 =[SEB]PRCCOD (SEPRC) !Block
  SAT SAT Region
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SEB]UPDUSR (AUTILIS) !Other
  USEBILLADR M*10 Billing address [menu 1: 1=No,2=Yes]
  VLTGUID A*50 Vault GUID
  VLTID A*50 Vault ID
  VLTREQ L*8 Request

## SEPAR (SEP) - Payment gateways
Notes: activity code SEPP; differs in V9.0 P12 (diff: AT3_SEPAR.htm)
Keys (first = PK; D = duplicates allowed): SEP0 JAVSRV
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SEP]CREUSR (AUTILIS) !Other
  JAVSRV A*15 Java server
  POLL C*4 Poll duration
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SEP]UPDUSR (AUTILIS) !Other
  USEPRDURL M*4 URL type [menu 1: 1=No,2=Yes]

## SEPRC (SER) - Payment gateway setup
Notes: activity code SEPP
Keys (first = PK; D = duplicates allowed): SER0 PRCCOD
Fields:
  AUTDAY C*4 Authorized days
  AUTPCT DCB*2.2 Authorized markup %
  AUTSTP M*15 Authorization step [menu 2093: 1=Order entry,2=Post order]
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[SER]BAN (BANK) !Block
  BKO M*4 Auto [menu 1: 1=No,2=Yes]
  CDTTYP TPY Credit type -> [TPY]TPY0 =CDTTYP;[V]GSUPCLE (TABPAYTYP) !Block
  CPY CPY Company -> [CPY]CPY0 =[SER]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SER]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SER]CUR (TABCUR) !Block
  FLACT M*6 Active flag [menu 1: 1=No,2=Yes]
  FLDEF M*6 Default [menu 1: 1=No,2=Yes]
  MERID A*12 Merchant ID
  MERKEY A*24 Merchant key
  MERVAL M*4 Validated [menu 1: 1=No,2=Yes]
  MINAMT MD1 Minimum amount
  PAYPRC M*4 Payment processor [menu 2098: 1=Sage Exchange,2=Sage Pay]
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  PRCCOD A*10 Processing code
  PRCDES DES Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SER]UPDUSR (AUTILIS) !Other
  VENDID A*15 Vendor code
  VERIF M*4 Verification [menu 1: 1=No,2=Yes]
  VERIFAMT DCB*3.2 Verification amount

## SERREQUEST (SRE) - Service requests
Notes: differs in V9.0 P12 (diff: AT3_SERREQUEST.htm); differs in V10 P1 (diff: ATD_SERREQUEST.htm)
Keys (first = PK; D = duplicates allowed): SRE0 SRENUM; SRE1 CREDAT (D); SRE2 CREDAT+SRENUM; SRE3 SREBPC (D); SRE4 SRECCN (D); SRE5 SREBPC+SRENUMBPC (D); SRE6 SOLNUM (D); SRE7 SREORI+SREORIVCR+SREORIVCRL (D); SRE8 SRERESDAT+SRERESHOU+SREASS+SRENUM
Fields:
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CONSPT CON Support contract -> [CON]CON0 =[SRE]CONSPT (CONTSERV) !Block
  CONSPTFLG C*1 Support contract flg
  CONSPTTYP AOB Contract type -> [AOB]ABREV =[SRE]CONSPTTYP (AOBJET) !Block
  COVAUSCLA A*30 Covered by
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  CTIMSPGDAY L*8 Cumul (days)
  CTIMSPGHOU L*8 Cumul (hours)
  CTIMSPGMNT L*8 Cumul (minutes)
  DIE DIE Dimension type code -> [DIE]DIE0 =[SRE]DIE (GDIE) !Block act:ANA
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[SRE]ENTCOD (GAUTACE) !Block
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[SRE]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  MACFLT MAC Base filter -> [MAC]MAC0 =[SRE]MACFLT (MACHINES) !Block
  MACFLTINT M*4 Customer filter [menu 1: 1=No,2=Yes]
  MANUPD M*4 Modify resolution [menu 1: 1=No,2=Yes]
  NBRMANUPD L*8 No. manual modifs
  NUMFULDES CLC Description chrono
  OVRCOV M*15 Global coverage [menu 3003: 1=Totally covered,2=Partially covered,3=Not covered,4=Covered by service contract,5=Covered by sales order,6=Covered commercially,7=Covered by direct invoicing]
  OVRCOVREN C*4 Non-coverage reason
  OVRCOVTYP AOB Contract type -> [AOB]ABREV =[SRE]OVRCOVTYP (AOBJET) !Block
  REP A*5 Sales rep
  SALFCY FCY Site -> [FCY]FCY0 =[SRE]SALFCY (FACILITY) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SOLNUM SOL Solution code -> [SOL]SOL0 =[SRE]SOLNUM (SOLUTION) !Block
  SREASS M*15 Assignment [menu 975: 1=Dispatching,2=Employee,3=Queue,4=Commercial,5=Closed]
  SREBPAADD ADR Address
  SREBPC BPR Customer -> [BPR]BPR0 =[SRE]SREBPC (BPARTNER) !Block
  SREBPCGRU BPR Group customer -> [BPR]BPR0 =[SRE]SREBPCGRU (BPARTNER) !Block
  SREBPCINV BPR Bill-to customer -> [BPR]BPR0 =[SRE]SREBPCINV (BPARTNER) !Block
  SREBPCPYR BPR Pay-by -> [BPR]BPR0 =[SRE]SREBPCPYR (BPARTNER) !Block
  SRECCN AIN Contact (relationship) -> [AIN]AIN0 =[SRE]SRECCN (CONTACTCRM) !Block
  SRECHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  SRECOV M*4 Covered [menu 1: 1=No,2=Yes]
  SRECOVAUS A*5 Covered by
  SRECOVAUT C*4 Auto cover
  SRECOVCTL A*5 To control by
  SRECOVNUM VCR Coverage reference
  SRECUR CUR Currency -> [TCU]TCU0 =[SRE]SRECUR (TABCUR) !Block
  SREDATASS D Assignment date
  SREDEP TDA Settlement discount -> [TDA]TDA0 =SREDEP;[V]GSUPCLE (TABDEPAGIO) !Block
  SREDES CLX Overview
  SREDESFLG C*2 Overview written
  SREDET VCR Assignment detail
  SREDOO BPR Service caller -> [BPR]BPR0 =[SRE]SREDOO (BPARTNER) !Block
  SREESC C*4 No. of escalations
  SREESC2 C*4 Historized escalation
  SREESC3 C*4 Incremental escaln
  SREGRALEV ADI Severity level -> [ADI]CODE =428;SREGRALEV (ATABDIV) !Block
  SREHOUASS HM Time
  SREINUMBPC L*8 Customer no. chrono
  SREINVFLG M*15 Invoicing flag [menu 3004: 1=Non-invoicable,2=Invoicable,3=Invoiced]
  SRELOK M*4 Blocking gravity [menu 1: 1=No,2=Yes]
  SREMAC MAC Base by default -> [MAC]MAC0 =[SRE]SREMAC (MACHINES) !Block
  SREMACPBL PBL Skills base/default -> [PBL]PBL0 =[SRE]SREMACPBL (FAMPB) !Block
  SRENUM VCR Sequence no.
  SRENUMBPC VCR Customer request
  SREORI M*20 Source [menu 2982: 1=Manual creation,2=Maintenance plan]
  SREORIVCR VCR Original document no.
  SREORIVCRL L*8 Source document line
  SREPBLGRP PBL Skill -> [PBL]PBL0 =[SRE]SREPBLGRP (FAMPB) !Block
  SREPIOLEV ADI Level of urgency -> [ADI]CODE =405;SREPIOLEV (ATABDIV) !Block
  SREPJT PJT Project -> [PIM]PIM0 =[SRE]SREPJT (PIMPL) !Block
  SREPRITYP M*6 Price type [menu 243: 1=Exclude tax,2=Include tax]
  SREPTE PTE Payment terms -> [TPT]TPT0 =SREPTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  SREREP REP Sales rep -> [REP]REP0 =[SRE]SREREP (SALESREP) !Block act:REC
  SRERESDAT D Desired resolution
  SRERESHOU HM Desired resolution
  SRERESREN A*80 Reason
  SRESAT ADI Request status -> [ADI]CODE =422;SRESAT (ATABDIV) !Block
  SRETIMSPG C*4 Total time spent
  SRETPL VCR Request model
  SRETTR A*80 Title
  SRETYPCOV M*25 Coverage type [menu 974: 1=by service contract,2=by order,3=by commercial decision,4=by direct invoicing,5=By loan contract,6=.]
  SREVACBPR TVB Tax rule -> [TVB]TVB0 =SREVACBPR;[V]GSUPCLE (TABVACBPR) !RTZ
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Storage site -> [FCY]FCY0 =[SRE]STOFCY (FACILITY) !Block
  TIMSPGDAY L*8 Time passed (days)
  TIMSPGHOU L*8 Time spent (hours)
  TIMSPGMNT L*8 Time passed (minute)
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TSDCOD ADI Statistical group -> [ADI]CODE =indice+445;TSDCOD(indice) (ATABDIV) !Block act:STR
  TSKREPCRE M*4 Sales rep task created [menu 1: 1=No,2=Yes]
  TYPFULDES CLT Description type
  TYPMAC M*15 Base type [menu 2983: 1=Listed base,2=Filtered base]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SERVICE (SRV) - Services
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SETMAC (SEM) - Listed base in requested model
Keys (first = PK; D = duplicates allowed): SEM0 SETNUM+ITMREF
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMREF ITM Product code -> [ITM]ITM0 =[SEM]ITMREF (ITMMASTER) !Delete
  SETNUM VCR Request model
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SETMACCPN (SEN) - Components concerned
Keys (first = PK; D = duplicates allowed): SEN0 SETNUM+ITMREF+TPYFLG (D)
Fields:
  AUUID AUUID Single identifier
  CPNITM ITM Component concerned -> [ITM]ITM0 =[SEN]CPNITM (ITMMASTER) !Delete
  CPNQTY L*8 Quantity
  CPNSEQ C*4 Sequence
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMREF ITM Product code -> [ITM]ITM0 =[SEN]ITMREF (ITMMASTER) !Delete
  SETNUM VCR Request model
  TPYFLG C*1 Temp record
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SETXN (SEX) - Credit card transactions
Notes: activity code SEPP
Keys (first = PK; D = duplicates allowed): SEX0 TXNDATTIM+REQRSP+TXNID (D); SEX1 REF2+TXNDATTIM+REQRSP (D)
Fields:
  ACCNAM NAM Name
  ADDLIG ADL(2) Address
  AMT MD1 Amount
  AUUID AUUID Single identifier
  AVS A*1 AVS
  AVSCV2RESP A*50 Security check
  BPCNUM BPC Customer -> [BPC]BPC0 =[SEX]BPCNUM (BPCUSTOMER) !Delete
  CRDTYP ADI Card type -> [ADI]CODE =398;CRDTYP (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SEX]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[SEX]CRY (TABCOUNTRY) !Block
  CTY CTY City
  CVV A*1 CVV
  DECLINECODE A*2 Reject code
  EMAIL MAI Email address
  EXPDAT A*4 Expiration
  GUID A*50 Vault GUID
  PAYDES A*20 Payment description
  PAYPRC M*4 Payment processor [menu 2098: 1=Sage Exchange,2=Sage Pay]
  POSCOD POS Postal code
  POSTCODERESP A*20 Postal code control
  REF1 A*50 Reference 1
  REF2 A*50 Reference 2
  REQRSP M*15 Response [menu 2096: 1=Request,2=Response]
  RESP A*15 Resp
  RSPCOD A*15 Response code
  RSPMSG A*250 Response message
  SAT SAT Region
  SPSECKEY A*10 Security key
  SPTXNID A*38 Transaction
  SPTXNTYP A*15 Transaction type
  TAXAMT MD1 Tax amount
  TXNDAT D Transaction date
  TXNDATTIM A*25 Txn date time
  TXNID A*50 Transaction
  TXNTYP ADI Type -> [ADI]CODE =399;TXNTYP (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SEX]UPDUSR (AUTILIS) !Other
  VANREF A*20 VAN reference

## SFANAPAR (SFA) - Sage fixed assets NA setup
Notes: activity code FASNA
Keys (first = PK; D = duplicates allowed): SFA0 ID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[SFA]CREUSR (AUTILIS) !Other
  DACDIA GDE Transaction -> [GDE]DIA =[SFA]DACDIA (GDIAENTRY) !Block
  DRTSTO A*250 Storage directory
  DRTWRK A*250 Work directory
  FILENAM A*50 Import file
  GASTPL AOE Journals -> [AOE]AOE0 =[SFA]GASTPL (AOBJEXT) !Block
  ID A*10 Identifier
  INTIT DES Description
  JOU JOU Journal -> [JOU]JOU0 =JOU;LEG (GJOURNAL) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[SFA]UPDUSR (AUTILIS) !Other

## SFOOTINV (SFI) - Invoicing elements
Notes: differs in V9.0 P12 (diff: AT3_SFOOTINV.htm); differs in V10 P1 (diff: ATD_SFOOTINV.htm)
Keys (first = PK; D = duplicates allowed): SFI0 SFINUM
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =11;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACTCLCBAS A*10 Action calcul.
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount]
  AUUID AUUID Single identifier
  BPCORI M*15 Original customer [menu 2218: 1=Invoice customer,2=Order customer]
  BRDRUL M*15(8) Split rule [menu 473: 1=1st order,2=1st delivery,3=1st invoice,4=1st credit memo,5=All orders,6=All deliveries,7=All invoices,8=All credit memos,9=Amount pro rata,10=Quantity pro rata,11=Weight pro rata,12=Volume pro rata]
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CLCBAS M*15 Calculation basis [menu 2219: 1=Before tax calculation,2=After tax calculation,3=Action]
  CLCDEB M*18 Intrastat taken into account [menu 2208: 1=No,2=Fiscal value,3=Statistical value] act:DEB
  CLCORD C*2 Calculation order
  CLCVACITM TVI Tax level selection -> [TVI]TVI0 =CLCVACITM;[V]GSUPCLE (TABVACITM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SFI]CUR (TABCUR) !Block
  DACBPC C*2 Customer entry
  DACDLV C*2 Delivery entry
  DACINV C*2 Invoice entry
  DACORD C*2 Order entry
  DEFVAL DCB*11.4 Default value
  DEPFLG M*4 Subject to discount [menu 1: 1=No,2=Yes]
  DESAXX AX2 Description
  DESVCR M*15(8) Destination document [menu 476: 23 values, see local-menus.md]
  DIE DIE Dimension type code -> [DIE]DIE0 =[SFI]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  DSPLIN M*15 Distribution [menu 475: 1=No,2=Quantity pro rata,3=Amount pro rata,4=Weight pro rata,5=Volume pro rata]
  EXCTAXRUL M*4 Special levy basis [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  GRUFLG M*15(8) Grouping [menu 474: 1=Yes,2=No if different]
  GRURUL M*15(8) Grouping rule [menu 472: 17 values, see local-menus.md]
  INCDCR M*10 Increase/Decrease [menu 254: 1=Increase,2=Decrease]
  INVFOOBRD SFI Split no. -> [SFI]SFI0 =[SFI]INVFOOBRD (SFOOTINV) !Other
  INVFOOGRU SFI Grouping no. -> [SFI]SFI0 =[SFI]INVFOOGRU (SFOOTINV) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[SFI]ITMREF (ITMMASTER) !Block
  LANDESSHO A*50 Descriptions
  MISRULSTD M*15 Sundry std rule [menu 463: 1=None,2=Discount on tax]
  MISRULUSR M*15 User rule [menu 464: 1=None]
  ORIVCR M*15(8) Source document [menu 476: 23 values, see local-menus.md]
  PRGCLCBAS A*10 Program calcul.
  PROCOD M*15 Processing mode [menu 271: 1=Modifiable,2=Not modifiable,3=Inactive]
  SFINUM SFI Invoicing element -> [SFI]SFI0 =[SFI]SFINUM (SFOOTINV) !Other
  SFINUMCAR A*3 Alpha no.
  SHOAXX AX1 Short description
  SPETAXRUL M*4 Special tax basis [menu 1: 1=No,2=Yes]
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  TRFDLY M*8 Include in ord-deliv [menu 442: 1=First,2=All]
  TRFINV M*8 Include in ord-inv [menu 442: 1=First,2=All]
  TSDMAX MD1 Maximum threshold
  TSDMIN MD1 Minimum threshold
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI Element tax level -> [TVI]TVI0 =VACITM;[V]GSUPCLE (TABVACITM) !Block
  VALTYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%]
  VATRUL M*10 Tax rule [menu 283: 1=Product,2=Maximum rate,3=Minimum rate,4=Fixed rate,5=Distribution]

## SFTINDREF (SFTIR) - Indirect references
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SFTAG0 INDCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SFTIR]CREUSR (AUTILIS) !Other
  INDCOD A*3 Code
  INDESAXX AX3 Description
  INDTYP M*4 Category type [menu 2417: 1=Time off,2=Break,3=Non-exclusive labor,4=Exclusive labor,5=Auto break]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SFTIR]UPDUSR (AUTILIS) !Other

## SFTSHIFT (SFTS) - Shift code
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SHF0 SHFCOD
Fields:
  AUUID AUUID Single identifier
  BRKCOD INDREF(10) Break code -> [SFTIR]SFTAG0 =[SFTS]BRKCOD (SFTINDREF) !Block
  BRKDUR DCB*2.2(10) Duration
  BRKEND HM(10) End time
  BRKSTR HM(10) Start time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DURCHECKB C*4(10) Check
  DURCHECKS C*4 Check
  SHFCOD A*6 Shift code
  SHFDES AX3 Description
  SHFDUR DCB*2.2 Duration
  SHFEND HM End time
  SHFSTR HM Start time
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SFTTEM (SFTTM) - Teams
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SFTTM0 TEAMNUM+TEAMLIN; SFTTM1 TEAMNUM+EMPNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SFTTM]CREUSR (AUTILIS) !Other
  EMPNUM TMA Employee ID -> [TMA]TMA0 =[SFTTM]EMPNUM (TABMAT) !Block
  STRDAT D Start date
  TEAMLIN C*4 Line
  TEAMNUM TMA Team -> [TMA]TMA0 =[SFTTM]TEAMNUM (TABMAT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SFTTM]UPDUSR (AUTILIS) !Other

## SFTTEMH (SFTTH) - Team history
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SFTTMH0 TEAMNUM+EMPNUM+TEAMSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SFTTH]CREUSR (AUTILIS) !Other
  EMPNUM TMA Employee ID -> [TMA]TMA0 =[SFTTH]EMPNUM (TABMAT) !Block
  ENDDAT D End date
  STRDAT D Start date
  TEAMNUM TMA Team -> [TMA]TMA0 =[SFTTH]TEAMNUM (TABMAT) !Block
  TEAMSEQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SFTTH]UPDUSR (AUTILIS) !Other

## SINVOICE (SIH) - Sales invoices
Notes: differs in V9.0 P12 (diff: AT3_SINVOICE.htm); differs in V10 P1 (diff: ATD_SINVOICE.htm)
Keys (first = PK; D = duplicates allowed): SIH0 NUM; SIH1 BPR+BPRVCR (D); SIH2 GTE+NUM; SIH3 ACCDAT+BPR (D); SIH4 BPRFCT+FCTVCR+FCTVCRFLG (D); SIH5 CUR+BPR+NUM; SIH6 STA+ORIMOD+INVTYP+NUM (D); SIH7 CPY+EECNUMDEB+ACCDAT (D); SIH8 RCRNUM+RCRDAT (D); SIH9 BVRREFNUM (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM L*8 Internal number
  ADRVAL M*4 Address [menu 1: 1=No,2=Yes] act:LTA
  AMTATI MD1 Amount + tax
  AMTATIL MD1 Invoice amt. + tax (co)
  AMTNOT MD1 Amount - tax
  AMTNOTL MD1 Amount - tax (co)
  AMTTAX MD1(10) Tax amount
  AMTTAXUSA MD1(10) Tax amount act:KUS
  AUUID AUUID Single identifier
  BASDEP MD1 Early disc/late charge calc basis
  BASTAX MD1(10) Tax basis
  BELVCS VCS VCS number act:KBE
  BILVCR VCR Draft no.
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Address
  BPAPAY ADR Business partner address
  BPR BPR BP -> [BPR]BPR0 =[SIH]BPR (BPARTNER) !Block
  BPRDAT D Source date
  BPRFCT FCT Factor -> [FCT]FCT0 =[SIH]BPRFCT (FACTOR) !Block act:FCT
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[SIH]BPRPAY (BPARTNER) !Block
  BPRSAC SAC Control
  BPRVCR A*30 Source document
  BPYADDLIG ADL(3) Address line
  BPYCRY CRY Country -> [TCY]TCY0 =[SIH]BPYCRY (TABCOUNTRY) !Block
  BPYCRYNAM NCY Country name
  BPYCTY CTY City
  BPYNAM NAM(2) Company name
  BPYPOSCOD POS Postal code
  BPYSAT SAT County
  BVRREFNUM A*27 ISR reference number act:KSW
  CAI A*10 CAI number act:KAG
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CPY CPY Company -> [CPY]CPY0 =[SIH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CRN CRT Site tax ID no.
  CRY CRY Country -> [TCY]TCY0 =[SIH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CSHVAT M*4 Cash VAT tax rule [menu 1: 1=No,2=Yes] act:KSP
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[SIH]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[SIH]CURLED (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DATVLYCAI D*1 CAI validity date act:KAG
  DCLEECNUM EEC VAT declaration no. act:VATTN
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DEPRAT RAT Early discount rate
  DES DES(5) Comments
  DIE DIE Dimension type code -> [DIE]DIE0 =[SIH]DIE (GDIE) !Block act:ANA
  DIRINVFLG M*4 Direct inv [menu 1: 1=No,2=Yes]
  EECNUMDEB C*4 EU Intrastat act:DEB
  ENDDATSVC D End service act:SVC
  EXEAMTTAX MD1(10) Exemption amount
  EXPNUM L*8 Export number
  FCTVCR VCR Receipt act:FCT
  FCTVCRFLG C*1 Validated receipt act:FCT
  FCY FCY Site -> [FCY]FCY0 =[SIH]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLD40REN ADI Field 40 - reason -> [ADI]CODE =8300;FLD40REN (ATABDIV) !Block act:KPO
  FLD41REN ADI Field 41 - reason -> [ADI]CODE =8301;FLD41REN (ATABDIV) !Block act:KPO
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  INVNUM VCR Invoice number
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  INVTYPSPA M*20 Spanish invoice type [menu 2109: 12 values, see local-menus.md] act:CTSW
  ISEXTDOC M*4 External document [menu 1: 1=No,2=Yes] act:DKS
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LASDATSVC D Accruals. revn. pstd act:SVC
  LED LED(10) Ledger -> [LED]LED0 =[SIH]LED (GLED) !Block
  METCOR M*20 Method of correction [menu 2069: 1=Rectificación íntegra,2=Rectificación por diferencias,3=Rectificación por descuento por volumen de operaciones durante un periodo,4=Autorizadas por la Agencia Tributaria] act:KSP
  NBRCPY C*2 Number of companies
  NBRTAX C*2 Number of taxes
  NUM VCR Document no.
  ORIDOCNUM A*30 Original document no. act:KPO
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[SIH]PAYBAN (BANK) !Block act:KSW
  PER C*2 Period
  PERDEB D Period start date act:KPO
  PERFIN D To act:KPO
  PJTH PJT Project -> [PIM]PIM0 =PJTH (PIMPL) !Block act:PJM
  POREXPDCL VCR Export declaration act:KPO
  POSCOD POS Postal code
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  QTCACCNUM L*8 Receipt actng. entry no. act:FCT
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  RCRDAT D Recurrence date
  RCRNUM VCR Recurring number
  REVCANSTA C*1 Cancellation status act:INVCA
  SALPRITYP M*10 Amount type [menu 243: 1=Exclude tax,2=Include tax]
  SAT SAT County
  SINUM A*10 Integrale part no. act:SMI
  SIVTYP TSV Invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Block
  SNS C*2 Sign
  SPADERNUM A*60 DER code act:KSP
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STA M*15 Status [menu 2261: 1=Not posted,2=Not used,3=Posted]
  STARPT M*4 Printing [menu 1: 1=No,2=Yes]
  STRDATSVC D Start service act:SVC
  STRDUDDAT D Due date basis
  TAX VAT(10) Taxes -> [TVT]TVT0 =TAX(indice);[V]GSUPCLE (TABVAT) !Block
  THEAMTTAX DCB*19.8 Theor. tax amt act:KAG
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VAC TVB Tax rule -> [TVB]TVB0 =VAC;[V]GSUPCLE (TABVACBPR) !Block
  VATDAT D Tax date on credit
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SIPARJOU (SPJ) - Integrale migration
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SIPARVAC (SPV) - Integrale migration
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SIPARVACB (SVB) - Integrale migration
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SIPARX3 (SPX) - Integrale migration
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SITEPAYE (HRSIT) - Sites
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SITRACAR (SIC) - Transcoding
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SITRACOD (SIR) - Transcoding
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SITRAWRK (SIW) - Transcoding
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SIWRKX3 (SWX) - Integrale migration
Notes: activity code SMI
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SPREASON (SPR) - Sales price list reasons
Keys (first = PK; D = duplicates allowed): SPR0 PRIREN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACMAN M*4 Manual entry [menu 1: 1=No,2=Yes]
  DES DES Description
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  LANDESSHO A*60 Descriptions
  PRIREN C*2 Reason
  PRIRENCAR A*3 Alpha no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDPRI M*4 Price change [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user

## SPRICCONF (SPC) - Customer pricing parameters
Keys (first = PK; D = duplicates allowed): SPC0 PLI; SPC1 PLIENAFLG+PLITYP+PIO+PLI
Fields:
  ABB A*3(5) Abbreviation
  ATICNVFLG M*4 Conversion - / +tax [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  COMPRO M*15 Commission factor [menu 244: 1=Yes,2=No,3=Initialization]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRIBPCNUM C*1 Customer criterion
  CRIBPR C*1 BP criterion
  CRICURNUM C*1 Currency criterion
  CRIDES DES(5) Criterion title
  CRIDIE DIE(5) Dimension type code -> [DIE]DIE0 =[SPC]CRIDIE (GDIE) !Block
  CRIIND C*4(5) Criterion index
  CRIITM C*1 Product criterion
  CRIITMNUM C*1 Product criterion
  CRILEN DCB*5(5) Field length
  CRINBR C*1 Numbers of criteria
  CRIUOMNUM C*1 Unit criterion
  CUR CUR Currency -> [TCU]TCU0 =[SPC]CUR (TABCUR) !Block
  CURCNVFLG M*4 Currency conversion [menu 1: 1=No,2=Yes]
  DESAXX AX3 Description
  DISCRGPRO M*15 Charge/Discount processing [menu 244: 1=Yes,2=No,3=Initialization] act:SPR
  EXPNUM L*8 Export number
  FIL ATB(5) Table -> [ATB]CODFIC =[SPC]FIL (ATABLE) !Block
  FLD AVA(5) Field
  FLDTYP ATY(5) Field type -> [ATY]CODTYP =[SPC]FLDTYP (ATYPE) !Block
  FLDTYPCPL A*10(5) Supplement type
  FOCPRO M*15 Free products [menu 273: 1=No,2=Same product,3=Other products,4=Order total]
  FOCTYP M*15 Free type [menu 274: 1=Threshold,2=Multiple]
  LANDESSHO A*60 Descriptions
  LIEN M*5(5) Link [menu 49: 1=No,2=Long,3=Short]
  PIO C*3 Priority
  PLI SPC Price list code -> [SPC]SPC0 =[SPC]PLI (SPRICCONF) !Other
  PLIBPRCNR M*15 BP concerns [menu 2210: 1=Outside group,2=Group,3=All]
  PLICPY CPY Company -> [CPY]CPY0 =[SPC]PLICPY (COMPANY) !Block
  PLIENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  PLISEA C*1 Price search
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Block
  PLITYP M*10 Price list type [menu 241: 1=Normal,2=Grouped,3=Restricted,4=Component]
  PPUMNU C*3(5) Local menu
  PRIFLD A*250 Base price field
  PRIIND C*4 Base price index
  PRIPRO M*15 Price processing [menu 270: 1=No,2=Value,3=Value for N,4=Factor,5=Calculation]
  PRIQTYFLG M*15 Price/Quantity [menu 239: 1=No,2=Yes,3=Quantity bands,4=Gross price bands,5=Net price bands]
  PRIREN SPR Reason -> [SPR]SPR0 =[SPC]PRIREN (SPREASON) !Block
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  UOMCNVFLG M*4 Unit conversion [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDNULPRI M*4 Update zero price [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user

## SPRICLIST (SPL) - Customer price lists
Keys (first = PK; D = duplicates allowed): SPL0 PLI+PLICRD+PLILIN; SPL1 PLI+PLICRI+PLISTRDAT (D); SPL2 PLI+PLICRI1+PLISTRDAT (D); SPL3 PLI+PLICRI2+PLISTRDAT (D); SPL4 PLI+PLICRI1+PLICRI2+PLICRI3+PLICRI4+PLICRI5 (D)
Fields:
  AUUID AUUID Single identifier
  COMCOE CCR Comm factor
  CPNITMREF ITM Component -> [ITM]ITM0 =[SPL]CPNITMREF (ITMMASTER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SPL]CUR (TABCUR) !Block
  DCGVAL MD8 Charge/discount value act:SPR
  EXPNUM L*8 Export number
  FOCAMTBKT MD1 Free Class
  FOCAMTMIN MD1 Free threshold
  FOCITMREF ITM Free product -> [ITM]ITM0 =[SPL]FOCITMREF (ITMMASTER) !Block
  FOCQTY QTY Free quantity
  FOCQTYBKT QTY Free Class
  FOCQTYMIN QTY Free threshold
  FOCUOM UOM Unit -> [TUN]TUN0 =[SPL]FOCUOM (TABUNIT) !Block
  IMPNUMLIG L*8 Import line
  LTI C*3 Lead time
  MAXAMT MD1 Maximum value
  MAXQTY QTY Maximum quantity
  MINAMT MD1 Minimum value
  MINQTY QTY Minimum quantity
  PLI SPC Price list code -> [SPC]SPC0 =[SPL]PLI (SPRICCONF) !Delete
  PLICRD VCR Price list record
  PLICRI SPX Criteria
  PLICRI1 SPU Criteria 1
  PLICRI2 SPU Criteria 2
  PLICRI3 SPU Criterion 3
  PLICRI4 SPU Criterion 4
  PLICRI5 SPU Criterion 5
  PLIENDDAT D Validity end date
  PLILIN L*8 Line
  PLISTRDAT D Validity start date
  PRI MD8 Price
  PRIDIV C*4 Price factor
  UOM UOM Unit -> [TUN]TUN0 =[SPL]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SREMAC (SRM) - Base concerned
Keys (first = PK; D = duplicates allowed): SRM1 SRENUM+MACNUM
Fields:
  AUUID AUUID Single identifier
  COVFLG M*15 Covered [menu 2985: 1=Totally covered,2=Partially covered,3=Not covered]
  COVSPT M*15 Blanket support [menu 974: 1=by service contract,2=by order,3=by commercial decision,4=by direct invoicing,5=By loan contract,6=.]
  COVVCR VCR Document no.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITNGRU A*15 Grouping code
  MACCOVREN C*4 Non-coverage reason
  MACNUM MAC Base concerned -> [MAC]MAC0 =[SRM]MACNUM (MACHINES) !Delete
  PBLNUM PBL Skill -> [PBL]PBL0 =[SRM]PBLNUM (FAMPB) !Block
  SRENUM SRE Service request -> [SRE]SRE0 =[SRM]SRENUM (SERREQUEST) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SREMACCPN (SRN) - Components concerned
Keys (first = PK; D = duplicates allowed): SRN0 SRENUM+MACNUM+TPYFLG (D)
Fields:
  AUUID AUUID Single identifier
  CPNCOVFLG M*15 Covered [menu 2985: 1=Totally covered,2=Partially covered,3=Not covered]
  CPNCOVREN C*4 Non-coverage reason
  CPNCOVSPT M*15 Blanket support [menu 974: 1=by service contract,2=by order,3=by commercial decision,4=by direct invoicing,5=By loan contract,6=.]
  CPNCOVVCR A*15 Document no.
  CPNITM ITM Component concerned -> [ITM]ITM0 =[SRN]CPNITM (ITMMASTER) !Delete
  CPNQTY L*8 Quantity
  CPNSEQ C*4 Sequence
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FGVCAH C*1 Cancel cache
  MACNUM MAC Base concerned -> [MAC]MAC0 =[SRN]MACNUM (MACHINES) !Delete
  SRENUM SRE Service request -> [SRE]SRE0 =[SRN]SRENUM (SERREQUEST) !Delete
  TPYFLG C*1 Temp record
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SRESTAT (SST) - Requested statistics
Keys (first = PK; D = duplicates allowed): SST0 USR (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CXTFLT CLX Filter
  CXTLIG L*8 Line no.
  CXTNAM A*100 Description
  CXTNUM VCR Stat grp
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SST]UPDUSR (AUTILIS) !Other
  USR A*5 User

## SRETEMPL (SET) - Service request model
Keys (first = PK; D = duplicates allowed): SET0 SETNUM
Fields:
  ASS M*15 Assignment type [menu 2988: 1=According to market sector,2=Dispatching,3=Queue,4=Nominal,5=Person on the base,6=External service provider]
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SET]CREUSR (AUTILIS) !Other
  DES CLX Description
  DESFLG C*2 Overview flag
  DETASS VCR Assignment
  ITNTYP ADI Intervention type -> [ADI]CODE =407;ITNTYP (ATABDIV) !Block
  LTIDAY L*8 Waiver extension D
  LTIHOU L*8 Waiver extension H
  LTIREN A*80 Reason
  MACFLT MAC Base filter -> [MAC]MAC0 =[SET]MACFLT (MACHINES) !Block
  MACFLTINT M*4 Customer filter [menu 1: 1=No,2=Yes]
  NUMFULDES CLC Description chrono
  PBL PBL Skill group -> [PBL]PBL0 =[SET]PBL (FAMPB) !Block
  PIOLEV ADI Severity level -> [ADI]CODE =428;PIOLEV (ATABDIV) !Block
  SALFCY FCY Site -> [FCY]FCY0 =[SET]SALFCY (FACILITY) !Block
  SETNUM VCR Sequence no.
  TPLCON M*4 Template / mainten [menu 1: 1=No,2=Yes]
  TPLNAM DCO Description
  TPLSVC M*4 Template / service [menu 1: 1=No,2=Yes]
  TTR A*80 Title
  TYPFULDES CLT Description type
  TYPMAC M*15 Base type [menu 2983: 1=Listed base,2=Filtered base]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SET]UPDUSR (AUTILIS) !Other

## STKMVTITC (SMI) - Movement with value pending
Keys (first = PK; D = duplicates allowed): SMI0 ITCSTRDAT+ITMREF+STOFCY+CSTTYP
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SMI]CREUSR (AUTILIS) !Other
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  ITCSEQ L*8 Sequence no.
  ITCSTRDAT D Valid from
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[SMI]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SMI]UPDUSR (AUTILIS) !Other

## STKTRS (SRT) - Stock transactions
Notes: differs in V9.0 P12 (diff: AT3_STKTRS.htm); differs in V10 P1 (diff: ATD_STKTRS.htm)
Keys (first = PK; D = duplicates allowed): SRT0 SRTTYP+SRTNUM; SRT1 SRTNUM+SRTTYP
Fields:
  ABCCOD M*15 ABC [menu 60: 1=Displayed,2=Hidden]
  ABCSCR M*15 [menu 99: 1=Form and table,2=Form,3=Table]
  ABYTYP M*15 Assembly type [menu 2730: 1=Assembly,2=Disassembly]
  ACSCOD ACS Access code -> [ACS]ACS0 =[SRT]ACSCOD (ACCCOD) !Block
  AGRCOD M*4 Line grouping [menu 1: 1=No,2=Yes]
  ALLSTKFLG M*4 Include allocated stock [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  AUZSST A*30 Authorized substatuses
  AUZSTA M*20 Authorized statuses [menu 2701: 1=Status 'A',2=Status 'Q',3=Status 'A'+'Q',4=Status 'R',5=Status 'A'+'R',6=Status 'Q'+'R',7=Status 'A'+'Q'+'R']
  AVSTOCOD1 M*15 Available stock [menu 60: 1=Displayed,2=Hidden]
  AVSTOSCR1 M*15 Available stock [menu 99: 1=Form and table,2=Form,3=Table]
  BETFCYCOD M*15 Destination [menu 792: 1=Internal,2=Intersite,3=Customer,4=Subcontract transfer,5=Subcontract return]
  BPCORDCOD M*15 Ship-to [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPRNUMCOD M*15 BP [menu 60: 1=Displayed,2=Hidden]
  BPRNUMSRC M*15 BP [menu 99: 1=Form and table,2=Form,3=Table]
  BPSLOTCOD M*15 Supplier lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTCOD1 M*15 Supplier lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTSCR M*15 Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPSLOTSCR1 M*15 Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPTCOD M*15 Carrier [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPTNUMCOD M*15 Carrier [menu 60: 1=Displayed,2=Hidden]
  CCECOD M*15 Analytical dimension line [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  CCECODS M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  CFMCOD M*4 Validate entry [menu 1: 1=No,2=Yes]
  CHANGECOD M*4 Lot mod type [menu 2739: 1=Lot characteristics modification,2=Renumbering, mixing and splitting]
  CHGEMPCOD M*4 Location change [menu 1: 1=No,2=Yes]
  CHGEMPTOT M*4 Mass locn change [menu 1: 1=No,2=Yes]
  CHGPCUCOD M*4 Unit change [menu 1: 1=No,2=Yes]
  CHGSTACOD M*4 Status change [menu 1: 1=No,2=Yes]
  CHGWRHCOD M*4 Destination warehouse [menu 1: 1=No,2=Yes]
  CLEFLGCOD M*15 Close [menu 60: 1=Displayed,2=Hidden]
  CLEFLGSCR M*15 Close [menu 99: 1=Form and table,2=Form,3=Table]
  COBMVTCOD M*15 Component quantities [menu 2732: 1=Without losses,2=With losses]
  CREDAT D Date created
  CREDATCOD M*15 Date created [menu 60: 1=Displayed,2=Hidden]
  CREDATSCR M*15 Date created [menu 99: 1=Form and table,2=Form,3=Table]
  CREDATTIM ADATIM Date time
  CREPPSCOD M*15 Date of storage list [menu 60: 1=Displayed,2=Hidden]
  CREPPSSCR M*15 Date of storage list [menu 99: 1=Form and table,2=Form,3=Table]
  CREUSR A*5 Creation user
  CREUSRCOD M*15 Creation user [menu 60: 1=Displayed,2=Hidden]
  CREUSRSCR M*15 Creation user [menu 99: 1=Form and table,2=Form,3=Table]
  CRIT1 M*15 Criteria 1 [menu 2719: 1=(None),2=Allocation date,3=Product,4=Location,5=Journal type/Number]
  CRIT2 M*15 Criteria 2 [menu 2719: 1=(None),2=Allocation date,3=Product,4=Location,5=Journal type/Number]
  CSMREO M*4 Consum area [menu 1: 1=No,2=Yes]
  CTGUSRFLG M*4 Count manager entry [menu 1: 1=No,2=Yes]
  CTRALLRGP M*4 Check alloc regroup [menu 1: 1=No,2=Yes]
  CUNAMTDSY M*4 Display value [menu 1: 1=No,2=Yes]
  CUNAMTDSY1 M*4 Display value [menu 1: 1=No,2=Yes]
  CUNAMTSCR M*15 Display value [menu 99: 1=Form and table,2=Form,3=Table]
  CUNAMTSCR1 M*15 Display value [menu 99: 1=Form and table,2=Form,3=Table]
  CUNDEVDSY M*4 Display variance [menu 1: 1=No,2=Yes]
  CUNDEVDSY1 M*4 Display variance [menu 1: 1=No,2=Yes]
  CUNDEVSCR M*15 Display variance [menu 99: 1=Form and table,2=Form,3=Table]
  CUNDEVSCR1 M*15 Display variance [menu 99: 1=Form and table,2=Form,3=Table]
  DEFLOCCOD M*15 Consump. locn [menu 60: 1=Displayed,2=Hidden]
  DEFLOCSCR M*15 Consump. locn [menu 99: 1=Form and table,2=Form,3=Table]
  DEFTYPCOD M*15 Consump. type [menu 60: 1=Displayed,2=Hidden]
  DEFTYPSCR M*15 Consump. type [menu 99: 1=Form and table,2=Form,3=Table]
  DEPAMTCOD1 M*15 Revaluation amt [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEPAMTSCR1 M*15 Revaluation amt [menu 99: 1=Form and table,2=Form,3=Table]
  DEPRATCOD1 M*15 Revaluation rate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEPRATSCR1 M*15 Revaluation rate [menu 99: 1=Form and table,2=Form,3=Table]
  DESAXX AX3 Description
  DIUCOD M*15 Dimension [menu 60: 1=Displayed,2=Hidden]
  DIUSCR M*15 Dimension [menu 99: 1=Form and table,2=Form,3=Table]
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[SRT]DOCNAM (AREPORT) !Block
  DRNCOD M*15 Route code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCFLG M*4 Version [menu 1: 1=No,2=Yes] act:ECC
  ECCSCR M*15 Major version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  ECCSCRMIN M*15 Minor version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[SRT]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  FLGLOCDES M*4 Enter dest loc [menu 1: 1=No,2=Yes]
  FORSTA A*200 Formula
  GFY AGF Group -> [AGF]AGF0 =[SRT]GFY (AGRPFCY) !Block
  GROWEICOD M*15 Weight of packages [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HEACCECOD M*15 Dimension header [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD01 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD02 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDEDSTCOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDEDSTCOD2 M*15 Identifier 2 dstn. [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDEDSTSCR1 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDEDSTSCR2 M*15 Identifier 2 dstn. [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR01 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR02 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR1 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR2 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  INVSGHCOD M*15 To be invoiced [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IPTDATCOD M*15 Allocation date [menu 60: 1=Displayed,2=Hidden]
  IPTDATCOD1 M*15 Allocation date [menu 60: 1=Displayed,2=Hidden]
  IPTDATSCR M*15 Allocation date [menu 99: 1=Form and table,2=Form,3=Table]
  IPTDATSCR1 M*15 Allocation date [menu 99: 1=Form and table,2=Form,3=Table]
  ITMDES1COD M*15 Standard description [menu 60: 1=Displayed,2=Hidden]
  ITMDES1SCR M*15 Standard description [menu 99: 1=Form and table,2=Form,3=Table]
  LINTYPCOD M*15 Line type [menu 60: 1=Displayed,2=Hidden]
  LINTYPSCR M*15 Line type [menu 99: 1=Form and table,2=Form,3=Table]
  LOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCORICOD M*15 Original location [menu 60: 1=Displayed,2=Hidden]
  LOCORISCR M*15 Original location [menu 99: 1=Form and table,2=Form,3=Table]
  LOCREO M*4 Reorder location [menu 1: 1=No,2=Yes]
  LOCSCR M*15 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LODCOD1 M*4 Preloading [menu 1: 1=No,2=Yes]
  LOTCOD M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTCOD1 M*4 Lot [menu 1: 1=No,2=Yes] act:ECC
  LOTORICOD M*15 Source lot [menu 60: 1=Displayed,2=Hidden]
  LOTORISCR M*15 Source lot [menu 99: 1=Form and table,2=Form,3=Table]
  LOTSCR M*15 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  MIXCOD M*4 Mix complete [menu 1: 1=No,2=Yes]
  MVTDESCOD M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESCOD1 M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESSCR M*15 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  MVTDESTXT DES Designation text
  MVTPRICOD M*15 Mvt price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTPRICOD1 M*15 Mvt price [menu 60: 1=Displayed,2=Hidden]
  MVTPRISCR M*15 Mvt price [menu 99: 1=Form and table,2=Form,3=Table]
  NBSLOFLG M*4 Sub-lot no. [menu 1: 1=No,2=Yes]
  ORIFLG M*15 Source [menu 2720: 1=Awaiting put-away,2=Replenishment]
  ORINUMCOD M*15 Order no. [menu 60: 1=Displayed,2=Hidden]
  ORINUMSCR M*15 Order no. [menu 99: 1=Form and table,2=Form,3=Table]
  OWNERCOD M*15 Owner [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OWNERSCR M*15 Owner [menu 99: 1=Form and table,2=Form,3=Table]
  PACNUMCOD M*15 Package number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCKCOD M*15 Packaging/Capacity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCKFLT M*4 Packaging filter [menu 1: 1=No,2=Yes]
  PCKSCR M*15 Packaging/Capacity [menu 99: 1=Form and table,2=Form,3=Table]
  PCUCOD M*15 Unit [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCUSCR M*15 Unit [menu 99: 1=Form and table,2=Form,3=Table]
  PCUSTUCOD M*15 Coefficient [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCUSTUOCOD M*15 Ori. coeff. [menu 60: 1=Displayed,2=Hidden]
  PCUSTUOSCR M*15 Ori. coeff. [menu 99: 1=Form and table,2=Form,3=Table]
  PCUSTUSCR M*15 Coefficient [menu 99: 1=Form and table,2=Form,3=Table]
  PERCOD M*15 Expiration [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PIOQTY M*30 Locn chg qty load [menu 2748: 1=All (Not allocated+allocated),2=Not allocated,3=Allocated]
  PJTCOD M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTSCR M*18 Project [menu 99: 1=Form and table,2=Form,3=Table]
  PKGTYP M*15 Packing type [menu 2753: 1=Declarative,2=Postpacking]
  PKTNUM TRS Transaction
  PNTMVTCOD M*4 Rec/ iss product [menu 1: 1=No,2=Yes]
  POTCOD M*15 Potency [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRNCOD1 M*15 Printing [menu 708: 1=No print,2=Labels,3=.,4=Transfer document,5=Analysis document]
  PRNNBFLG1 M*4 Number of copies [menu 1: 1=No,2=Yes]
  PRNNBSCR1 M*15 Entry of label no. [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR1 M*15 Printing [menu 99: 1=Form and table,2=Form,3=Table]
  QLYCRDCOD M*15 Technical sheet [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QLYCRDSCR M*15 Technical sheet [menu 99: 1=Form and table,2=Form,3=Table]
  QTYALLCOD1 M*4 Display allocated [menu 1: 1=No,2=Yes]
  QTYALLSCR1 M*15 Display allocated [menu 99: 1=Form and table,2=Form,3=Table]
  QTYPCUCOD M*15 Quantity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QTYPCUCOD1 M*15 Stock PAC [menu 60: 1=Displayed,2=Hidden]
  QTYPCUSCR M*15 Quantity [menu 99: 1=Form and table,2=Form,3=Table]
  QTYPCUSCR1 M*15 Stock PAC [menu 99: 1=Form and table,2=Form,3=Table]
  QTYQTUSCR1 M*15 Stock STK [menu 99: 1=Form and table,2=Form,3=Table]
  QTYSTUCOD M*15 STK quantity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QTYSTUCOD1 M*15 Stock STK [menu 60: 1=Displayed,2=Hidden]
  QTYSTUOCOD M*15 Qty STK of [menu 60: 1=Displayed,2=Hidden]
  QTYSTUSCR M*18 STK quantity [menu 99: 1=Form and table,2=Form,3=Table]
  RENUMCOD M*4 Sequence change [menu 1: 1=No,2=Yes]
  REOLOCCOD M*15 Subcontract location [menu 60: 1=Displayed,2=Hidden]
  REOLOCSCR M*15 Subcontract loc. [menu 99: 1=Form and table,2=Form,3=Table]
  SCCCODCOD M*15 SSCC code [menu 99: 1=Form and table,2=Form,3=Table]
  SCCCODSCR M*15 SSCC code [menu 99: 1=Form and table,2=Form,3=Table]
  SDHTYPCOD M*15 Delivery type [menu 60: 1=Displayed,2=Hidden]
  SDHTYPSCR M*15 Delivery type [menu 99: 1=Form and table,2=Form,3=Table]
  SERCOD M*15 Starting serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERCOD1 M*15 Serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD1 M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERESCR M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCR1 M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERORICOD M*15 Original serial [menu 60: 1=Displayed,2=Hidden]
  SERORISCR M*15 Original serial [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR M*15 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR1 M*15 Serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SHIDATCOD M*15 Ship date [menu 60: 1=Displayed,2=Hidden]
  SHIDATSCR M*15 Ship date [menu 99: 1=Form and table,2=Form,3=Table]
  SHTREO M*4 Shortages on location [menu 1: 1=No,2=Yes]
  SIHNUMCOD M*15 Invoice no. [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOCOD M*15 Sublot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOORICOD M*15 Original s/lot [menu 60: 1=Displayed,2=Hidden]
  SLOORISCR M*15 Original s/lot [menu 99: 1=Form and table,2=Form,3=Table]
  SLOSCR M*15 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SPERFLG M*4 Expiration [menu 1: 1=No,2=Yes]
  SPOTFLG M*4 Potency [menu 1: 1=No,2=Yes]
  SRGPPSCOD M*15 Storage list [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SRGPPSSCR M*15 Storage list [menu 99: 1=Form and table,2=Form,3=Table]
  SRGWAIFLG M*4 Receipt at dock [menu 1: 1=No,2=Yes]
  SRTDES A*35 Transaction description
  SRTNUM TRS Transaction
  SRTTYP M*15 Transaction type [menu 2721: 1=Miscellaneous receipt,2=Miscellaneous issue,3=Stock change,4=Lot modification,5=Putaway plan,6=Counting,7=Assembly/Disassembly,8=Quality control,9=Reorder plan,10=Shipment picking plan,11=Packing,12=Pick tickets]
  SRTTYPCAR A*2 Alpha no.
  SRUB1FLG M*4 Heading 1 [menu 1: 1=No,2=Yes]
  SRUB2FLG M*4 Section 2 [menu 1: 1=No,2=Yes]
  SRUB3FLG M*4 Section 3 [menu 1: 1=No,2=Yes]
  SRUB4FLG M*4 Section 4 [menu 1: 1=No,2=Yes]
  STACOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STAORICOD M*15 Original status [menu 60: 1=Displayed,2=Hidden]
  STAORISCR M*15 Original status [menu 99: 1=Form and table,2=Form,3=Table]
  STASCR M*15 Status [menu 99: 1=Form and table,2=Form,3=Table]
  STKFLG M*4 Automatic issue [menu 1: 1=No,2=Yes]
  STQDATCOD M*15 Control end date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STUCOD M*15 Stock unit [menu 60: 1=Displayed,2=Hidden]
  TRAFLG M*4 Log [menu 1: 1=No,2=Yes]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TRSFAMCOD M*15 Stock movement group [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TRSFAMDEF ADI Transaction group -> [ADI]CODE =9;TRSFAMDEF (ATABDIV) !Block
  TRSFAMSCR M*18 Txn group [menu 99: 1=Form and table,2=Form,3=Table]
  UOMSAIFLG M*4 UOM entry [menu 1: 1=No,2=Yes]
  UOMSAIFLG1 M*4 Enter packing unit [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRFLTCOD M*4 Deactivate filter [menu 1: 1=No,2=Yes]
  VCRLINCOD M*15 Journal line [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VCRLINSCR M*15 Journal line [menu 99: 1=Form and table,2=Form,3=Table]
  VCRNUMCOD M*15 Entry [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VCRNUMSCR M*15 Entry [menu 99: 1=Form and table,2=Form,3=Table]
  VCRTYPCOD M*15 Entry type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VCRTYPSCR M*15 Entry type [menu 99: 1=Form and table,2=Form,3=Table]
  VOLCOD M*15 Volume [menu 60: 1=Displayed,2=Hidden]
  VOLSCR M*15 Volume [menu 99: 1=Form and table,2=Form,3=Table]
  WEICOD M*15 Weight [menu 60: 1=Displayed,2=Hidden]
  WEICOD1 M*15 Weight [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WEISCR M*15 Weight [menu 99: 1=Form and table,2=Form,3=Table]
  WEISCR1 M*15 Weight [menu 99: 1=Form and table,2=Form,3=Table]
  WRHCOD M*15 Warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD1 M*15 Line warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHOBY M*15 Single warehouse [menu 1: 1=No,2=Yes]
  WRHORICOD M*15 Original whouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHORISCR M*15 Original whouse [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR M*15 Warehouse [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR1 M*15 Line warehouse [menu 99: 1=Form and table,2=Form,3=Table]
  ZERSTOFLG M*4 Display zero stock lines [menu 1: 1=No,2=Yes]

## STOQLYSMP (SMP) - Qual. control sampling
Keys (first = PK; D = duplicates allowed): SMP0 VCRTYP+VCRNUM+ITMREF+LOT
Fields:
  AUUID AUUID Single identifier
  CODSMP A*3 Sampling code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[SMP]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  QTYACP L*6 Acceptance
  QTYINISTU QTY Initial quantity
  QTYSMP L*6 Sampling size
  QTYSMPACP L*6 Accepted quantity
  QTYSMPREF L*6 Refused quantity
  RENSMP ADI Reason -> [ADI]CODE =104;RENSMP (ATABDIV) !Other
  STASMP A*3 Status
  STASMPCAL A*3 Initial status
  STU UOM Stock unit -> [TUN]TUN0 =[SMP]STU (TABUNIT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Analysis request
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## SUBCONT (PRX) - Service supplier
Keys (first = PK; D = duplicates allowed): PRX0 BPRNUM
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[PRX]BPRNUM (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PRX]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PRX]CUR (TABCUR) !RTZ
  EVRARA M*4 All fields [menu 1: 1=No,2=Yes]
  EXSINV ADI Expense invoicing -> [ADI]CODE =423;EXSINV (ATABDIV) !RTZ
  EXSVLT DCB*9.2 Expense costing
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !RTZ
  RATHOU DCB*9.2 Hourly rate
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PRX]UPDUSR (AUTILIS) !Other

## SUCURSAL (SCU) - Branch
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## SVATCTL (SVAT) - Control SVAT rules
Notes: activity code KPO; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SVAT0 ROOTACC+TAXCOD+LEDTYPE
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SVAT]CREUSR (AUTILIS) !Other
  DES A*250 Description
  LEDTYPE M*15 Ledger type [menu 2653: 1=Not applicable,2=SNC base,3=IAS/IFRS standards,4=SNS micro entities,5=Others]
  ROOTACC A*15 Account root no.
  SIGN M*15 Expected sign [menu 610: 1=Debit,2=Credit,3=Unspecified]
  TAXCOD A*10 Taxonomy code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SVAT]UPDUSR (AUTILIS) !Other

## TAAAXXX (XXX) - Template table to copy
Keys (first = PK; D = duplicates allowed): XXX0 XXXNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  XXXDES DES Description
  XXXNUM A*3
  XXXSHO SHO Short description

## TABACCINT (TCI) - Intercompany account mapping
Notes: activity code INTCO
Keys (first = PK; D = duplicates allowed): TCI0 CPYSRC+CPYTGR
Fields:
  ACCSRCCDT GAC Source credit -> [GAC]GAC0 =COASRC;ACCSRCCDT (GACCOUNT) !Block
  ACCSRCDEB GAC Source debit -> [GAC]GAC0 =COASRC;ACCSRCDEB (GACCOUNT) !Block
  ACCTGRCDT GAC Target credit -> [GAC]GAC0 =COATGR;ACCTGRCDT (GACCOUNT) !Block
  ACCTGRDEB GAC Target debit -> [GAC]GAC0 =COATGR;ACCTGRDEB (GACCOUNT) !Block
  AUUID AUUID Single identifier
  BPRSRC BPR Source BP -> [BPR]BPR0 =[TCI]BPRSRC (BPARTNER) !Block
  BPRTGR BPR Target BP -> [BPR]BPR0 =[TCI]BPRTGR (BPARTNER) !Block
  COASRC COA Source main chart -> [COA]COA0 =[TCI]COASRC (GCOA) !Block
  COATGR COA Target main chart -> [COA]COA0 =[TCI]COATGR (GCOA) !Block
  CPYSRC CPY Source company -> [CPY]CPY0 =[TCI]CPYSRC (COMPANY) !Block
  CPYTGR CPY Target company -> [CPY]CPY0 =[TCI]CPYTGR (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  LEDTYPSRC M*15 Source [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEDTYPTGR M*15 Target [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  SACSRCCDT SAC Control
  SACSRCDEB SAC Control
  SACTGRCDT SAC Control
  SACTGRDEB SAC Control
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABACCLIK (TCK) - Reciprocal accounts
Keys (first = PK; D = duplicates allowed): TCK0 COA+FCY1+FCY2
Fields:
  ACC GAC General account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[TCK]BPR (BPARTNER) !Block
  COA COA Chart of accounts -> [COA]COA0 =[TCK]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY1 FCY Site 1 -> [FCY]FCY0 =[TCK]FCY1 (FACILITY) !Block
  FCY2 FCY Site 2 -> [FCY]FCY0 =[TCK]FCY2 (FACILITY) !Block
  SAC SAC Control
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABALLRUL (TRU) - Allocation and issue rules
Keys (first = PK; D = duplicates allowed): TRU0 TRUCOD
Fields:
  AUUID AUUID Single identifier
  COEFLT M*15 Coefficient filter [menu 2702: 1=No filter,2=Coefficient =,3=Coefficient <=,4=Coefficient >=] act:RUL
  COESOR M*15 Sort by coef [menu 2703: 1=No,2=Descending,3=Ascending] act:RUL
  CPLPCU M*4 PAC complete [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DOCFLT M*4 Document units [menu 1: 1=No,2=Yes] act:RUL
  LOCFLT M*15 Location filter [menu 2704: 1=No filter,2=Local location,3=Location 1 product,4=Location 2 product,5=Location 3 product] act:RUL
  LOTMGT M*15 Lot allocation sequence [menu 2709: 1=By lot,2=FIFO,3=FEFO,4=LIFO]
  PCUFLT M*4 Packing unit [menu 1: 1=No,2=Yes] act:RUL
  STAFLT M*20 Quality filter [menu 2701: 1=Status 'A',2=Status 'Q',3=Status 'A'+'Q',4=Status 'R',5=Status 'A'+'R',6=Status 'Q'+'R',7=Status 'A'+'Q'+'R'] act:RUL
  STUFLT M*4 Stock unit [menu 1: 1=No,2=Yes] act:RUL
  TEX AC0*6 Description
  TRUAXX AX3 Description
  TRUCOD A*6 Rule
  TRUDES DES Description
  UNTLOT M*4 Single-lot [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABBOMALT (TBO) - BOM codes
Keys (first = PK; D = duplicates allowed): TBO0 BOMALTTYP+BOMALT; TBO1 FCY+BOMALT+BOMALTTYP; TBO2 BOMALT+BOMALTTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[TBO]ACSCOD (ACCCOD) !Block
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Delete
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTUSE M*4 Cost utilization [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TBO]FCY (FACILITY) !Block
  MFGUSE M*4 Prod utilization [menu 1: 1=No,2=Yes]
  MPSUSE M*4 MPS utilization [menu 1: 1=No,2=Yes]
  MRPUSE M*4 MRP utilization [menu 1: 1=No,2=Yes]
  TBODES DES Description
  TBODESAXX AX3 Description
  TBOSHO SHO Short description
  TBOSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABCONTAINER (TCTR) - Freight container
Keys (first = PK; D = duplicates allowed): TCTR0 TCTRNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  DIU UOM Size unit -> [TUN]TUN0 =[TCTR]DIU (TABUNIT) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  MAXWEI WEI Max wgt.
  RGT M*4 Refrigerated [menu 1: 1=No,2=Yes]
  SHOAXX AX1 Short description
  TARWEI WEI Tare weight
  TCTRHEI DCB*5.4 Height
  TCTRLEN DCB*5.4 Length
  TCTRNUM TCTR Freight container -> [TCTR]TCTR0 =[TCTR]TCTRNUM (TABCONTAINER) !BSRA
  TCTRTYP M*15 Container type [menu 2081: 1=Container,2=Pallet,3=Pack,4=Parcel,5=Other]
  TCTRVOL VOL Volume
  TCTRWID DCB*5.4 Width
  TEU C*4 Twenty-foot equivalent unit
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USFVOL VOL Usable volume
  VOU UOM Volume unit -> [TUN]TUN0 =[TCTR]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[TCTR]WEU (TABUNIT) !Block

## TABCOSTMET (TCM) - Valuation methods
Keys (first = PK; D = duplicates allowed): TCM0 VLTCOD
Fields:
  AUUID AUUID Single identifier
  AVCPER M*15 Ave cost freq [menu 741: 1=Monthly,2=Annual,3=Moving]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUNNEG M*20(2) Negative quantity variance [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  CUNNEG2 M*20(2) Negative alternate [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  CUNPOS M*20(2) Positive quantity variance [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  CUNPOS2 M*20(2) Positive alternate [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  EXPNUM L*8 Export number
  ISSVLT2 M*20(2) Valuation alternate [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  ISSVLTCOD M*20(2) Issue costing [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  NULPRI M*4(2) Allow null cost [menu 1: 1=No,2=Yes]
  PFMCLC2 M*20 Alternative default [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  PFMCLCBAS M*20 Calculation basis [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  PRIREG M*4(2) Cost adjustment [menu 1: 1=No,2=Yes]
  PRIREGS M*4 Cost adjustment [menu 1: 1=No,2=Yes]
  RCPVLT2 M*20(2) Receipt alternate [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  RCPVLTCOD M*20(2) Receipt costing [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  TCMAXX AX3 Description
  TCMDES DES Description
  TCMSHO SHO Short description
  TCMSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VLTCOD A*3 Valuation method
  VLTINT M*4 Internal transac val [menu 1: 1=No,2=Yes]

## TABCOSTMVT (TVM) - Movement values
Keys (first = PK; D = duplicates allowed): TVM0 VLTCOD+MVTTYP+TRSCOD (D); TVM1 VLTCOD+NUM+MVTTYP+TRSCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  MVTNUL M*4 Allow null cost [menu 1: 1=No,2=Yes]
  MVTTYP M*15 Movement type [menu 704: 35 values, see local-menus.md]
  MVTVLT M*20 Valuation [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  MVTVLT2 M*20 Alternative default [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  NUM C*4 Number
  PRIREGX M*4 Cost adjustment [menu 1: 1=No,2=Yes]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VLTCOD TCM Valuation method -> [TCM]TCM0 =[TVM]VLTCOD (TABCOSTMET) !Delete

## TABCTL (TCT) - Response table
Notes: differs in V10 P1 (diff: ATD_TABCTL.htm)
Keys (first = PK; D = duplicates allowed): TCT0 TCT+TCTLIN; TCT1 TCT+ALPCOD+NUMCOD
Fields:
  ALPCOD A*20 Alphanumeric code
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESCOD DCT Code description
  DESCOD1 DCT Code description
  DESCOD2 DCT Code description
  DESCOD3 DCT Code description
  DESCOD4 DCT Code description
  DESCOD5 DCT Code description
  DESCOD6 DCT Code description
  DESCOD7 DCT Code description
  DESCOD8 DCT Code description
  DESCOD9 DCT Code description
  LAN LAN(10) Language -> [TLA]TLA0 =[TCT]LAN (TABLAN) !Block
  LANNBR C*4 Number of descriptions
  NUMCOD DCB*20 Numeric code
  TCT A*3 Response table
  TCTDES DES Description
  TCTDESAXX AX3 Description
  TCTLIN C*4 Line
  TCTTYP M*15 Type [menu 262: 1=Alphanumeric,2=Numeric]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABDEPAGIO (TDA) - Early discount/late charge table
Keys (first = PK; D = duplicates allowed): TDA0 DEP+LEG; TDA1 DEP (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =12;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =[TDA]DEP (TABDEPAGIO) !Other
  DEPDAY C*3(12) Daily horizon
  DEPDES DES Description
  DEPRAT RAT(12) Bank discount / charge rate
  DEPSHO SHO Short description
  DEPTYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  DESAXX AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[TDA]DIE (GDIE) !Block act:ANA
  GFY AGC Group -> [AGF]AGF0 =[TDA]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  PFINUM PFI Purchase invoice element -> [PFI]PFI0 =PFINUM (PFOOTINV) !Block
  RMDCMG M*4 Reminder campaign [menu 1: 1=No,2=Yes]
  SFINUM SFI Sales invoice element -> [SFI]SFI0 =SFINUM (SFOOTINV) !Block
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABEECNAT (TEC) - Intrastat transaction nature table
Notes: activity code DEB
Keys (first = PK; D = duplicates allowed): TEC0 EECNAT+LEG
Fields:
  A1 A*40 Alpha 1
  A2 A*40 Alpha 2
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;LEG (TABEECNAT) !Delete
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  N1 DCB*11.6 Numeric 1
  N2 DCB*11.6 Numeric 2
  SHOAXX AX1 Short description
  SOC AGC Group of company -> [AGF]AGF0 =[TEC]SOC (AGRPFCY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALSTO M*4 Value stock [menu 1: 1=No,2=Yes]

## TABEECSCH (TSC) - Statistical rule table
Notes: activity code DEB
Keys (first = PK; D = duplicates allowed): TSC0 EECSCH+LEG
Fields:
  A1 A*40 Alpha 1
  A2 A*40 Alpha 2
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  EECSCH TSC Statistical rule -> [TSC]TSC0 =EECSCH;LEG (TABEECSCH) !Delete
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLUX M*15 Physical flow [menu 2241: 1=Receipt,2=Shipment]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  N1 DCB*11.6 Numeric 1
  N2 DCB*11.6 Numeric 2
  SHOAXX AX1 Short description
  SOC AGC Group of company -> [AGF]AGF0 =[TSC]SOC (AGRPFCY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALSTO M*4 Value stock [menu 1: 1=No,2=Yes]

## TABGEOCOD (TGE) - Geographic codes
Keys (first = PK; D = duplicates allowed): TGE0 GEOCOD
Fields:
  AUUID AUUID Single identifier
  COUNTY A*17 County
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTY CTY City
  GEOCOD A*9 Geographic code
  LANDES DES Description
  LANSHO SHO Short description
  POSCOD POS Postal code
  STACOD A*3 County
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABINVCND (INVCND) - Invoicing terms
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): INVCND0 INVCND+LEG; INVCND1 INVCND (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[INVCND]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  FREQINV C*4 Invoicing freq
  GRP AGC Group -> [AGF]AGF0 =[INVCND]GRP (AGRPFCY) !Delete
  INVCND VCR Code
  INVCNDTYP M*10 Scheduled invoice type [menu 2420: 1=Normal,2=Fixed percentage,3=Frequency]
  INVDAY C*2 Day
  INVFBDDAYFLG M*4(7) Restricted days [menu 1: 1=No,2=Yes]
  INVFBDHLYFLG M*4 Unavailable days [menu 1: 1=No,2=Yes]
  INVMETH M*15 Invoicing method [menu 2978: 1=Pre-invoicing (term to mature),2=Post-invoicing (over due term)]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  PERINV M*15 Periodicity [menu 2231: 1=Day,2=Week,3=Half-month,4=Month,5=Quarter,6=Half-year,7=Year,8=Decade]
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[INVCND]UPDUSR (AUTILIS) !Other

## TABINVCNDLIN (INVCNDD) - Invoicing terms
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): INVCNDD0 INVCND+LEG+INVCNDLIN; INVCND1 INVCND+INVCNDLIN (D); INVCND2 INVCND+LEG (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[INVCNDD]CREUSR (AUTILIS) !Other
  INVCND INVCND Code -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Delete
  INVCNDLIN L*8 Line number
  INVCNDTYP M*10 Scheduled invoice type [menu 2420: 1=Normal,2=Fixed percentage,3=Frequency]
  INVDAYMON C*2(6) Day of the month
  INVMONTHEND M*15 Month end [menu 2237: 1=No,2=End of next month,3=End of current month]
  INVNBDAYS C*3 Number of days
  INVNBMONTHS C*2 Number of months
  INVPERCENT RAT Percentage
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MINAMTNOT MD1 Minimum amount
  MINAMTNOTCUR CUR Currency -> [TCU]TCU0 =[INVCNDD]MINAMTNOTCUR (TABCUR) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[INVCNDD]UPDUSR (AUTILIS) !Other

## TABLINCFG (TLP) - Product lines
Keys (first = PK; D = duplicates allowed): TLP0 CFGLIN
Fields:
  AUUID AUUID Single identifier
  CFGALP1 M*25 Alpha field 1 [menu 760: 1=Not affected]
  CFGALP2 M*25 Alpha field 2 [menu 760: 1=Not affected]
  CFGALP3 M*25 Alpha field 3 [menu 760: 1=Not affected]
  CFGALP4 M*25 Alpha field 4 [menu 760: 1=Not affected]
  CFGALP5 M*25 Alpha field 5 [menu 760: 1=Not affected]
  CFGALP6 M*25 Alpha field 6 [menu 760: 1=Not affected]
  CFGALPCOD1 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPCOD2 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPCOD3 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPCOD4 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPCOD5 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPCOD6 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGALPTCT1 TCT Control table -> [TCT]TCT0 =CFGALPTCT1;1 (TABCTL) !Block
  CFGALPTCT2 TCT Control table -> [TCT]TCT0 =CFGALPTCT2;1 (TABCTL) !Block
  CFGALPTCT3 TCT Control table -> [TCT]TCT0 =CFGALPTCT3;1 (TABCTL) !Block
  CFGALPTCT4 TCT Control table -> [TCT]TCT0 =CFGALPTCT4;1 (TABCTL) !Block
  CFGALPTCT5 TCT Control table -> [TCT]TCT0 =CFGALPTCT5;1 (TABCTL) !Block
  CFGALPTCT6 TCT Control table -> [TCT]TCT0 =CFGALPTCT6;1 (TABCTL) !Block
  CFGLIN A*5 Product line
  CFGLINAXX AX3 Description
  CFGLINDES DES Description
  CFGNUM1 M*25 Numeric field 1 [menu 760: 1=Not affected]
  CFGNUM2 M*25 Numeric field 2 [menu 760: 1=Not affected]
  CFGNUM3 M*25 Numeric field 3 [menu 760: 1=Not affected]
  CFGNUM4 M*25 Numeric field 4 [menu 760: 1=Not affected]
  CFGNUM5 M*25 Numeric field 5 [menu 760: 1=Not affected]
  CFGNUM6 M*25 Numeric field 6 [menu 760: 1=Not affected]
  CFGNUMCOD1 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMCOD2 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMCOD3 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMCOD4 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMCOD5 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMCOD6 M*15 Input [menu 762: 1=Mandatory entry,2=Optional entry,3=Display,4=Hidden]
  CFGNUMTCT1 TCT Control table -> [TCT]TCT0 =CFGNUMTCT1;1 (TABCTL) !Block
  CFGNUMTCT2 TCT Control table -> [TCT]TCT0 =CFGNUMTCT2;1 (TABCTL) !Block
  CFGNUMTCT3 TCT Control table -> [TCT]TCT0 =CFGNUMTCT3;1 (TABCTL) !Block
  CFGNUMTCT4 TCT Control table -> [TCT]TCT0 =CFGNUMTCT4;1 (TABCTL) !Block
  CFGNUMTCT5 TCT Control table -> [TCT]TCT0 =CFGNUMTCT5;1 (TABCTL) !Block
  CFGNUMTCT6 TCT Control table -> [TCT]TCT0 =CFGNUMTCT6;1 (TABCTL) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  INDFLD C*4(15) Index
  ITMFLD A*10(15) Equivalence field
  ITMFLDNBR C*2 No. of fields
  SCENUM CFG Scenario -> [CSC]CSC0 =[TLP]SCENUM (CFGSCE) !Block act:CFG
  SEAKEY M*15 Search key [menu 761: 1=Product number,2=Product description,3=Search key,4=Product line,5=Cfg document number]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABMAT (TMA) - ID numbers
Notes: differs in V9.0 P12 (diff: AT3_TABMAT.htm); differs in V10 P1 (diff: ATD_TABMAT.htm)
Keys (first = PK; D = duplicates allowed): TMA0 EMPNUM; TMA1 USR (D)
Fields:
  ACTDAT D Active date
  AUUID AUUID Single identifier
  CHGRAT DCB*12 Labor rate
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFFCY FCY Site -> [FCY]FCY0 =[TMA]DEFFCY (FACILITY) !Block
  DEFWCR WCR Work center group -> [TWC]TWC0 =[TMA]DEFWCR (TABWRKCTR) !Block
  DEFWST WST Work center
  ELPFLG M*4 Elapsed labor [menu 1: 1=No,2=Yes]
  EMPDES DES Description
  EMPNUM C*4 Employee ID
  EMPSHO SHO Short description
  EMPTYP M*15 Employee type [menu 2425: 1=Employee,2=Detailed team,3=Summary team]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  INACTDAT D Inactive date
  SHIFT SHFT Shift code -> [SFTS]SHF0 =[TMA]SHIFT (SFTSHIFT) !Block
  SUMEMP L*8 Number of employees
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR AUS User code -> [AUS]CODUSR =[TMA]USR (AUTILIS) !Delete

## TABMODELIV (TMD) - Delivery mode table
Keys (first = PK; D = duplicates allowed): TMD0 MDL
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  EECICT ICT Incoterm -> [ICTH]ICT0 =[TMD]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  GFY AGF Group -> [AGF]AGF0 =[TMD]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  MDL MDL Delivery mode -> [TMD]TMD0 =[TMD]MDL (TABMODELIV) !Other
  PORT ADI Port -> [ADI]CODE =951;PORT (ATABDIV) !Block act:DEBP
  REGION ADI Region -> [ADI]CODE =950;REGION (ATABDIV) !Block act:KPO
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABMSG (TMS) - Message table
Keys (first = PK; D = duplicates allowed): TMS0 MSGNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  MSGDES A*70 Description
  MSGDESAXX AXX Description
  MSGNUM C*4 Message
  MSGSHO SHO Short description
  MSGSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABPACKAGE (TPA) - Packaging table
Keys (first = PK; D = duplicates allowed): TPA0 PCK
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  DIU UOM Size unit -> [TUN]TUN0 =[TPA]DIU (TABUNIT) !Block
  EXPNUM L*8 Export number
  LANDESSHO A*60 Descriptions
  LBLFMT ARP Label format -> [ARP]ARP0 =[TPA]LBLFMT (AREPORT) !Block
  PCK PCK Packaging -> [TPA]TPA0 =[TPA]PCK (TABPACKAGE) !Other
  PCKHEI DCB*5.4 Height
  PCKLEN DCB*5.4 Length
  PCKPRI MD1 Packaging price
  PCKWEI WEI Tare weight
  PCKWID DCB*5.4 Width
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VOL VOL Volume
  VOU UOM Volume unit -> [TUN]TUN0 =[TPA]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[TPA]WEU (TABUNIT) !Block

## TABPAM (TAM) - Payment method table
Notes: differs in V9.0 P12 (diff: AT3_TABPAM.htm); differs in V10 P1 (diff: ATD_TABPAM.htm)
Keys (first = PK; D = duplicates allowed): TAM0 PAM+LEG
Fields:
  ACCEPT M*15 Acceptance [menu 682: 1=Letter of credit not accepted,2=Letter of credit accepted,3=Promissory note,4=Letter of credit to accept]
  ACCEPTFLG M*4 Acceptance management [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  GFY AGC Group of company -> [AGF]AGF0 =[TAM]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  PAM TAM Payment method -> [TAM]TAM0 =PAM;LEG (TABPAM) !Delete
  PAPTRT M*4 Paper draft [menu 1: 1=No,2=Yes]
  SDDFLG M*4 SDD management [menu 1: 1=No,2=Yes] act:SDD
  SEPFLG M*4 Credit card [menu 1: 1=No,2=Yes] act:SEPP
  SFTPAYMET ADI SAF-T payment method -> [ADI]CODE =316;SFTPAYMET (ATABDIV) !Block act:KPO
  SHOAXX AX1 Short description
  SOI A*4 Statement
  SWIPAMBVR M*15 Swiss payment type [menu 3661: 1=Non-ISR,2=Print,3=DTA,4=EZAG,5=ISO] act:KSW
  TYP C*4 Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABPAYTERM (TPT) - Payment term table
Keys (first = PK; D = duplicates allowed): TPT0 PTE+LEG+PTELIN; TPT1 PTE+PTELIN (D); TPT2 PTE+LEG (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYMON C*2(6) Day of the month
  DESAXX AX3 Description
  DUDMINAMT MD1 Minimum due date amount
  DUDPRC DCB*3.2 Due date %
  ENDMONFLG M*20 Month end [menu 2237: 1=No,2=End of next month,3=End of current month]
  FBDDAYFLG M*4(7) Restricted days [menu 1: 1=No,2=Yes]
  FBDHLYFLG M*4 Holidays excluded [menu 1: 1=No,2=Yes]
  GFY AGC Group -> [AGF]AGF0 =[TPT]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBRDAY C*2 Number of days
  NBRMON C*2 Number of months
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAMTYP M*15 Payment type [menu 292: 1=Open item,2=Prepayment,3=Holdback]
  PTE PTE Payment term -> [TPT]TPT0 =[TPT]PTE (TABPAYTERM) !BSRA
  PTELIN C*2 Condition line
  PTEMINAMT MD1 Minimum condition amount
  RPLPTE A*15 Alternate payment
  SDDFLG M*4 SDD management [menu 1: 1=No,2=Yes] act:SDD
  SHOAXX AX1 Short description
  SOIFLG M*4 On statement [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VATPRC DCB*3.2 Sales tax %

## TABPIVTYP (TPV) - Supp invoice type table
Keys (first = PK; D = duplicates allowed): TPV0 PIVTYP+LEG
Fields:
  AUTINV M*12 Automatic invoice [menu 1: 1=No,2=Yes] act:KPO
  AUUID AUUID Single identifier
  COD GAU Purchase auto journal -> [GAU]GAU0 =[TPV]COD (GAUTACE) !Block
  COD2 GAU BP auto journal -> [GAU]GAU0 =[TPV]COD2 (GAUTACE) !Block
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TPV]CODNUM (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  FASDSPLIN M*15 Invoicing element [menu 3303: 1=Distribution based on invoicing element,2=No distribution] act:FAS
  GFY AGF Group -> [AGF]AGF0 =[TPV]GFY (AGRPFCY) !Block
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  PIHTYP M*20 Purchase invoice cat. [menu 533: 1=Invoice,2=Additional invoice,3=Credit memo,4=Credit memo/Return]
  PIVTYP TPV Supp invoice type -> [TPV]TPV0 =[TPV]PIVTYP (TABPIVTYP) !BSRA
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SAFTINVTYP M*15 SAF-T document type [menu 2028: 1=Invoice,2=Simplified invoice,3=Debit note,4=Credit note,5=Fixed assets sale,6=Fixed assets return,7=Invoice-Receipt,8=Proforma,9=Consignment invoice] act:KPO
  SHOAXX AX1 Short description
  SIVTYP TSV Customer invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Block
  TPVDES A*30 Description
  TPVSHO A*10 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABPLACE (TPC) - Transit area
Keys (first = PK; D = duplicates allowed): TPC0 TPC
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPSNUM BPS Supplier -> [BPS]BPS0 =[TPC]BPSNUM (BPSUPPLIER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPC]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  DESSHO AX1 Short description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TPC]FCY (FACILITY) !Block
  LTITPC C*4 Lead time
  TPC TPC Location -> [TPC]TPC0 =[TPC]TPC (TABPLACE) !BSRA
  TPCTYP M Location type [menu 2080: 1=Harbor,2=Airport,3=Station,4=Warehouse,5=Customs,6=Site,7=Supplier,8=Other]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPC]UPDUSR (AUTILIS) !Other

## TABPLACETIME (TPCT) - Transport lead time
Keys (first = PK; D = duplicates allowed): TPCT0 DPETPC+ARVTPC+TRNTPC+BPTNUM
Fields:
  ARVTPC TPC Transit - arrival -> [TPC]TPC0 =[TPCT]ARVTPC (TABPLACE) !Block
  AUUID AUUID Single identifier
  BPTNUM BPT Carrier -> [BPT]BPT0 =[TPCT]BPTNUM (BPCARRIER) !RTZ
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPCT]CREUSR (AUTILIS) !Other
  DPETPC TPC Transit - start -> [TPC]TPC0 =[TPCT]DPETPC (TABPLACE) !Block
  LTITPC C*4 Lead time
  TRNTPC M*15 Transport mode [menu 2027: 1=Air,2=Sea,3=Road,4=Rail,5=Multimodal,6=Not defined]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPCT]UPDUSR (AUTILIS) !Other

## TABPNHTYP (TPN) - Return type table
Notes: activity code TRSNE
Keys (first = PK; D = duplicates allowed): TPN0 PNHTYP+LEG; TPN1 PNHTYP (D)
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TPN]CODNUM (ACODNUM) !Block
  CODNUMCPT A*100 Counter complement
  CODNUMCPY ANM Inter-cy counter -> [ANM]ANM0 =[TPN]CODNUMCPY (ACODNUM) !Block
  CODNUMCPYD ANM Fnl inter-cy cntr -> [ANM]ANM0 =[TPN]CODNUMCPYD (ACODNUM) !Block
  CODNUMEND ANM Final counter -> [ANM]ANM0 =[TPN]CODNUMEND (ACODNUM) !Block
  CODNUMFCY ANM Intersite sequence no. -> [ANM]ANM0 =[TPN]CODNUMFCY (ACODNUM) !Block
  CODNUMFCYD ANM Fnl inter-site cntr -> [ANM]ANM0 =[TPN]CODNUMFCYD (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TPN]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  PNHTYP TPN Return type -> [TPN]TPN0 =PNHTYP;LEG (TABPNHTYP) !Delete
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document]
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)]
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABPRTMOD (TPM) - Print template table
Notes: differs in V9.0 P12 (diff: AT3_TABPRTMOD.htm); differs in V10 P1 (diff: ATD_TABPRTMOD.htm)
Keys (first = PK; D = duplicates allowed): TPM0 TPMCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  PURORC A*30 Supp. open order
  PURORCNBE C*1 No. copies supp. open order
  PURORD A*30 Supplier order
  PURORDNBE C*1 No. copies supp. order
  PURQUO A*30 RFQ
  PURQUONBE C*1 No. copies request for quote
  PURRET A*30 Supplier return
  PURRETNBE C*1 No. copies return
  SALCRE A*30 Customer credit memo
  SALCRENBE C*1 No. copies customer credit memo
  SALDLV A*30 Delivery
  SALDLVNBE C*1 No. copies delivery
  SALINV A*30 Customer invoice
  SALINVNBE C*1 No. copies customer inv.
  SALORC A*30 Customer open order
  SALORCNBE C*1 No. copies cust. open order
  SALORD A*30 Customer order
  SALORDNBE C*1 No. copies customer ord.
  SALQUO A*30 Quotes
  SALQUONBE C*1 No. copies quote
  SHOAXX AX1 Short description
  TPMCOD A*5 Template code
  TPMDES A*30 Description
  TPMSHO A*10 Short description
  TRSEFAT A*30 EFAT A/P-A/R invoice act:EFAT
  TRSEFATNBE C*1 No. copies act:EFAT
  TRSNCEFANBE C*1 No. copies act:EFAT
  TRSNCEFAT A*30 EFAT A/P-A/R cr. memo act:EFAT
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABRATVAT (TRA) - Tax rates
Keys (first = PK; D = duplicates allowed): TRA0 VAT+LEG+CPY+STRDAT; TRA1 VAT+CPY+STRDAT (D)
Fields:
  AMTTSD DCB*9.2 Threshold act:PTX
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TRA]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TRA]CREUSR (AUTILIS) !Other
  DEDRAT DCB*3.6 Deductible %
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  STRDAT D Validity start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TRA]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;LEG (TABVAT) !Delete
  VATEXEFLG M*4 Exemption flag [menu 1: 1=No,2=Yes]
  VATRAT DCB*3.6 Rate

## TABREOPOL (TRP) - Reorder policies table
Keys (first = PK; D = duplicates allowed): TRP0 REOPOL
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  PLNANYCOD M*4 Replanning analysis [menu 1: 1=No,2=Yes]
  REOPOL A*3 Reorder policy
  REOQTYCOD M*30 Reorder quantity [menu 258: 1=Net quantity,2=Minimum quantity without rounding,3=Minimum quantity with rounding]
  SAFSTOCOD M*4 Safety stock [menu 1: 1=No,2=Yes]
  SHRFLG M*4 Apply loss % [menu 1: 1=No,2=Yes]
  SPLCOD M*4 Splitting [menu 739: 1=None,2=Parallel,3=Successive]
  STOTIAFLG M*4 Include available stock [menu 1: 1=No,2=Yes]
  SUGTYP M*30 Suggestion type [menu 218: 1=No processing,2=With MRP pegging,3=Wthout MRP pegging,4=MRP pegging only]
  TRPAXX AX3 Policy description
  TRPDES DES Policy description
  TRPSHO SHO Short description
  TRPSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABROUALT (TRO) - BOM routings
Keys (first = PK; D = duplicates allowed): TRO0 ROUALT; TRO1 FCY+ROUALT
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[TRO]ACSCOD (ACCCOD) !Block
  AUUID AUUID Single identifier
  BOMALT1 TBO BOM code -> [TBO]TBO0 =2;BOMALT1 (TABBOMALT) !Block
  BOMALT2 TBO BOM code -> [TBO]TBO0 =2;BOMALT2 (TABBOMALT) !Block
  BOMALT3 TBO BOM code -> [TBO]TBO0 =2;BOMALT3 (TABBOMALT) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTUSE M*4 Cost utilization [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TRO]FCY (FACILITY) !Block
  MFGUSE M*4 Prod utilization [menu 1: 1=No,2=Yes]
  RCCUSE M*4 RCCP utilization [menu 1: 1=No,2=Yes]
  ROUALT TRO Routing code -> [TRO]TRO0 =[TRO]ROUALT (TABROUALT) !Delete
  TRODES DES Description
  TRODESAXX AX3 Description
  TROSHO SHO Short description
  TROSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABROUND (TRN) - Roundings
Keys (first = PK; D = duplicates allowed): TRD0 RNDCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  RNDCOD A*3 Rounding code
  RNDDEC DCB*2.2 Rounding
  RNDDES DES Description
  RNDDESAXX AX3 Description
  RNDSHO SHO Short description
  RNDSHOAXX AX1 Short description
  RNDTYP M*15 Rounding type [menu 221: 1=Round up,2=Round down,3=Round to the nearest]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSCA (TSR) - Rejects
Keys (first = PK; D = duplicates allowed): TSR0 SCANUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SCADES A*70 Description
  SCADESAXX AXX Description
  SCANUM C*4 Rejection
  SCASHO SHO Short description
  SCASHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSDHTYP (TSD) - Table types deliveries
Keys (first = PK; D = duplicates allowed): TSD0 SDHTYP+LEG
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TSD]CODNUM (ACODNUM) !Block
  CODNUMCPY ANM Inter-cy counter -> [ANM]ANM0 =[TSD]CODNUMCPY (ACODNUM) !Block
  CODNUMCPYD ANM Fnl inter-cy cntr -> [ANM]ANM0 =[TSD]CODNUMCPYD (ACODNUM) !Block
  CODNUMEND ANM Final counter -> [ANM]ANM0 =[TSD]CODNUMEND (ACODNUM) !Block
  CODNUMFCY ANM Intersite sequence no. -> [ANM]ANM0 =[TSD]CODNUMFCY (ACODNUM) !Block
  CODNUMFCYD ANM Fnl inter-site cntr -> [ANM]ANM0 =[TSD]CODNUMFCYD (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATUPDFLG M*12 Update document date [menu 1: 1=No,2=Yes] act:KPO
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TSD]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)] act:KPO
  SDHCAT M*20 Delivery category [menu 490: 1=Normal,2=Loan,3=For subcontract,4=Nonbillable]
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;LEG (TABSDHTYP) !Delete
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSGHTYP (TSG) - Stock change type
Notes: activity code TRSNE
Keys (first = PK; D = duplicates allowed): TSG0 SGHTYP+LEG; TSG1 SGHTYP (D)
Fields:
  AUUID AUUID Single identifier
  BETFCYCOD M*15 Destination [menu 792: 1=Internal,2=Intersite,3=Customer,4=Subcontract transfer,5=Subcontract return]
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TSG]CODNUM (ACODNUM) !Block
  CODNUMEND ANM Final counter -> [ANM]ANM0 =[TSG]CODNUMEND (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TSG]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document]
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)]
  SGHTYP TSG Stock change type -> [TSG]TSG0 =SGHTYP;LEG (TABSGHTYP) !Delete
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSIVTYP (TSV) - Customer invoice type table
Notes: differs in V9.0 P12 (diff: AT3_TABSIVTYP.htm)
Keys (first = PK; D = duplicates allowed): TSV0 SIVTYP+LEG; TSV1 SIVTYP (D)
Fields:
  AUTINV M*12 Automatic invoice [menu 1: 1=No,2=Yes] act:KPO
  AUUID AUUID Single identifier
  COD GAU Sales auto journal -> [GAU]GAU0 =[TSV]COD (GAUTACE) !Block
  COD2 GAU BP auto journal -> [GAU]GAU0 =[TSV]COD2 (GAUTACE) !Block
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TSV]CODNUM (ACODNUM) !Block
  CODNUMEND ANM Sequence number -> [ANM]ANM0 =[TSV]CODNUMEND (ACODNUM) !Block act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSHVATRGM M*4 Cash VAT [menu 1: 1=No,2=Yes] act:KPO
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  GFY AGF Group -> [AGF]AGF0 =[TSV]GFY (AGRPFCY) !Block
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  INVCAN M*4 Cancellation invoice [menu 1: 1=No,2=Yes] act:INVCA
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  NUMDAYINV C*4 Num day next invoice
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SAFTINVTYP M*15 SAF-T document type [menu 2028: 1=Invoice,2=Simplified invoice,3=Debit note,4=Credit note,5=Fixed assets sale,6=Fixed assets return,7=Invoice-Receipt,8=Proforma,9=Consignment invoice] act:KPO
  SHOAXX AX1 Short description
  SIVTYP TSV Customer invoice type -> [TSV]TSV0 =[TSV]SIVTYP (TABSIVTYP) !BSRA
  TSVDES A*30 Description
  TSVSHO A*10 Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSTASTO (TST) - Stock status report
Keys (first = PK; D = duplicates allowed): TST0 STASTO
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXYQQQSTA TST Obsolete Q status -> [TST]TST0 =[TST]EXYQQQSTA (TABSTASTO) !Block
  EXYRRRSTA TST Obsolete R status -> [TST]TST0 =[TST]EXYRRRSTA (TABSTASTO) !Block
  STAAXX AX3 Description
  STADES DES Description
  STASHO SHO Short description
  STASHOAXX AX1 Short description
  STASTO A*3 Status
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSTORUL (SRU) - Stock management rules
Keys (first = PK; D = duplicates allowed): SRU0 TCLCOD+STOFCY+TRSTYP+TRSCOD
Fields:
  AUUID AUUID Single identifier
  AUZACT M*25 Active version [menu 2782: 1=No,2=Yes, except on hold,3=Yes]
  AUZPRO M*25 Prototype version [menu 2782: 1=No,2=Yes, except on hold,3=Yes]
  AUZSST A*30 Authorized substatuses
  AUZSTA M*20 Authorized statuses [menu 2701: 1=Status 'A',2=Status 'Q',3=Status 'A'+'Q',4=Status 'R',5=Status 'A'+'R',6=Status 'Q'+'R',7=Status 'A'+'Q'+'R']
  AUZSTP M*25 Version stopped [menu 2783: 1=No,2=No, unless exception,3=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACLOT M*12 Lot entry [menu 2705: 1=No,2=Free,3=New lot]
  DEFSTA A*3 Default status
  FORSTA A*200 Formula
  LOCNUM M*15 Location no. [menu 2713: 1=,2=Receipt,3=Stock,4=Picking,5=Workstation,6=Delivery,7=Store,8=Customer return,9=Return from return,10=To be defined,11=To be defined,12=To be defined]
  LOCNUM2 M*15 Location no. [menu 2713: 1=,2=Receipt,3=Stock,4=Picking,5=Workstation,6=Delivery,7=Store,8=Customer return,9=Return from return,10=To be defined,11=To be defined,12=To be defined]
  LOCNUM3 M*15 Location no. [menu 2713: 1=,2=Receipt,3=Stock,4=Picking,5=Workstation,6=Delivery,7=Store,8=Customer return,9=Return from return,10=To be defined,11=To be defined,12=To be defined]
  LOTSUPINH M*15 Lot by default [menu 2708: 1=None,2=Supplier lot,3=Document number]
  ORDVER M*4 Entered version [menu 1: 1=No,2=Yes]
  QLYCTLFLG M*4 Analysis request [menu 1: 1=No,2=Yes]
  SHLLOT M*25 Output lot [menu 484: 1=No, expiration date control,2=No, use by date control,3=Yes]
  STOFCY FCY Storage site -> [FCY]FCY0 =[SRU]STOFCY (FACILITY) !Block
  TCLCOD ITG Category -> [ITG]ITG0 =STOFCY;TCLCOD (ITMCATEG) !Delete
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSTYP M*15 Movement type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABTNHTYP (TTN) - Transport note type
Notes: activity code TRSNE
Keys (first = PK; D = duplicates allowed): TTN0 TNHTYP+LEG; TTN1 TNHTYP (D)
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TTN]CODNUM (ACODNUM) !Block
  CODNUMEND ANM Final counter -> [ANM]ANM0 =[TTN]CODNUMEND (ACODNUM) !Block act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATUPDFLG M*12 Update document date [menu 1: 1=No,2=Yes] act:KPO
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TTN]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)] act:KPO
  SHOAXX AX1 Short description
  TNHTYP TTN Type -> [TTN]TTN0 =TNHTYP;LEG (TABTNHTYP) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABUNAVAIL (TUV) - Unavailable periods
Keys (first = PK; D = duplicates allowed): UVY0 UVYCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Site/Company group -> [AGF]AGF0 =[TUV]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UVYAXX AXX Description
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[TUV]UVYCOD (TABUNAVAIL) !Other
  UVYDES DES Description
  UVYENDDAT D End date act:TUV
  UVYNAM A*60 Description act:TUV
  UVYNBR C*4 Line
  UVYPER M*4 Periodic [menu 1: 1=No,2=Yes]
  UVYSHO SHO Short description
  UVYSTRDAT D Start date act:TUV

## TABVAC (TVC) - Tax determination table
Keys (first = PK; D = duplicates allowed): TVC0 COD+LEG; TVC1 VACBPR+VACITM (D); TVC2 VATTYP-ENAFLG-LEG-GRP-VACBPR-VACITM+COD
Fields:
  ANDOR M*5(5) And / or [menu 56: 1=And,2=Or]
  ATB ATB Table -> [ATB]CODFIC =[TVC]ATB (ATABLE) !Other
  AUUID AUUID Single identifier
  COD A*15 Tax determination code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXP1 A*250 Formula
  EXP2 A*250 Formula
  EXPTST A*250 Formula
  FLD AVA(5) Field
  GRP AGF Group -> [AGF]AGF0 =[TVC]GRP (AGRPFCY) !Delete
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  OPE M*10(5) Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB BP tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACDES DES Description
  VACITM TVI Product tax level -> [TVI]TVI0 =VACITM;[V]GSUPCLE (TABVACITM) !Block
  VACSHO SHO Short description
  VALI A*80(5) Value
  VALS AVV*80(5) Value
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]

## TABVACBPR (TVB) - BP tax rule table
Keys (first = PK; D = duplicates allowed): TVB0 VACBPR+LEG
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  REGVAC M*15 Rule type [menu 2603: 1=Normal,2=Export,3=Tax exempt,4=EU]
  SALCLA A*10 Sales class
  SHOAXX AX1 Short description
  SOC AGC Company group -> [AGF]AGF0 =[TVB]SOC (AGRPFCY) !Block
  SPADCL347 M*4 Declaration 347 [menu 1: 1=No,2=Yes] act:KSP
  SPADCL349 M*4 Declaration 349 [menu 1: 1=No,2=Yes] act:KSP
  SPAEURSRV M*4 EU services [menu 1: 1=No,2=Yes] act:KSP
  SPAEXEOPE M*4 Exempted operation [menu 1: 1=No,2=Yes] act:KSP
  SPAIGIC M*4 Canaries IGIC [menu 1: 1=No,2=Yes] act:KSP
  SPAISP M*4 Tax return (RC) [menu 1: 1=No,2=Yes] act:KSP
  SPAJOUDCL M*4 No book declaration [menu 1: 1=No,2=Yes] act:KSP
  SPAOPE340 ADI Operation 340 code -> [ADI]CODE =393;SPAOPE340 (ATABDIV) !Block act:KSP
  TYP C*4 Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;LEG (TABVACBPR) !Delete
  VAT VAT Tax code -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## TABVACITM (TVI) - Tax level table
Notes: differs in V9.0 P12 (diff: AT3_TABVACITM.htm)
Keys (first = PK; D = duplicates allowed): TVI0 VACITM+LEG
Fields:
  A1 A*40 Alpha 1
  A2 A*40 Alpha 2
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  N1 DCB*11.6 Numeric 1
  N2 DCB*11.6 Numeric 2
  SHOAXX AX1 Short description
  SOC AGC Company group -> [AGF]AGF0 =[TVI]SOC (AGRPFCY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI Tax level -> [TVI]TVI0 =VACITM;LEG (TABVACITM) !Delete
  WASMGT MGTW Waste management -> [MGTW]MGTW1 =[TVI]WASMGT (MGTWASTE) !Block act:KPO

## TABVAT (TVT) - Tax code table
Notes: differs in V9.0 P12 (diff: AT3_TABVAT.htm); differs in V10 P1 (diff: ATD_TABVAT.htm)
Keys (first = PK; D = duplicates allowed): TVT0 VAT+LEG; TVT1 VAT (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =10;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUS1AGSTSAL M*4 1A GST on sales [menu 1: 1=No,2=Yes] act:KAU
  AUS1BGSTPUR M*4 1B GST on purchases [menu 1: 1=No,2=Yes] act:KAU
  AUSBAS M*15 [menu 3676: 1=1A,2=1B] act:KAU
  AUSG10CAPPUR M*4 G10 capital purchase [menu 1: 1=No,2=Yes] act:KAU
  AUSG11NCAPPU M*4 G11 non capital pur [menu 1: 1=No,2=Yes] act:KAU
  AUSG1TOTSA M*4 G1 total sales [menu 1: 1=No,2=Yes] act:KAU
  AUSG2EXPSAL M*4 G2 export sales [menu 1: 1=No,2=Yes] act:KAU
  AUSG3GSTFRES M*4 G3 GST free sales [menu 1: 1=No,2=Yes] act:KAU
  AUSVAT VAT Associated tax code -> [TVT]TVT0 =AUSVAT;[V]GSUPLCE (TABVAT) !Block act:KAU
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[TVT]DIE (GDIE) !Block act:ANA
  GRP AGF Group -> [AGF]AGF0 =[TVT]GRP (AGRPFCY) !Delete
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  POREXEMOT A*3 Exemption reason act:KPO
  SAT A*1 Province act:KAG
  SHOAXX AX1 Short description
  SPAAGRVAT M*4 Agrarian tax rule [menu 1: 1=No,2=Yes] act:KSP
  SPAEXEVAT M*4 Operation to be excluded [menu 1: 1=No,2=Yes] act:KSP
  SPAIMPVAT M*4 Import tax [menu 1: 1=No,2=Yes] act:KSP
  SPAINR M*4 Interests [menu 1: 1=No,2=Yes] act:KSP
  SPAIVT303 M*4 Investments 303 [menu 1: 1=No,2=Yes] act:KSP
  SPANRS M*4 Nonresident [menu 1: 1=No,2=Yes] act:KSP
  SPAPRA303 M*4 Pro rata 303 [menu 1: 1=No,2=Yes] act:KSP
  SPAPURTAG M*4 Purchase travel agency [menu 1: 1=No,2=Yes] act:KSP
  SPARNT M*4 Rentals [menu 1: 1=No,2=Yes] act:KSP
  SPASPETAX M*4 Special tax [menu 1: 1=No,2=Yes] act:KSP
  SPAUSEPDT M*4 Used goods [menu 1: 1=No,2=Yes] act:KSP
  SPAVAT VAT Associated tax code -> [TVT]TVT0 =SPAVAT;[V]GSUPCLE (TABVAT) !Block act:KSP
  TEXAXX AXX Legal mention
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;LEG (TABVAT) !Other
  VATBAS M*15 Amount no. [menu 257: 1=No,2=Amount 1,3=Amount 2]
  VATCHA M*4 Subject to tax [menu 1: 1=No,2=Yes]
  VATDES DES Description
  VATFOR FOR Formula -> [TFO]TFO0 =1;VATFOR (TABFOR) !Block
  VATPAY M*15 VAT type [menu 204: 1=On debit,2=On payment]
  VATRAT DCB*3.2 Rate
  VATSHO SHO Short description
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]
  VATVAC TVB Tax rule -> [TVB]TVB0 =VATVAC;[V]GSUPCLE (TABVACBPR) !Block

## TABVATEXE (TEX) - Tax exemption table
Keys (first = PK; D = duplicates allowed): TEX0 BPCNUM+NUMORD
Fields:
  AUUID AUUID Single identifier
  BPCNUM BPR Customer -> [BPR]BPR0 =[TEX]BPCNUM (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[TEX]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D End date
  EXERAT DCB*3.6 Exemption rate
  EXEREN ADI Exemption reason -> [ADI]CODE =365;EXEREN (ATABDIV) !Block
  FLGUSE M*4 Usage flag [menu 1: 1=No,2=Yes]
  NUMORD C*2 Order no.
  SPPNUM A*30 Not justifying
  STRDAT D Start date
  TSDMAX DCB*9.2 Maximum threshold
  TSDMIN DCB*9.2 Minimum threshold
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]

## TABWEEDIA (TWD) - Weekly structures
Keys (first = PK; D = duplicates allowed): TWD0 TWD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYCAP DCB*2.2(7) Daily capacity
  DAYCAPNOM DCB*2.2 Capacity
  DIAHOU DIH(7) Time table schema -> [DIH]DIH0 =[TWD]DIAHOU (DIAHOU) !RTZ
  EXPNUM L*8 Export number
  TWD A*3 Weekly structure
  TWDDES DES Description
  TWDDESAXX AX3 Description
  TWDSHO SHO Short description
  TWDSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TACONTAINERC (TCTRC) - Container clobs
Keys (first = PK; D = duplicates allowed): TCTRC0 TCTRNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCTRC]CREUSR (AUTILIS) !Other
  IMG ABIMG*1 Images
  TCTRNUM TCTR Freight container -> [TCTR]TCTR0 =[TCTRC]TCTRNUM (TABCONTAINER) !Block
  TEX ACRTF*1 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCTRC]UPDUSR (AUTILIS) !Other

## TASK (TSK) - Task
Notes: differs in V9.0 P12 (diff: AT3_TASK.htm); differs in V10 P1 (diff: ATD_TASK.htm)
Keys (first = PK; D = duplicates allowed): TSK0 TSKNUM; TSK1 TSKDAT+TSKNUM; TSK2 TSKCMP (D); TSK3 TSKCCN (D); TSK4 TSKREP+TSKDAT+TSKNUM; TSK5 CREUSR (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  HOUTIMSPG L*8 Time spent (hours)
  MNTTIMSPG C*2 Time passed (minute)
  NUMFULOBJ CLC Chrono txt file
  NUMFULRPO CLC Chrono txt file
  OBJFLG C*2 Flag text file
  RPOFLG C*2 Flag text file
  SALFCY FCY Site -> [FCY]FCY0 =[TSK]SALFCY (FACILITY) !Block
  TSKCCN AIN Contact (relationship) -> [AIN]AIN0 =[TSK]TSKCCN (CONTACTCRM) !Block
  TSKCMGNUM CMG Marketing campaign -> [CMG]CMG0 =[TSK]TSKCMGNUM (CMARKETING) !Block
  TSKCMP BPR BP -> [BPR]BPR0 =[TSK]TSKCMP (BPARTNER) !Block
  TSKCOR COR Outlook contact -> [COR]COR0 =[TSK]TSKCOR (CORRESPOND) !Block
  TSKDAT D Due date
  TSKDEL C*4 Late
  TSKDES CLX Description
  TSKDON M*4 Completed [menu 1: 1=No,2=Yes]
  TSKNUM VCR Task chrono
  TSKOPGNUM VCR Marketing operation
  TSKOPGTYP AOB Operation type -> [AOB]ABREV =[TSK]TSKOPGTYP (AOBJET) !Block
  TSKORI M*15 Source [menu 2992: 1=None,2=Service Request,3=Mass mailing,4=Call campaign,5=Trade show,6=Media campaign,7=Follow-up campaign,8=Marketing campaign]
  TSKORIADI ADI Source -> [ADI]CODE =439;TSKORIADI (ATABDIV) !Block
  TSKORIAOB AOB Object code -> [AOB]ABREV =[TSK]TSKORIAOB (AOBJET) !Block
  TSKORITYP M*15 Source type [menu 3037: 1=Manual,2=Generated,3=Synchronization,4=Import]
  TSKORIVCR VCR Original document no.
  TSKORIVCRL L*8 Original line no.
  TSKPIOLEV ADI Priority level -> [ADI]CODE =405;TSKPIOLEV (ATABDIV) !Block
  TSKPJT PJT Project -> [PIM]PIM0 =[TSK]TSKPJT (PIMPL) !Block
  TSKREP REP Sales rep -> [REP]REP0 =[TSK]TSKREP (SALESREP) !Block
  TSKRPO CLX Report
  TSKSAO ADI Satisfaction -> [ADI]CODE =435;TSKSAO (ATABDIV) !Block
  TSKSTR D Start date
  TSKTYP ADI Category -> [ADI]CODE =431;TSKTYP (ATABDIV) !Block
  TYPFULOBJ CLT Type text file
  TYPFULRPO CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TAUTILIS (TAU) - Safe X3 WAS users
Notes: activity code TCAYT
Keys (first = PK; D = duplicates allowed): TAU0 USR
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[TAU]BPRNUM (BPARTNER) !Other
  CODPRF AYH Profile code -> [AYH]AYH0 =[TAU]CODPRF (AYTPRFUSR) !RTZ
  CODUSR AUS User -> [AUS]CODUSR =[TAU]CODUSR (AUTILIS) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TAU]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TAU]CUR (TABCUR) !RTZ
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  INTUSR AX3 Description
  MAIL MAI E-mail
  PWD A*24 Password
  SALFCY FCY Sales site -> [FCY]FCY0 =[TAU]SALFCY (FACILITY) !RTZ
  STOFCY FCY Shipment site -> [FCY]FCY0 =[TAU]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TAU]UPDUSR (AUTILIS) !Other
  USR TAU User code -> [TAU]TAU0 =[TAU]USR (TAUTILIS) !Delete

## TAXLINK (TLK) - Tax calc. basis calculation (link)
Keys (first = PK; D = duplicates allowed): DLK0 CLE
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =1;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AGTPCPBPR M*4 Collection agent [menu 1: 1=No,2=Yes]
  AGTPCPCPY M*4 Collection agent [menu 1: 1=No,2=Yes]
  AGTSATTAX M*4 Collection agent [menu 1: 1=No,2=Yes]
  AMTBAS MD5 Calculated basis
  AMTBAS1 MD5 Calculated basis
  AMTBAS2 MD5 Calculated basis
  AMTNOT MD1 Amount - tax
  AMTNOTLIN MD1 Line amount - tax
  AMTTAX1 MD1 Tax amount 1
  AMTTAXLIN1 MD1 Tax amount 1
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[TLK]BPRNUM (BPARTNER) !Other
  CLE A*3 Key
  CPY CPY Company -> [CPY]CPY0 =[TLK]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TLK]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TLK]CUR (TABCUR) !Other
  DAT D Date
  DLKFIL A*50
  FCY FCY Site -> [FCY]FCY0 =[TLK]FCY (FACILITY) !Other
  FLGSATTAX M*4(25) Collection agent [menu 1: 1=No,2=Yes]
  GRP AGF(99) Group -> [AGF]AGF0 =[TLK]GRP (AGRPFCY) !Delete
  ITMREF ITM Product -> [ITM]ITM0 =[TLK]ITMREF (ITMMASTER) !Delete
  ITMWEI WEI Item weight
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBGRP C*4 Number of groups
  PURFCY FCY Purchase site -> [FCY]FCY0 =[TLK]PURFCY (FACILITY) !Other
  QTY DCB*9.6 Quantity
  QTYSTU DCB*9.6 STK quantity
  RATRPT RCU Reporting rate
  SALFCY FCY Sales site -> [FCY]FCY0 =[TLK]SALFCY (FACILITY) !Other
  SATFLG C*4 Indicator
  SATISS SAT Issue act:PTX
  SATRCP SAT Receipt act:PTX
  SATTAX A*3(25) BP regions
  TCLCOD ITG Product category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Other
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TLK]UPDUSR (AUTILIS) !Other
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACITM TVI Tax level -> [TVI]TVI0 =VACITM;[V]GSUPCLE (TABVACITM) !Block
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]

## TBASKET (TBA) - Shopping basket
Notes: activity code TCAYT
Keys (first = PK; D = duplicates allowed): TBA0 NUM; TBA1 USR+SOHNUM+STAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TBA]CREUSR (AUTILIS) !Other
  NUM VCR Document no.
  SOHNUM VCR Order no.
  STAT M*4 Basket status [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TBA]UPDUSR (AUTILIS) !Other
  USR TAU User code -> [TAU]TAU0 =[TBA]USR (TAUTILIS) !Delete

## TBASKETD (TBD) - Shopping basket line
Notes: activity code TCAYT
Keys (first = PK; D = duplicates allowed): TBD0 NUM+BASKLIN; TBD1 NUM+ITMREF
Fields:
  AUUID AUUID Single identifier
  BASKLIN C*4 Line number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TBD]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[TBD]ITMREF (ITMMASTER) !Block
  NUM VCR Document no.
  PRICE DCB*9.2 Price
  QTY L*8 Quantity
  SLT M*4 Selected [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TBD]UPDUSR (AUTILIS) !Other

## TCBLOB (TBB) - Special folders
Keys (first = PK; D = duplicates allowed): TBB0 CODBLB+IDENT1+IDENT2+IDENT3
Fields:
  AUUID AUUID Single identifier
  BLOB ABB Image file
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CODBLB IDB Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TBB]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 IDB Identifier 3
  NAMBLB DES File name
  TYPBLB AT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TBB]UPDUSR (AUTILIS) !Other

## TCCLOB (TBC) - Special text files
Keys (first = PK; D = duplicates allowed): TBC0 CODCLB+IDENT1+IDENT2+IDENT3
Fields:
  AUUID AUUID Single identifier
  CLOB AC0*10 Text file (clob)
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CODCLB IDB Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TBC]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 IDB Identifier 3
  NAMCLB DES File name
  TYPCLB C*4 Type clob
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TBC]UPDUSR (AUTILIS) !Other

## TEXCLOB (TXC) - Text files
Keys (first = PK; D = duplicates allowed): TXC0 CODE; TXC1 IDENT1+IDENT2+IDENT3 (D)
Fields:
  AUUID AUUID Single identifier
  CODE TXC Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  IDENT1 A*30 Identifier 1
  IDENT2 A*30 Identifier 2
  IDENT3 A*30 Identifier 3
  TEXTE ACB Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## TEXCPT (TCC) - Text counter by table
Keys (first = PK; D = duplicates allowed): TCC0 ABRFIC
Fields:
  ABRFIC ABR Table abbreviation
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCC]CREUSR (AUTILIS) !Other
  TEXSEQ L*8 Text sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCC]UPDUSR (AUTILIS) !Other

## TIMEADJUST (TAD) - Daylight saving time
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TAD0 COD+STRDAT
Fields:
  AUUID AUUID Single identifier
  COD TAD Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TAD]CREUSR (AUTILIS) !Other
  DES AX3 Description
  OFFSET DCB*9.2 Time zone difference
  STRDAT D Start date
  TTRCODEND TTR Change
  TTRCODSTR TTR Change
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TAD]UPDUSR (AUTILIS) !Other

## TIMETRANS (TTR) - Change to daylight saving time
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TTR0 COD
Fields:
  AUUID AUUID Single identifier
  COD TTR Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TTR]CREUSR (AUTILIS) !Other
  DAYWEE M*20 Day of the week [menu 9833: 1=Monday,2=Tuesday,3=Wednesday,4=Thursday,5=Friday,6=Saturday,7=Sunday]
  DDAY C*2 Day
  DES AX3 Description
  FXDFLG M*20 Fixed date [menu 1: 1=No,2=Yes]
  MON M*20 Month [menu 9001: 1=January,2=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December]
  TIMDAY TIH Time
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TTR]UPDUSR (AUTILIS) !Other
  WEE C*1 Week

## TIMEZONEINFO (TZI) - Time zones
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TZI0 COD; TZI1 UTCOFFSET+COD
Fields:
  AUUID AUUID Single identifier
  COD TZI Code -> [TZI]TZI0 =[TZI]COD (TIMEZONEINFO) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TZI]CREUSR (AUTILIS) !Other
  DES AX3 Description
  DESLNG AXX Long description
  TADCOD TAD Daylight saving time
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TZI]UPDUSR (AUTILIS) !Other
  UTCOFFSET DCB*9.2 Time zone difference

## TITMLINK (TIK) - Linked WAS items
Notes: activity code TCAYT
Keys (first = PK; D = duplicates allowed): TIK0 ITMREF+ITMLNK
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TIK]CREUSR (AUTILIS) !Other
  ITMLNK ITM Linked item -> [ITM]ITM0 =[TIK]ITMLNK (ITMMASTER) !Block
  ITMREF ITM Parent product -> [ITM]ITM0 =[TIK]ITMREF (ITMMASTER) !Block
  LIG C*3 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TIK]UPDUSR (AUTILIS) !Other

## TITMMASTER (TIT) - Web items
Notes: activity code TCAYT
Keys (first = PK; D = duplicates allowed): TIT0 ITMREF
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TIT]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  IMG A*30(5) Images
  INTDES1 AX3 Web description
  ITMREF ITM Product -> [ITM]ITM0 =[TIT]ITMREF (ITMMASTER) !Block
  TITTEX TXC Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TIT]UPDUSR (AUTILIS) !Other
  VIG A*30 Gadget

## TMPCRPT (TCRPT) - Temporary print key table
Notes: differs in V10 P1 (diff: ATD_TMPCRPT.htm)
Keys (first = PK; D = duplicates allowed): TCRPT0 NUMREQ+USR+RPTCOD+VCRNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCRPT]CREUSR (AUTILIS) !Other
  NUMREQ L*8 Query no.
  PTATCOD A*50 AT code
  PTCPYADDLIG A*35(3) Address line
  PTCPYCTY A*30 City
  PTCPYNAM A*40 Company
  PTCPYPOSCOD POS Postal code
  PTCPYSAT SAT County
  PTMENTION01 A*100 Legal mention
  PTMENTION02 A*100 Legal mention
  PTMENTION03 A*100 Legal mention
  PTMENTION04 A*100 Legal mention
  PTMENTION05 A*100 Legal mention
  PTMENTION06 A*100 Legal mention
  PTMENTION07 A*60 Legal mention
  RPTCOD ARP Report code -> [ARP]ARP0 =[TCRPT]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCRPT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TCRPT]USR (AUTILIS) !Other
  VCRNUM VCR Document no.

## TMPSELCTR (TMC) - Contract selection
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## TMPSELMAT (TMT) - Employee selection
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## TRACKTPLD (TKTD) - Logistical tracking temp. detail
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TKTD0 TRKNUM+TRKLIN; TKTD1 TRKNUM+TRKSORT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TKTD]CREUSR (AUTILIS) !Other
  TRKCMT A*30 Comments
  TRKCOD ADI Step -> [ADI]CODE =108;TRKCOD (ATABDIV) !Block
  TRKDEPCOD ADI Dependency -> [ADI]CODE =108;TRKDEPCOD (ATABDIV) !Block
  TRKDEPLIN L*8 Line
  TRKENDDAT D End date
  TRKLIN L*8 Line
  TRKMDY M*4 Mandatory [menu 1: 1=No,2=Yes]
  TRKNUM VCR Tracking number
  TRKPLNDAT D Due date
  TRKSORT ISORT Sort order
  TRKUSR AUS User -> [AUS]CODUSR =[TKTD]TRKUSR (AUTILIS) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TKTD]UPDUSR (AUTILIS) !Other

## TRACKTPLH (TKTH) - Logistical tracking template
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TKTH0 TRKNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TKTH]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  SHIPFLG M*4 Shipment [menu 1: 1=No,2=Yes]
  TRKNUM VCR Tracking number
  TRNPFLG M*4 Transport [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TKTH]UPDUSR (AUTILIS) !Other

## TRADESHOW (OMT) - Professional trade shows
Keys (first = PK; D = duplicates allowed): OMT0 OMTNUM; OMT1 CMGNUM (D)
Fields:
  AUUID AUUID Single identifier
  BOOCST MD1 Booth cost
  BOOSUR L*8 Booth area
  BOOSURBAS A*2 Expression database
  CLO M*4 Closed [menu 1: 1=No,2=Yes]
  CLODAT D Closing date
  CMGNUM CMG Campaign code -> [CMG]CMG0 =[OMT]CMGNUM (CMARKETING) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[OMT]CUR (TABCUR) !Block
  DES DCO Description
  FCY FCY Site -> [FCY]FCY0 =[OMT]FCY (FACILITY) !Block
  NEWPPTOBJ L*8 Lead goals
  NUMFULOBJ CLC Chrono txt file
  OBJ CLX Objective
  OBJFLG C*2 Flag text file
  OMTEND D End
  OMTNUM VCR Code
  OMTSTR D Start
  OTHCST MD1 Other expenses
  TYPFULOBJ CLT Type text file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TRANNOTED (TND) - Transport note
Notes: activity code TRSNE
Keys (first = PK; D = duplicates allowed): TND0 TNHNUM+TNDLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TND]CREUSR (AUTILIS) !Other
  EXPNUM L*8 Export number
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[TND]ITMREF (ITMMASTER) !Block
  QTY QTY Delivered quantity
  TNDLIN L*8 Line
  TNHNUM VCR Transport note
  UOM UOM Unit -> [TUN]TUN0 =[TND]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TND]UPDUSR (AUTILIS) !Other

## TRANNOTEH (TNH) - Transport note
Notes: activity code TRSNE; differs in V10 P1 (diff: ATD_TRANNOTEH.htm)
Keys (first = PK; D = duplicates allowed): TNH0 TNHNUM
Fields:
  ARVDAT D Arrival date
  ATDTCOD A*200 AT code act:KPO
  AUUID AUUID Single identifier
  BPAADD ADR Delivery address
  BPCBPS M*15 Customer/Supplier [menu 242: 1=Customer,2=Supplier] act:KPO
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[TNH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPRNUM BPR BP -> [BPR]BPR0 =[TNH]BPRNUM (BPARTNER) !Block
  CFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  COPNBR C*1 No. pckg slip copies
  CPY CPY Company -> [CPY]CPY0 =[TNH]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TNH]CREUSR (AUTILIS) !Other
  DPEDAT D Departure date
  ETA HM Arrival time
  ETD HM Departure time
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[TNH]FCY (FACILITY) !Block
  GLBDOC M*4 Global document [menu 1: 1=No,2=Yes] act:KPO
  GLBDOCDAT D Global document date act:KPO
  GLBDOCNUM VCR Global document no. act:KPO
  GLBDOCTYP M*15 Global document type [menu 2047: 1=All types,2=Deliveries,3=Customer returns,4=Loan returns,5=Sub-cont material returns,6=Inter-site transfers,7=Sub-contract transfers,8=Sub-contract returns,9=Purchase returns,10=Transport note,11=Orders,12=Quotes,13=Proforma] act:KPO
  LICPLATE REGLIC Registration
  MANDOC DOC Manual document act:KPO
  SHIFRMADD ADR Receipt address
  SHIFRMADDLIG ADL(3) Address
  SHIFRMCRY CRY Country -> [TCY]TCY0 =[TNH]SHIFRMCRY (TABCOUNTRY) !Block
  SHIFRMCRYNAM NCY Country name
  SHIFRMCTY CTY City
  SHIFRMNAM NAM(2) Ship-from
  SHIFRMPOSCOD POS Postal code
  SHIFRMSAT SAT Country
  TMPTNHNUM VCR Doc no.
  TNHNUM VCR Transport note
  TNHTEX1 TXC Trans header text
  TNHTEX2 TXC Trans footer text
  TNHTYP TTN Type -> [TTN]TTN0 =TNHTYP;[V]GSUPCLE (TABTNHTYP) !Block
  TRLLICPLATE REGLIC Trailer license plate
  TRNDAT D Date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TNH]UPDUSR (AUTILIS) !Other

## TRCVCRDOC (TVD) - Log file of accounting entries
Keys (first = PK; D = duplicates allowed): TVD0 TYPNUM+NUM+TYPVCR+NUMVCR; TVD1 ACCNUM+TYPVCR+NUMVCR; TVD2 TYPVCR+NUMVCR
Fields:
  ACCNUM L*8 Internal number
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  NUM VCR Document number
  NUMVCR VCR Accounting document
  TYPNUM M*15 Document type [menu 2265: 1=Supplier invoice,2=Customer invoice]
  TYPVCR GTE Entry type -> [GTE]GTE0 =TYPVCR;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TXTBOL (TXB) - Text files
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BOLT0 LAN+TXTNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  LAN LAN Language -> [TLA]TLA0 =[TXB]LAN (TABLAN) !Block
  TXT1 AC0*4 Text
  TXTNUM C*4 Text number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TXTCTR (HRTXC) - Input document text
Notes: activity code FHRPA; not in V9.0 P12 (new table); not in V10 P1 (new table)
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## UNITOFTIME (UOT) - Unit of time
Keys (first = PK; D = duplicates allowed): UOT0 UOM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  TYPUOM MM*15 Valuation [menu 2986: 1=Units,2=Days,3=Hours,4=Minutes,5=Other]
  UOM UOM Unit -> [TUN]TUN0 =[UOT]UOM (TABUNIT) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## VATCLS (VCL) - Tax classification
Notes: activity code SAFT; differs in V10 P1 (diff: ATD_VATCLS.htm)
Keys (first = PK; D = duplicates allowed): VCL0 CPY+VAT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[VCL]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[VCL]CREUSR (AUTILIS) !Other
  PORTAXTYP M*15 Tax type [menu 2079: 1=Not applicable,2=VAT,3=Tax stamp,4=IEC,5=Other]
  RENEXN A*50 Exemption reason
  TAXCRYARA M*15 Tax country region [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  TAXLEV M*15 Tax level [menu 2275: 1=Reduced,2=Intermediate,3=Normal,4=Exemption,5=Other,6=Not applicable]
  TAXSTPCOD ADI Tax stamp -> [ADI]CODE =317;TAXSTPCOD (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Delete

## VATEXEREA (VER) - VAT exemption reasons
Notes: activity code KPO; differs in V9.0 P12 (diff: AT3_VATEXEREA.htm)
Keys (first = PK; D = duplicates allowed): VER0 CODE
Fields:
  AUUID AUUID Single identifier
  CODE A*3 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VER]CREUSR (AUTILIS) !Other
  DESCRIPTION A*65 Description
  NOTSUBVAT M*4 Not subject to VAT [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VER]UPDUSR (AUTILIS) !Other

## WAREHOUSE (WRH) - Warehouses
Notes: activity code WRH
Keys (first = PK; D = duplicates allowed): WRH0 WRH; WRH1 STOFCY+WRH
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  STOFCY FCY Stock site -> [FCY]FCY0 =[WRH]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =[WRH]WRH (WAREHOUSE) !Delete
  WRHNAM NAM Name
  WRHSHO SHO Short name

## WARFLYER (FLY) - Warranty vouchers
Keys (first = PK; D = duplicates allowed): FLY0 NUM; FLY1 FLYORI+FLYORIVCR+FLYORIVCRL (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Return address
  BPANAM NAM Site name
  BPANUM VCR Return address
  BPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CATRPTADI A*15 Report used
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  FCY FCY Site -> [FCY]FCY0 =[FLY]FCY (FACILITY) !Block
  FLYCAT ADI Category -> [ADI]CODE =450;FLYCAT (ATABDIV) !Block
  FLYORI M*15 Source [menu 3010: 1=Sales order,2=Sales delivery,3=Sales invoice]
  FLYORIVCR VCR Document no.
  FLYORIVCRL L*8 Journal line
  ITMREF ITM Product -> [ITM]ITM0 =[FLY]ITMREF (ITMMASTER) !Block
  LASPRNDAT D Last print
  LASPRNHOU HM Last print
  NUM VCR Sequence no.
  PRNDAT D(25) Printing
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRNHOU HM(25) Time of print
  RSLBPAADD ADR Reseller address
  RSLBPANUM VCR Reseller address
  RSLBPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  SERNUM SE1 Serial number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FLY]UPDUSR (AUTILIS) !Other
  WHOBPAADD ADR Wholesaler address
  WHOBPANUM VCR Wholesaler address
  WHOBPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]

## WARREQCPN (RCW) - Warranty request lines
Keys (first = PK; D = duplicates allowed): RCW0 RQWNUM+RQWNUMLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RCW]CREUSR (AUTILIS) !Other
  ITMREF ITM Product reference -> [ITM]ITM0 =[RCW]ITMREF (ITMMASTER) !Block
  MACBPCCUR CUR Purchase currency -> [TCU]TCU0 =[RCW]MACBPCCUR (TABCUR) !Block
  MACBPCDAT D Purchase date
  MACBPCPRI MD1 Purchase price
  MACSERNUM SE1 Serial number
  PLE CLX Location
  QTY L*8 Quantity
  RQWNUM VCR Warranty request
  RQWNUMLIN L*8 Line number
  RSL BPR Reseller -> [BPR]BPR0 =[RCW]RSL (BPARTNER) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RCW]UPDUSR (AUTILIS) !Other

## WARREQUEST (RQW) - Warranty requests
Keys (first = PK; D = duplicates allowed): RQW0 RQWNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Installation site
  BPC BPR Customer -> [BPR]BPR0 =[RQW]BPC (BPARTNER) !Block
  CCN AIN Contact (relationship) -> [AIN]AIN0 =[RQW]CCN (CONTACTCRM) !Block
  CFMDAT D Posting date
  CFMHOU HM Posting time
  CFMUSR A*5 Validating operator
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  FCY FCY Site -> [FCY]FCY0 =[RQW]FCY (FACILITY) !Block
  RQWCFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  RQWNUM VCR Sequence no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RQW]UPDUSR (AUTILIS) !Other

## WIPCOST (MWI) - WIP valuation
Keys (first = PK; D = duplicates allowed): MWI0 VCRTYP+VCRNUM+TXNTYP+WIPSEQ; MWI1 MFGTRKNUM+MFGTRKLIN+VCRTYP+VCRNUM+WIPSEQ; MWI2 VCRTYP+VCRNUM+VCRLIN+STU+WIPSEQ; MWI3 VCRTYP+VCRNUM+OPENUM+OPESPLNUM+STU+WIPSEQ; MWI4 VCRTYP+VCRNUM+VCRLIN+BOMSEQ+ITMREF+STU+WIPSEQ; MWI5 VCRTYP+VCRNUM+WIPSEQ+TXNTYP
Fields:
  AMOUNT DCB*11.4 Amount
  AUUID AUUID Single identifier
  BOMSEQ C*4 BOM sequence
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !RTZ act:ANA
  CPLOPETIM TIH Actual run time
  CPLSETTIM TIH Actual stp. time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Operator
  CSTELM DCB*11.4(17) Elements of cost
  CSTTYP M*15 Currency rate type [menu 314: 1=Unit,2=Fixed]
  DIE DIE Dimension type code -> [DIE]DIE0 =[MWI]DIE (GDIE) !RTZ act:ANA
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EMPNUM C*4 Employee ID
  ENTCOD GAU Automatic journal -> [GAU]GAU0 =[MWI]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  GLPDAT D Posted
  GLPSTA M*4 Posted [menu 1: 1=No,2=Yes]
  INVDTACST MD7 Invoicing element act:SPD
  ITMREF ITM Product -> [ITM]ITM0 =[MWI]ITMREF (ITMMASTER) !Block
  ITMTYP M*15 Revenue type [menu 2301: 1=Product,2=By-product]
  JOUNUM VCR Entry number
  JOUTYP GTE Journal type -> [GTE]GTE0 =JOUTYP;[V]GSUPCLE (GTYPACCENT) !Block
  LABCST MD7 Labor cost act:LAB
  MACCST MD7 Machine cost act:MAC
  MATCST MD7 Material cost act:MAT
  MATGRP M*15 Cost group [menu 325: 20 values, see local-menus.md]
  MATLEV0 MD7 Material cost level
  MATOVETYP M*15 General cost type [menu 331: 1=Stock receipt,2=Stock issue]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MWI]MFGFCY (FACILITY) !Block
  MFGTRKLIN L*8 Line
  MFGTRKNUM VCR Tracking number
  MTSNUM A*3 Transaction
  ONATYPCST M*15 Cost type [menu 319: 1=Material,2=Machine,3=Labor,4=Subcontracting,5=Overhead costs,6=Calculated cost]
  OPEGRP M*15 Cost group [menu 316: 1=Subtotal 1,2=Subtotal 2,3=Subtotal 3,4=Subtotal 4,5=Subtotal 5,6=Subtotal 6,7=Subtotal 7,8=Subtotal 8,9=Subtotal 9,10=Subtotal 10,11=Subtotal 11,12=Subtotal 12,13=Subtotal 13,14=Subtotal 14,15=Subtotal 15]
  OPENUM OPE Op.
  OPERAT DCB*6.4 Operation rate
  OPESPLNUM C*4 Operation split
  OVELABCST MD7 Labor OH act:SPD
  OVEMACCST MD7 Machine OH act:SPD
  OVEMATCST MD7 Mat. OH act:SPD
  OVENAT ONA Overhead cat. -> [ONA]ONA0 =[MWI]OVENAT (OVENAT) !Block
  OVENATAMT MS1 Account amount
  OVESCOCST MD7 Sub-con OH act:SPD
  PRINAT M*15 Cost source [menu 705: 1=Entered,2=Standard cost,3=Revised standard cost,4=Last cost,5=Historical AUC,6=FIFO cost,7=Lot average cost,8=Order cost,9=LIFO cost,10=Last purchase price]
  QTY QTY Quantity
  QTYACT QTY Active quantity
  REJQTY QTY Rejected quantity
  RGPMWI VCR Order no.
  SCOCST MD7 Subcontract cost act:SPD
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SETRAT DCB*6.4 Adjustment rate
  STU UOM Stock unit -> [TUN]TUN0 =[MWI]STU (TABUNIT) !Block
  TXNACT M*15 Transaction action [menu 2359: 1=New,2=Modified,3=Deleted]
  TXNDAT D Transaction date
  TXNTYP M*15 Transaction type [menu 2358: 20 values, see local-menus.md]
  UNTCST DCB*11.4 Unit cost
  UPDDAT D Chg date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VLTCCE A*20 Costing dimension
  WIPSEQ L*8 Sequence
  WST WST Work center

## WIPRESW (WRW) - WIPCOST summary for print
Keys (first = PK; D = duplicates allowed): WRW0 UID+VCRTYP+VCRNUM+VCRLIN+TYPCST+OVETYPCST+BRDCOD; WRW1 UID+MFGFCY+TYPCST+OVETYPCST+BRDCOD+VCRTYP+VCRNUM+VCRLIN
Fields:
  AUUID AUUID Single identifier
  BRDCOD C*4 Cost group
  CPLAMT DCB*11.4 Actual amount
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WRW]CREUSR (AUTILIS) !Other
  EXTAMT DCB*11.4 Expected amount
  MFGFCY FCY Production site -> [FCY]FCY0 =[WRW]MFGFCY (FACILITY) !Other
  OVETYPCST M*15 Type of overhead cost [menu 319: 1=Material,2=Machine,3=Labor,4=Subcontracting,5=Overhead costs,6=Calculated cost]
  TYPCST M*15 Cost type [menu 319: 1=Material,2=Machine,3=Labor,4=Subcontracting,5=Overhead costs,6=Calculated cost]
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WRW]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## WORKSTATIO (MWS) - Work centers
Notes: differs in V9.0 P12 (diff: AT3_WORKSTATIO.htm); differs in V10 P1 (diff: ATD_WORKSTATIO.htm)
Keys (first = PK; D = duplicates allowed): WST0 WST+WCRFCY; WST1 WCR+WSTTYP+WST (D); WST2 WSTDES (D); WST3 WCR+WST (D); WST4 WCRFCY+WCR+WST; WST5 WCRFCY+WST
Fields:
  AUUID AUUID Single identifier
  CLEPCTAUT DCB*3.3 Automatic closing %
  CONSTRAINT M*4 Constraint [menu 1: 1=No,2=Yes]
  CPLHOUTIM TIC Cumulative actual time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DSPLEV M*15 Display level [menu 2327: 1=Level 1,2=Level 2,3=Level 3]
  EFF DCB*3.3 % efficiency
  EXPNUM L*8 Export number
  EXTHOUTIM TIC Cumulative expected time
  GRPFLG M*4 Grouping [menu 1: 1=No,2=Yes]
  GRPHOR C*2 Grouping horizon
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[MWS]PCCCOD (PJMCOSTCTR) !Block act:PJM
  QLFLEV A*10 Qualification level
  RCCP M*4 RCCP [menu 1: 1=No,2=Yes]
  RPLAUTO M*4 Auto replacement [menu 1: 1=No,2=Yes]
  RUNBRKFLG M*4 Run during break [menu 1: 1=No,2=Yes]
  SBBFLG M*4 Distinct. of copies [menu 1: 1=No,2=Yes]
  SHR DCB*3.3 Shrinkage in %
  STOLOC LOC Storage location -> [STC]STC0 =WCRFCY;STOLOC (STOLOC) !Block
  TWD TWD Weekly structure -> [TWD]TWD0 =TWD (TABWEEDIA) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USE DCB*3.3 Use in %
  VLTCCE A*20 Costing dimension
  WCR WCR Work center group -> [TWC]TWC0 =[MWS]WCR (TABWRKCTR) !Block
  WCRFCY FCY Manufacturing site -> [FCY]FCY0 =[MWS]WCRFCY (FACILITY) !Block
  WST WST Work center
  WSTDES DES Work center title
  WSTDESAXX AX3 Work center title
  WSTNBR C*2 Number of resources
  WSTSHO SHO Short description
  WSTSHOAXX AX1 Short description
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]

