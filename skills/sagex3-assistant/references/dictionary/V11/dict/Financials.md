<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Financials module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BALAGEEOY (BGY) - EOFY aged overdue invoice list
Notes: not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BGY0 USR+NUMREQ+CPY+CODBLK+BPR+ACCDAT+DUDDAT+TYP+NUM+DUDLIG
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCDAT D Accounting date
  AMTNOT MD1 Remaining ex-tax amt.
  AMTNOTDUD MD1 Amount - tax
  AMTNOTDUD1 MD1 Open item amount 1
  AMTNOTDUD2 MD1 Open item amount 2
  AMTNOTDUD3 MD1 Open item amount 3
  AMTNOTDUD4 MD1 Open item amount 4
  AMTNOTDUD5 MD1 Open item amount 5
  AMTNOTDUDEXD MD1 Excluded OI amt.
  AMTNOTDUDTOT MD1 Total amount
  AMTNOTINV MD1 Turnover
  AMTTAX MD1 Remaining tax amt.
  AMTTAXDUD MD1 Tax amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BGY]BPR (BPARTNER) !Delete
  COA COA Chart code -> [COA]COA0 =[BGY]COA (GCOA) !Delete
  CODBLK L*8 Block
  CPY CPY Company -> [CPY]CPY0 =[BGY]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BGY]CREUSR (AUTILIS) !Delete
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BGY]CURLED (TABCUR) !Delete
  DUDDAT D Due date
  DUDLIG C*3 Due date number
  FCY FCY Site -> [FCY]FCY0 =[BGY]FCY (FACILITY) !Delete
  FLGTOTPURSAL M*4 Total flag [menu 1: 1=No,2=Yes]
  NBRDAYWAI L*8 Late
  NBRDUD1 L*8 Open item number 1
  NBRDUD2 L*8 Open item number 2
  NBRDUDEXD L*8 Excluded OI no.
  NUM VCR Document no.
  NUMREQ L*8 Query no.
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BGY]UPDUSR (AUTILIS) !Delete
  USR AUS Operator -> [AUS]CODUSR =[BGY]USR (AUTILIS) !Delete

## BALANA (BLA) - Analytical balance
Keys (first = PK; D = duplicates allowed): BLA0 LEDTYP+CPY+FCY+FIY+ACC+BPR+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+CUR; BLA1 ACCNUM; BLA2 LEDTYP+CPY+CUR+FCY+ACC+BPR+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+FIY; BLA3 LEDTYP+CUR+FCY+FIY+ACC+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+BPR+CPY
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BLA]BPR (BPARTNER) !Block
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Block
  CDT MD1 Credit act:PER
  CDTLED MD1 Ledger credit act:PER
  COA COA Chart code -> [COA]COA0 =[BLA]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BLA]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BLA]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BLA]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BLA]CURLED (TABCUR) !Block
  DEB MD1 Debit act:PER
  DEBLED MD1 Ledger debit act:PER
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[BLA]DIE (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[BLA]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BLA]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLA]UPDUSR (AUTILIS) !Other

## BALANCE (BAL) - General balance
Keys (first = PK; D = duplicates allowed): BAL0 LEDTYP+CPY+FCY+FIY+ACC+BPR+CUR; BAL1 ACCNUM; BAL2 LEDTYP+CUR+CPY+FCY+ACC+BPR+FIY
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BAL]BPR (BPARTNER) !Block
  CDT MD1 Credit act:PER
  CDTLED MD1 Ledger credit act:PER
  COA COA Chart code -> [COA]COA0 =[BAL]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BAL]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BAL]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BAL]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BAL]CURLED (TABCUR) !Block
  DEB MD1 Debit act:PER
  DEBLED MD1 Ledger debit act:PER
  FCY FCY Site -> [FCY]FCY0 =[BAL]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BAL]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BAL]UPDUSR (AUTILIS) !Other

## BALCONSO (BLC) - Consolidation trial balance
Notes: activity code CSL1; differs in V9.0 P12 (diff: AT3_BALCONSO.htm); differs in V10 P1 (diff: ATD_BALCONSO.htm)
Keys (first = PK; D = duplicates allowed): BLC0 LEDTYP+GRUGPY+CPYGRU+ACCGRU+BPRGRU+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+CURTRS+CRI
Fields:
  ACCGRU A*15 General account
  ANOUV M*4 Prior balances [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BLC MD1 Accounting balance
  BPRGRU A*15 Partner company
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Block
  CDTCNS MD1 Credit
  CDTTRS MD1 Credit
  CPYGRU A*10 Company
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CRI A*30 Criteria
  CURCNS CUR Currency -> [TCU]TCU0 =[BLC]CURCNS (TABCUR) !Block
  CURTRS CUR Currency -> [TCU]TCU0 =[BLC]CURTRS (TABCUR) !Block
  DATDEB D Start date
  DATFIN D End date
  DEBCNS MD1 Debit
  DEBTRS MD1 Debit
  DES DES Description
  DIE1 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE1 (GDIE) !Block
  DIE2 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE2 (GDIE) !Block
  DIE3 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE3 (GDIE) !Block
  DIE4 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE4 (GDIE) !Block
  DIE5 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE5 (GDIE) !Block
  DIE6 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE6 (GDIE) !Block
  DIE7 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE7 (GDIE) !Block
  DIE8 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE8 (GDIE) !Block
  DIE9 DIE Dimension type code -> [DIE]DIE0 =[BLC]DIE9 (GDIE) !Block
  GRUGPY AGF Conso. scope -> [AGF]AGF0 =[BLC]GRUGPY (AGRPFCY) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  SNSBLC C*2 Balance sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLC]UPDUSR (AUTILIS) !Other

## BALDEM (BAM) - Double entry balance
Notes: activity code KRU
Keys (first = PK; D = duplicates allowed): BAM0 LEDTYP+CPY+FCY+FIY+DEBACC+DEBBPR+CDTACC+CDTBPR+IDTDEBCCE+IDTCDTCCE+CUR
Fields:
  AMTCUR MD1 Amount in currency act:PER
  AMTLED MD1 Ledger amount act:PER
  AUUID AUUID Single identifier
  CDTACC GAC Credited account -> [GAC]GAC0 =COA;CDTACC (GACCOUNT) !Block
  CDTBPR BPR Credited BP -> [BPR]BPR0 =CDTBPR (BPARTNER) !Block
  CDTCCE CCE(9) Cred. dimensions -> [CCE]CCE0 =CDTDIE(indice);CDTCCE(indice) (CACCE) !Block
  CDTDIE DIE(9) Dimension codes -> [DIE]DIE0 =[BAM]CDTDIE (GDIE) !Block
  COA COA Chart code -> [COA]COA0 =[BAM]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BAM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BAM]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BAM]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BAM]CURLED (TABCUR) !Block
  DEBACC GAC Debited account -> [GAC]GAC0 =COA;DEBACC (GACCOUNT) !Block
  DEBBPR BPR Debited BP -> [BPR]BPR0 =DEBBPR (BPARTNER) !Block
  DEBCCE CCE(9) Deb. dimensions -> [CCE]CCE0 =DEBDIE(indice);DEBCCE(indice) (CACCE) !Block
  DEBDIE DIE(9) Dimension codes -> [DIE]DIE0 =[BAM]DEBDIE (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[BAM]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  IDTCDTCCE UNQ Cred. dimension ID
  IDTDEBCCE UNQ Deb. dimension ID
  LED LED Ledger -> [LED]LED0 =[BAM]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  QTY QTY Quantity act:PER
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BAM]UPDUSR (AUTILIS) !Other

## BALDEMIDT (BAI) - Double entry balance index
Notes: activity code KRU
Keys (first = PK; D = duplicates allowed): BAI0 CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9; BAI1 IDTCCE
Fields:
  AUUID AUUID Single identifier
  CCE1 A*15 Analytical dimension 1
  CCE2 A*15 Analytical dimension 2
  CCE3 A*15 Analytical dimension 3
  CCE4 A*15 Analytical dimension 4
  CCE5 A*15 Analytical dimension 5
  CCE6 A*15 Analytical dimension 6
  CCE7 A*15 Analytical dimension 7
  CCE8 A*15 Analytical dimension 8
  CCE9 A*15 Analytical dimension 9
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BAI]CREUSR (AUTILIS) !Other
  IDTCCE UNQ Dimension ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BAI]UPDUSR (AUTILIS) !Other

## BALPRECSL (BLP) - Pre-consolidation balances
Notes: activity code PRCSL; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BLP0 LEDTYP+CPY+FCY+FIY+ACC+BPR+CSLFLO+CSLBPR+IDTCCE+CUR; BLP1 ACCNUM; BLP2 LEDTYP+CPY+CUR+FCY+ACC+BPR+CSLFLO+CSLBPR+IDTCCE+FIY; BLP3 LEDTYP+CUR+FCY+FIY+ACC+IDTCCE+BPR+CSLFLO+CSLBPR+CPY
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BLP]BPR (BPARTNER) !Block
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Block
  CDT MD1 Credit act:PER
  CDTLED MD1 Ledger credit act:PER
  COA COA Chart code -> [COA]COA0 =[BLP]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BLP]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BLP]CREUSR (AUTILIS) !Other
  CSLBPR BPR Partner -> [BPR]BPR0 =[BLP]CSLBPR (BPARTNER) !Block act:PRCSL
  CSLFLO ADI Flow -> [ADI]CODE =324;CSLFLO (ATABDIV) !Block act:CSL1
  CUR CUR Currency -> [TCU]TCU0 =[BLP]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BLP]CURLED (TABCUR) !Block
  DEB MD1 Debit act:PER
  DEBLED MD1 Ledger debit act:PER
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[BLP]DIE (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[BLP]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  IDTCCE UNQ Dimension ID
  LED LED Ledger -> [LED]LED0 =[BLP]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLP]UPDUSR (AUTILIS) !Other

## BATCH (BTC) - Batch job parameters
Keys (first = PK; D = duplicates allowed): BTC0 COD; BTC1 RQT (D)
Fields:
  ACC M*4 Posting [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BAL M*4 Balance update [menu 1: 1=No,2=Yes]
  COD A*10 Task code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BTC]CREUSR (AUTILIS) !Other
  CRI AFR*250 Criteria
  FLG C*2 Existence flag
  MTC M*4 Matching [menu 1: 1=No,2=Yes]
  PID A*20 Processes
  RQT L*8 Query
  STA C*2 Status
  TIMOUT L*8(4) Time-out
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BTC]UPDUSR (AUTILIS) !Other

## BLACMM (BLM) - Analytical commitment balance
Keys (first = PK; D = duplicates allowed): BLM0 LEDTYP+CPY+FCY+FIY+ACC+BPR+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+CUR; BLM1 ACCNUM
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BLM]BPR (BPARTNER) !Block
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Block
  CMM MD1 Commitments act:PER
  CMMLED MD1 Commitments (ref) act:PER
  CMMPRP MD1 Precommitments act:PER
  CMMPRPLED MD1 Pre-commitments (ref) act:PER
  COA COA Chart code -> [COA]COA0 =[BLM]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BLM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BLM]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BLM]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[BLM]CURLED (TABCUR) !Block
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[BLM]DIE (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[BLM]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BLM]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLM]UPDUSR (AUTILIS) !Other

## BLAQTY (BLQ) - Analytical quantity balance
Keys (first = PK; D = duplicates allowed): BLQ0 LEDTYP+CPY+FCY+FIY+ACC+BPR+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+CUR; BLQ1 ACCNUM; BLQ3 LEDTYP+CUR+FCY+FIY+ACC+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9+BPR+CPY
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BLQ]BPR (BPARTNER) !Block
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Block
  COA COA Chart code -> [COA]COA0 =[BLQ]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BLQ]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BLQ]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BLQ]CUR (TABCUR) !Block
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[BLQ]DIE (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[BLQ]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BLQ]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  QTY QTY Quantity act:PER
  QTYCMM QTY Commitment act:PER
  QTYPRP QTY Precommitment act:PER
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[BLQ]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLQ]UPDUSR (AUTILIS) !Other

## BNKTRSIMP (BTI) - Import transfers from Sage treasury
Notes: activity code CASIN
Keys (first = PK; D = duplicates allowed): TFH0 FICHIER+LIN
Fields:
  ACC GAC General accounts -> [GAC]GAC0 ="";ACC (GACCOUNT) !Other
  ACCDAT D Accounting date
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Local currency amount
  AUUID AUUID Single identifier
  CODCPY CPY Company -> [CPY]CPY0 =[BTI]CODCPY (COMPANY) !Block
  CODSUP A*30 Support code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BTI]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BTI]CUR (TABCUR) !Block
  DES DES Description
  DESSUP DES Description
  FCYLIN FCY Site -> [FCY]FCY0 =[BTI]FCYLIN (FACILITY) !Block
  FICHIER FIC*50 File name
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Delete
  LIN C*4 Line number
  OFFACC GAC Offset -> [GAC]GAC0 ="";OFFACC (GACCOUNT) !Other
  OFFCOD A*30
  OFFDES DES Description
  OFFREF REF Reference
  OFFSNS C*2 Sign
  OPENUM A*30 Operation
  RAT RCU Rate
  REF REF Reference
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BTI]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## BOX1099 (BX9) - 1099 box
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): BX90 FRM1099+BOX1099
Fields:
  AUUID AUUID Single identifier
  BOX1099 A*4 1099 box
  BOXTYP M*8 Box type [menu 3603: 1=Amount,2=Text,3=Checkbox]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BX9]CREUSR (AUTILIS) !Other
  DES DCO Description
  ENAFLG M*4 Active supplier [menu 1: 1=No,2=Yes]
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  LOWLIM DCB*9.2 Lower limit
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BX9]UPDUSR (AUTILIS) !Other

## BP1096PRN (B96R) - 1096 print table
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B96R0 YR1099+CPY+NUMLIG
Fields:
  AMT1099 MD1 1099 amount
  AMTBOX4 MD1 Income tax withheld
  AUUID AUUID Single identifier
  BOXALPHA A*1(20) 1099 box alpha
  CLED1 D Date 1
  CLED2 D Date 2
  CPY CPY Company -> [CPY]CPY0 =[B96R]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B96R]CREUSR (AUTILIS) !Other
  FAX TEL Fax
  FRMCNT L*5 Number of forms
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  RESALE A*10 Resale
  RPTCOD ARP Report code -> [ARP]ARP0 =[B96R]RPTCOD (AREPORT) !Other
  SEQREQ L*8 Sequence
  STATEID A*15 State ID
  TEL TEL Telephone
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B96R]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[B96R]USR (AUTILIS) !Other
  YR1099 C*4 Year

## BP1099BEGBAL (B9B) - 1099 beginning balance
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B9B0 YR1099+CPY+BPSNUM+SEQ (D); B9B1 YR1099+CPY+BPSNUM+FRM1099+BOX1099
Fields:
  AUUID AUUID Single identifier
  BEGBAL MD1 Beginning balance
  BOX1099 A*4 1099 box
  BPSNUM BPS Supplier -> [BPS]BPS0 =[B9B]BPSNUM (BPSUPPLIER) !Other
  CPY CPY Company -> [CPY]CPY0 =[B9B]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B9B]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[B9B]CUR (TABCUR) !Other
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  SEQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B9B]UPDUSR (AUTILIS) !Other
  YR1099 C*4 Year

## BP1099PRN (B9R) - 1099 print table
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B9R0 YR1099+CPY+BPSNUM+NUMLIG
Fields:
  AMT1099 MD1(20) 1099 amount
  AUUID AUUID Single identifier
  BOXALPHA A*1(20) 1099 box alpha
  BPSNUM BPS Supplier -> [BPS]BPS0 =[B9R]BPSNUM (BPSUPPLIER) !Other
  CLED1 D Date 1
  CLED2 D Date 2
  CPY CPY Company -> [CPY]CPY0 =[B9R]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B9R]CREUSR (AUTILIS) !Other
  FILCHK A*10 FATCA filing
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  POSS A*20 Possession
  RESALE A*10 Resale
  RPTCOD ARP Report code -> [ARP]ARP0 =[B9R]RPTCOD (AREPORT) !Other
  SEQREQ L*8 Sequence
  STATEID A*15 State ID
  TEL TEL Telephone
  TINCHK A*10 2nd TIN not.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B9R]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[B9R]USR (AUTILIS) !Other
  YR1099 C*4 Year

## BPS1099GEN (B9G) - 1099 generation
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B9G0 YR1099+CPY+BPSNUM+FRM1099+BOX1099; B9G1 YR1099+CPY+BPSNUM (D); B9G2 YR1099+CPY+BPSNUM+FRM1099 (D)
Fields:
  AMT1099 MD1 1099 amount
  AUUID AUUID Single identifier
  BOX1099 A*4 1099 box
  BPSNUM BPS Supplier -> [BPS]BPS0 =[B9G]BPSNUM (BPSUPPLIER) !Other
  CPY CPY Company -> [CPY]CPY0 =[B9G]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B9G]CREUSR (AUTILIS) !Other
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  TXTFLD A*20 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B9G]UPDUSR (AUTILIS) !Other
  YR1099 C*4 Year

## BPS1099MNT (B9M) - Supplier 1099 maintenance
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B9M0 YR1099+CPY+BPSNUM+FRM1099+BOX1099
Fields:
  AUUID AUUID Single identifier
  BOX1099 A*4 Supplier 1099 box
  BPSNUM BPS Supplier -> [BPS]BPS0 =[B9M]BPSNUM (BPSUPPLIER) !Other
  CPY CPY Company -> [CPY]CPY0 =[B9M]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B9M]CREUSR (AUTILIS) !Other
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  TXTFLD A*20 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B9M]UPDUSR (AUTILIS) !Other
  YR1099 C*4 Year

## BPS1099PAY (B9P) - Supplier 1099 payments
Notes: activity code S1099
Keys (first = PK; D = duplicates allowed): B9P0 YR1099+CPY+BPSNUM+PAYNUM+PAYLIN; B9P1 YR1099+CPY+BPSNUM+FRM1099+BOX1099 (D)
Fields:
  AMT1099 MD1 1099 amount
  AUUID AUUID Single identifier
  BOX1099 A*4 1099 box
  BPSNUM BPS Supplier -> [BPS]BPS0 =[B9P]BPSNUM (BPSUPPLIER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[B9P]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[B9P]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[B9P]CUR (TABCUR) !Delete
  FRM1099 M*15 1099 form [menu 3601: 1=None,2=MISC,3=INT,4=DIV,5=NEC]
  INVNUM VCR Invoice number
  PAYLIN C*4 Line
  PAYNUM VCR Payment number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[B9P]UPDUSR (AUTILIS) !Other
  YR1099 C*4 Year

## BSEINQ (BSI) - Balance sheet inquiry
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BSI0 PRONUM+LINNUM; BSI1 PRONUM+GRUACC (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ANTCDT MC1 Beginning credit balance
  ANTCDTLED MC1 Ledger beginning credit balance
  ANTDEB MC1 Beginning debit balance
  ANTDEBLED MC1 Ledger beginning debit balance
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BSI]BPR (BPARTNER) !Delete
  CDT MD1 Credit
  CDTLED MD1 Ledger credit
  COA COA Chart of accounts -> [COA]COA0 =[BSI]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[BSI]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BSI]CREUSR (AUTILIS) !Other
  DEB MD1 Debit
  DEBLED MD1 Ledger debit
  DES DES Description
  FCY FCY Site -> [FCY]FCY0 =[BSI]FCY (FACILITY) !Delete
  FINCDT MC1 Ending credit balance
  FINCDTLED MC1 Ledger ending credit balance
  FINDEB MC1 Ending debit balance
  FINDEBLED MC1 Ledger ending debit balance
  FINSALLED MC1 Ledger ending balance
  GRU GRY Group code -> [GRY]GRY0 =PYM;GRU;1 (GACCGRUPYM) !Delete
  GRUACC A*30 Code
  LEV C*2 Level
  LINNUM L*8 Line number
  ORDFLD A*100 Sort order
  PRONUM L*8 Process number
  SOLCDT MC1 Period credit balance
  SOLCDTLED MC1 Ledger period credit
  SOLDEB MC1 Period debit balance
  SOLDEBLED MC1 Ledger period debit
  SOLFIN MC1 Ending balance
  SOLPER MD1 Period balance
  SOLPERLED MC1 Ledger period balance
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BSI]UPDUSR (AUTILIS) !Other
  VOIVAL M*10 Include zero amounts [menu 1: 1=No,2=Yes]

## BUD (BUD) - Budget table
Notes: differs in V9.0 P12 (diff: AT3_BUD.htm)
Keys (first = PK; D = duplicates allowed): BUD0 LEDTYP+BUD+CPY+FCY+FIY+VER+ACC+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9; BUD1 ACCNUM
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Unique number
  AMT MD1 Amount act:PER
  AMTAPP MD1 Approved amount
  AMTATT MD1 Year-end outcome
  AMTCAP MD1 Accrued expenses amount
  AMTCCA MD1 Purchase accruals amount act:SVC
  AMTCMM MD1 Committed amt act:PER
  AMTCMMPRP MD1 Precommitted amt act:PER
  AMTFAS MD1 Capitalized amount
  AMTREA MD1 Actual amount act:PER
  APPDAT D Approval date
  AUUID AUUID Single identifier
  BUD BUP Budget -> [BUP]BUP0 =[BUD]BUD (BUDPAR) !Block
  BUDRPT MDC Budget postponement
  CCE1 CCE Dimension type 1 -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Block
  CCE2 CCE Dimension type 2 -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Block
  CCE3 CCE Dimension type 3 -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Block
  CCE4 CCE Dimension type 4 -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Block
  CCE5 CCE Dimension type 5 -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Block
  CCE6 CCE Dimension type 6 -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Block
  CCE7 CCE Dimension type 7 -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Block
  CCE8 CCE Dimension type 8 -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Block
  CCE9 CCE Dimension type 9 -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Block
  COA A*5 Chart code
  CPY CPY Company -> [CPY]CPY0 =[BUD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[BUD]CUR (TABCUR) !Block
  DIE1 A*5 Dimension type code
  DIE2 A*5 Dimension type code
  DIE3 A*5 Dimension type code
  DIE4 A*5 Dimension type code
  DIE5 A*5 Dimension type code
  DIE6 A*5 Dimension type code
  DIE7 A*5 Dimension type code
  DIE8 A*5 Dimension type code
  DIE9 A*5 Dimension type code
  FCY FCY Site -> [FCY]FCY0 =[BUD]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BUD]LED (GLED) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LOT A*5 Lot
  QTY QTY Quantity act:PER
  QTYCMM QTY Commitment act:PER
  QTYCMMPRP QTY Precommitment act:PER
  QTYREA QTY Comp qty act:PER
  REVDAT D Latest review date
  STA M*4 Status [menu 2691: 1=Entered,2=To be approved,3=Approved,4=Closed,5=Commitments carried forward]
  TEX A*50 Text
  TEXPER A*50 Text act:PER
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[BUD]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VER BUV Version -> [BUV]BUV0 =[BUD]VER (BUDVER) !Block

## BUDAPP (BOA) - Budget approval
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): BOA0 NUM; BOA1 TYP+ENV+FIY+ACC (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCNUM UNQ Budget line
  AMT MD1 Amount
  AMTAPP MD1 Approved amount
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[BOA]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[BOA]CUR (TABCUR) !Delete
  DMDDAT D Request date
  ENV ENV Envelope -> [ENV]ENV0 =[BOA]ENV (ENVELOPPE) !Delete act:GDD
  EXPNUM L*8 Export number
  FIY C*2 Fiscal year
  NUM A*12 Approval no.
  PRJ PRJ Project -> [PRJ]PRJ0 =[BOA]PRJ (PROJET) !Delete
  RENTXT A*50 Reason
  STA M*3 Status [menu 2699: 1=Rejected,2=Requested,3=Approved,4=Cancelled]
  TYP M*3 Type [menu 2694: 1=Envelope,2=Fiscal year budget,3=Budget line,4=Multiple]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## BUDAPPDET (BAD) - Approval detail
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): BAD0 NUMERO+NUMAPP; BAD1 NUMAPP+NUMERO
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCNUM UNQ Budget line
  AMT MD1 Amount
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[BAD]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BAD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BAD]CUR (TABCUR) !Delete
  ENV ENV Envelope -> [ENV]ENV0 =[BAD]ENV (ENVELOPPE) !Delete act:GDD
  FIY C*2 Fiscal year
  NUMAPP A*12 Approval no.
  NUMERO C*2 Number
  PRJ PRJ Project -> [PRJ]PRJ0 =[BAD]PRJ (PROJET) !Delete
  TYP M*3 Type [menu 2694: 1=Envelope,2=Fiscal year budget,3=Budget line,4=Multiple]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BAD]UPDUSR (AUTILIS) !Other

## BUDFORCAL (BUC) - Budget calculation formula
Notes: differs in V9.0 P12 (diff: AT3_BUDFORCAL.htm)
Keys (first = PK; D = duplicates allowed): BUC0 BUDFOR+LIN
Fields:
  ACC A*15 Account
  AUUID AUUID Single identifier
  BUD BUP Budget -> [BUP]BUP0 =[BUC]BUD (BUDPAR) !Block
  BUDFOR A*10 Formula
  CCE A*15(9) Analytical dimension
  CLCFOR A*250 Expression
  CPY CPY Company -> [CPY]CPY0 =[BUC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEL M*4 Delete budget [menu 1: 1=No,2=Yes]
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENDDAT D Period end
  FCY FCY Site -> [FCY]FCY0 =[BUC]FCY (FACILITY) !Block
  FIYEND C*2 Fiscal year end
  FIYSTR C*2 Fiscal year start
  FLGDSP M*4 Distribution [menu 1: 1=No,2=Yes]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  OD M*4 Generate MO [menu 1: 1=No,2=Yes]
  PERDEB C*4 Period start
  PERFIN C*4 Period end
  SHOTRA AX1 Short description
  STRDAT D Period start
  TYP M*15 Formula type [menu 874: 1=Budgeted,2=Actual,3=Commited,4=Precommitted]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VER BUV Version -> [BUV]BUV0 =[BUC]VER (BUDVER) !Block

## BUDOD (BDE) - Budget misc. operations
Keys (first = PK; D = duplicates allowed): BDE0 NUM
Fields:
  AUUID AUUID Single identifier
  BUD BUP Budget -> [BUP]BUP0 =[BDE]BUD (BUDPAR) !Block
  BUDTYP TBU Transaction code -> [TBU]TBU0 =BUDTYP;1 (TABBUDTYP) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATEXT D Reversal date
  DES DES Description
  ENAEXT M*4 Reversal [menu 1: 1=No,2=Yes]
  NUM VCR Document no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VER BUV Version -> [BUV]BUV0 =[BDE]VER (BUDVER) !Block

## BUDODS (BDO) - Budget misc. operations
Notes: differs in V9.0 P12 (diff: AT3_BUDODS.htm)
Keys (first = PK; D = duplicates allowed): BDO0 NUM+LIN
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMT MD1 Amount
  AUUID AUUID Single identifier
  CCE1 CCE Dimension type 1 -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Block
  CCE2 CCE Dimension type 2 -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Block
  CCE3 CCE Dimension type 3 -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Block
  CCE4 CCE Dimension type 4 -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Block
  CCE5 CCE Dimension type 5 -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Block
  CCE6 CCE Dimension type 6 -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Block
  CCE7 CCE Dimension type 7 -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Block
  CCE8 CCE Dimension type 8 -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Block
  CCE9 CCE Dimension type 9 -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Block
  COA COA Chart code -> [COA]COA0 =[BDO]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[BDO]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BDO]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BDO]CUR (TABCUR) !Block
  DIE1 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE1 (GDIE) !Block
  DIE2 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE2 (GDIE) !Block
  DIE3 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE3 (GDIE) !Block
  DIE4 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE4 (GDIE) !Block
  DIE5 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE5 (GDIE) !Block
  DIE6 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE6 (GDIE) !Block
  DIE7 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE7 (GDIE) !Block
  DIE8 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE8 (GDIE) !Block
  DIE9 DIE Dimension type code -> [DIE]DIE0 =[BDO]DIE9 (GDIE) !Block
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[BDO]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED Ledger -> [LED]LED0 =[BDO]LED (GLED) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  STRDAT D Start date
  UOM UOM Unit -> [TUN]TUN0 =[BDO]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BDO]UPDUSR (AUTILIS) !Other

## BUDPAR (BUP) - Budget setup
Notes: differs in V9.0 P12 (diff: AT3_BUDPAR.htm)
Keys (first = PK; D = duplicates allowed): BUP0 BUD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[BUP]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  BUD BUP Budget -> [BUP]BUP0 =[BUP]BUD (BUDPAR) !Delete
  BUDCTL M*15 Control type [menu 2600: 1=None,2=Annual,3=Period,4=Sliding,5=Accumulated]
  BUPODS M*15 Budget misc. operations [menu 2609: 1=None,2=Manual,3=Complete]
  COA COA Chart of accounts -> [COA]COA0 =[BUP]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BUP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BUP]CUR (TABCUR) !Block
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE(9) Dimension type -> [DIE]DIE0 =[BUP]DIE (GDIE) !Block
  DIENBR C*1 Number of dimension types
  DIVAMT L*8 Divisor
  GDDFLG M*4 Expenses management [menu 1: 1=No,2=Yes]
  LEV M*20 Definition level [menu 623: 1=Company,2=Site]
  PYMACC GYM Pyramid -> [GYM]GYM0 =[BUP]PYMACC (GACCPYM) !Block
  PYMACCLEV C*2 Level
  PYMCCE CYM(9) Pyramids -> [CYM]CYM0 =[BUP]PYMCCE (GCCEPYM) !Block
  PYMCCELEV C*2(9) Level
  QTY M*4 Quantity entry [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BUP]UPDUSR (AUTILIS) !Other
  VLYEND D Validity end date
  VLYSTR D Validity start date

## BUDPURAUD (BUA) - Audit
Keys (first = PK; D = duplicates allowed): BUA0 TYP+TYPPCE+NUM+LIN+SEQ+ANALIN+FIY (D); BUA1 BUANUM
Fields:
  ACC GAC(10) Account -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Delete
  ANALIN L*8 Order information
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[BUA]BPR (BPARTNER) !Delete
  BUANUM UNQ Unique number
  BUD BUP Budget -> [BUP]BUP0 =[BUA]BUD (BUDPAR) !Delete
  CCE CCE(9) Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Delete
  CMM MD1 Commitments
  CMMLED MD1(10) Commitments (ref)
  CMMNUM VCR Commitment no.
  CMMPRP MD1 Precommitments
  CMMPRPLED MD1(10) Pre-commitments (ref)
  COA COA(10) Chart code -> [COA]COA0 =COA(indice) (GCOA) !Delete
  CODGAU A*10 Automatic journal
  CPY CPY Company -> [CPY]CPY0 =[BUA]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[BUA]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BUA]CUR (TABCUR) !Delete
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[BUA]CURLED (TABCUR) !Delete
  DAT D Date
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =DIE(indice) (GDIE) !Delete
  FCY FCY Site -> [FCY]FCY0 =[BUA]FCY (FACILITY) !Delete
  FIY C*2 Fiscal year
  GRDACT M*15 Last reason [menu 2683: 1=Creation,2=Modification,3=Deletion,4=Closing,5=Reversal,6=Closing cancellation,7=Carryforward,8=Resynchronization]
  GRDPCE M*15 Last journal [menu 2684: 1=Purchase request,2=Order,3=Invoice,4=GRNI (GoodsReceivedNotInvoiced),5=Receivable credit memos,6=Carryforward,7=Credit memo,8=Accounting document]
  LED LED(10) Ledger -> [LED]LED0 =LED(indice) (GLED) !Delete
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN L*8 Line number
  NUM VCR Document no.
  POSTPONED M*4 Postponed [menu 1: 1=No,2=Yes]
  QTY QTY Quantity
  REA MD1 Carried out
  REALED MD1(10) Carried out
  SEQ L*8 Sequence
  TYP M*15 Document type [menu 2684: 1=Purchase request,2=Order,3=Invoice,4=GRNI (GoodsReceivedNotInvoiced),5=Receivable credit memos,6=Carryforward,7=Credit memo,8=Accounting document]
  TYPPCE GTE Entry type -> [GTE]GTE0 =TYPPCE;[V]GSUPCLE (GTYPACCENT) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[BUA]UPDUSR (AUTILIS) !Other

## BUDREV (BRV) - Budget review
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): BRV0 NUM; BRV1 TYP+ENV+FIY+ACC (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCNUM UNQ Budget line
  AMT MD1 Amount
  AMTASK MD1 Requested amount
  AMTPNV MD1 Amount not distributed
  AMTPRS MD1 Reserve amount
  AMTRAL MD1 Extension
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[BRV]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[BRV]CUR (TABCUR) !Delete
  DMDDAT D Request date
  ENT ENT Recipient entity -> [ENT]ENT0 =[BRV]ENT (ENTITE) !Delete
  ENV ENV Envelope -> [ENV]ENV0 =[BRV]ENV (ENVELOPPE) !Delete act:GDD
  EXPNUM L*8 Export number
  FIY C*2 Fiscal year
  NUM A*12 Review no.
  RENTAB ADI Request reason -> [ADI]CODE =349;RENTAB (ATABDIV) !Block
  RENTXT ACB Refusal reason
  STA M*3 Status [menu 2699: 1=Rejected,2=Requested,3=Approved,4=Cancelled]
  TYP M*3 Review type [menu 2694: 1=Envelope,2=Fiscal year budget,3=Budget line,4=Multiple]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## BUDREVDET (BVD) - Review detail
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): BVD0 NUMERO+NUMREV
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCNUM UNQ Budget line
  AMT MD1 Amount
  AMTASK MD1 Requested amount
  AMTPNV MD1 Amount not distributed
  AMTPRS MD1 Reserve amount
  AMTRAL MD1 Extension
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[BVD]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BVD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[BVD]CUR (TABCUR) !Delete
  ENT ENT Recipient entity -> [ENT]ENT0 =[BVD]ENT (ENTITE) !Delete
  ENV ENV Envelope -> [ENV]ENV0 =[BVD]ENV (ENVELOPPE) !Delete act:GDD
  FIY C*2 Fiscal year
  NUMERO C*2 Number
  NUMREV A*12 Review no.
  TYP M*4 Review type [menu 2694: 1=Envelope,2=Fiscal year budget,3=Budget line,4=Multiple]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BVD]UPDUSR (AUTILIS) !Other

## BUDTYP (BUT) - Budget type
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): BUT0 BUDCOD
Fields:
  AUUID AUUID Single identifier
  BUDCOD A*5 Code
  COU ANM Sequence number -> [ANM]ANM0 =[BUT]COU (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  GFY AGC Group of company -> [AGF]AGF0 =[BUT]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*20 Manual sequence no. [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author
  YEAFLG M*2 Budget category [menu 2692: 1=Annual,2=Multiannual]

## BUDVARCAL (BVC) - Budget calculation variable
Keys (first = PK; D = duplicates allowed): BVC0 BUDFOR+VARCOD
Fields:
  AUUID AUUID Single identifier
  BUDFOR A*10 Formula
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BVC]CREUSR (AUTILIS) !Other
  DES DES Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BVC]UPDUSR (AUTILIS) !Other
  VARCOD A*10 Variable
  VARVAL A*20(30) Value

## BUDVER (BUV) - Budget versions
Keys (first = PK; D = duplicates allowed): BUV0 BUD+VER
Fields:
  AUUID AUUID Single identifier
  BUD BUP Budget -> [BUP]BUP0 =[BUV]BUD (BUDPAR) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BUV]CREUSR (AUTILIS) !Other
  CTL M*4 Final [menu 1: 1=No,2=Yes]
  DEF M*4 By default [menu 1: 1=No,2=Yes]
  DESTRA AX3 Description
  SHOTRA AX1 Short description
  STA M*15 Status [menu 2669: 1=Open,2=Closed]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BUV]UPDUSR (AUTILIS) !Other
  VER BUV Version -> [BUV]BUV0 =BUD;VER (BUDVER) !Delete

## BUILOCSPA (BLS) - Building location
Notes: activity code KSP
Keys (first = PK; D = duplicates allowed): BLS0 NUM
Fields:
  AUUID AUUID Single identifier
  BUILOC M*12 Location [menu 3611: 1=Located on national territory,2=Located in Basque Country or Navarre,3=Without cadastre reference,4=Located abroad]
  CDRREF A*25 Cadastre
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BLS]CREUSR (AUTILIS) !Other
  NUM VCR Document no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BLS]UPDUSR (AUTILIS) !Other

## CADISTMP (DTP) - Budget weighting codes
Keys (first = PK; D = duplicates allowed): DTP0 DTP
Fields:
  AUUID AUUID Single identifier
  COE DCB*9(12) Coefficients
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESTRA AX3 Description
  DTP DTP Distribution -> [DTP]DTP0 =[DTP]DTP (CADISTMP) !Delete
  EXPNUM L*8 Export number
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CAPFLOTMP (CWT) - Capital flow
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): CWT0 NUMREQ+LIN
Fields:
  AMT DCB*9.2(12) Amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CWT]CREUSR (AUTILIS) !Other
  LIN C*2 Line number
  NUMREQ L*8 Query no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CWT]UPDUSR (AUTILIS) !Other

## CASHPAYSPA (CPS) - Cash payments
Notes: activity code KSP; differs in V9.0 P12 (diff: AT3_CASHPAYSPA.htm); differs in V10 P1 (diff: ATD_CASHPAYSPA.htm)
Keys (first = PK; D = duplicates allowed): CPS0 TYP+NUM+LIN; CPS1 ACCNUM+LIN; CPS2 BPRNUM (D)
Fields:
  ACCNUM UNQ Internal number
  AMOUNT MD1 Amount
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =BPRNUM (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[CPS]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CPS]CREUSR (AUTILIS) !Other
  DATGAS D Entry date
  FCY FCY Site -> [FCY]FCY0 =[CPS]FCY (FACILITY) !Block
  INVDAT D Invoice date
  INVNUM VCR Invoice number
  LIN L*8 Line no.
  NUM VCR Document no.
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CPS]UPDUSR (AUTILIS) !Other

## CDIADSP (DAD) - Dimension allocations
Keys (first = PK; D = duplicates allowed): DAD0 LED+COD+LIN; DAD1 LED+COD (D)
Fields:
  ACCDEN GAC Destination account -> [GAC]GAC0 =COA;ACCDEN (GACCOUNT) !Block
  ACCDSP A*220 Distribution account
  ACCORI GAC Source account -> [GAC]GAC0 =COA;ACCORI (GACCOUNT) !Block
  ACCREF A*15 Account to distribute
  ACS ACS Access code -> [ACS]ACS0 =[DAD]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CCERCP A*15 Receiving dimension
  CCEREF A*15 Dimension to distribute
  COA COA Chart code -> [COA]COA0 =[DAD]COA (GCOA) !Block
  COD DAD Code -> [DAD]DAD0 =LED;COD;LIN (CDIADSP) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[DAD]DIE (GDIE) !Block
  EXPNUM L*8 Export number
  FRWCCE M*4 Carryforward [menu 1: 1=No,2=Yes]
  GSP A*10 Receiving group
  LED LED Ledger -> [LED]LED0 =[DAD]LED (GLED) !Delete
  LIN C*3 Line number
  PRC DCB*2.2 % distribution
  SHOTRA AX1 Short description
  TYP M*15 Type [menu 633: 1=Entry,2=Calculated amount,3=Calculated quantity]
  UOM UOM Unit -> [TUN]TUN0 =[DAD]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VLYEND D Validity end date
  VLYSTR D Validity start date

## CSFPARH (CWH) - Header extraction parameters
Notes: activity code CSFLO
Keys (first = PK; D = duplicates allowed): CWH0 CODANY
Fields:
  AUUID AUUID Single identifier
  CODANY A*10 Extraction code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Long title
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXTFLG M*4 Tax incl. extraction [menu 1: 1=No,2=Yes]
  FRM A*250 Accounts
  RATDEVFLG M*4 Include rate deviations [menu 1: 1=No,2=Yes]
  SHOTRA AX1 Short description
  TYPMNT M*15 Amount type [menu 2665: 1=Movements + CR + Closing,2=Movements + CR,3=Movements + Closing,4=Movements only,5=CR only,6=Closing only]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CSFPARL (CWL) - Line extraction parameters
Notes: activity code CSFLO
Keys (first = PK; D = duplicates allowed): CWL0 CODANY+LIG
Fields:
  AUUID AUUID Single identifier
  COD1 A*10 Code
  COD2 A*10 Subcode
  CODANY A*10 Extraction code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CWL]CREUSR (AUTILIS) !Other
  LIBEL A*50 Description
  LIG C*3 Line number
  ORIFRM A*250 Accounts
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CWL]UPDUSR (AUTILIS) !Other

## CSFRES (CWR) - Extraction result
Keys (first = PK; D = duplicates allowed): CWR0 NUMRPT+CODANY+LIG+CPY+FCY
Fields:
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  COD1 A*10 Code
  COD2 A*10 Subcode
  CODANY A*10 Extraction code
  CPY CPY Company -> [CPY]CPY0 =[CWR]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM HS Creation time
  CREUSR A*5 Creation user
  CURLED CUR Ledger currency -> [TCU]TCU0 =[CWR]CURLED (TABCUR) !Block
  DATDEB D Start date
  DATFIN D End date
  FCY FCY Site -> [FCY]FCY0 =[CWR]FCY (FACILITY) !Delete
  LIBEL A*50 Description
  LIG C*3 Line number
  NUMRPT RPT Query no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CWR]UPDUSR (AUTILIS) !Other

## CSFRESD (CSRD) - Cash flow analysis
Notes: activity code CSFLO
Keys (first = PK; D = duplicates allowed): CSRD0 NUMRPT+NUMLIN+NUMLINDET
Fields:
  ACC GAC Account -> [GAC]GAC0 =[CSRD]ACC (GACCOUNT) !BSRA
  AMTLEDN MD1 Ledger amount
  AMTLEDN1 MD1 Ledger amount (n-1)
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[CSRD]BPRNUM (BPARTNER) !Delete
  COD1 A*10 Code
  COD2 A*10 Subcode
  CPYLIN CPY Company -> [CPY]CPY0 =[CSRD]CPYLIN (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CSRD]CREUSR (AUTILIS) !Other
  CURLED CUR Ledger currency -> [TCU]TCU0 =[CSRD]CURLED (TABCUR) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[CSRD]FCYLIN (FACILITY) !Delete
  LIG C*3 Line number
  NUM VCR Document number
  NUMLIN L*8 Line
  NUMLINDET L*8 Sequence no.
  NUMRPT RPT Query no.
  PERIOD C*4 Period
  TYP GTE Entry type -> [GTE]GTE0 =[CSRD]TYP (GTYPACCENT) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CSRD]UPDUSR (AUTILIS) !Other

## CSFRESH (CSRH) - Cash flow analysis
Notes: activity code CSFLO
Keys (first = PK; D = duplicates allowed): CSRH0 NUMRPT
Fields:
  ALLFCY M*4 All sites [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BETCPYDET M*18 Intercompany detail [menu 1: 1=No,2=Yes]
  CODANY A*10 Extraction code
  CPY CPY Company -> [CPY]CPY0 =[CSRH]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Creation time
  CREUSR A*5 Creation user
  DATDEB D Start date
  DATFIN D End date
  ENDAMT0 MD1 End date amount
  ENDAMT1 MD1 Amt end date (n-1)
  FCY FCY Site -> [FCY]FCY0 =[CSRH]FCY (FACILITY) !Delete
  HMLPERFLG M*4 Previous period [menu 1: 1=No,2=Yes]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NUMRPT RPT Query no.
  RATDEV0 MD1 Rate variance
  RATDEV1 MD1 Rate variance
  STRAMT0 MD1 Start date amount
  STRAMT1 MD1 Amt start date (n-1)
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[CSRH]UPDUSR (AUTILIS) !Other

## CSFRESL (CSRL) - Cash flow analysis
Notes: activity code CSFLO
Keys (first = PK; D = duplicates allowed): CSRL0 NUMRPT+LIG+CPYLIN+FCYLIN+BPRNUM; CSRL1 NUMRPT+NUMLIN
Fields:
  AMTLED1N MD1 Ledger amount
  AMTLED1N1 MD1 Ledger amount (n-1)
  AMTLEDN MD1 Ledger amount
  AMTLEDN1 MD1 Ledger amount (n-1)
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =BPRNUM (BPARTNER) !Block
  COD1 A*10 Code
  COD2 A*10 Subcode
  CPYLIN CPY Company -> [CPY]CPY0 =[CSRL]CPYLIN (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Creation time
  CREUSR A*5 Creation user
  CURLED CUR Ledger currency -> [TCU]TCU0 =[CSRL]CURLED (TABCUR) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[CSRL]FCYLIN (FACILITY) !Delete
  LIBEL A*50 Description
  LIG C*3 Line number
  NUMLIN L*8 Line
  NUMRPT RPT Query no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CSRL]UPDUSR (AUTILIS) !Other
  USRFLG M*4 User value [menu 1: 1=No,2=Yes]
  USRFLG1 M*4 User value [menu 1: 1=No,2=Yes]

## DADCPY (DCP) - DASD company
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): DCP0 CPY
Fields:
  ABC A*1 BIS,TER,QUATER
  ABC2 A*1 BIS,TER,QUATER
  ADDCPL A*40 Address complement
  ADDCPL2 A*40 Address complement
  AUUID AUUID Single identifier
  CPY CPY DASD company -> [CPY]CPY0 =[DCP]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DCP]CREUSR (AUTILIS) !Other
  CTYNAM CT0 Municipality
  CTYNAM2 CT0 Municipality
  DADCPYNAM A*50 Company name
  DADCRN CRN Company tax ID no.
  DADCRN2 CRT Site tax ID no.
  DADNAF NAF SIC code
  DADPOSCOD A*5 Postal code
  DADPOSCOD2 A*5 Postal code
  POSCTY A*26 Distributor office
  POSCTY2 A*26 Distributor office
  POSCTYCOD A*5 Municipality code
  POSCTYCOD2 A*5 Municipality code
  STREET A*40 Street
  STREET2 A*40 Street
  STREETNUM A*4 Street number
  STREETNUM2 A*4 Street number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DCP]UPDUSR (AUTILIS) !Other

## DADFCY (DFC) - DAS2 site
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): DFC0 FCY
Fields:
  ABC A*1 BIS,TER,QUATER
  ADDCPL A*40 Address complement
  AUUID AUUID Single identifier
  CRAM A*17 CRAM number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DFC]CREUSR (AUTILIS) !Other
  CRN01 CRT Site tax ID no. on 01/01
  CTYNAM CT0 Municipality
  DADCRN CRT Site tax ID no.
  DADFCYNAM A*50 Company name
  DADNAF NAF SIC code
  DADPOSCOD A*5 Postal code
  DENNUMCOM A*100 Email
  EMAIL MAI Email address
  FCY FCY DAS2 site -> [FCY]FCY0 =[DFC]FCY (FACILITY) !Delete
  JOB A*30 Business
  NBDAS M*2 DAS2 number [menu 695: 1=1,2=2]
  POSCTY A*26 Distributor office
  POSCTYCOD A*5 Municipality code
  RPBFIRNAM A*20 First name
  RPBJOB A*39 Profession
  RPBSURNAM A*30 Last name
  STREET A*40 Street
  STREETNUM A*4 Street number
  TAXWAG M*4 Tax on salaries [menu 1: 1=No,2=Yes]
  TEL TEL Telephone
  TOTNUMYEA L*8 Annual headcount
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DFC]UPDUSR (AUTILIS) !Other
  URSCOD A*4 URSSAF code
  URSCPT A*20 URSSAF account

## DATEVBPACC (DTB) - DATEV BP assignment
Notes: activity code KDE
Keys (first = PK; D = duplicates allowed): DTB0 BPRNUM
Fields:
  ACCDATEV A*9 DATEV account
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[DTB]BPRNUM (BPARTNER) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTB]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTB]UPDUSR (AUTILIS) !Other

## DATEVCHRONO (DTC) - 
Notes: activity code KDE
Keys (first = PK; D = duplicates allowed): DTC0 ID
Fields:
  AUUID AUUID Single identifier
  CHRONO VCR Sequence no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTC]CREUSR (AUTILIS) !Other
  ID C*4 Identifier
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTC]UPDUSR (AUTILIS) !Other

## DATEVGLACC (DTA) - DATEV general acct. assignment
Notes: activity code KDE
Keys (first = PK; D = duplicates allowed): DTA0 COA+ACC
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDATEV A*8 DATEV account
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[DTA]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTA]CREUSR (AUTILIS) !Other
  FLGAUTO M*4 DATEV auto account [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTA]UPDUSR (AUTILIS) !Other

## DATEVTAX (DTT) - DATEV tax code assignment
Notes: activity code KDE; differs in V9.0 P12 (diff: AT3_DATEVTAX.htm); differs in V10 P1 (diff: ATD_DATEVTAX.htm)
Keys (first = PK; D = duplicates allowed): DTT0 LEG+TAX
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DTT]CREUSR (AUTILIS) !Other
  DTTISSCOD C*4 DATEV §13b issue code
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TAX VAT Tax code -> [TVT]TVT0 =TAX;LEG (TABVAT) !Block
  TAXDATEV A*30 DATEV tax code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DTT]UPDUSR (AUTILIS) !Other

## DCLCUSVATBE (DLCB) - Annual customer listing
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): DLCB0 CPY+NUMRPT+BPR+EECNUM
Fields:
  AMTNOT MD1 Amount - tax
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DLCB]BPR (BPARTNER) !Block
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[DLCB]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLCB]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[DLCB]CRY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[DLCB]CUR (TABCUR) !Block
  EECNUM A*20 EU VAT no. act:DEB
  ENDDAT D Declaration date
  NUMRPT L*8 Query no.
  STRDAT D Declaration date
  TEL TEL Telephone
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLCB]UPDUSR (AUTILIS) !Other

## DCLCUSVATBED (DLCBD) - Annual customer listing
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): DLCBD0 CPY+NUMRPT+BPR+EECNUM+TYP+NUM+LIN
Fields:
  ACCDAT D Accounting date
  AMTNOT MD1 Amount - tax
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DLCBD]BPR (BPARTNER) !Block
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[DLCBD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLCBD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DLCBD]CUR (TABCUR) !Block
  EECNUM A*20 EU VAT no. act:DEB
  LIN C*3 Line number
  NUM VCR Document no.
  NUMRPT L*8 Query no.
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLCBD]UPDUSR (AUTILIS) !Other
  VAT VAT VAT code -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATRAT DCB*3.6 VAT rate

## DCLEECVATBE (DLEB) - EU VAT statement (header)
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): DLEB0 CPY+NUMRPT+BPR+EECNUM+OPECOD
Fields:
  AMTNOT MD1 Amount - tax
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DLEB]BPR (BPARTNER) !Block
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[DLEB]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLEB]CREUSR (AUTILIS) !Other
  CRY CRY Countries -> [TCY]TCY0 =[DLEB]CRY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[DLEB]CUR (TABCUR) !Block
  EECNUM A*20 EU VAT no. act:DEB
  ENDDAT D Declaration date
  NUMRPT L*8 Query no.
  OPECOD ADI Operation code -> [ADI]CODE =369;OPECOD (ATABDIV) !Block
  STRDAT D Declaration date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLEB]UPDUSR (AUTILIS) !Other

## DCLEECVATBED (DLEBD) - EU VAT statement (detail)
Notes: activity code KBE
Keys (first = PK; D = duplicates allowed): DLEBD0 CPY+NUMRPT+BPR+EECNUM+OPECOD+TYP+NUM+LIN
Fields:
  ACCDAT D Accounting date
  AMTNOT MD1 Amount - tax
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DLEBD]BPR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLEBD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLEBD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DLEBD]CUR (TABCUR) !Block
  EECNUM A*20 EU VAT no. act:DEB
  LIN C*3 Line number
  NUM VCR Document no.
  NUMRPT L*8 Query no.
  OPECOD ADI Operation code -> [ADI]CODE =369;OPECOD (ATABDIV) !Block
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLEBD]UPDUSR (AUTILIS) !Other
  VAT VAT VAT code -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATRAT DCB*3.6 VAT rate

## DCLVAT (DLV) - Tax declaration on the debits
Notes: differs in V9.0 P12 (diff: AT3_DCLVAT.htm)
Keys (first = PK; D = duplicates allowed): DLV0 CPY+FCY+STRDAT+VAT+ACC+NUMRPT
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMT MD1 Amount
  AMTTAX MD1 Tax amount
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[DLV]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLV]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLV]CREUSR (AUTILIS) !Other
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[DLV]FCY (FACILITY) !Block
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  NUMRPT L*8 Query no.
  OPTDAT M*15 Date option [menu 687: 1=Accounting date,2=Document date]
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  TYPAMT M*15 Amount type [menu 686: 1=Base,2=Amount]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLV]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]

## DCLVATBOXDBD (DLVBD) - VAT detail
Notes: activity code DCL; not in V9.0 P12 (new table); differs in V10 P1 (diff: ATD_DCLVATBOXDBD.htm)
Keys (first = PK; D = duplicates allowed): DLVBD0 CPY+FCY+STRDAT+ACC+VATBOX+NUMRPT+TYP+NUM+LIN; DLVBD1 CPY+NUMRPT (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  AMT MD1 Amount
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[DLVBD]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLVBD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLVBD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DLVBD]CUR (TABCUR) !Block
  ENDDAT D Declaration date
  FCY FCY Site -> [FCY]FCY0 =[DLVBD]FCY (FACILITY) !Block
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  LIN C*3 Line
  NUM VCR Document no.
  NUMRPT L*8 Query no.
  OPTDAT M*15 Date option [menu 687: 1=Accounting date,2=Document date]
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  STRDAT D Declaration date
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPAMT M*15 Amount type [menu 686: 1=Base,2=Amount]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLVBD]UPDUSR (AUTILIS) !Other
  VAT VAT VAT code -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATBOX A*5 VAT box
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VATRAT DCB*3.6 VAT rate

## DCLVATBOXH (DLVB) - VAT header
Notes: activity code DCL; not in V9.0 P12 (new table); differs in V10 P1 (diff: ATD_DCLVATBOXH.htm)
Keys (first = PK; D = duplicates allowed): DLVB0 GRPCPY+CPY+DCLVATTYP+NUMRPT+VATBOX
Fields:
  AMT MD1 Amount
  AMTNOTCLT MD1 Collected -tax amount
  AMTNOTDED MD1 Deductible amount
  AMTVATCLT MD1 Collected tax amount
  AMTVATDED MD1 Deductible amount
  AUUID AUUID Single identifier
  CODVATGRP VATGRP VAT group -> [VATGH]VATGH0 =[DLVB]CODVATGRP (VATGRP) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLVB]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLVB]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DLVB]CUR (TABCUR) !Block
  DATMAX D Journal date
  DCLVATTYP M*15 VAT type [menu 204: 1=On debit,2=On payment]
  ENDDAT D Declaration date
  FCY FCY Site -> [FCY]FCY0 =[DLVB]FCY (FACILITY) !Block
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  GRPCPY AGF Company group -> [AGF]AGF0 =[DLVB]GRPCPY (AGRPFCY) !Block
  GRPVAT M*4 VAT group [menu 3652: 1=Issue operation (=collected -tax amount),2=Taxes due (=collected VAT),3=Receipt operations (=deductible -tax amount),4=Deductible taxes (=deductible VAT)]
  LIN C*3 Line
  NUMRPT L*8 Query no.
  OPT M*25 Option [menu 688: 1=VAT/debit allocated first,2=Pro rata]
  OPTDAT M*15 Date option [menu 687: 1=Accounting date,2=Document date]
  REFTEX A*10 Identifier 2
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  STRDAT D Declaration date
  TYPAMT M*15 Amount type [menu 686: 1=Base,2=Amount]
  TYPBOX M*4 Type [menu 3651: 1=Title,2=Detail,3=Total,4=Off declaration]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLVB]UPDUSR (AUTILIS) !Other
  VATBOX A*5 VAT box
  VATFNC AFC Function code -> [AFC]CODINT =[DLVB]VATFNC (AFONCTION) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]

## DCLVATBOXPYD (DLVBP) - VAT detail
Notes: activity code DCL; not in V9.0 P12 (new table); differs in V10 P1 (diff: ATD_DCLVATBOXPYD.htm)
Keys (first = PK; D = duplicates allowed): DLVBP0 CPY+FCY+STRDAT+ACC+BPR+MTC+VATBOX+VAT+VATIPT+NUMRPT+TYP+NUM+LIN
Fields:
  ACC GAC Accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCBPR SAC Control
  ACCDAT D Accounting date
  ACCNUM UNQ Internal number
  AMT MD1 Amount
  AMTVCR MD1 Payment amount
  ATIVCR MD1 Amount + tax
  AUUID AUUID Single identifier
  BASNOTLIN MD1 Base before tax
  BASVATLIN MD1 Tax base
  BPR BPR BP -> [BPR]BPR0 =[DLVBP]BPR (BPARTNER) !Block
  COA COA Chart code -> [COA]COA0 =[DLVBP]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLVBP]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLVBP]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DLVBP]CUR (TABCUR) !Block
  DATMAX D Journal date
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[DLVBP]FCY (FACILITY) !Block
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  FLGVATPAI M*4 Tax on debit [menu 1: 1=No,2=Yes]
  LIN C*3 Line number
  MTC A*5 Matching
  MTCACC GAC Account -> [GAC]GAC0 =COA;MTCACC (GACCOUNT) !Block
  MTCBPR SAC Control
  MTCDAT D Matching date
  NUM VCR Document no.
  NUMRPT L*8 Query no.
  OPT M*25 Option [menu 688: 1=VAT/debit allocated first,2=Pro rata]
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPAMT M*15 Amount type [menu 686: 1=Base,2=Amount]
  TYPREC C*1 Record type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLVBP]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATBOX A*5 VAT box
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VATRAT DCB*3.6 Tax

## DCLVATITA (DVI) - Italian VAT detail declaration
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): DVI0 CPY+FCY+VATTYP+ACCDAT+NUM+VATRAT+VAT+DEDRAT; DVI1 FIY+PER+VAT+VATRAT+DEDRAT (D)
Fields:
  ACC GAC General accounts -> [GAC]GAC0 ="";ACC (GACCOUNT) !Other
  ACCDAT D Accounting date
  AMTCUR MD1 Amount in currency
  AMTDUT MD1 Postable amount
  AMTDUTCUR MD1 Postable currency amt
  AMTDUTEUR MD1 Postable euro amount
  AMTEUR MD1 EURO VAT amount
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPRNAM NAM(2) Company name
  BPRNUM BPR BP -> [BPR]BPR0 =[DVI]BPRNUM (BPARTNER) !Block
  BPRTYP M*15 BP type [menu 644: 1=Customer,2=Supplier]
  CALMONTH C*2 Calendar month
  CALYEAR C*4 Civil year
  CPY CPY Company -> [CPY]CPY0 =[DVI]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DVI]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DVI]CUR (TABCUR) !Block
  DEDDUT MD1 Deductible base
  DEDRAT DCB*3.6 Deductible %
  DEDVAT MD1 Input VAT
  DESVCR DES Description
  EECNUM A*20 EU identification
  EURCUR CUR EURO currency code -> [TCU]TCU0 =[DVI]EURCUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[DVI]FCY (FACILITY) !Block
  FCYNUM FCY Site document code -> [FCY]FCY0 =[DVI]FCYNUM (FACILITY) !Block
  FIY C*2 Fiscal year
  INVDAT D Invoice date
  INVNUM VCR Invoice number
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  NUM VCR Document no.
  PER C*2 Period
  REGTYP A*1 Registry type
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  SNS C*2 Sign
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DVI]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATNUM A*15 IVA partita
  VATPAY M*15 Tax/collection flag [menu 204: 1=On debit,2=On payment]
  VATRAT DCB*3.6 Rate
  VATREG ANM VAT registry -> [ANM]ANM0 =[DVI]VATREG (ACODNUM) !Block
  VATTYP A*4 VAT type

## DCLVATITA2 (DV2) - Italian VAT total declaration
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): DV20 CPY+FCY+REGIVA+REGTYP+VAT+FIY+PER
Fields:
  AMTCUR MD1 Amount in currency
  AMTDUT MD1 Postable amount
  AMTDUTCUR MD1 Postable currency amt
  AMTDUTEUR MD1 Postable euro amount
  AMTEUR MD1 EURO VAT amount
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  CALMONTH C*2 Calendar month
  CALYEAR C*4 Civil year
  CPY CPY Company -> [CPY]CPY0 =[DV2]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DV2]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[DV2]CUR (TABCUR) !Block
  DEDDUT MD1 Deductible base
  DEDRAT DCB*3.6 Deductible %
  DEDVAT MD1 Input VAT
  EURCUR CUR EURO currency code -> [TCU]TCU0 =[DV2]EURCUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[DV2]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  PER C*2 Accounting period
  REGIVA A*3 VAT registry
  REGTYP A*1 Registry type
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DV2]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATPAY C*2 Invoice tax due
  VATRAT DCB*3.6 VAT rate

## DCLVATITA3 (DV3) - Annual italian VAT declaration
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): DV30 CPY+FCY+FIY+PER
Fields:
  AUUID AUUID Single identifier
  BASVAT MD1 Suspended tax base
  CALMONTH C*2 Calendar month
  CALYEAR C*4 Civil year
  CPY CPY Company -> [CPY]CPY0 =[DV3]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DV3]CREUSR (AUTILIS) !Other
  EURBASVAT MD1 Suspended euro tax base
  EURSPSVAT MD1 Suspended euro tax
  EURVATCRE MD1 EURO VAT credit
  EURVATDEB MD1 EURO VAT debit
  FCY FCY Site -> [FCY]FCY0 =[DV3]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  PER C*2 Accounting period
  SPSVAT MD1 Suspended tax
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DV3]UPDUSR (AUTILIS) !Other
  VATCRE MD1 VAT credit
  VATDEB MD1 VAT debit

## DCLVATPAY (DVP) - Tax declaration / collection
Keys (first = PK; D = duplicates allowed): DVP0 CPY+FCY+STRDAT+ACC+BPR+MTC+VATRAT+ACCNUM (D); DVP1 ACC+BPR+MTC+VATRAT+ACCNUM+NUMRPT
Fields:
  ACC GAC Accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCNUM UNQ Internal number
  AMTVATPAY MD1 Tax amount on collection
  AMTVCR MD1 Payment amount
  AUUID AUUID Single identifier
  BASVATPAY MD1 Tax base on collection
  BPR BPR BP -> [BPR]BPR0 =[DVP]BPR (BPARTNER) !Block
  COA COA Chart code -> [COA]COA0 =[DVP]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[DVP]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DVP]CREUSR (AUTILIS) !Other
  DATMAX D Journal date
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[DVP]FCY (FACILITY) !Block
  MTC A*5 Matching
  MTCDAT D Matching date
  NUMRPT L*8 Query no.
  OPT M*25 Option [menu 688: 1=VAT/debit allocated first,2=Pro rata]
  SIM M*4 Simulation [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  TOTAMTATI MD1 Total including tax
  TOTAMTVAT MD1 Tax total
  TYPREC C*1 Record type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DVP]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VATRAT A*15 Tax

## DCLVATPORB (DVPB) - VAT base information
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): DVPB0 DCLNUM+RECTYP+NUM+LIN+DCLFLD+DCLPAG; DVPB1 DCLNUM+DCLFLD+EECNUM (D); DVPB2 DCLNUM+EECNUM (D); DVPB3 DCLNUM+DCLFLD+EXPIMPVCR+EECNUM (D)
Fields:
  ACC A*20 Account
  ACCDAT D Accounting date
  AMTBAS MD1 Basis amt for calculation
  AMTVAT MD1 Tax amount
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[DVPB]BPRNUM (BPARTNER) !BSRA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM A*8 Time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[DVPB]CRY (TABCOUNTRY) !Block
  DCLFLD A*3 Declaration field
  DCLFLDTYP C*2 Amount type
  DCLNUM VCR Declaration
  DCLPAG M*15 Annex [menu 3618: 1=Main,2=Annex R-1,3=Annex R-2]
  DCLTYP M*12 Type [menu 2643: 1=Periodic,2=Annual,3=Recapitulative,4=European services]
  EECNUM EEC EU identification
  EXPIMPVCR A*20 Document no.
  FLD40REN ADI Field 40 - reason -> [ADI]CODE =8300;FLD40REN (ATABDIV) !Block
  FLD41REN ADI Field 41 - reason -> [ADI]CODE =8301;FLD41REN (ATABDIV) !Block
  LIN L*8 Line
  NUM VCR Document no.
  OPETYP C*2 Operation type
  RECTYP C*4 Record type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM A*8 Modification time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## DCLVATPORF (DVPF) - VAT declaration fields
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): DVPF0 DCLNUM+DCLPAG+DCLFLD
Fields:
  AMT DCB*11.2 Amount
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DVPF]CREUSR (AUTILIS) !Other
  DCLFLD A*5 Declaration field
  DCLNUM VCR Declaration
  DCLPAG M*15 Annex [menu 3618: 1=Main,2=Annex R-1,3=Annex R-2]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DVPF]UPDUSR (AUTILIS) !Other

## DCLVATPORH (DVPH) - VAT declaration
Notes: activity code KPO; differs in V9.0 P12 (diff: AT3_DCLVATPORH.htm); differs in V10 P1 (diff: ATD_DCLVATPORH.htm)
Keys (first = PK; D = duplicates allowed): DVPH0 DCLNUM
Fields:
  AMTSBS M*22 Total amount substitution [menu 1: 1=No,2=Yes]
  AN1LOC M*15 Fiscal area - annex R1 [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  AN2LOC M*15 Fiscal area - annex R2 [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  ANXI A*20 Annex I
  ANXPER1 A*20 Annex period 1
  ANXPER2 A*20 Annex period 2
  ANXPER3 A*20 Annex period 3
  AUTBAL M*26 VAT return [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPCFLG M*4 Customers [menu 1: 1=No,2=Yes]
  BPSFLG M*4 Suppliers [menu 1: 1=No,2=Yes]
  CHGPER M*15 Periodicity change [menu 663: 1=No,2=Yes,3=Unspecified]
  CPY CPY Company -> [CPY]CPY0 =[DVPH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DVPH]CREUSR (AUTILIS) !Other
  DCLMON M*20 Monthly [menu 9001: 1=January,2=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December]
  DCLNUM VCR Declaration
  DCLQUA M*20 Quarterly [menu 2222: 1=1st quarter,2=2nd quarter,3=3rd quarter,4=4th quarter]
  DCLTYP M*12 Type [menu 2643: 1=Periodic,2=Annual,3=Recapitulative,4=European services]
  DCLYEA C*4 Year
  ENDDAT D End date
  FAN1LINCOUNT L*8 Lines
  FAN1OPE C*2 Annex period 1
  FAN2LINCOUNT L*8 Lines
  FAN2OPE C*2 Annex period 2
  FAN3LINCOUNT L*8 Lines
  FAN3OPE C*2 Annex period 3
  FAN40LINCONT L*8 Lines
  FAN41LINCONT L*8
  FIRDCL M*20 First declaration [menu 1: 1=No,2=Yes]
  FLDAN102 DCB*11.2 Annex I field 02
  FLDAN104 DCB*11.2 Annex I field 04
  FLDAN105 DCB*11.2 Annex I field 05
  FLDAN106 DCB*11.2 Annex I field 06
  FLDAN206B DCB*11.2 Annex II field 06B
  FLDAN206V DCB*11.2 Annex II field 06V
  FLDAN207B DCB*11.2 Annex II field 07B
  FLDAN207V DCB*11.2 Annex II field 07V
  FLDAN22006B DCB*11.2 Annex II field 06B
  FLDAN22006V DCB*11.2 Annex II field 06V
  FLDAN22106B DCB*11.2 Annex II field 06B
  FLDAN22106V DCB*11.2 Annex II field 06V
  FLDAN22206B DCB*11.2 Annex II field 06B
  FLDAN22206V DCB*11.2 Annex II field 06V
  FLDAN22306B DCB*11.2 Annex II field 06B
  FLDAN22306V DCB*11.2 Annex II field 06V
  FLDAN22406B DCB*11.2 Annex II field 06B
  FLDAN22406V DCB*11.2 Annex II field 06V
  FLDAN302 DCB*11.2 Annex III field 02
  FLDAN303 DCB*11.2 Annex III field 03
  FLDAN304 DCB*11.2 Annex III field 04
  FLDAN305 DCB*11.2 Annex III field 05
  FLDAN306 DCB*11.2 Annex III field 06
  FLDAN307 DCB*11.2 Annex III field 07
  FLDAN308 DCB*11.2 Annex III field 08
  FLDAN309 DCB*11.2 Annex III field 09
  FLDAN4003 DCB*11.2 Annex 40 field 3
  FLDAN4003A DCB*11.2 Annex 40 field 3A
  FLDAN4003B DCB*11.2 Annex 40 field 3B
  FLDAN4004 DCB*11.2 Annex 40 field 4
  FLDAN4004A DCB*11.2 Annex 40 field 4A
  FLDAN4004B DCB*11.2 Annex 40 field 4B
  FLDAN4103A DCB*11.2 Annex 41 field 3A
  FLDAN4103B DCB*11.2 Annex 41 field 3B
  FLDAN4103C DCB*11.2 Annex 41 field 3A
  FLDAN4103D DCB*11.2 Annex 41 field 3A
  FLDAN4104A DCB*11.2 Annex 41 field 4A
  FLDAN4104B DCB*11.2 Annex 41 field 4B
  FLDAN4104C DCB*11.2 Annex 41 field 3A
  FLDAN4104D DCB*11.2 Annex 41 field 3A
  FPERIOD A*3 Period
  FRECAP_UE C*4 Annex I
  FTIPENT C*2 Type
  HQRLOC M*15 Hqr fiscal area [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  LASDCL M*20 Last [menu 1: 1=No,2=Yes]
  MULEECNUMPUR C*2 Multi EECNUM
  NOOPER M*4 No [menu 1: 1=No,2=Yes]
  ONTIMDCL M*10 On time [menu 1: 1=No,2=Yes]
  OTHERS M*4 Others [menu 1: 1=No,2=Yes]
  PERCHG M*20 Periodicity change [menu 1: 1=No,2=Yes]
  PREVDEC M*4 Amount change? [menu 1: 1=No,2=Yes]
  REGENDDAT D End date
  REGFLG M*4 Adjustments [menu 1: 1=No,2=Yes]
  REGSTRDAT D Reference date
  RENSBS ADI Substitution reason -> [ADI]CODE =396;RENSBS (ATABDIV) !Block
  SBSDCL M*10 Substitution dec [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DVPH]UPDUSR (AUTILIS) !Other

## DCLVATPORL (DVPL) - VAT declaration lines
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): DVPL0 DCLNUM+LINTYP+LSTLIN
Fields:
  AMTBAS DCB*11.2 Base
  AMTVAT DCB*11.2 VAT amount
  AUUID AUUID Single identifier
  BPRNUM BPR BP code -> [BPR]BPR0 =[DVPL]BPRNUM (BPARTNER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DVPL]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[DVPL]CRY (TABCOUNTRY) !Block
  DCLNUM VCR Declaration
  EECNUM EEC EU identification
  FLD40REN ADI Field 40 - reason -> [ADI]CODE =8300;FLD40REN (ATABDIV) !Block
  FLD41REN ADI Field 41 - reason -> [ADI]CODE =8301;FLD41REN (ATABDIV) !Block
  LINTYP C*4 Line type
  LSTLIN C*4 Line
  MON C*2 Month
  OPETYP M*15 Operation type [menu 638: 1=Not included on type 4,2=Not used,3=Not used,4=Triangular operations,5=Services]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DVPL]UPDUSR (AUTILIS) !Other
  VCRNUM A*30 Document
  YEA C*4 Year

## DCLVATPORP (DVPP) - VAT parameters
Notes: activity code KPO; differs in V10 P1 (diff: ATD_DCLVATPORP.htm)
Keys (first = PK; D = duplicates allowed): DVPP0 CPY+YEA
Fields:
  AN1LOC M*15 Fiscal area - annex R1 [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  AN2LOC M*15 Fiscal area - annex R2 [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  AUUID AUUID Single identifier
  BANACCROT A*15 Bank account
  BPCDISROT A*15 Customer financial discount
  BPSDISROT A*15 Supplier financial discount
  CPY CPY Company -> [CPY]CPY0 =[DVPP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[DVPP]CREUSR (AUTILIS) !Other
  CURRAT DCB*5.4 Currency rate
  HQRLOC M*15 Hqr fiscal area [menu 2274: 1=Mainland,2=Azores,3=Madeira,4=Non applicable]
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  MAXAMTPURA DCB*12.2 Purchasing cap
  MAXAMTPURP DCB*12.2 Purchasing cap
  MAXAMTSALA DCB*12.2 Sales cap
  MAXAMTSALP DCB*12.2 Sales cap
  MAXAMTSTLP DCB*12.2 Adjustments cap
  RCAEXNROT1 A*15 Recap account exception 1
  RCAEXNROT2 A*15 Recap account exception 2
  RCAEXNROT3 A*15 Recap account exception 3
  RCAEXNROT4 A*15 Recap account exception 4
  SALGOOROT A*15 Good sales
  SALIMOLESROT A*15 Fixed assets sales -
  SALIMOPLUROT A*15 Fixed assets sales +
  SALSRVROT A*15 Service sales
  TAXCDTREC M*15 Tax credit recovery [menu 3682: 1=None,2=Request reimbursement,3=Carry-forward excess]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[DVPP]UPDUSR (AUTILIS) !Other
  VATTPAROT A*15 VAT to pay
  VATTREROT A*15 VAT to receive
  YEA C*4 Year

## DCLVATPORT (DVPT) - Taxes
Notes: activity code KPO; differs in V9.0 P12 (diff: AT3_DCLVATPORT.htm)
Keys (first = PK; D = duplicates allowed): DVPT0 DCLTYP+DCLPAG+DCLFLD+CPY+VAT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[DVPT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DVPT]CREUSR (AUTILIS) !Other
  DCLFLD A*3 Declaration field
  DCLPAG M*15 Annex [menu 3618: 1=Main,2=Annex R-1,3=Annex R-2]
  DCLTYP M*12 Type [menu 2643: 1=Periodic,2=Annual,3=Recapitulative,4=European services]
  DES DES Description
  GOODAQU M*20 Good purchase [menu 1: 1=No,2=Yes]
  SERVAQU M*20 Service purchase [menu 1: 1=No,2=Yes]
  TRIOPE M*20 Triangular operation [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DVPT]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## DCLVATSPA (DVS) - Tax working table (SPA)
Notes: activity code KSP; differs in V9.0 P12 (diff: AT3_DCLVATSPA.htm)
Keys (first = PK; D = duplicates allowed): DVS0 TAXTYP+TYP+NUM+VAT+REGTYP; DVS1 CRN (D); DVS2 EECNUM (D); DVS3 TAXTYP+DCLDAT (D); DVS4 INDLNK (D); DVS5 TAXTYP+CRN+TYP+NUM (D); DVS6 COD347+CRN (D); DVS7 ACCNUM (D)
Fields:
  ACCDAT D Accounting date
  ACCNUM L*8 Internal number
  AMTATI MD1 Amount + tax
  AMTATIL MD1 Invoice amt. + tax (co)
  AMTNOT MD1 Amount - tax
  AMTNOTL MD1 Amount - tax (co)
  AMTTAX MD1 Tax amount
  AMTTAXL MD1 Tax amount (company)
  AUUID AUUID Single identifier
  BIDNUM A*32 Bank account number
  BOOKFLG M*4 Include in book [menu 1: 1=No,2=Yes]
  BPRDAT D Source date
  BPRNAM NAM(2) Company name
  BPRNUM BPR BP code -> [BPR]BPR0 =BPRNUM (BPARTNER) !Block
  BPRVCR A*20 Source document
  BUILOC M*12 Location [menu 3611: 1=Located on national territory,2=Located in Basque Country or Navarre,3=Without cadastre reference,4=Located abroad]
  CDRREF A*25 Cadastre
  CEEFLG M*4 EU invoice [menu 1: 1=No,2=Yes]
  COD347 A*3 Code 347
  CODOPE ADI Operation code -> [ADI]CODE =393;CODOPE (ATABDIV) !Block
  CPY CPY Company -> [CPY]CPY0 =[DVS]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DVS]CREUSR (AUTILIS) !Other
  CRN CRN Site tax ID no.
  CRY CRY Country -> [TCY]TCY0 =[DVS]CRY (TABCOUNTRY) !Block
  CSHVAT M*4 Cash VAT tax rule [menu 1: 1=No,2=Yes]
  CUR CUR Currency -> [TCU]TCU0 =[DVS]CUR (TABCUR) !Block
  D347FLG M*4 Declaration 347 [menu 1: 1=No,2=Yes]
  D349FLG M*4 Declaration 349 [menu 1: 1=No,2=Yes]
  DCLDAT D Declaration date
  DECCUR DCB*9.2 Declared tax
  DEDAMT MD1 Deductible amount
  DEDAMTL MD1 Deductible amt local
  DEDRAT DCB*3.6 Deductible %
  DOCTYP M*4 Document type [menu 2004: 1=Site tax ID number,2=Intracommunity tax ID number,3=Passport,4=Official document,5=Fiscal residence certificate,6=Others]
  EECNUM EEC EU identification
  ENFDAT D Enforceability date
  EURSRV M*4 Services [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[DVS]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  IGICFLG M*4 IGIC [menu 1: 1=No,2=Yes]
  IMPORT M*4 Import [menu 1: 1=No,2=Yes]
  INDLNK A*50 Index link
  INR M*4 Interest [menu 1: 1=No,2=Yes]
  INVFLG M*4 Invoice [menu 1: 1=No,2=Yes]
  INVNUM VCR Invoice number
  INVNUMDAT D Source date
  INVTYP M*4 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  INVUPDFLG M*4 Modif flag [menu 1: 1=No,2=Yes]
  NRS M*4 Nonresident [menu 1: 1=No,2=Yes]
  NUM VCR Document no.
  ORIMOD M*4 Source module [menu 14: 20 values, see local-menus.md]
  PAM ADI Tax rule type -> [ADI]CODE =990;PAM (ATABDIV) !Block
  PAYCUR DCB*9.2 Paid amount
  PER C*2 Period
  POSCOD POS Postal code
  PROFLG M*4 Processing flag [menu 1: 1=No,2=Yes]
  QUARTER C*2 Quarter
  REGTYP C*2 Tax rule type
  REVSAL M*4 Sales reverse charge [menu 1: 1=No,2=Yes]
  RNT M*4 Rental [menu 1: 1=No,2=Yes]
  SCDREF A*40 SCD reference
  SNS C*2 Sign
  SPADERNUM A*60 DER code
  TAG M*4 Purchase travel agency [menu 1: 1=No,2=Yes]
  TAXTYP A*4 Tax type
  TCKEND A*15 End ticket
  TCKINI A*15 Initial ticket
  TCKNUM L*8 Number of tickets
  TOTALPAY M*4 Paid [menu 1: 1=No,2=Yes]
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DVS]UPDUSR (AUTILIS) !Other
  VAC TVB Tax rule -> [TVB]TVB0 =VAC;[V]GSUPCLE (TABVACBPR) !Block
  VACAGR M*4 Agrarian tax rule [menu 1: 1=No,2=Yes]
  VAT VAT Tax -> [TVT]TVT0 =VAT;LEG (TABVAT) !Block
  VATRAT DCB*3.2 Rate
  VATTYP M*4 VAT type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]

## DUDLNK (DLN) - Open item links
Notes: activity code KIT
Keys (first = PK; D = duplicates allowed): DLN0 NUM; DLN1 NUMDUD1+NUMDUD2 (D); DLN2 NUMDUD2 (D)
Fields:
  AMTCUR MD1 Amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DLN]BPR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[DLN]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DLN]CREUSR (AUTILIS) !Other
  DAT D Date created
  NUM L*8 Sequence no.
  NUMDUD1 A*15 Due date
  NUMDUD2 A*15 Due date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DLN]UPDUSR (AUTILIS) !Other

## EDTDADSU (EDU) - DADSU file print
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): EDU0 REFSND (D); EDU1 REFSND+NUMLIN; EDU2 GRP (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EDU]CREUSR (AUTILIS) !Other
  GRP A*10 Group
  NUMLIN C*4 Line
  NUMREC A*20 Record no.
  REFSND A*10 Query number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EDU]UPDUSR (AUTILIS) !Other
  VALDADS A*250 Value

## EDTTDS (ETD) - TDS file report
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): ETD0 SIREN+CRN+RECTYP+NUMLIN+NUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ETD]CREUSR (AUTILIS) !Other
  CRN CRT Site tax ID no.
  DES DES Description
  NUM C*2 Order no.
  NUMLIN C*4 Line
  RECTYP M*15 Record type [menu 696: 1=Start flag,2=Company header,3=Site header,4=Fee lines,5=Declaration site total +,6=Company total +,7=End flag]
  SIREN A*9 Company tax ID no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ETD]UPDUSR (AUTILIS) !Other
  VALTDS A*100 Value

## ENTITE (ENT) - Entity
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): ENT0 ENT
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ENT]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[ENT]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  DESTRA AX3 Description
  DIE DIE Dimension codes -> [DIE]DIE0 =[ENT]DIE (GDIE) !Block act:ANA
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENT ENT Entity -> [ENT]ENT0 =[ENT]ENT (ENTITE) !Delete
  ENTAPP ENT Approval entity -> [ENT]ENT0 =[ENT]ENTAPP (ENTITE) !Other
  ENTFLG M*15 Budget entity [menu 1: 1=No,2=Yes]
  ENTRAT ENT Reporting entity -> [ENT]ENT0 =[ENT]ENTRAT (ENTITE) !Block
  EXPNUM L*8 Export number
  LEV C*1 Level
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author
  USR AUS Supervisor -> [AUS]CODUSR =[ENT]USR (AUTILIS) !Other
  VLYEND D Validity end date
  VLYSTR D Validity start date

## ENVELOPPE (ENV) - Envelope
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): ENV0 ENV
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ENV]ACS (ACCCOD) !Block
  AMTAPP MD1 Approved amount
  AMTENV MD1 Envelope amount
  AMTFIN MD0(10) Financed amount
  AMTPRV MD0(10) Projected amount
  AMTRES MD1 Reserve amount
  APPDAT D Approval date
  AUUID AUUID Single identifier
  BPRFIN BPR(10) BP -> [BPR]BPR0 =[ENV]BPRFIN (BPARTNER) !Block
  BUD BUP Budget -> [BUP]BUP0 =[ENV]BUD (BUDPAR) !Block
  BUDTYP BUT Budget type -> [BUT]BUT0 =[ENV]BUDTYP (BUDTYP) !Block act:GDD
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  CURENV CUR Currency -> [TCU]TCU0 =[ENV]CURENV (TABCUR) !Block
  DESTRA AX3 Description
  DRECOND D Date
  ENTAPP ENT Approval entity -> [ENT]ENT0 =[ENV]ENTAPP (ENTITE) !Block
  ENTMNA ENT Responsible entity -> [ENT]ENT0 =[ENV]ENTMNA (ENTITE) !Block act:GDD
  ENTRAT ENT Reporting entity -> [ENT]ENT0 =[ENV]ENTRAT (ENTITE) !Block
  ENV ENV Envelope -> [ENV]ENV0 =[ENV]ENV (ENVELOPPE) !Delete act:GDD
  ENVORG ENV Original envelope -> [ENV]ENV0 =[ENV]ENVORG (ENVELOPPE) !Block act:GDD
  ENVRCD ENV Renewed envelope -> [ENV]ENV0 =[ENV]ENVRCD (ENVELOPPE) !Block act:GDD
  EXDPRC DCB*2.2 Overflow control
  EXPNUM L*8 Export number
  EXTBUD M*4 Off-budget [menu 1: 1=No,2=Yes]
  FCY CFY Company/Site
  OBS ACB Notes
  PEREND D(10) End
  PERSTR D(10) Start
  PRJ PRJ Project -> [PRJ]PRJ0 =[ENV]PRJ (PROJET) !Block
  REAEND D Completion end
  REASTR D Completion start
  RECOND M*4 Renewable [menu 1: 1=No,2=Yes]
  REVDAT D Latest review date
  SHOTRA AX1 Short description
  SOCIETE CPY Company -> [CPY]CPY0 =[ENV]SOCIETE (COMPANY) !Delete
  STA M*4 Envelope status [menu 2691: 1=Entered,2=To be approved,3=Approved,4=Closed,5=Commitments carried forward]
  TSI ADI Statistical group -> [ADI]CODE =indice+341;TSI(indice) (ATABDIV) !Block act:STB
  TYP AT Document type
  TYPREC M*2 Renewal type [menu 2688: 1=Normal,2=Commitment carried forward]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## ENVFIY (ENF) - Distribute envelope/fiscal year
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): ENF0 ENV+FIYNUM; ENF1 ENV (D)
Fields:
  AMTAPPFIY MD1 Approved amount
  AMTBUDFIY MD1 Initial amount
  AMTRESFIY MD1 Reserve amount
  APPDATFIY D Approval date
  AUUID AUUID Single identifier
  BUDRPT MDC Budget postponement
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ENF]CREUSR (AUTILIS) !Other
  ENV ENV Envelope -> [ENV]ENV0 =[ENF]ENV (ENVELOPPE) !Block act:GDD
  FIYEND D End
  FIYNUM C*2 Fiscal year
  FIYSTR D Start
  REVDATFIY D Latest review date
  STAFIY M*4 Status [menu 2691: 1=Entered,2=To be approved,3=Approved,4=Closed,5=Commitments carried forward]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ENF]UPDUSR (AUTILIS) !Other

## EURSRVDCL (ESH) - European services declaration
Notes: activity code ESD
Keys (first = PK; D = duplicates allowed): ESH0 CPY+ENDDAT+BPR+EECNUM; ESH1 CPY+STRDAT+ENDDAT+EECNUM+BPR
Fields:
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BPs -> [BPR]BPR0 =[ESH]BPR (BPARTNER) !Block
  BPRNAM NAM(2) Company name
  CPY CPY Company -> [CPY]CPY0 =[ESH]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESH]CREUSR (AUTILIS) !Other
  CURLED CUR Ledger currency -> [TCU]TCU0 =[ESH]CURLED (TABCUR) !Block
  EECNUM A*20 EU identification act:DEB
  ENDDAT D End date
  NUMRPT L*8 Query no.
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESH]UPDUSR (AUTILIS) !Other

## EURSRVDCLD (ESD) - European services declaration
Notes: activity code ESD
Keys (first = PK; D = duplicates allowed): ESD0 CPY+ENDDAT+BPR+EECNUM+ACCNUM
Fields:
  ACC GAC General accounts -> [GAC]GAC0 ="";ACC (GACCOUNT) !Other
  ACCDAT D Accounting date
  ACCNUM L*8 Internal number
  ACCNUMBPR L*8 Internal number
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BPs -> [BPR]BPR0 =[ESD]BPR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[ESD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ESD]CREUSR (AUTILIS) !Other
  CURLED CUR Ledger currency -> [TCU]TCU0 =[ESD]CURLED (TABCUR) !Block
  DESVCR DES Description
  EECNUM A*20 EU identification act:DEB
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[ESD]FCY (FACILITY) !Block
  FLG M*15 Type [menu 2652: 1=Entered line,2=Extracted line]
  LIG C*3 Line number
  NUM VCR Document no.
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  SNS C*2 Sign
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ESD]UPDUSR (AUTILIS) !Other

## FAEPAR (FAE) - ACCENTFIL setup
Notes: activity code KFR
Keys (first = PK; D = duplicates allowed): FAE0 IDT
Fields:
  AUUID AUUID Single identifier
  CODPVT PIT Pivot -> [PIT]PIT0 =CODPVT (PIVOTS) !Block
  CPY CPY Company -> [CPY]CPY0 =[FAE]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[FAE]CREUSR (AUTILIS) !Block
  DES DES Description
  FIYPER M*15 FY/Period [menu 3639: 1=Full fiscal year,2=Period]
  IDT A*10 Identifier
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[FAE]UPDUSR (AUTILIS) !Block
  VOLFIL ASTO*250 Directory

## FILTDS (FTD) - File structure DADS-U
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): FTD0 GRP+NUMREC; FTD1 GRP (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FTD]CREUSR (AUTILIS) !Other
  CTLLNG M*4 Length control [menu 1: 1=No,2=Yes]
  DES DES Description
  DESREC A*200 Description
  FILREF A*4 File prefix
  FLGREC M*15 Usage [menu 2656: 1=Mandatory,2=Conditional,3=Optional]
  GRP A*10 Group
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LNGREC C*3 Length
  NUMREC A*20 Record no.
  TYPREC M*15 Type [menu 2657: 1=Alphanumeric,2=Numeric,3=Date]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FTD]UPDUSR (AUTILIS) !Other
  VALNUL M*4 Zero accepted [menu 1: 1=No,2=Yes]
  XPSRES A*250 Expression

## GACCENTRY (HAE) - Accounting entries
Notes: differs in V9.0 P12 (diff: AT3_GACCENTRY.htm); differs in V10 P1 (diff: ATD_GACCENTRY.htm)
Keys (first = PK; D = duplicates allowed): HAE0 TYP+NUM; HAE1 JOU+ACCDAT+TYP+NUM; HAE2 REFSIM+TYP+NUM; HAE3 DACDIA+TYP-NUM; HAE4 ACCDAT+TYP+NUM; HAE5 REFINT (D)
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  BANCIB ADI Interbank code -> [ADI]CODE =306;BANCIB (ATABDIV) !Block
  BANDAT D Bank date act:KIT
  BOLLATO VCR Bollato sequence number act:KIT
  BPRDATVCR D Document date
  BPRVCR A*20 Source document
  CAT M*15 Category [menu 618: 1=Actual,2=Active simulation,3=Inactive simulation,4=Off-balance-sheet,5=Template]
  CPY CPY Company -> [CPY]CPY0 =[HAE]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Entry currency -> [TCU]TCU0 =[HAE]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[HAE]CURLED (TABCUR) !Block
  DACDIA GDE Transaction -> [GDE]DIA =[HAE]DACDIA (GDIAENTRY) !Block
  DESVCR DES Description
  DUDDAT D Due date
  ENTDAT D Entry date
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[HAE]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGDAS M*4 Fees declaration [menu 1: 1=No,2=Yes] act:FEE2
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGGEN M*4 Auto generation [menu 1: 1=No,2=Yes]
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  FLGREP M*4 Carryforward [menu 1: 1=No,2=Yes]
  FNLPSTDAT D Final date
  FNLPSTNUM VCR(10) Final number
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LED LED(10) Ledger -> [LED]LED0 =[HAE]LED (GLED) !Block
  NUM VCR Document no.
  NUMDCL L*8 Declaration number
  ORIGIN M*15 Source [menu 2801: 1=Direct entry,2=Automatic loading,3=Import]
  ORIMOD M*10 Source module [menu 14: 20 values, see local-menus.md]
  PER C*2 Period
  PJT PJT Project -> [PIM]PIM0 =[HAE]PJT (PIMPL) !Block act:PJM
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

## GACCENTRYA (DAA) - Analytical accounting line
Keys (first = PK; D = duplicates allowed): DAA0 TYP+NUM+LIN+LEDTYP+ANALIN; DAA1 CPY+FCYLIN+COA+ACC+BPR+ACCDAT+ACCNUM+ANALIN; DAA2 TYP+NUM+LIN+ANALIN+LEDTYP; DAA3 ACCNUMDOE+ACCNUM+ANALIN+CPY+FCYLIN+ACCDAT
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ Unique number
  ACCNUMDOE UNQ Counterpart number
  AMTCUR MD1 Entry amount
  AMTLED MD1 Ledger amount
  ANALIN C*3 Order information
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DAA]BPR (BPARTNER) !Block
  CCE CCE(9) Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block
  COA COA Chart code -> [COA]COA0 =[DAA]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[DAA]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DAA]CREUSR (AUTILIS) !Other
  CUR CUR Entry currency -> [TCU]TCU0 =[DAA]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[DAA]CURLED (TABCUR) !Block
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[DAA]DIE (GDIE) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[DAA]FCYLIN (FACILITY) !Block
  IDTLIN A*5 Identifier
  LED LED Ledger -> [LED]LED0 =[DAA]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  SNS C*2 Sign
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[DAA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DAA]UPDUSR (AUTILIS) !Other

## GACCENTRYD (DAE) - Accounting entry lines
Notes: differs in V9.0 P12 (diff: AT3_GACCENTRYD.htm); differs in V10 P1 (diff: ATD_GACCENTRYD.htm)
Keys (first = PK; D = duplicates allowed): DAE0 TYP+NUM+LIN+LEDTYP; DAE1 CPY+FCYLIN+LEDTYP+ACC+BPR+ACCDAT+ACCNUM; DAE2 ACCNUM; DAE3 LEDTYP+ACC+BPR+CPY+ACCDAT+ACCNUM; DAE4 LEDTYP+BPR+CPY+ACCDAT+ACCNUM; DAE5 CPY+FCYLIN+LEDTYP+BPR+ACCDAT+ACCNUM; DAE6 LEDTYP+ACC+BPR+MTC+TYP+NUM+LIN+ACCNUM; DAE7 TYP+NUM+IDTLIN+LEDTYP+LIN; DAE8 PJTLIN (D)
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ Unique number
  ACCNUMDOE UNQ Counterpart number act:KRU
  ACCNUMORI UNQ Source number
  AMTCUR MD1 Entry amount
  AMTFLG M*4 Forced amount [menu 1: 1=No,2=Yes]
  AMTLED MD1 Ledger amount
  AMTLED1 MD1 Forced amount
  AMTVAT MD1 Declared amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[DAE]BPR (BPARTNER) !Block
  CAPFLOTYP ADI Capital flow -> [ADI]CODE =389;CAPFLOTYP (ATABDIV) !Block act:KPO
  CHK A*5 Reconciliation
  CHKDAT D Reconciliation date
  CHRNUM VCR Chronological number
  COA COA Chart code -> [COA]COA0 =[DAE]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[DAE]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DAE]CREUSR (AUTILIS) !Other
  CSLBPR BPR Partner -> [BPR]BPR0 =[DAE]CSLBPR (BPARTNER) !Block act:PRCSL
  CSLCOD A*10 Partner act:CSL
  CSLFLO ADI Flow -> [ADI]CODE =324;CSLFLO (ATABDIV) !Block act:CSL1
  CUR CUR Entry currency -> [TCU]TCU0 =[DAE]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[DAE]CURLED (TABCUR) !Block
  DES DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  EXPNUM L*8 Export number
  FCYLIN FCY Site -> [FCY]FCY0 =[DAE]FCYLIN (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGMTC M*4 Flag [menu 1: 1=No,2=Yes]
  FREREF REF Free reference
  IDTLIN A*5 Identifier
  INDEDVAT MD1 Non-deductible tax act:KIT
  LED LED Ledger -> [LED]LED0 =[DAE]LED (GLED) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  MRK A*20 Marking
  MTC A*5 Matching
  MTCDAT D Matching date
  MTCDATMAX D Maximum group date
  MTCDATMIN D Minimum group date
  NUM VCR Document no.
  OFFACC A*15 Offset
  PER C*2 Period
  PJTLIN PJT Project -> [PIM]PIM0 =[DAE]PJTLIN (PIMPL) !Block act:PJM
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
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[DAE]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DAE]UPDUSR (AUTILIS) !Other
  VATDEDRAT DCB*3.6 Deductib pro rata
  VATRAT DCB*3.6 Applied VAT rate

## GACCFIX (GAF) - Recurring entries
Keys (first = PK; D = duplicates allowed): GAF0 COD
Fields:
  AMT MD1 Amount
  AMTCUM MD1 Total amount
  AUUID AUUID Single identifier
  COD GAF Recurring entry -> [GAF]GAF0 =[GAF]COD (GACCFIX) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[GAF]CUR (TABCUR) !Block
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DSPTMP DTP Distribution -> [DTP]DTP0 =[GAF]DSPTMP (CADISTMP) !Block
  DUDDAT PTE Due date -> [TPT]TPT0 =DUDDAT;[V]GCURLEG;1 (TABPAYTERM) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENDDAT D End date
  EXPNUM L*8 Export number
  FORDES AFR*80 Description
  FORREF AFR*80 Reference
  JOU1 JOU Journal -> [JOU]JOU0 =JOU1;[V]GSUPCLE (GJOURNAL) !Block
  JOU2 JOU Journal -> [JOU]JOU0 =JOU2;[V]GSUPCLE (GJOURNAL) !Block
  LASDAT D(2) Last journal
  LASNUM VCR(2) Last journal
  LASTYP GTE(2) Last journal -> [GTE]GTE0 =LASTYP;[V]GSUPCLE (GTYPACCENT) !Block
  PERNBR C*4 Frequency
  PERTYP M*15 Periodicity [menu 635: 1=Days,2=Week,3=10-day period,4=2-week period,5=Month]
  REFNUM VCR Template journal no.
  REFTYP GTE Template entry type -> [GTE]GTE0 =REFTYP;[V]GSUPCLE (GTYPACCENT) !Block
  RVSDAT D Reversal date
  SHOTRA AX1 Short description
  STRDAT D Start date
  TYP M*15 Type [menu 640: 1=Fixed,2=Variable]
  TYP1 GTE Entry type -> [GTE]GTE0 =TYP1;[V]GSUPCLE (GTYPACCENT) !Block
  TYP2 GTE Entry type -> [GTE]GTE0 =TYP2;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GACCFIYENA (FYA) - C/fwd. temporary file
Keys (first = PK; D = duplicates allowed): FYA0 CUR+CPY+LEDTYP+FCY+GRP+ACC+BPR+LIG+ANALIG; FYA1 FCY+CPY+LEDTYP+CUR+GRP+ACC+BPR+LIG+ANALIG
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Local currency amount
  ANALIG L*8 Order information
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[FYA]BPR (BPARTNER) !Delete
  CCE CCE(9) Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Delete
  COA COA Chart code -> [COA]COA0 =[FYA]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[FYA]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FYA]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[FYA]CUR (TABCUR) !Delete
  CURLED CUR Ledger currency -> [TCU]TCU0 =[FYA]CURLED (TABCUR) !Delete
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[FYA]DIE (GDIE) !Delete
  FCY FCY Site -> [FCY]FCY0 =[FYA]FCY (FACILITY) !Delete
  GRP C*4 Group
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIG C*3 Line number
  QTY QTY Quantity
  UOM UOM Unit -> [TUN]TUN0 =[FYA]UOM (TABUNIT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FYA]UPDUSR (AUTILIS) !Other

## GACCFIYEND (FYD) - C/fwd. temporary file
Keys (first = PK; D = duplicates allowed): FYD0 CUR+CPY+LEDTYP+FCY+GRP+ACC+BPR+LIG; FYD1 FCY+CPY+LEDTYP+CUR+GRP+ACC+BPR+LIG
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCDAT D Accounting date
  ACCRES GAC Retained earnings account -> [GAC]GAC0 =COA;ACCRES (GACCOUNT) !Delete
  AMTAUT MD1(10) Automatic amounts
  AMTCUR MD1 Amount in currency
  AMTLOC MD1 Local currency amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[FYD]BPR (BPARTNER) !Delete
  COA COA Chart code -> [COA]COA0 =[FYD]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[FYD]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FYD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[FYD]CUR (TABCUR) !Delete
  CURLED CUR Ledger currency -> [TCU]TCU0 =[FYD]CURLED (TABCUR) !Delete
  FCY FCY Site -> [FCY]FCY0 =[FYD]FCY (FACILITY) !Delete
  GRP C*4 Group
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIG C*3 Line number
  QTY QTY Quantity
  RESACE M*4 Result [menu 1: 1=No,2=Yes]
  UOM UOM Unit -> [TUN]TUN0 =[FYD]UOM (TABUNIT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FYD]UPDUSR (AUTILIS) !Other

## GACCINTCPY (GIC) - Intercompany journal entry
Notes: activity code INTCO
Keys (first = PK; D = duplicates allowed): GIC0 NUM
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[GIC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  CUR CUR Entry currency -> [TCU]TCU0 =[GIC]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[GIC]CURLED (TABCUR) !Block
  DESNUM DES Description
  FCY FCY Site -> [FCY]FCY0 =[GIC]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  FLGPST M*15 Status [menu 2806: 1=Not posted,2=Posted simulation,3=Posted actual]
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LED LED(10) Ledger -> [LED]LED0 =[GIC]LED (GLED) !Block
  NBRCPY C*2 Number of companies
  NUM VCR Number
  PER C*2 Period
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## GACCINTCPYA (GIA) - Intercompany journal ana lines
Notes: activity code INTCO
Keys (first = PK; D = duplicates allowed): GIA0 NUM+LIN+ANALIN
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTCUR MD1 Amount in currency
  ANALIN C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[GIA]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GIA]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[GIA]DIE (GDIE) !Block act:ANA
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[GIA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GIA]UPDUSR (AUTILIS) !Other

## GACCINTCPYD (GID) - Intercompany journal ent lines
Notes: activity code INTCO
Keys (first = PK; D = duplicates allowed): GID0 NUM+LIN
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTCUR MD1 Entry amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[GID]BPR (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[GID]COA (GCOA) !Block
  CPYLIN CPY Company -> [CPY]CPY0 =[GID]CPYLIN (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GID]CREUSR (AUTILIS) !Other
  CURLIN CUR Entry currency -> [TCU]TCU0 =[GID]CURLIN (TABCUR) !Block
  DES DES Description
  DOCNUMLIN VCR Document number
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[GID]FCYLIN (FACILITY) !Block
  JOULIN JOU Journal code -> [JOU]JOU0 =JOULIN; [V]GSUPCLE (GJOURNAL) !Block
  LED LED(10) Ledger -> [LED]LED0 =[GID]LED (GLED) !Block
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  SAC SAC(10) Control
  SNS C*2 Sign
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  TYPLIN GTE Entry type -> [GTE]GTE0 =TYPLIN;[V]GSUPCLE (GTYPACCENT) !Block
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[GID]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GID]UPDUSR (AUTILIS) !Other

## GACCPYMLIK (GYK) - Account pyramid links
Keys (first = PK; D = duplicates allowed): GYK0 PYM+LEV+ACC
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[GYK]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GYK]CREUSR (AUTILIS) !Other
  GRU GRY Group code -> [GRY]GRY0 =PYM;GRU;1 (GACCGRUPYM) !Delete
  LEV C*2 Level
  PRNROW C*4 Print row
  PYM GYM Pyramid code -> [GYM]GYM0 =[GYK]PYM (GACCPYM) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GYK]UPDUSR (AUTILIS) !Other

## GACCPYMPRT (GYP) - Print pyramids
Keys (first = PK; D = duplicates allowed): GYP0 COA+PYM+ACC
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[GYP]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GYP]CREUSR (AUTILIS) !Other
  GRU GRY(10) Group code -> [GRY]GRY0 =PYM;GRU(indice);1 (GACCGRUPYM) !Delete
  LEV C*2 Level
  LIE C*2 Link
  PYM GYM Pyramid code -> [GYM]GYM0 =[GYP]PYM (GACCPYM) !Delete
  ROW C*4(10) Row
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GYP]UPDUSR (AUTILIS) !Other

## GAJOUSTA (JST) - Journals - reports per period
Keys (first = PK; D = duplicates allowed): JST0 CPY+JOU
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[JST]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  JOU JOU Journal -> [JOU]JOU0 =JOU;"" (GJOURNAL) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  OPGENDDAT D Opening end date
  OPGSTRDAT D Opening start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GAPARBSE (PBS) - Default reporting codes
Keys (first = PK; D = duplicates allowed): PBS0 COA+NUMCOD+ACCSTR
Fields:
  ACCSTR A*15 Account root
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[PBS]COA (GCOA) !Delete
  CODCDT A*10 Creditor code
  CODDEB A*10 Debtor code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  NUMCOD C*2 Code number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GAPARDUM (PDM) - Account balance transfer
Keys (first = PK; D = duplicates allowed): PDM0 COA+COD+NUMLIN; PDM1 COA+COD (D)
Fields:
  ACCCDT GAC Credited account -> [GAC]GAC0 =COA;ACCCDT (GACCOUNT) !Block
  ACCDEB GAC Debited account -> [GAC]GAC0 =COA;ACCDEB (GACCOUNT) !Block
  ACCSTR A*15 Account root
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[PDM]COA (GCOA) !Block
  COD A*5 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  NUMLIN C*1 Line number
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## GBAGSCR (GBS) - Aged balance screen
Keys (first = PK; D = duplicates allowed): GBS0 FLGHIS+COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GBS]ACS (ACCCOD) !Block
  AFFGRA M*15(2) Default display [menu 2936: 1=Table,2=Graph]
  AUUID AUUID Single identifier
  CMT M*4 Display comment [menu 1: 1=No,2=Yes]
  COD A*5 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CURFLG M*15 Currency type [menu 2606: 1=Transaction,2=Company]
  DAC C*4(80) Input
  DAC2 M*4(30) Y/N [menu 1: 1=No,2=Yes]
  DAC3 M*4(30) Y/N [menu 1: 1=No,2=Yes]
  DEFGRA M*15(2) Default graph [menu 2933: 1=Bars,2=Lines,3=Areas,4=Sectors]
  DES DES Description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLD A*10(80) Field
  FLGHIS M*4 History [menu 1: 1=No,2=Yes]
  FLGHISCAR A*3 History
  FSHGRA M*15(2) Representation [menu 2939: 1=Multiple,2=Cumulation,3=Comparison,4=Month,5=Week,6=Day]
  NBRCOL C*2 No. of fixed columns
  NBRFLD C*2 Field nb
  NBRINT C*1 Number of intervals
  NBRLIG C*4 Number of lines
  POSGRA M*15(2) Position [menu 2931: 1=To the right,2=To the left,3=Above,4=Below]
  REPGRA M*15(2) Representation [menu 2930: 1=Character,2=Character or graph,3=Character and graph,4=Graph]
  SHOTRA AX1 Short description
  TOTFLG M*4 Display totals [menu 1: 1=No,2=Yes]
  TYPGRA M*15(2) Type [menu 2932: 1=Simple graph,2=Multiple graph,3=Planning calendar,4=XSL,5=Gantt,6=Query tool]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## GCCEPYMLIK (CYK) - Dimension pyramid links
Keys (first = PK; D = duplicates allowed): CYK0 PYM+LEV+CCE
Fields:
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE;CCE (CACCE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CYK]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type -> [DIE]DIE0 =[CYK]DIE (GDIE) !Delete
  GRU CYR Group code -> [CRY]CRY0 =PYM;GRU;1 (GCCEGRUPYM) !Delete
  LEV C*2 Level
  PRNROW C*4 Print row
  PYM CYM Pyramid code -> [CYM]CYM0 =[CYK]PYM (GCCEPYM) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CYK]UPDUSR (AUTILIS) !Other

## GCCEPYMPRT (CYP) - Print pyramids
Keys (first = PK; D = duplicates allowed): CYP0 DIE+PYM+CCE
Fields:
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE;CCE (CACCE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CYP]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type -> [DIE]DIE0 =[CYP]DIE (GDIE) !Delete
  GRU CYR(10) Group code -> [CRY]CRY0 =PYM;GRU(indice);1 (GCCEGRUPYM) !Delete
  LEV C*2 Level
  LIE C*2 Link
  PYM CYM Pyramid code -> [CYM]CYM0 =[CYP]PYM (GCCEPYM) !Delete
  ROW C*4(10) Row
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CYP]UPDUSR (AUTILIS) !Other

## GCLCACEPAR (CLC) - Calculated journal entries
Keys (first = PK; D = duplicates allowed): CLC0 COD
Fields:
  ACC A*80 Calculation basis
  AUUID AUUID Single identifier
  COD A*10 Entry code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  FORAMT A*50 Formula
  FORDES AFR*80 Description
  FORREF AFR*80 Reference
  JOU1 JOU Journal -> [JOU]JOU0 =JOU1;[V]GSUPCLE (GJOURNAL) !Block
  JOU2 JOU Journal -> [JOU]JOU0 =JOU2;[V]GSUPCLE (GJOURNAL) !Block
  LASDAT D(2) Last journal
  LASNUM VCR(2) Last journal
  LASTYP GTE(2) Last journal -> [GTE]GTE0 =LASTYP;[V]GSUPCLE (GTYPACCENT) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  PERCLO M*4 Closing period [menu 1: 1=No,2=Yes]
  PERNEW M*4 Carryforwards [menu 1: 1=No,2=Yes]
  REFNUM VCR Template journal no.
  REFTYP GTE Template entry type -> [GTE]GTE0 =REFTYP;[V]GSUPCLE (GTYPACCENT) !Block
  SHOTRA AX1 Short description
  TYP1 GTE Template journal -> [GTE]GTE0 =TYP1;[V]GSUPCLE (GTYPACCENT) !Block
  TYP2 GTE Entry type -> [GTE]GTE0 =TYP2;[V]GSUPCLE (GTYPACCENT) !Block
  TYPGEN M*15 Generation type [menu 651: 1=Global,2=By BP]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author

## GCOMMIT (CMM) - Commitments
Keys (first = PK; D = duplicates allowed): CMM0 NUM; CMM1 NUMREF+TYPREF (D)
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[CMM]BPR (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[CMM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[CMM]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =[CMM]CURLED (TABCUR) !Block
  DESVCR DES Description
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[CMM]FCY (FACILITY) !Block
  FIY C*2 Fiscal year
  LED LED(10) Ledger -> [LED]LED0 =[CMM]LED (GLED) !Block
  NUM VCR Commitment
  NUMORG VCR Source document number
  NUMREF VCR Entry number
  PER C*2 Period
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  REFINT A*20 Internal reference
  REFSIM A*20 Simulation reference
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  TYP M*15 Type [menu 631: 1=Precommitment,2=Commitment]
  TYPCUR M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  TYPORG M*9 Source document type [menu 2623: 1=Order,2=Delivery request,3=Purchase request,4=Direct]
  TYPREF GTE Item type -> [GTE]GTE0 =TYPREF;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## GCOMMITD (CMD) - Commitment details
Keys (first = PK; D = duplicates allowed): CMD0 NUM+LIN
Fields:
  ACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  ACCDAT D Accounting date
  AMTCUR MD1 Entry amount
  AMTLED MD1(10) Ledger amount
  AUUID AUUID Single identifier
  BPRACC BPR BP -> [BPR]BPR0 =[CMD]BPRACC (BPARTNER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =COA(indice) (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[CMD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CMD]CREUSR (AUTILIS) !Other
  CUR CUR Entry currency -> [TCU]TCU0 =[CMD]CUR (TABCUR) !Block
  CURLED CUR(10) Ledger currency -> [TCU]TCU0 =CURLED(indice) (TABCUR) !Block
  DES DES Description
  DIE DIE Dimension type code -> [DIE]DIE0 =[CMD]DIE (GDIE) !Block act:ANA
  FCYLIN FCY Site -> [FCY]FCY0 =[CMD]FCYLIN (FACILITY) !Block
  FIY C*2 Fiscal year
  GRDACT M*15 Reason [menu 2683: 1=Creation,2=Modification,3=Deletion,4=Closing,5=Reversal,6=Closing cancellation,7=Carryforward,8=Resynchronization]
  GRDPCE M*15 Original document [menu 2684: 1=Purchase request,2=Order,3=Invoice,4=GRNI (GoodsReceivedNotInvoiced),5=Receivable credit memos,6=Carryforward,7=Credit memo,8=Accounting document]
  LED LED(10) Ledger -> [LED]LED0 =LED(indice) (GLED) !Block
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  PER C*2 Period
  QTY QTY Quantity
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[CMD]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CMD]UPDUSR (AUTILIS) !Other

## GCOMMITX (CMX) - Commitments (ref)
Keys (first = PK; D = duplicates allowed): CMX0 NUM+LIN+LEDTYP
Fields:
  ACC GAC Accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  ACCDAT D Accounting date
  AMTCUR MD1 Entry amount
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[CMX]BPR (BPARTNER) !Delete
  CCE CCE(9) Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Delete
  COA COA Chart code -> [COA]COA0 =[CMX]COA (GCOA) !Delete
  CPY CPY Company -> [CPY]CPY0 =[CMX]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CMX]CREUSR (AUTILIS) !Other
  CUR CUR Entry currency -> [TCU]TCU0 =[CMX]CUR (TABCUR) !Delete
  CURLED CUR Ledger currency -> [TCU]TCU0 =[CMX]CURLED (TABCUR) !Delete
  DES DES Description
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[CMX]DIE (GDIE) !Delete
  FCY FCY Site -> [FCY]FCY0 =[CMX]FCY (FACILITY) !Delete
  FCYLIN FCY Site -> [FCY]FCY0 =[CMX]FCYLIN (FACILITY) !Delete
  LED LED Ledger -> [LED]LED0 =[CMX]LED (GLED) !Delete
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  NUM VCR Document no.
  QTY QTY Quantity
  SNS M*15 Sign [menu 632: 1=Expense,2=Revenue]
  TYP M*15 Type [menu 631: 1=Precommitment,2=Commitment]
  UOM UOM Nonfinancial unit -> [TUN]TUN0 =[CMX]UOM (TABUNIT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CMX]UPDUSR (AUTILIS) !Other

## GDIAACC (GDA) - Account scheme header
Keys (first = PK; D = duplicates allowed): GDA0 DIA
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GDA]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  COA COA(9) Chart of accounts -> [COA]COA0 =[GDA]COA (GCOA) !Delete
  COANBR C*2 Plan no.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIA GDA Structure -> [GDA]GDA0 =[GDA]DIA (GDIAACC) !Delete
  DIE DIE Dimension types -> [DIE]DIE0 =[GDA]DIE (GDIE) !Delete act:ANA
  EXPNUM L*8 Export number
  GFY AGF Group -> [AGF]AGF0 =[GDA]GFY (AGRPFCY) !Block
  NBRACC C*2 Number of accounts
  NBRDIE C*2 No. dim.
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VLYEND D Validity end date
  VLYSTR D Validity start date

## GDIAACCD (GDC) - Account scheme lines
Keys (first = PK; D = duplicates allowed): GDC0 DIA+LINNUM
Fields:
  ACC GAC(9) Account -> [GAC]GAC0 =[GDC]ACC (GACCOUNT) !BSRA
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[GDC]BPR (BPARTNER) !Block
  CCE CCE Dimension -> [CCE]CCE0 =[GDC]CCE (CACCE) !BSRA act:ANA
  COE DCB*9 Coefficient
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DIA GDA Structure -> [GDA]GDA0 =[GDC]DIA (GDIAACC) !Delete
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  EXPNUM L*8 Export number
  LIGDES AFR*250 Description
  LINNUM C*2 Line number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block

## GDIAENTRY (GDE) - Entry transactions
Keys (first = PK; D = duplicates allowed): DIA DIA
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GDE]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  BPRFLG A*10 BP search
  CDE CDE Default dimensions -> [CDE]CDE0 =CDE;[V]GSUPCLE (CACCEDEF) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIA GDE Transaction -> [GDE]DIA =[GDE]DIA (GDIAENTRY) !Other
  DIAACC GDA(9) Account structure -> [GDA]GDA0 =[GDE]DIAACC (GDIAACC) !Block
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FLGBRO M*4 View left list [menu 1: 1=No,2=Yes]
  FLGEQL M*4 Balanced entry [menu 1: 1=No,2=Yes]
  FLGLOT M*4 Batch entry [menu 1: 1=No,2=Yes]
  FLGPAG M*4 Single page [menu 1: 1=No,2=Yes]
  GCM GCM(9) Account core model -> [GCM]GCM0 =[GDE]GCM (GACM) !Delete
  GFY AGF Group -> [AGF]AGF0 =[GDE]GFY (AGRPFCY) !Block
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBRCOL C*2 No. of fixed columns
  NBRGDA C*2 No. structures
  NBRLED C*2 No. of ledgers
  NBRRAT C*2 No. currency rates
  SHOTRA AX1 Short description
  TYPENT M*3 Entry type [menu 2646: 1=Column,2=Row,3=Tab]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VLYEND D Validity end date
  VLYSTR D Validity start date

## GDIAENTRYD (GDD) - Journal entry transactions
Keys (first = PK; D = duplicates allowed): GDD0 DIA+FLD
Fields:
  AUUID AUUID Single identifier
  CRD M*4 Form mode [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GDD]CREUSR (AUTILIS) !Other
  CTL ACL Control -> [ACL]ACL0 =[GDD]CTL (ACTL) !Block
  DAC M*15 Entry mode [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEFVAL AFR*250 Default value
  DIA GDE Transaction -> [GDE]DIA =[GDD]DIA (GDIAENTRY) !Delete
  FLD A*20 Field
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GDD]UPDUSR (AUTILIS) !Other

## GENTLOT (LOT) - Accounting journal batches
Keys (first = PK; D = duplicates allowed): LOT0 LOT
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[LOT]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DACDIA GDE Transaction -> [GDE]DIA =[LOT]DACDIA (GDIAENTRY) !Block
  DACDIAGAS GDE Transaction -> [GDE]DIA =[LOT]DACDIAGAS (GDIAENTRY) !Block
  DESLOT DES Description
  FCY FCY Site -> [FCY]FCY0 =[LOT]FCY (FACILITY) !Block
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LOT VCR Batch code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*4 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change author

## GENTLOTA (LOA) - Analytical batch entry lines
Keys (first = PK; D = duplicates allowed): LOA0 LOT+ORNVCR+LIN+ANALIN
Fields:
  AMTCUR MD1(9) Amount in currency
  ANALIN C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE(9) Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LOA]CREUSR (AUTILIS) !Other
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[LOA]DIE (GDIE) !Block
  LIN C*3 Line number
  LOT VCR Lot
  ORNVCR C*4 Journal number
  QTY QTY(9) Quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LOA]UPDUSR (AUTILIS) !Other

## GENTLOTD (LOD) - General batch entry lines
Keys (first = PK; D = duplicates allowed): LOD0 LOT+ORNVCR+LIN
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AMTCUR MD1 Amount in currency
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[LOD]BPR (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[LOD]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LOD]CREUSR (AUTILIS) !Other
  DES DES Description
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Block
  FCYLIN FCY Site -> [FCY]FCY0 =[LOD]FCYLIN (FACILITY) !Block
  FREREF REF Free reference
  LEDTYP M(10) Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LIN C*3 Line number
  LOT VCR Lot
  OFFACC A*15 Offset
  ORNVCR C*4 Journal number
  QTY QTY Quantity
  SAC SAC(10) Control
  SNS C*2 Sign
  STT1 ADI Statistics -> [ADI]CODE =351;STT1 (ATABDIV) !Block
  STT2 ADI Statistics -> [ADI]CODE =352;STT2 (ATABDIV) !Block
  STT3 ADI Statistics -> [ADI]CODE =353;STT3 (ATABDIV) !Block
  TAX VAT Tax -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LOD]UPDUSR (AUTILIS) !Other

## GENTLOTH (LOH) - Batch entry header
Keys (first = PK; D = duplicates allowed): LOH0 LOT+ORNVCR
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  BANDAT D Bank date act:KIT
  BPRDATVCR D Document date
  BPRVCR A*20 Source document
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LOH]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[LOH]CUR (TABCUR) !Block
  CURMGT CUR(10) Currency -> [TCU]TCU0 =[LOH]CURMGT (TABCUR) !Block
  DESVCR DES Description
  DUDDAT D Due date
  ENTDAT D Entry date
  FCYLIN FCY Site -> [FCY]FCY0 =[LOH]FCYLIN (FACILITY) !Block
  FLGDAS M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  FLGFUP M*4 Reminder [menu 1: 1=No,2=Yes]
  FLGPAZ M*15 Pay approval [menu 510: 1=Pending,2=Conflict,3=Delayed,4=Authorized to pay]
  LOT VCR Lot
  NBRCUR C*1 Number of currencies
  NUM VCR Document number
  ORNVCR C*4 Journal number
  RATDAT D Rate date
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  REF REF Reference
  RVS M*15 Reversal [menu 619: 1=No,2=Yes,3=Reversed]
  RVSDAT D Reversal date
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYPDUD M*15 Type of open item [menu 2614: 1=Order,2=Invoice,3=Payment,4=Others]
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LOH]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## GJOUCOA (JCO) - Journals - Chart of accounts
Keys (first = PK; D = duplicates allowed): JCO0 COA+JOU+LEG; JCO1 JOU+COA+LEG; JCO2 JOU+LEG+COA
Fields:
  ACC GAC Treasury account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[JCO]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FBDACC GAC(20) Restricted accounts -> [GAC]GAC0 =COA;FBDACC(indice) (GACCOUNT) !Block
  FBDNBR C*2 Number of restricted accounts
  FRQACC GAC(20) Frequent accounts -> [GAC]GAC0 =COA;FRQACC(indice) (GACCOUNT) !Block
  FRQCOD A*1(20) Short codes
  FRQNBR C*2 No. frequent accounts
  JOU JOU Journal -> [JOU]JOU0 =JOU;LEG (GJOURNAL) !Delete
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GJOURNAL (JOU) - Journal codes
Notes: differs in V9.0 P12 (diff: AT3_GJOURNAL.htm); differs in V10 P1 (diff: ATD_GJOURNAL.htm)
Keys (first = PK; D = duplicates allowed): JOU0 JOU+LEG; JOU1 DES (D)
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[JOU]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  BOLLATO ANM Bollato sequence no. -> [ANM]ANM0 =[JOU]BOLLATO (ACODNUM) !Block act:KIT
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSLFLO ADI Flow -> [ADI]CODE =324;CSLFLO (ATABDIV) !Block act:PRCSL
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCY CFY Company/site
  JOU JOU Journal -> [JOU]JOU0 =JOU;LEG (GJOURNAL) !Delete
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SHOTRA AX1 Short description
  TYP M*15 Type [menu 613: 1=Sales,2=Purchasing,3=Treasury,4=Misc. operations 1,5=Misc. operations 2,6=Misc. operations 3,7=Carryforward,8=Misc. operations 4,9=General journal,10=Misc. operations 6]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GLCONSO (GLC) - Consolidation ledger
Notes: activity code CSL
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## GRPCUR (GCU) - Currency groups
Keys (first = PK; D = duplicates allowed): GCU0 GRP
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GCU]CREUSR (AUTILIS) !Other
  CUR CUR(30) Currency -> [TCU]TCU0 =[GCU]CUR (TABCUR) !Block
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  GRP GCU Code -> [GCU]GCU0 =[GCU]GRP (GRPCUR) !Delete
  NBRCUR C*2 Number
  SHOTRA AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GCU]UPDUSR (AUTILIS) !Other

## GRPDSP (GSP) - Distribution groups
Keys (first = PK; D = duplicates allowed): GSP0 DIE+COD+CCE; GSP1 DIE (D)
Fields:
  AUUID AUUID Single identifier
  CCE CCE Dimension -> [CCE]CCE0 =DIE;CCE (CACCE) !Block
  COD A*10 Code
  COE DCB*9 Coefficient
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  DIE DIE Dimension type -> [DIE]DIE0 =[GSP]DIE (GDIE) !Block
  EXPNUM L*8 Export number
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GRPSAC (GSC) - Control groups
Keys (first = PK; D = duplicates allowed): GSC0 COA+GRU+NUMLIN; GSC1 COA+GRU+SAC
Fields:
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =[GSC]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  GRU GSC Group -> [GSC]GSC0 =COA;GRU;NUMLIN (GRPSAC) !Other
  NUMLIN C*2 Line number
  SAC SAC Control
  SHOTRA AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GSTDTL (GDL) - GST detail
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GDL0 RPTNUM (D); GDL1 NUM+BPR+VAT+SNS
Fields:
  ACCDAT D Accounting date
  AMTATI MD1 Amount + tax
  AMTVAT MD1 Declared amount
  AUS1AGSTSAL A*5 1A GST on sales
  AUS1BGSTPUR A*5 1B GST on purchases
  AUSBAS A*5
  AUSG10CAPPUR A*5 G10 capital purchase
  AUSG11NCAPPU A*5 G11 non capital pur
  AUSG1TOTSA A*5 G1 total sales
  AUSG2EXPSAL A*5 G2 export sales
  AUSG3GSTFRES A*5 G3 GST free sales
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[GDL]BPR (BPARTNER) !Other
  CPY CPY Company -> [CPY]CPY0 =[GDL]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GDL]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[GDL]FCY (FACILITY) !Other
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LIN L*8 Invoice line
  NETPRINOT MD8 Net price - tax
  NUM VCR Invoice no.
  RPTNUM A*20 Report
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GDL]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Other

## GSTGRP (GSTGH) - GST group header
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GSTGH0 CODGSTGRP
Fields:
  AUUID AUUID Single identifier
  CODGSTGRP GSTGRP GST group -> [GSTGH]GSTGH0 =[GSTGH]CODGSTGRP (GSTGRP) !BSRA
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GSTGH]CREUSR (AUTILIS) !Other
  DES DES Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  GSTPER M*4 Reporting period [menu 3698: 1=Monthly,2=Quarterly]
  PAYDAY C*2 Payment day
  REM A*250 Notes
  SHO SHO Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GSTGH]UPDUSR (AUTILIS) !Other

## GSTGRPD (GSTGD) - GST group details
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GSTGD0 CODGSTGRP+LIN; GSTGD1 CODGSTGRP+CPY
Fields:
  ABN A*11 ABN number
  AUUID AUUID Single identifier
  CODGSTGRP GSTGRP GST group -> [GSTGH]GSTGH0 =[GSTGD]CODGSTGRP (GSTGRP) !Delete
  CPY CPY GST member company -> [CPY]CPY0 =[GSTGD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GSTGD]CREUSR (AUTILIS) !Other
  DATCES D Date of cessation
  DATFOR D Formation date
  GSTHEA M*4 Head entity [menu 1: 1=No,2=Yes]
  LIN L*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GSTGD]UPDUSR (AUTILIS) !Other

## GSTHDR (GHR) - GST header
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GHR0 RPTNUM; GHR1 STRDAT+ENDDAT+FCY+CPY+ALLFCY+ALLCPY (D)
Fields:
  ALLCPY M*4 All companies [menu 1: 1=No,2=Yes]
  ALLFCY M*4 All sites [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[GHR]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GHR]CREUSR (AUTILIS) !Other
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[GHR]FCY (FACILITY) !Other
  NUM VCR Invoice no.
  RPTNUM A*20 Report
  RPTTYP M*15 Generation type [menu 2601: 1=Actual,2=Simulation]
  RUNDAT D Run date
  STRDAT D Start date
  TCPY CPY To company -> [CPY]CPY0 =[GHR]TCPY (COMPANY) !Other
  TFCY FCY To site -> [FCY]FCY0 =[GHR]TFCY (FACILITY) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GHR]UPDUSR (AUTILIS) !Other

## GSTPER (GSTPH) - GST reporting period header
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GSTPH0 CODGSTPER; GSTPH1 DATSTR-CODGSTGRP
Fields:
  AUUID AUUID Single identifier
  CODGSTGRP GSTGRP GST group -> [GSTGH]GSTGH0 =[GSTPH]CODGSTGRP (GSTGRP) !Block
  CODGSTPER L*8 Period code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GSTPH]CREUSR (AUTILIS) !Other
  DATEND D End date
  DATLDG D Date lodged
  DATSTR D Start date
  DOCIDT A*30 Document ID
  FLGPRE M*4 Include unreported transactions [menu 1: 1=No,2=Yes]
  GST1A MD1 1A
  GST1B MD1 1B
  GSTADD1 MD1 5A PAYG income tax inst.
  GSTADD2 MD1 4 PAYG tax withheld
  GSTADD3 MD1 Fuel tax 7C
  GSTADD4 MD1 6A Fringe benefit
  GSTADD5 MD1 Fuel tax 7D
  GSTADD6 MD1 Additional value 6
  GSTG1 MD1 G1
  GSTG10 MD1 G10
  GSTG11 MD1 G11
  GSTG13 MD1 G13
  GSTG14 MD1 G14
  GSTG2 MD1 G2
  GSTG3 MD1 G3
  GSTG4 MD1 G4
  GSTGRPSTA M*4 GST group status [menu 3699: 1=In review,2=Validated,3=Closed]
  PREDAT D As of date
  RCPIDT A*30 Receipt ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GSTPH]UPDUSR (AUTILIS) !Other

## GSTPERD (GSTPD) - GST reporting period details
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): GSTPD0 CODGSTPER+LIN
Fields:
  AUUID AUUID Single identifier
  CODGSTGRP GSTGRP GST group -> [GSTGH]GSTGH0 =[GSTPD]CODGSTGRP (GSTGRP) !Block
  CODGSTPER L*8 Period code
  CPY CPY GST member company -> [CPY]CPY0 =[GSTPD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GSTPD]CREUSR (AUTILIS) !Other
  GSTADD7C MD1 Fuel tax 7C
  GSTADD7D MD1 Fuel tax 7D
  GSTADDF01 MD1 FBT F1
  GSTADDF02 MD1 FBT F2
  GSTADDF03 MD1 FBT F3
  GSTADDF04 A*2 FBT F4 reason
  GSTADDT01 MD1 PAYG T1
  GSTADDT02 MD1 PAYG T2 %
  GSTADDT03 MD1 PAYG T3 %
  GSTADDT04 A*2 PAYG T4 reason
  GSTADDT07 MD1 PAYG T7
  GSTADDT08 MD1 PAYG T8
  GSTADDT09 MD1 PAYG T9
  GSTADDW01 MD1 PAYG W1
  GSTADDW02 MD1 PAYG W2
  GSTADDW03 MD1 PAYG W3
  GSTADDW04 MD1 PAYG W4
  GSTHEA M*4 Head entity [menu 1: 1=No,2=Yes]
  GSTMEMSTA M*4 Status [menu 3118: 1=Temporary,2=Final,3=To be defined]
  LIN L*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GSTPD]UPDUSR (AUTILIS) !Other

## GTABACC2 (GT2) - Account inquiries
Keys (first = PK; D = duplicates allowed): GT20 COA+ACCROO
Fields:
  ACCROO A*10 Account root
  AUUID AUUID Single identifier
  COA COA Chart code -> [COA]COA0 =[GT2]COA (GCOA) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  SCECODANA GTC Analytical screen code -> [GTC]GTC0 ="NAT";SCECODANA (GTABACC) !Block
  SCECODGEN GTC General screen code -> [GTC]GTC0 ="CPT";SCECODGEN (GTABACC) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## GTABACC3 (GTC3) - Balance graph
Keys (first = PK; D = duplicates allowed): GTC3 CNSCOD+COD
Fields:
  AFFGRAS M*15 Default display [menu 2936: 1=Table,2=Graph]
  AUUID AUUID Single identifier
  CNSCOD ACN Inquiry type -> [ACN]ACN0 =[GTC3]CNSCOD (ACONSULT) !Delete
  COD GTC Code -> [GTC]GTC0 =CNSCOD;COD (GTABACC) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[GTC3]CREUSR (AUTILIS) !Other
  DEFGRAS M*15 Default graph [menu 2933: 1=Bars,2=Lines,3=Areas,4=Sectors]
  FSHGRAS M*15 Representation [menu 2939: 1=Multiple,2=Cumulation,3=Comparison,4=Month,5=Week,6=Day]
  POSGRAS M*15 Position [menu 2931: 1=To the right,2=To the left,3=Above,4=Below]
  REPGRAS M*15 Representation [menu 2930: 1=Character,2=Character or graph,3=Character and graph,4=Graph]
  TYPAMT M*8 Amount type [menu 3605: 1=Balances in ledger currency,2=Movements and balances in ledger currency,3=Balances in transaction currency,4=Movements and balances in transaction currency]
  TYPAMT2 M*8 Amount type [menu 3606: 1=Balances,2=Movements and balances]
  TYPGRAS M*15 Type [menu 2932: 1=Simple graph,2=Multiple graph,3=Planning calendar,4=XSL,5=Gantt,6=Query tool]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[GTC3]UPDUSR (AUTILIS) !Other

## GTMPMTC (GMT) - Temporary matching table
Keys (first = PK; D = duplicates allowed): GMT0 ID+ACC+BPR+FCY+MTC+ACCNUM+DUDLIG
Fields:
  ACC GAC Account -> [GAC]GAC0 =[GMT]ACC (GACCOUNT) !BSRA
  ACCNUM UNQ Internal number
  AMTIPT MD1 Amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[GMT]BPR (BPARTNER) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[GMT]CREUSR (AUTILIS) !Other
  DUDLIG C*3 Due date number
  FCY FCY Site -> [FCY]FCY0 =[GMT]FCY (FACILITY) !Delete
  ID A*10 Identifier
  MTC A*5 Match letter
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[GMT]UPDUSR (AUTILIS) !Other

## HISTAXSPA (HTS) - Tax extraction history
Notes: activity code KSP
Keys (first = PK; D = duplicates allowed): HTS0 YEA+CPY+FCY
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[HTS]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HTS]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[HTS]FCY (FACILITY) !Block
  LASTUPDDAT D Last update date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HTS]UPDUSR (AUTILIS) !Other
  YEA C*4 Year

## HISTOAMD (HAM) - Amendment history
Notes: activity code SDD
Keys (first = PK; D = duplicates allowed): HAM0 CPY+UMRNUM+FLDCOD+PAYNUM
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[HAM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HAM]CREUSR (AUTILIS) !Other
  FLDCOD AVA Field code
  NEWVAL A*50 New value
  OLDVAL A*50 Previous value
  OPEDAT D Change date
  PAYNUM VCR Payment number
  UMRNUM MDT Mandate reference -> [MDT]MDT0 =CPY;UMRNUM (MANDATE) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HAM]UPDUSR (AUTILIS) !Other

## HON281 (HHO) - 281.5 fees (Belgium)
Notes: activity code BE281
Keys (first = PK; D = duplicates allowed): HHO0 CPY+YEA+PRVNUM
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[HHO]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HHO]CREUSR (AUTILIS) !Block
  CRYCOD A*3 Country code
  EECNUM EEC EU VAT no.
  FIRNAM A*20 First name
  JOB A*30 Profession
  LAN LAN Language -> [TLA]TLA0 =[HHO]LAN (TABLAN) !Block
  NATNUM A*11 National no.
  PHYPSL M*4 Natural person [menu 1: 1=No,2=Yes]
  POSCOD A*5 Postal code
  POSCTY A*26 Distributor office
  PRVNAM A*50 Company name
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[HHO]PRVNUM (HONPRV) !Block
  STREET A*40 Street
  STREETNUM A*4 Street number
  SURNAM A*30 Last name
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HHO]UPDUSR (AUTILIS) !Block
  YEA C*4 Year

## HON281D (DHO) - 281.5 fees details
Notes: activity code BE281
Keys (first = PK; D = duplicates allowed): DHO0 CPY+YEA+PRVNUM+TYPLIN+NUM+LIN; DHO1 CPY+YEA+PRVNUM+NUM+TYP281+TYPLIN+LIN
Fields:
  ACCDATINV D Invoice date
  ACCDATPAY D Payment date
  AMTLEDINV MD1 Ledger amount
  AMTLEDPAY MD1 Ledger amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[DHO]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[DHO]CREUSR (AUTILIS) !Block
  FCY FCY Site -> [FCY]FCY0 =[DHO]FCY (FACILITY) !Block
  JOU JOU Journal -> [JOU]JOU0 =JOU;[V]GSUPCLE (GJOURNAL) !Block
  LIN C*3 Line number
  MTC A*5 Matching
  NUM VCR Document no.
  NUMPAY VCR Payment no.
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[DHO]PRVNUM (HONPRV) !Block
  SNSINV C*2 Sign
  SNSPAY C*2 Sign
  TYP GTE Entry type -> [GTE]GTE0 =TYP;[V]GSUPCLE (GTYPACCENT) !Block
  TYP281 M*8 281.5 category [menu 3623: 1=Commission brokerage rebate,2=Fees or sessional payments,3=Benefits in kind,4=Expenses incurred on behalf of the beneficiary]
  TYPLIN M*8 Collection type [menu 3624: 1=Invoiced amounts,2=Paid amounts]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[DHO]UPDUSR (AUTILIS) !Block
  YEA C*4 Year

## HONLIN (HLN) - Fee lines
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): HLN0 FCY+PRVNUM+DAT+HON+LINNUM; HLN1 DADFCY+PRVNUM (D)
Fields:
  ACCNUM UNQ Internal number
  AMTCUR MD1 Amount
  AMTLOC MD1 Local currency amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[HLN]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[HLN]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[HLN]CUR (TABCUR) !Block
  DADFCY FCY DAS2 site -> [FCY]FCY0 =[HLN]DADFCY (FACILITY) !Block
  DAT D Date
  FCY FCY Site -> [FCY]FCY0 =[HLN]FCY (FACILITY) !Block
  HON M*15 Fee [menu 615: 1=Fees and vacations,2=Commissions,3=Brokerages,4=Rebates,5=Attendance tokens,6=Royalties,7=Inventor rights,8=Other payments,9=Indemnities and reimbursements,10=Perquisites,11=Withholding tax on income,12=Net tax on royalties]
  LINNUM C*4 Line number
  NUMINV VCR Invoice document number
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[HLN]PRVNUM (HONPRV) !Block
  TYPHON A*4 Fee type
  TYPINV GTE Invoice document type -> [GTE]GTE0 =TYPINV;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[HLN]UPDUSR (AUTILIS) !Other

## HONPRV (PRV) - Service suppliers
Notes: activity code FEE2; differs in V9.0 P12 (diff: AT3_HONPRV.htm)
Keys (first = PK; D = duplicates allowed): PRV0 PRVNUM
Fields:
  ABC A*1 BIS,TER,QUATER
  ADDCPL A*40 Address complement
  AFLG1 M*4 Other [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CRN CRT Site tax ID no.
  CRYCOD A*3 Country code
  CTYNAM CT0 Municipality
  DADFLG M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  DFLG3 M*4 Dispensed [menu 1: 1=No,2=Yes]
  EECNUM EEC EU VAT no. act:BE281
  FAX TEL Fax
  FFLG2 M*4 Allocation [menu 1: 1=No,2=Yes]
  FIRNAM A*20 First name
  FLG281 M*4 281.5 [menu 1: 1=No,2=Yes] act:BE281
  JOB A*30 Profession
  LAN LAN Language -> [TLA]TLA0 =[PRV]LAN (TABLAN) !Block act:BE281
  LFLG1 M*4 Lodging [menu 1: 1=No,2=Yes]
  NATNUM A*11 National no. act:BE281
  NFLG1 M*4 Food [menu 1: 1=No,2=Yes]
  PFLG2 M*4 Taking charge [menu 1: 1=No,2=Yes]
  PHYPSL M*4 Natural person [menu 1: 1=No,2=Yes]
  POSCOD A*5 Postal code
  POSCTY A*26 Distributor office
  POSCTYCOD A*10 Municipality code
  PRVNAM A*50 Company name
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[PRV]PRVNUM (HONPRV) !Other
  RFLG2 M*4 Reimbursement [menu 1: 1=No,2=Yes]
  RFLG3 M*4 Reduced rate [menu 1: 1=No,2=Yes]
  STREET A*40 Street
  STREETNUM A*4 Street number
  SURNAM A*30 Last name
  TEL TEL Telephone
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VFLG1 M*4 Car [menu 1: 1=No,2=Yes]

## IDTCCE (IDTC) - Dimension index
Notes: activity code PRCSL; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): IDTC0 LED+CCE1+CCE2+CCE3+CCE4+CCE5+CCE6+CCE7+CCE8+CCE9; IDTC1 IDTCCE
Fields:
  AUUID AUUID Single identifier
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE(0);CCE1 (CACCE) !Block
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE(1);CCE2 (CACCE) !Block
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE(2);CCE3 (CACCE) !Block
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE(3);CCE4 (CACCE) !Block
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE(4);CCE5 (CACCE) !Block
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE(5);CCE6 (CACCE) !Block
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE(6);CCE7 (CACCE) !Block
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE(7);CCE8 (CACCE) !Block
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE(8);CCE9 (CACCE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[IDTC]CREUSR (AUTILIS) !Other
  DIE DIE(9) Dimension type code -> [DIE]DIE0 =[IDTC]DIE (GDIE) !Block
  IDTCCE UNQ Dimension ID
  LED LED Ledger -> [LED]LED0 =[IDTC]LED (GLED) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[IDTC]UPDUSR (AUTILIS) !Other

## IMURANO (IPM) - Spanish payroll interface setup
Notes: activity code MURAN; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): IPM0 CPY+FCY+LEG
Fields:
  AUUID AUUID Single identifier
  CCEDEF CDE Default dimensions -> [CDE]CDE0 =CCEDEF;[V]GSUPCLE (CACCEDEF) !Block
  COD GAU Automatic journal -> [GAU]GAU0 =[IPM]COD (GAUTACE) !Block
  CPY CPY Company -> [CPY]CPY0 =[IPM]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[IPM]CREUSR (AUTILIS) !Other
  DES AX3 Description
  FCY FCY Site -> [FCY]FCY0 =[IPM]FCY (FACILITY) !Block
  FLGDET M*4 Detailed [menu 1: 1=No,2=Yes]
  HEAUSEVAL A*20(11) Value
  HEAUSEVAL2 A*20(11) Value 2
  HEAVALEND C*4(11) Ending position
  HEAVALINI C*4(11) Starting position
  HEAVALNAM M*20(11) Zone name [menu 2077: 1=Company,2=Site,3=Date,4=Employee,5=Description,6=Currency,7=Dimension 1,8=Dimension 2,9=Dimension 3,10=Dimension 4,11=Dimension 5]
  HEAVALUSE A*20(11) Parameter 1
  HEAVALUSE2 A*20(11) Parameter 2
  IDENT1 A*10 Identifier 1
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  NOLIB C*3(11) Local menu no.
  NOLIB1 C*3(11) Local menu no.
  NUMDEC C*1 Number of decimals
  REPDAT M*4 Report date [menu 1: 1=No,2=Yes]
  SEPDEC A*1 Decimal separator
  SEPREC A*8 Record separator
  TYP GTE Entry type -> [GTE]GTE0 =TYP;LEG (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[IPM]UPDUSR (AUTILIS) !Other

## IMURANOD (IPMD) - Spanish payroll interface setup
Notes: activity code MURAN; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): IPD0 CPY+FCY+LEG+LINNUM
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =26;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  CCEDEFL CDE Default dimensions -> [CDE]CDE0 =CCEDEFL;[V]GSUPCLE (CACCEDEF) !Block
  CODDES A*50 Concept
  CPY CPY Company -> [CPY]CPY0 =[IPMD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[IPMD]CREUSR (AUTILIS) !Other
  ENDPOS C*4 Ending position
  FCY FCY Site -> [FCY]FCY0 =[IPMD]FCY (FACILITY) !Block
  FLGACT M*4 Active [menu 1: 1=No,2=Yes]
  INIPOS C*4 Starting position
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LENGHT A*5 Length
  LINNUM C*4 Number
  SENSE M*10 Debit/Credit [menu 626: 1=Debit,2=Credit]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[IPMD]UPDUSR (AUTILIS) !Other

## INVNUMSPA (ISP) - Source document
Notes: activity code KSP
Keys (first = PK; D = duplicates allowed): ISP0 NUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ISP]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice number
  INVNUMDAT D Source date
  NUM VCR Document no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ISP]UPDUSR (AUTILIS) !Other

## KPYIMPDTL (KPD) - Sage 50/Murano payroll detail
Notes: activity code MUIMP; differs in V9.0 P12 (diff: AT3_KPYIMPDTL.htm); differs in V10 P1 (diff: ATD_KPYIMPDTL.htm)
Keys (first = PK; D = duplicates allowed): KPYD0 RECID+LINENO
Fields:
  ACC GAC(10) Account -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Delete
  ACC_CODE A*20 Code
  AMTCUR MD1 Amount
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CCEACC_CODE A*20 Code
  CCECOSTCENTR A*20 Cost Centre
  CCEDEPT A*20 Department
  CCEEMPLOYEE A*15 Employee
  COA COA(10) Chart of accounts -> [COA]COA0 =[KPD]COA (GCOA) !Block
  COSTCENTRE A*20 Cost Centre
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KPD]CREUSR (AUTILIS) !Other
  DEPT A*20 Department
  DIE DIE Dimension type code -> [DIE]DIE0 =[KPD]DIE (GDIE) !Block act:ANA
  DSP DSP Distribution -> [DSP]DSP0 =DSP;1 (CADSP) !Other act:MURAN
  EMPLOYEE A*10 Employee
  GRPGAS A*30 Group entry act:MURAN
  LED LED(10) Ledger -> [LED]LED0 =[KPD]LED (GLED) !Delete act:MURAN
  LINENO L*4 Line no.
  NARRATIVE A*50 Narrative
  NUMMURANO L*8 Number act:MURAN
  QTY QTY Quantity act:MURAN
  RECID A*25 Identifier
  REFNO A*50 Report line
  SNS C*2 Sign
  SRC_LINE A*10 Source line
  TMPACC1 A*50 Source account
  TRSDAT D Transaction date
  UOM UOM Unit -> [TUN]TUN0 =[KPD]UOM (TABUNIT) !Delete act:MURAN
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KPD]UPDUSR (AUTILIS) !Other

## KPYIMPDTLA (KPA) - Analytical line
Notes: activity code MURAN; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): KPYA0 RECID+LINENO+ANALIG
Fields:
  ACC GAC(10) General accounts -> [GAC]GAC0 =COA(indice);ACC(indice) (GACCOUNT) !Block
  AMTCUR MD1 Amount
  ANALIG C*3 Order information
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  COA COA(10) Chart code -> [COA]COA0 =[KPA]COA (GCOA) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KPA]CREUSR (AUTILIS) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[KPA]DIE (GDIE) !Block act:ANA
  DSPLIN M*4 Distribution [menu 1: 1=No,2=Yes]
  GRPGAS A*30 Group entry
  LINENO L*4 Line no.
  QTY QTY Quantity
  RECID A*25 Identifier
  UOM UOM Unit -> [TUN]TUN0 =[KPA]UOM (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KPA]UPDUSR (AUTILIS) !Other

## KPYIMPHDR (KPH) - Sage 50/Murano payroll header
Notes: activity code MUIMP; differs in V9.0 P12 (diff: AT3_KPYIMPHDR.htm); differs in V10 P1 (diff: ATD_KPYIMPHDR.htm)
Keys (first = PK; D = duplicates allowed): KPYH0 RECID; KPYH1 GRPGAS (D)
Fields:
  ACCDAT D Accounting date
  AUUID AUUID Single identifier
  BPRMURANO A*30 Employee act:MURAN
  CDE CDE Default dimensions -> [CDE]CDE0 =CDE;[V]GSUPCLE (CACCEDEF) !Block
  CHGRAT RCU Rate act:MURAN
  COD GAU Automatic journal -> [GAU]GAU0 =[KPH]COD (GAUTACE) !Block act:MURAN
  CPY CPY Company -> [CPY]CPY0 =[KPH]CPY (COMPANY) !Block
  CPYNAM A*90 Company name
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KPH]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[KPH]CUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[KPH]FCY (FACILITY) !Delete
  FLGDET M*4 Detailed [menu 1: 1=No,2=Yes] act:MURAN
  FLGVAL M*4 Validated [menu 1: 1=No,2=Yes] act:MURAN
  GRPGAS A*30 Group entry act:MURAN
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  IMPFIL A*50 Import file
  INTREF A*8 Internal reference
  LOT A*20 Lot act:MURAN
  NUM VCR Journal
  NUMMURANO L*8 Number act:MURAN
  ORIPAY M*10 Origin [menu 1: 1=No,2=Yes] act:MURAN
  RECID A*25 Identifier
  REF A*50 Your reference
  RPODAT D Report date
  RPONAM A*75 Report name
  RPOTIM A*10 Report time
  SRCFIL A*50 File name
  STA M*4 Posted [menu 1: 1=No,2=Yes]
  STALOT MM*15 Status [menu 617: 1=Temporary,2=Final] act:MURAN
  TMPFCY A*90 Site
  TOT MD1 Total
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KPH]UPDUSR (AUTILIS) !Other

## KPYIMPTRAN (KPT) - Sage 50 import transcribe
Notes: activity code MUIMP; differs in V9.0 P12 (diff: AT3_KPYIMPTRAN.htm)
Keys (first = PK; D = duplicates allowed): KPYT0 TYP+INVALUE+COA+FCY+ACC; KPUT1 TYP+COA+FCY (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT M*4 Report date [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CCE A*15 Analytical dimension
  CDE CDE Default dimensions -> [CDE]CDE0 =CDE;[V]GSUPCLE (CACCEDEF) !Block
  COA COA Chart of accounts -> [COA]COA0 =[KPT]COA (GCOA) !Delete
  CONTRA M*4 Offset [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[KPT]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[KPT]FCY (FACILITY) !Delete
  GAU GAU Automatic journal -> [GAU]GAU0 =[KPT]GAU (GAUTACE) !Other
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  INVALUE A*100 Source value
  TYP M*15 Type [menu 3700: 1=Site,2=Account,3=Employee dimension,4=Cost centre dimension,5=Department dimension,6=A/c code dimension]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[KPT]UPDUSR (AUTILIS) !Other

## MATCHCODE (MTC) - Match letters to use
Keys (first = PK; D = duplicates allowed): MTC0 COA+ACC+BPR
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Delete
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[MTC]BPR (BPARTNER) !Delete
  COA COA Chart code -> [COA]COA0 =[MTC]COA (GCOA) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MTC]CREUSR (AUTILIS) !Other
  MTC A*5 Match letter
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MTC]UPDUSR (AUTILIS) !Other

## MTCAUTO (MTU) - Automatic matching
Keys (first = PK; D = duplicates allowed): MTU0 NUM
Fields:
  ACC GAC General accounts -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCMTC GAC Offset -> [GAC]GAC0 =COA;ACCMTC (GACCOUNT) !Block
  AMTAUT MD1(10) Automatic amounts
  AMTCUR MD1 Currency amount
  AMTLED MD1 Ledger amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[MTU]BPR (BPARTNER) !Block
  COA COA Chart code -> [COA]COA0 =[MTU]COA (GCOA) !Block
  CPY CPY Company -> [CPY]CPY0 =[MTU]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MTU]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[MTU]CUR (TABCUR) !Block
  CURLED CUR Ledger currency -> [TCU]TCU0 =[MTU]CURLED (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[MTU]FCY (FACILITY) !Block
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NUM UNQ Identifier
  REFINT A*20 Internal reference
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MTU]UPDUSR (AUTILIS) !Other

## MTCBATCH (MTB) - Batch matching
Keys (first = PK; D = duplicates allowed): MTB0 MTCNUM+ACCNUM+DUDLIG
Fields:
  ACCNUM UNQ Internal number
  AMTIPT MD1 Amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[MTB]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MTB]CREUSR (AUTILIS) !Other
  DUDLIG C*3 Due date number
  MTCFLG C*1 Flag
  MTCNUM UNQ Matching no.
  MTCTYP C*2 Matching type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MTB]UPDUSR (AUTILIS) !Other

## MTCGAUTMP (MGT) - Document matching preparation
Keys (first = PK; D = duplicates allowed): MGT0 COD+LINNUM+CLEA1+CLEA2+ACCNUM
Fields:
  ACC GAC Account -> [GAC]GAC0 ="";ACC (GACCOUNT) !Other
  ACCNUM UNQ Internal number
  AMTCUR MD1 Amount in currency
  AMTLED MD1 Ledger currency amt
  AUUID AUUID Single identifier
  BPR BPR Bill-to/Order BP -> [BPR]BPR0 =[MGT]BPR (BPARTNER) !Block
  CLEA1 A*15 Alpha 1
  CLEA2 A*15 Alpha 2
  COD GAU Code -> [GAU]GAU0 =[MGT]COD (GAUTACE) !Block
  CPY CPY Company -> [CPY]CPY0 =[MGT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MGT]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[MGT]CUR (TABCUR) !Block
  LINNUM C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MGT]UPDUSR (AUTILIS) !Other

## NRYPAR (NRY) - ENERGY setup
Notes: activity code FAL
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## PAYVAT (PYHV) - Cash VAT (Portugal)
Notes: activity code KPO; differs in V9.0 P12 (diff: AT3_PAYVAT.htm)
Keys (first = PK; D = duplicates allowed): PYHV0 PAYNUM+PAYLIN+PAYMENTSTA
Fields:
  ACCDAT D Accounting date
  AMTTAX MD1(10) Tax amount
  AUUID AUUID Single identifier
  BASTAX MD1(10) Tax basis
  BPRNUM BPR BP -> [BPR]BPR0 =[PYHV]BPRNUM (BPARTNER) !Block
  CASHVATNUM A*250 Communication number
  CREDAT D Creation date
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[PYHV]CREUSR (AUTILIS) !Other
  INVNUM VCR Invoice number
  PAYLIN L*8 Receipt line
  PAYMENTSTA M*15 Receipt status [menu 3620: 1=Normal receipt,2=Receipt canceled]
  PAYNUM VCR Payment no.
  REVERSALDAT D Reversal date
  SNS C*2 Sign
  TAX VAT(10) Taxes -> [TVT]TVT0 =TAX(indice);[V]GSUPCLE (TABVAT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[PYHV]UPDUSR (AUTILIS) !Other
  VATRAT DCB*3.6(10) Rate
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block

## PBDCONFIG (PBDCNF) - Payment balance configuration
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDCNF0 CODE+LEG; PBDCNF1 LEG+GRPORCPY+LEDTYP+ROOTACC (D)
Fields:
  AMOUNT M*4 Amount [menu 3643: 1=Original transaction currency,2=Ledger currency]
  AMTLIMIT MD1 Limit
  AMTTYPE M*6 Amount type [menu 243: 1=Exclude tax,2=Include tax]
  AUUID AUUID Single identifier
  COA COA Chart of accounts -> [COA]COA0 =COA (GCOA) !Block
  CODE A*20 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDCNF]CREUSR (AUTILIS) !Other
  GRPORCPY CPY Group+company code -> [CPY]CPY0 =[PBDCNF]GRPORCPY (COMPANY) !Block
  LEDTYP MM*15 Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  PROCESSTYPE M*4 Process type [menu 3644: 1=Payments,2=Open items,3=Both]
  ROOTACC A*200 Triggering account
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDCNF]UPDUSR (AUTILIS) !Other

## PBDCONFIGD (PBDCNFD) - Payment balance configuration
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDCNFD0 CODE+LEG+ISINCLUDED+LINE
Fields:
  ACCSIGN M*15 Sign [menu 610: 1=Debit,2=Credit,3=Unspecified]
  AUUID AUUID Single identifier
  BALAMT M*4 Balance used [menu 1: 1=No,2=Yes]
  BPGROUP PBDBPG BP group
  COA COA Chart of accounts -> [COA]COA0 =COA (GCOA) !Block
  CODE A*20 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDCNFD]CREUSR (AUTILIS) !Other
  CROOTACC A*15 Account root
  DOCTYPE GTE Document type -> [GTE]GTE0 =[PBDCNFD]DOCTYPE (GTYPACCENT) !BSRA
  ISINCLUDED M*4 Included/excluded [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  LINE C*4 Line
  NOTES A*60 Notes
  ORIENT M*4 Orientation [menu 3645: 1=Credit=incoming and debit=outgoing,2=Credit=outgoing and debit=incoming]
  PBDECO PBDECO Economic reason code -> [PBDECO]PBDECO0 =PBDECO;LEG (PBDECOCOD) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDCNFD]UPDUSR (AUTILIS) !Other

## PBDECODITM (PBDEIT) - Economic reason by product
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDEIT0 LEG+ITM
Fields:
  AUUID AUUID Single identifier
  COD PBDECO Economic reason code -> [PBDECO]PBDECO0 =COD;LEG (PBDECOCOD) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDEIT]CREUSR (AUTILIS) !Other
  ITM ITM Product -> [ITM]ITM0 =[PBDEIT]ITM (ITMMASTER) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LIN C*3 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDEIT]UPDUSR (AUTILIS) !Other

## PBDGEN (PBDGEN) - Payment balance declaration
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDGEN0 CODE
Fields:
  AUUID AUUID Single identifier
  CODE A*20 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDGEN]CREUSR (AUTILIS) !Other
  DATEFROM DDB Start date
  DATETO DDF End date
  EXPORTED M*4 Exported [menu 1: 1=No,2=Yes]
  GRPORCPY A*5 Group+company code
  ISGRP C*4 Group
  LEDTYP MM*15 Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Other
  PBDCCODE A*20 Code
  POSTED M*4 Posted [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDGEN]UPDUSR (AUTILIS) !Other

## PBDGEND (PBDGEND) - Payment balance decl details
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDGEND0 CODE+LEG+ISDETAIL+ISOITEM+LINE
Fields:
  ACCCRY CRY Account country -> [TCY]TCY0 =[PBDGEND]ACCCRY (TABCOUNTRY) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ Unique number
  ACCTYP M*4 Account type [menu 3650: 1=Internal bank account,2=External bank account,3=Other external account,4=Compensation account,5=Without account transactions]
  ACTCRY CRY Active country -> [TCY]TCY0 =[PBDGEND]ACTCRY (TABCOUNTRY) !Block
  AMOUNT MD1 Amount
  AUUID AUUID Single identifier
  BALFLG M*4 Balance used [menu 1: 1=No,2=Yes]
  BIDNUM A*20 Bank acct. number
  BPR BPR BP -> [BPR]BPR0 =[PBDGEND]BPR (BPARTNER) !Block
  BPRCRY CRY BP country -> [TCY]TCY0 =[PBDGEND]BPRCRY (TABCOUNTRY) !Block
  CODE A*20 Code
  COUPAR A*50 Contra account
  COUPARCRY CRY Contra account country -> [TCY]TCY0 =[PBDGEND]COUPARCRY (TABCOUNTRY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDGEND]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[PBDGEND]CUR (TABCUR) !Block
  DOCNUM VCR Document number
  DOCTYP A*5 Document type
  DUEDAT D Due date
  ECOCOD PBDECO Economic reason code -> [PBDECO]PBDECO0 =ECOCOD;LEG (PBDECOCOD) !Block
  ECODES A*140 Econ reason descr.
  ECOTYP M Economic reason type [menu 3641: 1=Not used,2=Service,3=Capital flow,4=Transit trade]
  EUVATN A*9 EU VAT w/o country
  FLG M*4 Line flag [menu 3649: 1=Create,2=Delete,3=Modify]
  INFO A*40 Additional info
  ISDETAIL M*4 Detail [menu 1: 1=No,2=Yes]
  ISIN A*40 ISIN/Chapter no.
  ISOITEM M*4 Open item / payment [menu 1: 1=No,2=Yes]
  ISSCURR A*40 Issue currency
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  LINE C*4 Line
  NOMAMT MD1 Nominal value
  NOTES A*100 Notes
  NPC A*20 Entity fiscal number
  NPC2 A*20 Entity fiscal number 2
  ORIENT M*15 Orientation [menu 3645: 1=Credit=incoming and debit=outgoing,2=Credit=outgoing and debit=incoming]
  ORIENTCFG M*15 Orientation [menu 3645: 1=Credit=incoming and debit=outgoing,2=Credit=outgoing and debit=incoming]
  TYPAMT A*1 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDGEND]UPDUSR (AUTILIS) !Other

## PBDUICONF (PBDUIC) - Payment balance field settings
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDUIC0 LEG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDUIC]CREUSR (AUTILIS) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDUIC]UPDUSR (AUTILIS) !Other

## PBDUICONFD (PBDUID) - Payment balance field lines
Notes: activity code PBDCL
Keys (first = PK; D = duplicates allowed): PBDUID0 LEG+LIN
Fields:
  ADI323 ADI Misc -> [ADI]CODE =323;ADI323 (ATABDIV) !Block
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PBDUID]CREUSR (AUTILIS) !Other
  DES AXX Description
  FLD AVA Field
  GRPBYS M*4 Group by [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Delete
  LIN L*8 Line number
  ORDITM C*4 Disp order open item
  ORDPAY C*4 Disp order payments
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PBDUID]UPDUSR (AUTILIS) !Other

## PRJFAS (PJF) - Assets
Notes: activity code GDFAS
Keys (first = PK; D = duplicates allowed): PJF0 PRJ+LIG
Fields:
  AMTSALPRV MD1 Projected amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJF]CREUSR (AUTILIS) !Other
  FAS A*30 Assets
  LIG C*3 Line number
  LOTFAS A*5 Lot
  PRJ PRJ Project -> [PRJ]PRJ0 =[PJF]PRJ (PROJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJF]UPDUSR (AUTILIS) !Other

## PRJLOT (PJL) - Lot
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): PJL0 PRJ+LOT
Fields:
  ACTDAT D In service date
  AMTLOT MD1 Amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PJL]CREUSR (AUTILIS) !Other
  CURLOT CUR Currency -> [TCU]TCU0 =[PJL]CURLOT (TABCUR) !Block
  DESLOT DES Description
  FASGRP A*20 Fixed asset group
  FCY FCY Site -> [FCY]FCY0 =[PJL]FCY (FACILITY) !Block
  FINMOD ADI Funding mode -> [ADI]CODE =348;FINMOD (ATABDIV) !Block
  LOT A*5 Lot
  PRJ PRJ Project -> [PRJ]PRJ0 =[PJL]PRJ (PROJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PJL]UPDUSR (AUTILIS) !Other

## PRMDADSU (PRM) - Extraction parameterization
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): PRM0 CPY
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PRM]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PRM]CREUSR (AUTILIS) !Other
  DCLCRN CRT Site registration number
  DCLDOMCOD ADI Intervention area -> [ADI]CODE =367;DCLDOMCOD (ATABDIV) !Block
  DCLFCY FCY Reporting site -> [FCY]FCY0 =[PRM]DCLFCY (FACILITY) !Block
  DCLFCYADD ADR Declaring site address
  DCLFCYCNT CNT Declarant contact
  DENADD ADR Ship-to address
  DENCNT CNT Recipient contact
  DENCODCOM M*15 Report sending method [menu 881: 1=Email,2=Paper material by postal mail]
  DENFCY FCY Ship-to site -> [FCY]FCY0 =[PRM]DENFCY (FACILITY) !Block
  MAICRN CRT Site registration number
  MAIFCY FCY Headquarters site -> [FCY]FCY0 =[PRM]MAIFCY (FACILITY) !Block
  MAIFCYADD ADR Headquarters site address
  MAIFCYCNT CNT Headquarters contact
  NATFIL ADI Nature of declaration -> [ADI]CODE =368;NATFIL (ATABDIV) !Block
  OPTFIL ADI Characteristics -> [ADI]CODE =367;OPTFIL (ATABDIV) !Block
  TOTNUMYEA L*8 Annual headcount
  TYPFIL ADI Type of declaration -> [ADI]CODE =366;TYPFIL (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PRM]UPDUSR (AUTILIS) !Other

## PROJET (PRJ) - Project
Notes: activity code GDD
Keys (first = PK; D = duplicates allowed): PRJ0 PRJ
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[PRJ]ACS (ACCCOD) !Block
  AIM ADI Objective -> [ADI]CODE =347;AIM (ATABDIV) !Block
  AMTEVAL MDC Estimated amount
  AMTFIN MD0(10) Financed amount
  AMTPRV MD0(24) Projected amount
  AUUID AUUID Single identifier
  BPRFIN BPR(10) BP -> [BPR]BPR0 =[PRJ]BPRFIN (BPARTNER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[PRJ]CUR (TABCUR) !Block
  DESLNG ACB Description
  DESTRA AX3 Description
  EXPNUM L*8 Export number
  GCF A*5 Group
  INVTYP ADI Project type -> [ADI]CODE =346;INVTYP (ATABDIV) !Block
  PEREND D(24) End
  PERSTR D(24) Start
  PRJ PRJ Project -> [PRJ]PRJ0 =[PRJ]PRJ (PROJET) !Delete
  REAEND D Completion end
  REASTR D Completion start
  SHOTRA AX1 Short description
  STUEND D Study end
  STUSTR D Study start
  TSI ADI Statistical group -> [ADI]CODE =indice+341;TSI(indice) (ATABDIV) !Block act:STB
  TYP AT Document type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change author
  USR AUS Supervisor -> [AUS]CODUSR =[PRJ]USR (AUTILIS) !Block

## PYHCAS (PCH) - Treasury interface
Notes: activity code CASIN
Keys (first = PK; D = duplicates allowed): PCH1 REGNUM+ACCNUM+REGLIN (D); PCH2 NUMPCH (D); PCH3 REGNUM+RVSACCNUM+REGLIN (D)
Fields:
  ACC GAC Account -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCDAT D Accounting date
  ACCNUM UNQ Internal number
  AMTBAN MD1 Bank amount
  AMTCUR MD1 Operation amount
  AUUID AUUID Single identifier
  BAN BAN Bank -> [BAN]BAN0 =[PCH]BAN (BANK) !Block
  BPR BPR BP -> [BPR]BPR0 =[PCH]BPR (BPARTNER) !Block
  BUDG A*128 Setup
  CDC A*128 Setup
  CHQNUM A*15 Check number
  COA COA Chart of accounts -> [COA]COA0 =[PCH]COA (GCOA) !Block
  CODRIF A*128 Setup
  CPTA A*128 Setup
  CPY CPY Company -> [CPY]CPY0 =[PCH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PCH]CUR (TABCUR) !Block
  CURBAN CUR Account currency -> [TCU]TCU0 =[PCH]CURBAN (TABCUR) !Block
  DAT D Date
  DATPCH D Date
  DESCR A*128 Setup
  DOPE D Operation date
  DUDDAT D Due date
  FCY FCY Site -> [FCY]FCY0 =[PCH]FCY (FACILITY) !Block
  FIC FIC*30 File
  FLG M*4 Indicator [menu 1: 1=No,2=Yes]
  FRMNUM VCR Slip no.
  ISOCOD A*3 ISO code
  LCR A*128 Parameters
  NASS A*128 Check number
  NUMPCH L*8 Identifier
  NUMVCR VCR Accounting document
  PAM TAM Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PAYTYP TPY Payment type -> [TPY]TPY0 =PAYTYP;[V]GSUPCLE (TABPAYTYP) !Block
  REF A*128 Parameters
  REFXRT A*128 Setup
  REGLIN UNQ Line number
  REGNUM VCR Payment no.
  RVSACCNUM UNQ Reversal
  SAC SAC Control
  SNS C*2 Sign
  TRANS A*128 Parameters
  TRECOD A*16 Treasury interface
  TYPVCR GTE Entry type -> [GTE]GTE0 =TYPVCR;[V]GSUPCLE (GTYPACCENT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PCH]UPDUSR (AUTILIS) !Other
  VALDAT D Value date

## REPLINDEF (RLI) - TaxUID management
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): RLI0 LEG+RECTYP+COD; RLI1 LEG+RECTYP (D); RLI2 COD (D)
Fields:
  AUUID AUUID Single identifier
  COD A*8 Code
  COD2 A*8 Code 2
  CODDES A*80 Description
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RLI]CREUSR (AUTILIS) !Other
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  RECTYP M*30 Record type [menu 3614: 1=VAT declaration,2=Recapitulative statement]
  TYPDES DES Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RLI]UPDUSR (AUTILIS) !Other

## SPAMOD111 (SPM111) - Spanish form 111
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM111 CPY+FIY+PER+NUMDECL
Fields:
  ADEDUCIR DCB*10.2 To be deducted
  AUUID AUUID Single identifier
  COMPJUST A*13 Previous supporting document
  CPY CPY Company -> [CPY]CPY0 =[SPM111]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM111]CREUSR (AUTILIS) !Other
  CUENING A*10 Bank account
  DECLNEG M*4 Negative declaration [menu 1: 1=No,2=Yes]
  DIA A*2 Day
  DIGCOING A*2 Check digit
  ENTING A*4 Entity
  FIY A*4 Fiscal year
  FORMPAG M*15 Payment method [menu 2111: 1=En metálico,2=Cargado a cuenta]
  IBAN A*4 IBAN code
  IMP11 DCB*10.2 Cash amount from prof. activity
  IMP12 DCB*10.2 In-kind amount from prof. activity
  IMP21 DCB*10.2 Cash amount from business activity
  IMP22 DCB*10.2 In-kind amount from business activity
  IMP31 DCB*10.2 Winnings amount in cash
  IMP32 DCB*10.2 Winnings amount in kind
  IMP41 DCB*10.2 Cash amount from capital gains
  IMP42 DCB*10.2 In-kind amount from capital gains
  IMP51 DCB*10.2 Fee amount from image rights
  IMPING DCB*10.2 Revenue amount
  LOCALIDA A*16 City
  MES A*10 Month
  MODEL A*3 Form
  NIF A*9 Company tax ID no.
  NUM11 C*4 Recipients of prof. act. in cash
  NUM12 C*4 Recipients of prof. act. in kind
  NUM21 C*4 Recipients of business act. in cash
  NUM22 C*4 Recipients of bus. act. in kind
  NUM31 C*4 Recipients of winnings in cash
  NUM32 C*4 Recipients of winnings in kind
  NUM41 C*4 Recipients of capital gains in cash
  NUM42 C*4 Recipients of capital gains in kind
  NUM51 C*4 Recipients of image rights fees
  NUMDECL C*4 Declaration number
  PER A*2 Period
  RAZSOC A*30 Company name
  RESUL DCB*10.2 Result
  RESULDEC DCB*10.2 Amount to be deposited
  RET11 DCB*10.2 Withholding from prof. act. in cash
  RET12 DCB*10.2 Withholding from prof act. in kind
  RET21 DCB*10.2 Withholding from bus. act. in cash
  RET22 DCB*10.2 Withholding from bus. act. in kind
  RET31 DCB*10.2 Withholding from winnings in cash
  RET32 DCB*10.2 Withholding from winnings in kind
  RET41 DCB*10.2 Wht. from capital gains in cash
  RET42 DCB*10.2 Wht. from capital gains in kind
  RET51 DCB*10.2 Withholding from image rights fees
  SUCURING A*4 Branch
  TIPDEC ADI Declaration type -> [ADI]CODE =318;TIPDEC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM111]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD115 (SPM115) - Spanish form 115
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM115 CPY+FIY+PER+NUMDECL
Fields:
  ADEDUCIR DCB*11.2 To be deducted
  AUUID AUUID Single identifier
  CNOMBRE A*4 First name start
  CODADM L*5 Agency
  CODELECT A*16 Digital code
  CODPOSTAL A*5 Postal code
  COMPJUST A*13 Previous supporting document
  CONTACTO A*100 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM115]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM115]CREUSR (AUTILIS) !Other
  CUENTAING A*10 Bank account no.
  DIA A*2 Day
  DIGCONTING A*2 Check digit
  ENTIDADING A*4 Entity
  ESCALERA A*2 Staircase
  FIY A*4 Fiscal year
  FORMPAG M*15 Payment method [menu 2111: 1=En metálico,2=Cargado a cuenta]
  IBAN A*4 IBAN code
  IMP11 L*6 Number of recipients
  IMP12 DCB*11.2 Retained amount
  IMP21 DCB*11.2 Withholdings
  LOCALIDAD A*20 Locality
  MES A*10 Month
  MODEL A*3 Form
  NIF A*9 Company tax ID no.
  NOMBRE M*4 Number [menu 1: 1=No,2=Yes]
  NOMBREVIA A*17 Street
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  OBSERVACI1 A*100 Notes 1
  OBSERVACIO A*250 Notes
  PAGCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  PAGINA A*2 Page
  PER A*2 Period
  PISO A*2 Floor
  PROVINCIA A*15 Province
  PUERTA A*2 Door
  RAZSOC A*30 Company name
  RESULDEC DCB*11.2 Amount to be deposited
  RESULTADO DCB*11.2 Result
  SUCURSAING A*4 Branch
  TELEFONO A*9 Telephone
  TIPDEC ADI Declaration type -> [ADI]CODE =318;TIPDEC (ATABDIV) !Block
  TIPOVIA A*2 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM115]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD123 (SPM123) - Spanish form 123
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM123 CPY+FIY+PER+NUMDECL
Fields:
  ADEDUCIR DCB*11.2 To deduct
  AUUID AUUID Single identifier
  CNOMBRE A*4 First name start
  CODADM L*5 Agency
  CODELECT A*16 Digital code
  CODPOS A*5 Postal code
  COMPJUST A*13 Previous supporting document
  CONTACTO A*100 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM123]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM123]CREUSR (AUTILIS) !Other
  CUENING A*10 Bank account
  DIA A*2 Day
  DIGCOING A*2 Check digit
  ENTING A*4 Entity
  ESCALERA A*2 Staircase
  FIY A*4 Fiscal year
  FORMPAG M*15 Payment method [menu 2111: 1=En metálico,2=Cargado a cuenta]
  IMP11 L*6 Number of recipients
  IMP12 DCB*11.2 Amount
  IMP21 DCB*11.2 Retained amount
  IMP31 DCB*11.2 Previous FY amount
  IMP32 DCB*11.2 Adjustment
  LOCALIDA A*20 Locality
  MES A*10 Month
  MODELO A*3 Form
  NIF A*9 Company tax ID no.
  NOMBRE A*15 Name
  NOMBVIA A*17 Street
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  OBSERVA A*250 Notes
  OBSERVA1 A*100 Notes 1
  PAGCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  PAGINA A*2 Page
  PER A*2 Period
  PISO A*2 Floor
  PROVIN A*15 Province
  PUERTA A*2 Door
  RAZSOC A*30 Company name
  RESUL DCB*11.2 Result
  RESULDEC DCB*11.2 Amount to be deposited
  SUCURING A*4 Branch
  TELEFONO A*9 Telephone
  TIPOVIA A*2 Type
  TOTAL1 DCB*11.2 Total withholdings
  TYPDEC ADI Declaration type -> [ADI]CODE =1214;TYPDEC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM123]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD190 (SPM190) - Spanish form 190
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM190 CPY+FIY+PER+NUMDECL
Fields:
  ADMINIST A*20 Agency
  AUUID AUUID Single identifier
  CARGO A*35 Role
  CODADM L*5 Agency
  CODPOS A*5 Postal code
  COMPLEM M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  CONTACTO A*100 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM190]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM190]CREUSR (AUTILIS) !Other
  EDEVENGO A*4 Accrual FY
  FIRMANTE A*100 Signer
  FIY A*4 Fiscal year
  FPRESENT D Send date
  LOCALIDA A*20 Locality
  MODELO A*3 Form
  NIF A*9 Company tax ID no.
  NIFP A*9 Tax identification
  NJUSTIFI A*15 Supporting document no.
  NOMBRE A*15 Name
  NOMBREVIA A*17 Street
  NPERCEPT C*4 Beneficiaries
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  NUMDECLA A*13 Declaration number
  PAGCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  PAGINA A*2 Page
  PER A*2 Period
  PROVIN A*15 Province
  RAZSOC A*30 Company name
  SUSTITU M*4 Replacement [menu 1: 1=No,2=Yes]
  TELEFONO A*9 Telephone
  TIPOVIA A*2 Type
  TIPSOP M*15 Media type [menu 2112: 1=Telematic,2=CD-R,3=Form]
  TOTBASES DCB*11.2 Total payments received
  TOTRETEN DCB*11.2 Withholding total
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM190]UPDUSR (AUTILIS) !Other

## SPAMOD1901 (SPM1901) - Spanish form 190 details
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM1901 CPY+FIY+PER+NUMDECL+NIFP+CLAVE+SUBCLAVE
Fields:
  AD35E C*1 Disabled asc. 33-65 (whole unit)
  AD35T C*1 Disabled ascendant 33-65 y-o.
  AD65E C*1 Disabled asc. >= 65 (whole unit)
  AD65T C*1 Disabled ascendant >= 65 y-o.
  ADMRE C*1 Disabled asc. red. mob. (whole un)
  ADMRT C*1 Disabled asc. reduced mobility
  AM75E C*1 Ascendant < 75 y-o. (whole unit)
  AM75T C*1 Ascendant >= 75 y-o.
  AMI75E C*1 Ascendant >= 75 y-o. (whole unit)
  AMI75T C*1 Ascendant >= 75 y-o.
  ANUALID DCB*9.2 Yearly alimony
  AUUID AUUID Single identifier
  CLAVE A*1 Key
  CODADM L*5 Agency
  CODPOS A*5 Postal code
  CODPROV A*2 Province code
  COMUNICA M*4 Communication to main residence [menu 1: 1=No,2=Yes]
  CONTACTO A*100 Person to contact
  CONTADOR C*4 Sequence number
  CONTRATO C*1 Contract or employment relationship
  CPY CPY Company -> [CPY]CPY0 =[SPM1901]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM1901]CREUSR (AUTILIS) !Other
  DD35E C*2 Disabled desc. 33-65 (whole unit)
  DD35T C*2 Disabled descendant 33-65 y-o.
  DD65E C*2 Disabled desc. >= 65 (whole unit)
  DD65T C*2 Disabled descendant >= 65 y-o.
  DDMRE C*2 Disabled desc. red. mob. (whole un)
  DDMRT C*2 Disabled desc. reduced mobility
  DISCAP C*1 Disability
  DM3E C*1 Descendant < 3 y-o. (whole unit)
  DM3T C*1 Descendant < 3 y-o.
  DRE C*2 Desc. reduced mobility (whole unit)
  DRT C*2 Descendant with reduced mobility
  EDEVENGO A*4 Accrual FY
  FIY A*4 Fiscal year
  GASTOS DCB*9.2 Expenses
  HIJO1 M*12 Child 1 [menu 2114: 1=No,2=Whole unit,3=Half unit]
  HIJO2 M*12 Child 2 [menu 2114: 1=No,2=Whole unit,3=Half unit]
  HIJO3 M*12 Child 3 [menu 2114: 1=No,2=Whole unit,3=Half unit]
  ICINCLAB DCB*11.2 Payment on account for incapacity
  INCLAB DCB*11.2 Incapacity allowance
  INGREF DCB*9.2 Performed deposits
  INGRRE DCB*9.2 Collected deposits
  LOCALIDA A*16 Locality
  MODELO A*3 Form
  MOVILIDA M*4 Geographic mobility [menu 1: 1=No,2=Yes]
  NACIMIEN C*4 Year of birth
  NIF A*9 Company tax ID no.
  NIFCONY A*9 Spouse TIN
  NIFP A*9 Tax identification
  NIFREP A*9 Representative TIN
  NJUSTIFI A*15 Supporting document no.
  NOMBRE A*15 Name
  NOMBVIA A*17 Street
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  PAGCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  PAGINA A*2 Page
  PENSION DCB*9.2 Compensatory allowance
  PER A*2 Period
  PERCEPCI DCB*11.2 Total payments received
  PROVIN A*15 Province
  RAZSOCP A*30 Beneficiary
  REDUCCIO DCB*9.2 Reduction
  RENTAS M*4 Ceuta/Melilla [menu 1: 1=No,2=Yes]
  RETENCIO DCB*11.2 Withholdings
  RINCLAB DCB*11.2 Withholding on incapacity
  SITUACIO C*1 Marital status
  SUBCLAVE C*2 Subkey
  TELEFONO A*9 Telephone
  TIPOVIA A*2 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM1901]UPDUSR (AUTILIS) !Other
  VALORACI DCB*11.2 In-kind valuation

## SPAMOD193 (SPM193) - Spanish form 193
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM193 CPY+FIY+NUMDECL
Fields:
  AUUID AUUID Single identifier
  CODPOS A*5 Postal code
  CONTACTO A*40 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM193]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM193]CREUSR (AUTILIS) !Other
  DECCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  DECLANT A*13 Previous declaration
  DECSUST M*4 Replacement [menu 1: 1=No,2=Yes]
  DIA A*2 Day
  FIY A*4 Fiscal year
  GASTOS DCB*9.2 Expenses
  IMP11 L*6 Number of recipients
  IMP12 DCB*11.2 Withholding bases
  IMP13 DCB*11.2 Withholdings
  IMP14 DCB*11.2 Revenue withholdings
  IMP31 DCB*11.2 Previous FY amount
  IMP32 DCB*11.2 Adjustment
  LOCALIDA A*16 Locality
  MES A*10 Month
  MODELO A*3 Form
  NIF A*9 Company tax ID no.
  NOMBVIA A*17 Street
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  NUMJUST A*13 Supporting document number
  PROVIN A*15 Province
  RAZSOC A*30 Company name
  TELEFONO A*9 Telephone
  TYPDEC ADI Declaration type -> [ADI]CODE =318;TYPDEC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM193]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD1931 (SPM1931) - Spanish form 193_1
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM1931 CPY+FIY+NUMDECL+CONTADOR
Fields:
  AUUID AUUID Single identifier
  BASERET DCB*9.2 Withholding bases
  CLACOD A*2 Key code
  CLAPERC A*1 Key
  CODCUENT A*20 Bank account
  CODEMISO A*12 Issuer code
  COMPENSA DCB*9.2 Compensations
  CONTADOR C*4 Sequence number
  CPY CPY Company -> [CPY]CPY0 =[SPM1931]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM1931]CREUSR (AUTILIS) !Other
  EJEDEV C*4 Accrual FY
  FECHAFIN D Loan end date
  FECHAINI D Loan start date
  FIY A*4 Fiscal year
  GARANTIA DCB*9.2 Warranties
  IMPDEDUC DCB*9.2 Deductible amount
  IMPPERCE DCB*9.2 Received amount
  IMPRET DCB*9.2 Withholding
  INGANT DCB*9.2 Previous FY revenue
  MEDIADOR A*1 Mediator
  NATDECL A*1 Declaration nature
  NATURA A*2 Nature
  NIFPER A*9 Company tax ID no.
  NIFREP A*9 Representative TIN
  NUMDECL C*4 Declaration number
  PAGO A*1 Payment
  PENALIZA DCB*9.2 Penalty
  PENDIENT A*1 To be obtained
  PORRET DCB*2.2 Withholding %
  PROVIN A*15 Province
  RAZSOC A*30 Company name
  TIPCOD A*1 Code type
  TIPPERC C*1 Reception type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM1931]UPDUSR (AUTILIS) !Other

## SPAMOD1932 (SPM1932) - Spanish form 193_2
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM1932 CPY+FIY+NUMDECL+CONTADOR
Fields:
  AUUID AUUID Single identifier
  CONTADOR C*4 Sequence number
  CPY CPY Company -> [CPY]CPY0 =[SPM1932]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM1932]CREUSR (AUTILIS) !Other
  FIY A*4 Fiscal year
  GASTOS DCB*11.2 Expenses
  NIF A*9 Company tax ID no.
  NIFREP A*9 Representative TIN
  NUMDECL C*4 Declaration number
  RAZSOC A*30 Company name
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM1932]UPDUSR (AUTILIS) !Other

## SPAMOD216 (SPM216) - Spanish form 216
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM216 CPY+FIY+PER+NUMDECL
Fields:
  ADEDUCIR DCB*10 To deduct
  APELLIDO A*4 Surname
  AUUID AUUID Single identifier
  COMPJUST A*13 Previous supporting document
  CONTACTO A*100 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM216]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM216]CREUSR (AUTILIS) !Other
  CUENING A*10 Bank account
  DECLNEG M*4 Negative declaration [menu 1: 1=No,2=Yes]
  DIA A*2 Day
  DIGCOING A*2 Check digit
  ENTING A*4 Entity
  FIY A*4 Fiscal year
  FORMPAG M*15 Payment method [menu 2111: 1=En metálico,2=Cargado a cuenta]
  IMP11 DCB*10 Amount 1
  IMP12 DCB*10 Amount 2
  IMPING DCB*10 Revenue amount
  LOCALIDA A*16 Locality
  MES A*10 Month
  MODELO A*3 Form
  NIF A*9 Company tax ID no.
  NUM11 C*4 Recipients of prof. act. in cash
  NUM12 C*4 Recipients of prof. act. in kind
  NUMDECL C*4 Declaration number
  PER A*2 Period
  RAZSOC A*30 Company name
  RESUL DCB*11 Result
  RESULDEC DCB*10 Amount to be deposited
  RET11 DCB*10 Withholding from prof. act. in cash
  SUCURING A*4 Branch
  TELEFONO A*9 Telephone
  TIPDEC ADI Declaration type -> [ADI]CODE =318;TIPDEC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM216]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD296 (SPM296) - Spanish form 296
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM296 CPY+FIY+NUMDECL
Fields:
  AUUID AUUID Single identifier
  CODPOS A*5 Postal code
  CONTACTO A*40 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM296]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM296]CREUSR (AUTILIS) !Other
  DECANT A*13 Previous declaration
  DECCOMP M*4 Add. declaration page indicator [menu 1: 1=No,2=Yes]
  DECSUST M*4 Replacement [menu 1: 1=No,2=Yes]
  DIA A*2 Day
  FIY A*4 Fiscal year
  IMP11 L*6 Number of recipients
  IMP12 DCB*11.2 Withholding bases
  IMP13 DCB*11.2 Withholdings
  IMP14 DCB*11.2 Revenue withholdings
  LOCALIDA A*20 Locality
  MES A*10 Month
  MODELO A*3 Form
  NIF A*9 Company tax ID no.
  NIFREP A*9 Representative TIN
  NOMBVIA A*17 Street
  NUMCASA L*2 Street number
  NUMDECL C*4 Declaration number
  NUMJUST A*13 Supporting document number
  PROVIN A*15 Province
  RAZSOC A*30 Company name
  TELEFONO A*9 Telephone
  TYPDEC ADI Declaration type -> [ADI]CODE =318;TYPDEC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM296]UPDUSR (AUTILIS) !Other
  YEARDEC A*4 Declaration year

## SPAMOD2961 (SPM2961) - Spanish form 296_1
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM2961 CPY+FIY+NUMDECL+CONTADOR
Fields:
  AUUID AUUID Single identifier
  BASERET DCB*9.2 Withholding bases
  CIUDADNA A*35 Town/city of birth
  CLACOD C*1 Key code
  CLAPERC A*1 Key
  CLAVE A*1 Keywords
  CODCUENT A*20 Bank account
  CODEMISO A*12 Issuer code
  CODPOS A*5 Postal code
  COMPENSA DCB*9.2 Compensations
  CONTADOR C*4 Sequence number
  CPY CPY Company -> [CPY]CPY0 =[SPM2961]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM2961]CREUSR (AUTILIS) !Other
  DIRECC1 A*50 Address (1)
  DIRECC2 A*40 Address (2)
  EJEDEV C*4 Accrual FY
  FECHADEV D Submission date
  FECHAFIN D Loan end date
  FECHAINI D Loan start date
  FECHANAC D Date of birth
  FIY A*4 Fiscal year
  FJ A*1 P/L
  GARANTIA DCB*9.2 Warranties
  IMPRET DCB*9.2 Withholding
  MEDIADOR A*1 Mediator
  NATURA A*2 Nature
  NIFPAIS A*20 TIN in the country
  NIFPER A*9 Company tax ID no.
  NIFREP A*9 Representative TIN
  NUMDECL C*4 Declaration number
  PAGO C*1 Payment
  PAIS A*2 Country
  PAISFIS A*2 Country of residence
  PAISNAC A*2 Country of birth
  PENDIENT A*1 To be obtained
  POBLACIO A*30 Population
  PORRET DCB*2.2 Withholding %
  PROVIN A*15 Province
  RAZSOC A*30 Company name
  REMUNPRE DCB*9.2 Remuneration
  SUBCLAVE C*2 Subkey
  TIPCOD A*1 Code type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM2961]UPDUSR (AUTILIS) !Other

## SPAMOD303 (SPM303) - Spanish form 303
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM303 CPY+FIY+PER+NUMDECL
Fields:
  ADEDUCIR DCB*15.2 To deduct
  ATRADM DCB*3.2 Alloc. to TA
  ATRADMIMP DCB*15.2 Alloc. to TA amount
  AUUID AUUID Single identifier
  BASEDED DCB*15.2(10) Taxable bases
  BASIMPCI DCB*15.2 Taxable base IP
  BASIMPRE DCB*15.2(3) Taxable base ES
  BASIMPRG DCB*15.2(3) Taxable base GR
  BASISP DCB*10.2 Taxable base ISP
  CASILLA47 DCB*10.2 Box 47
  CASILLA48 DCB*10.2 Box 48
  CASILLA49 DCB*10.2 Box 49
  CASILLA50 DCB*10.2 Box 50
  CASILLA51 DCB*10.2 Box 51
  CASILLA52 DCB*10.2 Box 52
  CASILLA53 DCB*10.2 Box 53
  CASILLA54 DCB*10.2 Box 54
  CASILLA55 DCB*10.2 Box 55
  CASILLA56 DCB*10.2 Box 56
  CASILLA57 DCB*10.2 Box 57
  CASILLA62 DCB*10.2 Box 62
  CASILLA63 DCB*10.2 Box 63
  CASILLA74 DCB*10.2 Box 74
  CASILLA75 DCB*10.2 Box 75
  CDEREGS1 DCB*10.2 Derived annual tax
  CDEREGS2 DCB*10.2 Derived annual tax 2
  CODACT1 ADI Activity 1 -> [ADI]CODE =320;CODACT1 (ATABDIV) !Block
  CODACT2 ADI Activity 2 -> [ADI]CODE =320;CODACT2 (ATABDIV) !Block
  CODADM L*5 Tax office code
  COMAPE A*4 First name start
  COMPENSACI DCB*15.2 Compensation
  COMPLEMENT A*16 Digital code
  COMPLJUST A*13 Previous supporting document
  CONTACTO A*100 Person to contact
  COPECOR DCB*10.2 Accrued tax on ope.
  COPECOR2 DCB*10.2 Accrued tax on ope. 2
  COUMIN DCB*10.2 Minimum tax
  COUMIN2 DCB*10.2 Minimum tax 2
  CPY CPY Company -> [CPY]CPY0 =[SPM303]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM303]CREUSR (AUTILIS) !Other
  CSOPECOR DCB*10.2 Operations tax
  CSOPECOR2 DCB*10.2 Operations tax 2
  CSOPOPC1 DCB*10.2 Collected tax on ope.
  CSOPOPC2 DCB*10.2 Collected tax on ope. 2
  CUDERREGS DCB*10.2 Derived annual tax 3
  CUDERREGS2 DCB*10.2 Derived annual tax 4
  CUENTADEV A*10 Revenue bank account
  CUENTAING A*10 Bank account
  CUODEV1 DCB*10.2 Quota
  CUODEV2 DCB*10.2 Tax 2
  CUOISP DCB*10.2 Tax ISP
  CUOTACI DCB*15.2 Tax IP
  CUOTARE DCB*12.2(3) Tax ES
  CUOTARG DCB*15.2(3) Tax GR
  CUOTASANT DCB*15.2 Taxes to compensate
  DECCONJ DCB*15.2 Common statement
  DEVOTCRY DCB*10.2 Return collect. others
  DEVOTCRY2 DCB*10.2 Return collect. others 2
  DIA A*2 Day
  DIFERENCIA DCB*15.2 Difference
  DIGCONTDEV A*2 Revenue control digit
  DIGCONTING A*2 Check digit
  ENTIDADDEV A*4 Revenue entity
  ENTIDADING A*4 Entity
  ENTREIC DCB*15.2 Internal deliveries
  EPIGRAFE DCB*3.1 Epigraph IAE
  EPIGRAFE2 DCB*3.1 Epigraph IAE 2
  EXPORT DCB*15.2 Exports
  FIY A*4 Fiscal year
  FORMPAG ADI Payment method -> [ADI]CODE =319;FORMPAG (ATABDIV) !Block
  IMPMODULO2 DCB*9.2 Module amount 2
  IMPMODULOS DCB*9.2 Module amount
  IMPORTEDEV DCB*15.2 Returned amount
  IMPORTEING DCB*17.2 Collected amount
  INDCOMPLE M*4 Complementary declaration [menu 1: 1=No,2=Yes]
  INDCORTEM DCB*2.3 Activity correcting index
  INDCORTEM2 DCB*2.3 Activity correcting index 2
  INDCOU1 DCB*1.3 Correcting index
  INDCOU2 DCB*1.3 Correcting index 2
  INDPAG A*1 Complementary page
  INDSCORTE2 DCB*2.3 Correcting index 4
  INDSCORTEM DCB*2.3 Correcting index 3
  INGC1 DCB*10.2 Deposit on account
  INGC2 DCB*10.2 Collected on account 2
  INGCUEN DCB*10.2 Deposit on acct. (C-D)+E
  INGCUEN2 DCB*10.2 Deposit on acct. (C-D)+E 2
  INSRDM M*4 Registered in RDM [menu 1: 1=No,2=Yes]
  IVADED DCB*15.2(10) Deductible VATs
  LOCALIDAD A*16 Locality
  MES A*15 Month
  MODBAS DCB*10.2 Modified base
  MODCUO DCB*10.2 Modified tax
  MODELO A*3 Form
  MODULOS L*8 Modules
  MODULOS2 L*8 Modules 2
  NIF A*9 Company tax ID no.
  NOMBRE A*15 Name
  NUMDECL C*4 Declaration number
  OBSERVAC A*250 Notes
  OPERISP DCB*15.2 Operations ISP
  PAGINA A*2 Page
  PER A*2 Period
  PORCUOMIN DCB*2.3 % minimum tax
  PORCUOMIN2 DCB*2.3 % minimum tax 2
  PORINGC1 DCB*2.3 % deposit on account
  PORINGC2 DCB*2.3 % deposit on account 2
  PORINGCUE C*2 % deposit on acct. (C-D)+E
  PORINGCUE2 C*2 % deposit on acct. (C-D)+E 2
  RAZSOC A*30 Company name
  REDU DCB*10.2 Reductions
  REDU2 DCB*10.2 Reductions 2
  RESULDEC DCB*15.2 Amount to be deposited
  RESULT DCB*10.2 Result
  RESULT2 DCB*10.2 Result 2
  RESULTADO DCB*15.2 Amount GR
  SINACTIV M*4 No activity [menu 1: 1=No,2=Yes]
  SUCURSADEV A*4 Revenue branch
  SUCURSAING A*4 Branch
  TIPDEC ADI Declaration type -> [ADI]CODE =318;TIPDEC (ATABDIV) !Block
  TIPORE DCB*2.2(3) Type ES
  TIPORG DCB*2.2(3) Type GR
  TOTALDED DCB*15.2 Total deductible
  TOTALDEV DCB*15.2 Total accrued
  TOTBASMOD DCB*10.2 Total modified bases
  TOTCOUMOD DCB*10.2 Total modified taxes
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM303]UPDUSR (AUTILIS) !Other
  VOLING1 DCB*10.2 Volume of revenues
  VOLING2 DCB*10.2 Volume of revenues 2
  YEARDEC A*4 Declaration year

## SPAMOD349 (SPM349) - Spanish form 349
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM349 CPY+FIY+PER+NUMDECL
Fields:
  AUUID AUUID Single identifier
  CONTACTO A*40 Person to contact
  CPY CPY Company -> [CPY]CPY0 =[SPM349]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM349]CREUSR (AUTILIS) !Other
  CRN CRN Site tax ID no.
  DECCOM M*4 Add. declaration [menu 1: 1=No,2=Yes]
  DECLARADOS L*8 Number of declarants
  DECSUS M*4 Substitute [menu 1: 1=No,2=Yes]
  FIY A*4 Fiscal year
  IMPDECLARA DCB*10.2 Declared amount
  IMPRECTIFI DCB*10.2 Total amount
  NUMDECANT A*13 Previous supporting document
  NUMDECL C*4 Declaration number
  NUMDECLAR A*13 Previous declaration
  NUMRECTIF L*8 Number of amounts
  PER A*2 Period
  RAZSOCIAL A*40 Company name
  TELEFONO A*9 Telephone
  TIPOSOP M*4 Media type [menu 2112: 1=Telematic,2=CD-R,3=Form]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM349]UPDUSR (AUTILIS) !Other

## SPAMOD349D (SPM349D) - Spanish 349 form detail
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPM349 CPY+FIY+PER+NUMDECL+CONTADOR
Fields:
  AUUID AUUID Single identifier
  CLAOPE A*1 Operation key
  CONTADOR L*8 Sequence number
  CPY CPY Company -> [CPY]CPY0 =[SPM349D]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPM349D]CREUSR (AUTILIS) !Other
  CRNDECL A*17 Taxpayer TIN
  CRNDESFIN A*17 Final recipient TIN
  EJERRECT A*4 Correction
  FIY A*4 Fiscal year
  IMPDECLAR DCB*9.2 Declared amount
  IMPOPERAC DCB*9.2 Operation amount
  IMPRECTIF DCB*9.2 Corrected amount
  NUMDECL C*4 Declaration number
  PER A*2 Period
  PERRECT A*2 Correction period
  RAZSOCDEC A*40 BP name
  RAZSOCDECFIN A*40 Final recipient name
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPM349D]UPDUSR (AUTILIS) !Other

## SPAMODCPY (SPMDC) - Spanish forms by company
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPMDC CPY+CODE
Fields:
  ATRADM DCB*3.2 Alloc. to TA
  AUUID AUUID Single identifier
  CODADM L*5 Agency
  CODE SPMOD Spanish forms -> [SPMOD]SPMOD =[SPMDC]CODE (SPAMODELS) !Delete
  CPY CPY Company -> [CPY]CPY0 =[SPMDC]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPMDC]CREUSR (AUTILIS) !Other
  DESMOD A*100 Description
  INSRDM M*4 Registered in RDM [menu 1: 1=No,2=Yes]
  PER M*15 Periodicity [menu 2110: 1=Monthly,2=Quarterly,3=Yearly,4=Bi-monthly,5=Not periodic]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPMDC]UPDUSR (AUTILIS) !Other

## SPAMODELS (SPMOD) - Spanish forms
Notes: activity code KSP; not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SPMOD CODE
Fields:
  AUUID AUUID Single identifier
  CODE A*6 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPMOD]CREUSR (AUTILIS) !Other
  DES A*100 Description
  DESSHO A*30 Short desc
  PER M*15 Periodicity [menu 2110: 1=Monthly,2=Quarterly,3=Yearly,4=Bi-monthly,5=Not periodic]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPMOD]UPDUSR (AUTILIS) !Other

## TABBUDTYP (TBU) - Budget transactions
Notes: differs in V9.0 P12 (diff: AT3_TABBUDTYP.htm)
Keys (first = PK; D = duplicates allowed): TBU0 BUDTYP+COLNUM; TBU1 BUDTYP+LINSELCRI (D)
Fields:
  AUUID AUUID Single identifier
  BUDCAT M*15 Budget category [menu 876: 1=Period,2=Account,3=Dimension]
  BUDTYP A*5 Transaction code
  COLDES DES Column title
  COLDESTRA AXX Column title
  COLEXP AFR*40 Expression
  COLEXP2 AFR*250 Expression result
  COLNUM C*2 Column number
  COLSAIAFF M*4 Visible [menu 1: 1=No,2=Yes]
  COLTYP M*15 Content [menu 875: 1=Quantity,2=Amount,3=Actual quantity,4=Actual amount,5=Quantity committed,6=Amount committed,7=Quantity precommitted,8=Amount precommitted,9=Formula,10=Text]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  DES DES Description
  DESSHO SHO Short description
  DESTRA AX3 Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  GFY AGC Company group -> [AGF]AGF0 =[TBU]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LINSELCRI C*4 Criterion line
  LODFLG M*4 Preloading [menu 1: 1=No,2=Yes]
  MAXDIENBR C*4 Max no. of dim. types
  NOMZON A*10 Destination fields
  SHOTRA AX1 Short description
  TOT M*4 Total [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## TABFILCASH (TFC) - Treasury file
Notes: activity code CASIN
Keys (first = PK; D = duplicates allowed): TFC1 MODULE+CODCAS+CODPAR; TFC2 MODULE+CODCAS (D); TFC3 MODULE+CODPAR+CODCAS
Fields:
  AUUID AUUID Single identifier
  CLCFOR AFR*250 Formulas
  CODCAS A*20 Zone code
  CODPAR A*10 Parameter code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABFILTDS (TFT) - Fee declaration file
Notes: activity code FEE2; differs in V9.0 P12 (diff: AT3_TABFILTDS.htm)
Keys (first = PK; D = duplicates allowed): TFT0 COD+RECTYP+NUM
Fields:
  AUUID AUUID Single identifier
  COD A*10 File
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESLIN DES Title
  DESSHO SHO Short description
  EXPNUM L*8 Export number
  FILREF A*2 File extension
  FLDTYP M*15 Field type [menu 11: 1=Alphanumeric,2=Numeric,3=Date,4=Local menu]
  FRM AFR*250 Formula
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LNG C*3 Length
  NUM C*2 Order no.
  RECTYP M*15 Record type [menu 696: 1=Start flag,2=Company header,3=Site header,4=Fee lines,5=Declaration site total +,6=Company total +,7=End flag]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TDSPRV (TPR) - Fee total/service supplier
Notes: activity code DAS
Keys (first = PK; D = duplicates allowed): TPR0 PRVNUM+CPY
Fields:
  AMTLOC MD1(12) Local currency amount
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[TPR]BPRNUM (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[TPR]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPR]CREUSR (AUTILIS) !Other
  HON M*15(12) Fee [menu 615: 1=Fees and vacations,2=Commissions,3=Brokerages,4=Rebates,5=Attendance tokens,6=Royalties,7=Inventor rights,8=Other payments,9=Indemnities and reimbursements,10=Perquisites,11=Withholding tax on income,12=Net tax on royalties]
  PRVNUM PRV Service supplier code -> [PRV]PRV0 =[TPR]PRVNUM (HONPRV) !Delete
  SENFCY FCY Sending branch -> [FCY]FCY0 =[TPR]SENFCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPR]UPDUSR (AUTILIS) !Other
  YEA C*4 Year

## TMPBLA (TBL) - Temporary print key table
Notes: differs in V9.0 P12 (diff: AT3_TMPBLA.htm)
Keys (first = PK; D = duplicates allowed): ARM0 NUMREQ+USR+RPTCOD+NUMLIG; ARM1 USR+RPTCOD (D)
Fields:
  ACCNUM UNQ Internal number
  AMT1 DCB*13.2 Amount
  AMT2 DCB*13.2 Amount
  AMT3 DCB*13.2 Amount
  AUUID AUUID Single identifier
  CCE1 CCE Dimension -> [CCE]CCE0 ="";CCE1 (CACCE) !Other
  CCE2 CCE Dimension -> [CCE]CCE0 ="";CCE2 (CACCE) !Other
  CCE3 CCE Dimension -> [CCE]CCE0 ="";CCE3 (CACCE) !Other
  CCE4 CCE Dimension -> [CCE]CCE0 ="";CCE4 (CACCE) !Other
  CCE5 CCE Dimension -> [CCE]CCE0 ="";CCE5 (CACCE) !Other
  CCE6 CCE Dimension -> [CCE]CCE0 ="";CCE6 (CACCE) !Other
  CCE7 CCE Dimension -> [CCE]CCE0 ="";CCE7 (CACCE) !Other
  CCE8 CCE Dimension -> [CCE]CCE0 ="";CCE8 (CACCE) !Other
  CCE9 CCE Dimension -> [CCE]CCE0 ="";CCE9 (CACCE) !Other
  CCEA CCE Dimension -> [CCE]CCE0 ="";CCEA (CACCE) !Other
  CCEB CCE Dimension -> [CCE]CCE0 ="";CCEB (CACCE) !Other
  CCEC CCE Dimension -> [CCE]CCE0 ="";CCEC (CACCE) !Other
  CLEN1 UNQ Numeric 1
  CLEN2 UNQ Numeric 2
  CLEN3 UNQ Numeric 3
  CLEN4 UNQ Numeric 4
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TBL]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TBL]CUR (TABCUR) !Other
  DET1 A*15
  DET2 A*15
  DET3 A*15
  DET4 A*15
  DET5 A*15
  DET6 A*15
  DET7 A*15
  DET8 A*30
  DET9 A*15
  DETA A*15
  DETB A*15
  DETC A*15
  FCY FCY Site -> [FCY]FCY0 =[TBL]FCY (FACILITY) !Other
  LIBCCE1 DES Description
  LIBCCE2 DES Description
  LIBCCE3 DES Description
  LIBCCE4 DES Description
  LIBCCE5 DES Description
  LIBCCE6 DES Description
  LIBCCE7 DES Description
  LIBCCE8 DES Description
  LIBCCE9 DES Description
  LIBCCEA DES Description
  LIBCCEB DES Description
  LIBCCEC DES Description
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  PEREND C*2(3) Period end
  PERSTR C*2(3) Period start
  RPTCOD ARP Report code -> [ARP]ARP0 =[TBL]RPTCOD (AREPORT) !Other
  TRICCE1 A*20
  TRICCE2 A*20
  TRICCE3 A*20
  TRICCE4 A*20
  TRICCE5 A*20
  TRICCE6 A*20
  TRICCE7 A*20
  TRICCE8 A*20
  TRICCE9 A*20
  TRICCEA A*20
  TRICCEB A*20
  TRICCEC A*20
  UOM UOM Unit -> [TUN]TUN0 =[TBL]UOM (TABUNIT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TBL]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TBL]USR (AUTILIS) !Other

## TMPCNVECAR (TCE) - Exch. rate temporary table
Keys (first = PK; D = duplicates allowed): TCE0 LEDTYP+SOC+SITE+NUM+DEV
Fields:
  AMT MD1(10) Amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[TCE]BPR (BPARTNER) !Delete
  CPTDES A*30 Destination account
  CPTORI A*30 Source account
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TCE]CREUSR (AUTILIS) !Other
  DAT D Date
  DEV A*3 Currency
  LEDTYP M Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  NUM C*3 Number
  SITE FCY Site -> [FCY]FCY0 =[TCE]SITE (FACILITY) !Delete
  SOC CPY Company -> [CPY]CPY0 =[TCE]SOC (COMPANY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TCE]UPDUSR (AUTILIS) !Other

## TMPGACCENTRD (TMPDAE) - Accounting entry lines
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): DAE2 ACCNUM; RPTUID RPTUID (D)
Fields:
  ACCNUM UNQ Unique number
  AMTVAT MD1 Declared amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TMPDAE]CREUSR (AUTILIS) !Other
  RPTUID A*50 Unique identification number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TMPDAE]UPDUSR (AUTILIS) !Other

## TMPGACCENTRY (TMPHAE) - Accounting entries
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): HAE0 TYP+NUM; RPTUID RPTUID (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TMPHAE]CREUSR (AUTILIS) !Other
  NUM VCR Document no.
  NUMDCL L*8 Declaration number
  RPTUID A*50 Unique identification number
  TYP GTE Entry type -> [GTE]GTE0 =[TMPHAE]TYP (GTYPACCENT) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TMPHAE]UPDUSR (AUTILIS) !Other

## TXSA (TXS) - Financial data extraction parameters
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXS1 TXSNAM; TXS0 LSTGRP+TXSNAM
Fields:
  ACCINF A*10 Information
  ACS ACS Access code -> [ACS]ACS0 =[TXS]ACS (ACCCOD) !RTZ
  ANALEDTYP M*20 Ana. ledger [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  AUTVER M*4 Auto numbering of versions [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPRINF A*10 Information
  CCEINF A*10 Information
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DETACC M*4 Account detail [menu 1: 1=No,2=Yes]
  DETBPR M*4 BP detail [menu 1: 1=No,2=Yes]
  DETCCE M*4 Dimension detail [menu 1: 1=No,2=Yes]
  FC A*60(3) Center text
  FCYINF A*10 Information
  FL A*60(3) Left text
  FR A*60(3) Right text
  GENLEDTYP M*10 Ledger type [menu 2644: 1=Legal,2=Analytical,3=IAS,4=Ledger 4,5=Ledger 5,6=Ledger 6,7=Ledger 7,8=Ledger 8,9=Ledger 9,10=Alternative Currency]
  GRPCOD A*15 Graph code
  GRPDES AX3 Group title
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LSTGRP A*8 Report group
  NBLIG C*4 Number of lines
  NBLIG1 C*4 Number of lines
  NBLIG2 C*4 Number of lines
  NBRCOL C*2 Number of columns
  NBVAR C*3 Number of variables
  NEGSTO M*4 Negative [menu 1: 1=No,2=Yes]
  RPTCOD ARP Report code -> [ARP]ARP0 =[TXS]RPTCOD (AREPORT) !RTZ
  TC A*60(3) Center text
  TL A*60(3) Left text
  TR A*60(3) Right text
  TXSDES AX3 Description
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =LSTGRP;TXSNAM (TXSA) !Delete
  TYPDOC M*15 Document type [menu 7806: 1=Unspecified,2=Text,3=Image,4=Office,5=Word,6=Excel,7=PowerPoint]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TXSAC (TXA) - Grid column setup
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXA0 TXSNAM+NUMCOL
Fields:
  AUUID AUUID Single identifier
  COLNUM A*20 Cumulative column
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DECCOL C*2 Decimals
  DIVCOL DCB*10 Divisor
  EFFCOL M*15 Print effect [menu 873: 1=Normal,2=Strikethrough,3=Underlined]
  FMTCOL M*15 Print style [menu 872: 1=Normal,2=Bold,3=Italic,4=Bold italic]
  NAMCOL AX3 Column name
  NUMCOL C*4 Column number
  SAICOL M*15 Entry mode [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXA]TXSNAM (TXSA) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TXSD (TXD) - Financial data extraction detail
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXD0 TXSNAM+LIG+COL; TXD1 TXSNAM+COL+LIG
Fields:
  AUUID AUUID Single identifier
  CEN M*4 Summary reporting [menu 1: 1=No,2=Yes]
  COL C*2 Column
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TXD]CREUSR (AUTILIS) !Other
  DECCOL C*2 Decimals
  DES AX3 Description
  EFFPRN M*15 Print effect [menu 873: 1=Normal,2=Strikethrough,3=Underlined]
  FMTPRN M*15 Print style [menu 872: 1=Normal,2=Bold,3=Italic,4=Bold italic]
  FRM A*250 Formulas
  LIG C*3 Line number
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXD]TXSNAM (TXSA) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TXD]UPDUSR (AUTILIS) !Other

## TXSM (TXM) - Amounts
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXM0 TXSNAM+VERSION+LIG+COL+IND
Fields:
  ACC GAC Account/nature -> [GAC]GAC0 =COA;ACC (GACCOUNT) !Block
  ACCINF A*30 Information
  AMTCDT A*25 Credit
  AMTDEB A*25 Debit
  AMTVAL A*50 Value
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[TXM]BPR (BPARTNER) !Delete
  BPRINF A*30 Information
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =DIE1;CCE1 (CACCE) !Delete
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =DIE2;CCE2 (CACCE) !Delete
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =DIE3;CCE3 (CACCE) !Delete
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =DIE4;CCE4 (CACCE) !Delete
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =DIE5;CCE5 (CACCE) !Delete
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =DIE6;CCE6 (CACCE) !Delete
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =DIE7;CCE7 (CACCE) !Delete
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =DIE8;CCE8 (CACCE) !Delete
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =DIE9;CCE9 (CACCE) !Delete
  CCEINF A*30 Information
  COA COA Chart code -> [COA]COA0 =[TXM]COA (GCOA) !Block
  COL C*2 Column
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TXM]CREUSR (AUTILIS) !Other
  DIE1 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE1 (GDIE) !Block
  DIE2 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE2 (GDIE) !Block
  DIE3 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE3 (GDIE) !Block
  DIE4 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE4 (GDIE) !Block
  DIE5 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE5 (GDIE) !Block
  DIE6 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE6 (GDIE) !Block
  DIE7 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE7 (GDIE) !Block
  DIE8 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE8 (GDIE) !Block
  DIE9 DIE Dimension type code -> [DIE]DIE0 =[TXM]DIE9 (GDIE) !Block
  FCY FCY Site -> [FCY]FCY0 =[TXM]FCY (FACILITY) !Delete
  FCYINF A*30 Information
  IND L*8 Index
  LIG C*3 Line number
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXM]TXSNAM (TXSA) !Delete
  TYPAMT C*4 Amount type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TXM]UPDUSR (AUTILIS) !Other
  UPDVAL A*30 User value
  VERSION A*15 Version

## TXSP (TXP) - Value parameters/version
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXP0 TXSNAM+VERSION+COL
Fields:
  AUUID AUUID Single identifier
  COL C*2 Column
  CPY CPY Company -> [CPY]CPY0 =[TXP]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TXP]CREUSR (AUTILIS) !Other
  CURPRN CUR Printing currency -> [TCU]TCU0 =[TXP]CURPRN (TABCUR) !Block
  CURSEL CUR Currency -> [TCU]TCU0 =[TXP]CURSEL (TABCUR) !Block
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[TXP]FCY (FACILITY) !Block
  NAMCOL A*30 Column name
  STRDAT D Start date
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXP]TXSNAM (TXSA) !Delete
  TYPMNT M*15 Movement type [menu 2665: 1=Movements + CR + Closing,2=Movements + CR,3=Movements + Closing,4=Movements only,5=CR only,6=Closing only]
  TYPRAT M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TXP]UPDUSR (AUTILIS) !Other
  VERSION A*15 Version

## TXSV (TXX) - Fin data extras variables
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXX0 TXSNAM+VERSION+VARNAM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TXX]CREUSR (AUTILIS) !Other
  LSTGRP A*8 Report group
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXX]TXSNAM (TXSA) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TXX]UPDUSR (AUTILIS) !Other
  VARDEF A*30 Default / value
  VARDES A*40 Description
  VARNAM A*10 Variable
  VARPAR A*10 Parameter
  VARTRA AX3
  VARTYP ATY Type -> [ATY]CODTYP =[TXX]VARTYP (ATYPE) !Block
  VARVAL A*30 Value
  VERSION A*15 Version

## TXSW (TXW) - Versions
Notes: activity code TDB
Keys (first = PK; D = duplicates allowed): TXW0 LSTGRP+TXSNAM+VERSION; TXW1 TXSNAM+VERSION
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[TXW]ACS (ACCCOD) !RTZ
  AUUID AUUID Single identifier
  CENDET M*4 Detail summary reporting [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DETACC M*4 Account detail [menu 1: 1=No,2=Yes]
  DETBPR M*4 BP detail [menu 1: 1=No,2=Yes]
  DETCCE M*4 Dimension detail [menu 1: 1=No,2=Yes]
  FC A*30(3) Center text
  FL A*30(3) Left text
  FR A*30(3) Right text
  GENDAT D Generation date
  GENTIM HS Generation time
  LSTGRP A*8 Report group
  NBVAR C*3 Number of variables
  TC A*30(3) Center text
  TL A*30(3) Left text
  TR A*30(3) Right text
  TXSNAM TXS Extraction code name -> [TXS]TXS1 =[TXW]TXSNAM (TXSA) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VERDES DES Description
  VERSION A*15 Version

## VATBOX (VTB) - VAT boxes
Notes: activity code DCL; differs in V9.0 P12 (diff: AT3_VATBOX.htm); differs in V10 P1 (diff: ATD_VATBOX.htm)
Keys (first = PK; D = duplicates allowed): VTB0 VATFNC+LEG+LIN; VTB1 VATFNC+LEG+VATBOX
Fields:
  AUUID AUUID Single identifier
  CLCFOR A*80 Totals formula
  CNDFOR M*15 Formula condition [menu 3656: 1=None,2=Positive balance,3=Negative balance]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VTB]CREUSR (AUTILIS) !Other
  DESTRA AXX Long title
  DESVATFNC AX3 Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LIN C*3 Line
  SHOTRA AX1 Short description
  TYPBOX M*4 Type [menu 3651: 1=Title,2=Detail,3=Total,4=Off declaration]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VTB]UPDUSR (AUTILIS) !Other
  VATBOX A*5 VAT boxes
  VATFNC AFC Function code -> [AFC]CODINT =[VTB]VATFNC (AFONCTION) !Block
  VLYEND D Validity end date
  VLYSTR D Validity start date

## VATBOXD (VTD) - VAT boxes
Notes: activity code DCL; differs in V9.0 P12 (diff: AT3_VATBOXD.htm); differs in V10 P1 (diff: ATD_VATBOXD.htm)
Keys (first = PK; D = duplicates allowed): VTD0 VATFNC+LEG+LIN+FLGVAT+VATIPT+VAT+VCRTYP+VLYSTR+VLYEND (D); VTD1 VATFNC+LEG+VCRTYP+FLGVAT+VATIPT+VAT+VLYSTR+VLYEND (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VTD]CREUSR (AUTILIS) !Other
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LIN C*3 Line
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VTD]UPDUSR (AUTILIS) !Other
  VAT VAT Tax code -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATBOX A*5 VAT boxes
  VATFNC AFC Function code -> [AFC]CODINT =[VTD]VATFNC (AFONCTION) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]
  VCRTYP GTE Entry type -> [GTE]GTE0 =VCRTYP;[V]GSUPCLE (GTYPACCENT) !Block
  VLYEND D Validity end date
  VLYSTR D Validity start date

## VATENTFRM (VEF) - VAT form (definition)
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VEF0 VATFRM+VATFNC+LEG
Fields:
  AMTVATCUR CUR Currency -> [TCU]TCU0 =[VEF]AMTVATCUR (TABCUR) !Block
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VEF]CREUSR (AUTILIS) !Other
  DEC C*4 Decimals
  DESTRA AXX Long title
  ENAFLG M*1 Active [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  SHOTRA AX1 Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VEF]UPDUSR (AUTILIS) !Other
  VATFNC AFC Declaration -> [AFC]CODINT =[VEF]VATFNC (AFONCTION) !Block
  VATFRM A*15 VAT form
  VLYENDDAT D4 Validity end date
  VLYSTRDAT D4 Validity start date

## VATENTFRMD (VEFD) - VAT form detail (definition)
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VEFD0 VATFRM+VATFNC+LEG+LIN; VEFD1 VATFRM+VATFNC+LEG+VATBOX
Fields:
  ASYCOD ASY Style -> [ASY]ASY0 =[VEFD]ASYCOD (ASTYLE) !Block
  AUUID AUUID Single identifier
  CLCFOR A*80 Formula
  CNDFOR M*15 Formula condition [menu 3656: 1=None,2=Positive balance,3=Negative balance]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VEFD]CREUSR (AUTILIS) !Other
  DESLIN AXX Description
  FLDTYP M*15 Format [menu 245: 1=Alphanumeric,2=Numeric,3=Date]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LIN C*3 Line
  TYPBOX M*4 Type [menu 3651: 1=Title,2=Detail,3=Total,4=Off declaration]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VEFD]UPDUSR (AUTILIS) !Other
  VATBOX A*5 VAT box
  VATFNC AFC Declaration -> [AFC]CODINT =[VEFD]VATFNC (AFONCTION) !Block
  VATFRM A*15 VAT form

## VATFRMENT (VFE) - VAT form (values)
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VFE0 VATENTNUM; VFE1 VATENTNUM+VATFNC+LEG+CODVATGRP; VFE3 CODVATGRP+VATFNC-DCLSTRDAT (D)
Fields:
  ALLFCY M*4 All sites [menu 1: 1=No,2=Yes]
  AMTVATCUR CUR Currency -> [TCU]TCU0 =[VFE]AMTVATCUR (TABCUR) !Block
  AUUID AUUID Single identifier
  CODVATGRP VATGRP VAT group -> [VATGH]VATGH0 =[VFE]CODVATGRP (VATGRP) !Block
  CPY CPY Company -> [CPY]CPY0 =[VFE]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VFE]CREUSR (AUTILIS) !Other
  DATPCE D Due date until
  DCLENDDAT D4 Validity end date
  DCLSTRDAT D4 Validity start date
  DEC C*4 Decimals
  DESTRA AXX Long title
  DETDCL M*4 Off declaration detail [menu 1: 1=No,2=Yes]
  DUEDAT D Due date
  ECRAUX M*4 Auxilliary postings only [menu 1: 1=No,2=Yes]
  ENDDAT D Declaration end date
  ENDDAT2 D Matching end date
  EXTSTRDAT D Starting from
  FCY FCY Site -> [FCY]FCY0 =[VFE]FCY (FACILITY) !Other
  GRPCPY AGF Company group -> [AGF]AGF0 =[VFE]GRPCPY (AGRPFCY) !Other
  INCUNXENT M*4 Inc unextrac entries [menu 1: 1=No,2=Yes]
  LASSBM ADATIM Last submission
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  PERKEY A*10 Period
  RESULT AC0*3 Result
  STA M*15 Status [menu 880: 1=In progress,2=Validated,3=Submitted,4=Rejected,5=Completed]
  STRDAT D Declaration start date
  STRDAT2 D Matching start date
  SUBDAT D
  TRCFLG M*4 Log [menu 1: 1=No,2=Yes]
  TYPGEN M*20 Generation [menu 2601: 1=Actual,2=Simulation]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VFE]UPDUSR (AUTILIS) !Other
  VAT M*4 Launch VAT on debit [menu 1: 1=No,2=Yes]
  VATBOX A*5 VAT boxes
  VATDCLYEA C*4 Year
  VATENTNUM VCR Declaration number
  VATFNC AFC Function code -> [AFC]CODINT =[VFE]VATFNC (AFONCTION) !Block
  VATFRM A*15 VAT form
  VATPAY M*4 Launch VAT payment [menu 1: 1=No,2=Yes]
  VATRTNTYP M*15 VAT declaration type [menu 883: 1=Monthly,2=Quarterly,3=Yearly]
  VERSION C*3 Version

## VATFRMENTA (VFEA) - VAT form
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VFEA0 VATENTNUM+VFEACPY+VATBOX+LIG
Fields:
  ADJLEV M*15 Level [menu 3706: 1=Company level,2=Entity level]
  AUUID AUUID Single identifier
  COMMENT A*250 Comment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VFEA]CREUSR (AUTILIS) !Other
  LIG L*8 Line
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VFEA]UPDUSR (AUTILIS) !Other
  VATAMTADJ MDD Adjustment
  VATBOX A*5 VAT boxes
  VATENTNUM VCR Declaration number
  VFEACPY CPY Company -> [CPY]CPY0 =[VFEA]VFEACPY (COMPANY) !Other

## VATFRMENTC (VFEC) - VAT form by company
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VFEC0 VATENTNUM+LIG; VFEC1 VATENTNUM+CPY+VATBOX
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[VFEC]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VFEC]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[VFEC]CUR (TABCUR) !Block
  LIG L*8 Line
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VFEC]UPDUSR (AUTILIS) !Other
  VATAMT MDD Extracted value
  VATAMTADJ MDD Adjustment
  VATBOX A*5 VAT boxes
  VATENTNUM VCR Declaration number

## VATFRMENTD (VFED) - VAT form detail (values)
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VFED0 VATENTNUM+LIN; VFED1 VATENTNUM+VATBOX
Fields:
  AUUID AUUID Single identifier
  CLCFOR A*80 Formula
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VFED]CREUSR (AUTILIS) !Other
  DESLIN AXX Description
  LIN C*3 Line
  TYPBOX M*4 Type [menu 3651: 1=Title,2=Detail,3=Total,4=Off declaration]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VFED]UPDUSR (AUTILIS) !Other
  VATAMT MDD Submitted value
  VATAMTADJ MDD Adjustment
  VATAMTDCL MDD Extracted value
  VATBOX A*5 VAT boxes
  VATENTNUM VCR Declaration number

## VATFRMENTN (VFEN) - VAT form queries
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VFEN0 VATENTNUM+SEQ; VFEN1 VATENTNUM+DCLVATTYP+NUMRPT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VFEN]CREUSR (AUTILIS) !Other
  DATMAX D Journal date
  DCLVATTYP M*15 VAT type [menu 204: 1=On debit,2=On payment]
  ENDDAT D End date
  LOGFIL TRA Log file
  NUMRPT L*8 Query no.
  OPT M*25 Option [menu 688: 1=VAT/debit allocated first,2=Pro rata]
  OPTDAT M*15 Date option [menu 687: 1=Accounting date,2=Document date]
  SEQ L*8 Sequence
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VFEN]UPDUSR (AUTILIS) !Other
  VATENTNUM VCR Declaration number

## VATGRP (VATGH) - VAT entity header
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VATGH0 CODVATGRP
Fields:
  AUUID AUUID Single identifier
  CODVATGRP A*15 VAT entity
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VATGH]CREUSR (AUTILIS) !Other
  DES DES Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  REM A*250 Notes
  SHO SHO Short description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VATGH]UPDUSR (AUTILIS) !Other

## VATGRPD (VATGD) - VAT entity details
Notes: activity code DCL
Keys (first = PK; D = duplicates allowed): VATGD0 CODVATGRP+LIN; VATGD1 CODVATGRP+CPY
Fields:
  AUUID AUUID Single identifier
  CODVATGRP A*15 VAT entity
  CPY CPY VAT member company -> [CPY]CPY0 =[VATGD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[VATGD]CREUSR (AUTILIS) !Other
  LIN L*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[VATGD]UPDUSR (AUTILIS) !Other
  VATHEA M*4 Head entity [menu 1: 1=No,2=Yes]

## VDGERRSP (RSP) - Recapitulative statem. param.
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): RSP0 LEG+VAT+TRNTYP; RSP1 LEG+VAT-STRDAT (D); RSP2 LEG+VAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RSP]CREUSR (AUTILIS) !Other
  CRY CRY -> [TCY]TCY0 =[RSP]CRY (TABCOUNTRY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  STRDAT D Start date
  TRNTYP REPLINDE Turnover type -> [RLI]RLI0 =LEG;2;TRNTYP (REPLINDEF) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RSP]UPDUSR (AUTILIS) !Other
  VACBPR TVB BP tax rule -> [TVB]TVB0 =VACBPR;LEG (TABVACBPR) !Block
  VAT VAT Rate 1 activation date -> [TVT]TVT0 =VAT;LEG (TABVAT) !Block

## VDGERTRP (TRPG) - German tax return parameter
Notes: activity code KDEAT
Keys (first = PK; D = duplicates allowed): TRPG0 LEG+VAT+LINENO; TRPG1 VAT+FLGVAT+VATIPT (D); TRPG2 VAT (D); TRPG3 FLGVAT+VATIPT (D); TRPG4 LEG+VAT (D); TRPG5 LEG+VAT+REPLINE+FLGVAT+VATIPT+STRDAT+ENDDAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TRPG]CREUSR (AUTILIS) !Other
  ENDDAT D End date
  FLGVAT M*15 Tax management [menu 608: 1=Not subjected,2=Subjected,3=Tax account,4=EU tax,5=Prepayment account]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LINENO C*4 Line no.
  REPLINE REPLINDE Report line -> [RLI]RLI0 =LEG;1;REPLINE (REPLINDEF) !Block
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TRPG]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;LEG (TABVAT) !Block
  VATIPT M*15 Tax allocation [menu 609: 1=Collected sales,2=Collected fixed assets,3=Deductible purchases,4=Deductible fixed assets,5=Deductible G&S,6=State rules,7=Company rules,8=Collected G & S]

## VDSWITRP (TRSP) - Switzerland
Notes: activity code KSW; differs in V10 P1 (diff: ATD_VDSWITRP.htm)
Keys (first = PK; D = duplicates allowed): TRSP0 LEG+VAT+NUMLIG; TRSP1 LEG+VAT+REPLIN; TRSP2 LEG+VAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TRSP]CREUSR (AUTILIS) !Other
  DATEND D End date
  DATSTR D Start date
  DIGIT L*8
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NUMLIG L*8 Line no.
  REPLIN M*4 [menu 3640: 27 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TRSP]UPDUSR (AUTILIS) !Other
  VAT VAT Tax -> [TVT]TVT0 =VAT;LEG (TABVAT) !Block

## WHTDTL (WDL) - WHT detail
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): WDL0 RPTNUM (D)
Fields:
  ACCDAT D Accounting date
  AMTATI MD1 Amount + tax
  AMTVAT MD1 Declared amount
  AUUID AUUID Single identifier
  BPR BPR BP -> [BPR]BPR0 =[WDL]BPR (BPARTNER) !Delete
  CPY CPY Company -> [CPY]CPY0 =[WDL]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WDL]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =FCY (FACILITY) !Block
  INVDAT D Invoice date
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LIN L*8 Line number
  NETPRINOT MD8 Net price - tax
  NUM VCR Document no.
  RPTNUM A*20 Report
  SNS C*2 Sign
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WDL]UPDUSR (AUTILIS) !Other
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  WCAT A*3 Category

## WHTHDR (WHR) - WHT header
Notes: activity code KAU; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): WHR0 RPTNUM; WHR1 STRDAT+ENDDAT+FCY+CPY+ALLFCY+ALLCPY (D)
Fields:
  ALLCPY M*4 All companies [menu 1: 1=No,2=Yes]
  ALLFCY M*4 All sites [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WHR]CREUSR (AUTILIS) !Other
  ENDDAT D End date
  FCY FCY Site -> [FCY]FCY0 =[WHR]FCY (FACILITY) !Delete
  NUM VCR Document no.
  RPTNUM A*20 Report
  RPTTYP M*15 Generation type [menu 2601: 1=Actual,2=Simulation]
  RUNDAT D Run date
  STRDAT D Start date
  TCPY CPY To company -> [CPY]CPY0 =[WHR]TCPY (COMPANY) !Other
  TFCY FCY To site -> [FCY]FCY0 =[WHR]TFCY (FACILITY) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WHR]UPDUSR (AUTILIS) !Other

