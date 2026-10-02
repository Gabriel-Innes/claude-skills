<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# A/P-A/R accounting module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BANK (BAN) - Bank accounts
Notes: differs in V9.0 P12 (diff: AT3_BANK.htm); differs in V10 P1 (diff: ATD_BANK.htm)
Keys (first = PK; D = duplicates allowed): BAN0 BAN
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =13;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACS ACS Access code -> [ACS]ACS0 =[BAN]ACS (ACCCOD) !Block
  ADDLIG A*35(3) Address
  AUUID AUUID Single identifier
  BAN BAN Code -> [BAN]BAN0 =[BAN]BAN (BANK) !Delete
  BANACC GAC Account -> [GAC]GAC0 =COA;BANACC (GACCOUNT) !Block
  BANBPR BPR BP code -> [BPR]BPR0 =[BAN]BANBPR (BPARTNER) !Block
  BANCSH M*15 Bank or cash [menu 653: 1=Bank,2=Cash]
  BANFIL A*10 Bank file act:KPO
  BANTRA A*9 Bank transit act:CHQMG
  BANTRM A*10 Bank terms
  BICCOD A*11 BIC code
  BIDEXS BID Bank account no.
  BIDNUM BID Bank acct. number
  BNKPROBALCTL M*4 Balance control [menu 1: 1=No,2=Yes]
  BSIREFBAN A*50 Bank statement ID act:BSI
  BVRCUSTID A*12 Customer ID ISR act:KSW
  BVRNUM A*11 ISR customer no. act:KSW
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFOEXD M*4 Cash excluded [menu 1: 1=No,2=Yes] act:CFOM
  CHGDAT D Euro changeover date
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CHKACC A*17 Checking account act:CHQMG
  CHKCOD A*5 Reconciliation
  CHKFMT M*15 Format [menu 2760: 1=Not used,2=Check-stub-stub,3=Stub-check-stub,4=Check-stub] act:CHQMG
  CHQTYPFLG M*4 O/L check remit. [menu 1: 1=No,2=Yes]
  COA COA Chart code -> [COA]COA0 =[BAN]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[BAN]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRN CRT Site tax ID no.
  CRY CRY Country -> [TCY]TCY0 =[BAN]CRY (TABCOUNTRY) !Block
  CRYNAM A*30 Country name
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[BAN]CUR (TABCUR) !Block
  CUREXS CUR Expense currency -> [TCU]TCU0 =[BAN]CUREXS (TABCUR) !Block
  DEPRAT RAT Early discount rate
  DES DES Description
  DESSHO SHO Short description
  DIE DIE Dimension type code -> [DIE]DIE0 =[BAN]DIE (GDIE) !Block act:ANA
  EXPNUM L*8 Export number
  FAX TEL Fax
  FCY FCY Site -> [FCY]FCY0 =[BAN]FCY (FACILITY) !Block
  FILEXT A*3 File extension
  FRMDUDFLG M*4 Deposit by due date [menu 1: 1=No,2=Yes]
  GTE GTE(10) Entry type -> [GTE]GTE0 =GTE(indice);[V]GSUPCLE (GTYPACCENT) !Block
  IBACOD A*34 IBAN code
  JOU JOU(10) Journal -> [JOU]JOU0 =JOU(indice);[V]GSUPCLE (GJOURNAL) !Block
  JOUTYP M*15(10) Journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  MCRPRT M*4 MICR printing [menu 1: 1=No,2=Yes] act:CHQMG
  NBRJOU C*2 Number of journals
  NXTSEQ A*15 Next check no. act:CHQMG
  OLDCUR A*3 Old currency
  PAB1 A*30 Paying bank 1
  PAB2 A*30 Paying bank 2
  PABDUDFLG M*4 Paying bank notice by due date [menu 1: 1=No,2=Yes]
  PAYTPY MD1 Provisional payment
  POSCOD POS Postal code
  POSPAYFIL A*10 Bank file act:CHQMG
  QRCIBACOD A*34 QR-IBAN act:KSW
  RECCPT M*4 Addi recording [menu 1: 1=No,2=Yes]
  SAT SAT State
  SCTPROLOT M*4 Processing by batch [menu 1: 1=No,2=Yes]
  SENNUM A*10 Credit transfer issuer no.
  SENNUM2 A*10 Direct debit issuer no.
  TEL TEL Telephone
  TREACC GAC(10) Account -> [GAC]GAC0 =COA;TREACC(indice) (GACCOUNT) !Block
  TRECOD A*12 Treasury interface
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEB A*50 Internet address

## BANKPOSD (BPL) - Banking position
Notes: activity code BANFO
Keys (first = PK; D = duplicates allowed): BPL0 CNSUSR+CPY+FCY+GRPBAN+BAN+TYPFRT+DUDDAT; BPL1 INDLNK (D)
Fields:
  AMTCUR MD1(15) Amount in currency
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BPL]BAN (BANK) !Block
  CNSUSR AUS User -> [AUS]CODUSR =[BPL]CNSUSR (AUTILIS) !Block
  CPY CPY Company -> [CPY]CPY0 =[BPL]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BPL]CREUSR (AUTILIS) !Other
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[BPL]FCY (FACILITY) !Delete
  GRPBAN BGR Bank group -> [BGR]BGR0 =[BPL]GRPBAN (BGRBAN) !Block
  INDLNK A*50 Index link
  PER A*20(15) Period
  TYPFRT A*25 Concept
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BPL]UPDUSR (AUTILIS) !Other

## BANREC (BEH) - Bank Reconciliation Statement
Keys (first = PK; D = duplicates allowed): BEH0 RBKNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BEH]BAN (BANK) !Other
  BLC MD1 Book balance
  BNKDAT D Statement Date
  CRDREC MD1 Cleared withdrawals
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEBREC MD1 Cleared deposits
  ENDSTMT MD1 Ending statement balance
  EXPNUM L*8 Export number
  MRKCHRS A*5 Mark
  OUTDEP MD1 Outstanding deposits
  OUTWTH MD1 Withdrawals
  RBKDES DES Description
  RBKNUM VCR Statement number
  STAFLG M*15 Status [menu 17: 1=Not open,2=Open,3=Closed]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BANRECD (BED) - Bank Statement Lines
Keys (first = PK; D = duplicates allowed): BED0 RBKNUM+ACCNUM; BED1 ACCNUM
Fields:
  ACCNUM UNQ Unique number
  ADJREA ADI Reason -> [ADI]CODE =383;ADJREA (ATABDIV) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  RBKNUM VCR Statement number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BED]UPDUSR (AUTILIS) !Other

## BGRBAN (BGR) - Bank group
Notes: activity code BANFO
Keys (first = PK; D = duplicates allowed): BGR0 GRPBAN
Fields:
  AUUID AUUID Single identifier
  BAN BAN(50) Bank -> [BAN]BAN0 =[BGR]BAN (BANK) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BGR]CREUSR (AUTILIS) !Other
  DESBAN DES Description
  GRPBAN A*10 Bank group
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BGR]UPDUSR (AUTILIS) !Other

## BILSTA (BES) - Statement of bill of exchange
Notes: differs in V9.0 P12 (diff: AT3_BILSTA.htm)
Keys (first = PK; D = duplicates allowed): BES0 FRMNUM+LIN; BES1 PAYNUM+FRMNUM+LIN
Fields:
  ACP C*1 Acceptance
  ADELEA A*5 Main destination file
  AMT MD1 Initial amount
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BES]BAN (BANK) !Block
  CDTACC A*11 Assignor account
  CPY CPY Company -> [CPY]CPY0 =[BES]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BES]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BES]CUR (TABCUR) !Block
  DEBACC A*11 Drawee account
  DUDDAT D Due date
  ENTDAT D Note P/R date
  FCY FCY Site -> [FCY]FCY0 =[BES]FCY (FACILITY) !Block
  FLGANO M*4 Anomaly [menu 1: 1=No,2=Yes]
  FLGEXP M*4 Exports [menu 1: 1=No,2=Yes]
  FRMNUM VCR Internal statement no.
  IMPDAT D Bank file
  IMPFIL A*20 Bank file
  INDCUR A*1 Source currency index
  INSDAT D Return limit date
  LIN L*8 Number
  NAMCDT A*24 Payer name
  NAMDEB A*24 Drawee name
  NUM A*8 Statement number
  PABAMTPRT MD1 Partial amount
  PABCOT A*5 Paying bank clerk
  PABFCY A*5 Paying bank branch
  PABFLG M*4 Accepted [menu 1: 1=No,2=Yes]
  PABNAM A*24 Paying bank description
  PABORD A*8 Paying bank number
  PABREN ADI Non accepted reason -> [ADI]CODE =305;PABREN (ATABDIV) !Block
  PAYDAT D Payment date
  PAYNUM VCR Payment
  PROCEN A*6 Processing center
  REFCDT A*10 Payer reference
  REFDEB A*10 Drawee reference
  REFPRE A*8 Presenter reference
  SENCOT A*5 Sending clerk
  SENFCY A*5 Sending branch
  SENLEA A*5 Main source file
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BES]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## BLOBEXPENSES (BEXP) - Expense note photo
Keys (first = PK; D = duplicates allowed): BEXP0 ACCNUM; BEXP1 CLB+DATEXS (D)
Fields:
  ACCNUM UNQ Internal number
  AUUID AUUID Single identifier
  BLOB ABB Image file
  CLB AUS Employee -> [AUS]CODUSR =[BEXP]CLB (AUTILIS) !Delete
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[BEXP]CREUSR (AUTILIS) !Block
  DATEXS D Date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[BEXP]UPDUSR (AUTILIS) !Block

## BPCINVLIG (SIL) - Customer invoice lines
Notes: differs in V9.0 P12 (diff: AT3_BPCINVLIG.htm); differs in V10 P1 (diff: ATD_BPCINVLIG.htm)
Keys (first = PK; D = duplicates allowed): SIL0 NUM+LIG; SIL1 PJTLIN (D)
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  AMTATILIN MD1 Amount + tax
  AMTNOTLIN MD1 Amount - tax
  AMTTAX1 MD1 Tax amount
  AMTTAX2 MD1 Tax amount
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPRLIN BPR BP -> [BPR]BPR0 =[SIL]BPRLIN (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[SIL]COA (GCOA) !Block
  CPYLIN CPY Company -> [CPY]CPY0 =[SIL]CPYLIN (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SIL]CREUSR (AUTILIS) !Other
  DES A*30 Comment
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENDDAT D End date
  EXEAMTISS MD1 Exempt dispatch tax act:PTX
  EXEAMTOTH1 MD1 Exempt alt tax 1 act:PTX
  EXEAMTOTH2 MD1 Exempt alt tax 2 act:PTX
  EXEAMTRCP MD1 Exempt receipt tax act:PTX
  EXEAMTTAX1 MD1 Exemption tax 1 act:PTX
  EXEAMTTAX2 MD1 Exemption tax 2 act:PTX
  EXEAMTVAT MD1 Exemption VAT act:PTX
  FAS A*30 Fixed asset
  FCYLIN FCY Site -> [FCY]FCY0 =[SIL]FCYLIN (FACILITY) !Block
  FLGDEP M*4 Subject to discount [menu 1: 1=No,2=Yes]
  FLGGEN M*4 Auto generation [menu 1: 1=No,2=Yes]
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LED LED(10) Ledger -> [LED]LED0 =[SIL]LED (GLED) !Block
  LIG C*3 Line number
  NUM VCR Document no.
  PERNBR C*4 Periodicity
  PERTYP M*15 Periodicity [menu 635: 1=Days,2=Week,3=10-day period,4=2-week period,5=Month]
  PJTLIN PJT Project -> [PIM]PIM0 =PJTLIN (PIMPL) !Block act:PJM
  QTY QTY Quantity
  SAC SAC Control
  SALTYP M*15 Sales type [menu 2602: 1=Goods,2=Fixed assets,3=Services] act:KPO
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STRDAT D Start date
  STT1 A*3 Statistics
  STT2 A*3 Statistics
  STT3 A*3 Statistics
  TAX1 VAT Tax 1 -> [TVT]TVT0 =TAX1;[V]GSUPCLE (TABVAT) !Block
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  THEAMTOTH1 MD1 Theor other tax amt act:PTX
  THEAMTOTH2 MD1 Theor other tax amt act:PTX
  THEAMTTAX1 MD1 Theor. tax amt act:PTX
  THEAMTTAX2 MD1 Theor. tax amt act:PTX
  THEAMTTAXI MD1 Theor. issue tax amt act:PTX
  THEAMTTAXR MD1 Theor. recpt tax amt act:PTX
  THEAMTVAT MD1 Theor. tax amt act:PTX
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[SIL]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SIL]UPDUSR (AUTILIS) !Other
  VAT VAT Tax 3 -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## BPCINVLIGA (SIA) - Customer analytical line
Keys (first = PK; D = duplicates allowed): SIA0 NUM+LIG+ANALIG
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMT MD1 Amount
  ANALIG C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[SIA]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SIA]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[SIA]DIE (GDIE) !Block act:ANA
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LIG C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[SIA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SIA]UPDUSR (AUTILIS) !Other

## BPCINVVAT (SIT) - Tax rates
Keys (first = PK; D = duplicates allowed): SIT0 NUM
Fields:
  AUUID AUUID Single identifier
  CODE VAT(10) Code -> [TVT]TVT0 =CODE(indice);[V]GSUPCLE (TABVAT) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SIT]CREUSR (AUTILIS) !Other
  DOC C*1 Document type
  NUM VCR Invoice number
  TAUX DCB*3.6(10) Tax rates
  TEX A*80(10) Mention on invoice
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SIT]UPDUSR (AUTILIS) !Other

## BPSINVLIG (PIL) - Supplier invoice lines
Notes: differs in V9.0 P12 (diff: AT3_BPSINVLIG.htm); differs in V10 P1 (diff: ATD_BPSINVLIG.htm)
Keys (first = PK; D = duplicates allowed): PIL0 NUM+LIG; PIL1 PJTLIN (D)
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  AMTATILIN MD1 Amount + tax
  AMTNOTLIN MD1 Amount - tax
  AMTTAX1 MD1 Tax amount
  AMTTAX2 MD1 Tax amount
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPRLIN BPR BP -> [BPR]BPR0 =[PIL]BPRLIN (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[PIL]COA (GCOA) !Block
  CPYLIN CPY Company -> [CPY]CPY0 =[PIL]CPYLIN (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PIL]CREUSR (AUTILIS) !Other
  DCLEECNUM EEC VAT declaration no. act:KPO
  DEDTAX1 MD1 Deductible tax
  DEDTAX2 MD1 Deductible tax
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DEDVAT MD1 Input VAT
  DES A*30 Comment
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  ENDDAT D End date
  FCYLIN FCY Site -> [FCY]FCY0 =[PIL]FCYLIN (FACILITY) !Block
  FLG1099 M*4 1099 [menu 1: 1=No,2=Yes] act:S1099
  FLGDEP M*4 Subject to discount [menu 1: 1=No,2=Yes]
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LED LED(10) Ledger -> [LED]LED0 =[PIL]LED (GLED) !Block
  LIG C*3 Line number
  NUM VCR Document no.
  PERNBR C*4 Periodicity
  PERTYP M*15 Periodicity [menu 635: 1=Days,2=Week,3=10-day period,4=2-week period,5=Month]
  PJTLIN PJT Project -> [PIM]PIM0 =PJTLIN (PIMPL) !Block act:PJM
  PURTYP M*15 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  QTY QTY Quantity
  RITCODSRC RTZ Withholding tax code -> [RTZ]RTZ0 =[PIL]RITCODSRC (RITENZIONE) !Block act:KIT
  SAC SAC Control
  STRDAT D Start date
  STT1 A*3 Statistics
  STT2 A*3 Statistics
  STT3 A*3 Statistics
  TAX1 VAT Tax 1 -> [TVT]TVT0 =TAX1;[V]GSUPCLE (TABVAT) !Block
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[PIL]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PIL]UPDUSR (AUTILIS) !Other
  VAT VAT Tax 3 -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## BPSINVLIGA (PIA) - Supplier analytical line
Keys (first = PK; D = duplicates allowed): PIA0 NUM+LIG+ANALIG
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  AMT MD1 Amount
  ANALIG C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[PIA]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PIA]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[PIA]DIE (GDIE) !Block act:ANA
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LIG C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[PIA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PIA]UPDUSR (AUTILIS) !Other

## BSIBPRNUM (BSIBPN) - BP number definition
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIBPN0 CPY+FCY+FILFMT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CPYFCY A*21 Key
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIBPN]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIBPN]UPDUSR (AUTILIS) !Other

## BSIBPRNUMD (BSIBPND) - BP number definition
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIBPN0 CPY+FCY+FILFMT+LIN
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIBPND]CREUSR (AUTILIS) !Other
  DIR M*15 Search destination [menu 3669: 1=Sage X3,2=File]
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  LENINVEND C*4 To number length
  LENINVSTR C*4 From number length
  LIN C*4 Line number
  LNG C*4 No. of characters
  OPT M*15 Begin search at [menu 3670: 1=First character,2=Last character,3=Start position]
  PFX A*20 Prefix
  STRPOS C*4 Starting position
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIBPND]UPDUSR (AUTILIS) !Other

## BSIDUD (BSIDUD) - Open items
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIDUD0 STMCOD+LIN+LIN1; BSIDUD1 NUMDUD (D)
Fields:
  ACCNUM L*8 Internal number
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ref. amt. curr.
  AUUID AUUID Single identifier
  BALDUD MD1 Balance
  BAN BAN Bank -> [BAN]BAN0 =[BSIDUD]BAN (BANK) !Block
  BPAPAY ADR Business partner address
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[BSIDUD]BPR (BPARTNER) !Block
  BPRFCT FCT Factor -> [FCT]FCT0 =[BSIDUD]BPRFCT (FACTOR) !Block act:FCT
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[BSIDUD]BPRPAY (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  BPRVCR A*20 Original document
  BSIBAL MD1 Balance
  BSIDEPCUR MD1 Discount (currency)
  BSIDEPLOC MD1 Disc. (ledger curr.)
  BSIDEPSTM MD1 Disc. (stmt. curr.)
  BSIPAYCUR MD1 Paid (currency)
  BSIPAYLOC MD1 Paid (ledger curr.)
  BSIPAYSTM MD1 Paid (stmt. curr.)
  BSISNS C*2 Payment sign
  BSIUNDPAYCUR MD1 Underpaid (curr)
  BSIUNDPAYLOC MD1 Underpaid (ledger)
  BSIUNDPAYSTM MD1 Underpaid (stmt)
  CPY CPY Company -> [CPY]CPY0 =[BSIDUD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[BSIDUD]CUR (TABCUR) !Block
  DATFUP D Reminder date
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DEPAMT MD1 Discount amount
  DINAMT MD1 Prepayment deducted
  DPTCOD ADI Dispute code -> [ADI]CODE =315;DPTCOD (ATABDIV) !Block
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  DUDSEL M*4 Y/N [menu 1: 1=No,2=Yes]
  DUDSTA C*1 Status
  EXPSENDAT D Expected issue date
  FCTVCR VCR Receipt act:FCT
  FCY FCY Site -> [FCY]FCY0 =[BSIDUD]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGCLE C*1 Closed
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  IBDAMT MD1 Prepayment to deduct
  LEVFUP C*2 Reminder level
  LIG C*3 Line number
  LIN C*3 Line number
  LIN1 C*4 Line number
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
  STMCOD VCR Statement code
  TMPCUR MD1 Provisional payment
  TMPLOC MD1 Provisional payment
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPDUD M*15 Type of open item [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIDUD]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## BSIELTMAP (BSIELT) - Camt element mapping detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIELT0 COD
Fields:
  AUUID AUUID Single identifier
  COD BSIELT Mapping code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIELT]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIELT]UPDUSR (AUTILIS) !Other

## BSIELTMAPD (BSIELTD) - Camt element mapping
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIELTD0 COD+LIN
Fields:
  AUUID AUUID Single identifier
  COD BSIELT Mapping code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIELTD]CREUSR (AUTILIS) !Other
  DES A*30 Description
  ELT A*30 Element
  ELTPAH A*250 Path
  LEV C*4 Level
  LIN C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIELTD]UPDUSR (AUTILIS) !Other

## BSIFILFMT (BSIFFM) - Bank import format definition
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIFFM0 CODBFF
Fields:
  AUUID AUUID Single identifier
  CODBFF BSIBFF Format -> [BSIFFM]BSIFFM0 =[BSIFFM]CODBFF (BSIFILFMT) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIFFM]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  FILFMT M*10 Character coding [menu 945: 1=ascii,2=utf-8,3=ucs-2]
  FILTYP M*10 File type [menu 3677: 1=MT940,2=CSV,3=CAMT,4=BAI]
  FLDSEP A*4 Field separator
  RECSEP A*8 Record separator
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIFFM]UPDUSR (AUTILIS) !Other

## BSIFILFMTD (BSIFFD) - Bank import format def. detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIFFD0 CODBFF+LIN; BSIFFD1 CODBFF+SCT (D)
Fields:
  AUUID AUUID Single identifier
  CODBFF BSIBFF Format -> [BSIFFM]BSIFFM0 =CODBFF (BSIFILFMT) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIFFD]CREUSR (AUTILIS) !Other
  DBACT M*15 Operation [menu 3672: 1=Unspecified,2=Create,3=Update]
  LEV C*4 Level
  LIN C*4 Line number
  SCT BSISCT Segment
  SCTEND M*4 End [menu 1: 1=No,2=Yes]
  SCTSTR M*4 Start [menu 1: 1=No,2=Yes]
  SEGOBY M*4 Mandatory [menu 1: 1=No,2=Yes]
  TABTYP M*15 Header/Line [menu 3689: 1=Line detail,2=Header,3=Line]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIFFD]UPDUSR (AUTILIS) !Other

## BSIIMP (BSIIMP) - Bank statement import
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIMP0 STMCOD
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BSIIMP]BAN (BANK) !Block
  BLCEND MD1 End balance
  BLCENDSNS A*4 Sign
  BLCSTR MD1 Start balance
  BLCSTRSNS A*4 Sign
  BSITRS A*20 Transaction number
  CODIMPPAR BSIIMPP Import settings -> [BSIIP]BSIIP0 =CODIMPPAR (BSIIMPPAR) !Block
  CPY CPY Company -> [CPY]CPY0 =[BSIIMP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[BSIIMP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BSIIMP]CUR (TABCUR) !Block
  DATEND D End date
  DATSTR D Start date
  FCY FCY Site -> [FCY]FCY0 =[BSIIMP]FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  FILNAM FIC*100 File name
  FLGMTC M*4 Matching status [menu 3675: 1=Not matched,2=Matched,3=Validated,4=Reconcile]
  ORIGNTR A*10 BAI originator ID
  REFBAN A*30 Bank reference
  SEQNUM A*12 Sequence number
  STMCOD VCR Statement code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIIMP]UPDUSR (AUTILIS) !Other

## BSIIMPD (BSIIMPD) - Bank statement import detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIMPD0 STMCOD+LIN; BSIIMPD1 BAN+STMCOD (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =[BSIIMPD]ACC (GACCOUNT) !BSRA
  AMTCUR MD1 Amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BSIIMPD]BAN (BANK) !Block
  BPAINV ADR Billing address
  BPRINV BPR Bill-to BP -> [BPR]BPR0 =[BSIIMPD]BPRINV (BPARTNER) !Block
  BPRNAM NAM(2) Company name
  BPRPAY BPR BP -> [BPR]BPR0 =[BSIIMPD]BPRPAY (BPARTNER) !Block
  BPRREF A*30(5) BP reference
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CPY CPY Company -> [CPY]CPY0 =[BSIIMPD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIIMPD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BSIIMPD]CUR (TABCUR) !Block
  DENCOD CDA Destination -> [CDA]CDA0 =[BSIIMPD]DENCOD (GACCDENCOD) !BSRA
  DEP MD1 Discount
  DEPAMT MD1 Discount amount
  DES DES Reference
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  DUDDAT D Due date
  DUDLIG C*2 Due date number
  DUDNUM UNQ Internal number
  FCYLIN FCY Site -> [FCY]FCY0 =[BSIIMPD]FCYLIN (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  FLGAMT M*4 Amount [menu 1: 1=No,2=Yes]
  FLGBIDNUM M*4 BP bank account number [menu 1: 1=No,2=Yes]
  FLGBPR M*4 BP [menu 1: 1=No,2=Yes]
  FLGBPRNAM M*4 BP name [menu 1: 1=No,2=Yes]
  FLGBPRVCR M*4 Source document [menu 1: 1=No,2=Yes]
  FLGBVRREFNUM M*4 ISR reference number [menu 1: 1=No,2=Yes]
  FLGCRE M*15 Creation flag [menu 3690: 1=Not validated,2=Validated,3=Partially validated,4=Manually completed]
  FLGINVNUM M*4 Invoice number [menu 1: 1=No,2=Yes]
  FLGREFLIS M*4 Use search term list [menu 1: 1=No,2=Yes]
  FLGSOHNUM M*4 Order number [menu 1: 1=No,2=Yes]
  FREREF A*30(10) Free reference
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LET A*3 Matching flag
  LIN C*3 Line number
  OVERPAY MD1 Overpayment
  REF REF Reference
  REM A*250 Comment
  SAC SAC Control
  SNS A*2 Sign
  STMCOD VCR Statement code
  TRS A*10 Transaction
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIIMPD]UPDUSR (AUTILIS) !Other
  VALDAT D Value date
  VAT VAT Tax -> [TVT]TVT0 =[BSIIMPD]VAT (TABVAT) !BSRA

## BSIIMPDS (BSIIMPS) - Bank statement imp. sub-detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIMPS0 STMCOD+TRSLIN+DETLIN
Fields:
  ACCREF A*35(3) Reference
  AMTCURS MD1 Amount
  AUUID AUUID Single identifier
  BANTRSREF A*35(3) Transaction code
  BPRREFS A*140(5) BP reference
  BVRREF A*27 ISR reference number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIIMPS]CREUSR (AUTILIS) !Other
  CURS CUR Currency -> [TCU]TCU0 =[BSIIMPS]CURS (TABCUR) !Block
  DETLIN C*3 Line number
  RMTREF A*140(10) Reference
  SNSS A*4 Sign
  STMCOD VCR Statement code
  TRSLIN C*3 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIIMPS]UPDUSR (AUTILIS) !Other

## BSIIMPPAR (BSIIP) - Bank import settings
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIP0 CODIMPPAR
Fields:
  ACCSUSPENSE GAC Account -> [GAC]GAC0 =COA;ACCSUSPENSE (GACCOUNT) !Block
  ALLBPR M*4 All BPs [menu 1: 1=No,2=Yes]
  ALLCAT M*4 All categories [menu 1: 1=No,2=Yes]
  ALLTYP M*4 All BP types [menu 1: 1=No,2=Yes]
  AMT M*4 Amount [menu 1: 1=No,2=Yes]
  AMTVAR RAT Amount variance
  AMTVARCUR RAT Amount variance
  AMTVARLIM MD1 Limit
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BSIIP]BAN (BANK) !Block
  BPRBANID M*4 BP bank account number [menu 1: 1=No,2=Yes]
  BPREND BPR To BP -> [BPR]BPR0 =[BSIIP]BPREND (BPARTNER) !Block
  BPRNAM M*4 BP name [menu 1: 1=No,2=Yes]
  BPRNUM M*4 BP number [menu 1: 1=No,2=Yes]
  BPRSTR BPR From BP -> [BPR]BPR0 =[BSIIP]BPRSTR (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  BVRREFNUM M*4 ISR reference number [menu 1: 1=No,2=Yes] act:KSW
  CATBPC BCG Customer category -> [BCG]BCG0 =[BSIIP]CATBPC (BPCCATEG) !Block
  CATBPS BSG Supplier category -> [BSG]BSG0 =[BSIIP]CATBPS (BPSCATEG) !Block
  CDAACCSUSP CDA Payment attribute -> [CDA]CDA0 =CDAACCSUSP;LEG (GACCDENCOD) !Block
  CDAEXCPAY CDA Payment attribute -> [CDA]CDA0 =CDAEXCPAY;LEG (GACCDENCOD) !Block
  CDASHOPAY CDA Payment attribute -> [CDA]CDA0 =CDASHOPAY;LEG (GACCDENCOD) !Block
  CDAVARCUR CDA Payment attribute -> [CDA]CDA0 =CDAVARCUR;LEG (GACCDENCOD) !Block
  COA COA Chart of accounts -> [COA]COA0 =[BSIIP]COA (GCOA) !Delete
  CODIMPPAR A*20 Code
  CPY CPY Company -> [CPY]CPY0 =[BSIIP]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIIP]CREUSR (AUTILIS) !Other
  DEPTOL C*4 Allowance days
  DESAXX AX3 Description
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  FLGCLS M*4 Suppress intermediate posting [menu 1: 1=No,2=Yes]
  FLOTYP M*15 Flow type [menu 3694: 1=Standard,2=Reconciliation only]
  IMPVOL A*250 Import volume
  INVNUM M*4 Invoice number [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  MOVAFTIMP M*4 Move [menu 1: 1=No,2=Yes]
  MOVVOL A*250 Move to volume
  MRGDESFLD M*4 Merge [menu 3673: 1=No,2=Always,3=Second pass]
  ORDERNUM M*4 Order number [menu 1: 1=No,2=Yes]
  PAYTYP TPY Payment entry transaction -> [TPY]TPY0 =PAYTYP;LEG (TABPAYTYP) !Block
  RENAFTIMP M*4 Rename file after import [menu 1: 1=No,2=Yes]
  SEAEXD M*4 Use excluded search term list [menu 1: 1=No,2=Yes]
  SEAEXDLEN C*4 Minimum search term length
  SRCDOC M*4 Source document [menu 1: 1=No,2=Yes]
  TYPIMP M*15 File import [menu 921: 1=Client,2=Server]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIIP]UPDUSR (AUTILIS) !Other
  USESEALIS M*4 Use search term list [menu 3674: 1=No,2=First pass,3=Last pass]
  USESUBSTR M*4 Substring search [menu 1: 1=No,2=Yes]

## BSIIMPTC (BSITC) - Bank import type codes
Notes: activity code BSI; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): BSITC0 BSICODTC+BAN; BSITC1 BAN
Fields:
  AUUID AUUID Single identifier
  BAN BANACO Bank
  BSICODTC BSITCF Bank type code -> [BSITC]BSITC0 =[BSITC]BSICODTC (BSIIMPTC) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSITC]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  SHO SHO Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSITC]UPDUSR (AUTILIS) !Other

## BSIINVDIO (BSIIND) - Invoice number definition
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIND0 CPY+FCY+FILFMT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CPYFCY A*21 Key
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIIND]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  INVALLNUM M*4 Invoice no. always numeric [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIIND]UPDUSR (AUTILIS) !Other

## BSIINVDIOD (BSIINDD) - Invoice number definition
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIIND0 CPY+FCY+FILFMT+LIN
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIINDD]CREUSR (AUTILIS) !Other
  DIR M*15 Search destination [menu 3669: 1=Sage X3,2=File]
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  LENINVEND C*4 To number length
  LENINVSTR C*4 From number length
  LIN C*4 Line number
  LNG C*4 No. of characters
  OPT M*15 Begin search at [menu 3670: 1=First character,2=Last character,3=Start position]
  PFXINV A*20 Prefix invoice no.
  PFXTYP M*15 Search criteria [menu 3671: 1=Document no.,2=Source document no.]
  STRPOS C*4 Starting position
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIINDD]UPDUSR (AUTILIS) !Other

## BSIITCD (BSIITCD) - Bank import type codes
Notes: activity code BSI; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): BSITCD0 BSICODTC+BAN+COD; BSITCD1 BAN+COD; BSITCD2 BAN+COD+LEV
Fields:
  AUUID AUUID Single identifier
  BAN BANACO Bank
  BSICODTC BSITCF Code -> [BSITC]BSITC0 =BSICODTC;BAN (BSIIMPTC) !Delete
  COD A*3 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIITCD]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  DESFLD A*200 Destination
  LEV M*10 Level [menu 3695: 1=Status,2=Summary,3=Detail]
  LIN C*4 Line
  REC A*2 Record
  SIG M*10 Sign [menu 3696: 1=Credit,2=Debit]
  SUMCOD A*10 Summary code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIITCD]UPDUSR (AUTILIS) !Other

## BSIMANENT (BSIMAN) - Manual entry
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSIMAN0 STMCOD+LIN+LIN1
Fields:
  ACC GAC Account -> [GAC]GAC0 =[V]GPLAN(1);ACC (GACCOUNT) !Block
  ACCSAC GAC Account -> [GAC]GAC0 =[V]GPLAN(1);ACC (GACCOUNT) !Block
  AMT MD1 Amount
  AUUID AUUID Single identifier
  BPAINV ADR Address
  BPR BPR BP -> [BPR]BPR0 =[BSIMAN]BPR (BPARTNER) !Block
  BPRSAC SAC Control
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSIMAN]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BSIMAN]CUR (TABCUR) !Block
  DENCOD CDA Destination -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DES DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  LIN C*3 Line number
  LIN1 C*4 Line number
  REF REF Reference
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  STMCOD VCR Statement code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSIMAN]UPDUSR (AUTILIS) !Other
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## BSISCT (BSISCT) - Bank import segment
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSISCT0 CODSCT
Fields:
  AUUID AUUID Single identifier
  CODELT BSIELT Camt element mapping act:BSI
  CODSCT BSISCT Segment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSISCT]CREUSR (AUTILIS) !Other
  DESAXX AX3 Description
  FILTYP M*10 File type [menu 3677: 1=MT940,2=CSV,3=CAMT,4=BAI]
  LEV C*4 Level
  LNGMAX C*4 Maximum length
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSISCT]UPDUSR (AUTILIS) !Other

## BSISCTD (BSISCTD) - Bank import segment detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSISCTD0 CODSCT+LIN
Fields:
  AUUID AUUID Single identifier
  CODSCT BSISCT Segment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSISCTD]CREUSR (AUTILIS) !Other
  CTL M*15 Control type [menu 3668: 1=No control,2=Debit/Credit,3=Bank account ID]
  DESAXX AX3 Description
  FLD A*40 Destination field
  FLDFMT A*20 Format
  FLDIDT A*10 Identifier
  FLDOBY M*4 Mandatory [menu 1: 1=No,2=Yes]
  FLDTYP M*15 Field type [menu 3683: 1=Alphanumeric,2=Numeric,3=Date]
  FRM AFR*250 Formula
  LIN C*4 Line number
  LNG C*4 Length
  LNGTYP M*15 Length type [menu 3627: 1=Fixed,2=Variable]
  POS C*4 Position
  TYP M*15 Type [menu 3667: 1=Data,2=Segment ID,3=Field ID,4=Constant]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSISCTD]UPDUSR (AUTILIS) !Other

## BSISEAEXD (BSISEA) - Excluded terms
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSISEA0 CODSEA
Fields:
  AUUID AUUID Single identifier
  CODSEA A*30 Excluded terms
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSISEA]CREUSR (AUTILIS) !Other
  TXTSEA A*30 Excluded terms
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSISEA]UPDUSR (AUTILIS) !Other

## BSISEALIS (BSILIS) - Search term list
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSILIS0 CPY+BAN+FILFMT
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BSILIS]BAN (BANK) !Block
  CPY CPY Company -> [CPY]CPY0 =[BSILIS]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSILIS]CREUSR (AUTILIS) !Other
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSILIS]UPDUSR (AUTILIS) !Other

## BSISEALISD (BSILISD) - Search term list detail
Notes: activity code BSI; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSILISD0 CPY+BAN+FILFMT+LIN
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCSAC GAC Account -> [GAC]GAC0 =[V]GPLAN(1);ACC (GACCOUNT) !Block
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[BSILISD]BAN (BANK) !Block
  BPAINV ADR Address
  BPR BPR BP -> [BPR]BPR0 =[BSILISD]BPR (BPARTNER) !Block
  BPRSAC SAC Control
  COA COA Chart of accounts -> [COA]COA0 =COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[BSILISD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSILISD]CREUSR (AUTILIS) !Other
  DENCOD CDA Attribute -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DES DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  FILFMT BSIBFF File format -> [BSIFFM]BSIFFM0 =FILFMT (BSIFILFMT) !Block
  LIN C*4 Line number
  SEAAMT MD1 Amount
  SEABPRREF A*30 BP reference
  SEABTC A*70 BTC reference
  SEAOTH A*30 Payment description
  SEAPAYREF A*30 Payment reference
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSILISD]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## CFODUDDATE (CFODD) - Cash forecast management
Notes: activity code CFOM
Keys (first = PK; D = duplicates allowed): CFODD0 TYP+NUM+LIG+DUDLIG; CFODD1 FLGCLE+FCY+BPRPAY+CFODAT (D)
Fields:
  ACCNUM L*8 Internal number
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ref. amt. curr.
  AUUID AUUID Single identifier
  BPAPAY ADR Business partner address
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[CFODD]BPR (BPARTNER) !Block
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[CFODD]BPRPAY (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CFOBAN BAN Payment bank -> [BAN]BAN0 =[CFODD]CFOBAN (BANK) !Block
  CFODAT D Due date
  CPY CPY Company -> [CPY]CPY0 =[CFODD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CFODD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[CFODD]CUR (TABCUR) !Block
  DPTCOD ADI Dispute code -> [ADI]CODE =315;DPTCOD (ATABDIV) !Block
  DUDLIG C*3 Due date number
  DUDSTA C*1 Status
  FCY FCY Site -> [FCY]FCY0 =[CFODD]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGCLE C*1 Closed
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  LIG L*8 Line number
  NUM VCR Document no.
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAMTYP M*15 Payment type [menu 292: 1=Open item,2=Prepayment,3=Holdback]
  PAYCUR MD1 Paid
  PAYLOC MD1 Paid ref. currency
  PER C*2 Period
  SAC SAC Control
  SNS C*2 Sign
  TMPCUR MD1 Provisional payment
  TMPLOC MD1 Provisional payment
  TYP GTE Entry type -> [GTE]GTE0 =[CFODD]TYP (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFODD]UPDUSR (AUTILIS) !Other

## CFOMANMVT (CFOMM) - Cash forecast movements
Notes: activity code CFOM
Keys (first = PK; D = duplicates allowed): CFOMM0 CFOTYP+NUM+CFOLIN; CFOMM1 BPRNUM+BAN (D); CFOMM2 BAN+BPRNUM (D); CFOMM3 CFOTYP+CFOSTA+CPY+FCY (D)
Fields:
  ACCDAT D Accounting date
  AMTATI MD1 Amount
  AMTCUR MD1(20) Amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[CFOMM]BAN (BANK) !Block
  BPRNUM BPR BP -> [BPR]BPR0 =[CFOMM]BPRNUM (BPARTNER) !Block
  CFODAT D Due date
  CFOLIN L*8 Line
  CFOSTA M*15 Cash forecast status [menu 3637: 1=Active,2=Inactive,3=Modified,4=Obsolete]
  CFOTYP M*15 Forecast type [menu 3636: 21 values, see local-menus.md]
  COA COA Chart code -> [COA]COA0 =[CFOMM]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[CFOMM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CFOMM]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[CFOMM]CUR (TABCUR) !Block
  DAT D(20) Due date
  DAYS M*10(7) Days [menu 1: 1=No,2=Yes]
  DES A*40 Description
  DOCDAT D Document date
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[CFOMM]FCY (FACILITY) !Block
  IRT C*2 Increment
  LED LED Ledger -> [LED]LED0 =[CFOMM]LED (GLED) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NUM VCR Document no.
  PAM TAM Payment method -> [TAM]TAM0 =[CFOMM]PAM (TABPAM) !BSRA
  PAMDET TAM(20) Payment method -> [TAM]TAM0 =PAMDET;LEG (TABPAM) !Block
  PTE PTE Payment term -> [TPT]TPT0 =[CFOMM]PTE (TABPAYTERM) !BSRA
  RCR M*4 Periodic [menu 1: 1=No,2=Yes]
  SAC SAC Control
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  TEX AC0*4 Text
  TYPPER M*15 Periodicity [menu 3638: 1=Weekly,2=Monthly,3=First,4=Last]
  TYPRAT M*10 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFOMM]UPDUSR (AUTILIS) !Other

## CFOTYP (CFOT) - Cash forecast types
Notes: activity code CFOM
Keys (first = PK; D = duplicates allowed): CFOT0 CPY+FCY+CFOLIN; CFOT1 CPY+FCY+CFOTYP
Fields:
  AUUID AUUID Single identifier
  CFOLIN C*2 Line
  CFOTYP M*15 Forecast type [menu 3636: 21 values, see local-menus.md]
  CPY CPY Company -> [CPY]CPY0 =[CFOT]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CFOT]CREUSR (AUTILIS) !Other
  DAY1 C*2 Day 1
  DAY2 C*2 Day 2
  DAY3 C*2 Day 3
  DAYINC C*2 Increment
  FCY FCY Site -> [FCY]FCY0 =[CFOT]FCY (FACILITY) !Delete
  FLG M*4 Active [menu 1: 1=No,2=Yes]
  PASHOR C*3 Analysis period
  SNS M*10 Sign [menu 632: 1=Expense,2=Revenue]
  TYPRAT M*10 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFOT]UPDUSR (AUTILIS) !Other

## CHQBOK (CHB) - Checks table
Notes: activity code CHQ
Keys (first = PK; D = duplicates allowed): CHB0 BAN+CHQFIRNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[CHB]BAN (BANK) !Block
  CHQFIRNUM A*15 First check no.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCY FCY Site -> [FCY]FCY0 =[CHB]FCY (FACILITY) !Block
  NBRCHQ L*8 Number of checks
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CHQNUM (CHN) - Table of checks
Notes: activity code CHQ
Keys (first = PK; D = duplicates allowed): CHN0 BAN+CHQNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[CHN]BAN (BANK) !Block
  CHQNUM A*15 Check number
  CHQTYP M*15 Check type [menu 2761: 1=Manual,2=Normal]
  CLODAT D Cleared/Voided date
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  PAYNUM VCR Payment number
  PAYORDNUM A*1 Order of payment act:KAG
  POSPAYCREDAT D Positive Pay date act:CHQMG
  POSPAYSEQ A*14 Positive Pay seq. no. act:CHQMG
  PRNDAT D Print date
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  STA M*30 Status [menu 2658: 1=Unissued,2=Issued,3=Voided,4=Posted,5=Cleared]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## EDIFRM (EDM) - Formulas
Keys (first = PK; D = duplicates allowed): EDM0 MES+BAN+GRP+OCC+ORDNUM+SEG+SEGOCC+LIG
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[EDM]BAN (BANK) !Block
  CPS A*4 Composite
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDM]CREUSR (AUTILIS) !Other
  DATA A*4 Data
  FRM AFR*80 Formula
  GRP C*3 Group
  GRPCND AFR*40 Condition
  GRPSTA M*1 Group status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  LIG C*3 Line
  LONG C*4 Length
  MES A*10 Message
  OCC C*4 Group occurrences
  ORDNUM C*3 Order no.
  SEG EDS Segment -> [EDS]EDS0 =SEG;1 (EDISEG) !Block
  SEGCND AFR*40 Condition segment
  SEGOCC C*4 Segment occurrence
  SEGSTA M*1 Segment status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  STA M*1 Status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDM]UPDUSR (AUTILIS) !Other

## EDIPAR (EDP) - Message setup
Keys (first = PK; D = duplicates allowed): EDP0 MES+BAN+GRP+ORDNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[EDP]BAN (BANK) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDP]CREUSR (AUTILIS) !Other
  DES DES Description
  DESSHO SHO Short description
  FILREF A*2 File prefix
  GRP C*3 Group
  GRPSTA M*1 Status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  MES A*10 Message
  NATPAY M*5 File family [menu 2604: 1=None,2=LCR,3=PRE,4=VIR,5=SCT,6=SDD]
  OCC C*4 Group occurrences
  ORDNUM C*3 Order
  SEG EDS Segment -> [EDS]EDS0 =SEG;1 (EDISEG) !Block
  SEGOCC C*4 Segment occurrences
  SEGSTA M*1 Segment status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDP]UPDUSR (AUTILIS) !Other

## EDISEG (EDS) - Segments
Keys (first = PK; D = duplicates allowed): EDS0 SEG+LIG
Fields:
  AUUID AUUID Single identifier
  CPS A*4 Composite
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDS]CREUSR (AUTILIS) !Other
  DATA A*4 Data
  DES A*50 Description
  FLDTYP M*15 Field type [menu 783: 1=Alphanumeric,2=Numeric,3=Alpha]
  INTIT A*50 Field title
  LIG C*3 Line
  LONG C*4 Length
  SEG A*3 Segment
  STA M*1 Status [menu 782: 1=Mandatory,2=Required,3=Dependant,4=Advised,5=Optional,6=Not used]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDS]UPDUSR (AUTILIS) !Other

## EDITRBK (EBK) - Banking reconciliation report
Keys (first = PK; D = duplicates allowed): EBK0 BAN+CHK+NUMLIN; EBK1 BAN+NUMLIN
Fields:
  ACCDAT D Accounting date
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[EBK]BAN (BANK) !Block
  CHK A*5 Reconciliation
  CIB ADI Interbank code -> [ADI]CODE =306;CIB (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EBK]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[EBK]CUR (TABCUR) !Block
  DES DES Description
  ENTNUM A*15 Entry number
  NUMLIN C*4 Line number
  RBK A*6 Entry type
  REF REF Reference
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EBK]UPDUSR (AUTILIS) !Other

## EXPARAM (EXM) - Parameters
Keys (first = PK; D = duplicates allowed): EXM0 AXI+INDPF
Fields:
  AUUID AUUID Single identifier
  AXI M*15 Bracket [menu 2807: 1=10000,2=20000,3=999999]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  INDPF M*2 Vehicle category [menu 2808: 1=Category 1,2=Category 2,3=Category 3]
  INDRAT DCB*9.3 Rate
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## EXPENSES (EXS) - Expense
Notes: differs in V9.0 P12 (diff: AT3_EXPENSES.htm); differs in V10 P1 (diff: ATD_EXPENSES.htm)
Keys (first = PK; D = duplicates allowed): EXS0 CLB+DATEXS+NBREXS; EXS1 ACCNUM; EXS2 CPY+CUR+FCY+DATEXS (D); EXS3 VCRTYP+VCRNUM+ACCNUM; EXS4 PJTLIN (D)
Fields:
  ACC GAC(10) Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCNUM UNQ Internal number
  AMTATI MD2 Amount + tax
  AMTCUR MD2 Amount in currency
  AMTPAY MD2 Actual amt.
  AMTTAX1 MD2 Tax amount
  AMTTAX2 MD2 Tax amount
  AMTVAT MD2 Tax amount
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CLB AUS Employee -> [AUS]CODUSR =[EXS]CLB (AUTILIS) !Delete
  COA COA(10) Chart code -> [COA]COA0 =[EXS]COA (GCOA) !Delete
  CODEXP TES Expense codes -> [TES]TES0 =[EXS]CODEXP (TABEXPENS) !Block
  CPY CPY Company -> [CPY]CPY0 =[EXS]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[EXS]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[EXS]CURLED (TABCUR) !Delete
  DATEXS D Date
  DEDTAX1 MD2 Deductible tax
  DEDTAX2 MD2 Deductible tax
  DEDVAT MD2 Input VAT
  DES A*250 Comments
  DIE DIE Analytical dimension type -> [DIE]DIE0 =[EXS]DIE (GDIE) !Block act:ANA
  FCY FCY Site -> [FCY]FCY0 =[EXS]FCY (FACILITY) !Delete
  LED LED(10) Ledger -> [LED]LED0 =[EXS]LED (GLED) !Delete
  NBREXS C*2 Line no.
  PJTLIN PJT Project -> [PIM]PIM0 =[EXS]PJTLIN (PIMPL) !Block act:PJM
  QTY L*6 Quantity
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  STA M*15 Status [menu 2806: 1=Not posted,2=Posted simulation,3=Posted actual]
  TAX1 VAT Tax 1 -> [TVT]TVT0 =TAX1;[V]GSUPCLE (TABVAT) !Block
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Block
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax 3 -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block
  VISA AUS -> [AUS]CODUSR =[EXS]VISA (AUTILIS) !Block

## EXPENSESH (EXH) - Expense
Keys (first = PK; D = duplicates allowed): EXH0 CLB
Fields:
  ACSEXS ACS Access -> [ACS]ACS0 =[EXH]ACSEXS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CLB AUS Employee -> [AUS]CODUSR =[EXH]CLB (AUTILIS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FUP (FUP) - Reminders conducted
Notes: activity code FUP; differs in V9.0 P12 (diff: AT3_FUP.htm); differs in V10 P1 (diff: ATD_FUP.htm)
Keys (first = PK; D = duplicates allowed): FUP0 NUMEDT+LAN+TRI+GRPCRI (D); FUP1 NUMEDT+LAN+GRPCRI+LEVFUP (D); FUP2 TYP+NUM+LIG (D); FUP3 FUPMOD (D); FUP4 BPRFUP+ADD+FCY (D); FUP5 NUMEDT+ACCNUM+DUDLIG+NUMCOP; FUP6 NUMEDT+GRPCRI (D); FUP7 DST (D); FUP8 FCY (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM UNQ Internal number
  ADD ADR Address code
  AUUID AUUID Single identifier
  BANCRG MD1 Late charges
  BPRFUP BPR BP -> [BPR]BPR0 =[FUP]BPRFUP (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FUP]CREUSR (AUTILIS) !Other
  DATEDT D Print date
  DATREF D Reference date
  DEPRAT RAT Late charge rates
  DST AIM Destination -> [AIM]AIM0 =[FUP]DST (APRINTER) !Block
  DUDLIG C*3 Due date number
  FCY FCY Site -> [FCY]FCY0 =[FUP]FCY (FACILITY) !Block
  FUPCRG MD1 Reminder charge
  FUPCRGCUR MD1 Reminder charge
  FUPMOD M*15 Reminder method [menu 2629: 1=Letter,2=Email,3=Telephone,4=Fax]
  GRP FGP Group -> [FGP]FGP0 =[FUP]GRP (FUPGRP) !Block
  GRPCRI A*30 Grouping
  LAN LAN Language -> [TLA]TLA0 =[FUP]LAN (TABLAN) !Block
  LEVFUP C*2 Reminder level
  LIG C*3 Line number
  NBRCOP C*4 Number of copies
  NBRDAY C*3 Number of days
  NUM VCR Document no.
  NUMCOP C*4 Copy
  NUMEDT FUP Campaign number -> [TF0]TFP0 =NUMEDT (TMPFUP0) !Delete
  PREVIEW M*4 Pre-view [menu 1: 1=No,2=Yes]
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  TRI A*30 Sort criteria
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPTXT M*15 Text type [menu 2654: 1=By invoice,2=Global,3=By mail]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FUP]UPDUSR (AUTILIS) !Other

## FUPGRP (FGP) - Reminder groups
Notes: activity code FUP; differs in V9.0 P12 (diff: AT3_FUPGRP.htm); differs in V10 P1 (diff: ATD_FUPGRP.htm)
Keys (first = PK; D = duplicates allowed): FGP0 GRP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESTRA AX3 Description
  FUPBALTRS M*4 Balance [menu 1: 1=No,2=Yes]
  FUPCDT M*4 Taking into acc. of credit [menu 1: 1=No,2=Yes]
  FUPCRG MD1(5) Reminder charge
  FUPCTL M*4 Threshold/open item ctrl [menu 1: 1=No,2=Yes]
  FUPCUR M*4 Reminder/trans. curr. [menu 1: 1=No,2=Yes]
  FUPFCY M*4 Reminder by site [menu 1: 1=No,2=Yes]
  FUPFRY M*15 Reminder frequency [menu 3678: 1=Threshold,2=Interval]
  FUPINTERVAL C*4(5) Reminder interval
  FUPMAX C*1 Max. reminder level
  FUPMINAMT MD1 Minimum reminder
  FUPMOD M*15 Reminder method [menu 2629: 1=Letter,2=Email,3=Telephone,4=Fax]
  FUPTYP M*15 Reminder type [menu 235: 1=No reminder,2=By invoice,3=Global,4=Global by level,5=Global by date]
  GRP FGP Code -> [FGP]FGP0 =[FGP]GRP (FUPGRP) !Delete
  GRPNAM A*35 Group
  GRPSHO SHO Short description
  NBRCOP C*4 Number of copies
  SEUILS C*4(5) Reminder threshold
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## FUPTXT (FPT) - Reminder texts
Notes: activity code FUP
Keys (first = PK; D = duplicates allowed): FPT0 LAN+GRP+TYPTXT+LEVFUP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  GRP A*5 Group code
  LAN LAN Language -> [TLA]TLA0 =[FPT]LAN (TABLAN) !Block
  LEVFUP C*2 Reminder level
  TXT1 AC0*4 Header
  TXT2 AC0*4 Footer
  TYPTXT M*15 Reminder type [menu 2654: 1=By invoice,2=Global,3=By mail]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GACCDENCOD (CDA) - Payment attribute
Keys (first = PK; D = duplicates allowed): CDA0 COD+LEG
Fields:
  ACCBPR CAC Deposit acct code -> [CAC]CAC0 =14;ACCBPR;[V]GSUPCLE (GACCCODE) !Block
  ACCCOD CAC Accounting code -> [CAC]CAC0 =14;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACCSNS M*15 Accounting sign [menu 671: 1=Payment sign,2=Expense,3=Revenue]
  ACCTYP M*15 Account structure [menu 612: 1=Bank BP,2=Bank Account,3=Account BP]
  ACCVCRFLG M*4 Separate journal [menu 1: 1=No,2=Yes]
  ACS ACS Access code -> [ACS]ACS0 =[CDA]ACS (ACCCOD) !Block
  AMTMAX MD1 Maximum amount
  AUUID AUUID Single identifier
  BPCPIVTYP A*1 Customer invoice type act:KAG
  BPSPIVTYP A*1 Supp invoice type act:KAG
  CIB ADI Interbank code -> [ADI]CODE =306;CIB (ATABDIV) !Block
  COD CDA Destination code -> [CDA]CDA0 =COD;LEG (GACCDENCOD) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FLGEXPCRE M*4 Expense creation [menu 1: 1=No,2=Yes] act:FAS
  GFY AGF Group -> [AGF]AGF0 =[CDA]GFY (AGRPFCY) !Block
  IPTCOD GTE Entry type -> [GTE]GTE0 =IPTCOD;[V]GSUPCLE (GTYPACCENT) !Block
  IPTDAC M*4 Chargeable [menu 1: 1=No,2=Yes]
  IPTDEP M*4 Open item management [menu 1: 1=No,2=Yes]
  IPTTYP M*15 Internal type [menu 659: 1=Customer order,2=Supplier order,3=Accounting journal,4=Supplier proforma]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  PRCMAX DCB*2.2 Maximum %
  RPCVAT M*15 Tax management [menu 658: 1=No,2=Prepayment,3=Tax recovery,4=Tax/Charges]
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## GDUDSCR (GDS) - Open item screens
Keys (first = PK; D = duplicates allowed): GDS0 COD
Fields:
  AUUID AUUID Single identifier
  COD GDS Screen code -> [GDS]GDS0 =[GDS]COD (GDUDSCR) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAC C*4(60) Order
  DES DES Description
  DESTRA AX3
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLD A*10(60) Field
  NBRCOL C*2 No. of fixed columns
  NBRFLD C*2 Field nb
  NBRLIG C*4 Number of lines
  SAI M*4(60) Input [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  TOTDUD M*4 Open item total [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GFUPSCR (GFP) - Reminders screen
Notes: activity code FUP
Keys (first = PK; D = duplicates allowed): GFP0 COD
Fields:
  AUUID AUUID Single identifier
  COD GFP Screen code -> [GFP]GFP0 =[GFP]COD (GFUPSCR) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAC C*4(60) Order
  DES DES Description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLD A*10(60) Field
  NBRCOL C*2 No. of fixed columns
  NBRFLD C*2 Field nb
  NBRLIG C*4 Number of lines
  SAI M*4(60) Input [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  TOTDUD M*4 Open item total [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## HISTODUD (HDU) - Open item archive
Notes: activity code HDU
Keys (first = PK; D = duplicates allowed): HDU0 NUMHDU; HDU1 ACCNUM+DUDLIG (D); HDU2 CREDAT+NUMHDU; HDU3 ACCNUM+DUDLIG+NUMHDU
Fields:
  ACCNUM UNQ Internal number
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Local currency amount
  AUUID AUUID Single identifier
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[HDU]BPR (BPARTNER) !Other
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[HDU]BPRPAY (BPARTNER) !Other
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CPY CPY Company -> [CPY]CPY0 =[HDU]CPY (COMPANY) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[HDU]CUR (TABCUR) !Other
  DATEVT D Event date
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  DUDSTA C*1 Status
  FCY FCY Site -> [FCY]FCY0 =[HDU]FCY (FACILITY) !Other
  FLGCLE C*1 Closed
  FLGEVT A*10 Flag
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  LIG C*3 Line number
  NUM VCR Document no.
  NUMHDU UNQ Identifier
  PAYCUR MD1 Paid
  PAYDAT D Payment date
  PAYLOC MD1 Company paid
  SAC SAC Control
  SNS C*2 Sign
  TMPCUR MD1 Provisional payment
  TMPLOC MD1 Provisional payment
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Other
  TYPDUD M*15 Type of open item [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HDU]UPDUSR (AUTILIS) !Other

## INVDACPAR (IDP) - BP invoice entry settings
Keys (first = PK; D = duplicates allowed): IDP0 CPY+TYP
Fields:
  ACCDACFLG M*4(10) Enter account [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[IDP]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DAC C*4(10) Order
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NBRLED C*2 No. of ledgers
  TYP M*15 Document type [menu 2651: 1=Customer invoices,2=Supplier invoices]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## NETAUTO (NTO) - Netting
Keys (first = PK; D = duplicates allowed): NTO0 ACCNUM+DUDLIG+IND; NTO1 UIDUSR (D); NTO2 ACCNUMVCR (D)
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  ACCNUM L*8 Internal number
  ACCNUMVCR L*8 Internal number
  AMTCURNET MD1 Amount in currency
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =BPR (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[NTO]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =CUR (TABCUR) !Block
  DUDLIG C*3 Due date number
  FCYLIN FCY Site -> [FCY]FCY0 =FCYLIN (FACILITY) !Block
  IND C*4 Index
  NUM VCR Entry number
  SNS C*2 Sign
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PAYACCNUM (PAN) - Accounting payment entry
Keys (first = PK; D = duplicates allowed): PAN0 TYPNUM+NUM+STA+ACCNUM
Fields:
  ACCNUM UNQ Internal number
  ACCSTA C*2 Function
  ACETYP M*15 Grouping [menu 657: 1=Payment,2=Deposit slip/Paying bank,3=Due date]
  AUUID AUUID Single identifier
  CPTBAN M*4 Bank account [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PAN]CREUSR (AUTILIS) !Other
  GRP A*25 Group
  NUM VCR Payment
  RENCOD A*25 Reason
  RVSACCNUM UNQ Reversal
  STA C*3 Account structures
  TYPNUM M*15 Slip type [menu 685: 1=Bank deposits,2=Paying bank notice,3=Payment]
  TYPVCR A*2 Reference
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PAN]UPDUSR (AUTILIS) !Other

## PAYACCNUMD (PMD) - Accounting payment entry
Keys (first = PK; D = duplicates allowed): PMD0 NUM+ACCSTA+ACCNUM
Fields:
  ACCNUM UNQ Internal number
  ACCSTA C*2 Function
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PMD]CREUSR (AUTILIS) !Other
  NUM VCR Payment no.
  RVSACCNUM UNQ Reversal
  SNS C*2 Sign
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PMD]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Entry

## PAYFRM (FRM) - Payment slips
Keys (first = PK; D = duplicates allowed): FRM0 FRMFLG+FRMNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[FRM]BAN (BANK) !Block
  CHQTYP M*15 Check type [menu 654: 1=Check type 1,2=Check type 2,3=Foreign,4=Euro]
  CPY CPY Company -> [CPY]CPY0 =[FRM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXEDAT D Execution date
  FRMFCY FCY Site -> [FCY]FCY0 =[FRM]FRMFCY (FACILITY) !Block
  FRMFLG M*15 Slip type [menu 685: 1=Bank deposits,2=Paying bank notice,3=Payment]
  FRMNUM VCR Slip no.
  FRMTYP M*15 Discount type [menu 655: 1=Receipt,2=Discount,3=Receipt in value,4=Discount in value]
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  STA M*30 Status [menu 689: 1=Entered,2=Accepted,3=In draft management,4=Stage 4,5=Slip entered,6=Slip on file,7=Paying bank entered,8=On intermediate account,9=In the bank,10=Stage 10,11=Unpaid]
  TFBDAT D Bank file
  TFBFIL A*15 Bank file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PAYLOT (PYL) - Entry batch
Notes: differs in V9.0 P12 (diff: AT3_PAYLOT.htm); differs in V10 P1 (diff: ATD_PAYLOT.htm)
Keys (first = PK; D = duplicates allowed): PYL0 COD; PYL1 STA (D)
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[PYL]BAN (BANK) !Block
  BANCUR CUR Currency -> [TCU]TCU0 =[PYL]BANCUR (TABCUR) !BSRA
  COD VCR Code
  CPY CPY Company -> [CPY]CPY0 =[PYL]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  ENDBAL MD1 End balance
  FCY FCY Site -> [FCY]FCY0 =[PYL]FCY (FACILITY) !Block
  NBRPAY C*4 Number of payments
  PAYTYP TPY Transaction -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  PROBAL MD1 Progressive balance
  PRODIF MD1 Difference
  STA C*2 Status
  STRBAL MD1 Start balance
  TOTLOC DCB*13.2 Company currency total
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PAYMENTA (PYA) - Analytical payment lines
Keys (first = PK; D = duplicates allowed): PYA0 NUM+LIN+LINANA
Fields:
  AMTANA MD1 Amount
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PYA]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[PYA]DIE (GDIE) !Block act:ANA
  LIN C*3 Line
  LINANA C*3 Order no.
  NUM VCR Number
  QTYANA QTY Quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PYA]UPDUSR (AUTILIS) !Other

## PAYMENTD (PYD) - Payment lines
Keys (first = PK; D = duplicates allowed): PYD0 NUM+LIN; PYD1 DUDNUM+DUDLIG+NUM+LIN; PYD2 NUM+LIN+CURLIN
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  ACCSNS M*15 Accounting sign [menu 671: 1=Payment sign,2=Expense,3=Revenue]
  ACCTYP M*15 Account structure [menu 612: 1=Bank BP,2=Bank Account,3=Account BP]
  AMTBANFRC MD1 Bank amount
  AMTBANFRC1 MD1 Bank amount
  AMTBANFRC2 MD1 Bank amount
  AMTLIN MD1 Amount
  AMTLIN2 MD1 Allocated amount
  AUUID AUUID Single identifier
  BPRINV BPR Bill-to/Order BP -> [BPR]BPR0 =[PYD]BPRINV (BPARTNER) !Block
  BPRLIN BPR BPs -> [BPR]BPR0 =[PYD]BPRLIN (BPARTNER) !Block
  BPRSACINV SAC Inv. BP ctrl. account
  COA COA(10) Chart code -> [COA]COA0 =[PYD]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PYD]CREUSR (AUTILIS) !Other
  CURLIN CUR Currency -> [TCU]TCU0 =[PYD]CURLIN (TABCUR) !Block
  DENCOD CDA Destination -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DESLIN DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  DUDLIG C*2 Due date number
  DUDNUM UNQ Internal number
  EARDISFLG M*4 Settlement discount [menu 1: 1=No,2=Yes]
  FCYLIN FCY Site -> [FCY]FCY0 =[PYD]FCYLIN (FACILITY) !Block
  IPTTYP M*15 Internal type [menu 659: 1=Customer order,2=Supplier order,3=Accounting journal,4=Supplier proforma]
  LED LED(10) Ledger -> [LED]LED0 =[PYD]LED (GLED) !Block
  LIN C*3 Line
  NUM VCR Number
  NUMDEP A*1 Disc./charge invoice act:KAG
  PAYCURLIN MD1 Amount
  PAYLOCLIN MD1 Amount
  QTYLIN QTY Quantity
  RITAMT MD1 Retained amount act:KIT
  RITAMT2 MD1 Allocated withholdings act:KIT
  SACLIN SAC Control
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PYD]UPDUSR (AUTILIS) !Other
  VATLIN VAT VAT code -> [TVT]TVT0 =VATLIN;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block

## PAYMENTH (PYH) - Payment header
Notes: differs in V9.0 P12 (diff: AT3_PAYMENTH.htm); differs in V10 P1 (diff: ATD_PAYMENTH.htm)
Keys (first = PK; D = duplicates allowed): PYH0 NUM; PYH1 FRMFLG+FRMNUM+FRMLIN (D); PYH2 PAYLOT+PAYLOTLIG+NUM; PYH3 PAYTYP-NUM; PYH4 DUDDAT+NUM
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUMTRE UNQ(11) Internal number
  ACS ACS Access code -> [ACS]ACS0 =[PYH]ACS (ACCCOD) !Block
  AMTBAN MD1 Bank amount
  AMTCUR MD1 Amount
  AMTNYTBIL MD1 Note P/R amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[PYH]BAN (BANK) !Block
  BANDAT D Bank date act:KIT
  BANPAYTPY MD1 Bank amount
  BDFECOCOD PBDECO Economic reason -> [PBDECO]PBDECO0 =[PYH]BDFECOCOD (PBDECOCOD) !BSRA
  BDFMVTCOD ADI BDF movement code -> [ADI]CODE =307;BDFMVTCOD (ATABDIV) !Block
  BDFPAYCOD ADI BDF payment code -> [ADI]CODE =308;BDFPAYCOD (ATABDIV) !Block
  BICCOD A*11 BIC code act:VII
  BID BID Bank account number
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[PYH]BIDCRY (TABCOUNTRY) !Block
  BILDAT D Date created
  BILVCR VCR Draft no.
  BPAADDLIG A*35(3) Address line
  BPAINV ADR Address
  BPANAM NAM Company name
  BPR BPR BP -> [BPR]BPR0 =[PYH]BPR (BPARTNER) !Block
  BPRREF A*10 Drawee reference
  BPRSAC SAC Control
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  BSITRS A*30 Bank statement act:BSI
  CASHVATNUM A*250 Communication number act:KPO
  CHQBAN A*10 Pay-by branch
  CHQNUM A*15 Check number
  CHQTYP M*15 Check type [menu 654: 1=Check type 1,2=Check type 2,3=Foreign,4=Euro]
  COA COA Chart code -> [COA]COA0 =[PYH]COA (GCOA) !Block
  COMDAT D Communication date act:KPO
  CPY CPY Company -> [CPY]CPY0 =[PYH]CPY (COMPANY) !Block
  CRDAUZ A*10 Authorization number
  CRDEXYDAT D Validity date
  CRDNUM A*16 Bank card number
  CRDTYP ADI Card type -> [ADI]CODE =314;CRDTYP (ATABDIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[PYH]CRY (TABCOUNTRY) !Block
  CRYNAM A*30 Country name
  CSHVATRGM M*4 Tax rule [menu 1: 1=No,2=Yes] act:KPO
  CTY A*30 City
  CUR CUR Currency -> [TCU]TCU0 =[PYH]CUR (TABCUR) !Block
  CURRAT DCB*11 Currency rate
  DES DES Description
  DUDDAT D Due date
  EDTNUM L*8 Query no.
  EPANATPAY ADI Payment nature -> [ADI]CODE =313;EPANATPAY (ATABDIV) !Block act:VII
  EPARENPAY A*140 Payment reason act:VII
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[PYH]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGEND C*4 Endorsed flag act:KAG
  FRMDAT D Slip date
  FRMFCY FCY Note site -> [FCY]FCY0 =[PYH]FRMFCY (FACILITY) !Block
  FRMFLG M*15 Slip type [menu 685: 1=Bank deposits,2=Paying bank notice,3=Payment]
  FRMLIN C*4 Summary line
  FRMNUM VCR Slip no.
  FRMREF REF Remittance reference
  FRMTYP M*15 Discount type [menu 655: 1=Receipt,2=Discount,3=Receipt in value,4=Discount in value]
  FRMUSR A*5 Note user
  MIDBICCOD A*11 Intermediary bank BIC code act:VII
  MIDCRY CRY Intermediary bank country -> [TCY]TCY0 =[PYH]MIDCRY (TABCOUNTRY) !Block act:VII
  MIDPAB1 A*35 Intermediary bank name act:VII
  MIDPAB2 A*35 Intermediary bank address 1 act:VII
  MIDPAB3 A*35 Intermediary bank address 2 act:VII
  MIDPAB4 A*35 Intermediary bank address 3 act:VII
  NUM VCR Payment no.
  NUMORD A*1 Payment order act:KAG
  ORIDAT D Source date
  PAB1 A*35 Paying bank 1
  PAB2 A*35 Paying bank 2
  PAB3 A*35 Paying bank 3 act:VII
  PAB4 A*35 Paying bank 4 act:VII
  PABAMTPRT MD1 Partial amount
  PABFLG M*4 Accepted [menu 1: 1=No,2=Yes]
  PABREN ADI Non accepted reason -> [ADI]CODE =305;PABREN (ATABDIV) !Block
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAYLOT VCR Batch code
  PAYLOTLIG C*4 Batch line
  PAYNUMEND A*1 Endorsed payment act:KAG
  PAYTYP TPY Transaction -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  PER C*2 Period
  POSCOD POS Postal code
  PST C*1 Posted
  PURTYP M*15 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  REF REF Reference
  RENNOTPAY ADI Late payment reason -> [ADI]CODE =310;RENNOTPAY (ATABDIV) !Block
  SAT SAT County
  SENBPR A*1 Sender act:KAG
  SENCRN A*1 Site tax ID no. act:KAG
  SENORI A*1 Initial issuer act:KAG
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  STA M*30 Status [menu 689: 1=Entered,2=Accepted,3=In draft management,4=Stage 4,5=Slip entered,6=Slip on file,7=Paying bank entered,8=On intermediate account,9=In the bank,10=Stage 10,11=Unpaid]
  STAFLG M*4(11) Status flags [menu 1: 1=No,2=Yes]
  SUP1 A*20 Extra field 1
  SUP2 A*20 Extra field 2
  SUP3 A*20 Extra field 3
  SWIIPI A*20 IPI code act:KSW
  SWISUP1 M*15 Instruction key EZAG [menu 3660: 1=None,2=Personally,3=Urgent] act:KSW
  SWISUP2 M*15 Instruction key DTA [menu 3659: 1=None,2=Salary, Pension] act:KSW
  SWISUP3 M*15 Bank charge bearer [menu 3658: 1=Shared,2=Beneficiary,3=Applicant] act:KSW
  TFBDAT D Bank file
  TFBFIL A*15 Bank file
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UMRSEQ A*30 Sequence act:SDD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALDAT D Value date
  VATSTA M*15 Status [menu 3619: 1=Entered,2=Printed,3=Communicated] act:KPO

## PAYMENTPORD (PYPTD) - Payment lines
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PYPTD0 NUM+LIN
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  ACCSNS M*15 Accounting sign [menu 671: 1=Payment sign,2=Expense,3=Revenue]
  ACCTYP M*15 Account structure [menu 612: 1=Bank BP,2=Bank Account,3=Account BP]
  AMTBANFRC MD1 Bank amount
  AMTBANFRC1 MD1 Bank amount
  AMTBANFRC2 MD1 Bank amount
  AMTLIN MD1 Amount
  AMTLIN2 MD1 Allocated amount
  AUUID AUUID Single identifier
  BPRINV BPR Bill-to/Order BP -> [BPR]BPR0 =[PYPTD]BPRINV (BPARTNER) !Block
  BPRLIN BPR BPs -> [BPR]BPR0 =[PYPTD]BPRLIN (BPARTNER) !Block
  BPRSACINV SAC Inv. BP ctrl. account
  COA COA(10) Chart code -> [COA]COA0 =[PYPTD]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREDATTIM1 ADATIM User
  CREUSR AUS User -> [AUS]CODUSR =[PYPTD]CREUSR (AUTILIS) !Other
  CREUSR1 AUS User -> [AUS]CODUSR =[PYPTD]CREUSR1 (AUTILIS) !Other
  CURLIN CUR Currency -> [TCU]TCU0 =[PYPTD]CURLIN (TABCUR) !Block
  DENCOD CDA Destination -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DESLIN DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  DUDLIG C*2 Due date number
  DUDNUM UNQ Internal number
  EARDISFLG M*4 Settlement discount [menu 1: 1=No,2=Yes]
  FCYLIN FCY Site -> [FCY]FCY0 =[PYPTD]FCYLIN (FACILITY) !Block
  IPTTYP M*15 Internal type [menu 659: 1=Customer order,2=Supplier order,3=Accounting journal,4=Supplier proforma]
  LED LED(10) Ledger -> [LED]LED0 =[PYPTD]LED (GLED) !Block
  LIN C*3 Line
  NUM VCR Number
  NUMDEP A*10 Disc./charge invoice act:KAG
  PAYCURLIN MD1 Amount
  PAYLOCLIN MD1 Amount
  QTYLIN QTY Quantity
  RITAMT MD1 Retained amount act:KIT
  RITAMT2 MD1 Allocated withholdings act:KIT
  SACLIN SAC Control
  UPDDATTIM ADATIM Date time
  UPDDATTIM1 ADATIM User
  UPDUSR AUS User -> [AUS]CODUSR =[PYPTD]UPDUSR (AUTILIS) !Other
  UPDUSR1 AUS User -> [AUS]CODUSR =[PYPTD]UPDUSR1 (AUTILIS) !Other
  VATLIN VAT VAT code -> [TVT]TVT0 =VATLIN;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block

## PAYMENTPORH (PYPTH) - Payment header
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PYPTH0 NUM
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUMTRE UNQ(11) Internal number
  ACS ACS Access code -> [ACS]ACS0 =[PYPTH]ACS (ACCCOD) !Block
  AMTBAN MD1 Bank amount
  AMTCUR MD1 Amount
  AMTNYTBIL MD1 Note P/R amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[PYPTH]BAN (BANK) !Block
  BANDAT D Bank date act:KIT
  BANPAYTPY MD1 Bank amount
  BDFECOCOD PBDECO Economic reason -> [PBDECO]PBDECO0 =[PYPTH]BDFECOCOD (PBDECOCOD) !BSRA
  BDFMVTCOD ADI BDF movement code -> [ADI]CODE =307;BDFMVTCOD (ATABDIV) !Block
  BDFPAYCOD ADI BDF payment code -> [ADI]CODE =308;BDFPAYCOD (ATABDIV) !Block
  BICCOD A*11 BIC code act:VII
  BID BID Bank account number
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[PYPTH]BIDCRY (TABCOUNTRY) !Block
  BILDAT D Date created
  BILVCR VCR Draft no.
  BPAADDLIG A*35(3) Address line
  BPAINV ADR Address
  BPANAM NAM Company name
  BPR BPR BP -> [BPR]BPR0 =[PYPTH]BPR (BPARTNER) !Block
  BPRREF A*10 Drawee reference
  BPRSAC SAC Control
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  BSITRS A*30 Bank statement act:BSI
  CASHVATNUM A*250 Communication number act:KPO
  CHQBAN A*10 Pay-by branch
  CHQNUM A*15 Check number
  CHQTYP M*15 Check type [menu 654: 1=Check type 1,2=Check type 2,3=Foreign,4=Euro]
  COA COA Chart code -> [COA]COA0 =[PYPTH]COA (GCOA) !Block
  COMDAT D Communication date act:KPO
  CPY CPY Company -> [CPY]CPY0 =[PYPTH]CPY (COMPANY) !Block
  CRDAUZ A*10 Authorization number
  CRDEXYDAT D Validity date
  CRDNUM A*16 Bank card number
  CRDTYP ADI Card type -> [ADI]CODE =314;CRDTYP (ATABDIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREDATTIM1 ADATIM Date time
  CREUSR A*5 Creation user
  CREUSR1 AUS User -> [AUS]CODUSR =[PYPTH]CREUSR1 (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[PYPTH]CRY (TABCOUNTRY) !Block
  CRYNAM A*30 Country name
  CSHVATRGM M*4 Tax rule [menu 1: 1=No,2=Yes] act:KPO
  CTY A*30 City
  CUR CUR Currency -> [TCU]TCU0 =[PYPTH]CUR (TABCUR) !Block
  CURRAT MD5 Currency rate
  DES DES Description
  DUDDAT D Due date
  EDTNUM L*8 Query no.
  EPANATPAY ADI Payment nature -> [ADI]CODE =313;EPANATPAY (ATABDIV) !Block act:VII
  EPARENPAY A*140 Payment reason act:VII
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[PYPTH]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGEND C*4 Endorsed flag act:KAG
  FRMDAT D Slip date
  FRMFCY FCY Note site -> [FCY]FCY0 =[PYPTH]FRMFCY (FACILITY) !Block
  FRMFLG M*15 Slip type [menu 685: 1=Bank deposits,2=Paying bank notice,3=Payment]
  FRMLIN C*4 Summary line
  FRMNUM VCR Slip no.
  FRMREF REF Remittance reference
  FRMTYP M*15 Discount type [menu 655: 1=Receipt,2=Discount,3=Receipt in value,4=Discount in value]
  FRMUSR A*5 Note user
  MIDBICCOD A*11 Intermediary bank BIC code act:VII
  MIDCRY CRY Intermediary bank country -> [TCY]TCY0 =[PYPTH]MIDCRY (TABCOUNTRY) !Block act:VII
  MIDPAB1 A*35 Intermediary bank name act:VII
  MIDPAB2 A*35 Intermediary bank address 1 act:VII
  MIDPAB3 A*35 Intermediary bank address 2 act:VII
  MIDPAB4 A*35 Intermediary bank address 3 act:VII
  NUM VCR Payment no.
  NUMORD A*10 Payment order act:KAG
  ORIDAT D Source date
  PAB1 A*35 Paying bank 1
  PAB2 A*35 Paying bank 2
  PAB3 A*35 Paying bank 3 act:VII
  PAB4 A*35 Paying bank 4 act:VII
  PABAMTPRT MD1 Partial amount
  PABFLG M*4 Accepted [menu 1: 1=No,2=Yes]
  PABREN ADI Non accepted reason -> [ADI]CODE =305;PABREN (ATABDIV) !Block
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAYLOT VCR Batch code
  PAYLOTLIG C*4 Batch line
  PAYNUMEND A*10 Endorsed payment act:KAG
  PAYTYP TPY Transaction -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  PER C*2 Period
  POSCOD POS Postal code
  PST C*1 Posted
  PURTYP M*15 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  REF REF Reference
  RENNOTPAY ADI Late payment reason -> [ADI]CODE =310;RENNOTPAY (ATABDIV) !Block
  SAT SAT County
  SENBPR A*10 Sender act:KAG
  SENCRN A*10 Site tax ID no. act:KAG
  SENORI A*10 Initial issuer act:KAG
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  STA M*30 Status [menu 689: 1=Entered,2=Accepted,3=In draft management,4=Stage 4,5=Slip entered,6=Slip on file,7=Paying bank entered,8=On intermediate account,9=In the bank,10=Stage 10,11=Unpaid]
  STAFLG M*4(11) Status flags [menu 1: 1=No,2=Yes]
  SUP1 A*20 Extra field 1
  SUP2 A*20 Extra field 2
  SUP3 A*20 Extra field 3
  SWIIPI A*20 IPI code act:KSW
  SWISUP1 M*15 Instruction key EZAG [menu 3660: 1=None,2=Personally,3=Urgent] act:KSW
  SWISUP2 M*15 Instruction key DTA [menu 3659: 1=None,2=Salary, Pension] act:KSW
  SWISUP3 M*15 Bank charge bearer [menu 3658: 1=Shared,2=Beneficiary,3=Applicant] act:KSW
  TFBDAT D Bank file
  TFBFIL A*15 Bank file
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Block act:SDD
  UMRSEQ A*30 Sequence act:SDD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDDATTIM1 ADATIM Date time
  UPDUSR A*5 Change user
  UPDUSR1 AUS User -> [AUS]CODUSR =[PYPTH]UPDUSR1 (AUTILIS) !Other
  VALDAT D Value date
  VATSTA M*15 Status [menu 3619: 1=Entered,2=Printed,3=Communicated] act:KPO

## PAYMTCTMP (PMP) - Payment matching temp table
Keys (first = PK; D = duplicates allowed): PMP0 NUM+NUMORD+LEDTYP+FCY+ACC+BPR+OCC1+OCC2 (D); PMP1 NUM+NUMORD+LEDTYP+FCY+ACC+BPR+ACCNUM (D); PMP2 NUM+NUMORD+LEDTYP+CUR+FCY+ACC+BPR+OCC1+OCC2 (D); PMP3 UIDUSR (D)
Fields:
  ACC GAC General accounts -> [GAC]GAC0 ="";ACC (GACCOUNT) !Other
  ACCNUM UNQ Internal number
  AMTIPTCUR MD1 Amount in currency
  AMTIPTLED MD1 Amount in currency
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[PMP]BPR (BPARTNER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PMP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PMP]CUR (TABCUR) !Block
  DUDLIG C*3 Due date number
  FCY FCY Site -> [FCY]FCY0 =[PMP]FCY (FACILITY) !Block
  INVMTC M*4 Invoice matching [menu 1: 1=No,2=Yes]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NUM VCR Payment no.
  NUMORD C*2 Order no.
  OCC1 C*4 Occurrence
  OCC2 C*4 Occurrence
  TYPVCR M*20 Entry reference [menu 2626: 1=Main account,2=Account journal - business partner,3=Bank journal > account,4=Treasury currency MO,5=Currency MO,6=Business partner MO,7=Account transfer,8=Discounted drafts,9=Draft transfer,10=Tax stamp]
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PMP]UPDUSR (AUTILIS) !Other

## PAYMTCTMP2 (PM2) - Payment matching temp table
Keys (first = PK; D = duplicates allowed): PM20 TYP+NUM+LEDTYP+CUR+FCY+ACC+BPR+ACCNUM; PM21 UIDUSR (D)
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Internal number
  AMTIPTCUR MD1 Amount in currency
  AMTIPTLED MD1 Amount in currency
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[PM2]BPR (BPARTNER) !Block
  COA COA Chart code -> [COA]COA0 =[PM2]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PM2]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PM2]CUR (TABCUR) !Block
  DUDLIG C*3 Due date number
  FCY FCY Site -> [FCY]FCY0 =[PM2]FCY (FACILITY) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NUM VCR Document no.
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PM2]UPDUSR (AUTILIS) !Other

## PAYPTD (PYP) - Payment order lines/receipt
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PAYPTH (PAH) - Payment order header/receipts
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PAYPTHDOC (PAO) - Payment orders/receipt documents
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PAYPTHRIT (PRI) - Withholdings
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PAYTMP (PTP) - Temporary payments table
Keys (first = PK; D = duplicates allowed): PTP0 TYPREC+NUM+CODACE+LIGCODACE+VCRNUM+LIG+NUMORD; PTP1 TYPREC+NUM+CODACE+VCRNUM+LIG+LIGCODACE+NUMORD; PTP2 TYPREC+NUM+LIG+DUDNUM+DUDLIG+CODACE+LIGCODACE (D); PTP3 UIDUSR (D)
Fields:
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  CODACE GAU Entry code -> [GAU]GAU0 =CODACE (GAUTACE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PTP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PTP]CUR (TABCUR) !Delete
  CURCPY CUR Company currency -> [TCU]TCU0 =[PTP]CURCPY (TABCUR) !Delete
  DUDLIG C*3 Due date number
  DUDNUM UNQ Due date number
  LIG C*3 Line number
  LIGCODACE C*4 Line number
  NUM VCR Payment no.
  NUMORD C*2 Order no.
  SNS C*2 Sign
  TYPREC A*3 Record type
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PTP]UPDUSR (AUTILIS) !Other
  VCRNUM C*2 Document no.

## POOL (POO) - Banking pool
Keys (first = PK; D = duplicates allowed): POO0 POO+LIN
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[POO]BAN (BANK) !Block
  CPY CPY Company -> [CPY]CPY0 =[POO]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[POO]FCY (FACILITY) !Block
  LIN C*3 Line number
  POO A*10 Code
  PRC DCB*3.2 Percentage
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## PROROG (PRO) - Due date extension
Keys (first = PK; D = duplicates allowed): PRO0 NUM (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM UNQ(10) Internal number
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[PRO]BPR (BPARTNER) !Block
  COA COA Chart of accounts -> [COA]COA0 =[PRO]COA (GCOA) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PRO]CUR (TABCUR) !Block
  NEWDUDDAT D Due date
  NUM VCR Number
  OLDDUDDAT D Due date
  TYP C*1 BP type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PRO]UPDUSR (AUTILIS) !Other

## PROROGPCE (PRP) - Due date extension
Keys (first = PK; D = duplicates allowed): PRP0 ACCNUM; PRP1 NUM+ACCNUM
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ Internal number
  AMTCUR MD1(10) Amount in currency
  AMTLED MD1(10) Ledger amount
  AUUID AUUID Single identifier
  BPRC BPR BP -> [BPR]BPR0 =[PRP]BPRC (BPARTNER) !Block
  BPRD BPR BP -> [BPR]BPR0 =[PRP]BPRD (BPARTNER) !Block
  CLIFOU M*15 BP type [menu 644: 1=Customer,2=Supplier]
  COA COA(10) Chart of accounts -> [COA]COA0 =[PRP]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PRP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PRP]CUR (TABCUR) !Block
  DES DES Description
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[PRP]FCY (FACILITY) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[PRP]FCYLIN (FACILITY) !Block
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  NUM VCR Number
  NUM2 VCR Number
  TACCNUM MD1(10) Internal number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PRP]UPDUSR (AUTILIS) !Other

## RBKBELDET (RBD) - Belgian bank statement detail
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): RBD0 RBKNUM+RBKLIN; RBD1 FRMNUM (D)
Fields:
  ACCBAN GAC Bank account -> [GAC]GAC0 =COA;ACCBAN (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCTMP GAC Temporary account -> [GAC]GAC0 =COA;ACCTMP (GACCOUNT) !Block
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BPRNAM NAM Company name
  BPRNUM BPR BP code -> [BPR]BPR0 =[RBD]BPRNUM (BPARTNER) !Block
  COA COA Chart code -> [COA]COA0 =[RBD]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RBD]CREUSR (AUTILIS) !Other
  FCYLIN FCY Site -> [FCY]FCY0 =[RBD]FCYLIN (FACILITY) !Block
  FRMNUM VCR Slip no.
  PAYTYP TPY Payment transaction -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  PYHNUM VCR Payment number
  RBKLIN L*8 Statement line number
  RBKNUM VCR Statement number
  SNS M*15 Sign [menu 661: 1=Expense,2=Revenue,3=Unspecified]
  STATUT M*15 Status [menu 509: 1=Pending,2=To validate,3=Validated]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RBD]UPDUSR (AUTILIS) !Other
  VALDAT D Value date
  VALFLG M*4 To validate [menu 1: 1=No,2=Yes]

## RBKBELDUD (RBU) - Belgian bank stmnt open item
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): RBU0 RBKNUM+RBKLIN+LIN; RBU1 DUDNUM+DUDLIG (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTLIN MD1 Bank amount
  AMTLINCUR MD1 Currency amount
  AMTLINLOC MD1 Ref. amt. curr.
  AUUID AUUID Single identifier
  BELVCS VCS VCS number
  BICCOD A*11 BP BIC code
  BIDNUM BID BP account no.
  COA COA Chart code -> [COA]COA0 =[RBU]COA (GCOA) !Block
  CODOP A*4 Operation code
  COMFLD A*250 Communication field
  COMFLG M*4 Structured com [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RBU]CREUSR (AUTILIS) !Other
  DENCOD CDA Destination -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DUDDAT D Due date
  DUDLIG C*2 Due date number
  DUDNUM UNQ Internal number
  LIN C*3 Line
  NUMSEQ A*8 Sequence number
  OFFACCNAM NAM Counterpart name
  RBKLIN L*8 Statement line number
  RBKNUM VCR Statement number
  REFINT A*35 Internal reference
  RUB RRB Heading -> [RRB]RRB0 =[RBU]RUB (RBKRUBBEL) !Other
  TYP C*1 Type
  TYPCOM TYC Communication type -> [TYC]TYC0 =TYPCOM;1 (TYPCOMBEL) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RBU]UPDUSR (AUTILIS) !Other
  VATLIN VAT VAT code -> [TVT]TVT0 =VATLIN;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block

## RBKBELHEA (RBH) - Belgian bank statement
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): RBH0 RBKNUM; RBH1 ACCNUM
Fields:
  ACCDES NAM Account description
  ACCNAM NAM Account holder name
  ACCNUM UNQ Unique number
  AMTCDT MD1 Credit T/O
  AMTDEB MD1 Debit T/O
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[RBH]BAN (BANK) !Block
  BICCODBAN A*11 Bank BIC code
  BIDNUMBAN BID Bank account no.
  CPY CPY Company -> [CPY]CPY0 =[RBH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation author -> [AUS]CODUSR =[RBH]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[RBH]CUR (TABCUR) !Block
  DESTNAM NAM Recipient name
  EXTNUM C*3 Sequence
  FCY FCY Site -> [FCY]FCY0 =[RBH]FCY (FACILITY) !Block
  FILNAM A*20 File name
  FILTYP M*8 File format [menu 3622: 1=CODA,2=Manual]
  FRETXT A*80(10) Additional info
  IDENTNUM A*20 Identification no.
  NEWAMT MD1 New balance
  NEWDAT D New balance date
  NEWSNS M*10 New balance sign [menu 626: 1=Debit,2=Credit]
  OLDAMT MD1 Previous balance
  OLDDAT D Previous balance date
  OLDSNS M*10 Previous balance sign [menu 626: 1=Debit,2=Credit]
  RBKNUM VCR Statement number
  RELTYP M*15 Note type [menu 694: 1=Imported,2=Entered]
  STATUT M*15 Status [menu 509: 1=Pending,2=To validate,3=Validated]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[RBH]UPDUSR (AUTILIS) !Other

## RBKBELTMP (RBW) - Belgian bank stmnt open item
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): RBW0 RBKNUM+RBKLIN+LIN; RBW1 DUDNUM+DUDLIG (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTLIN MD1 Bank amount
  AMTLINCUR MD1 Currency amount
  AMTLINCURORI MD1 Original amount
  AMTLINLOC MD1 Ref. amt. curr.
  AMTLINORI MD1 Original amount
  AUUID AUUID Single identifier
  BELVCS VCS VCS number
  BICCOD A*11 BP BIC code
  BIDNUM BID BP account no.
  COA COA Chart code -> [COA]COA0 =[RBW]COA (GCOA) !Block
  CODOP A*4 Operation code
  COMFLD A*250 Communication field
  COMFLG M*4 Structured com [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RBW]CREUSR (AUTILIS) !Other
  DENCOD CDA Destination -> [CDA]CDA0 =DENCOD;[V]GSUPCLE (GACCDENCOD) !Block
  DUDDAT D Due date
  DUDLIG C*2 Due date number
  DUDLIGORI C*2 Origin line
  DUDNUM UNQ Internal number
  DUDNUMORI UNQ Source
  LIN C*3 Line
  NUMSEQ A*8 Sequence number
  OFFACCNAM NAM Counterpart name
  RBKLIN L*8 Statement line number
  RBKNUM VCR Statement number
  REFINT A*35 Internal reference
  RUB RRB Heading -> [RRB]RRB0 =[RBW]RUB (RBKRUBBEL) !Other
  TYP C*1 Type
  TYPCOM TYC Communication type -> [TYC]TYC0 =TYPCOM;1 (TYPCOMBEL) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RBW]UPDUSR (AUTILIS) !Other
  VATLIN VAT VAT code -> [TVT]TVT0 =VATLIN;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block

## RBKRUBBEL (RRB) - CODA headings
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): RRB0 RUB
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block act:NBCOA
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[RRB]COA (GCOA) !Block act:NBCOA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RRB]CREUSR (AUTILIS) !Block
  DES DES Description
  DESSHO SHO Short description
  IPTTYP M*8 Allocation [menu 3621: 1=None,2=Account]
  RUB RRB Heading -> [RRB]RRB0 =[RRB]RUB (RBKRUBBEL) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RRB]UPDUSR (AUTILIS) !Block

## RCRINVOICE (RCH) - Recurring invoices
Keys (first = PK; D = duplicates allowed): RCH0 RCRNUM; RCH1 RCRTYP+NUM (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[RCH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DLY M*20 Daily [menu 2812: 1=Daily,2=Weekdays]
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[RCH]FCY (FACILITY) !Block
  MONDAY C*3 Day of the month
  MONIRT C*3 Month increment
  NUM VCR Invoice number
  RCRNUM VCR Recurring number
  RCRPAN M*20 Recurrence pattern [menu 2811: 1=Daily,2=Weekly,3=Monthly]
  RCRSTA M*20 Status [menu 2814: 1=Pending,2=In process,3=Completed,4=Canceled]
  RCRTYP M*20 Recurring type [menu 2813: 1=Customer BP invoice,2=Supplier BP invoice]
  STRDAT D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  WEEDAY M*20 Day of the week [menu 742: 1=Monday,2=Tuesday,3=Wednesday,4=Thursday,5=Friday,6=Saturday,7=Sunday]
  WEEIRT C*3 Week increment

## RELBANK (RBK) - Bank account statement
Notes: differs in V9.0 P12 (diff: AT3_RELBANK.htm); differs in V10 P1 (diff: ATD_RELBANK.htm)
Keys (first = PK; D = duplicates allowed): RBK0 BAN+RBKNUM+RECTYP+RBKLIN; RBK1 BAN+RECTYP+OPEDAT+RBKNUM+RBKLIN; RBK2 BAN+RBKNUM (D); RBK3 BAN+NUMRBK; RBK4 NUMRBK
Fields:
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BAN BAN Code -> [BAN]BAN0 =[RBK]BAN (BANK) !Block
  BANCIB ADI Interbank code -> [ADI]CODE =306;BANCIB (ATABDIV) !Block
  BSISTM A*30 Bank statement act:BSI
  CHK A*5 Reconciliation
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RBK]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[RBK]CUR (TABCUR) !Block
  DATCHK D Reconciliation date
  DATXTR D Extraction date
  DES DES Description
  ENTNUM A*8 Entry number
  INDCOM M*4 Commission level [menu 1: 1=No,2=Yes]
  INDUVY M*4 Unavailable [menu 1: 1=No,2=Yes]
  NUMRBK UNQ Internal number
  OPEDAT D Date
  ORI M*15 Source [menu 694: 1=Imported,2=Entered]
  RBKLIN L*8 Number
  RBKNUM VCR Statement number
  RECTYP M*15 Record type [menu 656: 1=Header,2=Detail,3=Total,4=Subtotal,5=Detail 2]
  REF REF Reference
  RENREJ ADI Reject reason -> [ADI]CODE =305;RENREJ (ATABDIV) !Block
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RBK]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## RELBANKREM (RBR) - Bank statement comments
Keys (first = PK; D = duplicates allowed): CRR0 BAN+RBKNUM+RBKLIN+REMNUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank account -> [BAN]BAN0 =[RBR]BAN (BANK) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RBR]CREUSR (AUTILIS) !Other
  RBKLIN L*8 Statement line number
  RBKNUM VCR Statement number
  REM A*80 Comment
  REMNUM C*4 Comment number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RBR]UPDUSR (AUTILIS) !Other

## RELMT940 (RLT) - File FMT940 (header)
Notes: activity code KDE
Keys (first = PK; D = duplicates allowed): RLT0 FILNUM+TRFNUM+SEQNUM; RLT1 BAN+FILNUM (D); RLT2 BAN+FILNUM+TRFNUM+SEQNUM; RLT3 BAN+TRFNUM+SEQNUM (D)
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[RLT]BAN (BANK) !Block
  CPY CPY Company -> [CPY]CPY0 =[RLT]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[RLT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[RLT]CUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[RLT]FCY (FACILITY) !Block
  FILNUM VCR File number
  REFBAN A*30 Bank reference
  SEQNUM A*12 Sequence number
  TRFNUM A*20 Transaction number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RLT]UPDUSR (AUTILIS) !Other

## RELMT940D (RLD) - File FMT940 (lines)
Keys (first = PK; D = duplicates allowed): RLD0 FILNUM+TRFNUM+SEQNUM+LIN; RLD1 BAN+FILNUM (D)
Fields:
  AMTCUR MD1 Amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[RLD]BAN (BANK) !Block
  BIDNUM BID Bank account number
  BPRINV BPR Bill-to BP -> [BPR]BPR0 =[RLD]BPRINV (BPARTNER) !Block
  BPRPAY BPR BP -> [BPR]BPR0 =[RLD]BPRPAY (BPARTNER) !Block
  BPRREF A*30(5) BP reference
  CPY CPY Company -> [CPY]CPY0 =[RLD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RLD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[RLD]CUR (TABCUR) !Block
  DES DES Reference
  DUDDAT D Due date
  DUDLIG C*2 Due date number
  DUDNUM UNQ Internal number
  FCYLIN FCY Site -> [FCY]FCY0 =[RLD]FCYLIN (FACILITY) !Block
  FILNUM VCR File number
  FLGCRE C*1 Creation flag
  FREREF A*30(10) Free reference
  LET A*1 Code
  LIN C*3 Line number
  NUM VCR Invoice no.
  NUMREG VCR Payment no. generated
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  SEQNUM A*12 Sequence number
  SNS A*2 Sign
  TRFNUM A*20 Transaction number
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RLD]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## RITCUM (RCU) - Withholding total
Notes: activity code KAG
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## RSLINESGER1 (RSLG1) - Recapitulative statement
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): RSLG1 USERID (D); RSLG2 USERID+GEREECNUM+TRNTYP
Fields:
  AMTTRN MD1 Turnover
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[RSLG1]CREUSR (AUTILIS) !Block
  CRY CRY Country -> [TCY]TCY0 =[RSLG1]CRY (TABCOUNTRY) !Block
  FLG A*3
  GEREECNUM A*20 EU VAT no.
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TRNTYP REPLINDE Turnover type -> [RLI]RLI0 =LEG;2;TRNTYP (REPLINDEF) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[RSLG1]UPDUSR (AUTILIS) !Block
  USERID ID User identity+ adxuid

## RSLINESGER2 (RSLG2) - Recapitulative statement
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): RSLG2 USERID (D); RSLG3 USERID+GEREECNUM+TRNTYP (D)
Fields:
  AMTTRN MD1 Turnover
  AUUID AUUID Single identifier
  CAT M*15 Category [menu 618: 1=Actual,2=Active simulation,3=Inactive simulation,4=Off-balance-sheet,5=Template]
  COMMENT A*120 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[RSLG2]CREUSR (AUTILIS) !Block
  CRY CRY Country -> [TCY]TCY0 =[RSLG2]CRY (TABCOUNTRY) !Block
  DESVCR DES Description
  FLG A*3
  GEREECNUM A*20 EU VAT no.
  NUM VCR Document no.
  OFFACC BPR Offset -> [BPR]BPR0 =[RSLG2]OFFACC (BPARTNER) !Block
  STA M*15 Statistics [menu 617: 1=Temporary,2=Final]
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TRNTYP REPLINDE Turnover type -> [RLI]RLI0 =LEG;2;TRNTYP (REPLINDEF) !Block
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[RSLG2]UPDUSR (AUTILIS) !Block
  USERID ID User identity+ adxuid
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACBPRRSP TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block

## SOI (SOI) - Statement creation
Keys (first = PK; D = duplicates allowed): SOI0 SOINUM; SOI1 FWDSOI (D); SOI2 CPY+FCY+BPR+SOIDAT+SOINUM; SOI3 CPY+BPR+CUR+SOINUM; SOI4 TYPSOI+NUMSOI+SOINUM
Fields:
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BILVCR VCR Draft no.
  BPR BPR BP -> [BPR]BPR0 =[SOI]BPR (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CPY CPY Company -> [CPY]CPY0 =[SOI]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[SOI]CUR (TABCUR) !Block
  DUDDAT D Due date
  DUDNBR C*4 Number of due dates
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[SOI]FCY (FACILITY) !Block
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGFWD M*4 To carry forward [menu 1: 1=No,2=Yes]
  FLGFWDSOI M*4 Statement carryfwd. [menu 1: 1=No,2=Yes]
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  FLGPST M*4 Posted [menu 1: 1=No,2=Yes]
  FWDSOI VCR Carry-foward stmnt.
  NUMSOI VCR Document no.
  OD M*4 Generate MO [menu 1: 1=No,2=Yes]
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  SAC SAC Control
  SOICOD A*3 Statement code
  SOIDAT D Statement date
  SOINUM VCR Statement number
  TPYPAYCUR MD1 Paid
  TYPSOI GTE Entry type -> [GTE]GTE0 =TYPSOI;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## SWIEZAG (SWIEZ) - Temporary table
Notes: activity code KSW
Keys (first = PK; D = duplicates allowed): SWIEZ0 DAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWIEZ]CREUSR (AUTILIS) !Other
  DAT D Date
  SEQNUM L*2 Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWIEZ]UPDUSR (AUTILIS) !Other

## SWIIMPBVR (SWIIMP) - Import Swiss ISR file
Notes: activity code KSW
Keys (first = PK; D = duplicates allowed): SWIIMP0 NUMIMP+LINE
Fields:
  AMOUNT DCB*9.2 Line amount
  AUUID AUUID Single identifier
  BALINV DCB*9.2 Balance
  BAN BAN Bank -> [BAN]BAN0 =[SWIIMP]BAN (BANK) !Block
  BPR BPR Business partner -> [BPR]BPR0 =[SWIIMP]BPR (BPARTNER) !Block
  CODREJ L*1 Rejection code
  CODTRS A*2 Transaction
  COST DCB*9.2 Cost
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWIIMP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SWIIMP]CUR (TABCUR) !Block
  DATCRE D Creation date
  DATDEP D Assignment date
  DATIMP D Import date
  DATPOST D Posting date
  DATTRT D Process date
  DELTA DCB*9.2 Balance
  DEP DEP Discount
  DEPAMT DCB*9.2 Discount amount
  DEPRAT RAT Discount rate
  DUDLIN C*2 Due date number
  DUDNUM L*8 Internal number
  FCY FCY Site -> [FCY]FCY0 =[SWIIMP]FCY (FACILITY) !Block
  IMPORT M*4 Import [menu 1: 1=No,2=Yes]
  INVNUM SIH Invoice no. -> [SIV]SIV0 =[SWIIMP]INVNUM (SINVOICEV) !Block
  LINE L*8 Line
  NUMBPC A*9 Customer no.
  NUMIMP A*15 Import count
  NUMINV A*15 Invoice no.
  NUMMICRO L*8 Microfilm no.
  NUMREF A*27 Reference number
  OK C*1 OK
  PAM ADI Payment method -> [ADI]CODE =3;PAM (ATABDIV) !Block
  REFDEP A*10 Reference
  REFINST A*35 Customer
  SAC SAC Control account
  SRC A*1 Source
  TYPCUR A*3 Currency type
  TYPDIS A*1 Discount type
  TYPTRS A*3 Transaction type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWIIMP]UPDUSR (AUTILIS) !Other

## SWIIMPTMP (SWITMP) - Import Swiss ISR file (temp.)
Notes: activity code KSW
Keys (first = PK; D = duplicates allowed): SWITMP0 NUMIMP+LINE; SWITMP1 NUMIMP+CUR+NUMMICRO (D)
Fields:
  AMOUNT DCB*9.2 Line amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[SWITMP]BAN (BANK) !Block
  BPR BPR Business partner -> [BPR]BPR0 =[SWITMP]BPR (BPARTNER) !Block
  CODREJ L*1 Rejection code
  CODTRS A*2 Transaction
  COST DCB*9.2 Cost
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWITMP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SWITMP]CUR (TABCUR) !Block
  DATCRE D Creation date
  DATDEP D Assignment date
  DATIMP D Import date
  DATPOST D Posting date
  DATTRT D Process date
  DEPRAT RAT Discount rate
  FCY FCY Site -> [FCY]FCY0 =[SWITMP]FCY (FACILITY) !Block
  IMPORT M*4 Import [menu 1: 1=No,2=Yes]
  LINE L*8 Line
  NUMBPC A*9 Customer no.
  NUMIMP A*15 Import count
  NUMINV A*15 Invoice no.
  NUMMICRO L*8 Microfilm no.
  NUMREF A*27 Reference number
  REFDEP A*10 Reference
  REFINST A*35 Customer
  SAC SAC Control account
  SRC A*1 Source
  TYPCUR A*3 Currency type
  TYPDIS A*1 Discount type
  TYPTRS A*3 Transaction type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWITMP]UPDUSR (AUTILIS) !Other

## SWIQRC (SWIQRC) - Swiss QR-data
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SWIQRC0 NUM+ORIMOD; SWIQRC1 REF+ORIMOD (D)
Fields:
  ALTPAR1 A*100 Parameter
  ALTPAR2 A*100 Parameter
  AMT A*12 Payment amount
  AUUID AUUID Single identifier
  CDTRADRLIN1 A*70 Address
  CDTRADRLIN2 A*70 Address
  CDTRADRTP A*1 Address type
  CDTRBLDGNBR A*70 House no.
  CDTRCRY A*2 Country
  CDTRCTY A*35 City
  CDTRNAM A*70 Name
  CDTRPSTCOD A*16 Postal code
  CDTRSTRNAM A*70 Street
  CHRCODTYP A*1 Type
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWIQRC]CREUSR (AUTILIS) !Other
  CUR A*3 Currency
  IBACOD A*21 IBAN code
  IMGQRC ABB QR image
  NUM VCR Document no.
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  PAYREFTYP A*4 Type of payment reference
  QRCODTYP A*3
  REF A*27 Reference
  STAQRC M*4 QR image status [menu 1: 1=No,2=Yes]
  STRDBKGINF A*140 Invoice information
  TRAILER A*3 Unique code
  UCDTADRTP A*1 Address type
  UCDTRADRLIN1 A*70 Address
  UCDTRADRLIN2 A*70 Address
  UCDTRBLDGNBR A*70 House no.
  UCDTRCRY A*2 Country
  UCDTRCTY A*35 City
  UCDTRNAM A*70 Name
  UCDTRPSTCOD A*16 Postal code
  UCDTRSTRNAM A*70 Street
  UDBTADRTP A*1 Address type
  UDBTRADRLIN1 A*70 Address
  UDBTRADRLIN2 A*70 Address
  UDBTRBLDGNBR A*70 House no.
  UDBTRCRY A*2 Country
  UDBTRCTY A*35 City
  UDBTRNAM A*70 Name
  UDBTRPSTCOD A*16 Postal code
  UDBTRSTRNAM A*70 Street
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWIQRC]UPDUSR (AUTILIS) !Other
  USTREF A*140 Unstructured reference
  VER A*4 Version

## TABCODEDT (TED) - Report code table
Keys (first = PK; D = duplicates allowed): TED0 CODEDT+LEG
Fields:
  AUUID AUUID Single identifier
  CODEDT TED Payment report code -> [TED]TED0 =CODEDT;[V]GSUPCLE (TABCODEDT) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SHOAXX AX1 Short description
  TRT A*20 Processing
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABEXPENS (TES) - Expenses tables
Notes: differs in V9.0 P12 (diff: AT3_TABEXPENS.htm); differs in V10 P1 (diff: ATD_TABEXPENS.htm)
Keys (first = PK; D = duplicates allowed): TES0 CODEXP
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =20;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  ACS ACS Access code -> [ACS]ACS0 =[TES]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCEFLG M*4 Analytical modifications [menu 1: 1=No,2=Yes] act:ANA
  CODEXP TES Expense code -> [TES]TES0 =[TES]CODEXP (TABEXPENS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESEXP DES Description
  DESFLG M*4 Comment [menu 1: 1=No,2=Yes]
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Analytical dimension type -> [DIE]DIE0 =[TES]DIE (GDIE) !Block act:ANA
  GFY AGF Group -> [AGF]AGF0 =[TES]GFY (AGRPFCY) !Block
  INICCE M*4 Initialization [menu 2802: 1=Fixed,2=User] act:ANA
  NBRCCE C*2
  PCCCOD PJCC Cost type -> [PJCC]PCC0 =[TES]PCCCOD (PJMCOSTCTR) !Block act:PJM
  SHOTRA AX1 Short description
  TYPVLT M*15 Valuation type [menu 2803: 1=Fixed value,2=User value,3=Mileage]
  UOM ADI Unit -> [ADI]CODE =10;UOM (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VLTDEFPAR ADP Default value
  VLTDEFUNI DCB*9.2 Default value
  VLTPFDPAR ADP Cap
  VLTPFDUNI DCB*9.2 Cap
  VLYEND D Validity end date
  VLYSTR D Validity start date

## TABFILBAN (TFB) - Bank file definitions
Notes: differs in V10 P1 (diff: ATD_TABFILBAN.htm)
Keys (first = PK; D = duplicates allowed): TFB0 COD+BAN+RECTYP+ORDNUM+LEG+NUM
Fields:
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[TFB]BAN (BANK) !Block
  BANLEG A*25 Bank - Legislation
  CND AFR*250 Line condition
  COD A*10 Bank file
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR(99) Currency -> [TCU]TCU0 =[TFB]CUR (TABCUR) !Block
  CURCTL M*15 Currency [menu 3684: 1=Inactive,2=Authorization,3=Restriction]
  CURMULT M*4 Multicurrency [menu 1: 1=No,2=Yes]
  DES DES Description
  DESLIN DES Title
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENDSEP A*250 End separator
  EXPNUM L*8 Export number
  FILEXO A*4 File extension
  FILREF A*2 File extension
  FLDTYP M*15 Field type [menu 681: 1=Alphanumeric,2=Numeric,3=Date (DDMMYY),4=Date (YYMMDD),5=Year,6=Month,7=Day,8=Binary,9=Cent amount]
  FMT M*15 Format [menu 3627: 1=Fixed,2=Variable]
  FORCND AFR*40 Condition
  FRM AFR*250 Formula
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LNG C*3 Length
  NATPAY M*5 File family [menu 2604: 1=None,2=LCR,3=PRE,4=VIR,5=SCT,6=SDD]
  NUM C*2 Order no.
  OBY M*4 Mandatory [menu 1: 1=No,2=Yes]
  ORDNUM C*3 Order
  RECTYP M*15 Record type [menu 656: 1=Header,2=Detail,3=Total,4=Subtotal,5=Detail 2]
  SHOTRA AX1 Short description
  STRSEP A*250 Start separator
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABPAYTYP (TPY) - Payment transactions
Notes: differs in V9.0 P12 (diff: AT3_TABPAYTYP.htm)
Keys (first = PK; D = duplicates allowed): TPY0 PAYTYP+LEG
Fields:
  ACETYP91 M*15 Payment grouping [menu 657: 1=Payment,2=Deposit slip/Paying bank,3=Due date]
  ACETYP92 M*15 Discount grouping [menu 657: 1=Payment,2=Deposit slip/Paying bank,3=Due date]
  ACS ACS Access code -> [ACS]ACS0 =[TPY]ACS (ACCCOD) !Block
  AUTACE10 GRA Group entry -> [GRA]GRA0 =[TPY]AUTACE10 (GRPAUTACE) !Block
  AUTACE3 GRA Group entries -> [GRA]GRA0 =AUTACE3 (GRPAUTACE) !Block
  AUTACE8 GRA Group entries -> [GRA]GRA0 =AUTACE8 (GRPAUTACE) !Block
  AUTACE9 GRA Group entries -> [GRA]GRA0 =AUTACE9 (GRPAUTACE) !Block
  AUUID AUUID Single identifier
  BANCSH M*15 Bank or cash [menu 653: 1=Bank,2=Cash]
  BPRTYP M*15 Business partner [menu 644: 1=Customer,2=Supplier] act:KPO
  CIB ADI Interbank code -> [ADI]CODE =306;CIB (ATABDIV) !Block
  CODEDT TED Payment report code -> [TED]TED0 =CODEDT;[V]GSUPCLE (TABCODEDT) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSHVATRGM M*4 Cash VAT [menu 1: 1=No,2=Yes] act:KPO
  DACADD M*4 Address [menu 1: 1=No,2=Yes]
  DACAMTBAN M*4 Bank amount [menu 1: 1=No,2=Yes]
  DACBAN M*4 Bank [menu 1: 1=No,2=Yes]
  DACBANDAT M*4 Bank date [menu 1: 1=No,2=Yes]
  DACBID M*4 Bank account number [menu 1: 1=No,2=Yes]
  DACBILDAT M*4 Date created [menu 1: 1=No,2=Yes]
  DACBPRREF M*4 Drawee reference [menu 1: 1=No,2=Yes]
  DACCHQBAN M*4 Pay-by branch [menu 1: 1=No,2=Yes]
  DACCHQNUM M*4 Check number [menu 1: 1=No,2=Yes]
  DACCHQTYP M*4 Check type [menu 1: 1=No,2=Yes]
  DACCPY M*4 Company [menu 1: 1=No,2=Yes]
  DACCRDAUZ M*4 Credit card authorized [menu 1: 1=No,2=Yes]
  DACCRDNUM M*4 Bank card number [menu 1: 1=No,2=Yes]
  DACDES M*4 Header description [menu 1: 1=No,2=Yes]
  DACDESLIN M*4 Line description [menu 1: 1=No,2=Yes]
  DACDUDDAT M*4 Due date [menu 1: 1=No,2=Yes]
  DACFRMREF M*4 Remittance reference [menu 1: 1=No,2=Yes]
  DACFRMTYP M*4 Discount type [menu 1: 1=No,2=Yes]
  DACORIDAT M*4 Source date [menu 1: 1=No,2=Yes]
  DACPAB1 M*4 Paying bank 1 [menu 1: 1=No,2=Yes]
  DACPAB2 M*4 Paying bank 2 [menu 1: 1=No,2=Yes]
  DACPAM M*4 Payment method [menu 1: 1=No,2=Yes]
  DACPURTYP M*4 Purchase type [menu 1: 1=No,2=Yes]
  DACPYL M*4 Entry batch [menu 1: 1=No,2=Yes]
  DACREF M*4 Reference [menu 1: 1=No,2=Yes]
  DACSUP M*4(30) Extra field 1 [menu 1: 1=No,2=Yes]
  DACVALDAT M*4 Value date [menu 1: 1=No,2=Yes]
  DENDEF CDA Default payment attribute -> [CDA]CDA0 =DENDEF;[V]GSUPCLE (GACCDENCOD) !Block
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DUDFLG M*4 Due date [menu 1: 1=No,2=Yes]
  EDTFLG M*4 Edit flag [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EPACDTTRF M*4 SEPA generation [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FICCAS ADI File grouping code -> [ADI]CODE =325;FICCAS (ATABDIV) !Block act:CASIN
  FILREF6 A*10 File reference
  FILREF71 A*10 File reference
  FILREF72 A*10 File reference
  FILREF8 A*10 File reference
  FLGCAS M*15 Triggering event [menu 2673: 1=None,2=Notes payable/receivable posting,3=Intermediate posting,4=Bank posting] act:CASIN
  FLGEND C*4 Endorsement flag act:KAG
  GFY AGF Group -> [AGF]AGF0 =[TPY]GFY (AGRPFCY) !Block
  JOU10 M*15 Journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  JOU3 M*15 Journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  JOU8 M*15 Cash journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  JOU82 M*15 Discount journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  JOU9 M*15 Journal type [menu 660: 1=Bank,2=Check to cash,3=Notes payable to receive,4=Drafts payable on purchases,5=Drafts payable on fixed assets,6=Remittance for collection,7=Remittance for discount,8=Notes P/R risk closing,9=None]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LOTPROBALCTL M*4 Balance control [menu 1: 1=No,2=Yes]
  NATPAY M*5 File family [menu 2604: 1=None,2=LCR,3=PRE,4=VIR,5=SCT,6=SDD]
  NBRCOL C*2 No. of fixed columns
  NBRPAM C*2 Number of payment methods
  NBRSUP C*2 No.
  PAM TAM(10) Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAYPPS M*4 Auto proposal [menu 1: 1=No,2=Yes]
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;LEG (TABPAYTYP) !Delete
  RATINV M*4 Invoices rate [menu 1: 1=No,2=Yes]
  RATTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  SHOTRA AX1 Short description
  SNS M*15 Sign [menu 661: 1=Expense,2=Revenue,3=Unspecified]
  SPACSH M*4 Cash payment [menu 1: 1=No,2=Yes] act:KSP
  STA2 M*4 Acceptance return [menu 1: 1=No,2=Yes]
  STA3 M*4 Notes P/R posting [menu 1: 1=No,2=Yes]
  STA4 M*4 Bank allocation [menu 1: 1=No,2=Yes]
  STA5 M*4 Remittances [menu 1: 1=No,2=Yes]
  STA6 M*4 Electronic file [menu 1: 1=No,2=Yes]
  STA7 M*4 Paying banks [menu 1: 1=No,2=Yes]
  STA8 M*4 Intermediate posting [menu 1: 1=No,2=Yes]
  STA9 M*4 Bank posting [menu 1: 1=No,2=Yes]
  SWIPAYTYP M*15 Swiss payment type [menu 3662: 1=Normal,2=DTA,3=EZAG,4=ISO] act:KSW
  UPDBIL M*15 Portfolio update [menu 680: 1=No,2=Notes P/R 1,3=Notes P/R 2,4=Notes P/R 3]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  ZONSUP A*10(30) Extra field 2

## TMPARPT (TARPT) - Temporary print key table
Notes: differs in V9.0 P12 (diff: AT3_TMPARPT.htm); differs in V10 P1 (diff: ATD_TMPARPT.htm)
Keys (first = PK; D = duplicates allowed): TARPT0 NUMREQ+USR+RPTCOD+VCRNUM
Fields:
  AMTATIL MD1 Invoice amt. + tax (co)
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TARPT]CREUSR (AUTILIS) !Other
  NUMREQ L*8 Query no.
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
  RPTCOD ARP Report code -> [ARP]ARP0 =[TARPT]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TARPT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TARPT]USR (AUTILIS) !Other
  VCRNUM VCR Document no.
  WITHOLTAX DCB*13.4 Withholding tax

## TMPARPTDET (TARPTD) - Temporary print key table
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): TSRPTD0 NUMREQ+USR+RPTCOD+VCRNUM+LIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TARPTD]CREUSR (AUTILIS) !Other
  LIN L*8 Line no.
  NUMREQ L*8 Query no.
  RPTCOD ARP Report code -> [ARP]ARP0 =[TARPTD]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TARPTD]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TARPTD]USR (AUTILIS) !Other
  VATEXEREA A*100 VAT exemption reasons
  VCRNUM VCR Document no.

## TMPCNSBAN (TCB) - Bank inquiry
Keys (first = PK; D = duplicates allowed): TCB0 TCBNUM; TCB1 USRCRE+ADXNUM (D); TCB2 ACCNUM (D); TCB3 NUMPAY+USRCRE+ADXNUM (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM UNQ Unique number
  ADXNUM L*8 No.
  AMTBAN MD1 Bank amount
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BANDAT D Bank date act:KIT
  BID BID Bank account number
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[TCB]BIDCRY (TABCOUNTRY) !Block
  BILDAT D Date created
  BOLLATO VCR Bollato sequence number act:KIT
  BPR BPR BP -> [BPR]BPR0 =[TCB]BPR (BPARTNER) !Block
  BPRDATVCR D Document date
  BPRREF A*10 Drawee reference
  BPRSAC SAC Control
  BPRVCR A*20 Source document
  CHQNUM A*15 Check number
  COLOR C*1 Color
  CRDNUM A*16 Bank card number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCB]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TCB]CUR (TABCUR) !Block
  DES DES Description
  DUDDAT D Due date
  ENTDAT D Entry date
  FCY FCY Site -> [FCY]FCY0 =[TCB]FCY (FACILITY) !Block
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  NUM VCR Order no.
  NUMPAY VCR Payment no.
  ORIDAT D Source date
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAYLOT VCR Batch code
  PAYTYP TPY Transaction -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  RATCUR RCU Currency rate
  RATDAT D Rate date
  RATRPT RCU Reporting rate
  REF REF Reference
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  STA M*30 Status [menu 689: 1=Entered,2=Accepted,3=In draft management,4=Stage 4,5=Slip entered,6=Slip on file,7=Paying bank entered,8=On intermediate account,9=In the bank,10=Stage 10,11=Unpaid]
  TCBNUM L*8 Internal number
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCB]UPDUSR (AUTILIS) !Other
  USRCRE AUS User -> [AUS]CODUSR =[TCB]USRCRE (AUTILIS) !Block
  VALDAT D Value date

## TMPCSRQ (TCR) - Temporary cash requirements
Keys (first = PK; D = duplicates allowed): TCR0 CREUSR+BPR+FCY+TYP+NUM+DUDDAT+DUDLIG
Fields:
  ACCDAT D Accounting date
  AMT MD1 Invoice amount
  AMTDIS MD1 Discountable amount
  AUUID AUUID Single identifier
  BPR BPR Bill-to BP -> [BPR]BPR0 =[TCR]BPR (BPARTNER) !RTZ
  BPRDAT D Source date
  BPRNAM NAM(2) Name
  CPY CPY Company -> [CPY]CPY0 =[TCR]CPY (COMPANY) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCR]CREUSR (AUTILIS) !Other
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =[TCR]DEP (TABDEPAGIO) !RTZ
  DEPDES DES Description
  DISAMT MD1 Discount amount
  DISDAT D Discount
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  FCY FCY Geographical area -> [FCY]FCY0 =[TCR]FCY (FACILITY) !RTZ
  NETAMT MD1 Net amount
  NUM VCR Document no.
  PROCESS A*10 Process
  TYP A*5 Entry type
  UID L*8 Process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCR]UPDUSR (AUTILIS) !Other

## TMPEXPENSE (EXT) - Temporary table - Expenses
Keys (first = PK; D = duplicates allowed): EXT0 CPY+CUR+BPRGTETYP+FCY+SEP+DATEXS (D); EXT1 ACCNUM
Fields:
  ACCNUM UNQ Internal number
  AMTATI MD2 Amount + tax
  AMTCUR MD2 Amount in currency
  AMTPAY MD2 Actual amt.
  AMTTAX1 MD2 Tax amount
  AMTTAX2 MD2 Tax amount
  AMTVAT MD2 Tax amount
  AUUID AUUID Single identifier
  BPRGTETYP GTE Entry type -> [GTE]GTE0 =BPRGTETYP;[V]GSUPCLE (GTYPACCENT) !Delete
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CLB AUS Employee -> [AUS]CODUSR =[EXT]CLB (AUTILIS) !Delete
  CODEXP TES Expense codes -> [TES]TES0 =[EXT]CODEXP (TABEXPENS) !Delete
  CPY CPY Company -> [CPY]CPY0 =[EXT]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[EXT]CUR (TABCUR) !Delete
  DATEXS D Date
  DEDTAX1 MD2 Deductible tax
  DEDTAX2 MD2 Deductible tax
  DEDVAT MD2 Input VAT
  DES A*250 Comments
  DIE DIE Analytical dimension type -> [DIE]DIE0 =[EXT]DIE (GDIE) !Block act:ANA
  EXPBPR BPR Miscellaneous BP -> [BPR]BPR0 =[EXT]EXPBPR (BPARTNER) !Delete
  FCY FCY Site -> [FCY]FCY0 =[EXT]FCY (FACILITY) !Delete
  NBREXS C*2 Line no.
  QTY L*6 Quantity
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  SEP A*30 Separator
  STA M*15 Status [menu 2806: 1=Not posted,2=Posted simulation,3=Posted actual]
  TAX1 VAT Tax 1 -> [TVT]TVT0 =TAX1;[V]GSUPCLE (TABVAT) !Block
  TAX2 VAT Tax 2 -> [TVT]TVT0 =TAX2;[V]GSUPCLE (TABVAT) !Block
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax 3 -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VCRNUM VCR Entry
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block
  VISA AUS -> [AUS]CODUSR =[EXT]VISA (AUTILIS) !Block

## TMPFUP0 (TF0) - Campaign criteria
Notes: activity code FUP
Keys (first = PK; D = duplicates allowed): TFP0 QURNUM; TFP1 CREDAT+QURNUM
Fields:
  ACCLI M*4 Customer prepayments [menu 1: 1=No,2=Yes]
  AGIO M*4 Late charge calculation [menu 1: 1=No,2=Yes]
  ALLBPC M*4 All customers [menu 1: 1=No,2=Yes]
  ALLBPCGRU M*4 All group customers [menu 1: 1=No,2=Yes]
  ALLBPCRSK M*4 All risk customers [menu 1: 1=No,2=Yes]
  ALLCLS M*4 All classes [menu 1: 1=No,2=Yes]
  ALLFCY M*4 All sites [menu 1: 1=No,2=Yes]
  ALLFGP M*4 All reminder groups [menu 1: 1=No,2=Yes]
  ALLPAM M*4 All payment methods [menu 1: 1=No,2=Yes]
  ALLREP M*4 All sales reps. [menu 1: 1=No,2=Yes] act:REC
  ALLREP1 M*4 All representatives 1 [menu 1: 1=No,2=Yes]
  ALLREP2 M*4 All representatives 2 [menu 1: 1=No,2=Yes]
  ALLSAC M*4 All control accounts [menu 1: 1=No,2=Yes]
  ALLTSCCOD M*4 All stat groups [menu 1: 1=No,2=Yes]
  ALLUSR M*4 All users [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPCDEB BPR From customer -> [BPR]BPR0 =[TF0]BPCDEB (BPARTNER) !Block
  BPCFIN BPR To customer -> [BPR]BPR0 =[TF0]BPCFIN (BPARTNER) !Block
  BPCGRU BPR Group customer -> [BPR]BPR0 =[TF0]BPCGRU (BPARTNER) !Block
  BPCRSKEND BPR Risk BP -> [BPR]BPR0 =[TF0]BPCRSKEND (BPARTNER) !Block
  BPCRSKSTR BPR Risk BP -> [BPR]BPR0 =[TF0]BPCRSKSTR (BPARTNER) !Block
  BPRFUP M*15 Reminded BP [menu 672: 1=Pay-by BP,2=Bill-to BP]
  CLS M*15 Class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  CMT A*250 Comment
  COA COA Chart of accounts -> [COA]COA0 =[TF0]COA (GCOA) !Block
  CPY AGC Company -> [AGF]AGF0 =[TF0]CPY (AGRPFCY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TF0]CREUSR (AUTILIS) !Other
  CRI AFR*250 Criteria
  ECRAN GFP Screen -> [GFP]GFP0 =[TF0]ECRAN (GFUPSCR) !Block
  FCY FCY Site -> [FCY]FCY0 =[TF0]FCY (FACILITY) !Block
  FGP FGP Reminder group -> [FGP]FGP0 =[TF0]FGP (FUPGRP) !Block act:FUP
  FLGFUP M*4 [menu 1: 1=No,2=Yes]
  FUPLEVEND C*4 Level of reminder
  FUPLEVSTR C*4 Level of reminder
  GRPSAC GSC Control group -> [GSC]GSC0 =COA;GRPSAC;1 (GRPSAC) !Block
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  QURNUM FUP Campaign number -> [TF0]TFP0 =[TF0]QURNUM (TMPFUP0) !BSRA
  REFDAT D Reference date
  REPDEB REP From sales rep -> [REP]REP0 =[TF0]REPDEB (SALESREP) !Block act:REC
  REPDEB1 REP From sales rep -> [REP]REP0 =[TF0]REPDEB1 (SALESREP) !Block
  REPDEB2 REP From sales rep -> [REP]REP0 =[TF0]REPDEB2 (SALESREP) !Block
  REPFIN REP To sales rep -> [REP]REP0 =[TF0]REPFIN (SALESREP) !Block act:REC
  REPFIN1 REP To sales rep -> [REP]REP0 =[TF0]REPFIN1 (SALESREP) !Block
  REPFIN2 REP To sales rep -> [REP]REP0 =[TF0]REPFIN2 (SALESREP) !Block
  SAC SAC Control
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TF0]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[TF0]USR (AUTILIS) !Delete
  VALIDE M*4 Validated campaign [menu 1: 1=No,2=Yes]

## TMPFUP1 (TF1) - BPs for reminding
Notes: activity code FUP; differs in V9.0 P12 (diff: AT3_TMPFUP1.htm); differs in V10 P1 (diff: ATD_TMPFUP1.htm)
Keys (first = PK; D = duplicates allowed): TFP1 NUMREQ+BPC+CPY+FCY; TFP2 BPC (D); TFP3 CPY (D)
Fields:
  AUUID AUUID Single identifier
  BPC BPR Bill-to/Order BP -> [BPR]BPR0 =[TF1]BPC (BPARTNER) !Block
  CMT AC0*1 Comment
  CPY CPY Company -> [CPY]CPY0 =[TF1]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TF1]CREUSR (AUTILIS) !Block
  FCY FCY Site -> [FCY]FCY0 =[TF1]FCY (FACILITY) !Block
  FUPTOTAMT MD1 Amount for reminding
  NUMREQ FUP Campaign number -> [TF0]TFP0 =NUMREQ (TMPFUP0) !Delete
  SEL M*1 [menu 2638: 1=None,2=Partial,3=Total]
  TYPBLB AT Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TF1]UPDUSR (AUTILIS) !Block

## TMPFUP2 (TF2) - Open items to remind
Notes: activity code FUP; differs in V9.0 P12 (diff: AT3_TMPFUP2.htm); differs in V10 P1 (diff: ATD_TMPFUP2.htm)
Keys (first = PK; D = duplicates allowed): TFP1 NUMREQ+NUMDUD; TFP2 NUMDUD (D); TFP3 BPC (D); TFP4 BPC+FUPMOD (D); TFP5 NUMREQ+FCY (D); TFP6 NUMREQ+LEVFUP (D)
Fields:
  ADD ADR Address code
  AMTDEP MD1 Discount amount
  AMTDEPCUR MD1 Discount amount
  AUUID AUUID Single identifier
  BPC BPR BP -> [BPR]BPR0 =[TF2]BPC (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[TF2]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TF2]CREUSR (AUTILIS) !Other
  DEP TDA Early discount/Late charge -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DEPRAT RAT Late charge rates
  DPTCOD ADI Dispute code -> [ADI]CODE =315;DPTCOD (ATABDIV) !Block
  FCY FCY Site -> [FCY]FCY0 =[TF2]FCY (FACILITY) !Block
  FUPMOD M*15 Reminder method [menu 2629: 1=Letter,2=Email,3=Telephone,4=Fax]
  GRPCRI A*30 Grouping
  LEVFUP C*2 Reminder level
  NUMDUD A*15 Due date number
  NUMREQ FUP Campaign number -> [TF0]TFP0 =NUMREQ (TMPFUP0) !Delete
  SEL M*4 Selection [menu 1: 1=No,2=Yes]
  TYPTXT M*15 Text type [menu 2654: 1=By invoice,2=Global,3=By mail]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TF2]UPDUSR (AUTILIS) !Other

## TMPFUPCMT (TCF) - Open item comments
Notes: activity code FUP
Keys (first = PK; D = duplicates allowed): TCF0 NUMDUD
Fields:
  AUUID AUUID Single identifier
  CMT AC0*1 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCF]CREUSR (AUTILIS) !Other
  NUMDUD A*15 Due date number
  TYPBLB AT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCF]UPDUSR (AUTILIS) !Other

## TMPPAYDUD (TPD) - Temporary payment proposal
Notes: differs in V9.0 P12 (diff: AT3_TMPPAYDUD.htm); differs in V10 P1 (diff: ATD_TMPPAYDUD.htm)
Keys (first = PK; D = duplicates allowed): TPD0 CPY+PAYTYP+GRPCRI+FLG (D); TPD1 ACCNUM+DUDLIG; TPD2 AMTLOC (D); TPD3 DUDDAT (D)
Fields:
  ACCNUM UNQ Internal number
  AMTCUR MD1 Amount in currency
  AMTDEP MD1 Discount amount
  AMTLOC MD1 Ledger amount
  AUUID AUUID Single identifier
  BID BID Bank account number
  BIDCRY CRY Bank acct. country -> [TCY]TCY0 =[TPD]BIDCRY (TABCOUNTRY) !Delete
  BPR BPR BP -> [BPR]BPR0 =[TPD]BPR (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[TPD]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPD]CREUSR (AUTILIS) !Other
  DEPLTI L*8 Leadtime for discount
  DEPRAT RAT Bank discount / charge rate
  DISDAT D Discount date
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  EARDISFLG M*4 Settlement discount [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[TPD]FCY (FACILITY) !Delete
  FLG C*1 Flag
  FLGCRE C*1 Creation flag
  GRPCRI A*100 Grouping criterion (pmsim)
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Other
  RITAMT MD1 Retained amount act:KIT
  RITCUR MD1 Retained amount act:KIT
  RITLOC MD1 Retained amount act:KIT
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPD]UPDUSR (AUTILIS) !Other

## TMPPAYDUD2 (TP2) - Temporary payment proposal
Keys (first = PK; D = duplicates allowed): TP20 CPY+PAYTYP+GRPCRI+FLG+UIDUSR; TP21 AMTLOC (D)
Fields:
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[TP2]BPR (BPARTNER) !Delete
  BPRNAM NAM Company name
  CPY CPY Company -> [CPY]CPY0 =[TP2]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TP2]CREUSR (AUTILIS) !Other
  DISDAT D Discount date
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[TP2]FCY (FACILITY) !Delete
  FLG C*1 Flag
  FLGCRE C*1 Creation flag
  GRPCRI A*100 Grouping criterion (pmsim)
  NBR C*4 Number of lines
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Other
  UIDUSR L*8 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TP2]UPDUSR (AUTILIS) !Other

## TMPPAYTOT (PYT) - Temporary payment proposal
Keys (first = PK; D = duplicates allowed): PYT0 TRC+PAYTYP+FCY+CUR+BAN+DUDDAT+SNS
Fields:
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Ledger amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[PYT]BAN (BANK) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PYT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PYT]CUR (TABCUR) !Block
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[PYT]FCY (FACILITY) !Block
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Other
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  TRC A*20 Log
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PYT]UPDUSR (AUTILIS) !Other

## TYPCOMBEL (TYC) - Communication types
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): TYC0 COD+NUM
Fields:
  AUUID AUUID Single identifier
  COD TYC Type -> [TYC]TYC0 =COD;NUM (TYPCOMBEL) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESLIN DES Title
  DESSHO SHO Short description
  EXPNUM L*8 Export number
  FRM AFR*250 Formula
  LNG C*3 Length
  NUM C*2 Order no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## UNPAID (UNP) - Doubtful receipt entry
Keys (first = PK; D = duplicates allowed): UNP0 NUM+CUR
Fields:
  ACC GAC(10) Account -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  ACCBPR GAC(10) BP account -> [GAC]GAC0 =COA(indice);ACCBPR(indice) (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ(50) Internal number
  ACCSTA C*2 Function
  AMTACC MD1 Amount + tax
  AMTACCNUM MD1(50) Amount
  AMTBPR MD1 Amount - tax
  AMTCRG MD1 Line charge amount
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BAN BAN Code -> [BAN]BAN0 =[UNP]BAN (BANK) !Block
  BPR BPR BP -> [BPR]BPR0 =[UNP]BPR (BPARTNER) !Block
  BPRBAN BPR BP -> [BPR]BPR0 =[UNP]BPRBAN (BPARTNER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[UNP]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[UNP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[UNP]CUR (TABCUR) !Block
  DES DES Entry description
  DESVCR DES Entry description
  DIE DIE Dimension type code -> [DIE]DIE0 =[UNP]DIE (GDIE) !Block act:ANA
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[UNP]FCY (FACILITY) !Block
  FLGACT M*4 Debit note [menu 1: 1=No,2=Yes]
  FLGCRG M*4 Expenses on separate journal [menu 1: 1=No,2=Yes]
  GRP A*16 Group
  IPT M*4 Allocation [menu 1: 1=No,2=Yes]
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  NUM VCR Payment no.
  RENNOTPAY ADI Late payment reason -> [ADI]CODE =310;RENNOTPAY (ATABDIV) !Block
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TYPVCR A*1 Reference
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[UNP]UPDUSR (AUTILIS) !Other

## VATLINITMGER (VLI) - German VAT line items
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): VLI0 REFNO+IDUSER (D)
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTLOC MD2 Local currency amt
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[VLI]BPR (BPARTNER) !Block
  CEEFLG M*4 EU invoice [menu 1: 1=No,2=Yes]
  COA COA Chart code -> [COA]COA0 =[VLI]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VLI]CREUSR (AUTILIS) !Other
  DATSTR D Valid from
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  IDUSER A*30 User identity+ adxuid
  IVNUM VCR Entry
  OFFACC A*15 Offset
  REFNO A*10 Report line
  SNS A*5 Sign
  TAXNO VAT Tax -> [TVT]TVT0 =TAXNO;[V]GSUPCLE (TABVAT) !Block
  TYP GTE Document type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VLI]UPDUSR (AUTILIS) !Other
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VATRAT DCB*3.2 Rate

