<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Help Desk module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## DOOBPCLNK (DBL) - Order-giver association
Keys (first = PK; D = duplicates allowed): DBL0 DOONUM+BPCNUM; DBL1 DOONUM (D); DBL2 BPCNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPCNAM NAM Customer name
  BPCNUM BPR Customer -> [BPR]BPR0 =[DBL]BPCNUM (BPARTNER) !Block
  BPCSHO SHO Short description
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DBL]CREUSR (AUTILIS) !Other
  DOONAM NAM Order-placer name
  DOONUM BPR Service caller -> [BPR]BPR0 =[DBL]DOONUM (BPARTNER) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DBL]UPDUSR (AUTILIS) !Other

## EXKWORD (EKW) - Existing keywords
Keys (first = PK; D = duplicates allowed): EKW0 KEYWRD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EKW]CREUSR (AUTILIS) !Other
  KEYWRD A*35 Key word
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EKW]UPDUSR (AUTILIS) !Other
  WRDCOU L*8 Sequence number

## FAMPBQUE (PBQ) - Corresponding queues
Keys (first = PK; D = duplicates allowed): PBQ0 GRPPBLNUM (D); PBQ1 QUENUM (D); PBQ2 GRPPBLNUM+QUENUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBQ]CREUSR (AUTILIS) !Other
  GRPPBLNUM VCR Code
  QUENAM DCO Queue name
  QUENUM QUE Queue code -> [QUE]QUE0 =[PBQ]QUENUM (QUEUE) !Block
  SRECOU C*4 Request sequence number
  STTFLG C*2 Statistic flag
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBQ]UPDUSR (AUTILIS) !Other

## FAMPBREP (PBR) - Qualified employees
Keys (first = PK; D = duplicates allowed): PBR0 GRPPBLNUM+REPNUM; PBR1 REPNUM (D); PBR2 GRPPBLNUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBR]CREUSR (AUTILIS) !Other
  GRPPBLNUM VCR Code
  REPNAM NAM Sales rep name
  REPNUM AUS Sales rep -> [AUS]CODUSR =[PBR]REPNUM (AUTILIS) !Block
  SRECOU C*4 Request sequence number
  STTFLG C*2 Statistic flag
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBR]UPDUSR (AUTILIS) !Other

## HDKTASK (HDT) - After-sales serv. consumption
Keys (first = PK; D = duplicates allowed): HDT0 HDTNUM; HDT1 SRENUM+TPL (D); HDT2 ITNNUM+TPL (D)
Fields:
  AUUID AUUID Single identifier
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HDT]CREUSR (AUTILIS) !Other
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[HDT]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[HDT]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[HDT]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  HDTAMT MD1 Amount
  HDTAMTINV MD1 Amount invoiced
  HDTAUS A*15 Provider
  HDTAUSTYP M*15 Provider type [menu 2987: 1=Internal contact,2=External service provider]
  HDTAVA QTY Available
  HDTAVAUOM UOM Disp. unit -> [TUN]TUN0 =[HDT]HDTAVAUOM (TABUNIT) !Block
  HDTCPN ITM Component -> [ITM]ITM0 =[HDT]HDTCPN (ITMMASTER) !Block
  HDTCUR CUR Currency -> [TCU]TCU0 =[HDT]HDTCUR (TABCUR) !Block
  HDTDONDAT D Date executed
  HDTDONHOU L*8 Carried out the
  HDTINV M*4 Billable [menu 1: 1=No,2=Yes]
  HDTINVMOD M*15 Invoice method [menu 2989: 1=According to coverage,2=Always invoiced,3=Never invoiced]
  HDTISSISS QTY Quantity issued
  HDTISSQTY QTY Quantity to issue
  HDTITM ITM Product consumed -> [ITM]ITM0 =[HDT]HDTITM (ITMMASTER) !Block
  HDTMACSET ITM Parent product -> [ITM]ITM0 =[HDT]HDTMACSET (ITMMASTER) !Block
  HDTMACSRE MAC Base concerned -> [MAC]MAC0 =[HDT]HDTMACSRE (MACHINES) !Block
  HDTNUM VCR Sequence no.
  HDTPLNDAT D Planned the
  HDTQTY QTY Quantity/Duration
  HDTSALTEX TXC Sales text code
  HDTSTOFCY FCY Storage site -> [FCY]FCY0 =[HDT]HDTSTOFCY (FACILITY) !Block
  HDTSTOISS M*4 Stock issue [menu 1: 1=No,2=Yes]
  HDTSTUQTY QTY Quantity in STK
  HDTTEX CLX Text
  HDTTYP MM*15 Item/labor [menu 2984: 1=Other,2=Part,3=Labor,4=Expenses,5=Service contract]
  HDTTYPRUU M*15 Execution type [menu 2998: 1=Global,2=By base]
  HDTUOM UOM Unit -> [TUN]TUN0 =[HDT]HDTUOM (TABUNIT) !Block
  INVPITFLG C*2 Invoice flag/point
  ITNNUM VCR Service response chrono
  MANAMTFLG M*4 Manual amount modif [menu 1: 1=No,2=Yes]
  PRIREN SPR Price reason -> [SPR]SPR0 =[HDT]PRIREN (SPREASON) !Block
  SAUSTUCOE COE Conversion factor
  SPGTIMHOU L*8 Time spent
  SPGTIMMNT C*2 Time spent
  SRENUM VCR Serv. req. No.
  TPL M*4 Template [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HDT]UPDUSR (AUTILIS) !Other
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## HDKTASKINV (HDI) - Consumptions to be invoiced
Keys (first = PK; D = duplicates allowed): HDI0 SRENUM+HDTORD (D)
Fields:
  AUUID AUUID Single identifier
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HDI]CREUSR (AUTILIS) !Other
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[HDI]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[HDI]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[HDI]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  HDTAMTINV MD1 Amount
  HDTCUR CUR Currency -> [TCU]TCU0 =[HDI]HDTCUR (TABCUR) !Block
  HDTITM ITM Product consumed -> [ITM]ITM0 =[HDI]HDTITM (ITMMASTER) !Block
  HDTORD L*8 Display order
  HDTQTY QTY Quantity/Duration
  HDTSALTEX TXC Sales text code
  HDTSTUQTY QTY Quantity in STK
  HDTTEX A*200 Text
  HDTUOM UOM Unit -> [TUN]TUN0 =[HDI]HDTUOM (TABUNIT) !Block
  PRIREN SPR Price reason -> [SPR]SPR0 =[HDI]PRIREN (SPREASON) !Block
  SAUSTUCOE COE Conversion factor
  SRENUM SRE Serv. req. No. -> [SRE]SRE0 =[HDI]SRENUM (SERREQUEST) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HDI]UPDUSR (AUTILIS) !Other
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## HDKTRS (HTR) - HDK entry transaction
Notes: differs in V9.0 P12 (diff: AT3_HDKTRS.htm); differs in V10 P1 (diff: ATD_HDKTRS.htm)
Keys (first = PK; D = duplicates allowed): HTR0 HTRTYP+HTRNUM; HTR1 HTRNUM+HTRTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[HTR]ACSCOD (ACCCOD) !Block
  AMTINVCOD M*15 Invoicable amount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AUSTYPCOD M*15 Provider type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AUUID AUUID Single identifier
  BLOCINVI A*15(15) Hidden block
  BPCCURCOD M*15 Purchase currency [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCDATCOD M*15 Purchase date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCGRUCOD M*15 Group customer [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCINVCOD M*15 Bill-to customer [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCPRICOD M*15 Purchase price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCPYRCOD M*15 Pay-by [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BRACOD M*15 Brand [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCECOD M*15 Analytical dimensions [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CHGTYPCOD M*15 Rate type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CLELIS ANX(8) Index
  COLFIXNAM A*25(10) Fixed column grid
  COLFIXVAL C*1(10) Fix.col. grid value
  CONSPTCOD M*15 Support contract [menu 35: 1=Entered,2=Displayed,3=Hidden]
  COULIS M*4(8) Numbering active [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CURCOD M*15 Sales currency [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEPCOD M*15 Settlement discount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DERLU M*4 Last read [menu 1: 1=No,2=Yes]
  DESAXX AX3 Description
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[HTR]DOCNAM (AREPORT) !Block
  DONDATCOD M*15 Date executed [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DONHOUCOD M*15 Carried out the [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DOOCOD M*15 Service caller [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DTCKILCOD M*15 Distance [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[HTR]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  FCYITNFLG M*4 Address tab [menu 1: 1=No,2=Yes]
  FIRLIS M*4 In first position [menu 1: 1=No,2=Yes]
  FLTLIS A*215(8) Filter
  FLYWARFLG M*4 Warranty requests [menu 1: 1=No,2=Yes]
  GFY AGF Group -> [AGF]AGF0 =[HTR]GFY (AGRPFCY) !Block
  GRALEVCOD M*15 Severity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDKITNCAT M*4 Category [menu 1: 1=No,2=Yes]
  HDKITNDAT M*4 Period [menu 1: 1=No,2=Yes]
  HDKITNDSY M*4(15) Display [menu 1: 1=No,2=Yes]
  HDKITNPOS L*8(15) Position
  HDKITNSCO M*4 Sub-contracted operations [menu 1: 1=No,2=Yes]
  HDKITNUSR M*4 Employee [menu 1: 1=No,2=Yes]
  HDKSREDSY M*4(20) Display [menu 1: 1=No,2=Yes]
  HDKSREGRA M*4 Severity level [menu 1: 1=No,2=Yes]
  HDKSREPOS L*8(20) Position
  HDKSREQUE M*4 Queue [menu 1: 1=No,2=Yes]
  HDKSRESAT M*4 Status [menu 1: 1=No,2=Yes]
  HDKSREUSR M*4 Employee [menu 1: 1=No,2=Yes]
  HDTAMTCOD M*15 Amount consumed [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTAUSCOD M*15 Provider [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTCPNCOD M*15 Component [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTINVCOD M*15 Billable [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTMACCOD M*15 Base [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTNUMCOD M*15 Conso chrono [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTPITCOD M*15 Points debited [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTTEXCOD M*15 Text [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTTIMCOD M*15 Real duration [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HDTTOTFLG M*4 Totals [menu 1: 1=No,2=Yes]
  HDTTYPCOD M*15 Consumption type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HSTOFCYCOD M*15 Site stock (line) [menu 35: 1=Entered,2=Displayed,3=Hidden]
  HTRDES DES Description
  HTRNUM TRS Transaction
  HTRTYP M*15 Transaction type [menu 3020: 1=Base,2=Service request,3=Service response,4=Hotline planning calendar]
  HTRTYPCAR A*2 Alpha no.
  IFFADDCOD M*15 Address indications [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVDTACOD M*15 Invoice elements [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ISSISSCOD M*15 Quantity issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ISSQTYCOD M*15 Quantity to issue [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITNDATCOD M*15 Installation date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITNNUMCOD M*15 Action Chrono [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITNTIMFLG M*4 Time management [menu 1: 1=No,2=Yes]
  ITSDATCOD M*15 In service date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MACCONFLG M*4 Direct coverage [menu 1: 1=No,2=Yes]
  MAIFLG M*4 Installations [menu 1: 1=No,2=Yes]
  NPRFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  NPRNAM ARP Document -> [ARP]ARP0 =[HTR]NPRNAM (AREPORT) !Block
  NUMBPCCOD M*15 Customer request [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OBJCOD M*15 Additional info [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OBJLIS AOB(8) Object -> [AOB]ABREV =[HTR]OBJLIS (AOBJET) !Block
  ONGINVISI A*15(10) Hidden tab
  ONGLETACT AMK Active tab -> [AMK]CODMSK =[HTR]ONGLETACT (AMSK) !Block
  ORDLIS M*10(8) Sign [menu 90: 1=Ascending,2=Descending]
  PJTCOD M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PLNDATCOD M*15 Planned the [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRITYPCOD M*15 Price type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PTECOD M*15 Payment term [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PURDATCOD M*15 Sales date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REPCOD M*15 Sales reps [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RESDATCOD M*15 Resolution date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RESHOUCOD M*15 Resolution time [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RESRENCOD M*15 Reason [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SALPRICOD M*15 Sale price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SATCOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SBBTOTFLG M*4 Subtotals [menu 1: 1=No,2=Yes]
  SCOAMTCOD M*15 Subcontracted amount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SCOCOD M*15 Subcontracted [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SRETSDCOD M*15 Stat groups [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SSTENTCOD M*15 Entity/Use [menu 35: 1=Entered,2=Displayed,3=Hidden] act:LTA
  STOFCYCOD M*15 Site stock (header) [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOISSCOD M*15 Stock issue [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TIMSPGCOD M*15 Time spent [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TITNADDFLG M*4 Addresses [menu 1: 1=No,2=Yes]
  TITNHDTFLG M*4 Consumptions [menu 1: 1=No,2=Yes]
  TITNRSEFLG M*4 Resources [menu 1: 1=No,2=Yes]
  TRITIMCOD M*15 Commute time [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TSRECOVFLG M*4 Coverages [menu 1: 1=No,2=Yes]
  TSRECPNFLG M*4 Components [menu 1: 1=No,2=Yes]
  TSREESCFLG M*4 Escalations [menu 1: 1=No,2=Yes]
  TSREHDTFLG M*4 Consumptions [menu 1: 1=No,2=Yes]
  TSREHORFLG M*4 Timestamps [menu 1: 1=No,2=Yes]
  TSREINVFLG M*4 Invoicing [menu 1: 1=No,2=Yes]
  TSREMACFLG M*4 Base [menu 1: 1=No,2=Yes]
  TSREPBLFLG M*4 Skills [menu 1: 1=No,2=Yes]
  TSREPITFLG M*4 Points management [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPRCOD M*15 Tax rule [menu 35: 1=Entered,2=Displayed,3=Hidden]

## HDKTRSVAL (HTV) - HDK value entry transaction
Keys (first = PK; D = duplicates allowed): HTV0 HTRTYP+HTRNUM; HTV1 HTRNUM+HTRTYP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FIENAM A*24(90) Fields
  FIEVAL A*10(90) Values
  HTRNUM TRS Transaction
  HTRTYP M*15 Transaction type [menu 3020: 1=Base,2=Service request,3=Service response,4=Hotline planning calendar]
  ININAM A*24(20) Field name to assign
  INIVAL A*10(20) Value to assign
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SBGEO (SBG) - Consulting fields of service suppliers
Keys (first = PK; D = duplicates allowed): SBG0 BPRNUM (D); SBG1 CRY+ARACOD (D); SBG2 BPRNUM+CRY+ARACOD
Fields:
  ARACOD A*10 Geographical area
  ARANAM A*40 Field title
  AUUID AUUID Single identifier
  BPRNUM BPR Service supplier code -> [BPR]BPR0 =[SBG]BPRNUM (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SBG]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[SBG]CRY (TABCOUNTRY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SBG]UPDUSR (AUTILIS) !Other

## SBPBL (SBP) - Service suppliers' skills
Keys (first = PK; D = duplicates allowed): SBP0 BPRNUM (D); SBP1 PBL (D); SBP2 BPRNUM+PBL
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR Service supplier code -> [BPR]BPR0 =[SBP]BPRNUM (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SBP]CREUSR (AUTILIS) !Other
  PBL PBL Skill groups -> [PBL]PBL0 =[SBP]PBL (FAMPB) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SBP]UPDUSR (AUTILIS) !Other

## SOLRESULT (SOR) - Solutions found
Keys (first = PK; D = duplicates allowed): SOR0 SOLNUM (D); SOR1 NUM (D); SOR2 SSS (D); SOR3 SOLNUM+SSS+TYP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATSOL D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  MORSOL A*2 Associated solutions
  NUM L*8 No. in the list
  SOLNUM VCR Solution code
  SSS A*30 Session
  TTR A*80 Solution title
  TYP A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SOR]UPDUSR (AUTILIS) !Other

## SOLUTION (SOL) - Solutions
Keys (first = PK; D = duplicates allowed): SOL0 NUM; SOL1 SRENUM (D)
Fields:
  AUUID AUUID Single identifier
  CAT ADI Category -> [ADI]CODE =409;CAT (ATABDIV) !Block
  CODSOL SOL(25) Solution code -> [SOL]SOL0 =[SOL]CODSOL (SOLUTION) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHOU HM Creation time
  CREUSR A*5 Creation user
  KEYWRD A*35(25) Key word
  NUM VCR Solution chrono
  NUMPBLDES CLC Description chrono
  NUMSOLDES CLC Solution chrono
  PBLDES CLX Problem description
  PBLDESFLG C*2 Overview written
  PBLGRP PBL Skills group -> [PBL]PBL0 =[SOL]PBLGRP (FAMPB) !Block
  SOLDES CLX Solution overview
  SOLDESFLG C*2 Overview written
  SRENUM SRE Serv. req. No. -> [SRE]SRE0 =[SOL]SRENUM (SERREQUEST) !RTZ
  TTR A*80 Title
  TYPPBLDES CLT Description type
  TYPSOLDES CLT Solution type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDHOU HM Modification time
  UPDUSR A*5 Change user

## SRESAT (SRS) - Request status history
Keys (first = PK; D = duplicates allowed): SRS0 SRENUM (D)
Fields:
  ASS M*15 Assignment [menu 975: 1=Dispatching,2=Employee,3=Queue,4=Commercial,5=Closed]
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SRS]CREUSR (AUTILIS) !Other
  DET A*15 Assignment detail
  SAT A*30 Status
  SATDAT D Date
  SATHOU HM Time
  SRENUM SRE Service request -> [SRE]SRE0 =[SRS]SRENUM (SERREQUEST) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SRS]UPDUSR (AUTILIS) !Other

