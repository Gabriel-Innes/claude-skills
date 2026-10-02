<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Fixed Assets module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BRDKEY (BRD) - Distribution key
Keys (first = PK; D = duplicates allowed): BRD0 CPY+BRDREF+DSPKEY; BRD1 CPY+BRDREF
Fields:
  AUUID AUUID Single identifier
  BRDPRC RAT(30) Distribution %
  BRDREF VC9 Reference
  CHAMP1 M*15 Field 1 [menu 3129: 1=,2=Description 1,3=Description 2,4=Group,5=Accounting code,6=Free field 1,7=Free field 2,8=Free field 3,9=Free field 4,10=Free field 5,11=Free field 6,12=Free field 7,13=Free field 8,14=Free field 9,15=Free field 10]
  CHAMP2 M*15 Field 2 [menu 3129: 1=,2=Description 1,3=Description 2,4=Group,5=Accounting code,6=Free field 1,7=Free field 2,8=Free field 3,9=Free field 4,10=Free field 5,11=Free field 6,12=Free field 7,13=Free field 8,14=Free field 9,15=Free field 10]
  CHAMP3 M*15 Field 3 [menu 3129: 1=,2=Description 1,3=Description 2,4=Group,5=Accounting code,6=Free field 1,7=Free field 2,8=Free field 3,9=Free field 4,10=Free field 5,11=Free field 6,12=Free field 7,13=Free field 8,14=Free field 9,15=Free field 10]
  CPY CPY Company -> [CPY]CPY0 =[BRD]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DCO Description 1
  DSPKEY M*4 Distribution key [menu 3122: 1=Group,2=Accounting code,3=CoA account,4=IFRS account]
  NBVAL C*4 Number of values
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAL1 A*30(30) Value 1
  VAL2 A*30(30) Value 2
  VAL3 A*30(30) Value 3
  VALKEY A*10(30) Key value

## CALCDBG (CDG) - Calculation
Keys (first = PK; D = duplicates allowed): CDG0 BRKNORD
Fields:
  AUUID AUUID Single identifier
  BRKNORD C*4 Order information
  BRKPTDES A*200 Comment
  BRKPTFLG M*4 Active [menu 1: 1=No,2=Yes]
  BRKPTNAM A*20
  BRKPTPLN M*25 Plan [menu 3101: 16 values, see local-menus.md]
  BRKPTTRT A*20 Processing
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CDG]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CDG]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[CDG]USR (AUTILIS) !Delete

## CASHING (CAS) - Collections
Notes: activity code GRT
Keys (first = PK; D = duplicates allowed): CAS0 GRAREF+CASHDAT; CAS1 CPY+GRAREF+CASHDAT; CAS2 CPY+FCY+GRAREF+CASHDAT
Fields:
  AUUID AUUID Single identifier
  CASHAMT MD1 Collected amount
  CASHDAT D4 Collection date
  COMMENT A*80 Comment
  CPY CPY Company -> [CPY]CPY0 =[CAS]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[CAS]CUR (TABCUR) !Block
  EVTFLG M*1 Events [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[CAS]FCY (FACILITY) !Block
  GRAREF GRT Subsidy reference
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CCNCOE (COE) - Update coefficients
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): COE0 CPY+CCNACTCOD
Fields:
  AUUID AUUID Single identifier
  CCNACTCOD VC9 Update code
  CCNACTCOE RA1 Update coef.
  CPY CPY Company -> [CPY]CPY0 =[COE]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES1 DCO Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## CCNRPR (RPR) - Provisions for renewal
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): RPR0 AASREF+FIYENDDAT+PERENDDAT; RPR7 FLGDEV+CPY+FIYENDDAT+PERENDDAT (D)
Fields:
  AASREF VC9 Asset
  ACGRPRDEV MD1 Acc. prov. to be posted
  AUUID AUUID Single identifier
  CCNREF VC9 Reference
  CPY CPY Company -> [CPY]CPY0 =[RPR]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RPR]CREUSR (AUTILIS) !Other
  ENDRNWVAL MD1 Replacement amt end
  ETRPNT C*1 Entry point
  EXEACGRPR MD1 Acc. provision FY
  EXEFISRPR MD1 Fiscal provision FY
  EXERVERPR MD1 Tax prov. rev. FY
  EXESUPCAD MD1 Add. FY amort.
  E_1ACGRPR MD1 FY-1 tot. acc. prov.
  E_1FISRPR MD1 FY-1 total fisc. prov.
  E_1RVERPR MD1 FY-1 tot. tax rev.
  E_1SUPCAD MD1 FY-1 tot. add. tax cad.
  FCY FCY Financial site -> [FCY]FCY0 =[RPR]FCY (FACILITY) !Delete
  FISRPRDEV MD1 Fisc. prov. to post
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGDEV M*4 To post [menu 1: 1=No,2=Yes]
  FLGPST M*4 Posted [menu 1: 1=No,2=Yes]
  PERACGRPR MD1 Acc. provision per.
  PERENDDAT D4 Period end date
  PERFISRPR MD1 Fisc. provision per.
  PERRVERPR MD1 Fisc. prov. w. back per.
  PERSTRDAT D4 Period start date
  PERSUPCAD MD1 Add. period amort.
  PSTACGRPR MD1 Posted prov.
  PSTFISRPR MD1 F. prov. posted
  P_1ACGRPR MD1 P-1 tot. acc. prov.
  P_1FISRPR MD1 P-1 total tax prov.
  P_1RVERPR MD1 P-1 total tax reversal
  P_1SUPCAD MD1 P-1 total add. tax cad.
  RNWVALCOE COE New value coeff
  RNWVALFLG M*4 Replacement amt end [menu 1: 1=No,2=Yes]
  STRRNWVAL MD1 Replacement amt start
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RPR]UPDUSR (AUTILIS) !Other

## CDFCOD (CDC) - Recoding : codes
Keys (first = PK; D = duplicates allowed): CDC REFCDF+VALOLDCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  REFCDF A*10 Reference
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VALNEWCOD A*20 New code
  VALNEWDES A*30 New label
  VALOLDCOD A*20 Old code

## CDFCPY (CDS) - Recoding : select company
Keys (first = PK; D = duplicates allowed): CDS REFCDF+CPY
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[CDS]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  FLGCPY M*4 Company ticked [menu 1: 1=No,2=Yes]
  REFCDF A*10 Reference
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## CDFFCY (CDY) - Recoding : select site
Keys (first = PK; D = duplicates allowed): CDY REFCDF+FCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  FCY FCY Site -> [FCY]FCY0 =[CDY]FCY (FACILITY) !Delete
  FCYCPY CPY Comp for site -> [CPY]CPY0 =[CDY]FCYCPY (COMPANY) !Delete
  FLGFCY M*4 Site ticked [menu 1: 1=No,2=Yes]
  REFCDF A*10 Reference
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## CDFPAR (CDP) - Recoding : parameter
Keys (first = PK; D = duplicates allowed): CDF0 REFCDF; CDF1 TABNAM+REFCDF; CDF2 TABNAM+REFCDF+CPYSRC+CPYDES
Fields:
  ANDOR2 MM*15 AndOr [menu 56: 1=And,2=Or]
  ANDOR3 MM*15 AndOr [menu 56: 1=And,2=Or]
  ANDOR4 MM*15 AndOr [menu 56: 1=And,2=Or]
  ANDOR5 MM*15 AndOr [menu 56: 1=And,2=Or]
  AUUID AUUID Single identifier
  CCEDIE A*3 Analytical dimension type
  CPYDES CPY Target company -> [CPY]CPY0 =[CDP]CPYDES (COMPANY) !Delete
  CPYSRC CPY Source company -> [CPY]CPY0 =[CDP]CPYSRC (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DATENDACT D4 Validity end date
  FLD1 A*12 Heading
  FLD2 A*12 Heading
  FLD3 A*12 Heading
  FLD4 A*12 Heading
  FLD5 A*12 Heading
  FLGSIM M*4 Simulation index [menu 1: 1=No,2=Yes]
  FLGTRCEDT M*4 Log print ind [menu 1: 1=No,2=Yes]
  FLGUPDASS M*4 Assoc update index [menu 1: 1=No,2=Yes]
  OBCLDR M*15 Master object [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  OBCPCDFAS M*4 FAS proc object [menu 1: 1=No,2=Yes]
  OBCPCDGRT M*4 GRT proc object [menu 1: 1=No,2=Yes]
  OBCPCDIVY M*4 IVY proc object [menu 1: 1=No,2=Yes]
  OBCPCDLEA M*4 LEA proc object [menu 1: 1=No,2=Yes]
  OBCPCDLOF M*4 LOF proc object [menu 1: 1=No,2=Yes]
  OBCPCDPHY M*4 PHY processed item [menu 1: 1=No,2=Yes]
  OPE1 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE2 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE3 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE4 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE5 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  PRODAT D4 Process date
  PROSTA MM*15 Process status [menu 3236: 1=To be processed,2=To be processed (intra-group sale),3=Processed,4=Processed (intra-group sale)]
  PROUSR A*5 User
  REFCDF A*10 Reference
  REFDES A*30 Description
  REFTRFCMP A*10 Intra-grp trans ref
  REQUETE A*200 Query
  STAOLDCOD MM*15 Prev code status [menu 3237: 1=Saved,2=Inactive,3=Deleted]
  TABNAM A*4 Table name
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VAL1 A*30 Value
  VAL2 A*30 Value
  VAL3 A*30 Value
  VAL4 A*30 Value
  VAL5 A*30 Value

## CIGDEF (CIG) - IGS definition
Notes: activity code CIG
Keys (first = PK; D = duplicates allowed): CIG0 CIGCOD
Fields:
  AUUID AUUID Single identifier
  CIGCOD CIG Reference -> [CIG]CIG0 =[CIG]CIGCOD (CIGDEF) !Other
  CIGFIS M*25 Fiscal rule [menu 3163: 1=Favorable rule,2=Ordinary rule,3=Others]
  CIGSTA M*15 Operation status [menu 3131: 1=In preparation,2=Processed issues,3=Processed receipts]
  CIGTYP MM*25 Type of operation [menu 3172: 1=Partial transfer of assets,2=Merger,3=Split,4=Intra-group sales]
  CPYDES CPY(10) Target company -> [CPY]CPY0 =[CIG]CPYDES (COMPANY) !Delete
  CPYSRC CPY(10) Source company -> [CPY]CPY0 =[CIG]CPYSRC (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DCO Description
  EFFDAT D4 Effective date
  NBCPY C*4 Source comp number
  OPEDAT D4 Operation date
  PROUSR A*5 User
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CIGFXDSOR (CIB) - IGS adjustment : issued assets
Notes: activity code CIG
Keys (first = PK; D = duplicates allowed): CIB0 CIGCOD+CPYSRC+REFSELCIG+AASREF; CIB1 CIGCOD (D); CIB2 CIGCOD+CPYSRC+REFSELCIG (D); CIB3 CIGCOD+CPYSRC+AASREF (D); CIB4 AASREF (D)
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  AASREFNEW VC9 Target reference
  AUUID AUUID Single identifier
  CIGCOD CIG IGS operation code -> [CIG]CIG0 =[CIB]CIGCOD (CIGDEF) !Block
  CMP AAS Main -> [FAS]FAS0 =[CIB]CMP (FXDASSETS) !Other
  CPYDES CPY Target company -> [CPY]CPY0 =[CIB]CPYDES (COMPANY) !Delete
  CPYSRC CPY Source company -> [CPY]CPY0 =[CIB]CPYSRC (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CIB]CREUSR (AUTILIS) !Other
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  EPR MD1 Gross value
  FCYSRC FCY Financial site -> [FCY]FCY0 =[CIB]FCYSRC (FACILITY) !RTZ
  FLGAASCCL M*4 Cancelled asset [menu 1: 1=No,2=Yes]
  FLGCMP M*4 Link to main asset [menu 1: 1=No,2=Yes]
  GAL MD1 +/- Value
  ISSAMT MD1 Disposal amount
  ISSAMTUPD MD1 Disposal update amount
  ISSDAT D4 Issue date
  ISSSAT M*15 IGS asset disposal status [menu 3173: 1=Asset to be issued,2=Issued asset to be modified,3=Asset to be cancelled]
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  IVCVATRAT RAT Invd VAT rate
  IVCVATRATI RAT Invd VAT rate
  NVA MD1 Net value
  PLN M*25 Plan [menu 3101: 16 values, see local-menus.md]
  PRORATA RA1 Prorata
  PURDAT D4 Purchase date
  REFSELCIG A*4 IGS selection ref
  SET A*20 Group No
  THESLI DUR Theo holding duratn
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CIB]UPDUSR (AUTILIS) !Other
  VATRSD DUR Residual duration

## CIGREX (CIR) - IGS parametern
Notes: activity code CIG
Keys (first = PK; D = duplicates allowed): CIR0 CIGCOD+CPYSRC+CPYDES; CIR1 CIGCOD+CPYSRC (D); CIR2 CIGCOD (D)
Fields:
  AUUID AUUID Single identifier
  BASGAL M*15 Base +/- value [menu 3276: 1=Contribution value,2=Renewal to previous basis]
  CIGCOD CIG IGS operation code -> [CIG]CIG0 =[CIR]CIGCOD (CIGDEF) !Other
  CPYDES CPY Target company -> [CPY]CPY0 =[CIR]CPYDES (COMPANY) !Delete
  CPYSRC CPY Source company -> [CPY]CPY0 =[CIR]CPYSRC (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR(10) Currency -> [TCU]TCU0 =[CIR]CUR (TABCUR) !Block
  DPRDPM DPM(16) Depreciation method
  DPRDUR M(16) Depre. durn [menu 3138: 1=Remaining duration,2=Previous renewal duration]
  DPRDURDEF DUR(16) Default depre duratn
  DPRPLN M*25(16) Depreciation plan [menu 3101: 16 values, see local-menus.md]
  GACACNREA M*4(10) FA in service [menu 1: 1=No,2=Yes]
  GACACNWIP M*4(10) FA in progress [menu 1: 1=No,2=Yes]
  GALDAT D4 Reintegration date
  GALDPM DPM Deprec meth +/-value
  GALDUR DUR Depr durat +/-value
  GALPLNDES M*25 Plan +/-value tgt co [menu 3101: 16 values, see local-menus.md]
  GALPLNSRC M*25 Plan +/-value sce co [menu 3101: 16 values, see local-menus.md]
  GALPRO M*4 Process +/- value [menu 1: 1=No,2=Yes]
  ISSVATRAT RAT Disposal VAT rate
  NBRPLN C*4 Number sched/charts
  NBRSEL C*4 No.selections
  OUTDATEFF M*4(10) Issue after bill date [menu 1: 1=No,2=Yes]
  OWNTYPLEA M*4(10) Leasing holding [menu 1: 1=No,2=Yes]
  PLNTPL M*25(16) Templ plan [menu 3101: 16 values, see local-menus.md]
  PURDATEFF M*4(10) Purch after bill date [menu 1: 1=No,2=Yes]
  PURITSDAT M*15 Purchase/ps date [menu 3133: 1=Sale effective date,2=Renewal date source company]
  PURNAT M*15 Purchase nature [menu 3134: 1=Second-hand,2=Renewal of previous status]
  REFSELCIG A*4(10) IGS selection ref
  RULPRO M*30(16) Management rule [menu 3276: 1=Contribution value,2=Renewal to previous basis]
  RULTPFDAT D Rule date TP/TF
  SALPRI MD1(10) Sale price
  SALPRIDEF MD1(10) Def sale price
  SALPRIMOD M*30(10) Sale price calculn [menu 3278: 1=NV at effective date for spec. plan,2=GV of specified plan,3=Distrib. Envelope according to spec plan NV,4=Distrib. Envelope according to spec plan GV,5=Sale price identical to that entered by user]
  SALPRIPLN M*25(10) Specified plan [menu 3101: 16 values, see local-menus.md]
  TAXBASTPF M*30 TP/TF basis [menu 3132: 1=Renewal,2=Max (Contribution value / 80% srf tax basis),3=80% source tax basis,4=Contribution value,5=50% source tax basis,6=Contribution value]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VATTRFFLG M*4 Transferred VAT rule [menu 1: 1=No,2=Yes]

## CIGREXSEL (CIS) - IGS asset selection
Notes: activity code CIG
Keys (first = PK; D = duplicates allowed): CIS0 REFSELCIG; CIS1 REFSELCIG+CPYSRC
Fields:
  ANDOR2 MM*15(4) AndOr [menu 56: 1=And,2=Or]
  ANDOR3 MM*15 AndOr [menu 56: 1=And,2=Or]
  ANDOR4 MM*15 AndOr [menu 56: 1=And,2=Or]
  ANDOR5 MM*15 AndOr [menu 56: 1=And,2=Or]
  AUUID AUUID Single identifier
  CPYSRC CPY Source company -> [CPY]CPY0 =[CIS]CPYSRC (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FLD1 AVA(30) Heading
  FLD2 A*12 Heading
  FLD3 A*12 Heading
  FLD4 A*12 Heading
  FLD5 A*12 Heading
  OPE1 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE2 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE3 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE4 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  OPE5 MM*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  REFSELCIG A*4 IGS selection ref
  REQUETE A*200 Query
  SELCIGDES A*60 Description
  TBL1 A*20 Table
  TBL2 A*20 Table
  TBL3 A*20 Table
  TBL4 A*20 Table
  TBL5 A*20 Table
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAL1 A*30 Value
  VAL2 A*30 Value
  VAL3 A*30 Value
  VAL4 A*30 Value
  VAL5 A*30 Value

## CONCESSION (CCN) - Concession
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): CCN0 CCNREF; CCN1 CPY+CCNREF; CCN2 CPY+FCY+CCNREF
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =7;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCNDES1 DCO Description 1
  CCNDES2 DCO Description 2
  CCNREF VC9 Reference
  CCNSTA M*33 Status [menu 3284: 1=Under preparation,2=Active,3=Ended]
  CCNUSR BPR Grantor -> [BPR]BPR0 =[CCN]CCNUSR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[CCN]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR A*5 Creation user
  DFTCCNFLG M*4 Default [menu 1: 1=No,2=Yes]
  DIE DIE Dimension type code -> [DIE]DIE0 =[CCN]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENDCCNDAT D4 End of concession
  FCY FCY Financial site -> [FCY]FCY0 =[CCN]FCY (FACILITY) !Block
  REAENDCCN D4 Effective end
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  STRCCNDAT D4 Concession start
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## CONTEXT (CNX) - Contexts
Keys (first = PK; D = duplicates allowed): CNX0 CPY+CNX
Fields:
  AUUID AUUID Single identifier
  CCNCADPLN M*25 Amortization expense plan [menu 3101: 16 values, see local-menus.md] act:CCN
  CCNFLG M*4 Managed concessions [menu 1: 1=No,2=Yes] act:CCN
  CCNGRTFLG M*4 Managed subsidies [menu 1: 1=No,2=Yes] act:CCN
  CCNGRTPLN M*25 Subsidy plan [menu 3101: 16 values, see local-menus.md] act:CCN
  CCNINDPLN M*25 Industrial plan [menu 3101: 16 values, see local-menus.md] act:CCN
  CCNMOD M*20 Management mode [menu 3282: 1=1st concession asset,2=Renewal] act:CCN
  CCNRPRTYP M*20 Provision type [menu 3283: 1=Tax,2=Account] act:CCN
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA(15) Chart code -> [COA]COA0 =[CNX]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[CNX]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[CNX]CUR (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  FIYITSSTD M*4 [menu 1: 1=No,2=Yes]
  FLGCNXUO M*4 Management of the OU [menu 1: 1=No,2=Yes]
  FLGLNKPLN M*4(15) Linked plan [menu 1: 1=No,2=Yes]
  FLGPROACC M*4(15) Posting [menu 1: 1=No,2=Yes]
  FLGSIMDET M*4 Detail [menu 1: 1=No,2=Yes]
  FLUTRAACC M*4(15) Track funds account [menu 1: 1=No,2=Yes]
  FLUTRATXS A*5(15) Track funds file
  HRSEXE C*4 FY horizon
  HRSPER C*4 Period horizon
  HRZEXE C*4 FY horizon
  HRZPER C*4 Period horizon
  ISSSIMPL M*4 [menu 1: 1=No,2=Yes]
  LED LED(15) Ledger -> [LED]LED0 =[CNX]LED (GLED) !Delete
  LEDTYP M(15) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LNKPLN M*25(15) Linked plan [menu 3101: 16 values, see local-menus.md]
  NBPLC C*4 Plan number
  ORIBASDPR M*15(15) Deprec basis source [menu 3121: 1=CoA valuation,2=IAS valuation,3=Subsidy amount,4=To be entered]
  PLNCAA M*25(15) Depreciation plan [menu 3101: 16 values, see local-menus.md]
  PLNSTD M*4(15) Standard [menu 3192: 1=Standard,2=CRC2002-10,3=IAS/IFRS]
  PROWEK M*4 Prorata by week [menu 1: 1=No,2=Yes]
  RATPIOCAA M*15 [menu 3187: 1=Depreciation rate,2=Depreciation end date]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  UPDWAIBCO L*8(10) Number of assets to be modified
  UPDWAINBR C*4 Number of modifications
  UPDWAIPAR A*10(10) Modified parameter
  UPDWAITYP A*10(10) Type of modification

## DEPREC (DEP) - Charge
Keys (first = PK; D = duplicates allowed): DEP0 AASREF+DPRPLN+FIYENDDAT+PERENDDAT; DEP2 DPM+CPY (D); DEP3 CPY+DPRPLN+AASREF+FIYENDDAT+PERENDDAT; DEP5 AASREF+DPRPLN+FIYENDDAT+PERSTRDAT; DEP6 DEPSTA+CPY+CNX+FIYENDDAT+PERENDDAT (D); DEP7 FLGDEV+CPY+CNX+FIYENDDAT+PERENDDAT+DPRPLN (D); DEP8 CPY+FLGLNKDEV+CNX+FIYENDDAT+PERENDDAT (D); DEP9 CPY+DPRPLN+FLGPSTLNK+FIYENDDAT+PERENDDAT (D); DEPA CPY+DPRPLN+PERSTRDAT+PERENDDAT+FLGDEV (D)
Fields:
  AASREF VC9 Asset
  ACLCOE RA1 Acceleration coeff.
  ALWAMT MD1 Spc FYR rule amt
  ALWAMTFLG MZS*4 Forc spc FYR rule amt
  ALWCOD M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  ALWCUM MD1 Spc FYR rule tot
  ALWCUMFLG MZS*4 Forced spc rule tot
  APLDUR DUR Applied duration
  AUUID AUUID Single identifier
  BSEVAL MD1 Init bal sht value
  CADCRBDEV MD1 Cad. fund decr. to be posted act:CCN
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[DEP]CPY (COMPANY) !Delete
  CRBAMT MD1 Reintegrtd amount
  CRBCUM MD1 Reintegrtd total
  CRBCUMFLG MZS*4 Cumul réint forced
  CRBVEHCOD ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCOD (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DEP]CREUSR (AUTILIS) !Other
  DEPSTA M*15 Detailed status [menu 3110: 1=Not calculated,2=calculated,3=Closed]
  DERDEV MD1 B. vs T. to post
  DERRVEDEV MD1 B. vs T. rev. to post
  DFD MD1 Deferred deprec
  DFDBLC MD1 Deferred deprec balance
  DFDLIM MD1 Differable amt.
  DFDRVE MD1 Deferred reversal
  DPEDEV MD1 Charge to post
  DPEI MD1 PAC charge
  DPET MD1 Theo charge
  DPM DPM Depreciation method
  DPMI DPM Initial method used
  DPMT DPM Theoretical method used
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRCUMFLG MZS*4 FYR forc deprec tot
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DPRRAT2 RA1 Depreciation rate
  DPRRATFLG MZS*4 Forced deprec rate
  ENDDPE MD1 Fiscal Year charge
  ENDDPEFLG M*4 Forced FY charge [menu 1: 1=No,2=Yes]
  ENDDPEI MD1 Yearly deprec. init.
  ENDDPET MD1 Yearly deprec. theo
  ENDDPRDAT D4 Deprec end date
  ENDDPRFLG M*4 Forced deprec. amt [menu 1: 1=No,2=Yes]
  ETRPNT C*1 Entry point
  EXCCUM MD1 Total excep. amt
  EXCCUMI MD1 Acc excep deprec I
  EXCCUMT MD1 Exc FY-1 theo
  EXCDEV MD1 FY to post
  EXCDPR MD1 FYR except deprec
  EXCDPRI MD1 I FY exc deprec
  EXCDPRT MD1 T FY exc deprec
  EXECLOCUMI MD1 Init cuml clos FY
  EXECLOCUMT MD1 Theo cumul clos FY
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  EXTIMLTYP ADI External reason depr -> [ADI]CODE =516;EXTIMLTYP (ATABDIV) !Block
  FCY FCY Financial site -> [FCY]FCY0 =[DEP]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYQTY QTY FY units
  FIYSTRDAT D4 Fiscal year start date
  FLGDEV M*4 To post [menu 1: 1=No,2=Yes]
  FLGLNKDEV M*4 To post [menu 1: 1=No,2=Yes]
  FLGMIG M*4 Migrated [menu 1: 1=No,2=Yes]
  FLGPST M*4 Posted [menu 1: 1=No,2=Yes]
  FLGPSTLNK M*4 Posted [menu 1: 1=No,2=Yes]
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  IML MD1 P impairment loss
  IMLBLC MD1 Impairment loss balance
  IMLFLG MZS*4 Forced impairment loss
  IMLRVE MD1 Impair. loss reversal P
  IMLRVEFLG MZS*4 Reversal of forced impairment loss
  IMLRVELIM MD1 Reversal cap
  IMLRVETRF MD1 Impair. rev. - exc depr.
  IMLTYP M*15 Impairment loss type [menu 3280: 1=Exceptional,2=A voir]
  INTIMLTYP ADI Internal reason depr -> [ADI]CODE =519;INTIMLTYP (ATABDIV) !Block
  KBIRDAT D4 Anniversary date
  KBIRNBV MD1 Anniv. net value
  KBIRNBVI MD1 Anniv I net value
  KBIRNBVT MD1 Anniv T net value
  KFIYNBMSTP C*4 Depreciation stop
  KMDRDAT D4 Improvement date act:KPL
  KMDRDEV MD1 Improvement value act:KPL
  KNBMSTPDEP C*4 Number of months of stop
  KSTPDEPSTA M*4 Depreciation stop [menu 3289: 1=No stop,2=Improvement,3=Preservation,4=Stopped for improvement,5=Stopped for preservation,6=Restarted after improvement,7=Restarted after preservation,8=Suspend,9=Stopped,10=Restarted after extension,11=Restarted,12=Extension deprec,13=Suspended for extension]
  LEG MD1 Legal link amt
  LEGCUM MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUM MD1 Plan E-1 legal link rec.tot
  LNK MD1 Amount plan link
  LNKCUM MD1 Plan E-1 link total
  LNKDEV MD1 Variance to post
  LSTCLODAT D4 Closing date
  MTCDEVADJ M*15 Rec. meth chge var [menu 3169: 1=Carryforward,2=Exceptional depre fiscal year,3=Exceptional depre period,4=Charge fiscal year,5=Charge period]
  MTCDPEDAT D4 Methd chge date
  MTCDPEDEV MD1 Meth chge depr var
  MTCDPEDEVI MD1 Meth chge depr var
  MTCDPEDEVT MD1 Meth chge depr var
  MTCTIADAT D4 Chge effective date
  MTCTIATYP M*15 Chg effective start [menu 3268: 1=Depreciation start,2=FY start,3=Period start]
  NBV MD1 Net value
  NBVI MD1 Init net value
  NBVT MD1 Theor net value
  NSPVAL MD1 Market value
  PERCADCRB MD1 Amort. fund decrease act:CCN
  PERCLOCUM MD1 Periodic total P-1
  PERCLOCUMI MD1 Init cumul per clos
  PERCLOCUMT MD1 Theo cumul clos per
  PERCLOEXC MD1 Office P-1 amt excep.
  PERCLOEXCI MD1 Acc P-1 exc depr I
  PERCLOEXCT MD1 Acc P-1 exc depr T
  PERDPEFLG M*4 Per forced charge [menu 1: 1=No,2=Yes]
  PERENDDAT D4 Period end date
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PEREXCDPRI MD1 Excep per deprec I
  PEREXCDPRT MD1 Excep per deprec T
  PERIMLCUM MD1 Depre total P-1
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PERLNKCUM MD1 Plan P-1 link total
  PERQTY QTY Period unit
  PERQTYCUM QTY Total period P-1 OPE
  PERREFCLC D4 Calculation period
  PERREFCLCI D4 Per. for I calculation
  PERREFCLCT D4 Per. for T calculation
  PERRVACUM MD1 Acc. closed ps reval amt
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PERSTRDAT D4 Period start date
  PERTRFCUM MD1 Impair. loss rev. transf P-1
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  PSTCADCRB MD1 Cad. fund decr. posted act:CCN
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTLNK MD1 Posted variance
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  P_1CADCRB MD1 Decr. tot. P-1 act:CCN
  RATCUR RCU Currency rate
  RSDDUR DUR Residual duration
  RSDQTY QTY Start period residual duratn OPE
  RSDVAL MD1 Residual value
  RVAAMT MD1 Revaluation amount
  RVACOE COE Revaluation coef
  RVACOEREF A*20 Table reference
  RVACRB MD1 Revaluation reversal
  RVACRBDEV MD1 Re-eval rec. to be posted
  RVADAT D4 Revaluation date
  RVATIADAT M*15 Reval. effective start [menu 3273: 1=FY start,2=Period start,3=FY end]
  RVATYP M*15 Revaluation type [menu 3253: 1=Coefficient,2=Index,3=Market value]
  RVETRFDEV MD1 Depr rec trf to be posted
  STRDPRDAT D4 Depre start date
  TRFCADCUM MD1 Amortization fund act:CCN
  UOM UOM Unit -> [TUN]TUN0 =[DEP]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DEP]UPDUSR (AUTILIS) !Other

## DEPRECARC (DEA) - Charge archive
Keys (first = PK; D = duplicates allowed): DEP0 AASREF+DPRPLN+EVT+TIMSTP+FIYENDDAT+PERENDDAT
Fields:
  AASREF VC9 Asset
  ACLCOE RA1 Acceleration coeff.
  ALWAMT MD1 Spc FYR rule amt
  ALWAMTFLG MZS*4 Forc spc FYR rule amt
  ALWCOD M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  ALWCUM MD1 Spc FYR rule tot
  ALWCUMFLG MZS*4 Forced spc rule tot
  APLDUR DUR Applied duration
  AUUID AUUID Single identifier
  BSEVAL MD1 Init bal sht value
  CADCRBDEV MD1 Cad. fund decr. to be posted act:CCN
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[DEA]CPY (COMPANY) !Delete
  CRBAMT MD1 Reintegrtd amount
  CRBCUM MD1 Reintegrtd total
  CRBCUMFLG MZS*4 Cumul réint forced
  CRBVEHCOD ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCOD (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DEA]CREUSR (AUTILIS) !Other
  DEPSTA M*15 Detailed status [menu 3110: 1=Not calculated,2=calculated,3=Closed]
  DERDEV MD1 B. vs T. to post
  DERRVEDEV MD1 B. vs T. rev. to post
  DFD MD1 Deferred deprec
  DFDBLC MD1 Deferred deprec balance
  DFDLIM MD1 Differable amt.
  DFDRVE MD1 Deferred reversal
  DPEDEV MD1 Charge to post
  DPEI MD1 PAC charge
  DPET MD1 Theo charge
  DPM DPM Depreciation method
  DPMI DPM Initial method used
  DPMT DPM Theoretical method used
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRCUMFLG MZS*4 FYR forc deprec tot
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DPRRAT2 RA1 Depreciation rate
  DPRRATFLG MZS*4 Forced deprec rate
  ENDDPE MD1 Fiscal Year charge
  ENDDPEFLG M*4 Forced FY charge [menu 1: 1=No,2=Yes]
  ENDDPEI MD1 Yearly deprec. init.
  ENDDPET MD1 Yearly deprec. theo
  ENDDPRDAT D4 Deprec end date
  ENDDPRFLG M*4 Forced deprec. amt [menu 1: 1=No,2=Yes]
  ETRPNT C*1 Entry point
  EVT ADI Event type -> [ADI]CODE =962;EVT (ATABDIV) !Delete
  EXCCUM MD1 Total excep. amt
  EXCCUMI MD1 Acc excep deprec I
  EXCCUMT MD1 Exc FY-1 theo
  EXCDEV MD1 FY to post
  EXCDPR MD1 FYR except deprec
  EXCDPRI MD1 I FY exc deprec
  EXCDPRT MD1 T FY exc deprec
  EXECLOCUMI MD1 Init cuml clos FY
  EXECLOCUMT MD1 Theo cumul clos FY
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  EXTIMLTYP ADI External reason depr -> [ADI]CODE =516;EXTIMLTYP (ATABDIV) !Block
  FCY FCY Financial site -> [FCY]FCY0 =[DEA]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYQTY QTY FY units
  FIYSTRDAT D4 Fiscal year start date
  FLGDEV M*4 To post [menu 1: 1=No,2=Yes]
  FLGLNKDEV M*4 To post [menu 1: 1=No,2=Yes]
  FLGMIG M*4 Migrated [menu 1: 1=No,2=Yes]
  FLGPST M*4 Posted [menu 1: 1=No,2=Yes]
  FLGPSTLNK M*4 Posted [menu 1: 1=No,2=Yes]
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  IML MD1 P impairment loss
  IMLBLC MD1 Impairment loss balance
  IMLFLG MZS*4 Forced impairment loss
  IMLRVE MD1 Impair. loss reversal P
  IMLRVEFLG MZS*4 Reversal of forced impairment loss
  IMLRVELIM MD1 Reversal cap
  IMLRVETRF MD1 Impair. rev. - exc depr.
  IMLTYP M*15 Impairment loss type [menu 3280: 1=Exceptional,2=A voir]
  INTIMLTYP ADI Internal reason depr -> [ADI]CODE =519;INTIMLTYP (ATABDIV) !Block
  KBIRNBV MD1 Anniv. net value act:KRU
  KFIYNBMSTP C*4 Depreciation stop act:KRU
  LEG MD1 Legal link amt
  LEGCUM MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUM MD1 Plan E-1 legal link rec.tot
  LNK MD1 Amount plan link
  LNKCUM MD1 Plan E-1 link total
  LNKDEV MD1 Variance to post
  LSTCLODAT D4 Closing date
  MTCDEVADJ M*15 Rec. meth chge var [menu 3169: 1=Carryforward,2=Exceptional depre fiscal year,3=Exceptional depre period,4=Charge fiscal year,5=Charge period]
  MTCDPEDAT D4 Methd chge date
  MTCDPEDEV MD1 Meth chge depr var
  MTCDPEDEVI MD1 Meth chge depr var
  MTCDPEDEVT MD1 Meth chge depr var
  MTCTIADAT D4 Chge effective date
  MTCTIATYP M*15 Chg effective start [menu 3268: 1=Depreciation start,2=FY start,3=Period start]
  NBV MD1 Net value
  NBVI MD1 Init net value
  NBVT MD1 Theor net value
  NSPVAL MD1 Market value
  PERCADCRB MD1 Amort. fund decrease act:CCN
  PERCLOCUM MD1 Periodic total P-1
  PERCLOCUMI MD1 Init cumul per clos
  PERCLOCUMT MD1 Theo cumul clos per
  PERCLOEXC MD1 Office P-1 amt excep.
  PERCLOEXCI MD1 Acc P-1 exc depr I
  PERCLOEXCT MD1 Acc P-1 exc depr T
  PERDPEFLG M*4 Per forced charge [menu 1: 1=No,2=Yes]
  PERENDDAT D4 Period end date
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PEREXCDPRI MD1 Excep per deprec I
  PEREXCDPRT MD1 Excep per deprec T
  PERIMLCUM MD1 Depre total P-1
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PERLNKCUM MD1 Plan P-1 link total
  PERQTY QTY Period unit
  PERQTYCUM QTY Total period P-1 OPE
  PERREFCLC D4 Calculation period
  PERREFCLCI D4 Per. for I calculation
  PERREFCLCT D4 Per. for T calculation
  PERRVACUM MD1 Acc. closed ps reval amt
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PERSTRDAT D4 Period start date
  PERTRFCUM MD1 Impair. loss rev. transf P-1
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  PSTCADCRB MD1 Cad. fund decr. posted act:CCN
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTLNK MD1 Posted variance
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  P_1CADCRB MD1 Decr. tot. P-1 act:CCN
  RATCUR RCU Currency rate
  RSDDUR DUR Residual duration
  RSDQTY QTY Start period residual duratn OPE
  RSDVAL MD1 Residual value
  RVAAMT MD1 Revaluation amount
  RVACOE COE Revaluation coef
  RVACOEREF A*20 Table reference
  RVACRB MD1 Revaluation reversal
  RVACRBDEV MD1 Re-eval rec. to be posted
  RVADAT D4 Revaluation date
  RVATIADAT M*15 Reval. effective start [menu 3273: 1=FY start,2=Period start,3=FY end]
  RVATYP M*15 Revaluation type [menu 3253: 1=Coefficient,2=Index,3=Market value]
  RVETRFDEV MD1 Depr rec trf to be posted
  STRDPRDAT D4 Depre start date
  TIMSTP A*20 Time stamp
  TRFCADCUM MD1 Amortization fund act:CCN
  UOM UOM Unit -> [TUN]TUN0 =[DEA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DEA]UPDUSR (AUTILIS) !Other

## DEPSIMU (DPS) - Charge
Keys (first = PK; D = duplicates allowed): DPS0 AASREF+DPRPLN+FIYENDDAT+PERSTRDAT; DPS1 CPY+CNX (D)
Fields:
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[DPS]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DPS]CREUSR (AUTILIS) !Other
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EXCCUM MD1 Total excep. amt
  EXERVADEV MD1 Closed FY total reval. surpl.
  FCY FCY Financial site -> [FCY]FCY0 =[DPS]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  IML MD1 P impairment loss
  IMLBLC MD1 Impairment loss balance
  IMLRVE MD1 Impair. loss reversal P
  IMLRVEISS MD1(15) Impair. rev./disposal
  IMLRVETRF MD1 Impair. rev. - exc depr.
  NBV MD1 Net value
  PERCLOCUM MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERENDDAT D4 Period end date
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PERSTRDAT D4 Period start date
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  RATCUR RCU Currency rate
  STRDPRDAT D4 Depre start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DPS]UPDUSR (AUTILIS) !Other

## DPRMOD (DPM) - Depreciation methods
Notes: differs in V10 P1 (diff: ATD_DPRMOD.htm)
Keys (first = PK; D = duplicates allowed): DPM0 DPM+CPY; DPM1 STDDPMNUM (D); DPM2 DPRMODTYP+CPY+DPM; DPM3 STDDPM
Fields:
  ANIDATFLG M*4 Calculate on anniversary date [menu 1: 1=No,2=Yes]
  APLPLNFLG M*10(16) Applicable to plan [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BASTYP M*15 Depreciation basis type [menu 3106: 1=Balance sheet value,2=Net value,3=Balance sheet value/Depreciation duration,4=Net value/residual duration,5=Net value/total duration,6=Balance sheet value - salvage value,7=Net value - Salvage value,8=Net value/residual duration]
  CPY CPY Company -> [CPY]CPY0 =[DPM]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[DPM]CRY (TABCOUNTRY) !Block
  DES DES Description
  DESUPDFLG M*4 Label reason [menu 1: 1=No,2=Yes]
  DPM DPM Depreciation method
  DPRDISRUL M*15 Distribution rule [menu 3299: 1=Period distribution,2=1st available period]
  DPRMODTYP M*15 Depre method type [menu 3103: 1=Free,2=Standard]
  ENAFLG M*4 Active flag [menu 1: 1=No,2=Yes]
  ENDDATTYP M*15 Disposal date rule [menu 3124: 10 values, see local-menus.md]
  ENDDPRTYP M*15 Depre end rule [menu 3124: 10 values, see local-menus.md]
  ETRDATTYP M*15 Depre start rule [menu 3104: 1=On the specified day,2=From first day of the month,3=From first day of the next month,4=From first day of investment FY,5=From first day of next FY,6=From first day of investment half-year]
  EXCDPRRAT RA1 Exc. depr rate
  EXCDPRTYP M*15 Ex depre type [menu 3116: 21 values, see local-menus.md]
  FIRFIYFLG M*4 1st FY calculated for 1yr. [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MAXDPRRAT RA1 Ceiling rate
  MAXDPRTYP M*15 Ceiling value type [menu 3116: 21 values, see local-menus.md]
  MINDPRLIF DCB*2.3 Minimum depr duration
  MINDPRRAT RA1 Minimum rate
  MINDPRTYP M*15 Minimum value type [menu 3116: 21 values, see local-menus.md]
  NOMABT DES Description
  PRATYPTGR M*15 Target prorata type [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  PROTYP M*15 Prorata type [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  RATCOETYP M*15 Rate application rule [menu 3116: 21 values, see local-menus.md]
  RATNBR C*2 Number of rates
  RSDDPMTGR DPM Residual equivalent method
  STDDPM A*2 Calcn methd
  STDDPMNUM M*15 Calcn methd no. [menu 3228: 45 values, see local-menus.md]
  STRDATTYP M Depre start date [menu 3212: 1=Purchase date,2=First use date,3=Posting date]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## DPRMODOPT (DMO) - Depreciation method option
Keys (first = PK; D = duplicates allowed): DMO0 STDDPM+CPY+NUMDPM
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[DMO]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMO]CREUSR (AUTILIS) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  ENDVLYDAT D4 Validity end
  NUMDPM C*4 Order no.
  OPTCOD M*1 Option code [menu 3116: 21 values, see local-menus.md]
  OPTCPY CPY Company -> [CPY]CPY0 =[DMO]OPTCPY (COMPANY) !Delete
  OPTRAT RA1 Option rate
  OPTTYP M*15 Option type [menu 3114: 10 values, see local-menus.md]
  REFDATTYP M*15 Reference date type [menu 3115: 1=Depreciation start date,2=Asset purchase date,3=Reference date for the calculation of the +/- value,4=No reference date]
  STDDPM A*2 Calcn methd
  STRVLYDAT D4 Validity start
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMO]UPDUSR (AUTILIS) !Other

## DPRMODRAT (DMR) - Depreciation method rate
Keys (first = PK; D = duplicates allowed): DMR0 DPM+CPY+NUM
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[DMR]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DMR]CREUSR (AUTILIS) !Other
  DPM DPM Depreciation method
  NUM C*4 Order no.
  RAT RA1 Annuity rate
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DMR]UPDUSR (AUTILIS) !Other

## ECCNEND (E52) - Evt - concession end
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E52]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E52]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E52]FCY (FACILITY) !Delete
  LIN C*4 Line number
  REAENDCCN D4 Effective end
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ECCNREV (E51) - Evt - concession add. clause
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E51]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E51]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  ENDCCNDATN D4 Concession end after
  ENDCCNDATO D4 Concession end before
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E51]FCY (FACILITY) !Delete
  LIN C*4 Line number
  REF VC9 Reference
  REVREN DCO Reason
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASACT (E21) - Evt - update
Notes: differs in V10 P1 (diff: ATD_EFASACT.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACTDED MD1 Sales tax revision
  ACTDPR MD1 Revision
  ACTETR MD1 CoA revision
  ACTGAL MD1 Revision
  ACTIVC MD1 Sales tax revision
  ACTTAX MD1 Revision
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E21]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E21]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMTD MD1 Rec. sales tax revised
  DEDVATAMTO MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRBASD MD1 Balance sheet value revised
  DPRBASO MD1 Reval. BS value
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOTD MD1 Ex-tax value revised
  ETRNOTO MD1 Receipt value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E21]FCY (FACILITY) !Delete
  GALREFBASD MD1 Updated reference basis
  GALREFBASO MD1 Ref basis+/- value
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMTD MD1 Inv. sales tax revised
  IVCVATAMTO MD1 VAT invoiced
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TAXBASD MD1 Updated tax basis
  TAXBASO MD1 Tax basis
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASAFFAGE (E22) - Evt - analytical/geo transfer
Notes: differs in V10 P1 (diff: ATD_EFASAFFAGE.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUSD VC9 New activity
  AASBUSO VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACGETRNOT MD1 Receipt value ex-tax
  AUUID AUUID Single identifier
  CCE10D CCE Dimension -> [CCE]CCE0 =DIE10;CCE10D (CACCE) !Other
  CCE10O CCE Dimension -> [CCE]CCE0 =DIE10;CCE10O (CACCE) !Other
  CCE11D CCE Dimension -> [CCE]CCE0 =DIE11;CCE11D (CACCE) !Other
  CCE11O CCE Dimension -> [CCE]CCE0 =DIE11;CCE11O (CACCE) !Other
  CCE12D CCE Dimension -> [CCE]CCE0 =DIE12;CCE12D (CACCE) !Other
  CCE12O CCE Dimension -> [CCE]CCE0 =DIE12;CCE12O (CACCE) !Other
  CCE13D CCE Dimension -> [CCE]CCE0 =DIE13;CCE13D (CACCE) !Other
  CCE13O CCE Dimension -> [CCE]CCE0 =DIE13;CCE13O (CACCE) !Other
  CCE14D CCE Dimension -> [CCE]CCE0 =DIE14;CCE14D (CACCE) !Other
  CCE14O CCE Dimension -> [CCE]CCE0 =DIE14;CCE14O (CACCE) !Other
  CCE15D CCE Dimension -> [CCE]CCE0 =DIE15;CCE15D (CACCE) !Other
  CCE15O CCE Dimension -> [CCE]CCE0 =DIE15;CCE15O (CACCE) !Other
  CCE16D CCE Dimension -> [CCE]CCE0 =DIE16;CCE16D (CACCE) !Other
  CCE16O CCE Dimension -> [CCE]CCE0 =DIE16;CCE16O (CACCE) !Other
  CCE17D CCE Dimension -> [CCE]CCE0 =DIE17;CCE17D (CACCE) !Other
  CCE17O CCE Dimension -> [CCE]CCE0 =DIE17;CCE17O (CACCE) !Other
  CCE18D CCE Dimension -> [CCE]CCE0 =DIE18;CCE18D (CACCE) !Other
  CCE18O CCE Dimension -> [CCE]CCE0 =DIE18;CCE18O (CACCE) !Other
  CCE19D CCE Dimension -> [CCE]CCE0 =DIE19;CCE19D (CACCE) !Other
  CCE19O CCE Dimension -> [CCE]CCE0 =DIE19;CCE19O (CACCE) !Other
  CCE1D CCE New section -> [CCE]CCE0 =DIE1;CCE1D (CACCE) !Other
  CCE1O CCE Dimension -> [CCE]CCE0 =DIE1;CCE1O (CACCE) !Other
  CCE20D CCE Dimension -> [CCE]CCE0 =DIE20;CCE20D (CACCE) !Other
  CCE20O CCE Dimension -> [CCE]CCE0 =DIE20;CCE20O (CACCE) !Other
  CCE2D CCE New section -> [CCE]CCE0 =DIE2;CCE2D (CACCE) !Other
  CCE2O CCE Dimension -> [CCE]CCE0 =DIE2;CCE2O (CACCE) !Other
  CCE3D CCE New section -> [CCE]CCE0 =DIE3;CCE3D (CACCE) !Other
  CCE3O CCE Dimension -> [CCE]CCE0 =DIE3;CCE3O (CACCE) !Other
  CCE4D CCE New section -> [CCE]CCE0 =DIE4;CCE4D (CACCE) !Other
  CCE4O CCE Dimension -> [CCE]CCE0 =DIE4;CCE4O (CACCE) !Other
  CCE5D CCE New section -> [CCE]CCE0 =DIE5;CCE5D (CACCE) !Other
  CCE5O CCE Dimension -> [CCE]CCE0 =DIE5;CCE5O (CACCE) !Other
  CCE6D CCE New section -> [CCE]CCE0 =DIE6;CCE6D (CACCE) !Other
  CCE6O CCE Dimension -> [CCE]CCE0 =DIE6;CCE6O (CACCE) !Other
  CCE7D CCE New section -> [CCE]CCE0 =DIE7;CCE7D (CACCE) !Other
  CCE7O CCE Dimension -> [CCE]CCE0 =DIE7;CCE7O (CACCE) !Other
  CCE8D CCE New section -> [CCE]CCE0 =DIE8;CCE8D (CACCE) !Other
  CCE8O CCE Dimension -> [CCE]CCE0 =DIE8;CCE8O (CACCE) !Other
  CCE9D CCE New section -> [CCE]CCE0 =DIE9;CCE9D (CACCE) !Other
  CCE9O CCE Dimension -> [CCE]CCE0 =DIE9;CCE9O (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E22]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E22]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DEDVATFLG M*4 Forced rec VAT [menu 1: 1=No,2=Yes]
  DEDVATFLGI M*4 Forced rec VAT [menu 1: 1=No,2=Yes]
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  DERBAL MD1 Book vs tax balance FY-1
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSPD DSP New allocation -> [DSP]DSP0 =DSPD;1 (CADSP) !Delete
  DSPO DSP Distribution -> [DSP]DSP0 =DSPO;1 (CADSP) !Delete
  ENDDPE MD1 Fiscal Year charge
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EVTPRINC M*4 Main event [menu 1: 1=No,2=Yes]
  EXCDPR MD1 FYR except deprec
  FCY FCY Site -> [FCY]FCY0 =[E22]FCY (FACILITY) !Delete
  FCYD FCY New site -> [FCY]FCY0 =[E22]FCYD (FACILITY) !Block
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASCGUD ADI New CGU -> [ADI]CODE =613;IASCGUD (ATABDIV) !Delete
  IASCGUO ADI UGT -> [ADI]CODE =613;IASCGUO (ATABDIV) !Delete
  IASDEV MD1 IAS recov VAT var
  IASETRNOT MD1 Receipt value ex-tax
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  IVCVATFLG M*4 Invoiced VAT forced [menu 1: 1=No,2=Yes]
  IVCVATFLGI M*4 Invoiced VAT forced [menu 1: 1=No,2=Yes]
  LASMFLG M*10 Deductible VAT update [menu 1: 1=No,2=Yes]
  LASTDATTRF D4 Transfer date
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PCGDEV MD1 CoA recov VAT var
  PERCLOCUM MD1 Periodic total P-1
  PERIMLCUM MD1 Depre total P-1
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PSCDER MD1 Acc. B. vs T. rev. posted
  PSCDERRVE MD1 Merge derogatory reversal
  PSCDPE MD1 Acc charges accumul
  PSCEXC MD1 Exc. merging acc.
  PSCRVACRB MD1 Merge acc. reval. reversal
  PSCRVETRF MD1 Trf merging acc.
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  REF VC9 Reference
  REGUL MD1 Tax adjustment
  REN ADI Reason -> [ADI]CODE =612;REN (ATABDIV) !Block
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RSDVAL MD1 Residual value
  RVABAL MD1 Reval. balance FY-1
  RVEBAL MD1 Impair. loss closing E-1
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TAXCOE RAT Taxation coeff
  TAXCOEF RAT Taxation coeff
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TIMSTPP A*20 Time stamp
  TRFTYP C*2 Transfer type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount
  VATREGDAT D4 Reference date

## EFASCCN (E53) - Evt - concession attribute update
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCNACTCODN CCA Update code
  CCNACTCODO CCA Update code
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E53]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E53]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E53]FCY (FACILITY) !Delete
  LIN C*4 Line number
  OBYRNWCONN M*4 CRO flag [menu 1: 1=No,2=Yes]
  OBYRNWCONO M*4 CRO flag [menu 1: 1=No,2=Yes]
  REF VC9 Reference
  REN DCO Reason
  RNWDATN D4 Renewal date
  RNWDATO D4 Renewal date
  RNWFLGN M*4 ERO flag [menu 1: 1=No,2=Yes]
  RNWFLGO M*4 ERO flag [menu 1: 1=No,2=Yes]
  RNWTRFCAD MD1 Forwarded funds
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TPAFLGN M*4 Remittance with payment [menu 1: 1=No,2=Yes]
  TPAFLGO M*4 Remittance with payment [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCCNAGE (E34) - Evt - provision transfer
Notes: activity code CCN; differs in V10 P1 (diff: ATD_EFASCCNAGE.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUSD VC9 New activity
  AASBUSO VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE10D CCE Dimension -> [CCE]CCE0 =DIE10;CCE10D (CACCE) !Other
  CCE10O CCE Dimension -> [CCE]CCE0 =DIE10;CCE10O (CACCE) !Other
  CCE11D CCE Dimension -> [CCE]CCE0 =DIE11;CCE11D (CACCE) !Other
  CCE11O CCE Dimension -> [CCE]CCE0 =DIE11;CCE11O (CACCE) !Other
  CCE12D CCE Dimension -> [CCE]CCE0 =DIE12;CCE12D (CACCE) !Other
  CCE12O CCE Dimension -> [CCE]CCE0 =DIE12;CCE12O (CACCE) !Other
  CCE13D CCE Dimension -> [CCE]CCE0 =DIE13;CCE13D (CACCE) !Other
  CCE13O CCE Dimension -> [CCE]CCE0 =DIE13;CCE13O (CACCE) !Other
  CCE14D CCE Dimension -> [CCE]CCE0 =DIE14;CCE14D (CACCE) !Other
  CCE14O CCE Dimension -> [CCE]CCE0 =DIE14;CCE14O (CACCE) !Other
  CCE15D CCE Dimension -> [CCE]CCE0 =DIE15;CCE15D (CACCE) !Other
  CCE15O CCE Dimension -> [CCE]CCE0 =DIE15;CCE15O (CACCE) !Other
  CCE16D CCE Dimension -> [CCE]CCE0 =DIE16;CCE16D (CACCE) !Other
  CCE16O CCE Dimension -> [CCE]CCE0 =DIE16;CCE16O (CACCE) !Other
  CCE17D CCE Dimension -> [CCE]CCE0 =DIE17;CCE17D (CACCE) !Other
  CCE17O CCE Dimension -> [CCE]CCE0 =DIE17;CCE17O (CACCE) !Other
  CCE18D CCE Dimension -> [CCE]CCE0 =DIE18;CCE18D (CACCE) !Other
  CCE18O CCE Dimension -> [CCE]CCE0 =DIE18;CCE18O (CACCE) !Other
  CCE19D CCE Dimension -> [CCE]CCE0 =DIE19;CCE19D (CACCE) !Other
  CCE19O CCE Dimension -> [CCE]CCE0 =DIE19;CCE19O (CACCE) !Other
  CCE1D CCE New section -> [CCE]CCE0 =DIE1;CCE1D (CACCE) !Other
  CCE1O CCE Dimension -> [CCE]CCE0 =DIE1;CCE1O (CACCE) !Other
  CCE20D CCE Dimension -> [CCE]CCE0 =DIE20;CCE20D (CACCE) !Other
  CCE20O CCE Dimension -> [CCE]CCE0 =DIE20;CCE20O (CACCE) !Other
  CCE2D CCE New section -> [CCE]CCE0 =DIE2;CCE2D (CACCE) !Other
  CCE2O CCE Dimension -> [CCE]CCE0 =DIE2;CCE2O (CACCE) !Other
  CCE3D CCE New section -> [CCE]CCE0 =DIE3;CCE3D (CACCE) !Other
  CCE3O CCE Dimension -> [CCE]CCE0 =DIE3;CCE3O (CACCE) !Other
  CCE4D CCE New section -> [CCE]CCE0 =DIE4;CCE4D (CACCE) !Other
  CCE4O CCE Dimension -> [CCE]CCE0 =DIE4;CCE4O (CACCE) !Other
  CCE5D CCE New section -> [CCE]CCE0 =DIE5;CCE5D (CACCE) !Other
  CCE5O CCE Dimension -> [CCE]CCE0 =DIE5;CCE5O (CACCE) !Other
  CCE6D CCE New section -> [CCE]CCE0 =DIE6;CCE6D (CACCE) !Other
  CCE6O CCE Dimension -> [CCE]CCE0 =DIE6;CCE6O (CACCE) !Other
  CCE7D CCE New section -> [CCE]CCE0 =DIE7;CCE7D (CACCE) !Other
  CCE7O CCE Dimension -> [CCE]CCE0 =DIE7;CCE7O (CACCE) !Other
  CCE8D CCE New section -> [CCE]CCE0 =DIE8;CCE8D (CACCE) !Other
  CCE8O CCE Dimension -> [CCE]CCE0 =DIE8;CCE8O (CACCE) !Other
  CCE9D CCE New section -> [CCE]CCE0 =DIE9;CCE9D (CACCE) !Other
  CCE9O CCE Dimension -> [CCE]CCE0 =DIE9;CCE9O (CACCE) !Other
  CCNREFD CCN New concession -> [CCN]CCN0 =CPY;CCNREFD (CONCESSION) !RTZ
  CCNREFO CCN Concession -> [CCN]CCN0 =CPY;CCNREFO (CONCESSION) !RTZ
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E34]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E34]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSPD DSP New allocation -> [DSP]DSP0 =DSPD;1 (CADSP) !Delete
  DSPO DSP Distribution -> [DSP]DSP0 =DSPO;1 (CADSP) !Delete
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EVTPRINC M*4 Main event [menu 1: 1=No,2=Yes]
  E_1ACGRPR MD1 FY-1 tot. acc. prov.
  E_1FISRPR MD1 FY-1 total fisc. prov.
  E_1RVERPR MD1 FY-1 tot. tax rev.
  E_1SUPCAD MD1 FY-1 tot. add. tax cad.
  FCY FCY Site -> [FCY]FCY0 =[E34]FCY (FACILITY) !Delete
  FCYD FCY New site -> [FCY]FCY0 =[E34]FCYD (FACILITY) !Block
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASCGUD ADI New CGU -> [ADI]CODE =613;IASCGUD (ATABDIV) !Delete
  IASCGUO ADI UGT -> [ADI]CODE =613;IASCGUO (ATABDIV) !Delete
  LASTDATTRF D4 Transfer date
  LIN C*4 Line number
  PSTACGRPR MD1 Posted prov.
  PSTFISRPR MD1 F. prov. posted
  P_1ACGRPR MD1 P-1 tot. acc. prov.
  P_1FISRPR MD1 P-1 total tax prov.
  P_1RVERPR MD1 P-1 total tax reversal
  P_1SUPCAD MD1 P-1 total add. tax cad.
  REF VC9 Reference
  REN ADI Reason -> [ADI]CODE =612;REN (ATABDIV) !Block
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TIMSTPP A*20 Time stamp
  TRFTYP C*2 Transfer type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCCNCNL (E32) - Evt - asset deletion
Notes: activity code CCN; differs in V10 P1 (diff: ATD_EFASCCNCNL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E32]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E32]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  E_1ACGRPR MD1 FY-1 tot. acc. prov.
  E_1FISRPR MD1 FY-1 total fisc. prov.
  E_1RVERPR MD1 FY-1 tot. tax rev.
  E_1SUPCAD MD1 FY-1 tot. add. tax cad.
  FCY FCY Site -> [FCY]FCY0 =[E32]FCY (FACILITY) !Delete
  LIN C*4 Line number
  PSTACGRPR MD1 Posted prov.
  PSTFISRPR MD1 F. prov. posted
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCCNISS (E33) - Evt - asset disposal provision
Notes: activity code CCN; differs in V10 P1 (diff: ATD_EFASCCNISS.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CCNRPRTYP M*20 Processing type [menu 3283: 1=Tax,2=Account]
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E33]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E33]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  E_1ACGRPR MD1 FY-1 tot. acc. prov.
  E_1FISRPR MD1 FY-1 total fisc. prov.
  E_1RVERPR MD1 FY-1 tot. tax rev.
  E_1SUPCAD MD1 FY-1 tot. add. tax cad.
  FCY FCY Site -> [FCY]FCY0 =[E33]FCY (FACILITY) !Delete
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERSUPCAD MD1 Add. period amort. act:CCN
  PSTACGRPR MD1 Posted prov.
  PSTFISRPR MD1 F. prov. posted
  P_1ACGRPR MD1 P-1 tot. acc. prov.
  P_1FISRPR MD1 P-1 total tax prov.
  P_1RVERPR MD1 P-1 total tax reversal
  P_1SUPCAD MD1 P-1 total add. tax cad.
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCFS (E38) - Evt -Classification for sale
Notes: differs in V10 P1 (diff: ATD_EFASCFS.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACCCODD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCODD;[V]GSUPCLE (GACCCODE) !Block
  ACGGRPD FAM Acct group -> [FAM]FAM0 =ACGGRPD (FASFAM) !Block
  ACGGRPO FAM Acct group -> [FAM]FAM0 =ACGGRPO (FASFAM) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E38]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E38]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ENDDPE MD1 Fiscal Year charge
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EVTPRINC M*4 Main event [menu 1: 1=No,2=Yes]
  EXCCUM MD1 Total excep. amt
  EXCDPR MD1 FYR except deprec
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXTSALAMT MD1 Expected sale amount
  FCY FCY Site -> [FCY]FCY0 =[E38]FCY (FACILITY) !Delete
  GACACND M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACACNO M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACD GAC Account -> [GAC]GAC0 ="";GACD (GACCOUNT) !Other
  GACO GAC Account -> [GAC]GAC0 ="";GACO (GACCOUNT) !Other
  IASACCD GAC IFRS allocation -> [GAC]GAC0 ="";IASACCD (GACCOUNT) !Other act:IAS
  IASACCO GAC IFRS allocation -> [GAC]GAC0 ="";IASACCO (GACCOUNT) !Other act:IAS
  IASACND M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IASACNO M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IML MD1 Impairment
  IMLRVE MD1 Impairment loss reversal
  ITSDAT D4 In service date
  LEG MD1 Legal link amt
  LEGCUM MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUM MD1 Plan E-1 legal link rec.tot
  LIN C*4 Line number
  OWNTYPD M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  OWNTYPO M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUM MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERENDDPE MD1 Period P charge
  PERIMLCUM MD1 Depre total P-1
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  PURDAT D4 Purchase date
  REF VC9 Reference
  REN ADI Reason -> [ADI]CODE =603;REN (ATABDIV) !RTZ
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RSDVAL MD1 Residual value
  SALCLSDAT D4 Asset date for sale
  SALCLSDATO D4 Asset date for sale
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  STRDPRDAT D4 Depre start date
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TIMSTPP A*20 Time stamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCHGIMP (E23) - Evt - change acct allocation
Notes: differs in V10 P1 (diff: ATD_EFASCHGIMP.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCODD;[V]GSUPCLE (GACCCODE) !Other
  ACGGRPD FAM Acct group -> [FAM]FAM0 =ACGGRPD (FASFAM) !Other
  ACGGRPO FAM Acct group -> [FAM]FAM0 =ACGGRPO (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E23]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E23]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ENDDPE MD1 Fiscal Year charge
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EVTPRINC M*4 Main event [menu 1: 1=No,2=Yes]
  EXCCUM MD1 Total excep. amt
  EXCDPR MD1 FYR except deprec
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXTSALAMT MD1 Expected sale amount
  FCY FCY Site -> [FCY]FCY0 =[E23]FCY (FACILITY) !Delete
  GACACND M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACACNO M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACD GAC Account -> [GAC]GAC0 ="";GACD (GACCOUNT) !Other
  GACO GAC Account -> [GAC]GAC0 ="";GACO (GACCOUNT) !Other
  IASACCD GAC IFRS allocation -> [GAC]GAC0 ="";IASACCD (GACCOUNT) !Other act:IAS
  IASACCO GAC IFRS allocation -> [GAC]GAC0 ="";IASACCO (GACCOUNT) !Other act:IAS
  IASACND M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IASACNO M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IML MD1 Impairment
  IMLRVE MD1 Impairment loss reversal
  ITSDAT D4 In service date
  LEG MD1 Legal link amt
  LEGCUM MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUM MD1 Plan E-1 legal link rec.tot
  LIN C*4 Line number
  OWNTYPD M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  OWNTYPO M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUM MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERENDDPE MD1 Period P charge
  PERIMLCUM MD1 Depre total P-1
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  PURDAT D4 Purchase date
  REF VC9 Reference
  REN ADI Reason -> [ADI]CODE =603;REN (ATABDIV) !Other
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RSDVAL MD1 Residual value
  SALCLSDAT D4 Asset date for sale
  SALCLSDATO D4 Asset date for sale
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  STRDPRDAT D4 Depre start date
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TIMSTPP A*20 Time stamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCHGPPL (E37) - Evt-Production plan change
Notes: differs in V10 P1 (diff: ATD_EFASCHGPPL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E37]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E37]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E37]FCY (FACILITY) !Delete
  LIN C*4 Line number
  PROPLNN PPL Production plan -> [PLH]PPH0 =[E37]PROPLNN (PROPLNH) !Delete
  PROPLNO PPL Production plan -> [PLH]PPH0 =[E37]PROPLNO (PROPLNH) !Delete
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCNL (E30) - Evt - asset deletion
Notes: differs in V10 P1 (diff: ATD_EFASCNL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACCCODORI CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCODORI;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTEXEANT M*4 Reversal [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E30]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E30]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EXCCUM MD1 Total excep. amt
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  FCY FCY Site -> [FCY]FCY0 =[E30]FCY (FACILITY) !Delete
  IML MD1 Impairment
  IMLRVE MD1 Impairment loss reversal
  LEGCUM MD1 Plan E-1 llegal link total
  LEGRVECUM MD1 Plan E-1 legal link rec.tot
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PSTCADCRB MD1 Cad. fund decr. posted act:CCN
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RVAAMT MD1 Revaluation amount
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TYPANN C*2 Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASCRT (E24) - Evt - asset creation
Notes: differs in V10 P1 (diff: ATD_EFASCRT.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODLEA CAC Acc code contract -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCODLEA;[V]GSUPCLE (GACCCODE) !Other act:LEA
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E24]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E24]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOT MD1 Entry value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E24]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASIML (E25) - Evt - impairment loss
Notes: differs in V10 P1 (diff: ATD_EFASIML.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E25]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E25]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPM DPM Depreciation method
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E25]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other act:IAS
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  IML MD1 Impairment
  IMLRVE MD1 Impairment loss reversal
  IMLTYP M*15 Impairment loss type [menu 3280: 1=Exceptional,2=A voir]
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  PURNAT M*15 Purch nature [menu 3152: 1=New,2=Second-hand]
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RVARVE MD1 Revaluation reversal
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASISS (E26) - Evt - asset disposal
Notes: differs in V10 P1 (diff: ATD_EFASISS.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ADDDPR MD1 Additional expense
  AMTTAX1 MD1 Tax amount
  AMTTAX2 MD1 Tax amount
  AMTTAXISS MD1 Issue tax amount
  AMTTAXOTH1 MD1 Amount other tax 1
  AMTTAXOTH2 MD1 Amount other tax 2
  AMTTAXRCP MD1 Receipt tax amount
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPRSAC SAC Control
  BUY BPR Buyer -> [BPR]BPR0 =[E26]BUY (BPARTNER) !Other
  CADCRBDEV MD1 Cad. fund decr. to be posted act:CCN
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COMMENT1 DES Comment
  CPLDEDVAT MD1 Addit deduc tax
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E26]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E26]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DERRVEISS MD1 Book vs tax rev./disposal
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPM DPM Depreciation method
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EXCCUM MD1 Total excep. amt
  EXCDPR MD1 FYR except deprec
  FCY FCY Site -> [FCY]FCY0 =[E26]FCY (FACILITY) !Delete
  GAL MD1 +/- value
  GALREFBAS MD1 Ref basis+/- value
  GALREFDAT D4 Ref date +/- value
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other
  IML MD1 Impairment
  IMLBLC MD1 Impairment loss balance
  IMLRVE MD1 Impairment loss reversal
  IMLRVEISS MD1 Impair. rev./disposal
  ISSAMT MD1 Disposal amount
  ISSRATCUR RAT Currency rate
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  ISSVATAMT MD1 VAT due on disposal
  ISSVATRAT RAT Disposal VAT rate
  IVCSALISS A*20 Invoice reference
  IVCVATAMT MD1 VAT invoiced
  LIN C*4 Line number
  LNGGAL MD1 Long term +/- value
  NBV MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCADCRB MD1 Amort. fund decrease act:CCN
  PYBVATTYP M*15 VAT repayment [menu 3160: 1=1/5th rule,2=1/10th rule,3=1/20th rule,4=No VAT adjustment,5=Deductible VAT amount adjustment: increase,6=Deductible VAT amount adjustment: decrease]
  P_1CADCRB MD1 Decr. tot. P-1 act:CCN
  REF VC9 Reference
  REVVAT MD1 Add. VAT repay
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RSDVAL MD1 Residual value
  RVACRB MD1 Revaluation reversal
  SACACC A*10 Control
  SHOGAL MD1 Short term +/- value
  SIVTYP TSV(25) Customer invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Other
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  SORREG D4 Real disposal date
  SORREGI D4 Initial disposal date
  SORREGT D4 Theo disposal date
  TAX1 VAT Tax 1 -> [TVT]TVT0 =TAX1;[V]GSUPCLE (TABVAT) !Other
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Other
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Other
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Other
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Other
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Other
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TRFCADCUM MD1 Amortization fund act:CCN
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Other

## EFASLNKCNL (E36) - Evt - asset deletion
Notes: activity code LNK; differs in V10 P1 (diff: ATD_EFASLNKCNL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTEXEANT M*4 Reversal [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E36]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E36]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E36]FCY (FACILITY) !Delete
  LIN C*4 Line number
  LNKCUM MD1 Plan E-1 link total
  PSTLNK MD1 Posted variance
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASMTC (E27) - Evt - method change
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACLCOED RA1 Acceleration coeff.
  ACLCOEO RA1 Acceleration coeff.
  ALWCODD M*15 New part. rule [menu 3168: 19 values, see local-menus.md]
  ALWCODO M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E27]CPY (COMPANY) !Delete
  CRBVEHCODD ADI New reint ceiling -> [ADI]CODE =531;CRBVEHCODD (ATABDIV) !Other
  CRBVEHCODO ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCODO (ATABDIV) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E27]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DPMD DPM New mode
  DPMO DPM Depreciation method
  DPRDURD DUR New depr duration
  DPRDURO DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT2D RA1 New depr rate
  DPRRAT2O RA1 Depreciation rate
  DPRRATD RA1 New depr rate
  DPRRATO RA1 Depreciation rate
  ENDDPRDATD D4 Dep. end new date
  ENDDPRDATO D4 Deprec end date
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E27]FCY (FACILITY) !Delete
  LIN C*4 Line number
  MTCDEVADJ M*15 Rec. meth chge var [menu 3169: 1=Carryforward,2=Exceptional depre fiscal year,3=Exceptional depre period,4=Charge fiscal year,5=Charge period]
  PRATYPD M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  PRATYPO M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RSDVALD MD1 New salvage value
  RSDVALO MD1 Residual value
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  STRDPRDATD D4 New depr. start date
  STRDPRDATO D4 Depre start date
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASPLMDR (K33) - Evt - Improvement
Notes: activity code KPL; differs in V10 P1 (diff: ATD_EFASPLMDR.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODLEA CAC Acc code contract -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCODLEA;[V]GSUPCLE (GACCCODE) !Other act:LEA
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[K33]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[K33]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOT MD1 Entry value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[K33]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  KMDRDAT D4 Improvement date act:KPL
  KMDRDEV MD1 Improvement value act:KPL
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASREEVAL (E28) - Evt - revaluation
Notes: differs in V9.0 P12 (diff: AT3_EFASREEVAL.htm); differs in V10 P1 (diff: ATD_EFASREEVAL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E28]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E28]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPED MD1 Period P charge
  DPEO MD1 Period P charge
  DPM DPM Depreciation method
  DPRBASD MD1 Reval. BS value
  DPRBASO MD1 Reval. BS value
  DPRCUMD MD1 FY depre total
  DPRCUMFLG M*4 FYR forc deprec tot [menu 1: 1=No,2=Yes]
  DPRCUMFLGO M*4 FYR forc deprec tot [menu 1: 1=No,2=Yes]
  DPRCUMO MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  EXECLOCUMO MD1 Theo cumul clos FY
  EXECLOCUMT MD1 Theo cumul clos FY
  EXEIMLCUMD MD1 Cumulated exp. Y-1
  EXEIMLCUMO MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUMD MD1 Acc. impair. rev. FY-1
  EXERVECUMO MD1 Acc. impair. rev. FY-1
  EXETRFCUMD MD1 Depr rec transf FYR-1
  EXETRFCUMO MD1 Depr rec transf FYR-1
  FCY FCY Site -> [FCY]FCY0 =[E28]FCY (FACILITY) !Delete
  FIYSTRDAT D4 Fiscal year start date
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other act:IAS
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete act:IAS
  IMLRVELIM MD1 Reversal cap
  LIN C*4 Line number
  NBVD MD1 Net value
  NBVO MD1 Net value
  NSPVAL MD1 Market value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUMD MD1 Periodic total P-1
  PERCLOCUMO MD1 Periodic total P-1
  PERCLOCUMT MD1 Theo cumul clos per
  PERCLOEXCD MD1 Office P-1 amt excep.
  PERCLOEXCO MD1 Office P-1 amt excep.
  PERCLOEXCT MD1 Acc P-1 exc depr T
  PERIMLCUMD MD1 Depre total P-1
  PERIMLCUMO MD1 Depre total P-1
  PERREFCLC D4 Calculation period
  PERREFCLCT D4 Per. for T calculation
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUMD MD1 Acc. impair. rev. P-1
  PERRVECUMO MD1 Acc. impair. rev. P-1
  PERSTRDAT D4 Period start date
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  REF VC9 Reference
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RVAAMT MD1 Revaluation amount
  RVAAPR A*15 Evaluator
  RVACMT DCO Comment
  RVACOE COE Revaluation coef
  RVACRB MD1 Revaluation reversal
  RVACRBD MD1 Revaluation reversal
  RVADAT D4 Revaluation date
  RVADERRVE MD1 Imp loss rev on reval
  RVADEVCHG MD1 Reval. res. to loss
  RVATIADAT M*15 Reval. effective start [menu 3273: 1=FY start,2=Period start,3=FY end]
  RVATYP M*15 Revaluation type [menu 3253: 1=Coefficient,2=Index,3=Market value]
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASRNW (E31) - Evt- renewal
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCNCADDEV MD1 Amortization variance act:CCN
  CCNCADEXC MD1 Amortization excess act:CCN
  CCNTRFCAD MD1 Forwarded amortization act:CCN
  CCNTRFGRT MD1 Forwarded subsidy act:CCN
  CCNTRFRPR MD1 Forwarded provision act:CCN
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E31]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E31]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E31]FCY (FACILITY) !Delete
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  LIN C*4 Line number
  REF VC9 Reference
  RNWDAT D4 Renewal date act:CCN
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RNWVAL MD1 Renewal val. act:CCN
  RVERPRVAL MD1 Prov. to reverse act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASRNWCNL (E35) - Evt - asset deletion
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCNCADDEV MD1 Amortization variance act:CCN
  CCNCADEXC MD1 Amortization excess act:CCN
  CCNTRFCAD MD1 Forwarded amortization act:CCN
  CCNTRFGRT MD1 Forwarded subsidy act:CCN
  CCNTRFRPR MD1 Forwarded provision act:CCN
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E35]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E35]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E35]FCY (FACILITY) !Delete
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  LIN C*4 Line number
  REF VC9 Reference
  RNWDAT D4 Renewal date act:CCN
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RNWVAL MD1 Renewal val. act:CCN
  RVERPRVAL MD1 Prov. to reverse act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASRUCRT (K24) - Evt - asset creation
Notes: activity code KRU; differs in V10 P1 (diff: ATD_EFASRUCRT.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODLEA CAC Acc code contract -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCODLEA;[V]GSUPCLE (GACCCODE) !Other act:LEA
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[K24]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[K24]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOT MD1 Entry value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[K24]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  KBONUS MD1 Bonus act:KRU
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASRURST (K32) - Evt - restart depreciation
Notes: differs in V10 P1 (diff: ATD_EFASRURST.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODLEA CAC Acc code contract -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCODLEA;[V]GSUPCLE (GACCCODE) !Other act:LEA
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[K32]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[K32]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOT MD1 Entry value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[K32]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  KBONUS MD1 Bonus act:KRU
  KSTPDEPSTA M*4 Depreciation stop [menu 3289: 1=No stop,2=Improvement,3=Preservation,4=Stopped for improvement,5=Stopped for preservation,6=Restarted after improvement,7=Restarted after preservation,8=Suspend,9=Stopped,10=Restarted after extension,11=Restarted,12=Extension deprec,13=Suspended for extension]
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASRUSTP (K31) - Evt - stop depreciation
Notes: differs in V10 P1 (diff: ATD_EFASRUSTP.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  AASIPTDAT D4 Allocation date
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODLEA CAC Acc code contract -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCODLEA;[V]GSUPCLE (GACCCODE) !Other act:LEA
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[K31]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[K31]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  ETRNOT MD1 Entry value ex-tax
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[K31]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  KBONUS MD1 Bonus act:KRU
  KSTPDEPSTA M*4 Depreciation stop [menu 3289: 1=No stop,2=Improvement,3=Preservation,4=Stopped for improvement,5=Stopped for preservation,6=Restarted after improvement,7=Restarted after preservation,8=Suspend,9=Stopped,10=Restarted after extension,11=Restarted,12=Extension deprec,13=Suspended for extension]
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EFASVATREG (E29) - Evt - adjust. asset sales tax
Notes: differs in V10 P1 (diff: ATD_EFASVATREG.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  AASBUS VC9 Activity
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  AUUID AUUID Single identifier
  BASDEV MD1 Bal sheet val vari
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E29]CPY (COMPANY) !Delete
  CRBVAT MD1 VAT repayment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E29]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DEDVAT MD1 Add. VAT reduction
  DEDVATAMT MD1 VAT recovered
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E29]FCY (FACILITY) !Delete
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other act:IAS
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  IVCVATAMT MD1 VAT invoiced
  LIN C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  RATCUR RCU Currency rate
  REF VC9 Reference
  REGCOD C*1 VAT regul source
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount
  VATREGDAT D4 Reference date

## EGRTCASH (E61) - Evt - subsidy transfer
Notes: activity code GRT; differs in V10 P1 (diff: ATD_EGRTCASH.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGSUBV;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CASHAMT MD1 Collected amount
  CASHDAT D4 Collection date
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E61]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E61]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E61]FCY (FACILITY) !Delete
  GRAAMT MD1 Subsidy amount
  GRAORG ADI Organization -> [ADI]CODE =617;GRAORG (ATABDIV) !Other
  GRASTA MM*1 Status [menu 3225: 1=In process,2=Investment complete,3=Deleted,4=Totally reintegrated]
  GRATYP MM*25 Subsidy type [menu 3181: 1=Fixed rate,2=Percentage,3=Capped percentage]
  INVPLN ADI Project ref. -> [ADI]CODE =614;INVPLN (ATABDIV) !Other
  LIN C*4 Line number
  REF VC9 Reference
  REN A*15 Reason
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EGRTCNL (E64) - Evt - Subsidy deletion
Notes: activity code GRT; differs in V10 P1 (diff: ATD_EGRTCNL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGSUBV;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E64]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E64]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E64]FCY (FACILITY) !Delete
  LIN C*4 Line number
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EGRTCRB (E63) - Evt- subsidy reintegration
Notes: activity code GRT; differs in V10 P1 (diff: ATD_EGRTCRB.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGSUBV;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  APPROVDAT D4 Agreement date
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E63]CPY (COMPANY) !Delete
  CRBGRAAMT MD1 FYR reintegrated amount
  CRBGRACUM MD1 Reintegration total
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E63]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  CUTDAT D4 Update date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E63]FCY (FACILITY) !Delete
  GRAAMT MD1 Subsidy amount
  GRAORG ADI Organization -> [ADI]CODE =617;GRAORG (ATABDIV) !Other
  GRASTA MM*1 Status [menu 3225: 1=In process,2=Investment complete,3=Deleted,4=Totally reintegrated]
  GRATYP MM*25 Subsidy type [menu 3181: 1=Fixed rate,2=Percentage,3=Capped percentage]
  INVGRAAMT MD1 FA subsidy amt
  INVGRARAT RAT Subsidised inv %
  INVPLN ADI Invest project -> [ADI]CODE =614;INVPLN (ATABDIV) !Other
  LIN C*4 Line number
  MAXGRAAMT MD1 Subsidy cap
  REAGRAAMT MD1 Act investment amt
  REF VC9 Reference
  REN A*15 Reason
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EGRTCRT (E62) - Evt - subsidy creation
Notes: activity code GRT; differs in V10 P1 (diff: ATD_EGRTCRT.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGSUBV;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  APPROVDAT D4 Agreement date
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E62]CPY (COMPANY) !Delete
  CRBGRAAMT MD1 FYR reintegrated amount
  CRBGRACUM MD1 Reintegration total
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E62]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  CUTDAT D4 Update date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E62]FCY (FACILITY) !Delete
  GRAAMT MD1 Subsidy amount
  GRAORG ADI Organization -> [ADI]CODE =617;GRAORG (ATABDIV) !Other
  GRASTA MM*1 Status [menu 3225: 1=In process,2=Investment complete,3=Deleted,4=Totally reintegrated]
  GRATYP MM*25 Subsidy type [menu 3181: 1=Fixed rate,2=Percentage,3=Capped percentage]
  INVGRAAMT MD1 FA subsidy amt
  INVGRARAT RAT Subsidised inv %
  INVPLN ADI Invest project -> [ADI]CODE =614;INVPLN (ATABDIV) !Other
  LIN C*4 Line number
  MAXGRAAMT MD1 Subsidy cap
  REAGRAAMT MD1 Act investment amt
  REF VC9 Reference
  REN A*15 Reason
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEAACTU (E41) - Evt - contract actualization
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEAACTU.htm); differs in V10 P1 (diff: ATD_ELEAACTU.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E41]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E41]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  CUTDAT D4 Update date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ENDLEADATN D4 Contrct end date
  ENDLEADATO D4 Contrct end date
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E41]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Incremental borrowing rate
  IMPLEARAT RAT Implied interest rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LEAAMTN MD1 Capital amount
  LEAAMTO MD1 Capital amount
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E41]LEACUR (TABCUR) !Other
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[E41]LES (BPARTNER) !Other
  LIN C*4 Line number
  LSTPRECN MD1 Last present value
  LSTPRECO MD1 Last present value
  LSTPREIN MD1 Last present value
  LSTPREIO MD1 Last present value
  LSTPREN MD1 Last present value
  LSTPREO MD1 Last present value
  LSTROUCN MD1 Current right of use
  LSTROUCO MD1 Current right of use
  LSTROUIN MD1 Current right of use
  LSTROUIO MD1 Current right of use
  LSTROUN MD1 Current right of use
  LSTROUO MD1 Current right of use
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  RPUDATN D4 Option exercise date
  RPUDATO D4 Option exercise date
  RPUVALN MD1 Scrap value
  RPUVALO MD1 Scrap value
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEACNL (E47) - Evt - contract deletion
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEACNL.htm); differs in V10 P1 (diff: ATD_ELEACNL.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E47]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E47]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E47]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Incremental borrowing rate
  IMPLEARAT RAT Implied interest rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LIN C*4 Line number
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEACRT (E42) - Evt - contract creation
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEACRT.htm); differs in V10 P1 (diff: ATD_ELEACRT.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BEFRNT MD1 Advance rent
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E42]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E42]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ENDLEADAT D4 Contrct end date
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E42]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Incremental borrowing rate
  IMPLEARAT RAT Implied interest rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LEAAMT MD1 Capital amount
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E42]LEACUR (TABCUR) !Other
  LEAEXS MD1 Application fees
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEARAT RAT Interest rate
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[E42]LES (BPARTNER) !Other
  LIN C*4 Line number
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  RPUVAL MD1 Scrap value
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  STRLEADAT D4 Contrct start date
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEAEND (E43) - Evt - end of contract
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEAEND.htm); differs in V10 P1 (diff: ATD_ELEAEND.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E43]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E43]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  ENDLEADAT D4 Contrct end date
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E43]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Incremental borrowing rate
  IMPLEARAT RAT Implied interest rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E43]LEACUR (TABCUR) !Other
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[E43]LES (BPARTNER) !Other
  LIN C*4 Line number
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEAPAY (E44) - Evt - contract fee
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEAPAY.htm); differs in V10 P1 (diff: ATD_ELEAPAY.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+FSTMTHDAT+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E44]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E44]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E44]FCY (FACILITY) !Delete
  FSTMTHDAT D4
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E44]LEACUR (TABCUR) !Other
  LEAINTAMT MD1 Financial costs
  LEAINTAMTN MD1 Expensed end month m
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEAPAYAMT MD1 Rental amount
  LEAPAYAMTM MD1 Fee month m
  LEAPRIAMT MD1 Financial deprec
  LEAPRIAMTM MD1 Depr. end month m
  LEAPUROPT MD1 Purchase option price
  LEAPUROPTM MD1 Purchase option price
  LEARSDVAL MD1 Resid. val. guarantee
  LEARSDVALM MD1 Resid. val. guarantee
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATERPEN MD1 Penalties
  LEATERPENM MD1 Penalties
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LEAVARPAY MD1 Variable payments
  LEAVARPAYM MD1 Variable payments
  LES BPR Lessor -> [BPR]BPR0 =[E44]LES (BPARTNER) !Other
  LIN C*4 Line number
  PAYENDDAT D4 Open item end
  PAYSTRDAT D4 Due date start
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEARPU (E45) - Evt - purchase option exercise
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEARPU.htm); differs in V10 P1 (diff: ATD_ELEARPU.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E45]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E45]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E45]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Marginal int. rate
  IMPLEARAT RAT Implied int. rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E45]LEACUR (TABCUR) !Other
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[E45]LES (BPARTNER) !Other
  LIN C*4 Line number
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  RPUDAT D4 Option exercise date
  RPUVAL MD1 Scrap value
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELEATRM (E46) - Evt - contract termination
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_ELEATRM.htm); differs in V10 P1 (diff: ATD_ELEATRM.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E46]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E46]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E46]FCY (FACILITY) !Delete
  ICRBRWRAT RAT Marginal int. rate
  IMPLEARAT RAT Implied int. rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  LEACUR CUR Funding currency -> [TCU]TCU0 =[E46]LEACUR (TABCUR) !Other
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[E46]LES (BPARTNER) !Other
  LIN C*4 Line number
  REF VC9 Reference
  RESCOS MD1 Restoration cost
  RMNTPA MD1 Remaining for reimbursement
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TRMLEADAT D4 Termination date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELOFCIM (E01) - Evt - modify expense account
Notes: differs in V10 P1 (diff: ATD_ELOFCIM.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  ACT VC9 Activity
  AMTNOTCPY MD1 Amount - tax
  AMTNOTCUR MD1 Amount - tax
  AMTVATCPY MD1 Tax amount
  AMTVATCUR MD1 Tax amount
  AMTVATRCPY MD1 VAT recovered
  AMTVATRCUR MD1 Recvd VAT
  AUUID AUUID Single identifier
  BPR BPR Supplier -> [BPR]BPR0 =[E01]BPR (BPARTNER) !Other
  BPRVCR A*20 Invoice reference
  CCE10D CCE Dimension -> [CCE]CCE0 =DIE10;CCE10D (CACCE) !Other
  CCE10O CCE Dimension -> [CCE]CCE0 =DIE10;CCE10O (CACCE) !Other
  CCE11D CCE Dimension -> [CCE]CCE0 =DIE11;CCE11D (CACCE) !Other
  CCE11O CCE Dimension -> [CCE]CCE0 =DIE11;CCE11O (CACCE) !Other
  CCE12D CCE Dimension -> [CCE]CCE0 =DIE12;CCE12D (CACCE) !Other
  CCE12O CCE Dimension -> [CCE]CCE0 =DIE12;CCE12O (CACCE) !Other
  CCE13D CCE Dimension -> [CCE]CCE0 =DIE13;CCE13D (CACCE) !Other
  CCE13O CCE Dimension -> [CCE]CCE0 =DIE13;CCE13O (CACCE) !Other
  CCE14D CCE Dimension -> [CCE]CCE0 =DIE14;CCE14D (CACCE) !Other
  CCE14O CCE Dimension -> [CCE]CCE0 =DIE14;CCE14O (CACCE) !Other
  CCE15D CCE Dimension -> [CCE]CCE0 =DIE15;CCE15D (CACCE) !Other
  CCE15O CCE Dimension -> [CCE]CCE0 =DIE15;CCE15O (CACCE) !Other
  CCE16D CCE Dimension -> [CCE]CCE0 =DIE16;CCE16D (CACCE) !Other
  CCE16O CCE Dimension -> [CCE]CCE0 =DIE16;CCE16O (CACCE) !Other
  CCE17D CCE Dimension -> [CCE]CCE0 =DIE17;CCE17D (CACCE) !Other
  CCE17O CCE Dimension -> [CCE]CCE0 =DIE17;CCE17O (CACCE) !Other
  CCE18D CCE Dimension -> [CCE]CCE0 =DIE18;CCE18D (CACCE) !Other
  CCE18O CCE Dimension -> [CCE]CCE0 =DIE18;CCE18O (CACCE) !Other
  CCE19D CCE Dimension -> [CCE]CCE0 =DIE19;CCE19D (CACCE) !Other
  CCE19O CCE Dimension -> [CCE]CCE0 =DIE19;CCE19O (CACCE) !Other
  CCE1D CCE Dimension -> [CCE]CCE0 =DIE1;CCE1D (CACCE) !Other
  CCE1O CCE Dimension -> [CCE]CCE0 =DIE1;CCE1O (CACCE) !Other
  CCE20D CCE Dimension -> [CCE]CCE0 =DIE20;CCE20D (CACCE) !Other
  CCE20O CCE Dimension -> [CCE]CCE0 =DIE20;CCE20O (CACCE) !Other
  CCE2D CCE Dimension -> [CCE]CCE0 =DIE2;CCE2D (CACCE) !Other
  CCE2O CCE Dimension -> [CCE]CCE0 =DIE2;CCE2O (CACCE) !Other
  CCE3D CCE Dimension -> [CCE]CCE0 =DIE3;CCE3D (CACCE) !Other
  CCE3O CCE Dimension -> [CCE]CCE0 =DIE3;CCE3O (CACCE) !Other
  CCE4D CCE Dimension -> [CCE]CCE0 =DIE4;CCE4D (CACCE) !Other
  CCE4O CCE Dimension -> [CCE]CCE0 =DIE4;CCE4O (CACCE) !Other
  CCE5D CCE Dimension -> [CCE]CCE0 =DIE5;CCE5D (CACCE) !Other
  CCE5O CCE Dimension -> [CCE]CCE0 =DIE5;CCE5O (CACCE) !Other
  CCE6D CCE Dimension -> [CCE]CCE0 =DIE6;CCE6D (CACCE) !Other
  CCE6O CCE Dimension -> [CCE]CCE0 =DIE6;CCE6O (CACCE) !Other
  CCE7D CCE Dimension -> [CCE]CCE0 =DIE7;CCE7D (CACCE) !Other
  CCE7O CCE Dimension -> [CCE]CCE0 =DIE7;CCE7O (CACCE) !Other
  CCE8D CCE Dimension -> [CCE]CCE0 =DIE8;CCE8D (CACCE) !Other
  CCE8O CCE Dimension -> [CCE]CCE0 =DIE8;CCE8O (CACCE) !Other
  CCE9D CCE Dimension -> [CCE]CCE0 =DIE9;CCE9D (CACCE) !Other
  CCE9O CCE Dimension -> [CCE]CCE0 =DIE9;CCE9O (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E01]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E01]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DATIMP D4 Allocation date
  DATVCR D4 Invoice date
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPD DSP New allocation -> [DSP]DSP0 =DSPD;1 (CADSP) !Delete
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E01]FCY (FACILITY) !Delete
  GACACND M*15 Type [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACACNO M*15 Type [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACD GAC Account -> [GAC]GAC0 ="";GACD (GACCOUNT) !Other
  GACO GAC Account -> [GAC]GAC0 ="";GACO (GACCOUNT) !Other
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other act:IAS
  JOU JOU Journal -> [JOU]JOU0 =[E01]JOU (GJOURNAL) !Other
  LIN C*4 Line number
  ORDBUY A*20 Order reference
  QTY QTY Quantity
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  TYPVCR M*15 Invoice type [menu 3117: 1=Invoice,2=Credit note,3=Pre-payment,4=To be received,5=Return,6=Early discount/late charge,7=Stock issue]
  UOM UOM Unit -> [TUN]TUN0 =[E01]UOM (TABUNIT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRDEN AUS Destination -> [AUS]CODUSR =[E01]USRDEN (AUTILIS) !Other
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELOFCNL (E03) - Evt - expense deletion
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E03]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E03]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E03]FCY (FACILITY) !Delete
  LIN C*4 Line number
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ELOFVATREG (E02) - Evt - sales tax adjust expense
Notes: differs in V10 P1 (diff: ATD_ELOFVATREG.htm)
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACGGRP FAM Acct group -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  ACT VC9 Activity
  ADMCOE RAT Admission coef.
  AMTVATCPY MD1 Tax amount
  AMTVATRCPY MD1 VAT recovered
  ASJCOE RAT Liability coef.
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Other
  CCE10 CCE Dimension -> [CCE]CCE0 =DIE10;CCE10 (CACCE) !Other
  CCE11 CCE Dimension -> [CCE]CCE0 =DIE11;CCE11 (CACCE) !Other
  CCE12 CCE Dimension -> [CCE]CCE0 =DIE12;CCE12 (CACCE) !Other
  CCE13 CCE Dimension -> [CCE]CCE0 =DIE13;CCE13 (CACCE) !Other
  CCE14 CCE Dimension -> [CCE]CCE0 =DIE14;CCE14 (CACCE) !Other
  CCE15 CCE Dimension -> [CCE]CCE0 =DIE15;CCE15 (CACCE) !Other
  CCE16 CCE Dimension -> [CCE]CCE0 =DIE16;CCE16 (CACCE) !Other
  CCE17 CCE Dimension -> [CCE]CCE0 =DIE17;CCE17 (CACCE) !Other
  CCE18 CCE Dimension -> [CCE]CCE0 =DIE18;CCE18 (CACCE) !Other
  CCE19 CCE Dimension -> [CCE]CCE0 =DIE19;CCE19 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Other
  CCE20 CCE Dimension -> [CCE]CCE0 =DIE20;CCE20 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Other
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E02]CPY (COMPANY) !Delete
  CRBVAT MD1 VAT repayment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E02]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DATIMP D4 Allocation date
  DATVCR D4 Invoice date
  DEDVAT MD1 Add. VAT reduction
  DES DCO Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =DIE1 (GDIE) !Other
  DIE10 DIE Dimension type code -> [DIE]DIE0 =DIE10 (GDIE) !Other
  DIE11 DIE Dimension type code -> [DIE]DIE0 =DIE11 (GDIE) !Other
  DIE12 DIE Dimension type code -> [DIE]DIE0 =DIE12 (GDIE) !Other
  DIE13 DIE Dimension type code -> [DIE]DIE0 =DIE13 (GDIE) !Other
  DIE14 DIE Dimension type code -> [DIE]DIE0 =DIE14 (GDIE) !Other
  DIE15 DIE Dimension type code -> [DIE]DIE0 =DIE15 (GDIE) !Other
  DIE16 DIE Dimension type code -> [DIE]DIE0 =DIE16 (GDIE) !Other
  DIE17 DIE Dimension type code -> [DIE]DIE0 =DIE17 (GDIE) !Other
  DIE18 DIE Dimension type code -> [DIE]DIE0 =DIE18 (GDIE) !Other
  DIE19 DIE Dimension type code -> [DIE]DIE0 =DIE19 (GDIE) !Other
  DIE2 DIE Dimension type code -> [DIE]DIE0 =DIE2 (GDIE) !Other
  DIE20 DIE Dimension type code -> [DIE]DIE0 =DIE20 (GDIE) !Other
  DIE3 DIE Dimension type code -> [DIE]DIE0 =DIE3 (GDIE) !Other
  DIE4 DIE Dimension type code -> [DIE]DIE0 =DIE4 (GDIE) !Other
  DIE5 DIE Dimension type code -> [DIE]DIE0 =DIE5 (GDIE) !Other
  DIE6 DIE Dimension type code -> [DIE]DIE0 =DIE6 (GDIE) !Other
  DIE7 DIE Dimension type code -> [DIE]DIE0 =DIE7 (GDIE) !Other
  DIE8 DIE Dimension type code -> [DIE]DIE0 =DIE8 (GDIE) !Other
  DIE9 DIE Dimension type code -> [DIE]DIE0 =DIE9 (GDIE) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E02]FCY (FACILITY) !Delete
  GAC GAC Account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 Type [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other
  LIN C*4 Line number
  RATCUR RCU Currency rate
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TAXCOE RAT Taxation coeff
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EMODELE (E00) - Evt - template table
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*15 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E00]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E00]CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E00]FCY (FACILITY) !Delete
  LIN C*4 Line number
  REF VC9 Reference
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EPHYAFFGEO (E82) - Evt - Phys. asset geo transfer
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D); EVE3 REF+EVTDAT (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E82]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E82]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E82]FCY (FACILITY) !Delete
  LASTDATTRF D4 Date latest trans
  LCTCODD LCT Dest. location -> [LCT]LCT0 =[E82]LCTCODD (PHYLCT) !Other
  LCTCODO LCT Source location -> [LCT]LCT0 =[E82]LCTCODO (PHYLCT) !Other
  LIN C*4 Line number
  MVTDAT D4 Movement date
  REF VC9 Reference
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  REN ADI Tansfer reason -> [ADI]CODE =612;REN (ATABDIV) !Other
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EPHYCRT (E81) - Evt - Physical asset creation
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E81]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =CUR (TABCUR) !Block
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E81]FCY (FACILITY) !Delete
  LCTCOD LCT Location -> [LCT]LCT0 =[E81]LCTCOD (PHYLCT) !BSRA
  LIN C*4 Line number
  MVTDAT D4 Movement date
  REF VC9 Reference
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  REN ADI Reason -> [ADI]CODE =612;REN (ATABDIV) !Block
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## EPHYISS (E83) - Evt - Physical asset disposal
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): EVE0 REF+TIMSTP; EVE1 REF+TIMSTPO+TIMSTP; EVE2 CPTFLG+DPRPLN+CPY+FCY+REF (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPTDATINT D4 TRT accounting date
  CPTDATINTO D4 Src accountg TRT date
  CPTEVT M*4 Can be posted [menu 1: 1=No,2=Yes]
  CPTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CPY CPY Company -> [CPY]CPY0 =[E83]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CREUSRO A*5 Srce creatn operator
  CUR CUR Currency -> [TCU]TCU0 =[E83]CUR (TABCUR) !Other
  CURPERSTR D4 Period start date
  DES DCO Description
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVTDAT D4 Effective date
  EVTINT A*10 Internal code
  FCY FCY Site -> [FCY]FCY0 =[E83]FCY (FACILITY) !Delete
  ISSTYP M*15 Disposal reason [menu 3175: 1=Not disposed,2=Stock count issue,3=Sale,4=Scrap,5=Theft or disappearance]
  LCTCOD LCT Location -> [LCT]LCT0 =[E83]LCTCOD (PHYLCT) !BSRA
  LIN C*4 Line number
  MVTDAT D4 Movement date
  REF VC9 Reference
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  SNSCPT C*1 Sign
  SNSEVE M*15 Event type [menu 3109: 1=Action,2=Action cancellation]
  TIMSTP A*20 Time stamp
  TIMSTPO A*20 Sce timestamp
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USRFLDA1 A*20 Free field 1
  USRFLDA10 A*20 Free field 10
  USRFLDA2 A*20 Free field 2
  USRFLDA3 A*20 Free field 3
  USRFLDA4 A*20 Free field 4
  USRFLDA5 A*20 Free field 5
  USRFLDA6 A*20 Free field 6
  USRFLDA7 A*20 Free field 7
  USRFLDA8 A*20 Free field 8
  USRFLDA9 A*20 Free field 9
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## FASFAM (FAM) - Asset groups
Keys (first = PK; D = duplicates allowed): FAM0 FAMREF
Fields:
  AUUID AUUID Single identifier
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FAMDES AXX Description
  FAMREF FAM Family code -> [FAM]FAM0 =[FAM]FAMREF (FASFAM) !BSRA
  GFY AGC Group of company -> [AGF]AGF0 =[FAM]GFY (AGRPFCY) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SHODES AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FISCYEAR (FIS) - Fiscal year
Keys (first = PK; D = duplicates allowed): FIY0 CPY+CNX+DATSTRFIY; FIY1 CPY+CNX+STAFIY (D); FIY2 CPY+CNX+DATENDFIY
Fields:
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[FIS]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FIS]CREUSR (AUTILIS) !Other
  DATENDFIY D4 FY end date
  DATENDPER D4(24) Period end date
  DATSTRFIY D4 FY start date
  DATSTRPER D4(24) Period start
  DFDCOD M*30 Deferred rule [menu 3239: 1=None,2=Percentage,3=No book vs tax deferred depreciation,4=Reversal on residual duration]
  DFDRAT RAT Deferred rate
  DFDTYP M*15 Deferred type [menu 3232: 1=None,2=Loss-making deferred depreciation,3=Profit-making deferred depreciation,4=Deferred depreciation reversal,5=2013 2014 deferred]
  EVTCREFLG M*4 Generated events [menu 1: 1=No,2=Yes]
  INDCURPER C*4 Current period
  LSTTYPPRO M*4(24) Temp-->final acc [menu 1: 1=No,2=Yes]
  LVALIM MD1 LVA threshold
  LVATYP M*15 LVA management [menu 3297: 1=None,2=LVA,3=Pool]
  NBRDAYPER C*4(24) Number of days
  NBRMONPER C*4(24) Number of months
  NBRPER C*4 Number of periods
  NBRWEKPER C*4(24) Number weeks
  RAT39BIS RAT 39bis temp rate
  STAFIY M*15 FY status [menu 3102: 1=Closed,2=Current,3=Next,4=Next +1]
  STAPER M*15(24) Period status [menu 3161: 1=Not open,2=Current,3=Open,4=Closed]
  TYPPST M*15(24) Posting type [menu 3211: 1=Actual,2=Simulation]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FIS]UPDUSR (AUTILIS) !Other

## FREFLD (FRF) - Free fields
Keys (first = PK; D = duplicates allowed): FRF0 OBJ+CPY
Fields:
  ABRMSK A*4 Screen abbreviation
  ALPDES AX2(10) Alpha title field
  ALPREF C*4(10) Reference table
  AMTCUR M*10(6) Amt currency field [menu 3123: 1=Company,2=Object]
  AMTDES AX2(6) Amount title
  AMTRIOIND M*4(6) Prorata/split [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[FRF]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATDES AX2(4) Date field description
  EXPNUM L*8 Export number
  OBJ M*15 Object [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  RATDES AX2(2) Coeff. field title
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FXBLOB (FBB) - Special folders
Keys (first = PK; D = duplicates allowed): ABB0 CODBLB+IDENT1+IDENT2+IDENT3
Fields:
  AUUID AUUID Single identifier
  BLOB ABB Image file
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CODBLB A*10 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[FBB]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  NAMBLB DES File name
  TYPBLB AT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FBB]UPDUSR (AUTILIS) !Other

## FXDASSETS (FAS) - Assets
Keys (first = PK; D = duplicates allowed): FAS0 AASREF; FAS1 CPY+AASREF; FAS2 CPY+FCY+AASREF; FAS3 SET (D); FAS5 CMP (D); FAS4 PROPLN+AASREF (D); FAS7 CPY+ENAFAS (D); FAS8 CCNREF+RNWDAT+AASREF; FAS9 CCNACTCOD+CPY+AASREF; FAS10 KPSEPLN+CPY+AASREF; FAS11 CMPSTA+AASREF; FAS12 LEAREF (D)
Fields:
  AASBUS VC9 Activity
  AASCND ADI Report -> [ADI]CODE =511;AASCND (ATABDIV) !Block
  AASDES1 DCO Description
  AASDES2 DCO Description 2
  AASIPTDAT D4 Allocation date
  AASORINBV MD1 NV IGS source asset
  AASQTY QTY Quantity
  AASREF FAS Asset -> [FAS]FAS0 =[FAS]AASREF (FXDASSETS) !Other
  AASREFORI A*20 Original reference
  AASRPB A*15 Supervisor
  AASTYP M*15 Type [menu 3151: 1=Tangible,2=Intangible,3=Goodwill,4=Financial,5=Investment properties,6=Biological assets]
  AASUOM UOM Unit -> [TUN]TUN0 =[FAS]AASUOM (TABUNIT) !Block
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACGCPLDED MD1 Add deduc VAT CoA
  ACGCUR CUR CoA curr. -> [TCU]TCU0 =[FAS]ACGCUR (TABCUR) !Block
  ACGETRNOT MD1 Receipt value ex-tax
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGREVVAT MD1 CoA VAT repayment
  ADMCOE RAT Admission coef.
  ADMCOEF RAT Admission coef.
  ADMCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  ADMCOER RAT Admission coef.
  APRDAT D4 Valuation date
  ASJCOE RAT Liability coef.
  ASJCOEF RAT Liability coef.
  ASJCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  ASJCOER RAT Liability coef.
  AUUID AUUID Single identifier
  BPR BPR Supplier -> [BPR]BPR0 =[FAS]BPR (BPARTNER) !Block
  BUDFIY C*4 Budget FY
  BUDREF ADI Budget reference -> [ADI]CODE =615;BUDREF (ATABDIV) !Block
  BUY BPR Buyer -> [BPR]BPR0 =[FAS]BUY (BPARTNER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCNAASTYP M*4 Asset type [menu 3285: 1=Out-of-network,2=Networked] act:CCN
  CCNACTCOD CCA Update code act:CCN
  CCNCADDEV MD1 Amortization variance act:CCN
  CCNCADEXC MD1 Amortization excess act:CCN
  CCNETRNAT M*4 Contrib. origin [menu 3287: 1=Grantor,2=Grantee] act:CCN
  CCNETRTYP M*4 Contrib. type [menu 3286: 1=1st concession asset,2=Renewal] act:CCN
  CCNINICUM MD1 Initial fund act:CCN
  CCNREF CCN Concession contract -> [CCN]CCN0 =[FAS]CCNREF (CONCESSION) !Block act:CCN
  CCNTRFCAD MD1 Forwarded amortization act:CCN
  CCNTRFCUM MD1 Forwarded funds act:CCN
  CCNTRFGRT MD1 Forwarded subsidy act:CCN
  CCNTRFRPR MD1 Forwarded provision act:CCN
  CIGCOD A*10 IGS reference
  CMP AAS Main -> [FAS]FAS0 =[FAS]CMP (FXDASSETS) !Other
  CMPORI AAS Main source -> [FAS]FAS0 =[FAS]CMPORI (FXDASSETS) !Block
  CMPSTA M*15 Status [menu 3229: 1=Autonomous,2=Principal,3=Component,4=Component waiting assignment,5=Pool,6=LVA]
  CONNUM ADI Market no -> [ADI]CODE =620;CONNUM (ATABDIV) !Block
  CPY CPY Company -> [CPY]CPY0 =[FAS]CPY (COMPANY) !Delete
  CRBGRAAMT MD1 Reintegrtd amount
  CRBGRACUM MD1 Reintegration total
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR A*5 Creation user
  CWKTYP ADI Bodywork type -> [ADI]CODE =535;CWKTYP (ATABDIV) !Block
  DATISSPST D4 Issue date
  DEDCOE RAT Deduction coef
  DEDCOEF RAT Deduction coef
  DEDCOER RAT Deduction coef
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DEDVATFLG MZS*4 Forced rec VAT
  DEDVATFLGI MZS*4 Forced rec VAT
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  DERRVEISS MD1 Book vs tax rev./disposal
  DIE DIE Dimension type code -> [DIE]DIE0 =[FAS]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENAFAS M*4 Active [menu 1: 1=No,2=Yes]
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  EXPDAT D4 Usage limit
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  EXTSALAMT MD1 Expected sale amount
  FCY FCY Financial site -> [FCY]FCY0 =[FAS]FCY (FACILITY) !Block
  FIRICIDAT D4 1st use date
  FISOPETYP M*15 IGS fisc rule [menu 3163: 1=Favorable rule,2=Ordinary rule,3=Others]
  FLGCLC M*4 Asset to calculate [menu 1: 1=No,2=Yes]
  FLGCNXCLC M*4(11) Context to calculate [menu 3281: 1=No,2=Yes,3=Yes after closing]
  FLGCNXFLX A*11 Generated flows
  FLGPRV M*4 Legacy asset [menu 1: 1=No,2=Yes]
  FLGRPRCLC M*4 Provision to calculate [menu 1: 1=No,2=Yes] act:CCN
  FLGSPL M*4 Split [menu 1: 1=No,2=Yes]
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  FUEL M*4 Fuel type [menu 3167: 1=Fuel and similar products,2=Diesel and similar products,3=Electric,4=Other]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GAL MD1(15) +/- value
  GALINIAMT MD1 Initial amt +/- value
  GALREFBAS MD1 Ref basis+/- value
  GALREFDAT D4 Ref date +/- value
  GEOFCY FCY Geographic site -> [FCY]FCY0 =[FAS]GEOFCY (FACILITY) !Other
  GRAAMT MD1 Subsidy amount
  GRUEFFDAT D4 Oper. effect. date
  GRUINIAAS A*20 IGS initial asset ref
  GRUINICPY CPY IGS initial company -> [CPY]CPY0 =[FAS]GRUINICPY (COMPANY) !Other
  GRUISSREF A*41 Intra-grp sale ref
  GRUORIAAS A*20 IGS source asset
  GRUORICPY CPY IGS source company -> [CPY]CPY0 =[FAS]GRUORICPY (COMPANY) !Block
  GRUTAXBAS MD1 IGS tax basis
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Block
  IASCPLDED MD1 IAS/IFRS add ded VAT
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[FAS]IASCUR (TABCUR) !Block
  IASCURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  IASETRNOT MD1 Receipt value ex-tax
  IASRATCUR RCU Currency rate
  IASREGCUM MD1 VAT adj total
  IASREVVAT MD1 IFRS VAT repayment
  IASVATREG MD1 IAS/IFRS VAT adj
  IMLRVEISS MD1(15) Impair. rev./disposal
  INIDEDVAT RAT Initial VAT rate
  INVPLN ADI Project ref. -> [ADI]CODE =614;INVPLN (ATABDIV) !Block
  INVREQ ADI Invest request -> [ADI]CODE =616;INVREQ (ATABDIV) !Block
  INVTYP ADI Investment type -> [ADI]CODE =515;INVTYP (ATABDIV) !Other
  ISRCLCBAS M*15 Calculation basis [menu 3154: 1=Professional tax basis,2=Reference basis +/- value,3=CoA receipt value,4=CoA balance sheet value]
  ISRCONREF A*20 Contract ref
  ISRTYP M*15 Insurance type [menu 3153: 1=Not insured,2=Other insurance,3=Building insurance]
  ISRVAL MD1 Insurance value
  ISRVALCOE COE Asset insurance disc coeff
  ISRVALFLG MZS*4 Forcd ins val
  ISSAMT MD1(15) Disposal amount
  ISSDAT D4 Issue date
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  ISSFIYPRE M*4 Prev FYR disposal [menu 1: 1=No,2=Yes]
  ISSOPETYP M*15 IGS operation type [menu 3172: 1=Partial transfer of assets,2=Merger,3=Split,4=Intra-group sales]
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  ISSVATAMT MD1 VAT due on disposal
  ISSVATFLG MZS*4 Forced disposal VAT
  ISSVATRAT RAT Disposal VAT rate
  ISSVATTRF MD1 Transferable VAT
  ISSVATTRFI MD1 Transferable VAT
  ITSDAT D4 In service date
  IVCSALISS A*20 Invoice reference
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  IVCVATFLG MZS*4 Invoiced VAT forced
  IVCVATFLGI MZS*4 Invoiced VAT forced
  IVCVATRAT RAT Invd VAT rate
  IVCVATRATI RAT Invd VAT rate
  KANOREAV L*4(10) Revaluation year act:KPO
  KANOUTIL L*3(10) Expected useful years act:KPO
  KAREAV DCB*9.2(10) Reval. deprec. total act:KPO
  KBONUS MD1 Bonus act:KRU
  KCOEF DCB*3.4(10) Reval. coefficient act:KPO
  KPSEPLN PSE Seasonality plan act:PSE
  KSESFLG A*15 Seasonality flag act:PSE
  KVREAV DCB*9.2(10) Revalued value act:KPO
  LEAREF LEA Lse contract ref. -> [LEA]LEA0 =[FAS]LEAREF (LEASE) !RTZ act:LEA
  LEAREFORI LEA Src lease ct -> [LEA]LEA0 =[FAS]LEAREFORI (LEASE) !Other act:LEA
  LNGGAL MD1(15) Long term +/- value
  LOC A*38 Location
  NPL A*15 Registration no.
  OBYRNWCON M*4 CRO flag [menu 1: 1=No,2=Yes] act:CCN
  ORDLIG C*4 Order line
  ORDREF A*20 Order ref
  ORIPURAMT MD1 IGS src asst purc amt
  ORIPURDAT D4 IGS asset purch date
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PROPLN VC9 Production plan
  PURDAT D4 Purchase date
  PURNAT M*15 Purch nature [menu 3152: 1=New,2=Second-hand]
  PYBVATTYP M*15 VAT repayment [menu 3160: 1=1/5th rule,2=1/10th rule,3=1/20th rule,4=No VAT adjustment,5=Deductible VAT amount adjustment: increase,6=Deductible VAT amount adjustment: decrease]
  R76COE COE Reval. coeff. 76
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  RGNDAT D4 Registration date
  RNTDAYDUR L*8 Rent dur. days
  RNTENDDAT D4 Lease end
  RNTMONDUR DCB*6.3 Rent dur. months
  RNTSTRDAT D4 Lease start
  RNWAASREF VC9 Renewal asset act:CCN
  RNWDAT D4 Renewal date act:CCN
  RNWDATFLG M*4 Forced renewal date [menu 1: 1=No,2=Yes] act:CCN
  RNWDONFLG M*4 Renewal carried out [menu 1: 1=No,2=Yes] act:CCN
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RNWVAL MD1 Renewal val. act:CCN
  RNWVALFLG MZS*4 Replacement amt end act:CCN
  RPLVAL MD1 New value
  RPLVALCOE COE New value coeff
  RPLVALFLG MZS*4 New val
  RVAAPR ADI Evaluator -> [ADI]CODE =627;RVAAPR (ATABDIV) !Block
  RVACMT DCO Comment
  RVERPRVAL MD1 Prov. to reverse act:CCN
  SALCLSDAT D4 Asset date for sale
  SET A*20 Group No
  SHOGAL MD1(15) Short term +/- value
  SRLNBR SRL Serial number
  STABILTYP M*15 Stability type [menu 3156: 1=Fixed,2=General installation,3=Mobile]
  TAXBAS MD1 Tax basis
  TAXCOE RAT Taxation coeff
  TAXCOEF RAT Taxation coeff
  TAXCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TAXCOER RAT Taxation coeff
  TAXPLI M Taxation rate [menu 3164: 1=Full rate,2=50% exempt,3=Total exemption]
  TAXTYP M*15 Tax type [menu 3158: 1=BNPTF,2=BPTF,3=Ex-field]
  THESLI DUR Theo holding duratn
  TPAFLG M*4 Remittance with payment [menu 1: 1=No,2=Yes] act:CCN
  TRFDAT D4 Last transfer
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount
  VATREGAMT MD1 VAT repay adjust. - CoA
  VATREGCUM MD1 VAT adj total
  VATREGDAT D4 Reference date
  VATREGDED MD1 Deduct. VAT adjust - CoA
  VATREGDEDI MD1 Deduct VAT adjust - IAS
  VATRSD DUR Residual duration
  VATYEAFLG M*4 Yearly adjust. index [menu 1: 1=No,2=Yes]
  VEHBRA ADI Vehicle make -> [ADI]CODE =534;VEHBRA (ATABDIV) !Block
  VEHCO2 C*4 CO2 rate
  VEHPLCNBR C*4 Number of places
  VEHPWR C*4 Admin power
  VEHTAXRUL M*15 Tax rule [menu 3165: 1=Fiscal engine size (HP),2=CO2 emission rate]
  VEHTYP ADI Vehicle model -> [ADI]CODE =965;VEHTYP (ATABDIV) !Block
  VEHUSER ADI User -> [ADI]CODE =630;VEHUSER (ATABDIV) !Block
  VEHWEI1 DCB*9.2 TC wght
  VEHWEI2 DCB*9.2 TR wght

## FXDLIFL (FLU) - Track funds
Keys (first = PK; D = duplicates allowed): FLU0 AASREF+DPRPLN+TYP+FIYSTRDAT+PERSTRDAT+TXSCAT+FCY; FLU1 CODTXS+TXSCAT (D); FLU2 CPY+CNX+FLGSTATXS+FIYSTRDAT (D)
Fields:
  AASREF VC9 Asset
  AASTYPEND M*15 Type [menu 3151: 1=Tangible,2=Intangible,3=Goodwill,4=Financial,5=Investment properties,6=Biological assets]
  AASTYPSTR M*15 Type [menu 3151: 1=Tangible,2=Intangible,3=Goodwill,4=Financial,5=Investment properties,6=Biological assets]
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;COA (GACCCODE) !Other
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACNEND M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  ACNSTR M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  AUUID AUUID Single identifier
  BSEVALEND MD1 End FY srce val
  BSEVALSTR MD1 Init bal sht value
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart of accounts -> [COA]COA0 =[FLU]COA (GCOA) !Block
  CODTXS A*5 Funds code
  CPY CPY Company -> [CPY]CPY0 =[FLU]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FLU]CREUSR (AUTILIS) !Other
  DCRDPEOUT MD1 Disposal decrease
  DCRDPERVA MD1 Revaluation
  DCRDPRFCY MD1 Reduce transfer site
  DCRDPRTRF MD1 Transfer decrease
  DCRFCY MD1 Reduce transfer site
  DCRSAL MD1 Sale decrease
  DCRTRF MD1 Transfer decrease
  DERDPR MD1 Book vs Tax expense
  DERFLGDF M*4 Degressive method [menu 1: 1=No,2=Yes]
  DERFLGEXC M*4 Exceptional depreciations [menu 1: 1=No,2=Yes]
  DERISS MD1 Book vs Tax reversal
  DERRVE MD1 Book vs Tax reversal
  DPE MD1 Charges
  DPRBASEND MD1 Gross end val
  DPRBASRVA MD1 Depreciation base
  DPRBASSTR MD1 Gross start val
  DPRCUMEND MD1 Depreciations end
  DPRCUMSTR MD1 Depreciations start
  DPRDEG MD1 Decreasing deprec
  DPRLIN MD1 Linear deprec.
  DPROTH MD1 Other deprec.
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DPRRAT2 RA1 Depreciation rate
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  EXCDPR MD1 Exceptl deprn
  FCY FCY Site -> [FCY]FCY0 =[FLU]FCY (FACILITY) !Delete
  FCYORI FCY Original site -> [FCY]FCY0 =[FLU]FCYORI (FACILITY) !Block
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGSTATXS M*30 Funds status [menu 3266: 1=Non generated funds,2=Provisional funds,3=Final funds]
  GAC GAC General/IFRS acct. -> [GAC]GAC0 =COA;GAC (GACCOUNT) !Other
  GAL MD1 +/- value
  GRACUMEND MD1 Subsidy amount
  GRACUMSTR MD1 Subsidy amount
  IML MD1 P impairment loss
  IMLCUMEND MD1 Accumulated impairment loss
  IMLCUMSTR MD1 Accumulated impairment loss
  IMLRVE MD1 Impair. loss reversal P
  IMLRVEISS MD1(15) Impair. rev./disposal
  IMLRVETRF MD1 Impair. rev. - exc depr.
  INCBUY MD1 FY acquisition
  INCDPRFCY MD1 Increase site transfer
  INCDPRTRF MD1 Transfer increase
  INCFCY MD1 Increase site transfer
  INCTRF MD1 Transfer increase
  ISSAMT MD1 Disposal amount
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  NBVEND MD1 Net value
  NBVSTR MD1 Net value
  NSPVALEND MD1 Market value
  NSPVALSTR MD1 Market value
  NSPVALVAR MD1 Market value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  PURDAT D4 Purchase date
  PURNAT M*15 Purch nature [menu 3152: 1=New,2=Second-hand]
  RVAAMT MD1 Revaluation amount
  RVACUMEND MD1 Revaluation
  RVACUMSTR MD1 Revaluation
  RVARVEDPE MD1 Revaluation
  RVARVEIML MD1 Revaluation
  RVARVEISS MD1 Revaluation
  SALCLSDATEND D4 Asset date for sale
  SALCLSDATSTR D4 Asset date for sale
  SALCLSVAR MD1 Transfer
  STRDPRDAT D4 Depre start date
  TXSCAT A*15 Batch category
  TXSCATORI A*15 File cat FYR st
  TXSCLA A*2 Funds class
  TYP M*15 Funds tracking type [menu 3127: 1=Account group,2=Account]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FLU]UPDUSR (AUTILIS) !Other

## FXDLOFGRP (LFG) - Grouping of expenses
Keys (first = PK; D = duplicates allowed): LFG0 GRPREF; LFG1 CPY+GRPREF
Fields:
  ANDOR M*15(5) Operator [menu 56: 1=And,2=Or]
  AUUID AUUID Single identifier
  CODZON AVA(20) Field code
  CPY CPY Company -> [CPY]CPY0 =[LFG]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LFG]CREUSR (AUTILIS) !Other
  DES DCO Description
  EXP1 A*250 Expression
  FGACTIF M*4 Active [menu 1: 1=No,2=Yes]
  FLD AVA(5) Field
  GRPREF LGT Reference -> [LFG]LFG0 =[LFG]GRPREF (FXDLOFGRP) !BSRA
  NBCRIT C*4 Field nb
  OPE MM*15(5) Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  PRILOF M*15 Principal expense [menu 3296: 1=Upper excl tax amount,2=Most recent invoice date,3=Oldest invoice date,4=Most recent accounting date,5=Oldest accounting date]
  REQUETE A*250 Query
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LFG]UPDUSR (AUTILIS) !Other
  VALE A*30(5) Value

## FXDMVT (FXM) - Movement import - Header
Notes: differs in V9.0 P12 (diff: AT3_FXDMVT.htm)
Keys (first = PK; D = duplicates allowed): FXM0 IDMVT; FXM1 OBJMVT+REF1MVT+REF2MVT+SEQMVT+TYPMVT; FXM2 OBJMVT+TYPMVT+REF1MVT+REF2MVT+SEQMVT (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[FXM]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[FXM]CREUSR (AUTILIS) !BSRA
  DATINTMVT D Integration date
  DESRJTMVT A*250 Rejection description
  FCY FCY Site -> [FCY]FCY0 =[FXM]FCY (FACILITY) !Block
  IDMVT L*8 Movement no.
  OBJMVT M*15 Business object [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  ORIMVT M*15 Movement origin [menu 3295: 1=Import,2=Screen entry,3=Other]
  REF1MVT A*30 Reference
  REF2MVT A*30 Document no.
  SEQMVT L*8 Sequence no.
  STATMVT M*15 Movement status [menu 3294: 1=To be processed,2=Import in progress,3=Archived,4=Rejected]
  TRACE TRA Log
  TYPMVT M*15 Movement type [menu 3293: 1=Disposal,2=Transfer,3=Allocation change,4=Method change,5=Modification,6=All]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[FXM]UPDUSR (AUTILIS) !BSRA

## FXDMVTD (FXD) - Movement import - Detail
Keys (first = PK; D = duplicates allowed): FXD0 IDMVT+CODZONE+DIME+DPRPLN
Fields:
  AUUID AUUID Single identifier
  CODZONE AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FXD]CREUSR (AUTILIS) !Other
  DIME A*10 Dimension
  DPRPLN C*2 Depreciation plan
  IDMVT L*8 Movement no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FXD]UPDUSR (AUTILIS) !Other
  VALZONE A*250 Field value

## GRANTS (GRT) - Subsidies
Notes: activity code GRT
Keys (first = PK; D = duplicates allowed): GRT0 GRAREF; GRT1 CPY+GRAREF; GRT2 CPY+FCY+GRAREF; GRT3 CPY+FCY+INVPLN (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGSUBV;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  APPROVDAT D4 Agreement date
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CPY CPY Company -> [CPY]CPY0 =[GRT]CPY (COMPANY) !Delete
  CRBGRAAMT MD1 Reintegrtd amount
  CRBGRACUM MD1 Reintegration total
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[GRT]CUR (TABCUR) !Block
  DES DCO Description
  DES2 DCO Description 2
  DIE DIE Dimension type code -> [DIE]DIE0 =[GRT]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[GRT]FCY (FACILITY) !Block
  GRAAMT MD1 Subsidy amount
  GRAFLGFRC M*4 Subsidy amt forcing flag [menu 1: 1=No,2=Yes]
  GRAORG ADI Organization -> [ADI]CODE =617;GRAORG (ATABDIV) !Block
  GRAREF GRT Subsidy reference
  GRASTA MM*1 Status [menu 3225: 1=In process,2=Investment complete,3=Deleted,4=Totally reintegrated]
  GRATYP MM*25 Subsidy type [menu 3181: 1=Fixed rate,2=Percentage,3=Capped percentage]
  INVFLGFRC M*4 Capt forcing amount flag [menu 1: 1=No,2=Yes]
  INVGRAAMT MD1 FA subsidy amt
  INVGRARAT RAT Subsidised inv %
  INVPLN ADI Invest project -> [ADI]CODE =614;INVPLN (ATABDIV) !Block
  MAXGRAAMT MD1 Subsidy cap
  REAFLGFRC M*4 Act forcing amt flag [menu 1: 1=No,2=Yes]
  REAGRAAMT MD1 Act investment amt
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  TOBERECAMT MD1 Subs amt to be received
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## ITMACGGRP (ITA) - Product
Keys (first = PK; D = duplicates allowed): ITA0 ITMREF+LEG
Fields:
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ITA]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[ITA]ITMREF (ITMMASTER) !Delete
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ITA]UPDUSR (AUTILIS) !Other

## KCOEF (KCO) - Impairment loss coefficients
Notes: activity code KPO; differs in V9.0 P12 (diff: AT3_KCOEF.htm)
Keys (first = PK; D = duplicates allowed): KCO0 ANO
Fields:
  ANO L*4 Year of incidence
  AUUID AUUID Single identifier
  COEF DCB*4.2(99) Coefficient
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KCO]CREUSR (AUTILIS) !Other
  DECRETO A*50 Decree law
  PANO L*4(99) Reference year
  REAVAUT M*4 Fiscal reval. accepted [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KCO]UPDUSR (AUTILIS) !Other

## KTEMPPOR (KTP) - Temporary portuguese lists
Notes: activity code KPO; differs in V10 P1 (diff: ATD_KTEMPPOR.htm)
Keys (first = PK; D = duplicates allowed): KTP0 AASREF
Fields:
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  COEF DCB*4.2 Coefficient
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KTP]CREUSR (AUTILIS) !Other
  DECRETO A*50 Decree law
  KANOUTIL L*3(10) Expected useful years
  KAREAV_0 DCB*9.2 AD value previous FY
  KAREAV_1 DCB*9.2 AD value
  KVREAV_0 DCB*9.2 Last acq. value
  KVREAV_1 DCB*9.2 Revalued value
  KVREAV_2 DCB*9.2 Previous reval. val.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KTP]UPDUSR (AUTILIS) !Other

## LAYOUTFAS (LOF) - Expenses
Keys (first = PK; D = duplicates allowed): LOF0 CODLOF+LINLOF; LOF1 CPY+CODLOF+LINLOF+FLGLIKAAS+GACACN; LOF2 CPY+FCY+CODLOF+LINLOF; LOF5 FCY+CODLOF+LINLOF; LOF6 AASREF (D)
Fields:
  AASREF AAS Asset -> [FAS]FAS0 =[LOF]AASREF (FXDASSETS) !Other
  ACGGRP FAM Acct group -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACT VC9 Activity
  ADMCOE RAT Admission coef.
  AMTGRA MD1 Subsidy amount
  AMTNOTCPY MD1 Amount - tax
  AMTNOTCUR MD1 Amount - tax
  AMTNOTIAS MD1 IAS tax excl
  AMTVATCPY MD1 Tax amount
  AMTVATCUR MD1 Tax amount
  AMTVATIAS MD1 VAT invoiced
  AMTVATRCPY MD1 VAT recovered
  AMTVATRCUR MD1 Recvd VAT
  AMTVATRIAS MD1 VAT recovered
  ANALIGORI C*3 Ana. line source
  ASJCOE RAT Liability coef.
  AUUID AUUID Single identifier
  BPR BPR Supplier -> [BPR]BPR0 =[LOF]BPR (BPARTNER) !Block
  BPRVCR A*20 Invoice reference
  BUDINV ADI Investment budget -> [ADI]CODE =615;BUDINV (ATABDIV) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CODLOF LOF Reference
  CODLOFORI A*20 Original reference
  CONNUM ADI Market no -> [ADI]CODE =620;CONNUM (ATABDIV) !Block
  CPMCREORI M*15 Additional source [menu 3107: 1=Purchase invoices,2=BP invoices,3=Journal,4=Payment,5=Import,6=Stock issue]
  CPY CPY Company -> [CPY]CPY0 =[LOF]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[LOF]CUR (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DATIMP D4 Allocation date
  DATVCR D4 Invoice date
  DEMINV ADI Invest request -> [ADI]CODE =616;DEMINV (ATABDIV) !Block
  DES DCO Description 1
  DES2 DCO Description 2
  DIE DIE Dimension type code -> [DIE]DIE0 =[LOF]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  EXPNUM L*8 Export number
  FCY FCY Financial site -> [FCY]FCY0 =[LOF]FCY (FACILITY) !Block
  FIYBUD C*4 Fiscal year
  FLGAMTGRA MZS Subsidy strength
  FLGDETEXP M*4 Removable [menu 1: 1=No,2=Yes]
  FLGGRA M*4 Subsidized [menu 1: 1=No,2=Yes]
  FLGLIKAAS M*4 Asset link [menu 1: 1=No,2=Yes]
  FLGLOFMAI M*4 Principal expense [menu 1: 1=No,2=Yes]
  FLGRECFVR MZS*4 Force VAT recovered
  FLGVAL M*4 Validated [menu 1: 1=No,2=Yes]
  FLGVATFCR MZS*4 Force VAT
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACORI GAC Source CoA account -> [GAC]GAC0 ="";GACORI (GACCOUNT) !Other
  GEOFCY FCY Geographic site -> [FCY]FCY0 =[LOF]GEOFCY (FACILITY) !Other
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCORI GAC Source IFRS acct -> [GAC]GAC0 ="";IASACCORI (GACCOUNT) !Other
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[LOF]ITMREF (ITMMASTER) !Block
  JOU JOU Journal -> [JOU]JOU0 =[LOF]JOU (GJOURNAL) !Block
  KMDRDATACT D4 Improvement date act:KPL
  KMDRFLG M*4 Improvement [menu 1: 1=No,2=Yes] act:KPL
  LIGORI L*8 Detail line source
  LINLOF C*4 Line number
  LINLOFORI C*4 No. original line
  LOC A*38 Location
  ORDBUY A*20 Order reference
  PLNINV ADI Project ref. -> [ADI]CODE =614;PLNINV (ATABDIV) !Block
  QTY QTY Quantity
  RATCUR RCU Currency rate
  RATVAT RAT Invd VAT rate
  RATVATREC RAT Recovered VAT
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  TAXCOE RAT Taxation coeff
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TYPORI GTE Entry type -> [GTE]GTE0 =TYPORI;[V]GSUPCLE (GTYPACCENT) !Other
  TYPVCR M*15 Invoice type [menu 3117: 1=Invoice,2=Credit note,3=Pre-payment,4=To be received,5=Return,6=Early discount/late charge,7=Stock issue]
  UOM UOM Unit -> [TUN]TUN0 =[LOF]UOM (TABUNIT) !Block
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRDEN AUS Destination -> [AUS]CODUSR =[LOF]USRDEN (AUTILIS) !Block
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## LEABILBOOK (LBB) - Lease contract schedules
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_LEABILBOOK.htm); differs in V10 P1 (diff: ATD_LEABILBOOK.htm)
Keys (first = PK; D = duplicates allowed): LBB0 LEAREF+ENDPERDAT; LBB1 CPY+LEAREF+ENDPERDAT; LBB2 CPY+FCY+LEAREF+ENDPERDAT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[LBB]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDPERDAT D4 Period end
  FARFLG M*1 Invoice to be received [menu 1: 1=No,2=Yes]
  FARFLGI M*1 Invoice to be received [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[LBB]FCY (FACILITY) !Block
  FINDPR MD1 Financial depre
  FINEXS MD1 Financial cost
  LEAREF VC9 Lse contract ref.
  NBRDAYPER C*4 Number of days
  NBRMONPER C*4 Number of months
  NBRWEKPER C*4 Number weeks
  PAYDAT D4 Invoice date
  PAYREF A*20 Invoice ref
  PUROPT MD1 Purchase option price
  RMNTPA MD1 Remaining for reimbursement
  RNTAMT MD1 Rental amount
  RPACAP MD1 Reimbursed capital
  RSDVAL MD1 Resid. val. guarantee
  STRPERDAT D4 Period start
  TERPEN MD1 Penalties
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VARPAY MD1 Variable payments

## LEASE (LEA) - Lease contracts
Notes: activity code LEA; differs in V9.0 P12 (diff: AT3_LEASE.htm); differs in V10 P1 (diff: ATD_LEASE.htm)
Keys (first = PK; D = duplicates allowed): LEA0 LEAREF; LEA1 CPY+LEAREF; LEA2 CPY+FCY+LEAREF; LEA3 LEAREFORI (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AUUID AUUID Single identifier
  BEFRNT MD1 Advance rent
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CIGCOD A*10 IGS reference
  CPY CPY Company -> [CPY]CPY0 =[LEA]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR A*5 Creation user
  CUMIASBSE MD1 Receipt value total
  CUMRNTAMT MD1 Charge total
  CUR CUR Currency -> [TCU]TCU0 =[LEA]CUR (TABCUR) !Other
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CUTDAT D4 Update date
  DIE DIE Dimension type code -> [DIE]DIE0 =[LEA]DIE (GDIE) !Other act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DURPER C*4 Period duratns
  ENDLEADAT D4 Contrct end date
  FCY FCY Site -> [FCY]FCY0 =[LEA]FCY (FACILITY) !Block
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[LEA]IASCUR (TABCUR) !Other
  IASCURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  IASRATCUR RCU IFRS currency exch rate
  ICRBRWRAT RAT Incremental borrowing rate
  IMPLEARAT RAT Implied interest rate
  INIDIRCST MD1 Initial direct costs
  INIPREVAL MD1 Init. present value
  INIPREVALC MD1 Init. present value
  INIPREVALI MD1 Init. present value
  INIROU MD1 Initial right of use
  INIROUC MD1 Initial right of use
  INIROUI MD1 Initial right of use
  LEAAMT MD1 Capital amount
  LEAAMTDEV MD1 Capital in company currency
  LEAAMTIAS MD1 Capital in IFRS currency
  LEACUR CUR Funding currency -> [TCU]TCU0 =[LEA]LEACUR (TABCUR) !Other
  LEADES DCO Description 1
  LEADES2 DCO Description 2
  LEAEXS MD1 Building cost
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEARAT RAT Interest rate
  LEAREF LEA Lse contract ref. -> [LEA]LEA0 =[LEA]LEAREF (LEASE) !BSRA
  LEAREFORI VC9 Lease ag IGS origi
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[LEA]LES (BPARTNER) !Other
  RATCUR RCU Currency rate
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  RESCOS MD1 Restoration cost
  RPUDAT D4 Option exercise date
  RPUVAL MD1 Scrap value
  RPUVALDEV MD1 Scrap value
  RPUVALIAS MD1 Scrap value
  STRLEADAT D4 Contrct start date
  TRMLEADAT D4 Termination date
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Other
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Other
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Other
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Other
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Other
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Other
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Other
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Other
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Other
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Other
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## LNKCPTABD (LCD) - ABELX3 acc link detail
Keys (first = PK; D = duplicates allowed): LCA0 TYP+NUM (D); LCA1 TYP+NUM+NUMENR; LCA2 REF+DPRPLN+FIYENDDAT+PERENDDAT (D)
Fields:
  AUUID AUUID Single identifier
  CPTREF M*30 Accounting ledger [menu 3233: 1=Undetermined,2=Company accounting,3=Group accounting]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LCD]CREUSR (AUTILIS) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EVT ADI Event type -> [ADI]CODE =962;EVT (ATABDIV) !Block
  FIYENDDAT D4 Fiscal year end date
  LNKDAT D4 Date
  LNKSRC M Source [menu 3213: 1=Event,2=Depreciation,3=Other table,4=Provisions for renewal,5=Variance between plans]
  NUM VCR Document no.
  NUMENR L*8 Order information
  PERENDDAT D4 Period end date
  PSTACGRPR MD1 Posted prov. act:CCN
  PSTCADCRB MD1 Cad. fund decr. posted act:CCN
  PSTDER MD1 B. vs T. posted
  PSTDERRVE MD1 Book vs tax rev. posted
  PSTDPE MD1 Posted charge
  PSTEXC MD1 FYR posted
  PSTFISRPR MD1 F. prov. posted act:CCN
  PSTLNK MD1 Posted variance
  PSTRVACRB MD1 Re-ev. rec. posted
  PSTRVETRF MD1 Posted rec trf
  REF VC9 Reference
  TIMSTP A*20 Time stamp
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LCD]UPDUSR (AUTILIS) !Other

## LNKCPTABX3 (LCA) - ABELX3 acc link
Keys (first = PK; D = duplicates allowed): LCA0 CPY+FCY+TYP-ACCDAT+NUM; LCA1 CPTREF (D); LCA2 TYP+NUM; LCA3 CPY+FCY+ACETYP+TYP+NUM
Fields:
  ACCDAT D Accounting date
  ACCDATFIX D4 Accounting date
  ACCDATRUL M*15 Accounting date [menu 3130: 1=Automatic Journal,2=Start of processed period,3=End of processed period,4=Start of processed FY,5=End of processed FY,6=Start of current period,7=End of current period,8=Entered date,9=Specific date]
  ACETYP A*10 Entry type
  AUUID AUUID Single identifier
  CAT M*15 Category [menu 618: 1=Actual,2=Active simulation,3=Inactive simulation,4=Off-balance-sheet,5=Template]
  CPTREF M*30 Accounting ledger [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  CPY CPY Company -> [CPY]CPY0 =[LCA]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  FCY FCY Site -> [FCY]FCY0 =[LCA]FCY (FACILITY) !Delete
  FIY C*2 Fiscal year
  LNKDAT D4 Date
  LNKSRC M Source [menu 3213: 1=Event,2=Depreciation,3=Other table,4=Provisions for renewal,5=Variance between plans]
  NUM VCR Document no.
  PER C*2 Period
  TRACE TRA Linked trace file
  TYP GTE Entry type -> [GTE]GTE0 =[LCA]TYP (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PAREVT (PVT) - Parameterisation of events
Notes: differs in V10 P1 (diff: ATD_PAREVT.htm)
Keys (first = PK; D = duplicates allowed): PVT0 EVT+PLN+EVTINT; PVT1 EVT+EVTINT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PVT]CREUSR (AUTILIS) !Other
  EVT ADI Event type -> [ADI]CODE =962;EVT (ATABDIV) !Delete
  EVTINT A*15 Internal code
  OBJTYP M*1 Object type [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  PLN M*25 Plan [menu 3101: 16 values, see local-menus.md]
  TABEVT ATB Events table -> [ATB]CODFIC =[PVT]TABEVT (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PVT]UPDUSR (AUTILIS) !Other

## PAREVTD (PVD) - Parameterisation of events
Notes: differs in V10 P1 (diff: ATD_PAREVTD.htm)
Keys (first = PK; D = duplicates allowed): PVD0 EVTINT+FLDNAM; PVD1 EVTINT (D); PVD2 EVTINT+NUMLIG+FLDNAM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PVD]CREUSR (AUTILIS) !Other
  EVTINT A*15 Internal code
  FLDACT ACV Activity code -> [ACV]CODACT =[PVD]FLDACT (ACTIV) !Block
  FLDFIL A*250 Value
  FLDNAM A*10 Field
  FLDPRORAT M*4 Split [menu 1: 1=No,2=Yes]
  FLDTYP M*15 Type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  FLGKEEP C*4 Flag
  NUMLIG C*3 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PVD]UPDUSR (AUTILIS) !Other

## PARFLUX (PFL) - Parametn of funds(header)
Keys (first = PK; D = duplicates allowed): PFL0 CODTXS+COA+POSTXS
Fields:
  AUUID AUUID Single identifier
  CLATXS M*15 Funds class [menu 3128: 1=Intangible,2=Tangible,3=In process,4=Financial]
  COA COA Chart code -> [COA]COA0 =[PFL]COA (GCOA) !Block
  CODTXS A*5 Funds code
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES A*100 Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  OUTFUNDS M*4 Outside of fiscal statement [menu 1: 1=No,2=Yes]
  POSTXS C*4 Funds line
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PARFLUXDET (PFD) - Parametn of funds(detail)
Keys (first = PK; D = duplicates allowed): PFD0 CODTXS+COA+POSTXS+GAC; PFD1 CODTXS+COA+GAC
Fields:
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[PFD]COA (GCOA) !Block
  CODTXS A*5 Funds code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PFD]CREUSR (AUTILIS) !Other
  GAC GAC Account -> [GAC]GAC0 =COA;GAC (GACCOUNT) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  POSTXS C*4 Funds line
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PFD]UPDUSR (AUTILIS) !Other

## PARLDAP (LDA) - Expense asset link parameter
Keys (first = PK; D = duplicates allowed): LDA0 CPY
Fields:
  AUUID AUUID Single identifier
  CODZON AVA(10) Field code
  CPY CPY Company -> [CPY]CPY0 =[LDA]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  NBLDAP C*4 Number of fields
  ORNUL M*4(10) Or empty [menu 1: 1=No,2=Yes]
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PARTRZL (TZL) - Transit fields paramtn
Keys (first = PK; D = duplicates allowed): TZL0 KEYTZL; TZL1 OBJSRC+OBJDES+CPY
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TZL]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  KEYTZL TZL Identifier
  OBJDES MM*15 Destination object [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  OBJSRC MM*15 Source object [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WINDES FEN Target window -> [AWI]AWI0 =[TZL]WINDES (AWINDOW) !Delete
  WINSRC FEN Source window -> [AWI]AWI0 =[TZL]WINSRC (AWINDOW) !Delete

## PARTRZLDET (TZD) - Transit flds paramtn detl
Keys (first = PK; D = duplicates allowed): TZD0 KEYTZL+CODZONSRC+CODZONDES
Fields:
  ALLVALEQU M*4 Same value [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CNSVAL A*20 Constant
  CODZONDES AVA Destination field
  CODZONSRC AVA Source field
  CPY CPY Company -> [CPY]CPY0 =[TZD]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUM M*4 Total [menu 1: 1=No,2=Yes]
  FREMAI M*10 Empty/principal [menu 3190: 1=Empty,2=Main]
  KEYTZL TZL Identifier
  ORNUL M*4 Or empty [menu 1: 1=No,2=Yes]
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PHYBUI (BUI) - Building
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): BUI0 BUICOD
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Default address
  BUICOD BUI Building -> [BUI]BUI0 =[BUI]BUICOD (PHYBUI) !BSRA
  BUIDES DCO Description
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GEOLOC A*250 Geolocation
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PHYELT (PHY) - Physical assets
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): PHY0 PHYREF; PHY3 BAC+CPY (D); PHY4 CPY+FCY+PHYREF; PHY5 AASREF+PHYREF
Fields:
  AASREF FAS Assignment asset -> [FAS]FAS0 =[PHY]AASREF (FXDASSETS) !Block
  AUUID AUUID Single identifier
  BAC BAC Barcode
  BPS BPS Supplier -> [BPS]BPS0 =[PHY]BPS (BPSUPPLIER) !Block
  CNTNUM ADI Contact -> [ADI]CODE =630;CNTNUM (ATABDIV) !Block
  COMMENT ACRTF*1 Comments
  CPY CPY Company -> [CPY]CPY0 =[PHY]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR A*5 Creation user
  CURCND ADI Current status -> [ADI]CODE =538;CURCND (ATABDIV) !Block
  DNUMRECEP D4 Receipt date
  DORDBUY D4 Order date
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[PHY]FCY (FACILITY) !Block
  GEOLOC A*250 Geolocation
  GRUORIPHY A*20 IGS source element
  ISSDAT D4 Issue date
  ISSTYP M*15 Disposal reason [menu 3175: 1=Not disposed,2=Stock count issue,3=Sale,4=Scrap,5=Theft or disappearance]
  IVYDAT D4 Note date
  IVYRES M*15 Phys asset count result [menu 3194: 1=Disposal cancelled,2=Geographic change,3=Analytical change,4=Analytical and geographic change,5=Bar code allocation,6=Bar code change,7=Asset not found,8=Counted asset]
  IVYTIM HS Note time
  LCTCOD LCT Location -> [LCT]LCT0 =LCTCOD (PHYLCT) !Block
  NUMRECEP A*20 Receipt number
  ORDBUY A*20 Order number
  PHYCAT ADI Category -> [ADI]CODE =537;PHYCAT (ATABDIV) !Block
  PHYDES1 DCO Description
  PHYDES2 DCO Description 2
  PHYREF PHY Reference -> [PHY]PHY0 =[PHY]PHYREF (PHYELT) !Other
  PHYREFORI A*20 Original reference
  REFTAB1 C*4 Reference FF1
  REFTAB10 C*4 Reference FF10
  REFTAB2 C*4 Reference FF2
  REFTAB3 C*4 Reference FF3
  REFTAB4 C*4 Reference FF4
  REFTAB5 C*4 Reference FF5
  REFTAB6 C*4 Reference FF6
  REFTAB7 C*4 Reference FF7
  REFTAB8 C*4 Reference FF8
  REFTAB9 C*4 Reference FF9
  SRLNBR SRL Serial number
  TRFDAT D4 Last transfer
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## PHYLCT (LCT) - Localizations
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): LCT0 LCTCOD; LCT1 FCY+LCTCOD; LCT2 BAC+FCY+LCTCOD
Fields:
  AUUID AUUID Single identifier
  BAC BAC Barcode
  BUICOD BUI Building -> [BUI]BUI0 =[LCT]BUICOD (PHYBUI) !BSRA
  CPY CPY Company -> [CPY]CPY0 =[LCT]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LCT]CREUSR (AUTILIS) !Other
  DFLFLG M*4 Default location [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FLOOR A*30 Floor
  GEOLOC A*250 Geolocation
  LCTCOD LCT Location -> [LCT]LCT0 =[LCT]LCTCOD (PHYLCT) !BSRA
  LCTDES DCO Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LCT]UPDUSR (AUTILIS) !Other

## PHYMVT (PMVT) - Physical assets - movements
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): PMVT0 PHYREF+NUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PMVT]CREUSR (AUTILIS) !Other
  MVT M*30 Pending movements [menu 3275: 1=None,2=Disposal,3=Disposal cancellation,4=Geographic transfer,5=Geographic transfer cancellation]
  MVTDAT D4 Movement date
  MVTFCY FCY Dest. financial site -> [FCY]FCY0 =[PMVT]MVTFCY (FACILITY) !Delete
  MVTISSTYP M*15 Disposal reason [menu 3175: 1=Not disposed,2=Stock count issue,3=Sale,4=Scrap,5=Theft or disappearance]
  MVTLCTCOD LCT Dest. location -> [LCT]LCT0 =MVTLCTCOD (PHYLCT) !Block
  MVTTRANS ADI Tansfer reason -> [ADI]CODE =612;MVTTRANS (ATABDIV) !Block
  NUM C*4 Order no.
  PHYREF PHY Reference -> [PHY]PHY0 =PHYREF (PHYELT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PMVT]UPDUSR (AUTILIS) !Other

## PROPLN (PLP) - Production plan
Keys (first = PK; D = duplicates allowed): PPL0 PROPLN+FIYENDDAT+PERENDDAT
Fields:
  AUUID AUUID Single identifier
  CPLQTY QTY Actual OU
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  EXTQTY QTY Planned units
  FIYENDDAT D4 Fiscal year end date
  FIYQTY QTY FY units
  FIYSTRDAT D4 Fiscal year start date
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  PLNQTY QTY Plan unit
  PPLENDDAT D4 Production plan end
  PROPLN PLP Production plan
  RSDQTY QTY Residual unit
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## PROPLNH (PLH) - Production plan
Keys (first = PK; D = duplicates allowed): PPH0 PROPLN; PPH1 CPY+PROPLN; PPH2 CPY+FCY+PROPLN; PPH3 CPY+CNX (D)
Fields:
  AUUID AUUID Single identifier
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[PLH]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[PLH]FCY (FACILITY) !Delete
  PLNDES1 DCO Description
  PLNDES2 DCO Description 2
  PPLENDDAT0 D4 End date
  PROPLN PLP Production plan
  UOM UOM Unit -> [TUN]TUN0 =[PLH]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## PSEPLN (PSE) - Seasonality plan
Notes: activity code PSE
Keys (first = PK; D = duplicates allowed): PSE0 CPY+PSEPLN
Fields:
  ACTFLG M*4(12) Activity period [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PSE]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES1 DCO Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  PSEPLN VC9 Seasonality plan
  SESTYP M*15 Type [menu 3291: 1=Decreasing,2=Increasing]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## RNWPREP (RWP) - Renewal
Notes: activity code CCN
Keys (first = PK; D = duplicates allowed): RWP0 CPY+FCY+RNWAASREF+MOTHAASREF; RWP1 CPY+MOTHAASREF; RWP2 CPY+FCY+CCNREF+RNWAASREF (D); RWP3 RNWDONFLG (D)
Fields:
  AUUID AUUID Single identifier
  CCNREF VC9 Concession contract
  CCNUSR BPR Grantor -> [BPR]BPR0 =[RWP]CCNUSR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[RWP]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RWP]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[RWP]FCY (FACILITY) !Delete
  FLGCAL M*4 Calculation of funds [menu 1: 1=No,2=Yes]
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  MOTHAASREF VC9
  RNWAASREF VC9
  RNWDAT D4 Renewal date act:CCN
  RNWDONFLG M*4 Renewal carried out [menu 1: 1=No,2=Yes]
  RNWVALFLGO M*4 Renewal value forcing [menu 1: 1=No,2=Yes]
  RNWVALO MD1 Renewal value
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RWP]UPDUSR (AUTILIS) !Other

## RUBASSDEF (RDE) - Associations - definition
Keys (first = PK; D = duplicates allowed): RDE0 REFOBJ+DETAAS+ACM+CPY; RDE1 NUMASS
Fields:
  ACM GCM Account core model -> [GCM]GCM0 =[RDE]ACM (GACM) !Block
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[RDE]CPY (COMPANY) !Delete
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DETAAS MM*15 Decisive [menu 3113: 1=Asset group,2=Accounting code]
  ENAFLG M*4 Active flag [menu 1: 1=No,2=Yes]
  FRCFLG M*4(40) Forcing flag [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MGTFLG M*4(40) Management flag [menu 1: 1=No,2=Yes]
  NBRUB C*4 Number of sections
  NBRUB0 C*4 Number of sections
  NUMASS A*10 Association number
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  RUBRAS ADI(40) Deter sect -> [ADI]CODE =961;RUBRAS (ATABDIV) !Block
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*4(40) Update indicator [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user

## RUBASSDEFP (RDP) - Associations - definition/plan
Keys (first = PK; D = duplicates allowed): RDP0 REFOBJ+DETAAS+ACM+CPY+DPRPLN; RDP1 NUMASS+DPRPLN
Fields:
  ACM GCM Account core model -> [GCM]GCM0 =[RDP]ACM (GACM) !Block
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[RDP]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RDP]CREUSR (AUTILIS) !Other
  DETAAS MM*15 Decisive [menu 3113: 1=Asset group,2=Accounting code]
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  ENAFLG M*4 Active flag [menu 1: 1=No,2=Yes]
  FRCFLGP M*4(40) Forcing flag [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MGTFLGP M*4(40) Management flag [menu 1: 1=No,2=Yes]
  NBRUBP C*4 Number of sections
  NUMASS A*10 Association number
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  RUBRASP ADI(40) Deter sect -> [ADI]CODE =961;RUBRASP (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDFLGP M*4(40) Update indicator [menu 1: 1=No,2=Yes]
  UPDUSR AUS User -> [AUS]CODUSR =[RDP]UPDUSR (AUTILIS) !Other

## RUBASSVAL (RVA) - Associations - values
Keys (first = PK; D = duplicates allowed): RVA1 REFOBJ+DETAAS+ACM+CPY+VALDETAAS; RVA0 NUMASS+VALDETAAS; RVA2 REFOBJ+DETAAS+ACM+CPY (D)
Fields:
  ACM GCM Account core model -> [GCM]GCM0 =[RVA]ACM (GACM) !Delete
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[RVA]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RVA]CREUSR (AUTILIS) !Other
  DETAAS M*15 Decisive [menu 3113: 1=Asset group,2=Accounting code]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBLIG C*2 Number
  NOADI C*4(40) ADI table no.
  NOLIB C*4(40) Local menu no.
  NUMASS A*10 Association number
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  RUBRAS ADI(40) Given section -> [ADI]CODE =961;RUBRAS (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RVA]UPDUSR (AUTILIS) !Other
  VALDETAAS A*30 Overriding value
  VALDETEAS A*30(40) Given value

## RUBASSVALP (RVP) - Associations - values/plan
Keys (first = PK; D = duplicates allowed): RVP0 NUMASS+VALDETAAS+DPRPLN; RVP1 REFOBJ+DETAAS+ACM+CPY+VALDETAAS+DPRPLN
Fields:
  ACLCOE RA1 Acceleration coeff.
  ACM GCM Account core model -> [GCM]GCM0 =[RVP]ACM (GACM) !Block
  ALWCOD M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[RVP]CPY (COMPANY) !Delete
  CRBVEHCOD ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCOD (ATABDIV) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RVP]CREUSR (AUTILIS) !Other
  DETAAS M*15 Decisive [menu 3113: 1=Asset group,2=Accounting code]
  DPM DPM Depreciation method
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DPRRAT2 RA1 Exc. depr rate
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NUMASS A*10 Association number
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RVP]UPDUSR (AUTILIS) !Other
  VALDETAAS A*30 Overriding value

## RVACOED (COD) - Reval. coefficient (detail)
Keys (first = PK; D = duplicates allowed): COD0 RVACOEREF+CLETAB; COD1 RVANAT+YEA+MON (D)
Fields:
  AUUID AUUID Single identifier
  CLETAB A*18
  CPY CPY Company -> [CPY]CPY0 =[COD]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[COD]CREUSR (AUTILIS) !Other
  CRITDAT M*15 Date criterion [menu 3234: 1=Purchase date,2=Posting date,3=In service date]
  CRITNAT M*15 Nature critern [menu 3235: 1=Asset group,2=Accounting code]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  MON C*2 Months
  RVACOE COE Revaluation coef
  RVACOEREF A*20 Table reference
  RVAIND IND Revaluation index
  RVANAT A*12 Nature
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[COD]UPDUSR (AUTILIS) !Other
  YEA C*4 Year

## RVACOEH (COH) - Reval. coefficient (header)
Notes: differs in V9.0 P12 (diff: AT3_RVACOEH.htm); differs in V10 P1 (diff: ATD_RVACOEH.htm)
Keys (first = PK; D = duplicates allowed): COH0 RVACOEREF; COH1 CPY+RVACOEREF; COH2 RVACOEREF+CRITDAT+CRITNAT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[COH]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRITDAT M*15 Date criterion [menu 3234: 1=Purchase date,2=Posting date,3=In service date]
  CRITNAT M*15 Nature critern [menu 3235: 1=Asset group,2=Accounting code]
  DESTAB DCO Description
  ENAFLG M*4 Active flag [menu 1: 1=No,2=Yes]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  RVACOEREF TCO Table reference -> [COH]COH0 =[COH]RVACOEREF (RVACOEH) !BSRA
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SAITRS (SAI) - Entry transaction
Keys (first = PK; D = duplicates allowed): HST0 REFOBJ+TRSCOD
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[SAI]ACSCOD (ACCCOD) !RTZ
  AUUID AUUID Single identifier
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLGINV M*4(10) Visible [menu 1: 1=No,2=Yes]
  FLGINVORI M*4(10) Visible [menu 1: 1=No,2=Yes]
  GFY AGF Group -> [AGF]AGF0 =[SAI]GFY (AGRPFCY) !RTZ
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !RTZ act:LEG
  LISMSK AMK(10) Mask -> [AMK]CODMSK =[SAI]LISMSK (AMSK) !Block
  NBRMSK C*4 Numbers of masks
  NUMMSK C*4(10) Tab number
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  TRSCOD A*5 Entry transaction
  TRSCOP A*10 Entry transaction
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WIN FEN Window -> [AWI]AWI0 =[SAI]WIN (AWINDOW) !Delete

## SAITRSDET (DST) - Entry transaction detail
Keys (first = PK; D = duplicates allowed): DST0 REFOBJ+TRSCOD+NUMMSK+CODMSK+CODZON; DST1 REFOBJ+TRSCOD+CODMSK (D); DST2 CODMSK (D); DST3 BROMSK (D); DST4 NUMMSK (D)
Fields:
  AUUID AUUID Single identifier
  BROMSK A*20 Screen
  CODMSK AMK Screen code -> [AMK]CODMSK =[DST]CODMSK (AMSK) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[DST]CODTYP (ATYPE) !Delete
  CODZON AVA Field code
  CREDAT D4 Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DSPVAL M*4 Prorate [menu 1: 1=No,2=Yes]
  FLGTRT C*1 Processed
  INTIT ATX Description
  INTMSK ATX Screen title
  MODE M*15 Entry mode [menu 99: 1=Form and table,2=Form,3=Table]
  MODEORI M*15 Entry mode [menu 99: 1=Form and table,2=Form,3=Table]
  MODFLG M*4 Mod [menu 1: 1=No,2=Yes]
  MZSZON A*10 Assocd MZS field
  NUMBLOC C*3 Block number
  NUMMSK C*4 Tab number
  OBLIG M*4 Mandatory field [menu 1: 1=No,2=Yes]
  OBLIGORI M*4 Mandatory field [menu 1: 1=No,2=Yes]
  REFOBJ M*15 Object code [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  SAIAFF MM*15 Entry type [menu 936: 1=Enter,2=Display,3=Hidden,4=Technical]
  SAIAFFORI MM*15 Entry type [menu 936: 1=Enter,2=Display,3=Hidden,4=Technical]
  TRSCOD A*5 Entry transaction
  UPDDAT D4 Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALDEF A*80 Default value
  VALDEFORI A*80 Default value

## SECACT (SEA) - Activity sector
Keys (first = PK; D = duplicates allowed): SEA0 CPY+SAC
Fields:
  ASJCOE RAT Liability coef.
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SEA]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SAC SEA Activity sector
  SACDES DES Description
  TAXCOEDEF RAT Final tax coef
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TAXCOEINI RAT Temp. tax coef
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## TMP2054 (T54) - 2054 fiscal statement Temporary table
Keys (first = PK; D = duplicates allowed): T540 EDTNUM+CPY+CLATXS+POSTXS
Fields:
  A1 MD1 Gross start value
  A2 MD1 Revaluation increase
  A3 MD1 Transfer increase
  AC MD1 Component value
  AUUID AUUID Single identifier
  B1 MD1 Transfer decrease
  B2 MD1 Sale decrease
  B3 MD1 Gross end value
  B4 MD1 End FY source value
  CLATXS M*15 Funds class [menu 3128: 1=Intangible,2=Tangible,3=In process,4=Financial]
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CODTXS A*5 Funds code
  CPY CPY Company -> [CPY]CPY0 =[T54]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EDTNUM L*8 Processing number
  FCY FCY Site -> [FCY]FCY0 =[T54]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGSTATXS M*30 Funds status [menu 3266: 1=Non generated funds,2=Provisional funds,3=Final funds]
  GAC GAC General account -> [GAC]GAC0 =[T54]GAC (GACCOUNT) !BSRA
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  POSTXS C*4 Funds line
  POSTXSDES A*100 Description
  TXSCAT A*15 Batch category
  TYP M*15 Funds tracking type [menu 3127: 1=Account group,2=Account]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[T54]UPDUSR (AUTILIS) !Other

## TMP2055 (T55) - Fiscal statem. 2055 temp. table
Keys (first = PK; D = duplicates allowed): T550 EDTNUM+CPY+CLATXS+POSTXS
Fields:
  A1 MD1 Depreciations start
  A2 MD1 Increase by charges
  A3 MD1 Sale decrease
  A4 MD1 Depreciations end
  AUUID AUUID Single identifier
  B1 MD1 BvsT exp-durat
  B2 MD1 BvsT exp-decrea
  B3 MD1 BvsT exp-Exc dep
  B4 MD1 BvsT revers.-dur
  B5 MD1 BvsT revers.-decrea
  B6 MD1 BvsT revers.-Exc dep
  CLATXS M*15 Funds class [menu 3128: 1=Intangible,2=Tangible,3=In process,4=Financial]
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CODTXS A*5 Funds code
  CPY CPY Company -> [CPY]CPY0 =[T55]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  EDTNUM L*8 Processing number
  FCY FCY Site -> [FCY]FCY0 =[T55]FCY (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGSTATXS M*30 Funds status [menu 3266: 1=Non generated funds,2=Provisional funds,3=Final funds]
  GAC GAC General account -> [GAC]GAC0 =[T55]GAC (GACCOUNT) !BSRA
  PERENDDAT D4 Period end date
  PERSTRDAT D4 Period start date
  POSTXS C*4 Funds line
  POSTXSDES A*100 Description
  TOTB MD1 Total Box B
  TXSCAT A*15 Batch category
  TYP M*15 Funds tracking type [menu 3127: 1=Account group,2=Account]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TMP2855 (TVS) - Temporary table Fisc. Stmt 2855
Keys (first = PK; D = duplicates allowed): T550 EDTNUM+CPY+IMPSTRDAT+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TVS]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EDTNUM L*8 Processing number
  EXOENDDAT D4 Exemption end date
  FCY FCY Site -> [FCY]FCY0 =[TVS]FCY (FACILITY) !Delete
  FIRICIDAT D4 1st use date
  FUEL M*4 Fuel type [menu 3167: 1=Fuel and similar products,2=Diesel and similar products,3=Electric,4=Other]
  FUELDES DCO Fuel
  IMPENDDAT D4 End date
  IMPSTRDAT D4 Start date
  ISSDAT D4 Issue date
  NBTRIM1E C*4 No. quart. half-rate
  NBTRIM1P C*4 No. quart.full rate
  NBTRIM1T C*4 Total no. q
  NBTRIM2 C*4 No. quarters
  NPL A*15 Registration no.
  PURDAT D4 Purchase date
  RGNDAT D4 Registration date
  RNTDUR DUR Rent duration
  RNTENDDAT D4 Lease end
  RNTSTRDAT D4 Lease start
  T1STRDAT D4 Start date Q1
  T2STRDAT D4 Start date Q2
  T3STRDAT D4 Start date Q3
  T4STRDAT D4 Start date Q4
  TARIFAIR MD1 Tarif Air
  TARIFCO2 MD1 CO2 price list
  TARIFPWR MD1 Engine size rate
  TAXECOL1 MD1 Tax col 1
  TAXECOL2 MD1 Tax col 2
  TAXECOL3 MD1 Tax col 3
  TAXECOL4 MD1 Tax col 4
  TAXPLI M Taxation rate [menu 3164: 1=Full rate,2=50% exempt,3=Total exemption]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VEHCO2 C*4 CO2 rate
  VEHCO2RAT ADI CO2 emmission rate -> [ADI]CODE =629;VEHCO2RAT (ATABDIV) !Other
  VEHPWR C*4 Admin power
  VEHTAXRUL M*15 Tax rule [menu 3165: 1=Fiscal engine size (HP),2=CO2 emission rate]

## TMPCPTDTA (TCD) - Accounting interface -data
Keys (first = PK; D = duplicates allowed): TCD0 TRTNUM+PCENUM+SEQNUM+DSP+CCE
Fields:
  AASBUS ADI(2) Activity -> [ADI]CODE =410;AASBUS (ATABDIV) !Other
  AASTYP M*15 Type [menu 3151: 1=Tangible,2=Intangible,3=Goodwill,4=Financial,5=Investment properties,6=Biological assets]
  ACCCOD CAC(2) Accounting code -> [CAC]CAC0 =TYP;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  AGRKEY A*80 Aggregation level
  ALPHA A*20(4) Alphanumeric
  AMT DCB*11.2(20) Amounts
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CCED CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CPTKEY A*20(10) Key
  CPTREF M*30 Accounting ledger [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  CPTSTA L*8 Result
  CPY CPY Company -> [CPY]CPY0 =[TCD]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCD]CREUSR (AUTILIS) !Other
  CUR CUR(2) Currency -> [TCU]TCU0 =[TCD]CUR (TABCUR) !Other
  DAT D(2) Date
  DIE DIE Dimension type -> [DIE]DIE0 =[TCD]DIE (GDIE) !Other act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPD DSP New allocation -> [DSP]DSP0 =DSPD;1 (CADSP) !Other
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  EVTPRINC M*4 Main event [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TCD]FCY (FACILITY) !Other
  GAC GAC(4) Account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15(2) CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GRASTA M*1 Status [menu 3225: 1=In process,2=Investment complete,3=Deleted,4=Totally reintegrated] act:GRT
  GRATYP M*25 Subsidy type [menu 3181: 1=Fixed rate,2=Percentage,3=Capped percentage] act:GRT
  IASACC GAC(2) IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other act:IAS
  IASACN M*15(2) IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:IAS
  IASCGU ADI(2) UGT -> [ADI]CODE =413;IASCGU (ATABDIV) !Other act:IAS
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold] act:LEA
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent] act:LEA
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !RTZ
  LIN C*3 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PCENUM L*8 Document no.
  REF VC9 Reference
  SEQNUM L*8 Sequence number
  SNS C*2 Sign
  TRTNUM L*8 Processing number
  TYP M*15 Accounting code type [menu 602: 26 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCD]UPDUSR (AUTILIS) !Other

## TMPDERO (TDE) - Temporary table
Keys (first = PK; D = duplicates allowed): TDE0 EDTNUM+CPY+FCY+AASREF; TDE1 EDTNUM+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DCO Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[TDE]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[TDE]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TDE]CREUSR (AUTILIS) !Other
  CUMANTCPT MD1 Dep. merging FY start
  CUMANTFI MD1 Dep. merging FY start
  DATISSPSTC D4 Issue date
  DATISSPSTF D4 Issue date
  DEROPERCLO MD1 Book vs Tax provision
  DERRVEISS MD1 Book vs tax rev./disposal
  DOTCPT MD1 Accounting charge
  DOTFI MD1 Fiscal charge
  DPETC MD1 Theo charge
  DPETF MD1 Theo charge ex impair.
  DPMC DPM Depreciation method
  DPMF DPM Depreciation method
  DPRBASC MD1 Reval. BS value
  DPRBASF MD1 Reval. BS value
  DPRCUMC MD1 FY depre total
  DPRCUMF MD1 FY depre total
  DPRDURC DUR Depre. durn
  DPRDURF DUR Depre. durn
  DPRRATC RA1 Depreciation rate
  DPRRATF RA1 Depreciation rate
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPEC MD1 Fiscal Year charge
  ENDDPEF MD1 Fiscal Year charge
  ENDDPETC MD1 Yearly deprec. theo
  ENDDPRDATC D4 Deprec end date
  ENDDPRDATF D4 Deprec end date
  EXCDPRC MD1 FYR except deprec
  EXCDPRF MD1 FYR except deprec
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TDE]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FIYENDDATC D4 Fiscal year end date
  FIYENDDATF D4 Fiscal year end date
  FIYSTRDATC D4 Fiscal year start date
  FIYSTRDATF D4 Fiscal year start date
  FLGUPDISSC M*4 Modification [menu 1: 1=No,2=Yes]
  FLGUPDISSF M*4 Modification [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other
  IASCGUDES DCO Description
  ISSDAT D4 Issue date
  LEG MD1 Legal link amt
  LEGCUMC MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUMC MD1 Plan E-1 legal link rec.tot
  NBVC MD1 Net value
  NBVF MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUMC MD1 Periodic total P-1
  PERCLOCUMF MD1 Periodic total P-1
  PERENDDPEC MD1 Period P charge
  PERENDDPEF MD1 Period P charge
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PROVISION MD1 Provision
  REPRISE MD1 Recovery
  REPSOR MD1 Reversal on disposal
  SOLDEBEX MD1 FY start closing
  SOLFINEX MD1 FY end closing
  STRDPRDATC D4 Depre start date
  STRDPRDATF D4 Depre start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TDE]UPDUSR (AUTILIS) !Other

## TMPDFD (TDF) - DFDDPEreport temp table
Keys (first = PK; D = duplicates allowed): TDF0 EDTNUM+CPY+FCY+AASREF; TDF1 EDTNUM+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DCO Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =[TDF]CCE1 (CACCE) !BSRA
  CCE1DES DCO Description
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =[TDF]CCE2 (CACCE) !BSRA
  CCE2DES DCO Description
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =[TDF]CCE3 (CACCE) !BSRA
  CCE3DES DCO Description
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =[TDF]CCE4 (CACCE) !BSRA
  CCE4DES DCO Description
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =[TDF]CCE5 (CACCE) !BSRA
  CCE5DES DCO Description
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =[TDF]CCE6 (CACCE) !BSRA
  CCE6DES DCO Description
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =[TDF]CCE7 (CACCE) !BSRA
  CCE7DES DCO Description
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =[TDF]CCE8 (CACCE) !BSRA
  CCE8DES DCO Description
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =[TDF]CCE9 (CACCE) !BSRA
  CCE9DES DCO Description
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart code -> [COA]COA0 =[TDF]COA (GCOA) !Other
  CPY CPY Company -> [CPY]CPY0 =[TDF]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TDF]CREUSR (AUTILIS) !Other
  DATISSPST D4 Issue date
  DFD MD1 Deferred deprec
  DFDBLC MD1 Deferred deprec balance
  DFDRVE MD1 Deferred reversal
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[TDF]DIE (GDIE) !Other
  DPM DPM Depreciation method
  DPRBAS MD1 Reval. BS value
  DPRBASF MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRCUMF MD1 FY depre total
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPE MD1 Fiscal Year charge
  ENDDPEF MD1 Fiscal Year charge
  ENDDPRDAT D4 Deprec end date
  EXCDPR MD1 FYR except deprec
  EXCDPRF MD1 FYR except deprec
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TDF]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete
  IASCGUDES DCO Description
  ISSDAT D4 Issue date
  NBV MD1 Net value
  NBVF MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUM MD1 Periodic total P-1
  PERCLOCUMF MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERCLOEXCF MD1 Office P-1 amt excep.
  PERENDDAT D4 Period end date
  PERENDDPE MD1 Period P charge
  PERENDDPEF MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PEREXCDPRF MD1 Exceptional amortization
  PERSTRDAT D4 Period start date
  STRDPRDAT D4 Depre start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TDF]UPDUSR (AUTILIS) !Other

## TMPFAS1PAGE (T1PG) - Tmp. depr. one page report
Keys (first = PK; D = duplicates allowed): T1P0 CPY+AASREF (D)
Fields:
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[T1PG]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[T1PG]CREUSR (AUTILIS) !Other
  DPM DPM(6) Depreciation method
  DPRBAS MD1(6) Reval. BS value
  DPRCUM MD1(6) FY depre total
  DPRDUR DUR(6) Depre. durn
  DPRPLN M*25(6) Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1(6) Depreciation rate
  ENDDPRDAT D4(6) Deprec end date
  NBV MD1(6) Net value
  RSDVAL MD1(6) Residual value
  STRDPRDAT D4(6) Depre start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[T1PG]UPDUSR (AUTILIS) !Other

## TMPFAS246G (T246) - Tmp. depreciation report
Keys (first = PK; D = duplicates allowed): T2460 CPY+AASREF+DPRPLN+POSTXS (D)
Fields:
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  BASADDN MD1 Addition
  BASDEC MD1 Write-down
  BASDISP MD1 Disposal
  BASEND MD1 End acqu. costs
  BASINC MD1 Write-up
  BASSTR MD1 Start acqu. costs
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart code -> [COA]COA0 =[T246]COA (GCOA) !Delete
  CODTXS A*5 Funds code
  CPY CPY Company -> [CPY]CPY0 =[T246]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[T246]CREUSR (AUTILIS) !Other
  DATEND D4 Depr. end date
  DATSTR D4 Depr. st. date
  DPRCUM MD1 Depreciation
  DPRDSP MD1 Depr. on disposal
  DPREND MD1 End depreciation
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRSTR MD1 Start depreciation
  FCY FCY Site -> [FCY]FCY0 =[T246]FCY (FACILITY) !Delete
  GAC GAC Account -> [GAC]GAC0 =COA;GAC (GACCOUNT) !Delete
  NETEND MD1 End net value
  NETSTR MD1 Start net value
  NETVAL MD1 Net value
  POSTXS L*8 Funds line
  TRFVAL MD1 Transfer
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[T246]UPDUSR (AUTILIS) !Other

## TMPFASLIST (TFL) - Temporary print key table
Keys (first = PK; D = duplicates allowed): TFL0 EDTNUM+AASREF; TFL1 EDTNUM+CPY+FCY+AASREF
Fields:
  AASDES1 DCO Description
  AASIPTDAT D4 Allocation date
  AASREF AAS Asset -> [FAS]FAS0 =[TFL]AASREF (FXDASSETS) !BSRA
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[TFL]ACCCOD (GACCCODE) !BSRA
  ACCDES DCO Accounting code title
  ACGCUR CUR CoA curr. -> [TCU]TCU0 =[TFL]ACGCUR (TABCUR) !BSRA
  ACGETRNOT MD1 Receipt value ex-tax
  ACGGRP FAM Family -> [FAM]FAM0 =[TFL]ACGGRP (FASFAM) !BSRA
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =[TFL]CCE (CACCE) !BSRA act:ANA
  CCEDES DCO Description
  CMP AAS Main -> [FAS]FAS0 =[TFL]CMP (FXDASSETS) !BSRA
  CMPSTA M*15 Status [menu 3229: 1=Autonomous,2=Principal,3=Component,4=Component waiting assignment,5=Pool,6=LVA]
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart of accounts -> [COA]COA0 =[TFL]COA (GCOA) !BSRA
  CPY CPY Company -> [CPY]CPY0 =[TFL]CPY (COMPANY) !BSRA
  CPYNAM NAM Company name
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TFL]CREUSR (AUTILIS) !Other
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DIE DIE Dimension type code -> [DIE]DIE0 =[TFL]DIE (GDIE) !BSRA
  DPRBAS MD1 Reval. BS value
  DPRBASIAS MD1 Depreciation base
  DPRBASPCG MD1 Depreciation base
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =[TFL]DSP (CADSP) !BSRA
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPRDAT D4 Deprec end date
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TFL]FCY (FACILITY) !BSRA
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  GAC GAC General account -> [GAC]GAC0 =[TFL]GAC (GACCOUNT) !BSRA
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 =[TFL]IASACC (GACCOUNT) !BSRA
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =[TFL]IASCGU (ATABDIV) !BSRA
  IASCGUDES DCO Description
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[TFL]IASCUR (TABCUR) !BSRA
  IASETRNOT MD1 Receipt value ex-tax
  ISSDAT D4 Issue date
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  OWNTYPDEB DCO Description
  OWNTYPFIN DCO Description
  PURDAT D4 Purchase date
  STRDPRDAT D4 Depre start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TFL]UPDUSR (AUTILIS) !Other

## TMPFASPHY (TPH) - Temp table elem assignment
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): TPH0 NUMLIG
Fields:
  AASQTY QTY Quantity
  AASREF VC9 Asset
  AUUID AUUID Single identifier
  CODLOF VC9 Reference
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPH]CREUSR (AUTILIS) !Other
  MNT MD1 Amount
  NUMLIG C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPH]UPDUSR (AUTILIS) !Other

## TMPLEARNT (TLR) - Temporary table
Keys (first = PK; D = duplicates allowed): TDR0 EDTNUM+CPY
Fields:
  AUUID AUUID Single identifier
  BSENAT M*15(5) Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  BSENATDES DCO(5) Description
  CPY CPY Company -> [CPY]CPY0 =[TLR]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TLR]CREUSR (AUTILIS) !Other
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRPLNDES DCO Description
  EDTNUM L*8 Processing number
  TOTCAPCUM MD1(5) Repaid capital
  TOTCAPEXE MD1(5) Repaid capital
  TOTDPRCUM MD1(5) Depreciations
  TOTDPREXE MD1(5) Depreciations
  TOTFINDPRCUM MD1(5) Financial depre
  TOTFINDPREX MD1(5) Financial depre
  TOTFINEXSCUM MD1(5) Financial costs
  TOTFINEXSEXE MD1(5) Financial costs
  TOTRNTCUM MD1(5) Rental amount
  TOTRNTEXE MD1(5) Rental amount
  TOTVALORI MD1(5) Original value
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TLR]UPDUSR (AUTILIS) !Other

## TMPLISLOF (TLI) - Temporary print key table
Keys (first = PK; D = duplicates allowed): TLI0 EDTNUM+CODLOF+LINLOF; TLI1 EDTNUM+CPY+FCY+CODLOF+LINLOF
Fields:
  AASREF AAS Asset -> [FAS]FAS0 =[TLI]AASREF (FXDASSETS) !BSRA
  ACGGRP FAM Family -> [FAM]FAM0 =[TLI]ACGGRP (FASFAM) !BSRA
  ACGGRPDES DCO Family title
  ACT VC9 Activity
  ADMCOE RAT Admission coef.
  AMTGRA MD1 Subsidy amount
  AMTNOTCPY MD1 Amount - tax
  AMTNOTCUR MD1 Amount - tax
  AMTNOTIAS MD1 IAS tax excl
  AMTVATCPY MD1 Tax amount
  AMTVATCUR MD1 Tax amount
  AMTVATIAS MD1 VAT invoiced
  AMTVATRCPY MD1 VAT recovered
  AMTVATRCUR MD1 Recvd VAT
  AMTVATRIAS MD1 VAT recovered
  ANALIGORI C*3 Ana. line source
  ASJCOE RAT Liability coef.
  AUUID AUUID Single identifier
  BPR BPR Supplier -> [BPR]BPR0 =[TLI]BPR (BPARTNER) !BSRA
  BPRNAM NAM Company name
  BPRVCR A*20 Invoice reference
  BUDINV ADI Investment budget -> [ADI]CODE =[TLI]BUDINV (ATABDIV) !BSRA
  CCE CCE Analytical dimension -> [CCE]CCE0 =[TLI]CCE (CACCE) !BSRA act:ANA
  CCEDES DCO Description
  CODLOF LOF Reference
  CODLOFORI A*20 Original reference
  CONNUM ADI Market no -> [ADI]CODE =[TLI]CONNUM (ATABDIV) !BSRA
  CPMCREORI M*15 Additional source [menu 3107: 1=Purchase invoices,2=BP invoices,3=Journal,4=Payment,5=Import,6=Stock issue]
  CPY CPY Company -> [CPY]CPY0 =[TLI]CPY (COMPANY) !BSRA
  CPYNAM NAM Company name
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TLI]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TLI]CUR (TABCUR) !BSRA
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DATIMP D4 Allocation date
  DATVCR D4 Invoice date
  DEMINV ADI Invest request -> [ADI]CODE =[TLI]DEMINV (ATABDIV) !BSRA
  DES DES Description
  DES2 DCO Description 2
  DIE DIE Dimension type code -> [DIE]DIE0 =[TLI]DIE (GDIE) !BSRA
  DSP DSP Distribution -> [DSP]DSP0 =[TLI]DSP (CADSP) !BSRA
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[TLI]FCY (FACILITY) !BSRA
  FCYNAM NAM Name
  FIYBUD C*4 Fiscal year
  FLGAMTGRA MZS Subsidy strength
  FLGGRA M*4 Subsidized [menu 1: 1=No,2=Yes]
  FLGLIKAAS M*4 Asset link [menu 1: 1=No,2=Yes]
  FLGLOFMAI M*4 Principal expense [menu 1: 1=No,2=Yes]
  FLGRECFVR MZS*4 Force VAT recovered
  FLGVAL M*4 Validated [menu 1: 1=No,2=Yes]
  FLGVATFCR MZS*4 Force VAT
  GAC GAC General account -> [GAC]GAC0 =[TLI]GAC (GACCOUNT) !BSRA
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  GACORI GAC Source CoA account -> [GAC]GAC0 =[TLI]GACORI (GACCOUNT) !BSRA
  IASACC GAC IFRS allocation -> [GAC]GAC0 =[TLI]IASACC (GACCOUNT) !BSRA
  IASACCDES DCO Account heading
  IASACCORI GAC Source IFRS acct -> [GAC]GAC0 =[TLI]IASACCORI (GACCOUNT) !BSRA
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =[TLI]IASCGU (ATABDIV) !BSRA
  IASCGUDES DCO Description
  ITMREF ITM Product -> [ITM]ITM0 =[TLI]ITMREF (ITMMASTER) !BSRA
  JOU JOU Journal -> [JOU]JOU0 =[TLI]JOU (GJOURNAL) !BSRA
  LIGORI L*8 Detail line source
  LINLOF C*4 Line number
  ORDBUY A*20 Order number
  PLNINV ADI Project ref. -> [ADI]CODE =[TLI]PLNINV (ATABDIV) !BSRA
  QTY QTY Quantity
  RATCUR RCU Currency rate
  RATVAT RAT Invd VAT rate
  RATVATREC RAT Recovered VAT
  TAXCOE RAT Taxation coeff
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TYPORI GTE Entry type -> [GTE]GTE0 =[TLI]TYPORI (GTYPACCENT) !BSRA
  TYPVCR M*15 Invoice type [menu 3117: 1=Invoice,2=Credit note,3=Pre-payment,4=To be received,5=Return,6=Early discount/late charge,7=Stock issue]
  UOM UOM Unit -> [TUN]TUN0 =[TLI]UOM (TABUNIT) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TLI]UPDUSR (AUTILIS) !Other
  USRDEN AUS Destination -> [AUS]CODUSR =[TLI]USRDEN (AUTILIS) !BSRA

## TMPLOFGRP (TLG) - Temporary table
Keys (first = PK; D = duplicates allowed): TDE0 EDTNUM+CPY+FCY+AASREF+CODLOF+LINLOF; TDE1 EDTNUM+CODLOF+LINLOF; TDE2 EDTNUM+AASREF (D)
Fields:
  AASDES1 DCO Description
  AASIPTDAT D4 Allocation date
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DCO Accounting code title
  ACGCUR CUR CoA curr. -> [TCU]TCU0 =[TLG]ACGCUR (TABCUR) !Other
  ACGETRNOT MD1 Receipt value ex-tax
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  ACT VC9 Activity
  AMTNOTCPY MD1 Amount - tax
  AMTVATCPY MD1 Tax amount
  AMTVATRCPY MD1 VAT recovered
  AUUID AUUID Single identifier
  BPR BPR Supplier -> [BPR]BPR0 =[TLG]BPR (BPARTNER) !Other
  COA COA Chart of accounts -> [COA]COA0 =[TLG]COA (GCOA) !Delete
  CODLOF VC9 Reference
  COURS RCU Currency rate
  CPY CPY Company -> [CPY]CPY0 =[TLG]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREORI M*15 Entry origin [menu 3162: 1=Transactional entry,2=Split,3=Return,4=Interface,5=Others,6=Intra-group sale,7=Automatic creation,8=Expense grouping]
  CREUSR AUS Creation user -> [AUS]CODUSR =[TLG]CREUSR (AUTILIS) !Other
  DATCOURS D4 Rate date
  DATIMP D4 Allocation date
  DATVCR D4 Invoice date
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  DES DES Description
  DEVRPT CUR Reporting currency -> [TCU]TCU0 =[TLG]DEVRPT (TABCUR) !Other
  EDTNUM L*8 Processing number
  FCY FCY Financial site -> [FCY]FCY0 =[TLG]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FLGLIKAAS M*4 Asset link [menu 1: 1=No,2=Yes]
  FLGLOFMAI M*4 Principal expense [menu 1: 1=No,2=Yes]
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[TLG]IASCUR (TABCUR) !Other
  IASETRNOT MD1 Receipt value ex-tax
  ITSDAT D4 In service date
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  IVCVATRAT RAT Invd VAT rate
  IVCVATRATI RAT Invd VAT rate
  LED M*15 Ledger [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LINLOF C*4 Line number
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PURDAT D4 Purchase date
  QTY QTY Quantity
  TYPCUR M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TLG]UPDUSR (AUTILIS) !Other

## TMPMASFA2 (MF2) - Temporary table asset actions
Keys (first = PK; D = duplicates allowed): MF10 TRTNUM+OBJREF; MF11 TRTNUM+CPY+OBJREF
Fields:
  AASIND A*1 Grouping indicator
  AUUID AUUID Single identifier
  CCNCADDEV MD1 Amortization variance act:CCN
  CCNCADEXC MD1 Amortization excess act:CCN
  CCNINICUM MD1 Initial fund act:CCN
  CCNTRFCAD MD1 Forwarded amortization act:CCN
  CCNTRFCUM MD1 Forwarded funds act:CCN
  CCNTRFGRT MD1 Forwarded subsidy act:CCN
  CCNTRFRPR MD1 Forwarded provision act:CCN
  CPY CPY Company -> [CPY]CPY0 =[MF2]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MF2]CREUSR (AUTILIS) !Other
  DPET MD1 Theo charge
  EXCCUM MD1 Total excep. amt
  EXCCUMT MD1 Exc FY-1 theo
  FCY FCY Financial site -> [FCY]FCY0 =[MF2]FCY (FACILITY) !Delete
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  IMLRVETRF MD1 Impair. rev. - exc depr.
  MSGERR A*100 Message
  OBJREF VC9 Asset
  OBJREFN AAS Asset reference -> [FAS]FAS0 =[MF2]OBJREFN (FXDASSETS) !Delete
  OBJREFO AAS Srce ref for asset -> [FAS]FAS0 =[MF2]OBJREFO (FXDASSETS) !Delete
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PEREXCDPRT MD1 Excep per deprec T
  PERTRFCUM MD1 Impair. loss rev. transf P-1
  RNWVAL MD1 Renewal val. act:CCN
  RVERPRVAL MD1 Prov. to reverse act:CCN
  TRTNUM L*8 Processing number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MF2]UPDUSR (AUTILIS) !Other

## TMPMASFAS (MFS) - Temporary table asset actions
Notes: differs in V9.0 P12 (diff: AT3_TMPMASFAS.htm)
Keys (first = PK; D = duplicates allowed): MFS0 TRTNUM+OBJREF; MFS1 TRTNUM+CPY+OBJREF; MFS2 TRTNUM+AASIND+OBJREF; MFS3 TRTNUM+AASIND+OBJREFO (D)
Fields:
  AASBUS VC9 Activity
  AASBUSO VC9 Activity
  AASDES1 DCO Description
  AASDES1N DCO Description
  AASDES2 DCO Description 2
  AASDES2N DCO Description 2
  AASDESO DCO Description
  AASIND A*1 Grouping indicator
  AASIPTDAT D4 Allocation date
  AASORINBV MD1 NV IGS source asset
  AASQTY QTY Quantity
  AASQTYN QTY Quantity
  AASTYP M*15 Type [menu 3151: 1=Tangible,2=Intangible,3=Goodwill,4=Financial,5=Investment properties,6=Biological assets]
  AASUOM UOM Unit -> [TUN]TUN0 =[MFS]AASUOM (TABUNIT) !Delete
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCCODO CAC Accounting code -> [CAC]CAC0 =[V]GVML_COGIMMO;ACCCODO;[V]GSUPCLE (GACCCODE) !Other
  ACGBSEVAL MD1 CoA bal sht value
  ACGCPLDED MD1 Add deduc VAT CoA
  ACGCUR CUR CoA curr. -> [TCU]TCU0 =[MFS]ACGCUR (TABCUR) !Other
  ACGETRNOT MD1 Receipt value ex-tax
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGREVVAT MD1 CoA VAT repayment
  ADMCOE RAT Admission coef.
  ADMCOEF RAT Admission coef.
  ADMCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  ADMCOEFO RAT Admission coef.
  ADMCOER RAT Admission coef.
  ASJCOE RAT Liability coef.
  ASJCOEF RAT Liability coef.
  ASJCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  ASJCOEFO RAT Liability coef.
  ASJCOER RAT Liability coef.
  AUUID AUUID Single identifier
  BRDPRC RAT Distribution %
  BSEVAL MD1 Init bal sht value
  BUY BPR Buyer -> [BPR]BPR0 =[MFS]BUY (BPARTNER) !Other
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Delete act:ANA
  CCEO CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Delete act:ANA
  CCLTRF M*1 Cancellation [menu 1: 1=No,2=Yes]
  CCNACTCOD CCA Update code act:CCN
  CCNACTCODO CCA Update code act:CCN
  CCNREF CCN Concession contract -> [CCN]CCN0 =[MFS]CCNREF (CONCESSION) !Other act:CCN
  CMP AAS Main -> [FAS]FAS0 =[MFS]CMP (FXDASSETS) !Delete
  CMP1 AAS Main -> [FAS]FAS0 =[MFS]CMP1 (FXDASSETS) !Delete
  CMPORI AAS Main source -> [FAS]FAS0 =[MFS]CMPORI (FXDASSETS) !Delete
  CMPSTA M*15 Status [menu 3229: 1=Autonomous,2=Principal,3=Component,4=Component waiting assignment,5=Pool,6=LVA]
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[MFS]CPY (COMPANY) !Delete
  CRBGRAAMT MD1 Reintegrtd amount
  CRBGRACUM MD1 Reintegration total
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MFS]CREUSR (AUTILIS) !Other
  DATEFF D4 Deprec. bill date
  DATISSPST D4 Issue date
  DEDCOE RAT Deduction coef
  DEDCOEF RAT Deduction coef
  DEDCOEFO RAT Deduction coef
  DEDCOER RAT Deduction coef
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTI MD1 VAT recovered
  DEDVATFLG MZS*4 Forced rec VAT
  DEDVATFLGI MZS*4 Forced rec VAT
  DEDVATRAT RAT Recovered VAT rate
  DEDVATRATI RAT Recovered VAT rate
  DERRVEISS MD1 Book vs tax rev./disposal
  DIE DIE Dimension type code -> [DIE]DIE0 =[MFS]DIE (GDIE) !Other act:ANA
  DPM DPM Depreciation method
  DPMO DPM Depreciation method
  DPMT DPM Theoretical method used
  DPRBAS MD1 Reval. BS value
  DPRBASO MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRCUMFLG M*1 FYR forc deprec tot [menu 1: 1=No,2=Yes]
  DPRCUMO MD1 FY depre total
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Delete
  DSPO DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Delete
  ETRNAT M*15 Recpt nature [menu 3157: 1=Purchase,2=Internal production,3=Partial provision for asset,4=Merger,5=Split,6=Intra-group sales,7=Lease buyback]
  EXECLOCUIO MD1 Init cuml clos FY
  EXECLOCUMI MD1 Init cuml clos FY
  EXECLOCUMT MD1 Theo cumul clos FY
  EXECLOCUTO MD1 Theo cumul clos FY
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXEIMLCUMO MD1 Cumulated exp. Y-1
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXERVECUM MD1 Acc. impair. rev. FY-1
  EXERVECUMO MD1 Acc. impair. rev. FY-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  EXETRFCUMO MD1 Depr rec transf FYR-1
  EXTIMLTYP ADI Impair. ext. reason -> [ADI]CODE =516;EXTIMLTYP (ATABDIV) !RTZ
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  EXTSALAMT MD1 Expected sale amount
  FCY FCY Financial site -> [FCY]FCY0 =[MFS]FCY (FACILITY) !Delete
  FCYO FCY Financial site -> [FCY]FCY0 =[MFS]FCYO (FACILITY) !Delete
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGCLC M*4 Asset to calculate [menu 1: 1=No,2=Yes]
  FLGCNXCLC M*4(11) Context to calculate [menu 1: 1=No,2=Yes]
  FLGCNXFLX A*11 Generated flows
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GAL MD1(15) +/- value
  GALINIAMT MD1 Initial amt +/- value
  GALREFBAS MD1 Ref basis+/- value
  GRAAMT MD1 Subsidy amount
  GRUGAL MD1(15) Intra-group +/- val
  GRUTAXBAS MD1 IGS tax basis
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASBSEVAL MD1 IFRS bal sht val
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete
  IASCGUO ADI UGT -> [ADI]CODE =613;IASCGUO (ATABDIV) !Delete
  IASCPLDED MD1 IAS/IFRS add ded VAT
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[MFS]IASCUR (TABCUR) !Other
  IASCURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  IASDEV MD1 IAS bal sht var val
  IASETRNOT MD1 Receipt value ex-tax
  IASRATCUR RCU Currency rate
  IASREGCUM MD1 VAT adj total
  IASREVVAT MD1 IFRS VAT repayment
  IASVATREG MD1 IAS/IFRS tax adjust
  IML MD1 Impairment
  IMLANNFLG M*20 Deprec. canceln flag [menu 1: 1=No,2=Yes]
  IMLBLC MD1 Impairment loss balance
  IMLBLCO MD1 Impairment loss balance
  IMLO MD1 Impairment
  IMLRVE MD1 Impairment loss reversal
  IMLRVEISS MD1(15) Impair. rev./disposal
  IMLRVELIM MD1 Reversal cap
  IMLRVEO MD1 Impairment loss reversal
  IMLTYP M*15 Impairment loss type [menu 3280: 1=Exceptional,2=A voir]
  INTIMLTYP ADI Intern.reason -> [ADI]CODE =519;INTIMLTYP (ATABDIV) !RTZ
  ISRVAL MD1 Insurance value
  ISSAMT MD1(15) Disposal amount
  ISSDAT D4 Issue date
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  ISSVATAMT MD1 VAT due on disposal
  ISSVATRAT RAT Disposal VAT rate
  ISSVATTRF MD1 Transferable VAT
  ISSVATTRFI MD1 Transferable VAT
  ITSDAT D4 In service date
  IVCSALISS A*20 Invoice reference
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTI MD1 VAT invoiced
  IVCVATFLG MZS*4 Invoiced VAT forced
  IVCVATFLGI MZS*4 Invoiced VAT forced
  IVCVATRAT RAT Invd VAT rate
  LNGGAL MD1(15) Long term +/- value
  MSGERR A*100 Message
  MVTDAT D4 Transfer date
  NBV MD1 Net value
  NBVO MD1 Net value
  NBVT MD1 Theor net value
  NBVTO MD1 Theor net value
  NSPVAL MD1 Market value
  NSPVALO MD1 Prev market value
  OBJREF VC9 Asset
  OBJREFN AAS Asset reference -> [FAS]FAS0 =[MFS]OBJREFN (FXDASSETS) !Other
  OBJREFO AAS Srce ref for asset -> [FAS]FAS0 =[MFS]OBJREFO (FXDASSETS) !Other
  OBYRNWCON M*4 CRO flag [menu 1: 1=No,2=Yes] act:CCN
  OBYRNWCONO M*4 CRO flag [menu 1: 1=No,2=Yes] act:CCN
  ORIPURAMT MD1 IGS src asst purc amt
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PCGDEV MD1 CoA bal sht var val
  PERCLOCUIO MD1 Init cumul per clos
  PERCLOCUM MD1 Periodic total P-1
  PERCLOCUMI MD1 Init cumul per clos
  PERCLOCUMO MD1 Periodic total P-1
  PERCLOCUMT MD1 Theo cumul clos per
  PERCLOCUTO MD1 Theo cumul clos per
  PERCLOEXC MD1 Office P-1 amt excep.
  PERCLOEXCI MD1 Acc P-1 exc depr I
  PERCLOEXCO MD1 Office P-1 amt excep.
  PERCLOEXCT MD1 Acc P-1 exc depr T
  PERCLOEXIO MD1 Acc P-1 exc depr I
  PERCLOEXTO MD1 Acc P-1 exc depr T
  PERENDDAT D4 Period end date
  PERIMLCUM MD1 Depre total P-1
  PERIMLCUMO MD1 Depre total P-1
  PERREFCLC D4 Calculation period
  PERREFCLCT D4 Per. for T calculation
  PERRVADEV MD1 Closed P total reval. surpl.
  PERRVECUM MD1 Acc. impair. rev. P-1
  PERRVECUMO MD1 Acc. impair. rev. P-1
  PERSTRDAT D4 Period start date
  PURDAT D4 Purchase date
  PURNAT M*15 Purch nature [menu 3152: 1=New,2=Second-hand]
  PYBVATTYP M*15 VAT repayment [menu 3160: 1=1/5th rule,2=1/10th rule,3=1/20th rule,4=No VAT adjustment,5=Deductible VAT amount adjustment: increase,6=Deductible VAT amount adjustment: decrease]
  R76COE COE Reval. coeff. 76
  REGTVAFLG M*1 VAT adjustment [menu 1: 1=No,2=Yes]
  REGUL MD1 Tax adjustment
  REGULI MD1 Tax adjustment
  RENTRF ADI Reason -> [ADI]CODE =612;RENTRF (ATABDIV) !Delete
  RNWDAT D4 Renewal date act:CCN
  RNWDATFLG M*4 Forced renewal date [menu 1: 1=No,2=Yes] act:CCN
  RNWDATFLGO M*4 Forced renewal date [menu 1: 1=No,2=Yes] act:CCN
  RNWDATO D4 Renewal date act:CCN
  RNWFLG M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RNWFLGO M*4 ERO flag [menu 1: 1=No,2=Yes] act:CCN
  RPLVAL MD1 New value
  RSDVAL MD1 Residual value
  RVAAMT MD1 Revaluation amount
  RVAAMTO MD1 Revaluation amount
  RVAAPR A*15 Evaluator
  RVACMT DCO Comment
  RVACOE COE Revaluation coef
  RVACOEREF A*20 Table reference
  RVADAT D4 Revaluation date
  RVATIADAT M*15 Reval. effective start [menu 3273: 1=FY start,2=Period start,3=FY end]
  RVATYP M*15 Revaluation type [menu 3253: 1=Coefficient,2=Index,3=Market value]
  SALCLSDAT D4 Asset date for sale
  SHOGAL MD1(15) Short term +/- value
  STABILTYP M*15 Stability type [menu 3156: 1=Fixed,2=General installation,3=Mobile]
  STRDPRDAT D4 Depre start date
  TAXBAS MD1 Tax basis
  TAXCOE RAT Taxation coeff
  TAXCOEF RAT Taxation coeff
  TAXCOEFGLO M*4 Global adjust. index [menu 1: 1=No,2=Yes]
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TAXCOEFO RAT Taxation coeff
  TAXCOER RAT Taxation coeff
  TAXTYP M*15 Tax type [menu 3158: 1=BNPTF,2=BPTF,3=Ex-field]
  THESLI DUR Theo holding duratn
  TPAFLG M*4 Remittance with payment [menu 1: 1=No,2=Yes] act:CCN
  TPAFLGO M*4 Remittance with payment [menu 1: 1=No,2=Yes] act:CCN
  TRTNUM L*8 Processing number
  UNLINK M*4 Undo [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MFS]UPDUSR (AUTILIS) !Other
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Other
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Other
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Other
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Other
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Other
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Other
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Other
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Other
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Other
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Other
  USRFLDC1 COE Free field 1 coef
  USRFLDC2 COE Fr field coeff 2
  USRFLDD1 D4 Free field date 1
  USRFLDD2 D4 Free field date 2
  USRFLDD3 D4 Free field date 3
  USRFLDD4 D4 Free field date 4
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount
  VALNET MD1 Net value
  VATREGAMT MD1 VAT adj amount
  VATREGCUM MD1 VAT adj total
  VATREGDAT D4 Reference date
  VATREGDED MD1 Deduct. VAT adjust - CoA
  VATREGDEDI MD1 Deduct VAT adjust - IAS
  VATRSD DUR Residual duration
  VATYEAFLG M*4 Yearly adjust. index [menu 1: 1=No,2=Yes]

## TMPMASLCK (TML) - Mass action table lock
Keys (first = PK; D = duplicates allowed): TML0 TRTNUM+OBJREF (D); TML1 TRTNUM+OBJREF+OBJLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TML]CREUSR (AUTILIS) !Other
  OBJAMT DCB*15.6(5) Amounts
  OBJCPY CPY Company -> [CPY]CPY0 =[TML]OBJCPY (COMPANY) !Delete
  OBJLIN C*4 Line number
  OBJMAIN M*1 Principal objt [menu 1: 1=No,2=Yes]
  OBJREF VC9 Reference
  OBJSYM A*20 Symbol
  OBJTYP M*1 Object type [menu 3141: 1=Expense,2=Asset,3=Subsidy,4=Lease contract,5=Physical asset count,6=Physical asset,7=Concession]
  TRTNUM L*8 Processing number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TML]UPDUSR (AUTILIS) !Other

## TMPMASLEA (TLE) - Contract actions temp table
Keys (first = PK; D = duplicates allowed): MFS0 TRTNUM+OBJREF; MFS1 TRTNUM+CPY+OBJREF
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGLOCF;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BSENAT M*15 Bal sht line [menu 3226: 1=Land & Construction,2=Transport equipment,3=Equipment and tools,4=IT/office/ furniture equip.,5=Layout and installation]
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CPY CPY Company -> [CPY]CPY0 =[TLE]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[TLE]CUR (TABCUR) !Block
  CURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  DIE DIE Dimension type code -> [DIE]DIE0 =[TLE]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENDLEADAT D4 Contrct end date
  ENDPERDAT D4 Period end
  FCY FCY Financial site -> [FCY]FCY0 =[TLE]FCY (FACILITY) !Delete
  FCYO FCY Financial site -> [FCY]FCY0 =[TLE]FCYO (FACILITY) !Delete
  FINDPR MD1 Financial depre
  FINEXS MD1 Financial cost
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  LEAAMT MD1 Capital amount
  LEACUR CUR Funding currency -> [TCU]TCU0 =[TLE]LEACUR (TABCUR) !Block
  LEADES DCO Description 1
  LEANAT M*15 Nature [menu 3166: 1=Fixed assets,2=Movable assets]
  LEAORI M*15 Source [menu 3155: 1=New contract,2=Transferred contract]
  LEAREF VC9 Lse contract ref.
  LEASTA M*15 Status [menu 3227: 1=to be validated,2=in process,3=completed,4=buyback,5=terminated,6=sold]
  LEATYP M*15 Contract type [menu 3224: 1=Lease,2=Long term rent,3=Rent]
  LES BPR Lessor -> [BPR]BPR0 =[TLE]LES (BPARTNER) !Block
  MSGERR A*100 Message
  MVTDAT D4 Prc date
  OBJREF VC9 Contract
  PAYDAT D4 Payment date
  PAYREF A*20 Payment ref
  RNTAMT MD1 Rental amount
  STRLEADAT D4 Contrct start date
  STRPERDAT D4 Period start
  TRMLEADAT D4
  TRTNUM L*8 Processing number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TMPMASLOF (MLF) - Temporary table
Keys (first = PK; D = duplicates allowed): MFS0 TRTNUM+OBJREF; MFS1 TRTNUM+CPY+OBJREF
Fields:
  ACGCUR CUR CoA curr. -> [TCU]TCU0 =[MLF]ACGCUR (TABCUR) !Block
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Block
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[MLF]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MLF]CREUSR (AUTILIS) !Other
  FCY FCY Financial site -> [FCY]FCY0 =[MLF]FCY (FACILITY) !Delete
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCUR CUR IFRS curr. -> [TCU]TCU0 =[MLF]IASCUR (TABCUR) !Block
  IASCURTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  IASRATCUR RCU Currency rate
  MSGERR A*100 Message
  OBJREF VC9 Asset
  OBJREFN AAS Asset reference -> [FAS]FAS0 =[MLF]OBJREFN (FXDASSETS) !Block
  OBJREFO AAS Srce ref for asset -> [FAS]FAS0 =[MLF]OBJREFO (FXDASSETS) !Block
  TRTNUM L*8 Processing number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MLF]UPDUSR (AUTILIS) !Other
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## TMPMASPHY (MPY) - Temporary table actions elem
Notes: activity code PHY
Keys (first = PK; D = duplicates allowed): MFS0 TRTNUM+OBJREF; MFS1 TRTNUM+CPY+OBJREF
Fields:
  AASREF A*20 Assignment asset
  AUUID AUUID Single identifier
  CCLTRF M*1 Cancellation [menu 1: 1=No,2=Yes]
  CMPSTA M*15 Status [menu 3229: 1=Autonomous,2=Principal,3=Component,4=Component waiting assignment,5=Pool,6=LVA]
  CPY CPY Company -> [CPY]CPY0 =[MPY]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MPY]CREUSR (AUTILIS) !Other
  DNUMRECEP D4 Receipt date
  FCY FCY Financial site -> [FCY]FCY0 =[MPY]FCY (FACILITY) !Delete
  FCYO FCY Financial site -> [FCY]FCY0 =[MPY]FCYO (FACILITY) !Delete
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete
  IASCGUO ADI UGT -> [ADI]CODE =613;IASCGUO (ATABDIV) !Delete
  ISSAMT MD1(15) Disposal amount
  ISSDAT D4 Issue date
  ISSDATRUL M*30 Disposal date rule [menu 3274: 10 values, see local-menus.md]
  ISSTYP M*15 Disposal reason [menu 3159: 1=Sales,2=Scrap,3=Intra-group sale,4=Stolen or disappeared,5=Lease contract end,6=Partial acquisition,7=Merger,8=Split,9=Lease contract end,10=Cancelled contract,11=Imported asset,12=Renewal,13=Transferred to grantor]
  ITSDAT D4 In service date
  LOC LCT Location -> [LCT]LCT0 =[MPY]LOC (PHYLCT) !Block
  LOCO LCT Location -> [LCT]LCT0 =[MPY]LOCO (PHYLCT) !Block
  MSGERR A*100 Message
  MVT M*30(4) Pending movements [menu 3275: 1=None,2=Disposal,3=Disposal cancellation,4=Geographic transfer,5=Geographic transfer cancellation]
  MVTDAT D4 Transfer date
  MVTFCY FCY(4) Dest. financial site -> [FCY]FCY0 =[MPY]MVTFCY (FACILITY) !Block
  MVTGEO BLS(4) Destination geo site -> [FCY]FCY0 =[MPY]MVTGEO (FACILITY) !Block
  MVTLOC LCT(4) Dest. location -> [LCT]LCT0 =[MPY]MVTLOC (PHYLCT) !Block
  OBJREF VC9 Asset
  PHYDES1 DCO Description
  PHYDES1N DCO Description
  PHYDES2 DCO Description 2
  PHYDES2N DCO Description 2
  PHYDESO DCO Description
  RENTRF ADI Reason -> [ADI]CODE =612;RENTRF (ATABDIV) !Delete
  RVAAPR A*15 Evaluator
  RVACMT DCO Comment
  TRFDAT D4 Last transfer
  TRTNUM L*8 Processing number
  UNLINK M*4 Undo [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MPY]UPDUSR (AUTILIS) !Other
  USRFLDA1 ADI Free field 1 -> [ADI]CODE =REFTAB1;USRFLDA1 (ATABDIV) !Block
  USRFLDA10 ADI Free field 10 -> [ADI]CODE =REFTAB10;USRFLDA10 (ATABDIV) !Block
  USRFLDA2 ADI Free field 2 -> [ADI]CODE =REFTAB2;USRFLDA2 (ATABDIV) !Block
  USRFLDA3 ADI Free field 3 -> [ADI]CODE =REFTAB3;USRFLDA3 (ATABDIV) !Block
  USRFLDA4 ADI Free field 4 -> [ADI]CODE =REFTAB4;USRFLDA4 (ATABDIV) !Block
  USRFLDA5 ADI Free field 5 -> [ADI]CODE =REFTAB5;USRFLDA5 (ATABDIV) !Block
  USRFLDA6 ADI Free field 6 -> [ADI]CODE =REFTAB6;USRFLDA6 (ATABDIV) !Block
  USRFLDA7 ADI Free field 7 -> [ADI]CODE =REFTAB7;USRFLDA7 (ATABDIV) !Block
  USRFLDA8 ADI Free field 8 -> [ADI]CODE =REFTAB8;USRFLDA8 (ATABDIV) !Block
  USRFLDA9 ADI Free field 9 -> [ADI]CODE =REFTAB9;USRFLDA9 (ATABDIV) !Block
  USRFLDM1 MD1 Free field amount 1
  USRFLDM2 MD1 Free field amount 2
  USRFLDM3 MD1 Free field amount 3
  USRFLDM4 MD1 Free field amount 4
  USRFLDM5 MD1 Free field amount 5
  USRFLDM6 MD1 Free field 6 amount

## TMPPLNFAS (TPF) - Temporary table schedule actions
Keys (first = PK; D = duplicates allowed): TPF0 TRTNUM+OBJREF+DPRPLN
Fields:
  ACLCOE RA1 Acceleration coeff.
  ACLCOEO RA1 Acceleration coeff.
  ALWAMT MD1 Spc FYR rule amt
  ALWAMTFLG M*4 Forc spc FYR rule amt [menu 1: 1=No,2=Yes]
  ALWAMTO MD1 Spc FYR rule amt
  ALWCOD M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  ALWCODO M*15 Spec rule type [menu 3168: 19 values, see local-menus.md]
  AUUID AUUID Single identifier
  BSEVAL MD1 Init bal sht value
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CPY CPY Company -> [CPY]CPY0 =[TPF]CPY (COMPANY) !Delete
  CRBVEHCOD ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCOD (ATABDIV) !Block
  CRBVEHCODO ADI Vehicle reint cap -> [ADI]CODE =531;CRBVEHCOD (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPF]CREUSR (AUTILIS) !Other
  DPM DPM Depreciation method
  DPMI DPM Initial method used
  DPMIO DPM Initial method used
  DPMO DPM Depreciation method
  DPMT DPM Theoretical method used
  DPMTO DPM Theoretical method used
  DPRBAS MD1 Reval. BS value
  DPRBASO MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRCUMFLG M*4 FYR forc deprec tot [menu 1: 1=No,2=Yes]
  DPRCUMT MD1 FY depr total
  DPRDUR DUR Depre. durn
  DPRDURO DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DPRRAT2 RA1 Depreciation rate
  DPRRAT2O RA1 Depreciation rate
  DPRRATFLG M*4 Forced deprec rate [menu 1: 1=No,2=Yes]
  DPRRATFLGO M*4 Forced deprec rate [menu 1: 1=No,2=Yes]
  DPRRATO RA1 Depreciation rate
  ENDDPRDAT D4 Deprec end date
  ENDDPRDATO D4 Deprec end date
  ENDDPRFLG M*4 Forced deprec. amt [menu 1: 1=No,2=Yes]
  ENDDPRFLGO M*4 Forced deprec. amt [menu 1: 1=No,2=Yes]
  EXERVADEV MD1 Closed FY total reval. surpl.
  FIYENDDAT D4 Fiscal year end date
  FIYENDDAT2 D4 Fiscal year end date
  FIYENDDAT3 D4 Fiscal year end date
  FIYQTY QTY FY units
  FIYQTYO QTY FY units
  FIYSTRDAT D4 Fiscal year start date
  FLGERR M*1 Flag [menu 1: 1=No,2=Yes]
  FLGMOD M*1 Flag [menu 1: 1=No,2=Yes]
  GAL MD1 +/- value
  IML MD1 Impairment
  IMLBLC MD1 Impairment loss balance
  IMLCLC MD1 Calc. impairment loss
  IMLRVE MD1 Impairment loss reversal
  IMLRVECLC MD1 Calculation repeat
  IMLRVELIM MD1 Reversal cap
  ITSDAT D4 In service date
  LNGGAL MD1 Long term +/- value
  LSTCLODAT D4 Closing date
  MSGERR A*100 Message
  MTCDEVADJ M*15 Rec. meth chge var [menu 3169: 1=Carryforward,2=Exceptional depre fiscal year,3=Exceptional depre period,4=Charge fiscal year,5=Charge period]
  MTCTIADAT D4 Chge effective date
  MTCTIATYP M*15 Chg effective start [menu 3268: 1=Depreciation start,2=FY start,3=Period start]
  NBV MD1 Net value
  NBVO MD1 Net value
  NBVT MD1 Theor net value
  NSPVAL MD1 Market value
  OBJREF VC9 Asset
  PERCLOCUM MD1 Periodic total P-1
  PERENDDAT D4 Period end date
  PERENDDAT2 D4 Period end date
  PERENDDAT3 D4 Period end date
  PERQTY QTY Period unit
  PERQTYCUM QTY Total period P-1 OPE
  PERQTYO QTY Period unit
  PERREFCLC D4 Calculation period
  PERREFCLCI D4 Per. for I calculation
  PERREFCLCT D4 Per. for T calculation
  PERRVADEV MD1 Closed P total reval. surpl.
  PERSTRDAT D4 Period start date
  PLNCUR CUR Currency -> [TCU]TCU0 =[TPF]PLNCUR (TABCUR) !Delete
  PRATYP M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  PRATYPFLG M*4 Prorata [menu 1: 1=No,2=Yes]
  PRATYPO M*15 Prorata [menu 3105: 1=Day,2=Month,3=Week,4=1/2 year,5=1/2 month,6=1/2 quarter]
  RATCUR RCU Currency rate
  RSDQTY QTY Start period residual duratn OPE
  RSDQTYO QTY Start period residual duratn OPE
  RSDVAL MD1 Residual value
  RSDVALO MD1 Residual value
  RVAAMT MD1 Revaluation amount
  RVACOE COE Revaluation coef
  RVACOEREF A*20 Table reference
  RVADAT D4 Revaluation date
  RVATYP M*15 Revaluation type [menu 3253: 1=Coefficient,2=Index,3=Market value]
  SHOGAL MD1 Short term +/- value
  STRDPRDAT D4 Depre start date
  STRDPRDATO D4 Depre start date
  TRTNUM L*8 Processing number
  UOM UOM Unit -> [TUN]TUN0 =[TPF]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPF]UPDUSR (AUTILIS) !Other
  USRDAT D4 Date
  USRLIB A*50 Text
  USRMNT MD1 Amount

## TMPREEVAL (TRV) - Temp table report DEPREEVAL
Keys (first = PK; D = duplicates allowed): TRV0 EDTNUM+CPY+FCY+AASREF; TRV1 EDTNUM+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DES Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  BSEVAL MD1 Init bal sht value
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart code -> [COA]COA0 =[TRV]COA (GCOA) !Other
  CPY CPY Company -> [CPY]CPY0 =[TRV]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TRV]CREUSR (AUTILIS) !Other
  DPRBAS MD1 Reval. BS value
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPRDAT D4 Deprec end date
  EXERVADEV MD1 Closed FY total reval. surpl.
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TRV]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete act:IAS
  IASCGUDES DCO Description
  ISSDAT D4 Issue date
  NBV MD1 Net value
  NSPVAL MD1 Market value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERENDDAT D4 Period end date
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PERRVACUM MD1 Acc. closed ps reval amt
  PERRVADEV MD1 Closed P total reval. surpl.
  RSDVAL MD1 Residual value
  RSVRVA MD1 Revaluation surplus
  RVAAMT MD1 Revaluation amount
  RVAAPR ADI Evaluator -> [ADI]CODE =627;RVAAPR (ATABDIV) !Other
  RVAAPRDES DCO Description
  RVACOE COE Revaluation coef
  RVACRB MD1 Revaluation reversal
  RVADAT D4 Revaluation date
  STRDPRDAT D4 Depre start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TRV]UPDUSR (AUTILIS) !Other

## TMPSIMDERO (TDS) - Temporary print key table
Keys (first = PK; D = duplicates allowed): TDS0 EDTNUM+CPY+FCY+AASREF+FIYENDDAT+PERENDDAT; TDS1 EDTNUM+AASREF+FIYENDDAT+PERENDDAT
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DES Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[TDS]COA (GCOA) !Other
  CPY CPY Company -> [CPY]CPY0 =[TDS]CPY (COMPANY) !Other
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TDS]CREUSR (AUTILIS) !Other
  CUMANTCPT MD1 Dep. merging FY start
  CUMANTFI MD1 Dep. merging FY start
  DATISSPSTC D4 Issue date
  DATISSPSTF D4 Issue date
  DEROPERCLO MD1 Book vs Tax provision
  DOTCPT MD1 Accounting charge
  DOTFI MD1 Fiscal charge
  DPETC MD1 Theo charge
  DPETF MD1 Theo charge
  DPMC DPM Depreciation method
  DPMF DPM Depreciation method
  DPRBASC MD1 Reval. BS value
  DPRBASF MD1 Reval. BS value
  DPRCUMC MD1 FY depre total
  DPRCUMF MD1 FY depre total
  DPRDURC DUR Depre. durn
  DPRDURF DUR Depre. durn
  DPRRATC RA1 Depreciation rate
  DPRRATF RA1 Depreciation rate
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDAT D4 End date
  ENDDATHORI D4 End
  ENDDPEC MD1 Fiscal Year charge
  ENDDPEF MD1 Fiscal Year charge
  ENDDPETC MD1 Yearly deprec. theo
  ENDDPRDATC D4 Deprec end date
  ENDDPRDATF D4 Deprec end date
  EXCDPRC MD1 FYR except deprec
  EXCDPRF MD1 FYR except deprec
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TDS]FCY (FACILITY) !Other
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYENDDATC D4 Fiscal year end date
  FIYENDDATF D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FIYSTRDATC D4 Fiscal year start date
  FIYSTRDATF D4 Fiscal year start date
  FLGUPDISSC M*4 Modification [menu 1: 1=No,2=Yes]
  FLGUPDISSF M*4 Modification [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 Accounting nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others] act:FAS
  GACDES DCO Account heading
  HORIZON C*4 Horizon
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other
  IASCGUDES DCO Description
  ISSDAT D4 Issue date
  LEG MD1 Legal link amt
  LEGCUMC MD1 Plan E-1 llegal link total
  LEGRVE MD1 Legal link recovery
  LEGRVECUMC MD1 Plan E-1 legal link rec.tot
  NBVC MD1 Net value
  NBVF MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUMC MD1 Periodic total P-1
  PERCLOCUMF MD1 Periodic total P-1
  PERENDDAT D4 Period end date
  PERENDDATC D4 Period end date
  PERENDDATF D4 Period end date
  PERENDDPEC MD1 Period P charge
  PERENDDPEF MD1 Period P charge
  PERLEGCUM MD1 Plan P-1 legal link total
  PERLEGRVE MD1 Plan P-1 legal link rec.tot
  PROVISION MD1 Provision
  REPRISE MD1 Recovery
  REPSOR MD1 Reversal on disposal
  SOLDEBEX MD1 FY start closing
  SOLFINEX MD1 FY end closing
  STRDAT D4 Start date
  STRDPRDATC D4 Depre start date
  STRDPRDATF D4 Depre start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TDS]UPDUSR (AUTILIS) !Other

## TMPSITU (TSI) - Temp. table Report DEPSITU
Keys (first = PK; D = duplicates allowed): TDE0 EDTNUM+CPY+FCY+AASREF; TDE1 EDTNUM+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DCO Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =[TSI]CCE1 (CACCE) !BSRA
  CCE1DES DCO Description
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =[TSI]CCE2 (CACCE) !BSRA
  CCE2DES DCO Description
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =[TSI]CCE3 (CACCE) !BSRA
  CCE3DES DCO Description
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =[TSI]CCE4 (CACCE) !BSRA
  CCE4DES DCO Description
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =[TSI]CCE5 (CACCE) !BSRA
  CCE5DES DCO Description
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =[TSI]CCE6 (CACCE) !BSRA
  CCE6DES DCO Description
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =[TSI]CCE7 (CACCE) !BSRA
  CCE7DES DCO Description
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =[TSI]CCE8 (CACCE) !BSRA
  CCE8DES DCO Description
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =[TSI]CCE9 (CACCE) !BSRA
  CCE9DES DCO Description
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  COA COA Chart code -> [COA]COA0 =[TSI]COA (GCOA) !Other
  CPY CPY Company -> [CPY]CPY0 =[TSI]CPY (COMPANY) !Delete
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TSI]CREUSR (AUTILIS) !Other
  DATISSPST D4 Issue date
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[TSI]DIE (GDIE) !Other
  DPM DPM Depreciation method
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPE MD1 Fiscal Year charge
  ENDDPRDAT D4 Deprec end date
  EXCDPR MD1 FYR except deprec
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TSI]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Delete
  IASCGUDES DCO Description
  IML MD1 P impairment loss
  IMLBLC MD1 Impairment loss balance
  IMLRVE MD1 Impair. loss reversal P
  IMLRVETRF MD1 Impair. rev. - exc depr.
  ISSDAT D4 Issue date
  NBV MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUM MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PERIMLCUM MD1 Depre total P-1
  PERRVACUM MD1 Acc. closed ps reval amt
  PERRVECUM MD1 Acc. impair. rev. P-1
  PERTRFCUM MD1 Impair. loss rev. transf P-1
  RSDVAL MD1 Residual value
  RVAAMT MD1 Revaluation amount
  STRDPRDAT D4 Depre start date
  TCUMENDEXE MD1 Depr. total FY end
  TCUMENDPER MD1 Per end depr total
  TCUMSTREXE MD1 Dep. merging FY start
  TCUMSTRPER MD1 Per st dep total
  TDPEEXCEXE MD1 Except charge
  TDPEEXCPER MD1 Except charge
  TDPEEXE MD1 Fiscal Year charge
  TDPEPER MD1 Charge period
  TIMLBLCEXE MD1 Impair. balance
  TIMLBLCPER MD1 Impair. balance
  TIMLEXE MD1 Impairment
  TIMLPER MD1 Impairment
  TIMLRVEEXE MD1 Depr. reversal
  TIMLRVEISS MD1(15) Impair. rev./disposal
  TIMLRVEPER MD1 Depr. reversal
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TSI]UPDUSR (AUTILIS) !Other

## TMPSITUCUR (TSIC) - Temp. table Report DEPSITU
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TDE0 EDTNUM+CPY+FCY+AASREF; TDE1 EDTNUM+AASREF
Fields:
  AASDES1 DCO Description
  AASREF VC9 Asset
  ACCCOD CAC Accounting code -> [CAC]CAC0 =GVML_COGIMMO;ACCCOD;[V]GSUPCLE (GACCCODE) !Other
  ACCDES DCO Accounting code title
  ACGGRP FAM Family -> [FAM]FAM0 =ACGGRP (FASFAM) !Other
  ACGGRPDES DCO Family title
  AUUID AUUID Single identifier
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =[TSIC]CCE1 (CACCE) !BSRA
  CCE1DES DCO Description
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =[TSIC]CCE2 (CACCE) !BSRA
  CCE2DES DCO Description
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =[TSIC]CCE3 (CACCE) !BSRA
  CCE3DES DCO Description
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =[TSIC]CCE4 (CACCE) !BSRA
  CCE4DES DCO Description
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =[TSIC]CCE5 (CACCE) !BSRA
  CCE5DES DCO Description
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =[TSIC]CCE6 (CACCE) !BSRA
  CCE6DES DCO Description
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =[TSIC]CCE7 (CACCE) !BSRA
  CCE7DES DCO Description
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =[TSIC]CCE8 (CACCE) !BSRA
  CCE8DES DCO Description
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =[TSIC]CCE9 (CACCE) !BSRA
  CCE9DES DCO Description
  CNX M*25 Context [menu 3100: 1=Finance,2=Context 2,3=Context 3,4=Context 4,5=Context 5,6=Context 6,7=Context 7,8=Context 8,9=Context 9,10=Context 10,11=Context 11]
  CNXCUR CUR Currency -> [TCU]TCU0 =[TSIC]CNXCUR (TABCUR) !Other
  COA COA Chart code -> [COA]COA0 =[TSIC]COA (GCOA) !Other
  CPY CPY Company -> [CPY]CPY0 =[TSIC]CPY (COMPANY) !Other
  CPYNAM NAM Company name
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TSIC]CREUSR (AUTILIS) !Other
  DATISSPST D4 Issue date
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[TSIC]DIE (GDIE) !Other
  DPM DPM Depreciation method
  DPRBAS MD1 Reval. BS value
  DPRCUM MD1 FY depre total
  DPRDUR DUR Depre. durn
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  DPRRAT RA1 Depreciation rate
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other
  DSPDES DCO Description
  EDTNUM L*8 Processing number
  ENDDPE MD1 Fiscal Year charge
  ENDDPRDAT D4 Deprec end date
  EXCDPR MD1 FYR except deprec
  EXEIMLCUM MD1 Cumulated exp. Y-1
  EXETRFCUM MD1 Depr rec transf FYR-1
  EXTISSFLG M*4 Provisional disposal [menu 1: 1=No,2=Yes]
  FCY FCY Financial site -> [FCY]FCY0 =[TSIC]FCY (FACILITY) !Other
  FCYNAM NAM Name
  FIYENDDAT D4 Fiscal year end date
  FIYSTRDAT D4 Fiscal year start date
  FLGUPDISS M*4 Disposal modification [menu 1: 1=No,2=Yes]
  GAC GAC General account -> [GAC]GAC0 ="";GAC (GACCOUNT) !Other
  GACACN M*15 CoA nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  GACDES DCO Account heading
  IASACC GAC IFRS allocation -> [GAC]GAC0 ="";IASACC (GACCOUNT) !Other
  IASACCDES DCO Account heading
  IASACN M*15 IFRS nature [menu 2628: 1=Fixed assets in progress,2=Fixed assets in service,3=Cost,4=Others]
  IASCGU ADI UGT -> [ADI]CODE =613;IASCGU (ATABDIV) !Other
  IASCGUDES DCO Description
  IML MD1 P impairment loss
  IMLBLC MD1 Impairment loss balance
  IMLRVE MD1 Impair. loss reversal P
  IMLRVETRF MD1 Impair. rev. - exc depr.
  ISSDAT D4 Issue date
  NBV MD1 Net value
  OWNTYP M*15 Holding type [menu 3171: 1=Owned,2=Rented,3=Leased,4=Provisional,5=Concession,6=Template,7=Cancelled]
  PERCLOCUM MD1 Periodic total P-1
  PERCLOEXC MD1 Office P-1 amt excep.
  PERENDDPE MD1 Period P charge
  PEREXCDPR MD1 Exceptional amortization
  PERIMLCUM MD1 Depre total P-1
  PERRVACUM MD1 Acc. closed ps reval amt
  PERRVECUM MD1 Acc. impair. rev. P-1
  PERTRFCUM MD1 Impair. loss rev. transf P-1
  RATCUR RCU Currency rate
  RPTCUR CUR Print currency -> [TCU]TCU0 =[TSIC]RPTCUR (TABCUR) !Block
  RSDVAL MD1 Residual value
  RVAAMT MD1 Revaluation amount
  STRDPRDAT D4 Depre start date
  TCUMENDEXE MD1 Depr. total FY end
  TCUMENDPER MD1 Per end depr total
  TCUMSTREXE MD1 Dep. merging FY start
  TCUMSTRPER MD1 Per st dep total
  TDPEEXCEXE MD1 Except charge
  TDPEEXCPER MD1 Except charge
  TDPEEXE MD1 Fiscal Year charge
  TDPEPER MD1 Charge period
  TIMLBLCEXE MD1 Impair. balance
  TIMLBLCPER MD1 Impair. balance
  TIMLEXE MD1 Impairment
  TIMLPER MD1 Impairment
  TIMLRVEEXE MD1 Depr. reversal
  TIMLRVEISS MD1(15) Impair. rev./disposal
  TIMLRVEPER MD1 Depr. reversal
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TSIC]UPDUSR (AUTILIS) !Other

## TMPTCHANGE (TCG) - Currency rates temp. table
Keys (first = PK; D = duplicates allowed): TCG0 CHGTYP+CURDEN+CUR+CHGSTRDAT
Fields:
  AUUID AUUID Single identifier
  CHGDIV L*5 Divisor
  CHGRAT RCU Rate
  CHGSTRDAT D Rate date
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCG]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TCG]CUR (TABCUR) !Delete
  CURDEN CUR Destination currency -> [TCU]TCU0 =[TCG]CURDEN (TABCUR) !Delete
  REVCOURS RCU Reverse
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCG]UPDUSR (AUTILIS) !Other

## TRCABX3 (TAB) - Abel X3 logs
Keys (first = PK; D = duplicates allowed): TAB0 NUMACT+CPY+TRITRC+SEQNUM+ERRCOD; TAB1 NUMACT+TRITRC+CPY+SEQNUM
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TAB]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TAB]CREUSR (AUTILIS) !Other
  ERRCOD C*4 Error code
  MSG A*250 Message
  NUMACT L*8 Action number
  SEQNUM L*8 Sequence number
  TRITRC C*4 Log sort
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TAB]UPDUSR (AUTILIS) !Other

## TYPACE (TPE) - Accounting entry types
Keys (first = PK; D = duplicates allowed): TPE0 ACETYP+LEG+CPY; TPE1 LEG+CPY+DPRPLN+ACEGRP+ACETYP (D)
Fields:
  ACCDATFIX D4 Accounting date
  ACCDATRUL M*15 Accounting date [menu 3130: 1=Automatic Journal,2=Start of processed period,3=End of processed period,4=Start of processed FY,5=End of processed FY,6=Start of current period,7=End of current period,8=Entered date,9=Specific date]
  ACEGRP A*10 Group
  ACETYP TPE Entry type -> [TPE]TPE0 =[TPE]ACETYP (TYPACE) !BSRA
  AUUID AUUID Single identifier
  CPTREF M*30 Accounting ledger [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  CPY CPY Company -> [CPY]CPY0 =[TPE]CPY (COMPANY) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DBGMOD M*4 Debugger [menu 1: 1=No,2=Yes]
  DES DCO Description
  DESTRA AX3 Description
  DIRCPTFLG M*4 Immediate accounting [menu 1: 1=No,2=Yes]
  DIRCPTTRA M*4 Log [menu 1: 1=No,2=Yes]
  DIVCRIT A*250 Criteria
  DPRPLN M*2 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  ENAFLG M*1 Active [menu 1: 1=No,2=Yes]
  EVTPLN M*4 Plan [menu 1: 1=No,2=Yes]
  EVTTYP ADI Event type -> [ADI]CODE =952;EVTTYP (ATABDIV) !Delete
  GAU GAU Automatic journal -> [GAU]GAU0 =[TPE]GAU (GAUTACE) !RTZ
  GRA GRA Group entry -> [GRA]GRA0 =[TPE]GRA (GRPAUTACE) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !RTZ
  NBCRIT C*4 Field nb
  PERCLOFLG M*4 Closed period [menu 1: 1=No,2=Yes]
  PERCOUFLG M*4 Current period [menu 1: 1=No,2=Yes]
  PEROPEFLG M*4 Open period [menu 1: 1=No,2=Yes]
  RUPPCEFLG M*4(5) Entry [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  SORTCCE M*4 Preliminary analytical sorting [menu 1: 1=No,2=Yes]
  SORTFLD A*10(5) Sort criteria
  SORTFLDTAB ATB(5) Table for sort field -> [ATB]CODFIC =[TPE]SORTFLDTAB (ATABLE) !Block
  SRCTYP M Source [menu 3213: 1=Event,2=Depreciation,3=Other table,4=Provisions for renewal,5=Variance between plans]
  TABCPT ATB Table to browse -> [ATB]CODFIC =[TPE]TABCPT (ATABLE) !Block
  TABOBJ ATB Table -> [ATB]CODFIC =[TPE]TABOBJ (ATABLE) !Block
  TRTINT A*20 Processing
  TRTSPE ADC Specific processing
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TYPACEINT (TPI) - Accounting entry types
Keys (first = PK; D = duplicates allowed): TPI0 ACETYP+LEG+CPY+TMPFLD+TMPIND
Fields:
  ACETYP TPE Entry type -> [TPE]TPE0 =ACETYP;LEG;CPY (TYPACE) !Other
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TPI]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENALIG M*4 Active [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  NUMLIG C*3 Line no.
  ORICND A*80 Source condition
  ORIEXP A*250 Source expression
  ORIFLD A*10 Source field
  ORITAB ATB Source table -> [ATB]CODFIC =[TPI]ORITAB (ATABLE) !Block
  TMPFLD A*10 Destination
  TMPIND C*4 Index
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TYPACELEG (TPL) - Accounting entry types
Keys (first = PK; D = duplicates allowed): TPL0 ACETYP+LEG+CPY+LEGLIN
Fields:
  ACETYP TPE Entry type -> [TPE]TPE0 =ACETYP;LEG;CPY (TYPACE) !RTZ
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[TPL]CPY (COMPANY) !RTZ
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GTE GTE Entry type -> [GTE]GTE0 =GTE;LEGLIN (GTYPACCENT) !RTZ
  GTEPRO GTE Entry type -> [GTE]GTE0 =GTEPRO;LEGLIN (GTYPACCENT) !RTZ
  JOU JOU Journal -> [JOU]JOU0 =JOU;LEGLIN (GJOURNAL) !RTZ
  JOUPRO JOU Journal -> [JOU]JOU0 =JOUPRO;LEGLIN (GJOURNAL) !RTZ
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !RTZ
  LEGLIN ADI Legislation -> [ADI]CODE =909;LEGLIN (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## VATHIS (VAT) - Tax - history
Keys (first = PK; D = duplicates allowed): VAT0 AASREF+DPRPLN+DATVATREG+TIMSTP; VAT1 AASREF+DPRPLN+VATREGTYP+DATVATREG+TIMSTP
Fields:
  AASBUS VC9 Activity
  AASBUSO VC9 Activity
  AASREF VC9 Asset
  ACGETRNOT MD1 Receipt value ex-tax
  ADMCOE RAT Admission coef.
  ADMCOEF RAT Admission coef.
  ADMCOEFO RAT Admission coef.
  ADMCOEO RAT Admission coef.
  ADMCOER RAT Admission coef.
  ADMCOERO RAT Admission coef.
  ASJCOE RAT Liability coef.
  ASJCOEF RAT Liability coef.
  ASJCOEFO RAT Liability coef.
  ASJCOEO RAT Liability coef.
  ASJCOER RAT Liability coef.
  ASJCOERO RAT Liability coef.
  AUUID AUUID Single identifier
  BASDEV MD1 Bal sheet val vari
  CPY CPY Company -> [CPY]CPY0 =[VAT]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VAT]CREUSR (AUTILIS) !Other
  DATVATREG D4 Date
  DEDCOE RAT Deduction coef
  DEDCOEF RAT Deduction coef
  DEDCOEFO RAT Deduction coef
  DEDCOEO RAT Deduction coef
  DEDCOER RAT Deduction coef
  DEDCOERO RAT Deduction coef
  DEDVATAMT MD1 VAT recovered
  DEDVATAMTO MD1 VAT recovered
  DEDVATFLG M*4 Forced rec VAT [menu 1: 1=No,2=Yes]
  DPRBAS MD1 Basis after update
  DPRBASO MD1 Basis before adj.
  DPRPLN M*25 Depreciation plan [menu 3101: 16 values, see local-menus.md]
  FCY FCY Financial site -> [FCY]FCY0 =[VAT]FCY (FACILITY) !Block
  FORMULE A*50 Formula
  ISSVATAMT MD1 VAT due on disposal
  ISSVATFLG MZS*4 Forced disposal VAT
  IVCVATAMT MD1 VAT invoiced
  IVCVATAMTO MD1 VAT invoiced
  IVCVATFLG MZS*4 Invoiced VAT forced
  IVCVATRAT RAT Invd VAT rate
  PYBVATTYP M*15 VAT repayment [menu 3160: 1=1/5th rule,2=1/10th rule,3=1/20th rule,4=No VAT adjustment,5=Deductible VAT amount adjustment: increase,6=Deductible VAT amount adjustment: decrease]
  TAXCOE RAT Taxation coeff
  TAXCOEF RAT Taxation coeff
  TAXCOEFLG M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TAXCOEFLGO M*4 Forced taxation coef [menu 1: 1=No,2=Yes]
  TAXCOEFO RAT Taxation coeff
  TAXCOEO RAT Taxation coeff
  TAXCOER RAT Taxation coeff
  TAXCOERO RAT Taxation coeff
  THESLI DUR Adujst period
  TIMSTP A*20 Time stamp
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VAT]UPDUSR (AUTILIS) !Other
  VATREGAMT MD1 VAT repay adj.
  VATREGCUM MD1 VAT adj total
  VATREGDATO D4 Reference date
  VATREGDED MD1 VAT ded adj.
  VATREGTYP M*25 Tax adjust type [menu 3269: 13 values, see local-menus.md]
  VATRSD DUR Residual duration
  VATYEAFLG M*4 Yearly adjust. index [menu 1: 1=No,2=Yes]

