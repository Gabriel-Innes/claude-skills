<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Supervisor module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## AABREV (AAB) - Abbreviation
Keys (first = PK; D = duplicates allowed): AAB0 ABREV; AAB1 MOT
Fields:
  ABREV A*15 Abbreviation
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AAB]CREUSR (AUTILIS) !Other
  MOT A*30 Word
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AAB]UPDUSR (AUTILIS) !Other

## ABANK (ABN) - Bank sort codes
Keys (first = PK; D = duplicates allowed): ABN0 CRY+BAN
Fields:
  AUUID AUUID Single identifier
  BAN A*20 Bank
  BIC A*11 BIC code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABN]CREUSR (AUTILIS) !Other
  CRY CRY Cnty -> [TCY]TCY0 =[ABN]CRY (TABCOUNTRY) !Block
  PAB PAB Paying bank
  PORBANCOD A*4 Bank code act:PBDPO
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABN]UPDUSR (AUTILIS) !Other
  VLYEND D Validity end date
  VLYSTR D Validity start date

## ABATABT (ABA) - Batch server (recurring tasks)
Notes: differs in V9.0 P12 (diff: AT3_ABATABT.htm)
Keys (first = PK; D = duplicates allowed): CODABT CODABT
Fields:
  AUUID AUUID Single identifier
  CAL ABC Calendar -> [ABC]ABC0 =[ABA]CAL (ABATCAL) !Block
  CNTERR M*4 Proceed if error [menu 1: 1=No,2=Yes]
  CODABT ABA Recurring task code -> [ABA]CODABT =[ABA]CODABT (ABATABT) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABA]CREUSR (AUTILIS) !Other
  DATDEP M*15(10) Base date [menu 910: 1=Current date,2=Start of month,3=End of month,4=Start of year,5=End of year,6=Start of quarter,7=End of quarter,8=Start of week,9=End of week,10=Start of fortnight,11=End of fortnight,12=Start of 10-day period,13=End of 10-day period,14=Formula,15=Absolute date]
  DATFRM AFR*250(10) Formula
  DATJRS M*15(10) Time unit [menu 913: 1=Days,2=Weeks,3=Months,4=Years]
  DATNBR C*3(10) Increment
  DATZON A*20(10) Date field
  DJOUR D Last date
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ABA]DOSSIER (ADOSSIER) !Delete
  DREL M*4 Reminder [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EPUR M*4 Purge [menu 1: 1=No,2=Yes]
  FDM M*4 Month end [menu 1: 1=No,2=Yes]
  FORCE M*4 Forced execution [menu 1: 1=No,2=Yes]
  FRQ L*8 Frequency (min)
  GRP ABG Group -> [ABG]ABG0 =[ABA]GRP (ABATGRP) !Block
  HDEB HM Start time
  HEURE HM(3) Time
  HFIN HM End time
  JOUR M*4(7) Current date [menu 1: 1=No,2=Yes]
  LAN LAN Language -> [TLA]TLA0 =[ABA]LAN (TABLAN) !Other
  NBDAT C*3 No. of lines
  NOMABT DES Description
  ONE M*4 One single query [menu 1: 1=No,2=Yes]
  PERIO M*15 Periodicity [menu 911: 1=Weekly,2=Monthly]
  QUANT C*2(5) Days of the month
  TACHE ABT Task code -> [ABT]CODTAC =[ABA]TACHE (ABATTAC) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABA]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[ABA]USER (AUTILIS) !Other

## ABATABTD (ABD) - Batch server (recurring tasks)
Keys (first = PK; D = duplicates allowed): ABD0 CODABT+CODTAC+LIG+NUM+PARAM
Fields:
  AUUID AUUID Single identifier
  CODABT ABA Recurring task code -> [ABA]CODABT =[ABD]CODABT (ABATABT) !Delete
  CODTAC ABT Task code -> [ABT]CODTAC =[ABD]CODTAC (ABATTAC) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABD]CREUSR (AUTILIS) !Other
  LIG C*3 Line number
  NUM C*4 Number
  PARAM A*15 Parameter
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABD]UPDUSR (AUTILIS) !Other
  VALEUR A*30 Value

## ABATCAL (ABC) - Batch server calendar
Keys (first = PK; D = duplicates allowed): ABC0 COD
Fields:
  AUUID AUUID Single identifier
  COD ABC Calendar -> [ABC]ABC0 =[ABC]COD (ABATCAL) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABC]CREUSR (AUTILIS) !Other
  DES DES Description
  ENDDAT D(25) End date
  NBRDAT C*4 Number of lines
  STRDAT D(25) Start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABC]UPDUSR (AUTILIS) !Other

## ABATGRP (ABG) - Batch server (groups)
Keys (first = PK; D = duplicates allowed): ABG0 CODGRP
Fields:
  AUUID AUUID Single identifier
  CNTERR M*4 Proceed if error [menu 1: 1=No,2=Yes]
  CODGRP ABG Group -> [ABG]ABG0 =[ABG]CODGRP (ABATGRP) !Delete
  CODTAC ABT(30) Task code -> [ABT]CODTAC =[ABG]CODTAC (ABATTAC) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABG]CREUSR (AUTILIS) !Other
  DES ATX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  HOR ABH Hourly constraints -> [ABH]ABH0 =[ABG]HOR (ABATHOR) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBTAC C*4 Number
  NIVEAU C*2 Authorization level
  SEQ L*8(30) Sequence
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABG]UPDUSR (AUTILIS) !Other

## ABATHOR (ABH) - Hourly constraints
Keys (first = PK; D = duplicates allowed): ABH0 COD
Fields:
  AUUID AUUID Single identifier
  CAL ABC Calendar -> [ABC]ABC0 =[ABH]CAL (ABATCAL) !Block
  COD ABH Constraint -> [ABH]ABH0 =[ABH]COD (ABATHOR) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABH]CREUSR (AUTILIS) !Other
  DAYOPE M*4(7) Working day [menu 1: 1=No,2=Yes]
  DES DES Description
  ENDCLO HM(5) End time
  ENDOPE HM(5) End time
  NBRCLO C*4 Lines
  NBROPE C*4 Lines
  STRCLO HM(5) Start time
  STROPE HM(5) Start time
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABH]UPDUSR (AUTILIS) !Other

## ABATPAR (ABP) - Batch server (parameters)
Keys (first = PK; D = duplicates allowed): SPOOL SPOOL
Fields:
  APPLI A*10 Server name
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABP]CREUSR (AUTILIS) !Other
  FLGPATCH M*4 Patch [menu 1: 1=No,2=Yes]
  JOB M*4 Batch [menu 1: 1=No,2=Yes]
  LECPID C*2 Waiting read PID
  NBTACHE C*2 No. active requests
  NUMREQ L*8 Query no.
  PROCESS A*10 Process no.
  REPJOB FIC*80(7) Batch files
  RETARD L*8 Late
  RQTLOG M*4 Log [menu 1: 1=No,2=Yes]
  SPOOL A*1 Search key
  STOP C*1 Stop flag
  TEMPS L*8 Search
  TIMIMP L*8 Time-out
  TIMOUT L*8 Time-out
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABP]UPDUSR (AUTILIS) !Other

## ABATRQT (ABR) - Batch server (queries)
Notes: differs in V9.0 P12 (diff: AT3_ABATRQT.htm)
Keys (first = PK; D = duplicates allowed): NUMREQ NUMREQ; PRIO DAT+HEURE+NUMREQ; FLAG FLAG+NUMREQ; FLAG2 FLAG+DAT+HEURE+NUMREQ
Fields:
  AUUID AUUID Single identifier
  CNTERR M*4 Proceed if error [menu 1: 1=No,2=Yes]
  CODABT ABA Recurring task code -> [ABA]CODABT =[ABR]CODABT (ABATABT) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABR]CREUSR (AUTILIS) !Other
  DAT D Date
  DFIN D End date
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ABR]DOSSIER (ADOSSIER) !Delete
  EPUR M*4 Purge [menu 1: 1=No,2=Yes]
  ETAT ADC Processing
  FLAG M*15 Status [menu 21: 1=Standby,2=In progress,3=Finished,4=Held,5=Kill,6=Canceled,7=Error,8=Overdue,9=Warning]
  FLGV3 C*4 V3 flag
  FRQ L*8 Frequency (min)
  FRQFIN HM End time
  GRP ABG Group -> [ABG]ABG0 =[ABR]GRP (ABATGRP) !Block
  HDEB HS Start time
  HEURE HM Time
  HFIN HS Time
  IMPETX C*2 Printer
  JOB FIC*50 Batch file
  LAN LAN Language -> [TLA]TLA0 =[ABR]LAN (TABLAN) !Other
  MESSAGE M*4 Message - user [menu 1: 1=No,2=Yes]
  MONO M*4 Single-user [menu 1: 1=No,2=Yes]
  MOTINT DES Reason for interruption
  NUMGRP L*8 Order no.
  NUMREQ L*8 Query no.
  ONE M*4 One single query [menu 1: 1=No,2=Yes]
  PORT L*8 Port
  PRIO C*2 Priority
  PROCESS A*10 Process no.
  SEQGRP L*8 Sequence
  SERVER AMC Server
  TACHE ABT Task code -> [ABT]CODTAC =[ABR]TACHE (ABATTAC) !Block
  TIMOUT L*8 Time-out
  TYPTAC M*15 Task type [menu 20: 1=Processing,2=Script]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABR]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[ABR]USER (AUTILIS) !Other
  USRINT AUS User -> [AUS]CODUSR =[ABR]USRINT (AUTILIS) !Other

## ABATRQTL (ABL) - Batch server (queries)
Keys (first = PK; D = duplicates allowed): NUMREQ NUMREQ+NUM+PARAM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABL]CREUSR (AUTILIS) !Other
  NUM C*3 Number
  NUMREQ L*8 Query no.
  PARAM A*15 Parameter
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABL]UPDUSR (AUTILIS) !Other
  VALEUR A*30 Value

## ABATTAC (ABT) - Batch server (tasks)
Notes: differs in V9.0 P12 (diff: AT3_ABATTAC.htm)
Keys (first = PK; D = duplicates allowed): CODTAC CODTAC
Fields:
  AUUID AUUID Single identifier
  CODTAC ABT Task code -> [ABT]CODTAC =[ABT]CODTAC (ABATTAC) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABT]CREUSR (AUTILIS) !Other
  DES ATX Description
  DOSPAR ADS Parameter folder -> [ADS]DOSSIER =[ABT]DOSPAR (ADOSSIER) !Delete
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FONCTION AFC Function -> [AFC]CODINT =[ABT]FONCTION (AFONCTION) !Other
  HOR ABH Hourly constraints -> [ABH]ABH0 =[ABT]HOR (ABATHOR) !Block
  MESSAGE M*4 User message [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MONO M*4 Single-user [menu 1: 1=No,2=Yes]
  MULTIDOS M*4 Multi-folder [menu 1: 1=No,2=Yes]
  NIVEAU C*2 Authorization level
  PARAM A*15 Parameter
  PRIO C*2 Priority
  PROGPAR ADC Parameter program
  RETARD L*8 Late
  TIMOUT A*10 Time-out
  TRAIT ADC Object
  TYPTAC M*15 Task type [menu 20: 1=Processing,2=Script]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABT]UPDUSR (AUTILIS) !Other

## ABICOND (AII) - Predefined conditions
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): AII0 COD; AII1 ORD+COD; AII2 ABM+CODABF+COD
Fields:
  ABM ABM Datamart -> [ABM]ABM0 =[AII]ABM (ABIDATMRT) !Block
  ACV ACV Activity code -> [ACV]CODACT =[AII]ACV (ACTIV) !Block
  AUUID AUUID Single identifier
  CNDDEF AFR*250 Condition
  CNDORA AFR*250 Oracle condition
  CNDSQL AFR*250 Sql-server condition
  COD AII Code -> [AII]AII0 =[AII]COD (ABICOND) !Delete
  CODABF ABF Fact table -> [ABF]ABF0 =[AII]CODABF (ABITABDAT) !Block
  CODABF1 ABF(2) Fact table -> [ABF]ABF0 =[AII]CODABF1 (ABITABDAT) !Block
  CODDIM1 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM1 (ABIDIM) !Block
  CODDIM2 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM2 (ABIDIM) !Block
  CODDIM3 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM3 (ABIDIM) !Block
  CODDIM4 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM4 (ABIDIM) !Block
  CODDIM5 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM5 (ABIDIM) !Block
  CODDIM6 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM6 (ABIDIM) !Block
  CODDIM7 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM7 (ABIDIM) !Block
  CODDIM8 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM8 (ABIDIM) !Block
  CODDIM9 ABI(2) Dimension -> [ABI]ABI0 =[AII]CODDIM9 (ABIDIM) !Block
  CODFLD1 AVA(2) Field code
  CODLNK ABI Dimension -> [ABI]ABI0 =[AII]CODLNK (ABIDIM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AII]CREUSR (AUTILIS) !Other
  DES ATX Description
  EXPLNK A*80 Link expression
  FLDDIM1 AVA(2) Field code
  FLDDIM2 AVA(2) Field code
  FLDDIM3 AVA(2) Field code
  FLDDIM4 AVA(2) Field code
  FLDDIM5 AVA(2) Field code
  FLDDIM6 AVA(2) Field code
  FLDDIM7 AVA(2) Field code
  FLDDIM8 AVA(2) Field code
  FLDDIM9 AVA(2) Field code
  INTEVAL A*60 Evaluated title
  INTVALTEX A*60 Evaluated title
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  ORD C*3 Order
  TEX ATX Prompt text
  TYPOPT A*15(2) Option
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AII]UPDUSR (AUTILIS) !Other

## ABIDATMRT (ABM) - Datamart
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABM0 COD; ABM1 ABR (D)
Fields:
  ABR ABR Abbreviation
  ACTABF ACV(50) Activity code -> [ACV]CODACT =[ABM]ACTABF (ACTIV) !Block
  ANSI M*4 ANSI standard [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  AUZFCY M*4 Authorization site [menu 1: 1=No,2=Yes]
  COD ABM Code -> [ABM]ABM0 =[ABM]COD (ABIDATMRT) !Delete
  CODABF ABF(50) Fact tables -> [ABF]ABF0 =[ABM]CODABF (ABITABDAT) !Block
  CODACT ACV Activity code -> [ACV]CODACT =[ABM]CODACT (ACTIV) !Block
  COMPL M*4 Additional info [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABM]CREUSR (AUTILIS) !Other
  DATNUL M*4 Null date management [menu 1: 1=No,2=Yes]
  DUREE L*8 Duration
  FNC AFC Function -> [AFC]CODINT =[ABM]FNC (AFONCTION) !Block
  INTIT ATX Description
  MESURE M*4 Flag class [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRABF C*4 No. of tables
  PREFIX M*4 Prefix [menu 1: 1=No,2=Yes]
  RESULT L*8 Result
  SCLASS M*4 Sub-class [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABM]UPDUSR (AUTILIS) !Other

## ABIDATWRH (ABW) - Data warehouse
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABW0 COD
Fields:
  ADXDOS ADD(20) Folder
  AUUID AUUID Single identifier
  COD ABW Code -> [ABW]ABW0 =[ABW]COD (ABIDATWRH) !Delete
  CODABM ABM(50) Datamart -> [ABM]ABM0 =[ABW]CODABM (ABIDATMRT) !Block
  CODDBA M*10 Format [menu 930: 1=ASCII,2=Unicode]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABW]CREUSR (AUTILIS) !Other
  GRPFIL M*4 Use file groups [menu 1: 1=No,2=Yes]
  INTIT DES Description
  LAN LAN Language -> [TLA]TLA0 =[ABW]LAN (TABLAN) !Block
  NBRABM C*4 Number of lines
  NBRDOS ABS No. folders
  SIZDAT L*8 Data size
  SIZIDX L*8 Index size
  SOLBI ASO BI solution
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABW]UPDUSR (AUTILIS) !Other

## ABIDIM (ABI) - Dimensions
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABI0 CODDIM
Fields:
  ABRDIM ABR Abbreviation
  ABRLNK ABR(11) Abbreviation
  ADXDOS ADD(20) Folder
  AUUID AUUID Single identifier
  CLE A*80 Key
  CLELNK ANX(11) Link key
  CODACT ACV Activity code -> [ACV]CODACT =[ABI]CODACT (ACTIV) !Block
  CODDIM ABI Dimension -> [ABI]ABI0 =[ABI]CODDIM (ABIDIM) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABI]CREUSR (AUTILIS) !Other
  DATMAJ D Update date
  EXPLNK A*80(11) Link expression
  FILTRE AFR*250 Filter
  FLDDAT M*4(11) Date field [menu 1: 1=No,2=Yes]
  INDLEC ANX Key
  INTEVAL A*60 Evaluated title
  INTIT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MULDOS M*4 Multi-folder [menu 1: 1=No,2=Yes]
  NBRDOS ABS No. folders
  NBRLNK ABS No. of tables
  NOMBRE M*4 Number [menu 1: 1=No,2=Yes]
  SUPVID M*4 Deletion empty [menu 1: 1=No,2=Yes]
  TABLNK A*12(11) Linked tables
  TABORG ATB Origin table -> [ATB]CODFIC =[ABI]TABORG (ATABLE) !Block
  TRTSPE ADC Specific
  TRTSPV ADC Vertical processing
  TRTSTD ADC Standard processing
  TYPLNK M*5(11) Link type [menu 2916: 1=0,1,2=0,n,3=1,1,4=1,n]
  TYPMAJ M*4 Update type [menu 7820: 1=Incremental,2=Cancels and replaces,3=Incremental Audit]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABI]UPDUSR (AUTILIS) !Other

## ABIDIMFLD (ABJ) - Dimensions (fields)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABJ0 CODDIM+NUMDIM+FLDDIM; ABJ1 CODDIM+FLDDIM; DICO FLDDIM (D)
Fields:
  ACTDIM ACV Activity code -> [ACV]CODACT =[ABJ]ACTDIM (ACTIV) !Block
  AUTO ATX Self-join
  AUTOEVAL A*60 Self-join
  AUUID AUUID Single identifier
  CODDIM ABI Dimension -> [ABI]ABI0 =[ABJ]CODDIM (ABIDIM) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[ABJ]CODTYP (ATYPE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABJ]CREUSR (AUTILIS) !Other
  DIMFAT ABI Parent dimension -> [ABI]ABI0 =[ABJ]DIMFAT (ABIDIM) !Block
  DIMFLD AVA Name of field
  DIMINT ATX Dimension
  DIMVALINT A*60 Evaluated title
  FLDDIM AVA Field code
  FLDLIE AVA Linked object
  FLDORG AFR*250 Formula
  INTDIM ATX Description
  INTVALDIM A*60 Evaluated title
  LNG DCB*4 Length
  MENLOC MNL Local menu number
  NUMDIM C*4 Line number
  OPTJNT M*15 Join option [menu 7823: 1=Inner,2=Left outer,3=Right outer]
  TABDIV ADV Miscellaneous table -> [ADV]CODE =[ABJ]TABDIV (ATABTAB) !Block
  TUNNEL M*4 Tunnel toward object [menu 1: 1=No,2=Yes]
  TYPDAT A*10 Date type
  TYPFLD M*15 Field type [menu 7826: 1=Dimension,2=Information,3=Parent dimension,4=Technical]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABJ]UPDUSR (AUTILIS) !Other

## ABIHIERA (AHH) - Hierarchies
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): AHH0 COD; AHH1 ABM+COD
Fields:
  ABM ABM Datamart -> [ABM]ABM0 =[AHH]ABM (ABIDATMRT) !Block
  ACV ACV Activity code -> [ACV]CODACT =[AHH]ACV (ACTIV) !Block
  AUUID AUUID Single identifier
  COD AHH Code -> [AHH]AHH0 =[AHH]COD (ABIHIERA) !Delete
  CODABF ABF(15) Fact table -> [ABF]ABF0 =[AHH]CODABF (ABITABDAT) !Block
  CODDIM1 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM1 (ABIDIM) !Block
  CODDIM2 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM2 (ABIDIM) !Block
  CODDIM3 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM3 (ABIDIM) !Block
  CODDIM4 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM4 (ABIDIM) !Block
  CODDIM5 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM5 (ABIDIM) !Block
  CODDIM6 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM6 (ABIDIM) !Block
  CODDIM7 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM7 (ABIDIM) !Block
  CODDIM8 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM8 (ABIDIM) !Block
  CODDIM9 ABI(15) Dimension -> [ABI]ABI0 =[AHH]CODDIM9 (ABIDIM) !Block
  CODFLD AVA(15) Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AHH]CREUSR (AUTILIS) !Other
  DES ATX Description
  FLDDIM1 AVA(15) Field code
  FLDDIM2 AVA(15) Field code
  FLDDIM3 AVA(15) Field code
  FLDDIM4 AVA(15) Field code
  FLDDIM5 AVA(15) Field code
  FLDDIM6 AVA(15) Field code
  FLDDIM7 AVA(15) Field code
  FLDDIM8 AVA(15) Field code
  FLDDIM9 AVA(15) Field code
  INTEVAL A*60 Evaluated title
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBAHH C*4 Number
  NIVEAU C*4 Level
  TYPOPT A*15(15) Option
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AHH]UPDUSR (AUTILIS) !Other

## ABIPRFUSR (AIU) - BI user profile
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): AIU0 PRF
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AIU]CREUSR (AUTILIS) !Other
  INTUSR AX3 Description
  MODE M*15 Method [menu 7835: 1=Enterprise,2=LDAP,3=Windows AD,4=Windows NT]
  PRF AIU Profile code -> [AIU]AIU0 =[AIU]PRF (ABIPRFUSR) !Delete
  PWD A*24 BI password
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AIU]UPDUSR (AUTILIS) !Other
  USR A*30 BI user

## ABIREGDES (ABY) - Synchronization rules (dest)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABY0 CODREG+NUMDES; ABY1 CODREG+FLDDES; ABY2 CODREG+TABDES+NUMDES
Fields:
  AUUID AUUID Single identifier
  CODREG ABV Rule -> [ABV]ABV0 =[ABY]CODREG (ABIREGORG) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABY]CREUSR (AUTILIS) !Other
  FLDDES AVA Field
  FORDES AFR*250 Formula
  NUMDES C*4 Line number
  TABDES ABF Destination table -> [ABF]ABF0 =[ABY]TABDES (ABITABDAT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABY]UPDUSR (AUTILIS) !Other

## ABIREGORG (ABV) - Synchronisation rules
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABV0 CODREG; ABV1 TABORG+CODREG
Fields:
  ABRLNK ABR(11) Abbreviation
  ADXDOS ADD(20) Folder
  AJOUT M*4 Addition [menu 1: 1=No,2=Yes]
  ANNUL M*4 Cancellation [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CLELNK ANX(11) Link key
  CNDLIG AFR*250 Line condition
  CODACT ACV Activity code -> [ACV]CODACT =[ABV]CODACT (ACTIV) !Block
  CODREG ABV Rule -> [ABV]ABV0 =[ABV]CODREG (ABIREGORG) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABV]CREUSR (AUTILIS) !Other
  DESFLG M*4 Deactivation [menu 1: 1=No,2=Yes]
  EXPLNK A*80(11) Link expression
  FILTRE AFR*250 Filter
  FLDDEC AVA Triggering field
  INDLEC ANX Key
  INTIT ATX Description
  MODIF M*4 Modification [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRDOS ABS No. folders
  NBRLNK ABS No. of tables
  TABLNK A*12(11) Linked tables
  TABORG ATB Origin table -> [ATB]CODFIC =[ABV]TABORG (ATABLE) !Block
  TRTSPE ADC Specific
  TRTSPV ADC Vertical processing
  TRTSTD ADC Standard processing
  TYPLNK M*5 Creation rule [menu 2916: 1=0,1,2=0,n,3=1,1,4=1,n]
  TYPLNKTAB M*8(11) Link type [menu 2916: 1=0,1,2=0,n,3=1,1,4=1,n]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABV]UPDUSR (AUTILIS) !Other

## ABIREPORT (ABO) - Business objects reports
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABO0 COD; ABO1 REPCOD+COD; ABO2 DATAM+COD (D)
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ABO]ACS (ACCCOD) !Block
  ACV ACV Activity code -> [ACV]CODACT =[ABO]ACV (ACTIV) !Block
  AUUID AUUID Single identifier
  COD ABO Code -> [ABO]ABO0 =[ABO]COD (ABIREPORT) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABO]CREUSR (AUTILIS) !Other
  DATAM ABM Datamart -> [ABM]ABM0 =[ABO]DATAM (ABIDATMRT) !Block
  DES ATX Description
  DES1 ATX Description
  DES2 ATX Description
  DES3 ATX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ETAREF M*4 Reference [menu 1: 1=No,2=Yes]
  LANREF LAN Reference language -> [TLA]TLA0 =[ABO]LANREF (TABLAN) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  REPCOD A*50 BO report
  SHO ATX Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABO]UPDUSR (AUTILIS) !Other

## ABIREPORTD (ABQ) - Business objects reports
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABQ0 COD+LIG
Fields:
  AUUID AUUID Single identifier
  COD ABO Code -> [ABO]ABO0 =[ABQ]COD (ABIREPORT) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABQ]CREUSR (AUTILIS) !Other
  CTL AFR*80 Control
  DAC M*15 Input [menu 1: 1=No,2=Yes]
  INTEVAL A*60 Evaluated title
  LIG C*4 Line
  LNG DCB*4 Length
  MENLOC MNL Local menu number
  OPT A*20 Options
  PAR AFR*80 Parameter
  PARACS ACS Access code -> [ACS]ACS0 =[ABQ]PARACS (ACCCOD) !Block
  PARCTL ACL Control table -> [ACL]ACL0 =[ABQ]PARCTL (ACTL) !Block
  STREND M*10 Range [menu 7854: 1=No,2=Start range,3=End range]
  TABDIV ADV Miscellaneous table -> [ADV]CODE =[ABQ]TABDIV (ATABTAB) !Block
  TEX ATX Prompt text
  TYP ATY Data type -> [ATY]CODTYP =[ABQ]TYP (ATYPE) !Block
  TYPBO M*15 Type [menu 7833: 1=Simple,2=Multiple]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABQ]UPDUSR (AUTILIS) !Other
  VALDEF AFR*80 Default value

## ABIREPORTID (ABOID) - Business objects reports
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABOID0 COD+DATAW+LAN
Fields:
  AUUID AUUID Single identifier
  COD ABO Code -> [ABO]ABO0 =[ABOID]COD (ABIREPORT) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABOID]CREUSR (AUTILIS) !Other
  DATAW ABW Data warehouse -> [ABW]ABW0 =[ABOID]DATAW (ABIDATWRH) !Block
  DOCID A*80 Identifier
  LAN LAN Languages -> [TLA]TLA0 =[ABOID]LAN (TABLAN) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABOID]UPDUSR (AUTILIS) !Other

## ABITABAGG (ABE) - Fact table (aggregates)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABE0 CODABF+NUMAGG+CODAGG; ABE1 CODABF+CODAGG
Fields:
  ACTAGG ACV Activity code -> [ACV]CODACT =[ABE]ACTAGG (ACTIV) !Block
  AUUID AUUID Single identifier
  CODABF ABF Fact tables -> [ABF]ABF0 =[ABE]CODABF (ABITABDAT) !Delete
  CODAGG A*7 Name
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABE]CREUSR (AUTILIS) !Other
  DIMAGG ABI(16) Dimension -> [ABI]ABI0 =[ABE]DIMAGG (ABIDIM) !Block
  FLDAGG AVA(16) Name of field
  INDAGG A*80(8) Index
  LNKAGG A*80(16) Fields
  NBRAGD C*2 No. dimensions
  NBRAGI C*2 Index number
  NIVAGG M*15(16) Aggregation level [menu 7825: 1=Day,2=Week,3=10-day period,4=Half-month,5=Month,6=Quarter,7=Half-year,8=Year]
  NUMAGG C*4 Aggregate
  TYPAGG M*15(16) Dim view type [menu 7826: 1=Dimension,2=Information,3=Parent dimension,4=Technical]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABE]UPDUSR (AUTILIS) !Other

## ABITABDAT (ABF) - Fact tables
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABF0 CODABF
Fields:
  ABRABF ABR Abbreviation
  AUUID AUUID Single identifier
  AUZFCY M*4 Authorization site [menu 1: 1=No,2=Yes]
  CODABF ABF Code -> [ABF]ABF0 =[ABF]CODABF (ABITABDAT) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[ABF]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABF]CREUSR (AUTILIS) !Other
  FLDDAT AVA Date field
  FLDFCY AVA Site field
  FNC AFC Function -> [AFC]CODINT =[ABF]FNC (AFONCTION) !Delete
  INTEVAL A*60 Evaluated title
  INTIT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBEPU C*4 Days
  NBRABF M*4 Number [menu 1: 1=No,2=Yes]
  STK AC0*2 Storage
  TYPMAJ M*4 Update type [menu 7820: 1=Incremental,2=Cancels and replaces,3=Incremental Audit]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ABF]UPDUSR (AUTILIS) !Other

## ABITABFLD (ABZ) - Fact table (fields)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABZ0 CODABF+NUMFLD+CODFLD; ABZ1 CODABF+CODFLD; DICO CODFLD (D)
Fields:
  ACTFLD ACV Activity code -> [ACV]CODACT =[ABZ]ACTFLD (ACTIV) !Block
  AUUID AUUID Single identifier
  CODABF ABF Fact tables -> [ABF]ABF0 =[ABZ]CODABF (ABITABDAT) !Delete
  CODFLD AVA Field code
  CODTYP ATY Data type -> [ATY]CODTYP =[ABZ]CODTYP (ATYPE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABZ]CREUSR (AUTILIS) !Other
  INTFLD ATX Description
  INTSSC ATX Sub-class
  INTVALFLD A*60 Evaluated title
  INTVALSSC A*60 Sub-class
  LNGFLD DCB*4 Length
  MENLOC MNL Local menu number
  NUMFLD C*3 Line no.
  TABDIV ADV Miscellaneous table -> [ADV]CODE =[ABZ]TABDIV (ATABTAB) !Block
  TUNNEL M*4 Tunnel toward object [menu 1: 1=No,2=Yes]
  TYPDAT A*10 Date type
  TYPFLD M*15 Field type [menu 7821: 1=Measurement,2=Information,3=Dimension,4=Technical]
  TYPOPE M*4 Distinct account [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABZ]UPDUSR (AUTILIS) !Other

## ABITABIND (ABX) - Fact table (index)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABX0 CODABF+NUMIND
Fields:
  ACTIND ACV Activity code -> [ACV]CODACT =[ABX]ACTIND (ACTIV) !Block
  AUUID AUUID Single identifier
  CODABF ABF Fact tables -> [ABF]ABF0 =[ABX]CODABF (ABITABDAT) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABX]CREUSR (AUTILIS) !Other
  EXPIND A*80 Description
  NUMIND C*4 Line number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABX]UPDUSR (AUTILIS) !Other

## ABITABLNK (ABK) - Fact table (links)
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ABK0 CODABF+NUMLNK
Fields:
  AUUID AUUID Single identifier
  CODABF ABF Fact tables -> [ABF]ABF0 =[ABK]CODABF (ABITABDAT) !Delete
  CODLNK ABI Dimension -> [ABI]ABI0 =[ABK]CODLNK (ABIDIM) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ABK]CREUSR (AUTILIS) !Other
  EXPLNK A*80 Link expression
  INTCOMP ATX Additional info
  INTLNK ATX Description
  INTVALCOMP A*60 Additional info
  INTVALLNK A*60 Description
  NUMLNK C*4 Line number
  OPTJNT M*15 Join option [menu 7823: 1=Inner,2=Left outer,3=Right outer]
  TYPJNT M*15 Join type [menu 7824: 1=Mandatory,2=Shortcut]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABK]UPDUSR (AUTILIS) !Other

## ABITRAUNV (ATV) - Report translation
Notes: activity code ABI
Keys (first = PK; D = duplicates allowed): ATV0 ABM+RAPORT+LANTRA+TEXTE; ATV1 ABM+RAPORT+LANTRA+TYPERR+TEXTE
Fields:
  ABM ABM Datamart -> [ABM]ABM0 =[ATV]ABM (ABIDATMRT) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATV]CREUSR (AUTILIS) !Other
  LANREF LAN Reference language -> [TLA]TLA0 =[ATV]LANREF (TABLAN) !Block
  LANTRA LAN Translation language -> [TLA]TLA0 =[ATV]LANTRA (TABLAN) !Block
  RAPORT A*80 Report
  STA M*4 Status [menu 1: 1=No,2=Yes]
  TEXTE A*80 Text
  TXTREF ATX No. text reference
  TXTTRA A*80 Text to translate
  TYPERR M*15 Error [menu 7832: 1=Text does not exist,2=Text without its translation,3=Duplicates,4=Translated text]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATV]UPDUSR (AUTILIS) !Other

## ABLBSYS (ASB) - Graphic components
Keys (first = PK; D = duplicates allowed): ASB0 CAT+CODFIC
Fields:
  AUUID AUUID Single identifier
  BLOB AB0*9 Image file
  CAT ADI Category -> [ADI]CODE =914;CAT (ATABDIV) !Block
  CODFIC ASB Code -> [ASB]ASB0 =[ASB]CODFIC (ABLBSYS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ASB]CREUSR (AUTILIS) !Other
  INTIT DES Description
  INTIT1 ATX Description
  NAMFIC FIC*250 File name
  TYPFIC AT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASB]UPDUSR (AUTILIS) !Other

## ABLOB (ABB) - Special folders
Notes: differs in V10 P1 (diff: ATD_ABLOB.htm)
Keys (first = PK; D = duplicates allowed): ABB0 CODBLB+IDENT1+IDENT2+IDENT3
Fields:
  AUUID AUUID Single identifier
  BLOB ABB Image file
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CODBLB A*12 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ABB]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  NAMBLB DES File name
  TYPBLB AT Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ABB]UPDUSR (AUTILIS) !Other

## ACALCUL (AKL) - Calculator history
Keys (first = PK; D = duplicates allowed): AKL0 USR+NUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AKL]CREUSR (AUTILIS) !Other
  FORMUL AFR*250 Formula
  NUM L*8 Sequence no.
  RES A*250 Result
  TRC C*1 Truncation
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AKL]UPDUSR (AUTILIS) !Other
  USR AUS Code -> [AUS]CODUSR =[AKL]USR (AUTILIS) !Delete

## ACCCOD (ACS) - Access codes
Keys (first = PK; D = duplicates allowed): ACS0 CODACC
Fields:
  AUUID AUUID Single identifier
  CODACC ACS Access code -> [ACS]ACS0 =[ACS]CODACC (ACCCOD) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACS]CREUSR (AUTILIS) !Other
  DESACC AX3 Description
  INTACC A*30 Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACS]UPDUSR (AUTILIS) !Other

## ACCES (ACC) - Access by user
Keys (first = PK; D = duplicates allowed): CODACC USR+CODACC (D); PRFCOD PRFCOD+CODACC+USR
Fields:
  AUUID AUUID Single identifier
  CODACC ACS Access code -> [ACS]ACS0 =[ACC]CODACC (ACCCOD) !Delete
  CONSUL M*4 Inquiry [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACC]CREUSR (AUTILIS) !Other
  EXEC M*4 Execution [menu 1: 1=No,2=Yes]
  MODIF M*4 Modification [menu 1: 1=No,2=Yes]
  PRFCOD AFT Profile code -> [AFT]AFT0 =[ACC]PRFCOD (AFCTFCT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACC]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[ACC]USR (AUTILIS) !Delete

## ACHANGE (ACG) - Key change set up
Keys (first = PK; D = duplicates allowed): ACG0 COD+LIG
Fields:
  AUUID AUUID Single identifier
  CLE1 ID1 Identifier
  CLE2 ID2 Identifier
  COD ACG Code -> [ACG]ACG0 =COD;[V]GSUPCLE (ACHANGE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACG]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  INTIT AX3 Description
  LIG C*3 Line no.
  NEWCOD ID1 New code
  OBJ AOB Object -> [AOB]ABREV =[ACG]OBJ (AOBJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACG]UPDUSR (AUTILIS) !Other

## ACLACOL (ACLAC) - Classes (Collections)
Keys (first = PK; D = duplicates allowed): ACLAC0 CODCLA+CODCOL
Fields:
  ACTCOL ACV Activity code -> [ACV]CODACT =[ACLAC]ACTCOL (ACTIV) !Block
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAC]CODCLA (ACLASSE) !Delete
  CODCOL AVA Collection
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACLAC]CREUSR (AUTILIS) !RTZ
  FLGAPDCOL M*4 Addition [menu 1: 1=No,2=Yes]
  FLGINSCOL M*4 Insertion [menu 1: 1=No,2=Yes]
  FLGSUPCOL M*4 Deletion [menu 1: 1=No,2=Yes]
  FLGTRICOL M*4 Sort [menu 1: 1=No,2=Yes]
  INTCOL ATX Collection description
  MAXCOL C*4 Maxi
  MINCOL M*15 Mini [menu 7966: 1=0,2=1,3=Maximum]
  PROCOL AVA Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACLAC]UPDUSR (AUTILIS) !RTZ

## ACLAFLD (ACLAF) - Classes (lines)
Keys (first = PK; D = duplicates allowed): ACLAF0 CODCLA+FLDCLA; ACLAF1 CODCLA+NUMLIG+FLDCLA; ACLAF2 CODCLA+NUMFLD+NUMLIG+FLDCLA
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ACLAF]ACS (ACCCOD) !Block
  ACTFLD ACV Activity code -> [ACV]CODACT =[ACLAF]ACTFLD (ACTIV) !Block
  AUUID AUUID Single identifier
  CATSEARCH ADI Category -> [ADI]CODE =16;CATSEARCH (ATABDIV) !Block
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAF]CODCLA (ACLASSE) !Other
  CODCTL ACL Control table -> [ACL]ACL0 =[ACLAF]CODCTL (ACTL) !Block
  CODTYP ATY Data type -> [ATY]CODTYP =[ACLAF]CODTYP (ATYPE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACLAF]CREUSR (AUTILIS) !Other
  FLDCLA AVA Field code
  FLDGRP AVA Group
  FLDSEARCH M*4 Searchable [menu 1: 1=No,2=Yes]
  FLGACCGET M*4 GET accessor [menu 1: 1=No,2=Yes]
  INTEVAL A*60 Evaluated title
  INTFLD ATX Description
  INTSHTFLD ATX Short description
  LNKCLA ACLA Linked class -> [ACLA]ACLA0 =[ACLAF]LNKCLA (ACLASSE) !Block
  LOBCNT AVA Content type
  LOBFLD AVA Lob field
  LOBTAB ATB Lob table -> [ATB]CODFIC =[ACLAF]LOBTAB (ATABLE) !Block
  LONG DCB*4 Length
  NOLIB MNL Local menu no.
  NUMFLD DCB*3.2 Order
  NUMLIG C*3 Line no.
  OBLIG M*4 Mandatory field [menu 1: 1=No,2=Yes]
  TABCONT A*250 Dependency
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACLAF]UPDUSR (AUTILIS) !Other

## ACLALNK (ACLAK) - Classes (tables)
Keys (first = PK; D = duplicates allowed): ACLAK0 CODCLA+REFLNK; ACLAK1 CODCLA+NUMLIG+REFLNK
Fields:
  ABRLNK ABR Linked abbreviation
  ABRORI ABR Abbreviation origin
  ACVLNK ACV Activity code -> [ACV]CODACT =[ACLAK]ACVLNK (ACTIV) !Block
  AUUID AUUID Single identifier
  CLALNK ACLA Class code -> [ACLA]ACLA0 =[ACLAK]CLALNK (ACLASSE) !Block
  CLELNK ANX Link key
  CLESORT ANX Sort index
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAK]CODCLA (ACLASSE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACLAK]CREUSR (AUTILIS) !BSRA
  EXPLNK A*250 Link expression
  EXPSEL AFR*250 Selection
  FLGA M*4 Management [menu 1: 1=No,2=Yes]
  FLGC M*4 Creation [menu 1: 1=No,2=Yes]
  FLGD M*4 Deletion [menu 1: 1=No,2=Yes]
  FLGR M*4 Reading [menu 1: 1=No,2=Yes]
  FLGU M*4 Modification [menu 1: 1=No,2=Yes]
  FLGV M*4 Del/ins management [menu 1: 1=No,2=Yes]
  NUMLIG C*2 Line no.
  REFLNK AVC Pointer
  TABLNK ATB Linked table -> [ATB]CODFIC =[ACLAK]TABLNK (ATABLE) !BSRA
  TABORI ATB Origin table -> [ATB]CODFIC =[ACLAK]TABORI (ATABLE) !Block
  TYPLNK M*5 Link type [menu 2916: 1=0,1,2=0,n,3=1,1,4=1,n]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACLAK]UPDUSR (AUTILIS) !BSRA

## ACLAMAP (ACLAKP) - Classes (mapping)
Keys (first = PK; D = duplicates allowed): ACLAKP0 CODCLA+REFLNK+KEYMAP
Fields:
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAKP]CODCLA (ACLASSE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACLAKP]CREUSR (AUTILIS) !BSRA
  KEYMAP AVA Column
  PROMAP AVA Property
  REFLNK AVC Pointer
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACLAKP]UPDUSR (AUTILIS) !BSRA
  VALDEFMAP AVC Default value

## ACLAMET (ACLAM) - Classes (methods)
Keys (first = PK; D = duplicates allowed): ACLAM0 CODCLA+CODMET; ACLAM1 CODCLA+NOMET+CODMET
Fields:
  ACSOPE A*10 Authorizations
  ACTMET ACV Activity code -> [ACV]CODACT =[ACLAM]ACTMET (ACTIV) !Block
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAM]CODCLA (ACLASSE) !Delete
  CODMET ASM Method code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACLAM]CREUSR (AUTILIS) !Other
  DONMET M*15 Return type [menu 7843: 1=Date,2=Char,3=Integer,4=Decimal,5=Text file,6=Image file]
  FLGOPE M*4 Operation [menu 1: 1=No,2=Yes]
  INDOPE ANX Index
  INTMET ATX Description
  NOMET C*4 Method no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACLAM]UPDUSR (AUTILIS) !Other

## ACLAMETSTD (ACLAT) - Classes (standard methods)
Keys (first = PK; D = duplicates allowed): ACLAT0 CODCLA+CODMETSTD; ACLAT1 CODCLA+NOMETSTD+CODMETSTD
Fields:
  ACSMETSTD A*10 Authorizations
  ACTMETSTD ACV Activity code -> [ACV]CODACT =[ACLAT]ACTMETSTD (ACTIV) !Block
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAT]CODCLA (ACLASSE) !Delete
  CODMETSTD A*5 Method code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACLAT]CREUSR (AUTILIS) !Other
  ENAMETSTD M*4 Selection [menu 1: 1=No,2=Yes]
  NOMETSTD C*4 Method no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACLAT]UPDUSR (AUTILIS) !Other

## ACLAOPT (ACLAO) - Classes (options)
Keys (first = PK; D = duplicates allowed): ACLAO0 CODCLA+OPTCOD
Fields:
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLAO]CODCLA (ACLASSE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACLAO]CREUSR (AUTILIS) !RTZ
  OPTACT ACV Activity code -> [ACV]CODACT =[ACLAO]OPTACT (ACTIV) !Block
  OPTCND AFR*250 Option condition
  OPTCOD A*10 Option code
  OPTERR ATX Error message
  OPTLIB ATX Option title
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACLAO]UPDUSR (AUTILIS) !RTZ

## ACLAPARDEF (ACLPD) - Classes (parameters)
Keys (first = PK; D = duplicates allowed): ACLPD0 CODCLA+CODE+CODPAR; ACLPD1 CODCLA+CODE+NOPAR+CODPAR (D)
Fields:
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CLAPAR ACLA Class -> [ACLA]ACLA0 =[ACLPD]CLAPAR (ACLASSE) !Block
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLPD]CODCLA (ACLASSE) !Other
  CODE ASM Method code
  CODPAR AVB Parameter code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACLPD]CREUSR (AUTILIS) !Other
  DIMPAR M*15 Dimension [menu 7987: 1=None,2=From 1,3=From 0]
  INTPAR ATX Description
  MODPAR M*15 Method [menu 34: 1=Address,2=Value,3=Constant]
  NOPAR C*4 Order
  TYPINTPAR M*15 Parameter type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  TYPKEY M*4 Key type [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACLPD]UPDUSR (AUTILIS) !Other

## ACLAPARFLD (ACLFP) - Classes (parameters)
Keys (first = PK; D = duplicates allowed): ACLFP0 CODCLA+TYPPAR+TYPKEY+FLDCLA+CODPAR; ACLFP1 CODCLA+TYPPAR+TYPKEY+FLDCLA+NUMPAR (D)
Fields:
  ADRVAL M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLFP]CODCLA (ACLASSE) !Other
  CODPAR AVB Parameter code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACLFP]CREUSR (AUTILIS) !Other
  FLDCLA AVA Field code
  NUMPAR C*4 Number
  TYPINT M*15 Internal type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  TYPKEY M*4 Keys [menu 1: 1=No,2=Yes]
  TYPPAR C*4 Parameter type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACLFP]UPDUSR (AUTILIS) !Other
  VALEUR A*80 Value

## ACLASSE (ACLA) - Classes
Keys (first = PK; D = duplicates allowed): ACLA0 CODCLA
Fields:
  ACCSTR AVA Access code
  ACTTRT ACV(20) Activity code -> [ACV]CODACT =[ACLA]ACTTRT (ACTIV) !Block
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ACLA]CODACT (ACTIV) !Block
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ACLA]CODCLA (ACLASSE) !Delete
  CODTRT ADC(20) Processing
  CPYSTR AVA Company
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACLA]CREUSR (AUTILIS) !RTZ
  FCYSTR AVA Site
  FLGACTX M*4 Contextual [menu 1: 1=No,2=Yes]
  FLGBUFFER M*4 Buffer class [menu 1: 1=No,2=Yes]
  FLGCONSULT M*4 Inquiry [menu 1: 1=No,2=Yes]
  FLGCREF M*4 Creation [menu 1: 1=No,2=Yes]
  FLGDREF M*4 Deletion [menu 1: 1=No,2=Yes]
  FLGRREF M*4 Reading [menu 1: 1=No,2=Yes]
  FLGSEARCH M*4 Searchable [menu 1: 1=No,2=Yes]
  FLGSYSTEM M*4 System [menu 1: 1=No,2=Yes]
  FLGTR M*4 Transaction management [menu 1: 1=No,2=Yes]
  FLGUREF M*4 Modification [menu 1: 1=No,2=Yes]
  FLTREF AFF*250 Filter
  INDREF ANX Main index
  INTCLA ATX Description
  KEYINT A*250 Key
  LEGSTR AVA Legislation
  LNKOBJ AOB Linked object -> [AOB]ABREV =[ACLA]LNKOBJ (AOBJET) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRTRT C*2 No. processes
  RANTRT C*4(20) Order
  RAW M*4 Technical [menu 1: 1=No,2=Yes]
  TABREF AVWT Main table
  TYPCLA M*15 Class type [menu 7986: 1=Basic,2=Persistent,3=Technical,4=System,5=Interface]
  TYPTRT M(20) Type [menu 7844: 1=Standard,2=Vertical,3=Specific]
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACLA]UPDUSR (AUTILIS) !RTZ

## ACLBSYS (ASA) - Graphic components
Keys (first = PK; D = duplicates allowed): ASA0 CAT+CODFIC
Fields:
  AUUID AUUID Single identifier
  CAT ADI Category -> [ADI]CODE =914;CAT (ATABDIV) !Block
  CLOB AC0*9 Text file (clob)
  CODFIC ASB Code -> [ASB]ASB0 =[ASA]CODFIC (ABLBSYS) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASA]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASA]UPDUSR (AUTILIS) !Other

## ACLOB (ACB) - Special folders
Notes: differs in V10 P1 (diff: ATD_ACLOB.htm)
Keys (first = PK; D = duplicates allowed): ACB0 CODBLB+IDENT1+IDENT2+IDENT3
Fields:
  AUUID AUUID Single identifier
  CLOB ACB Text file (clob)
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CODBLB A*12 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACB]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  NAMBLB DES File name
  TYPDOC ADI Document type -> [ADI]CODE =902;TYPDOC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACB]UPDUSR (AUTILIS) !Other

## ACODIF (ACO) - Section coding
Keys (first = PK; D = duplicates allowed): ACO0 ABB; ACO1 ENGDES (D); ACO2 FREDES (D)
Fields:
  ABB A*3 Abbreviation
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACO]CREUSR (AUTILIS) !Other
  ENGDES A*50 English description
  FREDES A*50 Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACO]UPDUSR (AUTILIS) !Other

## ACODNUM (ANM) - Doc sequence numbers
Keys (first = PK; D = duplicates allowed): ANM0 CODNUM
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[ANM]CODNUM (ACODNUM) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ANM]CREUSR (AUTILIS) !Other
  CTLCHR M*4 Chronological control [menu 1: 1=No,2=Yes]
  DES AX3 Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LNG C*2 Length
  NBPOS C*2 Number of components
  NIVDEF M*15 Definition level [menu 45: 1=Folder,2=Company,3=Site]
  NIVRAZ M*15 RTZ level [menu 48: 1=No RTZ,2=Annual,3=Monthly,4=Fiscal year,5=Period]
  POSCTE A*80(10) Constants
  POSLNG C*2(10) Component length
  POSTYP M*15(10) Component type [menu 47: 1=Constant,2=Year,3=Month,4=Week,5=Day,6=Company,7=Site,8=Sequence number,9=Complement,10=Fiscal year,11=Period,12=Formula]
  SEQ M*15 Sequence [menu 932: 1=Normal,2=Database sequence,3=Grouped]
  SEQABR A*5 Abbreviation
  SEQNBR C*4 No. of numerals
  SEQTBL ATB Table -> [ATB]CODFIC =[ANM]SEQTBL (ATABLE) !Block
  TYP M*15 Type [menu 46: 1=Alphanumeric,2=Numeric]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ANM]UPDUSR (AUTILIS) !Other
  ZERO M*4 Reset to zero [menu 1: 1=No,2=Yes]

## ACONSTANT (ACST) - Constants
Keys (first = PK; D = duplicates allowed): ACST0 CODVAR; ACST1 CATEG+CODVAR
Fields:
  AUUID AUUID Single identifier
  CATEG A*12 Category
  CODACT ACV Activity code -> [ACV]CODACT =[ACST]CODACT (ACTIV) !Block
  CODVAR ACST Variable code -> [ACST]ACST0 =[ACST]CODVAR (ACONSTANT) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACST]CREUSR (AUTILIS) !Other
  FLGSUP M*4 Supervisor [menu 1: 1=No,2=Yes]
  INTIT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  TYPVAR M*15 Type [menu 7882: 1=Char,2=Integer,3=Decimal,4=Date]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACST]UPDUSR (AUTILIS) !Other
  VALCHAR A*250 Value
  VALDAT D Value
  VALDEC DCB*15.6 Value
  VALINT C*4 Value

## ACONSULT (ACN) - Inquiries
Keys (first = PK; D = duplicates allowed): ACN0 COD
Fields:
  AUUID AUUID Single identifier
  COD ACN Code -> [ACN]ACN0 =[ACN]COD (ACONSULT) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[ACN]CODACT (ACTIV) !Block
  CPNKEY AVA(8) Key component
  CPNSCR AVA(8) Header fields
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACN]CREUSR (AUTILIS) !Other
  DSYCRI M*4(50) Display [menu 1: 1=No,2=Yes]
  FILABB ABR Abbreviation
  FILCND AFR*30(3) Condition
  FILKEY ANX Key
  FILNAM ATB Main table -> [ATB]CODFIC =[ACN]FILNAM (ATABLE) !Block
  FILOPN ATB(50) Table -> [ATB]CODFIC =[ACN]FILOPN (ATABLE) !Block
  FLD0 AVA(50) Criteria fields
  FLD1 AVA(50) Header fields
  LIBEL ATX Description
  MAGNETO M*4 Radio buttons [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRCPNKEY C*1 Number components
  NBRCRI C*2 Numbers of criteria
  NBRFIL C*2 Number of tables
  OBJET AOB Object -> [AOB]ABREV =[ACN]OBJET (AOBJET) !Block
  PRGSPE ADC Specific processing
  PRGSTD ADC Standard processing
  SCRCOD GTC Screen code -> [GTC]GTC0 =COD;SCRCOD (GTABACC) !RTZ
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACN]UPDUSR (AUTILIS) !Other
  WND0 FEN Criteria window -> [AWI]AWI0 =[ACN]WND0 (AWINDOW) !Block
  WND1 FEN Main window -> [AWI]AWI0 =[ACN]WND1 (AWINDOW) !Block
  ZACC AVA Access code field
  ZSITE AVA Site field

## ACONTEXT (ACTX) - Context
Keys (first = PK; D = duplicates allowed): ACTX0 CODCTX; ACTX1 CHAPTER+RANG+CODCTX; ACTX2 PARAM+CODCTX
Fields:
  AUUID AUUID Single identifier
  CHAPTER ADI Chapter -> [ADI]CODE =96;CHAPTER (ATABDIV) !Block
  CHGMOD M*4 Loading on request [menu 1: 1=No,2=Yes]
  CODACT ACV Activity code -> [ACV]CODACT =[ACTX]CODACT (ACTIV) !Block
  CODCTX ACTX Context code -> [ACTX]ACTX0 =[ACTX]CODCTX (ACONTEXT) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[ACTX]CODTYP (ATYPE) !RTZ
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACTX]CREUSR (AUTILIS) !Other
  FORDEB M*4(2) From [menu 1: 1=No,2=Yes]
  FORDIM AFR*80(2) Formula
  FORINI AFR*80 Init. formula
  INTIT ATX Description
  LNGTYP AFR*80 Length
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  PARAM ADP Parameter
  PUBFLG M*4 Public [menu 1: 1=No,2=Yes]
  RANG C*4 Sequence
  TRTINI AC0*2 Initial processing
  TRTSTD ADC Processing
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACTX]UPDUSR (AUTILIS) !Other

## ACTCODPAR (AAR) - Action parameters
Keys (first = PK; D = duplicates allowed): CODPAR CODPAR
Fields:
  AUUID AUUID Single identifier
  CODPAR AAR Parameter code -> [AAR]CODPAR =[AAR]CODPAR (ACTCODPAR) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AAR]CREUSR (AUTILIS) !Other
  INTITPAR ATX Description
  TYPPAR M*15 Parameter type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AAR]UPDUSR (AUTILIS) !Other

## ACTION (ACT) - Action dictionary
Keys (first = PK; D = duplicates allowed): ACTION ACTION
Fields:
  ABTFLG M*4 Batch [menu 1: 1=No,2=Yes]
  ACTION ACT Action code -> [ACT]ACTION =[ACT]ACTION (ACTION) !Delete
  ACTSUI ACT Linked action -> [ACT]ACTION =[ACT]ACTSUI (ACTION) !Block
  AMSFLG M*4 Workflow [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ACT]CODACT (ACTIV) !Block
  CODTRT ADC Processing
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACT]CREUSR (AUTILIS) !Other
  INSTRU A*200 Adonix instruction
  INTITA ATX Action title
  INTITC ATX Normal title
  INTITL ATX Long title
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBPAR C*2 No. of parameters
  NOWEB M*4 Batch only [menu 1: 1=No,2=Yes]
  PARAM1 ACN Inquiry code -> [ACN]ACN0 =[ACT]PARAM1 (ACONSULT) !Block
  PARAM2 FEN Main window -> [AWI]AWI0 =[ACT]PARAM2 (AWINDOW) !Block
  PARAM3 M*20 First entry [menu 78: 1=No initial entry,2=Yes / No confirmation,3=Dialog box,4=Window entry,5=List selection,6=Table selection]
  PARAM4 FEN Criteria window -> [AWI]AWI0 =[ACT]PARAM4 (AWINDOW) !Block
  PARAM5 A*10 Process for STD/SPE action
  PARAM6 M*4 Parameter [menu 1: 1=No,2=Yes]
  PUBFLG M*4 Public [menu 1: 1=No,2=Yes]
  SPETRT ADC Processing
  SUBPRG ASU Subprograms
  TYP M*20 Template [menu 81: 1=Object management,2=Inquiry,3=Standard processing,4=Window entry,5=List selection,6=Table selection,7=Miscellaneous display,8=Outside model]
  TYPACT M*4 Current field [menu 1: 1=No,2=Yes]
  TYPUTI M*30 Use type [menu 7860: 1=Miscellaneous,2=Control,3=Entry,4=Selection,5=Update,6=Information search,7=Calculation]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACT]UPDUSR (AUTILIS) !Other

## ACTIV (ACV) - Activity codes
Keys (first = PK; D = duplicates allowed): CODACT CODACT; ACV1 MODULE+CODACT; ACV2 ORDRE+CODACT
Fields:
  ACTDEP ACV Activity code -> [ACV]CODACT =[ACV]ACTDEP (ACTIV) !Block
  ACTFOR AFR*80 Formula
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ACV]CODACT (ACTIV) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACV]CREUSR (AUTILIS) !Other
  DEP M*15 Dependency [menu 74: 1=None,2=Reverse,3=Sizing,4=Formula]
  DIME L*5 Screen size
  DIMFIL L*5 Minimum size
  DIMMAX L*5 Maximum size
  FLACT M*6 Active flag [menu 1: 1=No,2=Yes]
  INTIT DES Description
  LIBACT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  ORDRE L*8 Order
  RANG C*4 Sequence
  TYP M*15 Type [menu 93: 1=Functional,2=Sizing,3=Localization]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACV]UPDUSR (AUTILIS) !Other

## ACTL (ACL) - Control tables
Keys (first = PK; D = duplicates allowed): ACL0 CTL
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACL]CREUSR (AUTILIS) !Other
  CTL ACL Table -> [ACL]ACL0 =[ACL]CTL (ACTL) !Delete
  CTLOBL AFR*80 Mandatory
  DEPCTL ACL Dependency -> [ACL]ACL0 =[ACL]DEPCTL (ACTL) !Block
  DEPCTL2 ACL Dependency -> [ACL]ACL0 =[ACL]DEPCTL2 (ACTL) !Block
  DEPCTL3 ACL Dependency -> [ACL]ACL0 =[ACL]DEPCTL3 (ACTL) !Block
  DEPVAL A*15(30) Dependent values
  DEPVAL2 A*15(30) Dependent values
  DEPVAL3 A*15(30) Dependent values
  DES AX3 Description
  EXEACT M*15 Execution [menu 928: 1=Interactive,2=Import/batch,3=Always]
  FRM AFR*80 Formula
  FRM2 AFR*80 Formula
  FRM3 AFR*80 Formula
  LSTVAL A*15(30) List of values
  LSTVAL2 A*15(30) List of values
  LSTVAL3 A*15(30) List of values
  MSG AFR*50 Error message
  MSG2 AFR*50 Error message
  MSG3 AFR*50 Error message
  NBRVAL C*2 No. of values
  NBRVAL2 C*2 No. of values
  NBRVAL3 C*2 No. of values
  OBL M*4 Mandatory field [menu 1: 1=No,2=Yes]
  TYPCTL M*20 Control type [menu 79: 1=Mandatory values,2=Prohibited values,3=Range of values,4=Table reference,5=Expression,6=Other]
  TYPCTL2 M*20 Control type [menu 79: 1=Mandatory values,2=Prohibited values,3=Range of values,4=Table reference,5=Expression,6=Other]
  TYPCTL3 M*20 Control type [menu 79: 1=Mandatory values,2=Prohibited values,3=Range of values,4=Table reference,5=Expression,6=Other]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACL]UPDUSR (AUTILIS) !Other

## ACTLDEV (ACD) - Reserved brackets
Keys (first = PK; D = duplicates allowed): ACD0 COD
Fields:
  AUUID AUUID Single identifier
  COD A*10 Development code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ACD]CREUSR (AUTILIS) !Other
  DEV M*20 Level [menu 7867: 1=Standard,2=Add-on,3=Vertical,4=Specific]
  ENV AFR*250 Environment
  INTCOD AX3 Description
  INTRAN AX3(99) Comment
  NBLIG C*3 Number of lines
  PRO M*20 Type of product [menu 7866: 1=All,2=Supervisor,3=X3,4=Geode,5=Payroll]
  RAN A*20(99) Brackets
  TYP M*20(99) Bracket type [menu 7865: 1=Object,2=Message,3=Miscellaneous table,4=Field]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ACD]UPDUSR (AUTILIS) !Other

## ACTPAR (ATR) - Action parameters
Keys (first = PK; D = duplicates allowed): NOPAR ACTION+NOPAR; CODPAR CODPAR (D)
Fields:
  ACTION ACT Action code -> [ACT]ACTION =[ATR]ACTION (ACTION) !Delete
  ADRVAL M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AUUID AUUID Single identifier
  CODPAR AAR Parameter code -> [AAR]CODPAR =[ATR]CODPAR (ACTCODPAR) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATR]CREUSR (AUTILIS) !Other
  INTITPAR ATX Parameter title
  NOPAR C*2 Parameter no.
  TYPPAR M*15 Parameter type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATR]UPDUSR (AUTILIS) !Other

## ADELETE (ADL) - Deletion
Keys (first = PK; D = duplicates allowed): ADL0 NUM; ADL1 OBJ+CLE1+CLE2
Fields:
  AUUID AUUID Single identifier
  CLE1 ID1 Identifier
  CLE2 ID2 Identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADL]CREUSR (AUTILIS) !Other
  NUM L*8 Number
  OBJ AOB Object -> [AOB]ABREV =[ADL]OBJ (AOBJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADL]UPDUSR (AUTILIS) !Other

## ADELIVER (ADLV) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLV0 COD
Fields:
  ADLVTYP M*15 Deliverable type [menu 2907: 1=Deliverable,2=Setup kit]
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLV]COD (ADELIVER) !Delete
  COMMENT A*80 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLV]CREUSR (AUTILIS) !Other
  CRYDEF CRY Default country -> [TCY]TCY0 =[ADLV]CRYDEF (TABCOUNTRY) !Block
  DLVDES AX3 Description
  DOSLEG ADI(40) Legislation -> [ADI]CODE =909;DOSLEG (ATABDIV) !Block
  EDT M*10 Edition [menu 2906: 1=,2=Premium,3=Standard,4=Standard NA,5=Standard UK,6=Standard SPAIN,7=Standard PORTUGAL,8=Standard GERMANY,9=Standard SWITZERLAND,10=Standard CHINA,11=Standard South Africa and ASEAN,12=Standard AUSTRALIA]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ITYKIT ADLK(20) Setup kit -> [ADLV]ADLV0 =[ADLV]ITYKIT (ADELIVER) !Block
  ITYKITROW L*3(20) Sequence
  LAN LAN(20) Languages -> [TLA]TLA0 =[ADLV]LAN (TABLAN) !Block
  LANDEF LAN Default language -> [TLA]TLA0 =[ADLV]LANDEF (TABLAN) !Block
  LICMODULE M*4(20) Requiring a license [menu 1: 1=No,2=Yes]
  MODENAFLG M*4(20) By default [menu 1: 1=No,2=Yes]
  MODNOTAVA M*4(20) Not available [menu 1: 1=No,2=Yes]
  MODULE M*20(20) Installed modules [menu 14: 20 values, see local-menus.md]
  PDT M Product [menu 7884: 1=Sage X3,2=Sage X3 Warehousing,3=Sage X3 HR & Payroll,4=Sage X3 Fixed Assets]
  RPBUSR AUS Supervisor -> [AUS]CODUSR =[ADLV]RPBUSR (AUTILIS) !Block
  RPTCUR CUR Inter-company currency -> [TCU]TCU0 =[ADLV]RPTCUR (TABCUR) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLV]UPDUSR (AUTILIS) !Other

## ADELIVERB (ADLB) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLB0 COD+CODFNC+CODBDG; ADLB1 COD+CODBDG+CODFNC
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLB]COD (ADELIVER) !Other
  CODBDG ADI Badge -> [ADI]CODE =83;CODBDG (ATABDIV) !Block
  CODFNC AFC Function -> [AFC]CODINT =[ADLB]CODFNC (AFONCTION) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLB]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLB]UPDUSR (AUTILIS) !Other

## ADELIVERD (ADLD) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLD0 COD+CODACT
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLD]COD (ADELIVER) !Other
  CODACT ACV Activity code -> [ACV]CODACT =[ADLD]CODACT (ACTIV) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLD]CREUSR (AUTILIS) !Other
  DIMACT L*8 Dimension
  FLGACT M*4 By default [menu 1: 1=No,2=Yes]
  LICACT M*4 Requiring a license [menu 1: 1=No,2=Yes]
  NOTAVAACT M*4 Not available [menu 1: 1=No,2=Yes]
  TYPACV M*1 Type [menu 93: 1=Functional,2=Sizing,3=Localization]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLD]UPDUSR (AUTILIS) !Other

## ADELIVERL (ADLL) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLL0 COD+FNCLIM
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLL]COD (ADELIVER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLL]CREUSR (AUTILIS) !Other
  FNCLIM ADI Function limits -> [ADI]CODE =926;FNCLIM (ATABDIV) !Block
  TYPFNCLIM ADI Type -> [ADI]CODE =925;TYPFNCLIM (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLL]UPDUSR (AUTILIS) !Other

## ADELIVERO (ADLO) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLO0 COD+TABCOD+TABKEY; ADLO1 COD+TABCOD+TABAWM (D)
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLO]COD (ADELIVER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLO]CREUSR (AUTILIS) !Other
  NULRECFLG M*908 Data [menu 1: 1=No,2=Yes]
  TABADINUM ADV Table number -> [ADV]CODE =[ADLO]TABADINUM (ATABTAB) !Block
  TABAWM AWM Template -> [AWM]AWM0 =[ADLO]TABAWM (AWRKLNK) !Block
  TABCOD ATB Table -> [ATB]CODFIC =[ADLO]TABCOD (ATABLE) !Block
  TABKEY A*200 Record key
  TABKEYFMT A*120 Key description
  TABKEYNAM A*10 Key code
  TABLEG ADI Legislation -> [ADI]CODE =909;TABLEG (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLO]UPDUSR (AUTILIS) !Other

## ADELIVERP (ADLP) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLP0 COD+PARAM+CLEPARAM
Fields:
  AUUID AUUID Single identifier
  CLEPARAM A*10 Key
  COD ADLV Code -> [ADLV]ADLV0 =[ADLP]COD (ADELIVER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLP]CREUSR (AUTILIS) !Other
  PARAM ADP Description
  TYPPARAM M*15 Value type [menu 11: 1=Alphanumeric,2=Numeric,3=Date,4=Local menu]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLP]UPDUSR (AUTILIS) !Other
  VALPARAM ADW Value

## ADELIVERR (ADLR) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLR0 COD+CODASW+CODBDG
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLR]COD (ADELIVER) !Other
  CODASW ASW Representation -> [ASW]ASW0 =[ADLR]CODASW (ASHW) !Other
  CODBDG ADI Badge -> [ADI]CODE =83;CODBDG (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLR]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLR]UPDUSR (AUTILIS) !Other

## ADELIVERT (ADLT) - Deliverable
Keys (first = PK; D = duplicates allowed): ADLT0 COD+CODSES+CODDVC
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADLT]COD (ADELIVER) !Other
  CODDVC ADI Device -> [ADI]CODE =928;CODDVC (ATABDIV) !Block
  CODSES ADI Session type -> [ADI]CODE =924;CODSES (ATABDIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADLT]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADLT]UPDUSR (AUTILIS) !Other

## ADICTRT (ADC) - Processes dictionary
Keys (first = PK; D = duplicates allowed): ADC0 CODTRT
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ADC]CODACT (ACTIV) !Block
  CODTRT ADC Processing
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADC]CREUSR (AUTILIS) !Other
  DES A*80 Description
  INTERN M*4 Internationalized [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  SRC M*4 Source delivered [menu 1: 1=No,2=Yes]
  SRCINT M*4 In-house use [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADC]UPDUSR (AUTILIS) !Other

## ADIMENSION (ADM) - Sizing elements
Keys (first = PK; D = duplicates allowed): ADM0 COD; ADM1 ORDRE+COD
Fields:
  AUUID AUUID Single identifier
  COD A*10 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADM]CREUSR (AUTILIS) !Other
  DES ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  ORDRE L*8 Order
  RANG C*4 Sequence
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADM]UPDUSR (AUTILIS) !Other

## ADOCBLB (ADB) - Documentation (linked files)
Keys (first = PK; D = duplicates allowed): ADB0 LAN+TYP+COD+LEV+SUBLEV+LIG
Fields:
  AUUID AUUID Single identifier
  COD A*30 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADB]CREUSR (AUTILIS) !Other
  LAN LAN Language -> [TLA]TLA0 =[ADB]LAN (TABLAN) !Block
  LEV C*4 Level
  LIG C*2 Line
  NAM A*40 Name
  PICTUR ABD Picture
  REPERT A*15 Directory
  SUBLEV L*4 Sub-level
  TRAFIL M*4 To translate [menu 1: 1=No,2=Yes]
  TYP ADI Type of document -> [ADI]CODE =910;TYP (ATABDIV) !Block
  TYPBLB AT Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADB]UPDUSR (AUTILIS) !Other

## ADOCCLB (ADH) - Documentation (texts)
Keys (first = PK; D = duplicates allowed): ADH0 LAN+TYP+COD+LEV+SUBLEV
Fields:
  AUUID AUUID Single identifier
  COD A*30 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADH]CREUSR (AUTILIS) !Other
  LAN LAN Language -> [TLA]TLA0 =[ADH]LAN (TABLAN) !Block
  LEV C*4 Level
  SUBLEV L*4 Sub-level
  TEXTE AC0*8 Text
  TYP ADI Type of document -> [ADI]CODE =910;TYP (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADH]UPDUSR (AUTILIS) !Other

## ADOCFLD (ADZ) - Field documentation
Keys (first = PK; D = duplicates allowed): ADZ0 LAN+MOTCLE; ADZ1 MOTCLE+LAN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADZ]CREUSR (AUTILIS) !Other
  GEN M*4 General help [menu 1: 1=No,2=Yes]
  LAN LAN Language -> [TLA]TLA0 =[ADZ]LAN (TABLAN) !Delete
  LNKHLP ADZ Linked h. -> [ADZ]ADZ0 =[V]GLANGUE;LNKHLP (ADOCFLD) !Block
  LNKORD M*15 Link [menu 7810: 1=Before,2=After]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MOTCLE ADZ Key word -> [ADZ]ADZ0 =LAN;MOTCLE (ADOCFLD) !Delete
  PRIO M*15 Translation priority [menu 2953: 1=Normal,2=High,3=Maximum,4=Do not translate]
  TEXTE AC0*5 Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADZ]UPDUSR (AUTILIS) !Other

## ADOCFNC (ADF) - Documentation links
Keys (first = PK; D = duplicates allowed): ADF0 TYP+COD+NUM
Fields:
  AUUID AUUID Single identifier
  CLELNK A*30 Link key
  COD A*30 Code
  CODACT ACV Activity code -> [ACV]CODACT =[ADF]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADF]CREUSR (AUTILIS) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NUM C*4 Line number
  TYP ADI Type of document -> [ADI]CODE =910;TYP (ATABDIV) !Block
  TYPLNK ADI Link type -> [ADI]CODE =913;TYPLNK (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADF]UPDUSR (AUTILIS) !Other

## ADOCUMENT (ADO) - Documentation
Keys (first = PK; D = duplicates allowed): ADO0 LAN+TYP+COD+LEV+SUBLEV; ADO1 LAN+TYP+COD+PAR (D); ADO2 COD+LEV+SUBLEV (D); ADO3 TYP+COD+LEV+SUBLEV (D)
Fields:
  AUUID AUUID Single identifier
  COD A*30 Code
  CODACT ACV Activity code -> [ACV]CODACT =[ADO]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADO]CREUSR (AUTILIS) !Other
  LAN LAN Language -> [TLA]TLA0 =[ADO]LAN (TABLAN) !Block
  LEV C*4 Level
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MSK AMK Screen -> [AMK]CODMSK =[ADO]MSK (AMSK) !RTZ
  PAR ADI Paragraph -> [ADI]CODE =911;PAR (ATABDIV) !Block
  PRIO M*15 Translation priority [menu 2953: 1=Normal,2=High,3=Maximum,4=Do not translate]
  STY C*2 Style
  SUBLEV L*4 Sub-level
  TIT A*80 Description
  TYP ADI Type of document -> [ADI]CODE =910;TYP (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADO]UPDUSR (AUTILIS) !Other
  VLDDAT D Posting date
  VLDFLG M*4 Validated [menu 1: 1=No,2=Yes]

## ADOPAR (ADP) - Parameters
Keys (first = PK; D = duplicates allowed): ADP0 CHAPITRE+PARAM; ADP1 PARAM; ADP3 CHAPITRE+RANG+PARAM; ADP4 OBJET+PARAM; ADP5 CHAPITRE+GRPPAR+PARAM
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ADP]ACS (ACCCOD) !Block
  AUSMODIF M*4 Modify by user [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CHAPITRE ADI Chapter -> [ADI]CODE =901;CHAPITRE (ATABDIV) !Block
  CNDMOD AFR*250 Condition
  CODACT ACV Activity code -> [ACV]CODACT =[ADP]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADP]CREUSR (AUTILIS) !Other
  GRPPAR ADI Group -> [ADI]CODE =903;GRPPAR (ATABDIV) !Block
  MODIF M*4 Changeable [menu 1: 1=No,2=Yes]
  NAM ATX Description
  NBVAL C*2 Number of values
  NIVDEF M*15 Definition level [menu 987: 1=Folder,2=Company,3=Site,4=User,5=Legislation]
  NOLIB MNL Local menu no.
  OBJET AOB Object -> [AOB]ABREV =[ADP]OBJET (AOBJET) !Block
  PARAM ADP Description
  RANG L*8 Sequence
  SELOPT A*20 Selection options
  SUPP A*10 Description
  TRAIT ADC Processing
  TYPVAL M*15 Value type [menu 11: 1=Alphanumeric,2=Numeric,3=Date,4=Local menu]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADP]UPDUSR (AUTILIS) !Other
  VALDEF M*4 Folder value [menu 1: 1=No,2=Yes]
  VALFLG M*4 Off value [menu 1: 1=No,2=Yes]
  VALUES A*10(15) Values

## ADOSACT (ADA) - Activity codes
Keys (first = PK; D = duplicates allowed): ADA0 DOSSIER+CODACT
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ADA]CODACT (ACTIV) !Other
  COP M*4 Copy [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADA]CREUSR (AUTILIS) !Other
  DIME L*5 Dimension
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ADA]DOSSIER (ADOSSIER) !Delete
  FLACT M*6 Active flag [menu 1: 1=No,2=Yes]
  INTIT DES Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADA]UPDUSR (AUTILIS) !Other

## ADOSDIM (ADE) - Sizing elements
Keys (first = PK; D = duplicates allowed): ADE0 DOSSIER+DIMCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADE]CREUSR (AUTILIS) !Other
  DIMCOD A*10 Code
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ADE]DOSSIER (ADOSSIER) !Delete
  NBR L*8 Value
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADE]UPDUSR (AUTILIS) !Other

## ADOSLIV (ADK) - Deliverables
Keys (first = PK; D = duplicates allowed): ADK0 DOSSIER+COD
Fields:
  AUUID AUUID Single identifier
  COD ADLV Code -> [ADLV]ADLV0 =[ADK]COD (ADELIVER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADK]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ADK]DOSSIER (ADOSSIER) !Delete
  INSTAL M*4 Active [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADK]UPDUSR (AUTILIS) !Other

## ADOSSIER (ADS) - Folder table
Notes: differs in V9.0 P12 (diff: AT3_ADOSSIER.htm)
Keys (first = PK; D = duplicates allowed): DOSSIER DOSSIER
Fields:
  AUUID AUUID Single identifier
  BLBLNG C*2 Image size
  CHGCOD A*10 Recoding list
  CLBLNG C*2 Text size
  CODDBA M*10 Format [menu 930: 1=ASCII,2=Unicode]
  CPTDOS A*10 Accounts folder
  CPTX3 M*4 X3 accounts [menu 1: 1=No,2=Yes]
  CRECNS M*4 Inquiry update [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMSK M*4 Screen update [menu 1: 1=No,2=Yes]
  CREOBJ M*4 Object update [menu 1: 1=No,2=Yes]
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADS]CREUSR (AUTILIS) !Other
  CREWIN M*4 Make windows up-to-date [menu 1: 1=No,2=Yes]
  CRYDEF CRY Default country -> [TCY]TCY0 =[ADS]CRYDEF (TABCOUNTRY) !Block
  DOSCOP ADS Copy folder -> [ADS]DOSSIER =[ADS]DOSCOP (ADOSSIER) !Block
  DOSHIS A*10 Purge folder
  DOSLEG ADI(40) Legislation -> [ADI]CODE =909;DOSLEG (ATABDIV) !Block
  DOSREF ADS Reference folder -> [ADS]DOSSIER =[ADS]DOSREF (ADOSSIER) !Block
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ADS]DOSSIER (ADOSSIER) !Delete
  GRPFIL M*4 Use file groups [menu 1: 1=No,2=Yes]
  LAN LAN(20) Languages -> [TLA]TLA0 =[ADS]LAN (TABLAN) !Block
  LANDEF LAN Default language -> [TLA]TLA0 =[ADS]LANDEF (TABLAN) !Block
  LANREF M*4(20) Translation ref. [menu 1: 1=No,2=Yes]
  MAJSCR M*4 Script modifications [menu 1: 1=No,2=Yes]
  MODULE M*4(20) Installed modules [menu 1: 1=No,2=Yes]
  NBLEG C*4 Number
  NBRLAN C*2 No.
  NOMDOS DES Name
  OPTINI M*4(30) Copy options [menu 1: 1=No,2=Yes]
  RPTCUR CUR Inter-company currency -> [TCU]TCU0 =[ADS]RPTCUR (TABCUR) !Block
  SIZDAT L*8 Data size
  SIZIDX L*8 Index size
  SOLAUZ M*10(99) Authorization [menu 7812: 1=None,2=Read,3=All]
  SOLDOS ADS(99) Folder -> [ADS]DOSSIER =[ADS]SOLDOS (ADOSSIER) !RTZ
  SPEFLG M*4 Specific flag [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  SYSPAR L*8(10) System parameters
  TRCFIL A*10 Log file
  TRCFILHIS A*10 Log file
  TRVAL M*4(30) Transactions [menu 1: 1=No,2=Yes]
  TSTFLG M*4 Test flag [menu 1: 1=No,2=Yes]
  TYPDBA M*15 Database type [menu 57: 1=Oracle,2=SQL Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADS]UPDUSR (AUTILIS) !Other
  VOLUME A*1 Volume

## ADOSSOL (ADD) - Solution by folder
Keys (first = PK; D = duplicates allowed): ADD0 DOSSIER+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ADD]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[ADD]DOSSIER (ADOSSIER) !Delete
  LDBA A*30 Name of the database
  LDOSTARG ADS Linked folder -> [ADS]DOSSIER =[ADD]LDOSTARG (ADOSSIER) !Other
  LLIENACT M*4 Active link [menu 1: 1=No,2=Yes]
  LMAC AMC Machine
  LPWD A*24 Password
  LPWDJAV A*30 Password
  LREP FIC*80 Directory
  LSERV L*5 Service
  LSOL ASO Solution
  LSRC A*30 Data source
  LTYPDBA M*15 Database type [menu 57: 1=Oracle,2=SQL Server]
  LTYPLIEN M*15 Link type [menu 920: 1=Miscellaneous,2=To Accounting,3=To Fixed Assets,4=To payroll,5=To Logistics]
  LTYPOS M*10 Type of OS [menu 946: 1=Unix,2=Windows,3=Linux]
  LUSR A*20 DBMS user
  LUSRJAV A*20 System user
  NUMLIG C*2 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ADD]UPDUSR (AUTILIS) !Other

## ADOVAL (ADW) - Parameter values
Keys (first = PK; D = duplicates allowed): ADW0 CMP+FCY+PARAM; ADW1 PARAM+CMP+FCY
Fields:
  AUUID AUUID Single identifier
  CMP CPY Company -> [CPY]CPY0 =[ADW]CMP (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADW]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[ADW]FCY (FACILITY) !Delete
  JEU ADI Set of values -> [ADI]CODE =912;JEU (ATABDIV) !RTZ
  PARAM ADP Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADW]UPDUSR (AUTILIS) !Other
  VALEUR ADW Value

## ADOVALAUS (ADU) - User parameter values
Keys (first = PK; D = duplicates allowed): ADU0 CODUSR+PARAM; ADU1 PARAM+CODUSR
Fields:
  AUUID AUUID Single identifier
  CODUSR AUS User -> [AUS]CODUSR =[ADU]CODUSR (AUTILIS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADU]CREUSR (AUTILIS) !Other
  JEU ADI Set of values -> [ADI]CODE =912;JEU (ATABDIV) !RTZ
  PARAM ADP Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADU]UPDUSR (AUTILIS) !Other
  VALEUR ADW Value

## ADOVALGRP (ADG) - Sets of values
Keys (first = PK; D = duplicates allowed): ADG0 CHAPITRE+GRPPAR+GRPDEF+PARAM; ADG1 GRPDEF+CHAPITRE+GRPPAR+PARAM
Fields:
  AUUID AUUID Single identifier
  CHAPITRE ADI Chapter -> [ADI]CODE =901;CHAPITRE (ATABDIV) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADG]CREUSR (AUTILIS) !Other
  GRPDEF ADI Set of values -> [ADI]CODE =912;GRPDEF (ATABDIV) !Block
  GRPPAR ADI Group -> [ADI]CODE =903;GRPPAR (ATABDIV) !Block
  PARAM ADP Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADG]UPDUSR (AUTILIS) !Other
  VALEUR ADW Value

## ADOVALHIS (AHW) - Parameter values
Keys (first = PK; D = duplicates allowed): AHW0 CMP+FCY+PARAM; AHW1 PARAM+CMP+FCY
Fields:
  AUUID AUUID Single identifier
  CMP CPY Company -> [CPY]CPY0 =[AHW]CMP (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AHW]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[AHW]FCY (FACILITY) !Delete
  JEU ADI Set of values -> [ADI]CODE =912;JEU (ATABDIV) !RTZ
  PARAM ADP Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AHW]UPDUSR (AUTILIS) !Other
  VALEUR ADW Value

## AECLIDBG (AEG) - Eclipse
Keys (first = PK; D = duplicates allowed): AEG0 NUMLIG; AEG1 DOSSIER+LOGIN (D)
Fields:
  ALIIDE A*80 IDE alias
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AEG]CREUSR (AUTILIS) !Other
  DATDEB D Start date
  DATFIN D End date
  DOSSIER ADS Folder -> [ADS]DOSSIER =[AEG]DOSSIER (ADOSSIER) !Delete
  HEUDEB L*8 Start time
  HEUFIN L*8 End time
  LOGIN ALO Login
  NUMLIG L*8 Line no.
  PORT L*8 Port
  PRTDBG L*8 MAP port
  SRVAPP AMC Application server
  SRVCLI AMC Client
  TYPDBG M*15 MAP type [menu 7877: 1=In progress,2=Debug,3=Other session]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AEG]UPDUSR (AUTILIS) !Other

## AECLIRDV (AEC) - Eclipse
Keys (first = PK; D = duplicates allowed): AEC0 NUMLIG; AEC1 DOSSIER+LOGIN (D)
Fields:
  ALIIDE A*80 IDE alias
  AUUID AUUID Single identifier
  CODTRT ADC Processing
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AEC]CREUSR (AUTILIS) !Other
  DATDEB D Start date
  DATFIN D End date
  DBGMAC A*250 Debugger machine
  DBGPRT L*8 Debugger port
  DOSSIER ADS Folder -> [ADS]DOSSIER =[AEC]DOSSIER (ADOSSIER) !Delete
  HEUDEB L*8 Start time
  HEUFIN L*8 End time
  LOGIN ALO Login
  NUMLIG L*8 Line no.
  PORT L*8 Port
  SRVAPP AMC Application server
  SRVCLI AMC Client
  SRVTRT AMC Processing server
  TYPEXE A*3 Execution type
  TYPRDV M*15 Type [menu 7862: 1=Pending,2=Under progress,3=Ended,4=Canceled,5=Error]
  UNICID L*8 Adonix id
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AEC]UPDUSR (AUTILIS) !Other
  WRKIDE FIC*250 IDE workspace

## AELT (AEL) - Web elements dictionary
Keys (first = PK; D = duplicates allowed): ELT0 ELTTYP+ELT+ELTLAN; ELT1 ELTTYP+ELTINV+ELT+ELTLAN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AEL]CREUSR (AUTILIS) !Other
  ELT A*14 Entry
  ELTINV A*1 Valid
  ELTLAN A*3 Language
  ELTSTP A*14 Time stamp
  ELTTYP A*4 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AEL]UPDUSR (AUTILIS) !Other

## AELTLINK (AEK) - Web element links
Keys (first = PK; D = duplicates allowed): ELK0 ELTTYP+ELT+ELTTYPLK+ELTLK; ELK1 ELTTYPLK+ELTLK+ELTTYP+ELT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AEK]CREUSR (AUTILIS) !Other
  ELT A*14 Entry
  ELTLK A*14 Linked element
  ELTTYP A*4 Type
  ELTTYPLK A*4 Linked type
  ELTUSAGE A*1 Type of use
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AEK]UPDUSR (AUTILIS) !Other

## AENCHAINE (AEN) - Import/export sequence
Keys (first = PK; D = duplicates allowed): CODE CODE+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CHEMIN A*250 Access path
  CODE A*10 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AEN]CREUSR (AUTILIS) !Other
  DES AX3 Description
  MODELE AOE Template -> [AOE]AOE0 =[AEN]MODELE (AOBJEXT) !Block
  NUMLIG C*3 Order no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AEN]UPDUSR (AUTILIS) !Other

## AENTREE (APE) - Entry points
Keys (first = PK; D = duplicates allowed): APE0 TRTSTD+OBJ+TRTSPE
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[APE]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APE]CREUSR (AUTILIS) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  OBJ AOB Object -> [AOB]ABREV =[APE]OBJ (AOBJET) !Block
  RNG C*4 Order
  TRTPAR A*250 Setup
  TRTSPE ADC Specific processing
  TRTSTD ADC Standard processing
  TYP M*4 Type [menu 7989: 1=Entry point,2=Object]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APE]UPDUSR (AUTILIS) !Other

## AESPION (AES) - Trace system transactions
Keys (first = PK; D = duplicates allowed): ESPDAT ESPDAT+ESPTIM (D); ESPUSR ESPUSR+ESPDAT+ESPTIM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AES]CREUSR (AUTILIS) !Other
  ESP1 ID Parameter
  ESP2 ID Parameter
  ESPDAT D Date
  ESPFNC AFC Function -> [AFC]CODINT =[AES]ESPFNC (AFONCTION) !Delete
  ESPMOT ADI Reason -> [ADI]CODE =81;ESPMOT (ATABDIV) !RTZ
  ESPNAT M*15 Operation nature [menu 83: 1=Create,2=Change,3=Cancel,4=Validate,5=Edit,6=Code]
  ESPTAB ATB Table -> [ATB]CODFIC =[AES]ESPTAB (ATABLE) !Delete
  ESPTIM A*8 Time
  ESPUSR AUS User -> [AUS]CODUSR =[AES]ESPUSR (AUTILIS) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AES]UPDUSR (AUTILIS) !Other

## AEXPV3 (AEV) - Table setup/import
Keys (first = PK; D = duplicates allowed): AEV0 CODE
Fields:
  AUUID AUUID Single identifier
  CODDBA M*10 File format [menu 945: 1=ascii,2=utf-8,3=ucs-2]
  CODE AEV Code -> [AEV]AEV0 =[AEV]CODE (AEXPV3) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AEV]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FILV3 FIC*250 File to convert
  FILX3 FIC*250 Destination file
  FLGV3 A*10(8) Break field
  INTIT AX3 Description
  MODELE AOE Template -> [AOE]AOE0 =[AEV]MODELE (AOBJEXT) !Block
  TYPV3 M*15 Destination type [menu 921: 1=Client,2=Server]
  TYPX3 M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AEV]UPDUSR (AUTILIS) !Other

## AEXPV3D (AED) - Table setup/import
Keys (first = PK; D = duplicates allowed): AED0 CODE+LIG
Fields:
  AUUID AUUID Single identifier
  CODE AEV Code -> [AEV]AEV0 =[AED]CODE (AEXPV3) !Delete
  COND A*80 Condition
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AED]CREUSR (AUTILIS) !Other
  INIT A*80 Initialization
  LIG C*4 Line
  NUMTAB AOR Transcoding -> [AOR]AOR0 =NUMTAB;1 (AOBJEXTR) !RTZ
  OBLIG M*4 Mandatory field [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AED]UPDUSR (AUTILIS) !Other
  ZON A*10 Field no.

## AFCTCUR (AFU) - Current function
Notes: differs in V9.0 P12 (diff: AT3_AFCTCUR.htm)
Keys (first = PK; D = duplicates allowed): AFU0 UID+FCT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AFU]CREUSR (AUTILIS) !Other
  FCT A*80 Function
  LOGIN ALO Login
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  UID A*12 Identifier
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AFU]UPDUSR (AUTILIS) !Other
  USR AUS Code -> [AUS]CODUSR =[AFU]USR (AUTILIS) !Delete

## AFCTEXE (AFE) - Last functions executed
Keys (first = PK; D = duplicates allowed): AFE0 USR+LIG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AFE]CREUSR (AUTILIS) !Other
  FCT AFC Function -> [AFC]CODINT =[AFE]FCT (AFONCTION) !Delete
  LIG L*8 Line number
  TRN A*10 Transaction
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AFE]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AFE]USR (AUTILIS) !Delete

## AFCTFCT (AFT) - User function profile
Keys (first = PK; D = duplicates allowed): AFT0 PRFCOD
Fields:
  ALLACS M*4 All access [menu 1: 1=No,2=Yes]
  ALLFCT M*4 All functions [menu 1: 1=No,2=Yes]
  AUTETA M*4(99) Report group author. [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AFT]CREUSR (AUTILIS) !Other
  DIFIMP M*4 [menu 1: 1=No,2=Yes]
  FCYDEF FCY(20) Default site -> [FCY]FCY0 =[AFT]FCYDEF (FACILITY) !Block
  FILTRE A*10 Report filters
  FLGPOR M*4 Fixed dashboard [menu 1: 1=No,2=Yes]
  INTPRF AX3 Description
  PRFCOD AFT Profile code -> [AFT]AFT0 =[AFT]PRFCOD (AFCTFCT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AFT]UPDUSR (AUTILIS) !Other

## AFCTFCY (AFF) - Site profile function
Keys (first = PK; D = duplicates allowed): AFF0 FCY+PRFCOD+FNC; AFF1 PRFCOD+FNC (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AFF]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[AFF]FCY (FACILITY) !Delete
  FNC AFC Function -> [AFC]CODINT =[AFF]FNC (AFONCTION) !Delete
  OPT A*23 Options
  PRFCOD AFT Profile code -> [AFT]AFT0 =[AFF]PRFCOD (AFCTFCT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AFF]UPDUSR (AUTILIS) !Other

## AFCTPRF (AFP) - Functional authorization
Keys (first = PK; D = duplicates allowed): AFP0 PRFCOD+FNC+FCYGRU
Fields:
  ACS M*4 Access [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation author -> [AUS]CODUSR =[AFP]CREUSR (AUTILIS) !Other
  FCYGRU CPY Site grouping -> [CPY]CPY0 =[AFP]FCYGRU (COMPANY) !Delete
  FCYGRUCOD M*15 Menu [menu 912: 1=Site grouping,2=Site]
  FNC AFC Function -> [AFC]CODINT =[AFP]FNC (AFONCTION) !Delete
  OPT A*23 Options
  PRFCOD AFT Profile code -> [AFT]AFT0 =[AFP]PRFCOD (AFCTFCT) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change author -> [AUS]CODUSR =[AFP]UPDUSR (AUTILIS) !Other

## AFONCTION (AFC) - Function dictionary
Keys (first = PK; D = duplicates allowed): CODINT CODINT; CODEXT CODEXT; MENU MENU+RANG+CODINT; NUMFNC NUMFNC; MODULE MODULE+MENU+CODINT
Fields:
  ACTION ACT Action code -> [ACT]ACTION =[AFC]ACTION (ACTION) !Block
  ACTOPT ACV(19) Activity code -> [ACV]CODACT =[AFC]ACTOPT (ACTIV) !Block
  ACTVAR ACV(10) Activity code -> [ACV]CODACT =[AFC]ACTVAR (ACTIV) !Block
  AIDE ATX Entry help
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AFC]CODACT (ACTIV) !Block
  CODEXT A*12 External code
  CODINT AFC Internal code -> [AFC]CODINT =[AFC]CODINT (AFONCTION) !Delete
  CODPAR AAR(20) Parameter code -> [AAR]CODPAR =[AFC]CODPAR (ACTCODPAR) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AFC]CREUSR (AUTILIS) !Other
  FCYAUZ M*4 Authorization site [menu 1: 1=No,2=Yes]
  FLAG A*1(19) Options
  FNCOPT AFC(19) Function -> [AFC]CODINT =[AFC]FNCOPT (AFONCTION) !RTZ
  LIBMENU ATX Menu title
  MENU AFC Parent menu -> [AFC]CODINT =[AFC]MENU (AFONCTION) !RTZ
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MONO M*4 Single [menu 1: 1=No,2=Yes]
  NAVIG M*30 Navigation [menu 7848: 1=Authorized,2=Prohibited to this function,3=Prohibited from this function,4=Prohibited in all cases]
  NBOPT C*4 No. of options
  NBVAR C*4 Number of variables
  NOM ATX Description
  NUMFNC L*8 Number
  OPTION ATX(19) Option title
  RANG C*4 Row in menu
  RPT1 ARX Report 1
  RPT2 ARX Report 2
  TRAIT ADC Menu/process
  TRTENT A*10 Entry points
  TYP M*4 Access type object [menu 1: 1=No,2=Yes]
  TYPTRAIT M*20 Function type [menu 13: 1=Process,2=Menu]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AFC]UPDUSR (AUTILIS) !Other
  VALEUR A*20(10) Value
  VALPAR A*30(20) Parameter value
  VARIA AVA(10) Variable

## AFORDIM (AFO) - Sizing formulas
Keys (first = PK; D = duplicates allowed): AFO0 CODFIC
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[AFO]CODFIC (ATABLE) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AFO]CREUSR (AUTILIS) !Other
  FORDIM AFR*80 Formula
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AFO]UPDUSR (AUTILIS) !Other

## AGDPRMAI (AGMAI) - 
Notes: not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): AGMAI0 NUMREQ; AGMAI1 MAICOD+TABCOD+TABFLD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AGMAI]CREUSR (AUTILIS) !Other
  MAICOD MAI
  NUMREQ L*8 Query no.
  TABCOD ATB Table -> [ATB]CODFIC =[AGMAI]TABCOD (ATABLE) !Block
  TABFLD AVA Fields
  TABKEY A*200 Record key
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AGMAI]UPDUSR (AUTILIS) !Other

## AGDPRPHONE (AGPHO) - 
Notes: not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): AGPHO0 NUMREQ; AGPHO1 TELCOD+TABCOD+TABFLD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AGPHO]CREUSR (AUTILIS) !Other
  NUMREQ L*8 Query no.
  TABCOD ATB Table -> [ATB]CODFIC =[AGPHO]TABCOD (ATABLE) !Block
  TABFLD AVA Fields
  TABKEY A*200 Record key
  TELCOD E164TEL
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AGPHO]UPDUSR (AUTILIS) !Other

## AGDPRSETTING (AGS) - GDPR setup
Notes: not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): AGS0 CODE; AGS1 TYP+CODE; AGS2 TYP+CODATY+CODATB+CODE
Fields:
  AUUID AUUID Single identifier
  CODATB ATB Table -> [ATB]CODFIC =[AGS]CODATB (ATABLE) !Block
  CODATY ATY Data type -> [ATY]CODTYP =[AGS]CODATY (ATYPE) !Block
  CODE A*20 Code
  CODFLD AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AGS]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  RECSTD M*4 Standard [menu 1: 1=No,2=Yes]
  TYP M*20 Type [menu 7947: 1=Reference,2=E-mail,3=Phone]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AGS]UPDUSR (AUTILIS) !Other

## AGDPRVCR (AGVCR) - GDPR search
Notes: not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): AGVCR0 UID+CODATY+CODFIC+CODE+VCRKEY; AGVCR1 UID+VCRKEY (D)
Fields:
  AUUID AUUID Single identifier
  CODATY ATY Data type -> [ATY]CODTYP =[AGVCR]CODATY (ATYPE) !Block
  CODE A*30 Code
  CODFIC ATB Table -> [ATB]CODFIC =[AGVCR]CODFIC (ATABLE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AGVCR]CREUSR (AUTILIS) !Other
  DATMAX D Maximum date
  DATMIN D Earliest date
  UID L*8 Identifier
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AGVCR]UPDUSR (AUTILIS) !Other
  VCRKEY A*50 Document

## AGLOBVAR (AGB) - Global variables
Keys (first = PK; D = duplicates allowed): AGB0 CODVAR; AGB1 TRTSTD+RANG+CODVAR; AGB2 PARAM+CODVAR
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AGB]CODACT (ACTIV) !Block
  CODTYP ATY Data type -> [ATY]CODTYP =[AGB]CODTYP (ATYPE) !RTZ
  CODVAR AGB Variable code -> [AGB]AGB0 =[AGB]CODVAR (AGLOBVAR) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AGB]CREUSR (AUTILIS) !Other
  FORDEB M*4(2) From [menu 1: 1=No,2=Yes]
  FORDIM AFR*80(2) Formula
  FORINI AFR*80 Init. formula
  INTIT ATX Description
  LNGTYP AFR*80 Length
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  PARAM ADP Parameter
  PUBFLG M*4 Public [menu 1: 1=No,2=Yes]
  RANG C*4 Sequence
  TRTINI AC0*2 Initial processing
  TRTSTD ADC Processing
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AGB]UPDUSR (AUTILIS) !Other

## AGRPCPY (AGC) - Company groupings
Keys (first = PK; D = duplicates allowed): AGC0 GRP+CPY; AGC1 CPY+GRP
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[AGC]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AGC]CREUSR (AUTILIS) !Other
  GRP AGF Group -> [AGF]AGF0 =[AGC]GRP (AGRPFCY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AGC]UPDUSR (AUTILIS) !Other

## AGRPFCY (AGF) - Site groupings
Keys (first = PK; D = duplicates allowed): AGF0 GRP
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AGF]CREUSR (AUTILIS) !Other
  DES DES Description
  EXPNUM L*8 Export number
  FLGCPY M*4 Group of company [menu 1: 1=No,2=Yes]
  FLGLEG M*4 Legal company [menu 1: 1=No,2=Yes]
  GRP AGF Group -> [AGF]AGF0 =[AGF]GRP (AGRPFCY) !Delete
  SHO SHO Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AGF]UPDUSR (AUTILIS) !Other

## AHISTO (AHI) - History/purge
Keys (first = PK; D = duplicates allowed): AHI0 COD
Fields:
  AUUID AUUID Single identifier
  COD AHI Code -> [AHI]AHI0 =[AHI]COD (AHISTO) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[AHI]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AHI]CREUSR (AUTILIS) !Other
  CTLTRT ADC Processing
  DAT1 D Date
  DAT2 D Date
  DES ATX Description
  DESSHO ATX Short description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLG1 M*4 Archive [menu 1: 1=No,2=Yes]
  FLG2 M*4 Purge [menu 1: 1=No,2=Yes]
  FRQ1 C*4 Frequency
  FRQ2 C*4 Frequency
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRTBL C*2 Number of tables
  SPETRT ADC Processing
  TIM1 C*4 Data retention days
  TIM2 C*4 Purge time
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AHI]UPDUSR (AUTILIS) !Other

## AHISTOD (AHD) - History/purge
Keys (first = PK; D = duplicates allowed): AHD0 COD+LIG
Fields:
  AUUID AUUID Single identifier
  COD AHI Code -> [AHI]AHI0 =[AHD]COD (AHISTO) !Delete
  CPYFLD AVA Company field
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AHD]CREUSR (AUTILIS) !Other
  DATFLD AVA Date field
  FCYFLD AVA Site field
  FRM AFR*250 Formula
  LIG C*3 Line number
  LNKTBL ATB Linked tables -> [ATB]CODFIC =[AHD]LNKTBL (ATABLE) !Block
  TBL ATB Table -> [ATB]CODFIC =[AHD]TBL (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AHD]UPDUSR (AUTILIS) !Other

## AINDEX (ANX) - Specific index
Keys (first = PK; D = duplicates allowed): ANX0 LIG; ANX1 TABLE+LIG; ANX2 TABLE+CODIND
Fields:
  AUUID AUUID Single identifier
  CODIND ANX Index code
  COM ATX Comment
  COMDES AXX Comment
  COMMENT A*40 Comment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ANX]CREUSR (AUTILIS) !Other
  DESCRIPT A*120 Index descriptor
  FLACT M*4 Active flag [menu 1: 1=No,2=Yes]
  LIG C*3 Line number
  TABLE ATB Table -> [ATB]CODFIC =[ANX]TABLE (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ANX]UPDUSR (AUTILIS) !Other

## AITRLNK (AIT) - Interactive components
Keys (first = PK; D = duplicates allowed): AIT0 CODLNK
Fields:
  AUUID AUUID Single identifier
  CNTFRM AFR*250 Counting
  CODCOL ADI(20) Color -> [ADI]CODE =922;CODCOL (ATABDIV) !Block
  CODFUN AFC Function -> [AFC]CODINT =[AIT]CODFUN (AFONCTION) !Block
  CODLNK A*20 Identifier
  CODSHP ADI(20) Form -> [ADI]CODE =923;CODSHP (ATABDIV) !Block
  CODTRA AFR*250 Transaction
  CODVAL L*8(20) Value
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AIT]CREUSR (AUTILIS) !Other
  INTIT AX3 Description
  KEYVAL AFR*250 Value of the key
  LFTLST A*30 Left list
  NBRVAL ABS
  PARVAL A*30 Parameter
  REDOLY M*4 Read only [menu 1: 1=No,2=Yes]
  SELFRM AFR*250 Selection
  TIPTEX AXX Tooltip
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AIT]UPDUSR (AUTILIS) !Other

## AJSAUDIT (AJA) - Audit
Notes: activity code ASD
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## AJSCONT (AJC) - Sdata contract
Notes: activity code ASD
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## AJSEXCEPT (AJE) - Exception
Notes: activity code ASD
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## AJSSYNC (AJS) - Synchro
Notes: activity code ASD
Fields: (Sage publishes no key or column detail for this table in this version's help - read the structure from the client's folder)

## ALINK (ALI) - Link explorer
Keys (first = PK; D = duplicates allowed): ALI0 USRCOD+SRCOBJ+SRCKEY+DSTOBJ+DSTKEY
Fields:
  AUTFLG M*4 Automatic [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ALI]CREUSR (AUTILIS) !Other
  DSTDES DES Description
  DSTKEY ID2 Destination key
  DSTOBJ AOB Destination object -> [AOB]ABREV =[ALI]DSTOBJ (AOBJET) !Delete
  DSTTIT ATX Title
  DSTXXX A*45 Technical field
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  INVFLG M*4 Reverse link [menu 1: 1=No,2=Yes]
  LNK ADI Link code -> [ADI]CODE =61;LNK (ATABDIV) !Delete
  SRCKEY ID2 Source key
  SRCOBJ AOB Source object -> [AOB]ABREV =[ALI]SRCOBJ (AOBJET) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ALI]UPDUSR (AUTILIS) !Other
  USRCOD A*10 Group

## ALISTEC (ALC) - Graphical query tool
Keys (first = PK; D = duplicates allowed): ALC0 COD
Fields:
  AUUID AUUID Single identifier
  CLBCNF AC0*2 Configuration
  COD ALH Code -> [ALH]ALH0 =[ALC]COD (ALISTEH) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALC]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALC]UPDUSR (AUTILIS) !Other

## ALISTED (ALD) - Query tool
Keys (first = PK; D = duplicates allowed): ALD0 COD+LIG; ALD1 COD+ORD (D)
Fields:
  AUUID AUUID Single identifier
  BOLD M*4 Bold [menu 1: 1=No,2=Yes]
  CLC A*250 Expression
  COD ALH Code -> [ALH]ALH0 =[ALD]COD (ALISTEH) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[ALD]CODTYP (ATYPE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALD]CREUSR (AUTILIS) !Other
  CUM M*4 Total [menu 1: 1=No,2=Yes]
  FLD A*15 Field
  FONT M*25 Font [menu 2903: 1=Standard,2=Arial,3=Times New Roman]
  GRA M*15 Graph type [menu 2937: 1=Value,2=Default,3=Description,4=None]
  GRP M*4 Group [menu 1: 1=No,2=Yes]
  INTITLIG AX3 Description
  ITALICS M*4 Italic [menu 1: 1=No,2=Yes]
  LIG C*3 Line number
  LNG DCB*3.2 Length
  NIV C*4 Level
  NOLIB L*5 Local menu no.
  NUMTEX C*4 Text number
  ORD C*3 Order
  REP M*15 Representation [menu 2938: 1=Default,2=Bar,3=Line]
  SRT M*15 Sort [menu 10: 1=None,2=Ascending,3=Descending]
  STREND M*15 Range [menu 890: 1=No,2=Yes,3=Criteria not displayed]
  TBL AVWT Table
  TUN M*4 Tunnel toward object [menu 1: 1=No,2=Yes]
  UNDERLINE M*4 Underlined [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALD]UPDUSR (AUTILIS) !Other
  VALDEB AFR*80 Default value
  VALFIN AFR*80 Default value

## ALISTEH (ALH) - Query tool
Keys (first = PK; D = duplicates allowed): ALH0 COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ALH]ACS (ACCCOD) !Block
  AFFGRA M*15 Default display [menu 2936: 1=Table,2=Graph]
  ALLUSR M*15 Query type [menu 2915: 1=Normal,2=Shared,3=Recalculated]
  AUUID AUUID Single identifier
  COD ALH Code -> [ALH]ALH0 =[ALH]COD (ALISTEH) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ALH]CREUSR (AUTILIS) !Other
  DEFGRA M*15 Default graph [menu 2933: 1=Bars,2=Lines,3=Areas,4=Sectors]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCTLNK AFC Function -> [AFC]CODINT =[ALH]FCTLNK (AFONCTION) !Block
  FSHGRA M*15 Representation [menu 2939: 1=Multiple,2=Cumulation,3=Comparison,4=Month,5=Week,6=Day]
  GRAFLG M*4 Active graphic [menu 1: 1=No,2=Yes]
  GRP A*10 Group
  INTIT AX3 Description
  INTITSHO AX1 Short description
  LNK A*120(5) Link
  MAXLIG L*8 Maximum lines
  MAXTIM L*8 Maximum times
  NBRCOL C*2 No. of fixed columns
  NBRLIG C*4 Number of lines
  OBJLNK AOB Object -> [AOB]ABREV =[ALH]OBJLNK (AOBJET) !Block
  POSGRA M*15 Position [menu 2931: 1=To the right,2=To the left,3=Above,4=Below]
  REPGRA M*15 Representation [menu 2930: 1=Character,2=Character or graph,3=Character and graph,4=Graph]
  RPT ARP Report -> [ARP]ARP0 =[ALH]RPT (AREPORT) !Block
  SEL A*120(5) Selection criteria
  TYP C*1 Type
  TYPGRA M*15 Type [menu 2932: 1=Simple graph,2=Multiple graph,3=Planning calendar,4=XSL,5=Gantt,6=Query tool]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ALH]UPDUSR (AUTILIS) !Other

## ALISTEL (ALL) - Graphical query tool
Keys (first = PK; D = duplicates allowed): ALL0 COD+LNKORG+LNKDES
Fields:
  AUUID AUUID Single identifier
  COD ALH Code -> [ALH]ALH0 =[ALL]COD (ALISTEH) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALL]CREUSR (AUTILIS) !Other
  LNKDES A*20 Link
  LNKORG A*20 Link
  LNKTYP M*15 Join type [menu 7823: 1=Inner,2=Left outer,3=Right outer]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALL]UPDUSR (AUTILIS) !Other

## ALISTER (ALR) - Query tool
Keys (first = PK; D = duplicates allowed): ALR0 COD+USR+NIV+LIG+COL
Fields:
  AUUID AUUID Single identifier
  COD ALH Code -> [ALH]ALH0 =[ALR]COD (ALISTEH) !Other
  COL C*4 Column
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM A*4 Time
  CREUSR AUS User -> [AUS]CODUSR =[ALR]CREUSR (AUTILIS) !Other
  DAT D Date
  LIG L*8 Line
  NIV C*4 Level
  NUM DCB*13.2 Value
  TYP M*15 Type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALR]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[ALR]USR (AUTILIS) !Other
  VLR AVR Value

## ALISTET (ALT) - Graphical query tool
Keys (first = PK; D = duplicates allowed): ALT0 COD+TBL
Fields:
  AUUID AUUID Single identifier
  COD ALH Code -> [ALH]ALH0 =[ALT]COD (ALISTEH) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALT]CREUSR (AUTILIS) !Other
  HIG C*4 Height
  LRG C*4 Width
  TBL ATB Table -> [ATB]CODFIC =[ALT]TBL (ATABLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALT]UPDUSR (AUTILIS) !Other
  X C*4 Position
  Y C*4 Position

## ALNKSUB (ALB) - Subdivision links
Keys (first = PK; D = duplicates allowed): ALB0 CRY+TYP+POS; ALB1 COD+CRY+TYP (D)
Fields:
  AUUID AUUID Single identifier
  COD SAT Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ALB]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[ALB]CRY (TABCOUNTRY) !Delete
  POS A*20 Postal code
  TYP M*15 Subdivision [menu 7831: 1=None,2=Subdivision 1,3=Subdivision 2]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ALB]UPDUSR (AUTILIS) !Other

## ALOGIN (ALO) - Login table
Notes: activity code AUDIT
Keys (first = PK; D = duplicates allowed): ALO0 BDDID+FLG (D); ALO1 SEQ; ALO2 ADOID (D)
Fields:
  ADOID A*10 X3 identifier
  ADOLOG ALO X3 login
  ADOTYP M*15 Type of connection [menu 924: 35 values, see local-menus.md]
  ADOUSR A*5 X3 user
  ADRCLI A*30 Customer address
  AUUID AUUID Single identifier
  BDDID A*10 BDD identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALO]CREUSR (AUTILIS) !Other
  DATCNX D Connection date
  DATDCX D Disconnection date
  FLG M*4 Active flag [menu 1: 1=No,2=Yes]
  HOUCNX HS Connection time
  HOUDCX HS Time of connection
  MSG A*80 Message
  SEQ L*8 Sequence no.
  STA C*4 Status
  SYSUSR A*20 System user
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALO]UPDUSR (AUTILIS) !Other

## ALSTRD (ALS) - Last records read
Keys (first = PK; D = duplicates allowed): ALS0 USR+OBJ+LIG
Fields:
  AUUID AUUID Single identifier
  CLES ID1 Key
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ALS]CREUSR (AUTILIS) !Other
  LIG L*8 Line number
  OBJ AOB Object to process -> [AOB]ABREV =[ALS]OBJ (AOBJET) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ALS]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[ALS]USR (AUTILIS) !Other

## AMAINT (AMI) - Database mass update
Keys (first = PK; D = duplicates allowed): AMI0 COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[AMI]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  COD A*5 Code
  CODACT ACV Activity code -> [ACV]CODACT =[AMI]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AMI]CREUSR (AUTILIS) !Other
  FLD A*15(6) Field
  FLDFRM AFR*80(6) Formulas
  FLDSUP M*4(6) Deletion [menu 915: 1=Modification,2=Deletion,3=Creation]
  FLDTBL ATB(6) Tables -> [ATB]CODFIC =[AMI]FLDTBL (ATABLE) !Other
  INTIT ATX Description
  INTITSHO ATX Short description
  LNKEXP A*50(5) Link
  LNKFLD A*15(5) Fields
  LNKTBL ATB(5) Linked tables -> [ATB]CODFIC =[AMI]LNKTBL (ATABLE) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRFLD C*2 Field nb
  NBRFRM C*2 Number
  NBRLNK C*2 No. of links
  NBRVAR C*2 Number
  SELFRM AFR*80(5) Selection formulas
  TBL ATB Table -> [ATB]CODFIC =[AMI]TBL (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AMI]UPDUSR (AUTILIS) !Other
  VARCTL ACL(6) Control table -> [ACL]ACL0 =[AMI]VARCTL (ACTL) !Block
  VARDEF AFR*50(6) Default value
  VARINTIT ATX(6) Description
  VARLNG DCB*8(6) Length
  VARMEN MNL(6) Local menu
  VARPAR A*10(6) Object parameter
  VARTYP ATY(6) Type -> [ATY]CODTYP =[AMI]VARTYP (ATYPE) !Block

## AMEMO (AMM) - Memo
Keys (first = PK; D = duplicates allowed): AMM0 MEMO
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AMM]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AMM]CREUSR (AUTILIS) !Other
  DES ATX Description
  MEMO A*10 Memo
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AMM]UPDUSR (AUTILIS) !Other
  WIN FEN Window -> [AWI]AWI0 =[AMM]WIN (AWINDOW) !Other

## AMENLOC (AML) - Header messages
Keys (first = PK; D = duplicates allowed): MENLOC MENLOC
Fields:
  AUUID AUUID Single identifier
  AUZMOD M*4 Changeable [menu 1: 1=No,2=Yes]
  CODACT ACV Activity code -> [ACV]CODACT =[AML]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AML]CREUSR (AUTILIS) !Other
  LONG C*3 Length
  MAXI C*4 Maximum number
  MENLOC MNL Local menu
  MENLOCAL M*4 Local menu flag [menu 1: 1=No,2=Yes]
  MINI C*4 Minimum number
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NONTRA M*4 Do not translate [menu 1: 1=No,2=Yes]
  SPECIF M*4 Specific [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AML]UPDUSR (AUTILIS) !Other

## AMENUSER (AMU) - User profile menu
Keys (first = PK; D = duplicates allowed): CODMEN CODPRF+NUMLIG; MENCOD CODPRF+MENU+NUMLIG; MENFCT CODPRF+FONCTION (D)
Fields:
  AUUID AUUID Single identifier
  CODMEN A*15 Menu code
  CODPRF APM Profile code -> [APF]CODPRF =0;CODPRF (APROFIL) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AMU]CREUSR (AUTILIS) !Other
  FONCTION AFC Function -> [AFC]CODINT =[AMU]FONCTION (AFONCTION) !Delete
  INTIT A*35 Description
  LIBMENU ATX Description
  MENU A*5 Menu code
  NUMLIG C*4 Line number
  ORDSYS A*40 System command
  TYPFCT C*1 Function type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMU]UPDUSR (AUTILIS) !Other

## AMETUTI (AME) - Professional profile
Keys (first = PK; D = duplicates allowed): AME0 CODMET
Fields:
  AUUID AUUID Single identifier
  CODMET AME Profession code -> [AME]AME0 =[AME]CODMET (AMETUTI) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AME]CREUSR (AUTILIS) !Other
  INTMET AX3 Description
  PRFFCT AFT Function profile -> [AFT]AFT0 =[AME]PRFFCT (AFCTFCT) !Block
  PRFMEN APM Menu profile -> [APF]CODPRF =0;PRFMEN (APROFIL) !Block
  PRFXTD AYH Safe X3 WAS profile -> [AYH]AYH0 =[AME]PRFXTD (AYTPRFUSR) !Block act:AYT
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AME]UPDUSR (AUTILIS) !Other
  USRBI AIU BI user -> [AIU]AIU0 =[AME]USRBI (ABIPRFUSR) !Block act:ABI

## AMIGKEY (AMY) - Keys
Notes: differs in V9.0 P12 (diff: AT3_AMIGKEY.htm); differs in V10 P1 (diff: ATD_AMIGKEY.htm)
Keys (first = PK; D = duplicates allowed): AMY0 DOSSIER+IDENT
Fields:
  AUUID AUUID Single identifier
  CLOB ACB Text file (clob)
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AMY]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[AMY]DOSSIER (ADOSSIER) !Delete
  IDENT ID1 Identifier
  PCDRECNBR ANB No. processed
  PROENDFLG M*15 Status [menu 21: 1=Standby,2=In progress,3=Finished,4=Held,5=Kill,6=Canceled,7=Error,8=Overdue,9=Warning]
  PRORECNBR ANB No. read
  TOTRECNBR DCB*12.3 No. of records
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMY]UPDUSR (AUTILIS) !Other

## AMOTCLE (AMC) - Help key-words
Keys (first = PK; D = duplicates allowed): AMC0 TYPZON+IDENT1+IDENT2; AMC1 IDENT1+IDENT2 (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AMC]CREUSR (AUTILIS) !Other
  IDENT1 A*30 Identifier 1
  IDENT2 A*200 Identifier 2
  INFBUL ADZ Screentip -> [ADZ]ADZ0 =[V]GLANGUE;INFBUL (ADOCFLD) !Block
  MOTCLE ADZ Help key-word -> [ADZ]ADZ0 =[V]GLANGUE;MOTCLE (ADOCFLD) !Block
  TYPZON M*20 Type [menu 7985: 1=Table,2=Screen,3=Class,4=Representation]
  UNAFFHTM M*4 Hidden in HTML [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMC]UPDUSR (AUTILIS) !Other

## AMOULIN (AI0) - Migration process
Keys (first = PK; D = duplicates allowed): AI01 CODE; AI02 INDICEM
Fields:
  ACTIF M*4 Active [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CODE A*12 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AI0]CREUSR (AUTILIS) !Other
  DESCRIP ATX Description
  DESCRIP1 ATX Description
  DESCRIP2 ATX Description
  ETAPE M*20 Step [menu 7906: 1=Initialization,2=Common data,3=Module,4=Post-migration]
  INDICEM L*6 Index
  INDMOD C*4 Module index
  INTIT ATX Description
  MODULE M*20 Module [menu 14: 20 values, see local-menus.md]
  PHASE C*4 Phase
  RANG C*4 Sequence
  RANGMOD C*4 Module rank
  STANDARD M*4 Standard [menu 1: 1=No,2=Yes]
  TABLEM ATB(12) Tables -> [ATB]CODFIC =[AI0]TABLEM (ATABLE) !Other
  TABLEP ATB Main table -> [ATB]CODFIC =[AI0]TABLEP (ATABLE) !Other
  TABTYP M*4(12) Update [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AI0]UPDUSR (AUTILIS) !Other

## AMOULIN1 (AI1) - Migration plan
Keys (first = PK; D = duplicates allowed): AI11 PLAN
Fields:
  AUUID AUUID Single identifier
  CODEEC A*12 Procedure in progress
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AI1]CREUSR (AUTILIS) !Other
  DAAFIL A*50 Data
  DATEEC D Update date
  DATEL D Launch date
  DOSSIER ADS Folder -> [ADS]DOSSIER =[AI1]DOSSIER (ADOSSIER) !Other
  HEUEC HM Update time
  HEUL HM Launch time
  IDXFIL A*50 Index
  INTIT DES Description
  NBPARL C*4 No. of parallel launches
  NBREL C*4 Number of relaunches
  NOMTRACE A*200 Global log
  PHASEAUTO M*4 Phase auto start [menu 1: 1=No,2=Yes]
  PLAN A*10 Plan
  POSTAUTO M*4 Post-mig auto start [menu 1: 1=No,2=Yes]
  STATUT M*15 Status [menu 7944: 1=Pending,2=In progress,3=Completed,4=Completed with errors,5=Interrupted,6=Pending interruption,7=Pending stop,8=Launched,9=Stopped,10=Blocked,11=Bypassed]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AI1]UPDUSR (AUTILIS) !Other

## AMOULIN2 (AI2) - Migration plan detail
Keys (first = PK; D = duplicates allowed): AI21 PLAN+CODE
Fields:
  AUUID AUUID Single identifier
  CODE A*12 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AI2]CREUSR (AUTILIS) !Other
  DATEL D Launch date
  DATEMAJ D Update date
  FICTRA A*200 Log file
  HEUL HM Launch time
  HEUMAJ HM Update time
  INDICEM L*6 Index
  MODULE M*20 Module [menu 14: 20 values, see local-menus.md]
  NBENREG L*8 No. of records
  NBENREGT L*8 No. processed
  NBREL C*4 Number of relaunches
  NUMREQ L*8 Query no.
  PHASE C*4 Phase
  PLAN A*10 Plan
  RANG C*4 Sequence
  RANGMOD M*20 Step [menu 7906: 1=Initialization,2=Common data,3=Module,4=Post-migration]
  STATUT M*4 Status [menu 7944: 1=Pending,2=In progress,3=Completed,4=Completed with errors,5=Interrupted,6=Pending interruption,7=Pending stop,8=Launched,9=Stopped,10=Blocked,11=Bypassed]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AI2]UPDUSR (AUTILIS) !Other

## AMSK (AMK) - Screen dictionary
Keys (first = PK; D = duplicates allowed): CODMSK CODMSK; ABRMSK ABRMSK (D)
Fields:
  ABRMSK ABR Screen abbreviation
  ACTBLOC ACV(15) Activity code -> [ACV]CODACT =[AMK]ACTBLOC (ACTIV) !Block
  AUUID AUUID Single identifier
  BASPAG AVA(15) Zone parameter
  BLOCACT1 A*60(15) Parameters
  BLOCAFFD M*15(15) Default display [menu 2936: 1=Table,2=Graph]
  BLOCGDEF M*15(15) Default graph [menu 2933: 1=Bars,2=Lines,3=Areas,4=Sectors]
  BLOCLIEN1 AUR(15) Link 1 -> [AUR]AUR0 =[AMK]BLOCLIEN1 (AURL) !Block
  BLOCLIEN2 AUR(15) Link 2 -> [AUR]AUR0 =[AMK]BLOCLIEN2 (AURL) !Block
  BLOCLIEN3 AUR(15) Link 3 -> [AUR]AUR0 =[AMK]BLOCLIEN3 (AURL) !Block
  BLOCPAR1 A*10(15)
  BLOCPAR2 A*10(15)
  BLOCPOSG M*15(15) Graphics position [menu 2931: 1=To the right,2=To the left,3=Above,4=Below]
  BLOCREPD M*15(15) Representation [menu 2939: 1=Multiple,2=Cumulation,3=Comparison,4=Month,5=Week,6=Day]
  BLOCTYPG M*15(15) Graph type [menu 2932: 1=Simple graph,2=Multiple graph,3=Planning calendar,4=XSL,5=Gantt,6=Query tool]
  BLOCTYPT M*15(15) Tupe of table [menu 2930: 1=Character,2=Character or graph,3=Character and graph,4=Graph]
  BLOCVIEW APV(15) Dashboard view -> [APV]APV0 =[AMK]BLOCVIEW (APTLVW) !Block act:APL
  CODACT ACV Activity code -> [ACV]CODACT =[AMK]CODACT (ACTIV) !Block
  CODMSK AMK Screen code -> [AMK]CODMSK =[AMK]CODMSK (AMSK) !Delete
  COLBLOC C*2(15) Columns
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AMK]CREUSR (AUTILIS) !Other
  DETBLC C*2(15) Grid block
  FICREF ATB(5) Reference tables -> [ATB]CODFIC =[AMK]FICREF (ATABLE) !RTZ
  HTBLOC C*2(15) Height
  INTBLOC A*60(15) Evaluated title
  INTMSK ATX Screen title
  LGBLOC C*2(15) Width
  LINBLOC C*2(15) Lines
  LNGLIB C*2(15) Text length
  MDL M*4 Templ. screen [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBBLOC C*4 Number of blocks
  NBFIC C*4 Number of tables
  NBLIGT L*5(15) Number of lines
  NBRCOL C*3 Number of columns
  NBRLIG C*3 Number of lines
  OPTION A*15(15) Grid options
  POSBLOC DCB*9.2(15) Position
  RANG C*4(15) Sequence
  STYBLOC ASY(15) Style title -> [ASY]ASY0 =[AMK]STYBLOC (ASTYLE) !Block
  TITBLOC ATX(15) Block title
  TRTSPE ADC Specific
  TRTSPV ADC Vertical
  TRTSTD ADC Standard
  TYPBLOC M*15(15) Block type [menu 38: 1=Table,2=List,3=Photo,4=Text,5=Hidden,6=Flash,7=Office,8=Browser,9=Html editor,10=Technique,11=Business Intelligence]
  TYPMSK M*10 Type [menu 929: 1=Tab,2=Dialogue box,3=Full screen,4=Full screen with list,5=Header,6=VT screen]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[AMK]UPDUSR (AUTILIS) !Other

## AMSKACT (AMA) - Action-object assignment table
Keys (first = PK; D = duplicates allowed): TYPAFF TYPAFF+CODAFF+CODZON+TYPACT+NOACT; NOACT CODAFF+CODZON+TYPACT+NOACT+TYPAFF
Fields:
  ACTION ACT Action code -> [ACT]ACTION =[AMA]ACTION (ACTION) !Block
  AUUID AUUID Single identifier
  CODAFF AMK Assignment code -> [AMK]CODMSK =[AMA]CODAFF (AMSK) !Other
  CODZON AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AMA]CREUSR (AUTILIS) !Other
  DISACT M*10 Deactivation [menu 2944: 1=None,2=Standard,3=Vertical,4=All]
  EXEACT M*15 Execution [menu 928: 1=Interactive,2=Import/batch,3=Always]
  INTITACT ATX Button title
  NOACT C*4 Order no.
  TYPACT M*15 Action type [menu 31: 31 values, see local-menus.md]
  TYPAFF C*3 Assignment type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMA]UPDUSR (AUTILIS) !Other

## AMSKPAR (AMP) - Action-object parameters
Keys (first = PK; D = duplicates allowed): CODPAR TYPAFF+CODAFF+CODZON+CODPAR; CODAFF CODAFF+CODZON (D)
Fields:
  AUUID AUUID Single identifier
  CODAFF AMK Assignment code -> [AMK]CODMSK =[AMP]CODAFF (AMSK) !Other
  CODPAR AAR Parameter code -> [AAR]CODPAR =[AMP]CODPAR (ACTCODPAR) !Block
  CODZON AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AMP]CREUSR (AUTILIS) !Other
  TYPAFF C*3 Assignment type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMP]UPDUSR (AUTILIS) !Other
  VALPAR A*80 Parameter value

## AMSKZON (AMZ) - Screen field dictionary
Keys (first = PK; D = duplicates allowed): CODE CODMSK+CODZON; CODZON CODMSK+NUMBLOC+NOZONE+CODZON; CODTYP CODTYP+CODMSK+CODZON; DICO CODZON+CODMSK
Fields:
  AUUID AUUID Single identifier
  CHGRAPH M*15 Graphic field type [menu 2937: 1=Value,2=Default,3=Description,4=None]
  CHPARG A*15 Setup
  CHREPR M*15 Representation [menu 2938: 1=Default,2=Bar,3=Line]
  CODACC ACS Access code -> [ACS]ACS0 =[AMZ]CODACC (ACCCOD) !Block
  CODACT ACV Activity code -> [ACV]CODACT =[AMZ]CODACT (ACTIV) !Block
  CODCTL ACL Control table -> [ACL]ACL0 =[AMZ]CODCTL (ACTL) !Block
  CODMSK AMK Screen code -> [AMK]CODMSK =[AMZ]CODMSK (AMSK) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[AMZ]CODTYP (ATYPE) !Block
  CODZON AVA Field code
  CONSAI A*80 Entry condition
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AMZ]CREUSR (AUTILIS) !Other
  DIME L*5 Dimension
  INTEVAL A*60 Evaluated title
  INTIT ATX Description
  INTSTYL ASY Style title -> [ASY]ASY0 =[AMZ]INTSTYL (ASTYLE) !Block
  LIEN M*5 Linked field [menu 49: 1=No,2=Long,3=Short]
  LONG DCB*5 Field length
  MODE M*15 Entry mode [menu 99: 1=Form and table,2=Form,3=Table]
  NOLIB MNL Local menu no.
  NOZONE DCB*2.1 Field number
  NUMBLOC C*3 Block code
  NUMLIG C*2 Line no.
  OBLIG M*4 Mandatory field [menu 1: 1=No,2=Yes]
  OPTFOR A*30 Format options
  OPTLNG C*3 Display length
  OPTOBJ A*20 Object options
  OPTSAI A*10 Entry options
  PDSZON C*4 Column
  SAIAFF M*15 Entry type [menu 936: 1=Enter,2=Display,3=Hidden,4=Technical]
  STYCND ASL Conditional style -> [ASL]ASL0 =STYCND;1 (ASTYLEC) !Block
  STYZON ASY Style -> [ASY]ASY0 =[AMZ]STYZON (ASTYLE) !Block
  TRANSM M*15 Transmission [menu 2942: 1=Not downloaded,2=All clients,3=Web services]
  TUNNEL M*6 Tunnel toward object [menu 1: 1=No,2=Yes]
  TYPGRAPH M*15 Graphic object type [menu 43: 1=None,2=Check box,3=Buttons (Vc),4=Buttons (Vs),5=Buttons (Hc),6=Buttons (Hs),7=Spin edit,8=Program bar,9=Photo,10=Multiline text,11=Relative rtf file,12=Absolute text file rtf,13=Icon]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AMZ]UPDUSR (AUTILIS) !Other
  VAL1 DCB*9.2 Value 1
  VAL2 DCB*9.2 Value 2
  VAL3 DCB*9.2 Value 3
  VALDEF A*80 Default value

## ANAVCRE (ANI) - Navigation
Keys (first = PK; D = duplicates allowed): ANI0 COD+LIG; ANI1 FNC+OBJ+LIG
Fields:
  AUUID AUUID Single identifier
  COD ANG Navigation code -> [ANG]ANG0 =[ANI]COD (ANAVIG) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ANI]CREUSR (AUTILIS) !Other
  FLD A*30 Field
  FNC AFC Starting function -> [AFC]CODINT =[ANI]FNC (AFONCTION) !Delete
  FRM AFR*250 Formula
  LIG C*3 Line number
  OBJ AOB Arrival object -> [AOB]ABREV =[ANI]OBJ (AOBJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ANI]UPDUSR (AUTILIS) !Other

## ANAVFIL (ANH) - Navigation
Keys (first = PK; D = duplicates allowed): ANH0 COD+LIG; ANH1 FNC+OBJ+LIG
Fields:
  AUUID AUUID Single identifier
  CND AFR*250 Condition
  COD ANG Navigation code -> [ANG]ANG0 =[ANH]COD (ANAVIG) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ANH]CREUSR (AUTILIS) !Other
  FIL AFR*250 Filter
  FNC AFC Starting function -> [AFC]CODINT =[ANH]FNC (AFONCTION) !Delete
  LIG C*3 Line number
  OBJ AOB Arrival object -> [AOB]ABREV =[ANH]OBJ (AOBJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ANH]UPDUSR (AUTILIS) !Other

## ANAVIG (ANG) - Navigation
Keys (first = PK; D = duplicates allowed): ANG0 COD; ANG1 FNC+OBJ
Fields:
  AUUID AUUID Single identifier
  COD ANG Navigation code -> [ANG]ANG0 =[ANG]COD (ANAVIG) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[ANG]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ANG]CREUSR (AUTILIS) !Other
  DES ATX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FNC AFC Starting function -> [AFC]CODINT =[ANG]FNC (AFONCTION) !Delete
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  OBJ AOB Arrival object -> [AOB]ABREV =[ANG]OBJ (AOBJET) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ANG]UPDUSR (AUTILIS) !Other

## ANNUAIRE (ANU) - User directory
Keys (first = PK; D = duplicates allowed): ANU0 COD
Fields:
  ADDFLD A*30(20) Directory field
  AUUID AUUID Single identifier
  COD ANU Code -> [ANU]ANU0 =[ANU]COD (ANNUAIRE) !Delete
  CODFLD AVA(20) X3 field
  CONNEC A*250 Connection
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ANU]CREUSR (AUTILIS) !Other
  DOMAIN A*50 Domain
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FORFLD A*250(2) Formula
  INTIT AX3 Description
  NBRFLD C*2 Field nb
  PARAM1 A*250 Parameter 1
  PARAM2 A*250 Parameter 2
  PASSE A*50 Password
  PORT L*8 Port number
  SERV1 AMC Main server
  SERV2 AMC Secondary server
  TYPFLD M*15(20) Field type [menu 7846: 1=Identifier,2=Identifier 2,3=Record,4=Parameter]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ANU]UPDUSR (AUTILIS) !Other

## AOBJBUR (AOA) - Office documents
Keys (first = PK; D = duplicates allowed): AOA0 ABREV+IDENT1+IDENT2+IDENT3
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOA]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  BLOB AB0*11 Image file
  CNTTYP ATYP Content type -> [ATYP]ATYP0 =CNTTYP (ATYPEPRO) !Block
  CPY CPY Company -> [CPY]CPY0 =[AOA]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOA]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  MODELE A*10 Template code
  TRN A*10 Transaction
  TYP AT Document type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOA]UPDUSR (AUTILIS) !Other

## AOBJBURMOD (AON) - Default documents
Keys (first = PK; D = duplicates allowed): AON0 ABREV+TRN+CPY+MODELE
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AON]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  BLOB AB0*11 Image file
  CPY CPY Company -> [CPY]CPY0 =[AON]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AON]CREUSR (AUTILIS) !Other
  INTIT AX3 Description
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MODELE A*10 Template code
  TRN A*10 Transaction
  TRNCPYMOD A*30 Key
  TYP AT Document type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AON]UPDUSR (AUTILIS) !Other

## AOBJET (AOB) - Basic objects
Keys (first = PK; D = duplicates allowed): ABREV ABREV; NOMFIC NOMFIC+ABREV
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOB]ABREV (AOBJET) !Delete
  ABRFIC ABR Table abbreviation
  ARCURL AFR*250 Archiving URL
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AOB]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AOB]CREUSR (AUTILIS) !Other
  IMPMSK AMK(16) Screen -> [AMK]CODMSK =[AOB]IMPMSK (AMSK) !Block
  IMPORT M*4 Import [menu 1: 1=No,2=Yes]
  IMPTAB AVA(16) Line field
  IMPTBL ATB(16) Table -> [ATB]CODFIC =[AOB]IMPTBL (ATABLE) !Block
  LIBEL ATX Object title
  LIBPAR ATX Parameter title
  LIBSHO ATX Short description
  MENU AFC Menu -> [AFC]CODINT =[AOB]MENU (AFONCTION) !RTZ
  MLOCK M*4 Lock in modification [menu 1: 1=No,2=Yes]
  MODELE AWM Data model -> [AWM]AWM0 =[AOB]MODELE (AWRKLNK) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBOPT C*2 No. of options
  NBRIMP C*2 Import
  NBSCR C*2 Number of screens
  NBVUE C*2 Number of views
  NOMFIC ATB Linked table -> [ATB]CODFIC =[AOB]NOMFIC (ATABLE) !Block
  OPTCND AFR*50(20) Option condition
  OPTCOD A*1(20) Option code
  OPTERR ATX(20) Error message
  OPTLIB ATX(20) Option title
  RANG C*4 Row in menu
  RPT1 ARX Report 1
  RPT2 ARX Report 2
  SCRABR ABR(8) Abbreviations
  SCRNAM AMK(8) Screens -> [AMK]CODMSK =[AOB]SCRNAM (AMSK) !Block
  SELCAR C*4 No. characters
  SELCLE A*10 Index
  SELOPT A*20 Selection options
  SELORD M*15 Sign [menu 90: 1=Ascending,2=Descending]
  SELTREE M*4 Hierarchical list [menu 1: 1=No,2=Yes]
  STA M*4 Statistics [menu 1: 1=No,2=Yes]
  TRTSPE ADC Specific
  TRTSPV ADC Vertical processing
  TYPGES M*15 Management type [menu 29: 1=Simple,2=Table,3=Combined,4=Browser]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[AOB]UPDUSR (AUTILIS) !Other
  VUEABR ABR(10) Abbreviation
  VUEACT ACV(10) Activity code -> [ACV]CODACT =[AOB]VUEACT (ACTIV) !Block
  VUECOD AVW(10) View code -> [AVW]AVW0 =[AOB]VUECOD (AVIEW) !Block
  ZACC AVA Access code field
  ZSITE AVA Site field

## AOBJEXT (AOE) - Import/export templates
Keys (first = PK; D = duplicates allowed): AOE0 EXT; AOE1 OBJ+EXT
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[AOE]ACS (ACCCOD) !Block
  AOWSTA M*4 Import/export temporary storage space [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CHRNUM L*8 Export sequence no.
  CODACT ACV Activity code -> [ACV]CODACT =[AOE]CODACT (ACTIV) !Block
  CODDBA M*10 File format [menu 945: 1=ascii,2=utf-8,3=ucs-2]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AOE]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENAWRK M*4 Workflow [menu 1: 1=No,2=Yes]
  EXPORT M*4 Export [menu 1: 1=No,2=Yes]
  EXT AOE Template -> [AOE]AOE0 =[AOE]EXT (AOBJEXT) !Delete
  FIL ATB(20) Tables -> [ATB]CODFIC =[AOE]FIL (ATABLE) !Block
  FILEXT FIC*250 Data file
  FLDLIM A*1 Field delimiter
  FLGEXP AFR*120(20) Criteria
  FLGFIL ATB(8) Table -> [ATB]CODFIC =[AOE]FLGFIL (ATABLE) !Block
  FLGKEY A*10(8) Key
  FLGLEV C*1(8) Level
  FLGLNK A*50(8) Link
  FLGREC AOI(8) Indicator
  FONCTION AFC Function -> [AFC]CODINT =[AOE]FONCTION (AFONCTION) !Block
  IMPORT M*4 Import [menu 1: 1=No,2=Yes]
  INTIT AX3 Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRFLG C*2 No.
  NBRLIG C*3 Number of lines
  OBJ AOB Object -> [AOB]ABREV =[AOE]OBJ (AOBJET) !Block
  OPTCHA M*15 Character set [menu 9: 1=ISO 8859,2=IBM PC,3=7 bits US,4=7 bits France,5=MacIntosh,6=HP Roman 8]
  OPTDAT C*1 Date format
  OPTMNL C*1 Local menu format
  OPTSPE M*4 Specific import [menu 1: 1=No,2=Yes]
  OPTUPD M*4 Modifcn. authorized [menu 1: 1=No,2=Yes]
  RECLEN C*4(8) Record length
  REPFIN FIC*250 Final directory
  SEPDEC A*1 Decimal separator
  SEPFLD A*8 Field separator
  SEPREC A*8 Record separator
  SPEIMP ADC Import processing
  TRTIMP ADC Import processing
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  TYPFIL M*15 File type [menu 94: 1=ASCII (1),2=ASCII (2),3=Delimited,4=Fixed length,5=XML,6=Flat,7=With header]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AOE]UPDUSR (AUTILIS) !Other

## AOBJEXTD (AOD) - Object import/export lines
Keys (first = PK; D = duplicates allowed): AOD0 EXT+NUMLIG
Fields:
  AUUID AUUID Single identifier
  BAL AOI Field tag
  COM A*30 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOD]CREUSR (AUTILIS) !Other
  ENDVAL A*30 Final value
  EXT AOE Template -> [AOE]AOE0 =[AOD]EXT (AOBJEXT) !Delete
  FIL ATB File -> [ATB]CODFIC =[AOD]FIL (ATABLE) !Delete
  FLD A*50 Field
  FMT A*10 Format
  INTFLD AXX Comment
  LNG C*3 Length
  LOC C*4 Position
  NUMLIG C*2 Line no.
  NUMTAB AOR Transcoding -> [AOR]AOR0 =NUMTAB;1 (AOBJEXTR) !RTZ
  OBL M*4 Mandatory [menu 1: 1=No,2=Yes]
  PATTERN A*30 Pattern
  SEL M*10 Range [menu 890: 1=No,2=Yes,3=Criteria not displayed]
  STRVAL A*30 First value
  TYP AOI Indicator
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOD]UPDUSR (AUTILIS) !Other

## AOBJEXTMP (AOW) - Import/export temporary storage space
Keys (first = PK; D = duplicates allowed): AOW0 NUMLOT; AOW1 EXT+NUMLOT (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AOW]CREUSR (AUTILIS) !Other
  EXT AOE Template -> [AOE]AOE0 =[AOW]EXT (AOBJEXT) !Delete
  FILEXT FIC*250 Data file
  NBRLIG C*3 Number of lines
  NUMLOT AOW Lot no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AOW]UPDUSR (AUTILIS) !Other

## AOBJEXTMPB (AOZ) - Import/export temporary storage space
Keys (first = PK; D = duplicates allowed): AOZ0 NUMLOT+NUMLIG; AOZ2 NUMLOT-NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOZ]CREUSR (AUTILIS) !Other
  FLDBLB AB0*9 Image file
  NUMLIG DCB*9 Line no.
  NUMLOT AOW Lot no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOZ]UPDUSR (AUTILIS) !Other

## AOBJEXTMPC (AOY) - Import/export temporary storage space
Keys (first = PK; D = duplicates allowed): AOY0 NUMLOT+NUMLIG; AOY2 NUMLOT-NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOY]CREUSR (AUTILIS) !Other
  FLDCLB AC0*9 Text file (clob)
  NUMLIG DCB*9 Line no.
  NUMLOT AOW Lot no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOY]UPDUSR (AUTILIS) !Other

## AOBJEXTMPD (AOV) - Import/export temporary storage space
Keys (first = PK; D = duplicates allowed): AOV0 NUMLOT+NUMLIG+FLDNUM; AOV1 NUMLOT+NUMLIG (D); AOV2 NUMLOT-NUMLIG+FLDNUM; AOV3 NUMLOT-NUMLIG+AOVFIL+AOVFLD+FLDNUM
Fields:
  AOVFIL A*10 Table
  AOVFLD A*50 Field
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOV]CREUSR (AUTILIS) !Other
  ENREG C*4 Recording
  FLDNUM C*4 Field number
  FLDVAL A*250 Value
  LEV C*4 Level
  LEVCOD AOI Indicator
  NUMLIG DCB*9 Line no.
  NUMLOT AOW Lot no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOV]UPDUSR (AUTILIS) !Other

## AOBJEXTMPE (AOU) - Import/export temporary storage space
Keys (first = PK; D = duplicates allowed): AOU0 NUMLOT+NUMLIG+FLDNUM; AOU2 NUMLOT-NUMLIG+FLDNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOU]CREUSR (AUTILIS) !Other
  ERR A*250 Error
  ERRSTA C*4 Status
  FLD A*50 Field
  FLDNUM C*4 Field number
  NUMLIG DCB*9 Line no.
  NUMLOT AOW Lot no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOU]UPDUSR (AUTILIS) !Other

## AOBJEXTR (AOR) - Transcribe import/export
Keys (first = PK; D = duplicates allowed): AOR0 NUMTAB+NUMLIG; AOR1 NUMTAB+CODEXT+NUMLIG; AOR2 NUMTAB+CODLOC+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CODEXT A*30 Code transcribed
  CODINTIT AX3 Transcoded title
  CODLOC A*30 Code to transcribe
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOR]CREUSR (AUTILIS) !Other
  INTIT AX3 Description
  NUMCAR A*4 Table number
  NUMLIG C*3 Line no.
  NUMTAB C*3 Table number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOR]UPDUSR (AUTILIS) !Other

## AOBJLNK (AOK) - Link explorer
Keys (first = PK; D = duplicates allowed): AOK0 SRCOBJ+LIN
Fields:
  ABRFIC ABR Table abbreviation
  AUUID AUUID Single identifier
  BASPAG A*30 Line field
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOK]CREUSR (AUTILIS) !Other
  DSTOBJ AOB Destination object -> [AOB]ABREV =[AOK]DSTOBJ (AOBJET) !Delete
  EXPLIEN A*50 Link expression
  LIN C*4 Line no.
  LNK ADI Link code -> [ADI]CODE =61;LNK (ATABDIV) !Delete
  SRCOBJ AOB Source object -> [AOB]ABREV =[AOK]SRCOBJ (AOBJET) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOK]UPDUSR (AUTILIS) !Other

## AOBJLST (AOL) - Basic objects
Keys (first = PK; D = duplicates allowed): AOL0 ABREV
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOL]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOL]CREUSR (AUTILIS) !Other
  DELDEF M*4 Deferred deletion [menu 1: 1=No,2=Yes]
  NBSEL C*2 No. of selection fields
  SELEXP AFR*200(16) Expression
  SELFIC ATB(16) Table -> [ATB]CODFIC =[AOL]SELFIC (ATABLE) !Block
  SELINT ATX(16) Description
  SELLNG DCB*5(16) Length
  SELSAI A*10(16) Entry options
  SELTYP ATY(16) Data type -> [ATY]CODTYP =[AOL]SELTYP (ATYPE) !Block
  SELZON AVA(16) Selection fields
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOL]UPDUSR (AUTILIS) !Other

## AOBJPROP (AOP) - Object properties
Keys (first = PK; D = duplicates allowed): AOP0 OBJ+NUM
Fields:
  AUUID AUUID Single identifier
  CLELNK AVA(5) Link key
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AOP]CREUSR (AUTILIS) !Other
  FRM AFR*250 Formula
  INTIT AX3 Description
  LNK A*80(5) Expression
  NBRTBL C*4 Number
  NUM C*4 Number
  OBJ AOB Object -> [AOB]ABREV =[AOP]OBJ (AOBJET) !Delete
  TBL ATB(5) Table -> [ATB]CODFIC =[AOP]TBL (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AOP]UPDUSR (AUTILIS) !Other

## AOBJSEL (AOS) - Select memo file
Keys (first = PK; D = duplicates allowed): AOS0 CODE+MEMO+ALL+USR; AOS1 CODE+NUMORD+ALL
Fields:
  ALL M*4 All [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CODE ATB Object code -> [ATB]CODFIC =[AOS]CODE (ATABLE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOS]CREUSR (AUTILIS) !Other
  DES AX3 Description
  MEMO AMM Memo code
  NUMORD L*8
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOS]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AOS]USR (AUTILIS) !Delete

## AOBJTAB (AOT) - Object table
Keys (first = PK; D = duplicates allowed): ABREV ABREV+NUMLIG; TABFIC ABREV+TABFIC+TABABR
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOT]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOT]CREUSR (AUTILIS) !Other
  NUMLIG C*2 Line no.
  TABABR ABR Table abbreviation
  TABACT ACV Activity code -> [ACV]CODACT =[AOT]TABACT (ACTIV) !Block
  TABCLE ANX Index
  TABFIC ATB Tables to open -> [ATB]CODFIC =[AOT]TABFIC (ATABLE) !Block
  TABLIEN A*200 Link expression
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOT]UPDUSR (AUTILIS) !Other

## AOBJTXT (AOX) - Attachments
Keys (first = PK; D = duplicates allowed): AOX0 ABREV+IDENT1+IDENT2+IDENT3
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOX]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  CAT M*15 Category [menu 96: 1=Confidential,2=Internal,3=External,4=External 2]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOX]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  IDTCNT A*20 Container act:ARCH
  IDTSTO A*50 Identifier act:ARCH
  MOTCLE A*10(5) Key word
  NAM A*250 Document name
  TYPDOC ADI Document type -> [ADI]CODE =902;TYPDOC (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOX]UPDUSR (AUTILIS) !Other
  VERSION A*10 Version act:ARCH

## AOBJTXTA (AOM) - Key word table
Keys (first = PK; D = duplicates allowed): AOM0 ABREV+IDENT1+IDENT2+IDENT3+MOTCLE; AOM1 MOTCLE+ABREV+IDENT1+IDENT2+IDENT3
Fields:
  ABREV AOB Object code -> [AOB]ABREV =[AOM]ABREV (AOBJET) !Delete
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AOM]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  IDENT3 A*10 Identifier 3
  MOTCLE A*10 Key word
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AOM]UPDUSR (AUTILIS) !Other

## APARIMPEXP (APX) - Import/export parameters
Keys (first = PK; D = duplicates allowed): APX0 COD
Fields:
  AUUID AUUID Single identifier
  COD A*10 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APX]CREUSR (AUTILIS) !Other
  DIRECTORY FIC*250 Directories
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APX]UPDUSR (AUTILIS) !Other

## APATCH (APT) - Patch tracking
Notes: differs in V9.0 P12 (diff: AT3_APATCH.htm)
Keys (first = PK; D = duplicates allowed): APT0 NUM; APT1 FIC (D); APT2 TYP+FICRELABR+NUMP (D)
Fields:
  AUUID AUUID Single identifier
  COMMENT A*50 Comments
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APT]CREUSR (AUTILIS) !Other
  DAT D Date
  FIC A*30 File
  FICRELABR A*10 Release abbreviation
  NUM L*8 Number
  NUMP L*8 No.
  PATNUM C*4 Patch
  RELEASE A*20 Version
  TYP A*1 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[APT]USR (AUTILIS) !RTZ

## APATCHLOG (APL) - Patch tracking
Keys (first = PK; D = duplicates allowed): APT0 AFOLDER+AUPDATE+IDENT
Fields:
  AFOLDER ADS Folder -> [ADS]DOSSIER =[APL]AFOLDER (ADOSSIER) !Delete
  AUPDATE A*15 Updates
  AUUID AUUID Single identifier
  CPTMAINT C*4 Sequence number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APL]CREUSR (AUTILIS) !Other
  DETAR_CLI M*4 Flag [menu 1: 1=No,2=Yes]
  DETAR_PER M*4 Flag [menu 1: 1=No,2=Yes]
  DETAR_STD M*4 Flag [menu 1: 1=No,2=Yes]
  DETAR_VER M*4 Flag [menu 1: 1=No,2=Yes]
  DETAR_WEB M*4 Flag [menu 1: 1=No,2=Yes]
  DETAR_X3C M*4 Flag [menu 1: 1=No,2=Yes]
  ERRMAINT A*30 Maintenance
  FLGMAINT M*10 Patch status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FLGPAT M*10 Patch list status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FLGTRT M*10 Process status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FLGVAL M*10 Validation status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  IDENT A*15 Identifier
  ISACSTMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISACTXMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISAGBMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISASWMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISASYMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISMENMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISNEWFUN M*4 Flag [menu 1: 1=No,2=Yes]
  ISTRTUSED M*4 Flag [menu 1: 1=No,2=Yes]
  ISTYPMOD M*4 Flag [menu 1: 1=No,2=Yes]
  ISVUE M*4 Flag [menu 1: 1=No,2=Yes]
  MAINTENANCE A*30 Number
  NBMAINT C*4 Total
  REQUESTID L*8 Query
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APL]UPDUSR (AUTILIS) !Other

## APATCHLOGD (APLD) - Patch tracking
Keys (first = PK; D = duplicates allowed): APLD0 AFOLDER+AUPDATE+IDENT+TYP+LINE
Fields:
  AFOLDER ADS Folder -> [ADS]DOSSIER =[APLD]AFOLDER (ADOSSIER) !Delete
  AUPDATE A*15 Updates
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APLD]CREUSR (AUTILIS) !Other
  IDENT A*15 Identifier
  LINE L*8 Line
  NUM L*8 Number
  TXT A*30 Text
  TYP AVB Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APLD]UPDUSR (AUTILIS) !Other

## APATCHMOD (APH) - Setup templates
Keys (first = PK; D = duplicates allowed): APH0 MODPAT+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[APH]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APH]CREUSR (AUTILIS) !Other
  EXPSEL AFR*210 Selection
  INTPAT AX3 Description
  MODDON AWM Data model -> [AWM]AWM0 =[APH]MODDON (AWRKLNK) !Block
  MODPAT APH Template code -> [APH]APH0 =MODPAT;NUMLIG (APATCHMOD) !Delete
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NUMLIG C*3 Line no.
  TRANSAC ATN Transaction -> [ATN]ATN0 =[APH]TRANSAC (ATRANSAC) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APH]UPDUSR (AUTILIS) !Other

## APATCHTMP (APATMP) - Patch integration
Keys (first = PK; D = duplicates allowed): APATMP0 NUMREQ+FICNAM+FOLD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APATMP]CREUSR (AUTILIS) !Other
  FICLOG FIC*30 Log file
  FICNAM FIC*50 File name
  FLGPAT M*10 Patch list status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FLGTRT M*10 Process status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FLGVAL M*10 Validation status [menu 7883: 1=Pending,2=In progress,3=Completed,4=Not installed,5=Error,6=Completed with errors]
  FOLD ADS Folder -> [ADS]DOSSIER =[APATMP]FOLD (ADOSSIER) !Delete
  NUMREQ L*8 Query no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APATMP]UPDUSR (AUTILIS) !Other
  VOLUME AVL Volume -> [AVL]CODE =[APATMP]VOLUME (AVOLUME) !Block

## APLCOM (ACM) - Sequence number definition
Keys (first = PK; D = duplicates allowed): COMCLE COMNOM+COMIND
Fields:
  AUUID AUUID Single identifier
  COMFLD A*50 Value
  COMIND C*2 Index
  COMLEN C*2 Length
  COMNOM A*12 Name
  COMTYP C*3 Type
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACM]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACM]UPDUSR (AUTILIS) !Other

## APLCOMH (ACMH) - Sequence number definition
Keys (first = PK; D = duplicates allowed): ACMH0 COMNOM
Fields:
  AUUID AUUID Single identifier
  COMLEN C*2 Length
  COMNOM A*12 Name
  COMTYP C*3 Type
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ACMH]CREUSR (AUTILIS) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ACMH]UPDUSR (AUTILIS) !Other

## APLLCK (ALK) - Lock table
Keys (first = PK; D = duplicates allowed): LCKCLE LCKSYM+LCKIND; PIDFLG LCKPID+LCKFLG (D)
Fields:
  LCKDAT D Date created
  LCKFLG M*4 Transaction flag [menu 1: 1=No,2=Yes]
  LCKIND C*4 Index
  LCKPID L*8 Process no.
  LCKSYM ASYM Symbol
  LCKTIM L*8 Time

## APLSTD (AST) - Local menus
Keys (first = PK; D = duplicates allowed): CLE LANCHP+LANNUM+LAN; LAN LAN+LANCHP+LANNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AST]CREUSR (AUTILIS) !Other
  LAN A*3 Language
  LANCHP MNL Chapter
  LANMES A*123 Message
  LANNUM C*5 Number
  LANORI LAN Original language -> [TLA]TLA0 =[AST]LANORI (TABLAN) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AST]UPDUSR (AUTILIS) !Other

## APOOLBRG (APB) - Pool of the java bridge
Keys (first = PK; D = duplicates allowed): APB1 POOLALIAS
Fields:
  AUTOSTART M*4 Auto start [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APB]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[APB]DOSSIER (ADOSSIER) !Other
  IMPCLI M*4 Optimization [menu 1: 1=No,2=Yes]
  INTITPOOL A*40 Description
  LIFETIME C*4 Maximum time (s)
  MAXENTRY C*3 Max number entries
  NBENTRY C*3 Number of entries
  NOPORT L*8 Port
  POOLALIAS A*20 Pool alias
  SERVEURAPP A*60 Application server
  SERVEURTRT A*60 Processing server
  SWEBALIAS A*40 Web server alias
  SYSTMDP A*40 System password
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APB]UPDUSR (AUTILIS) !Other
  USR A*5 User code
  USRLAN LAN Language -> [TLA]TLA0 =[APB]USRLAN (TABLAN) !Other
  USRMDP A*40 Password
  USRSYST A*40 System user

## APOOLWS (APW) - Web services pool
Keys (first = PK; D = duplicates allowed): APW1 CLE; APW2 SOLUTION+DOSSIER+SWEBALIAS+POOLALIAS
Fields:
  AUUID AUUID Single identifier
  CLE A*200 Key
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APW]CREUSR (AUTILIS) !Other
  DOSSIER ADS Folder -> [ADS]DOSSIER =[APW]DOSSIER (ADOSSIER) !Other
  INTITPOOL A*40 Description
  MAXENTRY C*3 Max number entries
  NBENTRY C*3 Number of entries
  POOLALIAS A*20 Pool alias
  PORTSSL L*6 HTTPS port
  PORTWEB L*6 Port
  PORTWEBEXT L*6 External port
  SADDEXT A*60 External address
  SERWEB A*60 Web server
  SOLUTION A*40 Solution
  SSLENABLED M*4 Active SSL [menu 1: 1=No,2=Yes]
  SWEBALIAS A*40 Web server alias
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APW]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[APW]USR (AUTILIS) !Other
  USRLAN LAN Language -> [TLA]TLA0 =[APW]USRLAN (TABLAN) !Other
  USRMDP A*10 Password

## APORTMOD (AMO) - Dashboard modules
Keys (first = PK; D = duplicates allowed): AMO0 CODUSR+CODTAB+CODMOD; AMO1 VIGNETTE+CODUSR (D)
Fields:
  AUUID AUUID Single identifier
  CODMOD A*10 Module
  CODTAB A*10 Tab
  CODUSR AUS User -> [AUS]CODUSR =[AMO]CODUSR (AUTILIS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AMO]CREUSR (AUTILIS) !Other
  EXPEND M*4 Unfolded [menu 1: 1=No,2=Yes]
  ICONE A*100 Icon
  INTPART ATX(10) Description
  MODTYP A*30 Technical module
  NAMPAR A*20(10) Parameter name
  SHBORDM A*5 Display borders
  SHHEADM A*5 Display header
  TEXTCL AC0*7 Text
  TITELT A*30 Title
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AMO]UPDUSR (AUTILIS) !Other
  VALPAR A*250(10) Parameter value
  VIGNETTE AVP Gadget -> [AVP]AVP0 =[AMO]VIGNETTE (APORTVIG) !Block

## APORTTAB (APA) - Dashboard gadgets
Keys (first = PK; D = duplicates allowed): APA0 CODUSR+CODTAB
Fields:
  AUUID AUUID Single identifier
  CODMOD A*10(50) Module
  CODTAB A*10 Tab
  CODUSR AUS User -> [AUS]CODUSR =[APA]CODUSR (AUTILIS) !Delete
  COLCOUNT C*4 Columns
  COLNUM C*4(50) Column no.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APA]CREUSR (AUTILIS) !Other
  FSHBORDT A*5 Force borders
  ICONE A*100 Icon
  LASTMOD C*4 Last row
  MAPT ACB Map
  NBMOD C*4 Number of elements
  SHSEPT A*5 Display separator
  TITELT A*80 Title
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APA]UPDUSR (AUTILIS) !Other

## APORTTYP (ATP) - Gadget group
Keys (first = PK; D = duplicates allowed): ATP0 CODFA
Fields:
  AUUID AUUID Single identifier
  CODFA A*5 Family code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATP]CREUSR (AUTILIS) !Other
  DESCR A*200 Description
  ICONE A*100 Icon
  INTITF ATX Description
  MODTYP A*30 Technical module
  NBPAR C*2 No. of parameters
  PROPDEF A*250(10) Default value
  PROPI ATX(10) Description
  PROPMOD M*4(10) Changeable [menu 1: 1=No,2=Yes]
  PROPN A*20(10) Name
  PROPT M*15(10) Type [menu 7838: 1=Character,2=Integer,3=Boolean,4=Numeric,5=Date,6=Text,7=Enumeration]
  TYPVIG M*15 Gadget type [menu 7836: 1=Gadget,2=Menu,3=Separator]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATP]UPDUSR (AUTILIS) !Other

## APORTUSER (APU) - User dashboard
Keys (first = PK; D = duplicates allowed): APU0 CODUSR
Fields:
  ACTIF A*10 Active
  AUUID AUUID Single identifier
  CODTAB A*10(30) Tab
  CODUSR AUS User -> [AUS]CODUSR =[APU]CODUSR (AUTILIS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APU]CREUSR (AUTILIS) !Other
  LASTNUM C*4 Last row
  MENUOPEN M*4 Unfolded menu [menu 1: 1=No,2=Yes]
  NBTAB C*4 Number of elements
  PIDUSE A*10 Owner
  REINIT A*5 Initialized by
  TITELT A*30 Title
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APU]UPDUSR (AUTILIS) !Other

## APORTVIG (AVP) - Gadgets
Keys (first = PK; D = duplicates allowed): AVP0 CODVI; AVP1 MENUR+RANGR+CODVI
Fields:
  AUUID AUUID Single identifier
  CODACC ACS Access code -> [ACS]ACS0 =[AVP]CODACC (ACCCOD) !Block
  CODACT ACV Activity code -> [ACV]CODACT =[AVP]CODACT (ACTIV) !Block
  CODFA ATP Family code -> [ATP]ATP0 =[AVP]CODFA (APORTTYP) !Block
  CODVI A*10 Gadget code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AVP]CREUSR (AUTILIS) !Other
  DESCR A*200 Description
  ICONE A*100 Icon
  INTIT1 AX3 Description
  MENUR AVP Connection menu -> [AVP]AVP0 =[AVP]MENUR (APORTVIG) !Block
  MODVAL M*4(10) Changeable [menu 1: 1=No,2=Yes]
  NBPAR C*2 No. of parameters
  PROPVAL A*250(10) Parameter value
  RANGR C*4 Sequence
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AVP]UPDUSR (AUTILIS) !Other

## APRINTDES (AID) - Printer description
Keys (first = PK; D = duplicates allowed): AID0 COD+NUM
Fields:
  AUUID AUUID Single identifier
  COD AIM Code -> [AIM]AIM0 =[AID]COD (APRINTER) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AID]CREUSR (AUTILIS) !Other
  NUM L*8 Number
  PRTDES A*250(2) Description
  PRTDESEX A*100 Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AID]UPDUSR (AUTILIS) !Other

## APRINTER (AIM) - Destinations
Keys (first = PK; D = duplicates allowed): AIM0 COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[AIM]ACS (ACCCOD) !Block
  ASSCPY M*4 Assembled copies [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  COD AIM Code -> [AIM]AIM0 =[AIM]COD (APRINTER) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AIM]CREUSR (AUTILIS) !Other
  DES DES Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  NBRCPY C*4 Number of copies
  PRT M*15 Destination [menu 95: 1=Preview,2=Printer,3=Message,4=File,5=Printer/file,6=ZPL printer,7=Archiving]
  PRTDRV A*80 Driver
  PRTFMT M*15 Export format [menu 91: 31 values, see local-menus.md]
  PRTNAM A*80 Printer
  PRTNAT M*15 Type [menu 22: 1=Normal,2=Fax,3=Thermal,4=Color]
  PRTORIENT C*2 Orientation
  PRTPOR A*100 Port
  PRTSRV A*80 Server
  PRTTYP M*15 Orientation [menu 98: 1=Portrait,2=Landscape]
  PRTZPL FIC*250 Destination file
  SHO SHO Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AIM]UPDUSR (AUTILIS) !Other

## APROCESSUS (APR) - Processes
Keys (first = PK; D = duplicates allowed): APR1 CODLEG+CODPRO; APR0 CODPRO (D); APR2 CODPRO+CODLEG
Fields:
  AUUID AUUID Single identifier
  CLOB AC0*9 Text file (clob)
  CODACC ACS Access code -> [ACS]ACS0 =[APR]CODACC (ACCCOD) !Block
  CODACT ACV Activity code -> [ACV]CODACT =[APR]CODACT (ACTIV) !Block
  CODLEG ADI Legislation -> [ADI]CODE =909;CODLEG (ATABDIV) !Block
  CODPRO A*10 Process code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APR]CREUSR (AUTILIS) !Other
  DESCR A*200 Description
  INTIT1 AX3 Description
  LANGDESC LAN Language -> [TLA]TLA0 =[APR]LANGDESC (TABLAN) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  TYPEP M*15 Type [menu 7855: 1=Process,2=Menu]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APR]UPDUSR (AUTILIS) !Other

## APROCTEXTE (AXP) - Process texts
Keys (first = PK; D = duplicates allowed): AXP0 CODPRO+CODLEG+LANG+UNIQIDP; AXP1 LANG+CODPRO+CODLEG+UNIQIDP
Fields:
  AUUID AUUID Single identifier
  CLBTEXT AC0*5 Text
  CODLEG ADI Legislation -> [ADI]CODE =909;CODLEG (ATABDIV) !Block
  CODPRO APR Process code -> [APR]APR1 =[AXP]CODPRO (APROCESSUS) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AXP]CREUSR (AUTILIS) !Other
  LANG LAN Language -> [TLA]TLA0 =[AXP]LANG (TABLAN) !Other
  UNIQIDP A*30 Key
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AXP]UPDUSR (AUTILIS) !Other

## APROFIL (APF) - User profile
Keys (first = PK; D = duplicates allowed): CODPRF MODULE+CODPRF; APF1 CODPRF+MODULE
Fields:
  AUUID AUUID Single identifier
  CODPRF APM Profile code -> [APF]CODPRF =0;CODPRF (APROFIL) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APF]CREUSR (AUTILIS) !Other
  INTPRF AX3 Profile description
  MEM L*8 Memory
  MENDEP A*5 Start menu
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  TYPPRF M*15 Profile type [menu 926: 1=Standard,2=Administrator,3=Developer]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APF]UPDUSR (AUTILIS) !Other

## APROMEN (APO) - Process menu
Keys (first = PK; D = duplicates allowed): APO1 LEG+CODMEN; APO0 CODMEN (D); APO2 CODMEN+LEG
Fields:
  AUUID AUUID Single identifier
  CODMEN A*10 Menu code
  COMMENT AXX
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[APO]CREUSR (AUTILIS) !Other
  DESCR A*200 Description
  INTIT DES Description
  INTLNG AX3 Long title
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NBPROC C*4 Number
  NIVEAU M*4(50) Level [menu 7859: 1=Level 1,2=Level 2,3=Level 3]
  PROCESSUS APR(50) Processes -> [APR]APR1 =PROCESSUS;"" (APROCESSUS) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[APO]UPDUSR (AUTILIS) !Other

## APRTAUS (AIA) - Destinations by user
Keys (first = PK; D = duplicates allowed): AIA0 USR+RPTCOD+CMP
Fields:
  AUUID AUUID Single identifier
  CMP A*10 Additional information
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AIA]CREUSR (AUTILIS) !Other
  OBL M*4 Mandatory [menu 1: 1=No,2=Yes]
  PRT AIM Destination -> [AIM]AIM0 =[AIA]PRT (APRINTER) !Delete
  RPTCOD ARP Report code -> [ARP]ARP0 =[AIA]RPTCOD (AREPORT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AIA]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AIA]USR (AUTILIS) !Delete

## APRTBRW (AP2) - Multilists
Notes: activity code APL
Keys (first = PK; D = duplicates allowed): AP20 AP2BRW
Fields:
  AP2BRW AP2 Supplier -> [AP2]AP20 =[AP2]AP2BRW (APRTBRW) !Delete
  AP2INTIT AX3 Description
  AP2NBOBJ C*4 Number
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AP2]CREUSR (AUTILIS) !Other
  NBREC C*4(10) Number of records
  OBJ AOB(10) Object -> [AOB]ABREV =[AP2]OBJ (AOBJET) !Block
  OBJSEL A*10(10) Selection
  ORDTRI M*10(10) [menu 90: 1=Ascending,2=Descending]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AP2]UPDUSR (AUTILIS) !Other

## APTLPAGE (APS) - Dashboard pages
Notes: activity code APL
Keys (first = PK; D = duplicates allowed): APS0 APSPAG
Fields:
  APSINTIT AX3 Description
  APSNBCAD C*4 Number of settings
  APSPAG APS Dashboard pages -> [APS]APS0 =[APS]APSPAG (APTLPAGE) !Delete
  APSPRE M*15 Present. settings [menu 2913: 1=1 framework,2=4 identical,3=2 vertical,4=2 horizontal,5=1+2 horizontal,6=2+1 horizontal,7=1+2 vertical,8=2+1 vertical]
  APSURL A*200(9) Internet address
  APSVW APV(9) Dashboard view -> [APV]APV0 =[APS]APSVW (APTLVW) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## APTLPAR (APP) - Dashboard view parameters
Notes: activity code APL
Keys (first = PK; D = duplicates allowed): APP0 APPTYP+APPCOD
Fields:
  APPCOD APP Code -> [APP]APP0 =APPTYP;APPCOD (APTLPAR) !Delete
  APPDES ATX Description
  APPTYP M*15 Type [menu 2912: 1=Data Source,2=Visual component]
  AUUID AUUID Single identifier
  CMPURL A*100(10) Relative address
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APP]CREUSR (AUTILIS) !Other
  PARCOD A*10(20) Parameter
  PARDEFVAL AFF*80(20) Default value
  PARDES ATX(20) Parameter title
  PARLNG DCB*9.2(20) Length
  PARNBR C*4 No. of parameters
  PARNOLIB C*4(20) Local menu
  PARTYP ATY(20) Data type -> [ATY]CODTYP =[APP]PARTYP (ATYPE) !Block
  SRCCODLNK APP(10) Data source -> [APP]APP0 =1;SRCCODLNK(indice) (APTLPAR) !Block
  SRCNBR C*4 No.
  SRCTYP ATY Source object -> [ATY]CODTYP =[APP]SRCTYP (ATYPE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APP]UPDUSR (AUTILIS) !Other

## APTLVW (APV) - Dashboard views
Notes: activity code APL
Keys (first = PK; D = duplicates allowed): APV0 APVCOD
Fields:
  APVCOD APV Code -> [APV]APV0 =[APV]APVCOD (APTLVW) !Delete
  APVINTIT AX3 Description
  AUUID AUUID Single identifier
  CMPCODTYP APP Visual component -> [APP]APP0 =2;CMPCODTYP (APTLPAR) !Block
  CMPPARCOD A*10(20) Parameter
  CMPPARFOR AFF*80(20) Formula
  CMPPARNBR C*4 No. of parameters
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[APV]CREUSR (AUTILIS) !Other
  SRCCOD A*10 Source code
  SRCCODTYP APP Data source -> [APP]APP0 =1;SRCCODTYP (APTLPAR) !Block
  SRCPARCOD A*10(20) Parameter
  SRCPARFOR AFF*80(20) Formula
  SRCPARNBR C*4 No. of parameters
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[APV]UPDUSR (AUTILIS) !Other

## ARCHPAR (ARC) - Archiving rules
Keys (first = PK; D = duplicates allowed): ARC0 CODARC
Fields:
  AUUID AUUID Single identifier
  CAT AFR*50 Category
  CODACT ACV Activity code -> [ACV]CODACT =[ARC]CODACT (ACTIV) !Block
  CODARC ARC Archiving code -> [ARC]ARC0 =[ARC]CODARC (ARCHPAR) !BSRA
  CPY CPY Company -> [CPY]CPY0 =[ARC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ARC]CREUSR (AUTILIS) !Other
  DEBUG M*20 Debug mode [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPEVT AOE Template -> [AOE]AOE0 =[ARC]EXPEVT (AOBJEXT) !Block
  FCTEVT AFC Function -> [AFC]CODINT =[ARC]FCTEVT (AFONCTION) !Block
  FILTRE AFR*250 Criteria
  FLDCPY AFR*20 Company field
  FLDFCY AFR*20 Site field
  FORFIC AFR*250 File name
  IDTCNT AFR*250 Container
  IDTSTO AFR*250 Identifier
  IDTVOL ADI Volume identifier -> [ADI]CODE =81;IDTVOL (ATABDIV) !Block
  INTERV M*20 Parameter display [menu 1: 1=No,2=Yes]
  INTIT AX3 Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MOTCLE AFR*50(5) Key word
  NAM AFR*250 Document name
  OBJCLE A*250 Link key
  OBJEVT AOB Object code -> [AOB]ABREV =[ARC]OBJEVT (AOBJET) !Block
  OBJLNK AOB Object to link -> [AOB]ABREV =[ARC]OBJLNK (AOBJET) !Block
  RPTEVT ARP Report code -> [ARP]ARP0 =[ARC]RPTEVT (AREPORT) !Block
  TYPDOC ADI Document type -> [ADI]CODE =902;TYPDOC (ATABDIV) !Block
  TYPEVT M*20 Event type [menu 7870: 1=Object,2=Report,3=Export,4=Log,5=Excel,6=Manual]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ARC]UPDUSR (AUTILIS) !Other
  VERSION AFR*250 Version

## ARCHPARE (ARE) - Archiving parameters
Keys (first = PK; D = duplicates allowed): ARE0 TYPDOC+IDTVOL+NUMLIG
Fields:
  ADRPAR M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AUUID AUUID Single identifier
  CODPAR A*50 Parameter code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARE]CREUSR (AUTILIS) !Other
  IDTVOL ADI Volume identifier -> [ADI]CODE =81;IDTVOL (ATABDIV) !Block
  INTPAR AX3 Parameter title
  NUMLIG C*3 Line no.
  TYPDOC ADI Document type -> [ADI]CODE =902;TYPDOC (ATABDIV) !Block
  TYPPAR MM*15 Internal type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARE]UPDUSR (AUTILIS) !Other

## ARCHPARU (ARU) - EDM user profile
Keys (first = PK; D = duplicates allowed): ARU0 ARCPRF
Fields:
  ARCLOG A*25 Login
  ARCNAM DES Description
  ARCPAS A*20 Password
  ARCPRF ARU Profile code -> [ARU]ARU0 =[ARU]ARCPRF (ARCHPARU) !Delete
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARU]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARU]UPDUSR (AUTILIS) !Other

## ARCHPARW (ARW) - Archiving parameters
Keys (first = PK; D = duplicates allowed): ARW0 CODARC+CODPAR
Fields:
  AUUID AUUID Single identifier
  CODARC ARC Archiving code -> [ARC]ARC0 =[ARW]CODARC (ARCHPAR) !Block
  CODPAR A*50 Parameter code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARW]CREUSR (AUTILIS) !Other
  FORPAR AFR*250 Value
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARW]UPDUSR (AUTILIS) !Other

## AREFAML (ARN) - Text cross references
Keys (first = PK; D = duplicates allowed): ARN0 NOLIB+NUM
Fields:
  AUUID AUUID Single identifier
  CLES A*50 Key
  CODMSK AMK Screen code -> [AMK]CODMSK =[ARN]CODMSK (AMSK) !Other
  CODZON AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARN]CREUSR (AUTILIS) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NOLIB MNL Local menu no.
  NUM L*8 Sequence no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARN]UPDUSR (AUTILIS) !Other

## AREFTXT (ART) - Text cross references
Keys (first = PK; D = duplicates allowed): ART0 TXTNUM+NUM; ART1 TXTNUM+CODFIC+CODZONE+CLES; ART2 CODFIC+CODZONE+CLES+TXTNUM
Fields:
  AUUID AUUID Single identifier
  CLES A*50 Key
  CODFIC ATB Table code -> [ATB]CODFIC =[ART]CODFIC (ATABLE) !Other
  CODZONE A*10 Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ART]CREUSR (AUTILIS) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NUM L*8 Sequence no.
  TXTNUM L*8 Text number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ART]UPDUSR (AUTILIS) !Other

## AREPORT (ARP) - Report dictionary
Keys (first = PK; D = duplicates allowed): ARP0 RPTCOD; ARP1 GRP+RPTCOD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ARP]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  AUZFCY M*4 Authorization site [menu 1: 1=No,2=Yes]
  CODACT ACV Activity code -> [ACV]CODACT =[ARP]CODACT (ACTIV) !Block
  CODZPL ARZ ZPL setup -> [ARZ]ARZ0 =[ARP]CODZPL (AREPORTZ) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ARP]CREUSR (AUTILIS) !Other
  CRYCOD ACR(5) Crystal reports
  DEVAPP ADS(5) Folder -> [ADS]DOSSIER =[ARP]DEVAPP (ADOSSIER) !RTZ
  DEVDAT D(5) Date
  DEVLAN LAN(5) Language -> [TLA]TLA0 =[ARP]DEVLAN (TABLAN) !RTZ
  DEVSRV AMC(5) Print server
  DEVSTA M*15(5) Status [menu 7945: 1=Shared,2=Transfer request,3=Sandbox,4=Commit request,5=Revert request,6=CR Designer loading]
  DEVUSR AUS(5) User -> [AUS]CODUSR =[ARP]DEVUSR (AUTILIS) !RTZ
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXEBAT M*4 Execute in batch [menu 1: 1=No,2=Yes]
  EXEFLG M*4 Not executable [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FNC AFC Function -> [AFC]CODINT =[ARP]FNC (AFONCTION) !Block
  FORETA M*40(5) Paper size [menu 7943: 48 values, see local-menus.md]
  GESZPL M*4 ZPL printer [menu 1: 1=No,2=Yes]
  GRP M*15 Group [menu 97: 78 values, see local-menus.md]
  HOR ABH Hourly constraints -> [ABH]ABH0 =[ARP]HOR (ABATHOR) !Block
  IMPLIE M*4 Linked prints [menu 1: 1=No,2=Yes]
  LAN LAN Language -> [TLA]TLA0 =[ARP]LAN (TABLAN) !Block
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MULLAN M*4 Multi-language [menu 1: 1=No,2=Yes]
  ORIENT M*15(5) Orientation [menu 98: 1=Portrait,2=Landscape]
  PARSEG A*15 Segmentation
  PRTDEF AIM Printer -> [AIM]AIM0 =[ARP]PRTDEF (APRINTER) !Block
  PRTDES A*250(2) Description
  PRTDRV A*30 Driver
  PRTFRM AFR*250 Add info formula
  PRTNAM A*50 Destination
  PRTNAT M*15 Type [menu 22: 1=Normal,2=Fax,3=Thermal,4=Color]
  PRTOBL M*4 Mandatory [menu 1: 1=No,2=Yes]
  PRTPOR A*30 Port
  PRTSRV A*30 Server
  RPTCOD ARP Report code -> [ARP]ARP0 =[ARP]RPTCOD (AREPORT) !Delete
  RPTDES ATX Description
  RPTSHO ATX Short description
  TRTINI ADC Standard processing
  TRTSPE ADC Specific processing
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ARP]UPDUSR (AUTILIS) !Other

## AREPORTA (ARA) - Printer setup
Keys (first = PK; D = duplicates allowed): ARA0 PATNAM-TIMSTP+TYP+SEQ; ARA1 PATNAM-VER (D); ARA2 PATNAM+VER+TYP+SEQ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ARA]CREUSR (AUTILIS) !Other
  LIG A*250 Lines
  PATNAM ARA Template file
  SEQ C*4 Sequence
  TIMSTP DCB*10 Date time
  TYP M*15 Record type [menu 7868: 1=Header,2=Line,3=Footer]
  TYPPAT M*15 Pattern type [menu 7869: 1=Structures,2=Mask]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARA]UPDUSR (AUTILIS) !Other
  VER C*3 Version

## AREPORTD (ARD) - Report parameters
Keys (first = PK; D = duplicates allowed): ARD0 RPTCOD+PARNUM; ARD1 PARCOD+RPTCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARD]CREUSR (AUTILIS) !Other
  PARACS ACS Access code -> [ACS]ACS0 =[ARD]PARACS (ACCCOD) !Block
  PARCOD A*15 Description
  PARCTL AFR*80 Control
  PARCTLTAB ACL Control table -> [ACL]ACL0 =[ARD]PARCTLTAB (ACTL) !Block
  PARDEF1 AFR*80 Default value
  PARDEF2 AFR*80 Default value
  PARLNG DCB*9.2 Length
  PARNAM ATX Parameter title
  PARNOLIB C*5 Local menu
  PARNUM C*3 Parameter no.
  PAROPT A*20 Options
  PARPAR AFR*80 Parameter
  PARSAI M*4 Input [menu 1: 1=No,2=Yes]
  PARSTREND M*15 Value type [menu 7800: 1=Single,2=Range,3=Multiple]
  PARTYP ATY Data type -> [ATY]CODTYP =[ARD]PARTYP (ATYPE) !Block
  RPTCOD ARP Report code -> [ARP]ARP0 =[ARD]RPTCOD (AREPORT) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARD]UPDUSR (AUTILIS) !Other

## AREPORTG (ARG) - Printer setup
Keys (first = PK; D = duplicates allowed): ARG0 CODPAR+NUM+LIG
Fields:
  AUUID AUUID Single identifier
  CND AFR*250 Condition
  CODPAR ARZ Setup code -> [ARZ]ARZ0 =[ARG]CODPAR (AREPORTZ) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARG]CREUSR (AUTILIS) !Other
  EXPLIG AFR*250 Expression
  LIG C*3 Line number
  NUM C*4 Number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARG]UPDUSR (AUTILIS) !Other

## AREPORTM (ARM) - Temporary print key table
Keys (first = PK; D = duplicates allowed): ARM0 NUMREQ+USR+RPTCOD+NUMLIG; ARM1 USR+RPTCOD (D); ARM2 NUMREQ+USR+SEQREQ+RPTCOD+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CLEA1 A*40 Alpha 1
  CLEA10 A*40 Alpha 10
  CLEA11 A*40 Alpha 11
  CLEA2 A*40 Alpha 2
  CLEA3 A*40 Alpha 3
  CLEA4 A*40 Alpha 4
  CLEA5 A*40 Alpha 5
  CLEA6 A*40 Alpha 6
  CLEA7 A*40 Alpha 7
  CLEA8 A*40 Alpha 8
  CLEA9 A*40 Alpha 9
  CLED1 D Date 1
  CLED2 D Date 2
  CLEMD1 DCB*13.2 Decimal 1
  CLEMD2 DCB*13.2 Decimal
  CLEMD3 DCB*13.2 Decimal
  CLEMD4 DCB*13.2 Decimal
  CLEN1 L*8 Numeric 1
  CLEN2 L*8 Numeric 2
  CLEN3 L*8 Numeric 3
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARM]CREUSR (AUTILIS) !Other
  NUMCOP L*8 Copy
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  RPTCOD ARP Report code -> [ARP]ARP0 =[ARM]RPTCOD (AREPORT) !Other
  SEQREQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARM]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[ARM]USR (AUTILIS) !Other

## AREPORTS (ARO) - Reports - data sources
Keys (first = PK; D = duplicates allowed): ARO0 RPTCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARO]CREUSR (AUTILIS) !Other
  DOSSIER AFR*80(5) Default folder
  NBRSRC C*4 No. of sources
  NBRTBL C*2 Number of tables
  NUM C*2(50) Number
  RPTCOD ARP Report code -> [ARP]ARP0 =[ARO]RPTCOD (AREPORT) !Delete
  SRC ATX(5) Data source
  TBL AC*15(50) Table
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARO]UPDUSR (AUTILIS) !Other

## AREPORTV (ARV) - Reports
Keys (first = PK; D = duplicates allowed): ARV0 FONCTION+TYPCOD+ETAT+PARAM; ARV1 TYPCOD+ETAT+PARAM+FONCTION
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARV]CREUSR (AUTILIS) !Other
  ETAT A*15 Report
  FONCTION AFC Function -> [AFC]CODINT =[ARV]FONCTION (AFONCTION) !Delete
  PARAM A*30 Parameter
  TYPCOD M*20 Print type [menu 7818: 1=Reports,2=Queries,3=SQL queries,4=Exports,5=Business objects]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARV]UPDUSR (AUTILIS) !Other
  VALDEF1 AFR*250 Default value
  VALDEF2 AFR*250 Default value

## AREPORTX (ARX) - Reports
Keys (first = PK; D = duplicates allowed): ARX0 INTCOD+TYPCOD+EXTCOD+LAN (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARX]CREUSR (AUTILIS) !Other
  EXTCOD A*20 Print code
  IMPNOW M*4 Direct print [menu 1: 1=No,2=Yes]
  INTCOD ARX Internal code
  LAN LAN Language -> [TLA]TLA0 =[ARX]LAN (TABLAN) !Block
  TYPCOD M*20 Print type [menu 7818: 1=Reports,2=Queries,3=SQL queries,4=Exports,5=Business objects]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARX]UPDUSR (AUTILIS) !Other

## AREPORTZ (ARZ) - ZPL reports
Keys (first = PK; D = duplicates allowed): ARZ0 CODPAR
Fields:
  AUUID AUUID Single identifier
  CODPAR ARZ Setup code -> [ARZ]ARZ0 =[ARZ]CODPAR (AREPORTZ) !Delete
  CONDIT AFR*250(5) Criteria
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ARZ]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENVMSK M*4 Mask issue [menu 1: 1=No,2=Yes]
  INTIT AX3 Description
  MODDON AWM Data model -> [AWM]AWM0 =[ARZ]MODDON (AWRKLNK) !Block
  PATNAM A*30 Template file
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ARZ]UPDUSR (AUTILIS) !Other
  VER C*3 Version

## AROLE (ARL) - Row level permissions
Keys (first = PK; D = duplicates allowed): ARL0 OBJ+ROL; ARL1 ROL+OBJ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ARL]CREUSR (AUTILIS) !Other
  FLD A*15 Field
  OBJ AOB Object -> [AOB]ABREV =[ARL]OBJ (AOBJET) !Block
  ROL ADI Permission code -> [ADI]CODE =60;ROL (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ARL]UPDUSR (AUTILIS) !Other

## ASHW (ASW) - Representations
Keys (first = PK; D = duplicates allowed): ASW0 CODREP
Fields:
  ABRCLA ABR Instance
  ACTLNKFAC ACV(10) Activity code -> [ACV]CODACT =[ASW]ACTLNKFAC (ACTIV) !Block
  ACTTRT ACV(20) Activity code -> [ACV]CODACT =[ASW]ACTTRT (ACTIV) !Block
  AFCRIGHT AFC Authorization -> [AFC]CODINT =[ASW]AFCRIGHT (AFONCTION) !Block
  AFFLNKFAC M*20(10) Anchor type [menu 7965: 1=Property,2=Collection line,3=Collection,4=Page,5=Record]
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ASW]CODACT (ACTIV) !Block
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ASW]CODCLA (ACLASSE) !Block
  CODCOM M*15(20) Code [menu 7968: 1=Creation,2=Update,3=Deletion,4=PDF printing,5=Excel reporting,6=Word reporting,7=Word mail merge,8=Quick edit]
  CODFAC M*15(10) Facet code [menu 7964: 1=Detail,2=Edit,3=Query,4=Lookup,5=Summary]
  CODIND ANX Index
  CODREP ASW Representation code -> [ASW]ASW0 =[ASW]CODREP (ASHW) !Delete
  CODTRT ADC(20) Processing
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASW]CREUSR (AUTILIS) !Other
  DEFLNKFAC M*4(10) Default [menu 1: 1=No,2=Yes]
  DEFREP M*4 Search rep [menu 1: 1=No,2=Yes]
  DESCRIPT A*120 Index descriptor
  ENACOM M*4(20) Active [menu 1: 1=No,2=Yes]
  ENAFAC M*4(10) Active [menu 1: 1=No,2=Yes]
  FLGSYSTEM M*4 System [menu 1: 1=No,2=Yes]
  FONCTION AFC Function -> [AFC]CODINT =[ASW]FONCTION (AFONCTION) !Block
  INTREP ATX Description
  LNKMENFAC AVB(10) Link/Menu
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRCOM C*4 Behaviors
  NBRFAC C*4 Facets
  NBRTRT C*2 No. processes
  RANTRT C*4(20) Order
  TYPMSKREP M*15 Screen type [menu 7963: 1=Desktop,2=Mobile phone,3=Tablet]
  TYPREP M*15 Type [menu 7967: 1=Main,2=Child]
  TYPTRT M(20) Type [menu 7844: 1=Standard,2=Vertical,3=Specific]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASW]UPDUSR (AUTILIS) !Other

## ASHWBLC (ASWB) - Representation (Blocks)
Keys (first = PK; D = duplicates allowed): ASWB0 CODREP+CODBLC; ASWB1 CODREP+NIVBLC+CODBLC
Fields:
  ACTBLC ACV Activity code -> [ACV]CODACT =[ASWB]ACTBLC (ACTIV) !Block
  AUUID AUUID Single identifier
  CODBLC A*10 Block code
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWB]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWB]CREUSR (AUTILIS) !Other
  INTBLC ATX Description
  NIVBLC C*4 Order
  SECBLC A*10 Section
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWB]UPDUSR (AUTILIS) !Other

## ASHWCOL (ASWC) - Representations (Collections)
Keys (first = PK; D = duplicates allowed): ASWC0 CODREP+CODCOL
Fields:
  ACTCOL ACV Activity code -> [ACV]CODACT =[ASWC]ACTCOL (ACTIV) !Block
  ALIASCOL AVB Alias
  AUUID AUUID Single identifier
  CODCOL AVC Group code
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWC]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWC]CREUSR (AUTILIS) !Other
  FLGAPDCOL M*4 Addition [menu 1: 1=No,2=Yes]
  FLGINSCOL M*4 Insertion [menu 1: 1=No,2=Yes]
  FLGSUPCOL M*4 Deletion [menu 1: 1=No,2=Yes]
  FLGTRICOL M*4 Sort [menu 1: 1=No,2=Yes]
  INTCOL ATX Collection description
  MAXCOL C*4 Maxi
  MINCOL M*15 Mini [menu 7966: 1=0,2=1,3=Maximum]
  PROCOL AVA Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWC]UPDUSR (AUTILIS) !Other

## ASHWEXPPRO (ASWR) - Representations (displayed)
Keys (first = PK; D = duplicates allowed): ASWR0 CODREP+ALIAS; ASWR1 CODREP+NUMPRO+CODPRO (D); ASWR2 CODREP+ORDPRO+NUMPRO+CODPRO (D); ASWR3 CODREP+CODPRO (D)
Fields:
  ACTPRO ACV Activity code -> [ACV]CODACT =[ASWR]ACTPRO (ACTIV) !Block
  ALIAS AVB Alias
  AUUID AUUID Single identifier
  BLCPRO A*10 Block
  CODPRO AVC Property
  CODREP ASW Code -> [ASW]ASW0 =[ASWR]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWR]CREUSR (AUTILIS) !Other
  DETPRO M*4 Detail [menu 1: 1=No,2=Yes]
  EDIPRO M*4 Edit [menu 1: 1=No,2=Yes]
  INTEVALPRO A*60 Evaluated description
  INTPRO ATX Description
  INTSHTPRO ATX Short description
  LOKPRO M*4 Lookup [menu 1: 1=No,2=Yes]
  NUMPRO C*4 Number
  ORDPRO C*4 Order
  PARENTPRO M*4 Entry P [menu 1: 1=No,2=Yes]
  PARFILPRO M*4 Filter P [menu 1: 1=No,2=Yes]
  QRYPRO M*4 Query [menu 1: 1=No,2=Yes]
  STADETPRO M*15 Detail status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  STAEDIPRO M*15 Edit status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  STAINIPRO M*15 Initial status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  STALOKPRO M*15 Lookup status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  STAQRYPRO M*15 Query status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  STASUMPRO M*15 Summary status [menu 7970: 1=Visible,2=Invisible,3=Technical]
  SUMPRO M*4 Summary [menu 1: 1=No,2=Yes]
  TAGPRO A*250 Tag
  TYPAFFPRO M*4 Editable [menu 1: 1=No,2=Yes]
  UOMPRO AVC Unit
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWR]UPDUSR (AUTILIS) !Other

## ASHWFLD (ASWF) - Representations (Lines)
Keys (first = PK; D = duplicates allowed): ASWF0 CODREP+CODFLD; ASWF1 CODREP+NUMFLD+CODFLD; ASWF2 CODREP+NUMFLD+NUMLIG+CODFLD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ASWF]ACS (ACCCOD) !Block
  ACTFLD ACV Activity code -> [ACV]CODACT =[ASWF]ACTFLD (ACTIV) !Block
  AUUID AUUID Single identifier
  CODCTL ACL Control table -> [ACL]ACL0 =[ASWF]CODCTL (ACTL) !Block
  CODFLD AVA Field
  CODREP ASW Code -> [ASW]ASW0 =[ASWF]CODREP (ASHW) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[ASWF]CODTYP (ATYPE) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWF]CREUSR (AUTILIS) !Other
  FLDGRP AVC Group
  FLGACCGET M*4 GET accessor [menu 1: 1=No,2=Yes]
  INTEVAL A*60 Evaluated title
  INTFLD ATX Description
  INTSHTFLD ATX Short description
  LOBCNT AVA Content type
  LOBFLD AVA Lob field
  LOBTAB ATB Lob table -> [ATB]CODFIC =[ASWF]LOBTAB (ATABLE) !Block
  LONG DCB*4 Length
  NOLIB MNL Local menu no.
  NUMFLD DCB*3.2 Order
  NUMLIG C*3 Line no.
  OBLIG M*4 Mandatory field [menu 1: 1=No,2=Yes]
  TABCONT A*250 Dependency
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWF]UPDUSR (AUTILIS) !Other

## ASHWLNK (ASWK) - Representations (Anchors)
Keys (first = PK; D = duplicates allowed): ASWK0 CODREP+AFFLNK+ANCLNK+CODLNK; ASWK1 CODREP+ANCLNK+ORDTECLNK+AFFLNK+MENLNK+CODLNK (D)
Fields:
  ACVLNK ACV Activity code -> [ACV]CODACT =[ASWK]ACVLNK (ACTIV) !Block
  AFFLNK M*15 Assignment [menu 7965: 1=Property,2=Collection line,3=Collection,4=Page,5=Record]
  ANCLNK AVC Anchor
  ATTLNK M*4 Attribute [menu 7973: 1=Simple link,2=Detail,3=Lookup,4=Summary]
  AUUID AUUID Single identifier
  CLALNK ACLA Class code -> [ACLA]ACLA0 =[ASWK]CLALNK (ACLASSE) !Other
  CLAPTRLNK AVC Instance path
  CMPLNK M*25 Behavior [menu 7971: 22 values, see local-menus.md]
  CODFNCLNK AFC Function -> [AFC]CODINT =[ASWK]CODFNCLNK (AFONCTION) !Block
  CODLNK AVA Code
  CODMETLNK ASM Method code
  CODOPELNK ASM Operation code
  CODREP ASW Code -> [ASW]ASW0 =[ASWK]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWK]CREUSR (AUTILIS) !Other
  DETLNK M*4 Detail [menu 1: 1=No,2=Yes]
  EDILNK M*4 Edit [menu 1: 1=No,2=Yes]
  ENALNK M*4 Active [menu 1: 1=No,2=Yes]
  FLGASYLNK M*4 Asynchronous [menu 1: 1=No,2=Yes]
  FLGSTDLNK M*4 Std [menu 1: 1=No,2=Yes]
  FREELNK A*250 URL
  INTLNK ATX Description
  INVLNK M*4 Invalid [menu 1: 1=No,2=Yes]
  LOKLNK M*4 Lookup [menu 1: 1=No,2=Yes]
  MENLNK A*30 Menu
  NUMLNK C*4 Line number
  ORDLNK C*4 Order
  ORDTECLNK C*5 Order
  QRYLNK M*4 Query [menu 1: 1=No,2=Yes]
  REMSTDLNK AVA Replacement
  REPLNK ASW Representation -> [ASW]ASW0 =[ASWK]REPLNK (ASHW) !Other
  RPTCOD ARP Report code -> [ARP]ARP0 =[ASWK]RPTCOD (AREPORT) !Block
  SUMLNK M*4 Summary [menu 1: 1=No,2=Yes]
  TARLNK M*20 Target [menu 7975: 1=Default,2=New page,3=Embedded]
  TYPLNK M*20 Link type [menu 7974: 1=Representation,2=Method,3=Operation,4=X3 Convergence,5=Free,6=Crystal report]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWK]UPDUSR (AUTILIS) !Other

## ASHWMENU (ASWMN) - Representations (Menus)
Keys (first = PK; D = duplicates allowed): ASWMN0 CODREP+CODMENU; ASWMN1 CODREP+PARMENU+ORDMENU+CODMENU
Fields:
  ACTMENU ACV Activity code -> [ACV]CODACT =[ASWMN]ACTMENU (ACTIV) !Block
  AUUID AUUID Single identifier
  CODMENU AVA Code
  CODREP ASW Code -> [ASW]ASW0 =[ASWMN]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWMN]CREUSR (AUTILIS) !Other
  LIBMENU ATX Description
  ORDMENU C*4 Order
  PARMENU AVA Parent
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWMN]UPDUSR (AUTILIS) !Other

## ASHWMET (ASWM) - Representation (methods)
Keys (first = PK; D = duplicates allowed): ASWM0 CODREP+CODMET; ASWM1 CODREP+NOMET+CODMET
Fields:
  ACTMET ACV Activity code -> [ACV]CODACT =[ASWM]ACTMET (ACTIV) !Block
  AUUID AUUID Single identifier
  CODMET ASM Method code
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWM]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWM]CREUSR (AUTILIS) !Other
  DONMET M*15 Return type [menu 7843: 1=Date,2=Char,3=Integer,4=Decimal,5=Text file,6=Image file]
  FLDMET AVA Return variable
  INTMET ATX Description
  NOMET C*4 Method no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWM]UPDUSR (AUTILIS) !Other

## ASHWOPT (ASWO) - Representations (Options)
Keys (first = PK; D = duplicates allowed): ASWO0 CODREP+OPTCOD
Fields:
  AUUID AUUID Single identifier
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWO]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWO]CREUSR (AUTILIS) !Other
  OPTACT ACV Activity code -> [ACV]CODACT =[ASWO]OPTACT (ACTIV) !Block
  OPTCND AFR*250 Option condition
  OPTCOD A*10 Option code
  OPTDEF M*4 Default [menu 1: 1=No,2=Yes]
  OPTERR ATX Error message
  OPTFLGCLA M*4 Class [menu 1: 1=No,2=Yes]
  OPTLIB ATX Option title
  OPTOBY M*4 Mandatory [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWO]UPDUSR (AUTILIS) !Other

## ASHWPAR (ASWP) - Representation (parameters)
Keys (first = PK; D = duplicates allowed): ASWP0 CODREP+TYPPAR+TYPKEY+CODFLD+CODLNK+AFFLNK+CODPAR; ASWP1 CODREP+TYPPAR+CODFLD+CODLNK+AFFLNK+NUMPAR+TYPKEY+CODPAR (D)
Fields:
  ADRVAL M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AFFLNK M*15 Assignment [menu 7965: 1=Property,2=Collection line,3=Collection,4=Page,5=Record]
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CODFLD AVC Field
  CODLNK AVA Link
  CODPAR AVB Parameter code
  CODREP ASW Code -> [ASW]ASW0 =[ASWP]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWP]CREUSR (AUTILIS) !Other
  INTVAL A*250 Internal value
  LNG C*3 Length
  NOLIB MNL Local menu no.
  NUMPAR C*4 Number
  PARENT M*4 Entry P [menu 1: 1=No,2=Yes]
  PARFIL M*4 Filter P [menu 1: 1=No,2=Yes]
  TYPAFF M*4 Input [menu 1: 1=No,2=Yes]
  TYPINT M*15 Internal type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  TYPKEY M*20 Keys [menu 7976: 1=Parameter,2=Key,3=End parameter]
  TYPPAR M*4 Parameter type [menu 59: 1=Property parameter,2=Displayed property parameter,3=Link parameter]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWP]UPDUSR (AUTILIS) !Other
  VALEUR A*250 Value

## ASHWPARMET (ASWMP) - Representation (method param)
Keys (first = PK; D = duplicates allowed): ASWMP0 CODREP+CODMET+CODPARMET; ASWMP1 CODREP+CODMET+NOPARMET+CODPARMET (D)
Fields:
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CLAPARMET ACLA Class -> [ACLA]ACLA0 =[ASWMP]CLAPARMET (ACLASSE) !Block
  CODMET ASM Method code
  CODPARMET AVB Parameter code
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWMP]CODREP (ASHW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWMP]CREUSR (AUTILIS) !Other
  DIMPARMET M*15 Dimension [menu 7987: 1=None,2=From 1,3=From 0]
  INTPARMET ATX Description
  MODPARMET M*15 Method [menu 34: 1=Address,2=Value,3=Constant]
  NOPARMET C*4 Number
  TYPPARMET M*15 Parameter type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWMP]UPDUSR (AUTILIS) !Other

## ASHWSEC (ASWS) - Representation (Sections)
Keys (first = PK; D = duplicates allowed): ASWS0 CODREP+CODSEC; ASWS1 CODREP+NIVSEC+CODSEC
Fields:
  ACTSEC ACV Activity code -> [ACV]CODACT =[ASWS]ACTSEC (ACTIV) !Block
  AUUID AUUID Single identifier
  CODREP ASW Representation code -> [ASW]ASW0 =[ASWS]CODREP (ASHW) !Delete
  CODSEC A*10 Code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASWS]CREUSR (AUTILIS) !Other
  INTSEC ATX Description
  NIVSEC C*4 Display order
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASWS]UPDUSR (AUTILIS) !Other

## ASTYLE (ASY) - Presentation styles
Keys (first = PK; D = duplicates allowed): ASY0 COD
Fields:
  AUUID AUUID Single identifier
  COD ASY Code -> [ASY]ASY0 =[ASY]COD (ASTYLE) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ASY]CREUSR (AUTILIS) !Other
  DES ATX Description
  LIG C*4 Line
  SHO ATX Short description
  STY A*250 Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ASY]UPDUSR (AUTILIS) !Other

## ASTYLEC (ASL) - Conditional styles
Keys (first = PK; D = duplicates allowed): ASL0 COD+LIG
Fields:
  AUUID AUUID Single identifier
  CND AFR*250 Condition
  COD ASL Code -> [ASL]ASL0 =COD;LIG (ASTYLEC) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ASL]CREUSR (AUTILIS) !Other
  DES DES Description
  LIG C*4 Line
  STY ASY Style -> [ASY]ASY0 =[ASL]STY (ASTYLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ASL]UPDUSR (AUTILIS) !Other

## ASTYLEP (AYP) - Personalized styles
Keys (first = PK; D = duplicates allowed): AYP0 CAT+LIG; AYP1 CAT+COD
Fields:
  AUUID AUUID Single identifier
  CAT AYP Category -> [AYP]AYP0 =[AYP]CAT (ASTYLEP) !Delete
  COD ASY Code -> [ASY]ASY0 =[AYP]COD (ASTYLE) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AYP]CREUSR (AUTILIS) !Other
  INTIT DES Description
  LIG C*4 Line
  STY A*250 Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AYP]UPDUSR (AUTILIS) !Other

## ASUBPROG (ASU) - Subprogram table
Keys (first = PK; D = duplicates allowed): ASU0 PRG+SUBPRG
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ASU]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ASU]CREUSR (AUTILIS) !Other
  EXPNUM L*8 Export number
  FONCTION M*4 Function [menu 1: 1=No,2=Yes]
  INTIT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRCOM C*2 Number of comments
  NBRPAR C*2 No. of parameters
  PRG ADC Processing
  PUBLINAM A*10 Publication name
  SUBPRG ASU Subprograms
  TYPASU M*30 Use type [menu 7849: 1=Miscellaneous,2=Control,3=Entry,4=Selection,5=Update,6=Xsl,7=Status,8=Info search,9=Calculation]
  TYPFCT M*15 Argument type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ASU]UPDUSR (AUTILIS) !Other
  WEBS M*4 Web services [menu 1: 1=No,2=Yes]

## ASUBPROGD (ASP) - Sub-program (fields)
Keys (first = PK; D = duplicates allowed): ASP0 PRG+SUBPRG+LIGNE; ASP1 PRG+SUBPRG+PARAM
Fields:
  ADRVAL M*15 Argument type [menu 34: 1=Address,2=Value,3=Constant]
  AUUID AUUID Single identifier
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ASP]CODCLA (ACLASSE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASP]CREUSR (AUTILIS) !Other
  DIME C*4 Dimension
  INTITPAR ATX Description
  LIGNE C*4 Line
  LONG C*3 Length
  PARAM AVB Description
  PRG ADC Processing
  PUBLI APU Publication name
  SUBPRG ASU Subprograms
  TYPPAR M*15 Parameter type [menu 33: 1=Char,2=Integer,3=Decimal,4=Date,5=Libelle,6=Clbfile,7=Blbfile,8=Instance,9=Uuident,10=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASP]UPDUSR (AUTILIS) !Other

## ASYSSMDBASSO (ASM3) - X3
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): DBIDENT1 DBIDENT1; SESSIONID SESSIONID (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASM3]CREUSR (AUTILIS) !Other
  DBIDENT1 A*40 BDD identifier
  DBIDENT2 A*40 BDD identifier
  SESSIONID L*8 Session ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASM3]UPDUSR (AUTILIS) !Other

## ASYSSMEXTERN (ASM1) - X3
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PROCESSID PROCESSID; SESSIONID SESSIONID (D)
Fields:
  ALOGIN ALO Login
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASM1]CREUSR (AUTILIS) !Other
  ESESSIONID L*8 External identifier
  FOLD ADS Folder -> [ADS]DOSSIER =[ASM1]FOLD (ADOSSIER) !Other
  PORT L*8 Port
  PROCESSID L*8 Identifier
  SERVER AMC Host machine
  SESSIONID L*8 Session ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASM1]UPDUSR (AUTILIS) !Other

## ASYSSMINTERN (ASM0) - X3
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): SESSIONID SESSIONID; FOLDER FOLD (D)
Fields:
  ALOGIN ALO Login
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASM0]CREUSR (AUTILIS) !Other
  FOLD ADS Folder -> [ADS]DOSSIER =[ASM0]FOLD (ADOSSIER) !Other
  LAN LAN Language -> [TLA]TLA0 =[ASM0]LAN (TABLAN) !Other
  NATURE M Type [menu 7990: 1=Internal,2=External]
  PEER A*250 Machine
  PROCESSADX L*8 Process
  REMOTE A*40 Client
  SESSIONID L*8 Session ID
  SESSIONTYPE M Type [menu 924: 35 values, see local-menus.md]
  SOLUTION A*40 Solution
  SYSTEMUSER A*250 System user
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASM0]UPDUSR (AUTILIS) !Other

## ASYSSMPROCES (ASM2) - X3
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): PSESSIONID PROCESSID+SESSIONID; SESSIONID SESSIONID (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ASM2]CREUSR (AUTILIS) !Other
  PORT L*8 Port
  PROCESSID L*8 Identifier
  PROCESSNAME A*40 Process
  SERVER AMC Server
  SESSIONID L*8 Session ID
  SYSTEMID L*8 ID of process
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ASM2]UPDUSR (AUTILIS) !Other

## ATABAUD (ATA) - Fields audited
Notes: activity code AUDIT
Keys (first = PK; D = duplicates allowed): ATA0 CODFIC+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[ATA]CODFIC (ATABLE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATA]CREUSR (AUTILIS) !Other
  FLD AVA Field
  NUMLIG C*3 Line no.
  OPE M*15 Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATA]UPDUSR (AUTILIS) !Other
  VALEUR AVV*30 Value

## ATABDIV (ADI) - Miscellaneous tables
Keys (first = PK; D = duplicates allowed): CODE NUMTAB+CODE
Fields:
  A1 A*40 Alpha 1
  A10 A*40 Alpha 10
  A11 A*40 Alpha
  A12 A*40 Alpha
  A13 A*40 Alpha
  A14 A*40 Alpha
  A15 A*40 Alpha
  A2 A*40 Alpha 2
  A3 A*40 Alpha 3
  A4 A*40 Alpha 4
  A5 A*40 Alpha 5
  A6 A*40 Alpha 6
  A7 A*40 Alpha 7
  A8 A*40 Alpha 8
  A9 A*40 Alpha 9
  AUUID AUUID Single identifier
  CODE ADI Code -> [ADI]CODE =NUMTAB;CODE (ATABDIV) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADI]CREUSR (AUTILIS) !Other
  DEFVAL M*4 Default value [menu 1: 1=No,2=Yes]
  DEPCOD ADI Dependency -> [ADI]CODE =NUMTAB;DEPCOD (ATABDIV) !Other
  ENAFLG M*4 Active flag [menu 1: 1=No,2=Yes]
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LNGDES AX3 Description
  N1 DCB*11.6 Numeric 1
  N10 DCB*11.6 Numeric 9
  N11 DCB*11.6 Numeric
  N12 DCB*11.6 Numeric
  N13 DCB*11.6 Numeric
  N14 DCB*11.6 Numeric
  N15 DCB*11.6 Numeric
  N2 DCB*11.6 Numeric 2
  N3 DCB*11.6 Numeric 3
  N4 DCB*11.6 Numeric 4
  N5 DCB*11.6 Numeric 5
  N6 DCB*11.6 Numeric 6
  N7 DCB*11.6 Numeric 7
  N8 DCB*11.6 Numeric 8
  N9 DCB*11.6 Numeric 9
  NUMTAB ADV Table number -> [ADV]CODE =[ADI]NUMTAB (ATABTAB) !Block
  SHODES AX1 Short description
  SOC AGC Group of company -> [AGF]AGF0 =[ADI]SOC (AGRPFCY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADI]UPDUSR (AUTILIS) !Other

## ATABIND (ATI) - Index dictionary
Keys (first = PK; D = duplicates allowed): CODIND CODFIC+CODIND; NUMLIG CODFIC+NUMLIG+CODIND
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ATI]CODACT (ACTIV) !Block
  CODFIC ATB Table code -> [ATB]CODFIC =[ATI]CODFIC (ATABLE) !Delete
  CODIND ANX Index code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATI]CREUSR (AUTILIS) !Other
  DESCRIPT A*120 Index descriptor
  HOMONYM M*15 Duplicate flag [menu 1: 1=No,2=Yes]
  NIVDEC C*2 Data breakdown level
  NUMLIG C*3 Line no.
  ORDIND M*4 Clustered index [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATI]UPDUSR (AUTILIS) !Other

## ATABLE (ATB) - Table dictionary
Keys (first = PK; D = duplicates allowed): CODFIC CODFIC; ABRFIC ABRFIC
Fields:
  ABRFIC ABR Table abbreviation
  ASDCLE A*10 S-data key act:ASD
  AUDBI M*20 Audit bl [menu 1: 1=No,2=Yes] act:ABI
  AUDCLE ANX Key act:AUDIT
  AUDCRE M*20 Audit creation [menu 1: 1=No,2=Yes] act:AUDIT
  AUDDEL M*20 Audit deletion [menu 1: 1=No,2=Yes] act:AUDIT
  AUDSDA C*4 S-data audit act:ASD
  AUDUPD M*20 Auudit modification [menu 1: 1=No,2=Yes] act:AUDIT
  AUDWRK M*20 Workflow [menu 1: 1=No,2=Yes] act:AUDIT
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ATB]CODACT (ACTIV) !Block
  CODFIC ATB Table code -> [ATB]CODFIC =[ATB]CODFIC (ATABLE) !Delete
  COLDEC AVA Decimals column
  COLFMT AVA Format column
  COLLNG AVA Length column
  CRE M*15 Copy type [menu 25: 1=No copy,2=Automatic copy,3=Conditional copy]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATB]CREUSR (AUTILIS) !Other
  FLG130 M*20 Format 130 [menu 1: 1=No,2=Yes]
  FLGLEG M*4 Copy legislation [menu 1: 1=No,2=Yes] act:LEG
  GENTRA M*20 Text generation [menu 1: 1=No,2=Yes]
  INTIT AVA Description field
  INTITC AVA Short title field
  INTITFIC ATX Table title
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBENREG L*8 No. of records
  OPT M*15 Copy option [menu 26: 17 values, see local-menus.md]
  SECURE M*20 Open access [menu 1: 1=No,2=Yes]
  STA M*15 Table type [menu 27: 1=Normal,2=Extension dictionary,3=Dictionary,4=A.E. system,5=Other]
  SYMBOL AVA Symbol column
  TYPDBA M*15 Database type [menu 23: 1=C-ISAM,2=Oracle,3=Folder,4=SQL Server,5=DB2]
  TYPDLV M*20 Delivery type [menu 58: 1=Not delivered,2=Delivered empty,3=Delivered with indus data,4=Common data,5=Data by country]
  TYPFIC M*15 Table type [menu 39: 1=Application,2=Supervisor,3=Sage X3 system,4=Dictionary,5=Internal]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATB]UPDUSR (AUTILIS) !Other
  ZERO M*20 Reset to zero [menu 1: 1=No,2=Yes]

## ATABTAB (ADV) - Miscellaneous table set-up
Keys (first = PK; D = duplicates allowed): CODE NUMTAB
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[ADV]ACS (ACCCOD) !Block
  ALPDES1 AX1 Alpha 1
  ALPDES2 AX1 Alpha 2
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ADV]CODACT (ACTIV) !Block
  CODTYP1 ATY Type -> [ATY]CODTYP =[ADV]CODTYP1 (ATYPE) !Block
  CODTYP2 ATY Type -> [ATY]CODTYP =[ADV]CODTYP2 (ATYPE) !Block
  CODTYP3 ATY Type -> [ATY]CODTYP =[ADV]CODTYP3 (ATYPE) !Block
  CODTYP4 ATY Type -> [ATY]CODTYP =[ADV]CODTYP4 (ATYPE) !Block
  COLALPDES AX1(15) Description
  COLALPSUP A*10(15) Option
  COLALPTYP ATY(15) Data type -> [ATY]CODTYP =[ADV]COLALPTYP (ATYPE) !Block
  COLDES AX1(15) Description
  COLNUMDES AX1(15) Description
  COLNUMSUP A*10(15) Option
  COLNUMTYP ATY(15) Data type -> [ATY]CODTYP =[ADV]COLNUMTYP (ATYPE) !Block
  COLSUP A*10(15) Option
  COLTYP ATY(15) Data type -> [ATY]CODTYP =[ADV]COLTYP (ATYPE) !Block
  COLTYPTYP M*15(15) Column type [menu 46: 1=Alphanumeric,2=Numeric]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ADV]CREUSR (AUTILIS) !Other
  DEPNUM ADV Dependency -> [ADV]CODE =[ADV]DEPNUM (ATABTAB) !Block
  FLGENA M*4 Active flag [menu 1: 1=No,2=Yes]
  FLGLEG M*4 Filter legislation [menu 1: 1=No,2=Yes]
  FLGSOC M*4 Company filter [menu 1: 1=No,2=Yes]
  LNG C*3 Length
  LNGDES AX3 Description
  LNGFLG M*4 Modifiable length [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBCOL C*4 Number
  NUMCAR A*5 Table number
  NUMDES1 AX1 Numeric 1
  NUMDES2 AX1 Numeric 2
  NUMTAB ADV Table number -> [ADV]CODE =[ADV]NUMTAB (ATABTAB) !Delete
  OBLLEG M*4 Legislation entry [menu 1: 1=No,2=Yes]
  SHODES AX1 Short description
  SUP1 A*10 Option
  SUP2 A*10 Option
  SUP3 A*10 Option
  SUP4 A*10 Option
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*4 Modifiable flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[ADV]UPDUSR (AUTILIS) !Other

## ATABZON (ATZ) - Field dictionary
Keys (first = PK; D = duplicates allowed): NUMLIG CODFIC+NUMLIG+CODZONE; CODZONE CODFIC+CODZONE; CODTYP CODTYP+CODFIC+CODZONE; LIEN LIEN+CODFIC+CODZONE; DICO CODZONE (D)
Fields:
  ANNUL M*15 Cancellation flag [menu 24: 1=Block,2=Delete,3=RTZ,4=Other]
  AUUID AUUID Single identifier
  CHPLEG M*4 Copy legislation [menu 1: 1=No,2=Yes] act:LEG
  CODACT ACV Activity code -> [ACV]CODACT =[ATZ]CODACT (ACTIV) !Block
  CODFIC ATB Table code -> [ATB]CODFIC =[ATZ]CODFIC (ATABLE) !Delete
  CODTYP ATY Data type -> [ATY]CODTYP =[ATZ]CODTYP (ATYPE) !Block
  CODZONE AVA Field code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATZ]CREUSR (AUTILIS) !Other
  DIME C*2 Dimension
  EXPLIEN A*100 Link expression
  LIEN ATB Linked table -> [ATB]CODFIC =[ATZ]LIEN (ATABLE) !Other
  LONG DCB*5 Field length
  NOABREG ATX Abbreviated text
  NOCOURT ATX Normal text
  NOLIB MNL Local menu no.
  NOLONG ATX Long text
  NUMLIG C*3 Line no.
  OBLIG M*4 Mandatory link [menu 1: 1=No,2=Yes]
  OPTION A*10 Entry options
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATZ]UPDUSR (AUTILIS) !Other
  VERIF M*4 Verification [menu 1: 1=No,2=Yes]
  ZERO M*4 Reset to zero [menu 1: 1=No,2=Yes]

## ATEXTE (ATX) - Dictionary messages
Notes: differs in V10 P1 (diff: ATD_ATEXTE.htm)
Keys (first = PK; D = duplicates allowed): NUMERO LAN+NUMERO; TEXTE LAN+TEXTE (D); CLEREC LAN+CLEREC (D); DERNUM NUMERO+LAN
Fields:
  AUUID AUUID Single identifier
  CLEREC A*20 Search key
  COMMENT A*80 Comment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATX]CREUSR (AUTILIS) !Other
  LAN LAN Language -> [TLA]TLA0 =[ATX]LAN (TABLAN) !Block
  LANORI LAN Original language -> [TLA]TLA0 =[ATX]LANORI (TABLAN) !Block
  LONG C*4 Text length
  NOMOBJ A*12 Object name
  NOMZON A*12 Field name
  NUMERO L*8 Text number
  TEXTE A*80 Text
  TYPOBJ M*25 Object type [menu 42: 26 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATX]UPDUSR (AUTILIS) !Other

## ATEXTEXCEP (AEX) - Exceptions (translations)
Notes: activity code DIS
Keys (first = PK; D = duplicates allowed): AEX0 VERORI+LAN+NUMERO; AEX1 VERORI+NAMREP+SUBREP+SECREP+OBJREP+LAN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AEX]CREUSR (AUTILIS) !Other
  DESREP A*65 Description
  LAN LAN Language -> [TLA]TLA0 =[AEX]LAN (TABLAN) !Block
  NAMREP A*25 Name
  NUMERO L*8 Number
  OBJREP L*2 Object
  SECREP L*2 Dimension
  SUBREP L*2 Sub-report
  TXT A*80 Text
  TXTREF ATX No. text reference
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AEX]UPDUSR (AUTILIS) !Other
  VERORI A*4 Version

## ATEXTRA (AXX) - Texts to translate
Keys (first = PK; D = duplicates allowed): AXX0 CODFIC+ZONE+LANGUE+IDENT1+IDENT2; AXX1 LANGUE+CODFIC+ZONE (D)
Fields:
  AUUID AUUID Single identifier
  CODFIC ATB Table -> [ATB]CODFIC =[AXX]CODFIC (ATABLE) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AXX]CREUSR (AUTILIS) !Other
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  LANGUE LAN Language -> [TLA]TLA0 =[AXX]LANGUE (TABLAN) !Delete
  LANORI LAN Original language -> [TLA]TLA0 =[AXX]LANORI (TABLAN) !Block
  TEXTE A*80 Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AXX]UPDUSR (AUTILIS) !Other
  ZONE AVA Field

## ATMPTRA (ATT) - Temporary trace file
Keys (first = PK; D = duplicates allowed): ATT0 NUMREQ+LIG
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATT]CREUSR (AUTILIS) !Other
  LIG L*6 Line number
  NUMREQ L*8 Query no.
  TXT A*250 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATT]UPDUSR (AUTILIS) !Other

## ATRANSAC (ATN) - Transaction type
Keys (first = PK; D = duplicates allowed): ATN0 COD; ATN1 OBJGES (D)
Fields:
  AUUID AUUID Single identifier
  CND AFR*250 Condition
  COD ATN Code -> [ATN]ATN0 =[ATN]COD (ATRANSAC) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[ATN]CODACT (ACTIV) !Block
  CODTRT ADC Processing
  COP M*4 Copy [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATN]CREUSR (AUTILIS) !Other
  DES ATX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLDCOD A*10 Code
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  OBJ AOB Object -> [AOB]ABREV =[ATN]OBJ (AOBJET) !Block
  OBJGES AOB Management object -> [AOB]ABREV =[ATN]OBJGES (AOBJET) !Block
  TBL ATB Table -> [ATB]CODFIC =[ATN]TBL (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATN]UPDUSR (AUTILIS) !Other

## ATYPE (ATY) - Data types
Keys (first = PK; D = duplicates allowed): CODTYP CODTYP; GLOBVAR TYPTYP+CODTYP
Fields:
  ACTION ACT(30) Action code -> [ACT]ACTION =[ATY]ACTION (ACTION) !Block
  ACTTYP M*15(30) Action type [menu 31: 31 values, see local-menus.md]
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[ATY]CODACT (ACTIV) !Block
  CODCLA ACLA Class code -> [ACLA]ACLA0 =[ATY]CODCLA (ACLASSE) !Block
  CODTYP ATY Data type -> [ATY]CODTYP =[ATY]CODTYP (ATYPE) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATY]CREUSR (AUTILIS) !Other
  DEFREPDES ASW Desktop -> [ASW]ASW0 =[ATY]DEFREPDES (ASHW) !Block
  DEFREPMOB ASW Mobile phone -> [ASW]ASW0 =[ATY]DEFREPMOB (ASHW) !Block
  DEFREPTAB ASW Pad -> [ASW]ASW0 =[ATY]DEFREPTAB (ASHW) !Block
  EXEACT M*15(30) Execution [menu 928: 1=Interactive,2=Import/batch,3=Always]
  FICLIEN ATB Linked table -> [ATB]CODFIC =[ATY]FICLIEN (ATABLE) !Block
  FMTPROSYR M*30 Prototype format [menu 7880: 1=Aucun,2=$email,3=$phone,4=$combo,5=$radios,6=TT,7=password]
  FORTYP A*50 Adonix format
  INTITTYP ATX Description
  LNGTYP DCB*5 Length
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBTYP C*2 Number of actions
  NOLIB MNL Local menu no.
  OBJLIEN AOB Linked object -> [AOB]ABREV =[ATY]OBJLIEN (AOBJET) !Block
  OPTION A*10 Entry options
  OPTTAB M*4 Variable format [menu 1: 1=No,2=Yes]
  PARTAB AAR Parameter -> [AAR]CODPAR =[ATY]PARTAB (ACTCODPAR) !Block
  SUPFLG M*20 Supervisor mgmt [menu 1: 1=No,2=Yes]
  TYPPROSYR ATYP Content type -> [ATYP]ATYP0 =[ATY]TYPPROSYR (ATYPEPRO) !Block
  TYPSELSYR M*15 Type [menu 7881: 1=Simple,2=Reference,3=Rich media]
  TYPTYP M*15 Internal type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATY]UPDUSR (AUTILIS) !Other
  VALDEF A*80 Default value
  VARTAB A*15 Variable

## ATYPELNK (ATYL) - Data type links
Keys (first = PK; D = duplicates allowed): ATYL0 CODTYP+CODLNK
Fields:
  ACTLNK ACV Activity code -> [ACV]CODACT =[ATYL]ACTLNK (ACTIV) !Block
  AUUID AUUID Single identifier
  CODLNK A*8 Code
  CODTYP ATY Data type -> [ATY]CODTYP =[ATYL]CODTYP (ATYPE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATYL]CREUSR (AUTILIS) !Other
  ORDLNK C*4 Sequence
  REPLNK ASW Representation -> [ASW]ASW0 =[ATYL]REPLNK (ASHW) !Block
  TYPLNK M*25 Link type [menu 7971: 22 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATYL]UPDUSR (AUTILIS) !Other

## ATYPELPAR (ATYLP) - Data type parameters
Keys (first = PK; D = duplicates allowed): ATYLP0 CODTYP+CODLNK+PARCOD
Fields:
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CODLNK A*8 Code
  CODTYP ATY Data type -> [ATY]CODTYP =[ATYLP]CODTYP (ATYPE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATYLP]CREUSR (AUTILIS) !Other
  PARCLA ACLA Class code -> [ACLA]ACLA0 =[ATYLP]PARCLA (ACLASSE) !Block
  PARCOD A*50 Code
  PARDIM M*15 Dim. [menu 7987: 1=None,2=From 1,3=From 0]
  PARMOD M*15 Method [menu 34: 1=Address,2=Value,3=Constant]
  PARTIT ATX Description
  PARTYP M*15 Type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATYLP]UPDUSR (AUTILIS) !Other

## ATYPEPRO (ATYP) - Content type
Keys (first = PK; D = duplicates allowed): ATYP0 COD
Fields:
  AUUID AUUID Single identifier
  COD A*10 Code
  CODACT ACV Activity code -> [ACV]CODACT =[ATYP]CODACT (ACTIV) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATYP]CREUSR (AUTILIS) !Other
  INTIT ATX Description
  LISFLG M*15 List [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  PREFLG M*15 Specifiable [menu 1: 1=No,2=Yes]
  PROTYP A*100 Content type
  STDFLG M*15 Standard [menu 1: 1=No,2=Yes]
  TYPTYP M*15 Internal type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATYP]UPDUSR (AUTILIS) !Other

## ATYPERPAR (ATYRP) - Data type parameters
Keys (first = PK; D = duplicates allowed): ATYRP0 CODTYP+TYPRUL+TRTRUL+PRGRUL+PARCOD; ATYRP1 CODTYP+TYPRUL+TRTRUL+PRGRUL+PARORD (D)
Fields:
  AUUID AUUID Single identifier
  AWMAJTYP M*4 [menu 1: 1=No,2=Yes]
  CODTYP ATY Data type -> [ATY]CODTYP =[ATYRP]CODTYP (ATYPE) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATYRP]CREUSR (AUTILIS) !Other
  PARCLA ACLA Class code -> [ACLA]ACLA0 =[ATYRP]PARCLA (ACLASSE) !Block
  PARCLE M*4 Key [menu 1: 1=No,2=Yes]
  PARCOD A*50 Code
  PARDIM M*15 Dim. [menu 7987: 1=None,2=From 1,3=From 0]
  PARMOD M*15 Method [menu 34: 1=Address,2=Value,3=Constant]
  PARORD C*4 Order
  PARTIT ATX Description
  PARTYP M*15 Type [menu 10030: 1=TinyInt,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Blob,10=Clob,11=Uuid,12=Datetime,13=Instance]
  PRGRUL ASU Sub-program
  TRTRUL ADC Processing
  TYPRUL M*15 Type [menu 7961: 1=INIT,2=CONTROL,3=PROPAGATE,4=GETVALUE,5=FORMAT,6=READ_MEDIA,7=UPDATE_MEDIA,8=DELETE_MEDIA,9=INSERT_MEDIA,10=READ_MEDIA_CNT,11=EXIST_MEDIA]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATYRP]UPDUSR (AUTILIS) !Other

## ATYPERUL (ATYR) - Data type rules
Keys (first = PK; D = duplicates allowed): ATYR0 CODTYP+TYPRUL+TRTRUL+PRGRUL
Fields:
  ACTRUL ACV Activity code -> [ACV]CODACT =[ATYR]ACTRUL (ACTIV) !Block
  AUUID AUUID Single identifier
  CODTYP ATY Data type -> [ATY]CODTYP =[ATYR]CODTYP (ATYPE) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATYR]CREUSR (AUTILIS) !Other
  ENARUL M*4 Active [menu 1: 1=No,2=Yes]
  ORDRUL C*4 Sequence
  PRGRUL ASU Sub-program
  TRTRUL ADC Processing
  TYPRUL M*15 Type [menu 7961: 1=INIT,2=CONTROL,3=PROPAGATE,4=GETVALUE,5=FORMAT,6=READ_MEDIA,7=UPDATE_MEDIA,8=DELETE_MEDIA,9=INSERT_MEDIA,10=READ_MEDIA_CNT,11=EXIST_MEDIA]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATYR]UPDUSR (AUTILIS) !Other

## AUDITBI (AUI) - Audit bl
Notes: activity code AUDIT; differs in V9.0 P12 (diff: AT3_AUDITBI.htm)
Keys (first = PK; D = duplicates allowed): AUD0 SEQ; AUD1 STA+SEQ; AUD2 ADOUSR (D); AUD3 STABI+SEQ
Fields:
  ADOUSR A*5 X3 user
  ADRCLI A*30 Customer address
  CHAR1 ID2 Alphanumeric key
  CHAR10 ID2 Alphanumeric key
  CHAR11 ID2 Alphanumeric key
  CHAR12 ID2 Alphanumeric key
  CHAR13 ID2 Alphanumeric key
  CHAR14 ID2 Alphanumeric key
  CHAR15 ID2 Alphanumeric key
  CHAR16 ID2 Alphanumeric key
  CHAR2 ID2 Alphanumeric key
  CHAR3 ID2 Alphanumeric key
  CHAR4 ID2 Alphanumeric key
  CHAR5 ID2 Alphanumeric key
  CHAR6 ID2 Alphanumeric key
  CHAR7 ID2 Alphanumeric key
  CHAR8 ID2 Alphanumeric key
  CHAR9 ID2 Alphanumeric key
  DAT D Date
  EVT A*10 Event
  HOU HS Time
  ID1 A*250 Key
  ID2 A*250 Secondary key
  NUM1 DCB*9.2 Numeric key
  NUM10 DCB*9.2 Numeric key
  NUM11 DCB*9.2 Numeric key
  NUM12 DCB*9.2 Numeric key
  NUM13 DCB*9.2 Numeric key
  NUM14 DCB*9.2 Numeric key
  NUM15 DCB*9.2 Numeric key
  NUM16 DCB*9.2 Numeric key
  NUM2 DCB*9.2 Numeric key
  NUM3 DCB*9.2 Numeric key
  NUM4 DCB*9.2 Numeric key
  NUM5 DCB*9.2 Numeric key
  NUM6 DCB*9.2 Numeric key
  NUM7 DCB*9.2 Numeric key
  NUM8 DCB*9.2 Numeric key
  NUM9 DCB*9.2 Numeric key
  SEQ L*8 Sequence no.
  STA M*10 Workflow status [menu 947: 1=None,2=To process,3=Processed]
  STABI M*10 Status BI [menu 947: 1=None,2=To process,3=Processed]
  SYSUSR A*20 System user
  TBL ATB Table -> [ATB]CODFIC =[AUI]TBL (ATABLE) !Block

## AUDITH (AUD) - Audit - header
Notes: activity code AUDIT; differs in V9.0 P12 (diff: AT3_AUDITH.htm)
Keys (first = PK; D = duplicates allowed): AUD0 SEQ; AUD1 STA+SEQ; AUD2 ADOUSR (D); AUD3 STABI+SEQ
Fields:
  ADOUSR A*5 X3 user
  ADRCLI A*30 Customer address
  CHAR1 ID2 Alphanumeric key
  CHAR10 ID2 Alphanumeric key
  CHAR11 ID2 Alphanumeric key
  CHAR12 ID2 Alphanumeric key
  CHAR13 ID2 Alphanumeric key
  CHAR14 ID2 Alphanumeric key
  CHAR15 ID2 Alphanumeric key
  CHAR16 ID2 Alphanumeric key
  CHAR2 ID2 Alphanumeric key
  CHAR3 ID2 Alphanumeric key
  CHAR4 ID2 Alphanumeric key
  CHAR5 ID2 Alphanumeric key
  CHAR6 ID2 Alphanumeric key
  CHAR7 ID2 Alphanumeric key
  CHAR8 ID2 Alphanumeric key
  CHAR9 ID2 Alphanumeric key
  DAT D Date
  EVT A*10 Event
  HOU HS Time
  ID1 A*250 Key
  ID2 A*250 Secondary key
  NUM1 DCB*9.2 Numeric key
  NUM10 DCB*9.2 Numeric key
  NUM11 DCB*9.2 Numeric key
  NUM12 DCB*9.2 Numeric key
  NUM13 DCB*9.2 Numeric key
  NUM14 DCB*9.2 Numeric key
  NUM15 DCB*9.2 Numeric key
  NUM16 DCB*9.2 Numeric key
  NUM2 DCB*9.2 Numeric key
  NUM3 DCB*9.2 Numeric key
  NUM4 DCB*9.2 Numeric key
  NUM5 DCB*9.2 Numeric key
  NUM6 DCB*9.2 Numeric key
  NUM7 DCB*9.2 Numeric key
  NUM8 DCB*9.2 Numeric key
  NUM9 DCB*9.2 Numeric key
  SEQ L*8 Sequence no.
  STA M*10 Workflow status [menu 947: 1=None,2=To process,3=Processed]
  STABI M*10 Status BI [menu 947: 1=None,2=To process,3=Processed]
  SYSUSR A*20 System user
  TBL ATB Table -> [ATB]CODFIC =[AUD]TBL (ATABLE) !Block

## AUDITL (AUL) - Audit - lines
Notes: activity code AUDIT
Keys (first = PK; D = duplicates allowed): AUL0 SEQ+COL
Fields:
  COL A*20 Column
  NVAL A*250 New value
  OVAL A*250 Previous value
  SEQ L*8 Sequence no.

## AURL (AUR) - Definition of URL
Keys (first = PK; D = duplicates allowed): AUR0 CODURL
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AUR]CODACT (ACTIV) !Block
  CODURL AUR Code -> [AUR]AUR0 =[AUR]CODURL (AURL) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AUR]CREUSR (AUTILIS) !Other
  INTEVAL A*60 Evaluated title
  INTIT ATX Description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  PARXSL A*10 Parameter code
  PLEURL M*20 Location [menu 2908: 1=World wide web,2=Public folder,3=Current folder]
  SECLEV M*10 Security level [menu 2909: 1=High,2=Medium,3=Low]
  TYPURL M*15 Link type [menu 2934: 1=URL,2=XSL,3=Html]
  TYPXSL M*15 XSL type [menu 9835: 1=Miscellaneous,2=Planning,3=BOM,4=Radar]
  UCOD A*6(5) Code
  UMEN C*4(5) Local menu
  UPARCOD A*6(5) Parameter code
  UPARDEF A*10(5) Value
  UPARLIB A*30(5) Description
  UPARMEN M*4(5) Local menu [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AUR]UPDUSR (AUTILIS) !Other
  UPRG ADC(3) Program
  URL A*250 URL
  USPRG ASU(3) Subprograms
  XSLCLOB AC1 XSL

## AUSRBPR (AUB) - BP users
Keys (first = PK; D = duplicates allowed): AUB0 USR+BPR+ROL
Fields:
  AUUID AUUID Single identifier
  BPR A*30 BP
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AUB]CREUSR (AUTILIS) !Other
  ROL ADI Roles -> [ADI]CODE =60;ROL (ATABDIV) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AUB]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AUB]USR (AUTILIS) !Delete

## AUSRSOL (AUO) - Solution users
Keys (first = PK; D = duplicates allowed): AUO0 USR
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AUO]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AUO]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AUO]USR (AUTILIS) !Other

## AUSRSTA (AUA) - Statistics
Keys (first = PK; D = duplicates allowed): AUA0 NUM; AUA1 DOSSIER+USR+PER+EVT+ARG1+ARG2
Fields:
  ARG1 A*12 Argument 1
  ARG2 A*12 Argument 2
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AUA]CREUSR (AUTILIS) !Other
  CTR A*24 Control key
  DOSSIER ADS Folder -> [ADS]DOSSIER =[AUA]DOSSIER (ADOSSIER) !Delete
  EVT M*4 Event [menu 7858: 1=Connection,2=Function,3=Others]
  FLG L*8 Sent flag
  NBR L*8 Value
  NUM L*8 Number
  PER A*4 Period
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AUA]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AUA]USR (AUTILIS) !Delete

## AUTILIS (AUS) - Users
Keys (first = PK; D = duplicates allowed): CODUSR USR; LOGIN LOGIN (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GCACAUS;ACCCOD;[V]GSUPCLE (GACCCODE) !Other act:CPT
  ACSUSR ACS Access -> [ACS]ACS0 =[AUS]ACSUSR (ACCCOD) !Block
  ADDEML MAI Email address
  ADDNAM A*250 AD reference
  ALLACS M*4 All access codes [menu 1: 1=No,2=Yes]
  ARCPRF ARU Profile code -> [ARU]ARU0 =[AUS]ARCPRF (ARCHPARU) !Block
  ARVHOU HM(7) Arrival time
  AUSDAY M*15(7) Days [menu 742: 1=Monday,2=Tuesday,3=Wednesday,4=Thursday,5=Friday,6=Saturday,7=Sunday]
  AUUID AUUID Single identifier
  AUZDSCDEM M*4 Dispatching [menu 1: 1=No,2=Yes]
  BIDNUM BID Bank acct. number
  BPAADD ADR Default address
  BPRNUM A*10 BP
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHEF AUS(20) Supervisors -> [AUS]CODUSR =[AUS]CHEF (AUTILIS) !RTZ
  CHGDAT M*4 Date change [menu 1: 1=No,2=Yes]
  CODADRDFT ADR Default address
  CODMET AME Profession code -> [AME]AME0 =[AUS]CODMET (AMETUTI) !Block
  CODRIBDFT BID Default bank ID
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AUS]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[AUS]CUR (TABCUR) !Block
  DATCONN D Connection date
  DECTIME L*5 Time-out
  DIE DIE Dimension type code -> [DIE]DIE0 =[AUS]DIE (GDIE) !Block act:ANA
  DIFIMP M*4 Deferred prints [menu 1: 1=No,2=Yes]
  DPEHOU HM(7) Leaving time
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ESCSTRDAT D Escalation start date
  FAX TEL Default fax
  FLGPASPRV M*4 Provisional [menu 1: 1=No,2=Yes]
  FNC M*15 Function [menu 977: 1=Sales Engineer,2=Telesales,3=Sales Director,4=Customer support,5=Other]
  FNCCOD AFC(8) Functions -> [AFC]CODINT =[AUS]FNCCOD (AFONCTION) !Block
  FNCPAR A*10(8) Parameters
  FULTIM M*4 Full time [menu 1: 1=No,2=Yes]
  HDKREP M*4 Help-desk [menu 1: 1=No,2=Yes]
  INTUSR AX3 Name
  KILRAT DCB*9.2 Kilometer rate
  LOGIN ALO Login
  MNA M*15 Supervisor [menu 50: 1=Supervisor,2=Department Head,3=Director]
  MSNEND D End of the mission
  MSNSTR D Task start
  NBDAY C*4 Number of days
  NBFNC C*4 No.
  NBRCON C*4 Number of connections
  NBRESC C*4 No. of escalations
  NEWPAS A*24 New password
  NOMUSR DES Name
  PASSDAT D Validity date
  PASSE A*10 Password
  PRFFCT AFT Function profile -> [AFT]AFT0 =[AUS]PRFFCT (AFCTFCT) !Block
  PRFMEN APM Menu profile -> [APF]CODPRF =0;PRFMEN (APROFIL) !Block
  PRFXTD AYH Safe X3 WAS profile -> [AYH]AYH0 =[AUS]PRFXTD (AYTPRFUSR) !Block act:AYT
  PRTDEF AIM(10) Destination -> [AIM]AIM0 =[AUS]PRTDEF (APRINTER) !Block
  PWDBI A*24 BI password act:ABI
  REPNUM A*10 Sales rep code
  RPCREP C*4 Sales rep
  STA M*15 Status [menu 978: 1=Permanent,2=Temporary,3=Part time]
  TELEP TEL Default telephone
  TIMCONN A*10 Connection time
  TIT AFR*250 Title bar
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AUS]UPDUSR (AUTILIS) !Other
  USR AUS Code -> [AUS]CODUSR =[AUS]USR (AUTILIS) !Delete
  USRBI AIU BI user -> [AIU]AIU0 =[AUS]USRBI (ABIPRFUSR) !Block act:ABI
  USRCONNECT M*4 X3 connection [menu 1: 1=No,2=Yes]
  USRCONXTD M*4 Web services connect. [menu 1: 1=No,2=Yes]
  USREXT M*4 External user [menu 1: 1=No,2=Yes]
  USRPRT AUS User model -> [AUS]CODUSR =[AUS]USRPRT (AUTILIS) !Block
  WITHOUTLDAP M*4 Without LDAP [menu 1: 1=No,2=Yes]
  WRH WRH Warehouse -> [WRH]WRH0 =[AUS]WRH (WAREHOUSE) !Block act:WRH

## AVALATT (AVA) - Sequence number values
Keys (first = PK; D = duplicates allowed): AVA0 CODNUM+SITE+PERIODE+COMP+VALEUR
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =CODNUM (ACODNUM) !Delete
  COMP A*20 Additional info
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVA]CREUSR (AUTILIS) !Other
  PERIODE C*4 Period
  SITE FCY Site or company -> [FCY]FCY0 =[AVA]SITE (FACILITY) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVA]UPDUSR (AUTILIS) !Other
  VALEUR DCB*20 Sequence no.

## AVALNUM (AVN) - Sequence number values
Keys (first = PK; D = duplicates allowed): AVN0 CODNUM+SITE+PERIODE+COMP
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =CODNUM (ACODNUM) !Delete
  COMP A*25 Additional info
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVN]CREUSR (AUTILIS) !Other
  PERIODE C*4 Period
  SITE A*5 Site or company
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVN]UPDUSR (AUTILIS) !Other
  VALEUR DCB*20 Sequence no.

## AVARLOC (AVR) - Formula wizard setup
Keys (first = PK; D = duplicates allowed): AVR0 TYP+FCT+COD
Fields:
  AUUID AUUID Single identifier
  COD AFR*80 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AVR]CREUSR (AUTILIS) !Other
  FCT AFC Function -> [AFC]CODINT =[AVR]FCT (AFONCTION) !Block
  INTIT ATX Description
  TYP M*15 Type [menu 2945: 1=Global variables,2=Local variables,3=Functions]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AVR]UPDUSR (AUTILIS) !Other

## AVIEW (AVW) - Dictionary of views
Keys (first = PK; D = duplicates allowed): AVW0 CODVUE; AVW1 ABRVUE (D)
Fields:
  ABRVUE ABR Abbreviation
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AVW]CODACT (ACTIV) !Block
  CODVUE AVW View code -> [AVW]AVW0 =[AVW]CODVUE (AVIEW) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AVW]CREUSR (AUTILIS) !Other
  INTIT ATX View title
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  SECURE M*20 Open access [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[AVW]UPDUSR (AUTILIS) !Other

## AVIEWB (AVB) - Dictionary of views
Keys (first = PK; D = duplicates allowed): AVB0 CODVUE+TYPDBA
Fields:
  AUUID AUUID Single identifier
  CODVUE AVW View code -> [AVW]AVW0 =[AVB]CODVUE (AVIEW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVB]CREUSR (AUTILIS) !Other
  TEXTE AC0*5 Query
  TYPDBA M*15 Database type [menu 57: 1=Oracle,2=SQL Server]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVB]UPDUSR (AUTILIS) !Other

## AVIEWC (AVC) - Dictionary of keys
Keys (first = PK; D = duplicates allowed): AVC0 CODVUE+CODCLE; AVC1 CODVUE+NUMLIG+CODCLE
Fields:
  AUUID AUUID Single identifier
  CLEACT ACV Activity code -> [ACV]CODACT =[AVC]CLEACT (ACTIV) !Block
  CODCLE ANX Key code
  CODVUE AVW View code -> [AVW]AVW0 =[AVC]CODVUE (AVIEW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVC]CREUSR (AUTILIS) !Other
  DESCLE A*120 Key description
  KEYDUP M*4 Duplicate flag [menu 1: 1=No,2=Yes]
  NUMLIG C*3 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVC]UPDUSR (AUTILIS) !Other

## AVIEWD (AVD) - Dictionary of views
Keys (first = PK; D = duplicates allowed): AVD0 CODVUE+NUMLIG+FLDVUE; AVD1 CODVUE+FLDVUE; AVD2 CODTYP+CODVUE+FLDVUE
Fields:
  AUUID AUUID Single identifier
  CODTYP ATY Data type -> [ATY]CODTYP =[AVD]CODTYP (ATYPE) !Block
  CODVUE AVW View code -> [AVW]AVW0 =[AVD]CODVUE (AVIEW) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVD]CREUSR (AUTILIS) !Other
  DIME C*2 Dimension
  FLDACT ACV Activity code -> [ACV]CODACT =[AVD]FLDACT (ACTIV) !Block
  FLDINT ATX Description
  FLDVUE AVA Fields
  LNG DCB*5 Length
  NOLIB MNL Local menu no.
  NUMLIG C*3 Line no.
  OPTION A*10 Display options
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVD]UPDUSR (AUTILIS) !Other

## AVOCAB (AVO) - Personalized vocabulary
Notes: differs in V9.0 P12 (diff: AT3_AVOCAB.htm)
Keys (first = PK; D = duplicates allowed): AVO0 LAN+VER+TYP+CHP+NUM
Fields:
  AUUID AUUID Single identifier
  CHP C*5 Chapter
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVO]CREUSR (AUTILIS) !Other
  CUR M*15 Version [menu 7840: 1=Version 1,2=Version 2,3=Version 3]
  LAN LAN Language -> [TLA]TLA0 =[AVO]LAN (TABLAN) !Delete
  NUM L*8 Number
  TXT A*123 Text
  TYP M*15 Text type [menu 937: 1=Text,2=Message]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVO]UPDUSR (AUTILIS) !Other
  VER M*15 Version [menu 7840: 1=Version 1,2=Version 2,3=Version 3]

## AVOLUME (AVL) - Volume
Keys (first = PK; D = duplicates allowed): CODE VOLUME
Fields:
  AUUID AUUID Single identifier
  CODACC ACS Access code -> [ACS]ACS0 =[AVL]CODACC (ACCCOD) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AVL]CREUSR (AUTILIS) !Other
  DES AX3 Description
  ROOT A*250 Root
  TITLE A*250 Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AVL]UPDUSR (AUTILIS) !Other
  VOLTYP M*20 Type [menu 7871: 1=File,2=Image file in database,3=Text file in database]
  VOLUME AVL Volume -> [AVL]CODE =[AVL]VOLUME (AVOLUME) !BSRA

## AWEBSERDES (AWY) - Web service mapping
Keys (first = PK; D = duplicates allowed): AWY1 PUBLI+GRP+CHP
Fields:
  AUTMAX M*4 Maximum entry [menu 1: 1=No,2=Yes]
  AUTMIN M*4 Minimum entry [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CHAMP A*40 Code
  CHP A*30 Field
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWY]CREUSR (AUTILIS) !Other
  FRACTIONDIG C*1 Fractiondigits
  GROUPE A*40 Group
  GRP A*10 Block
  IDX C*4 Index
  LONCHP C*4 Length
  MAXINCLU M*4 Include [menu 1: 1=No,2=Yes]
  MININCLU M*4 Include [menu 1: 1=No,2=Yes]
  NOLIB MNL Local menu no.
  PATTERN A*30 Pattern
  PUBLI AWE Publication name
  SELECT M*4 Selected [menu 1: 1=No,2=Yes]
  TOTALDIGIT C*2 Totaldigits
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWY]UPDUSR (AUTILIS) !Other
  USERP AUS User -> [AUS]CODUSR =[AWY]USERP (AUTILIS) !Other
  VALMAX L*8 Value
  VALMIN C*4 Value

## AWEBSERVIC (AWE) - Web services
Keys (first = PK; D = duplicates allowed): AWE1 PUBLI
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWE]CREUSR (AUTILIS) !Other
  DATPUB A*14 Published on
  INVISIBLE M*4 Invisible fields [menu 1: 1=No,2=Yes]
  LIBW AX3 Description
  OBJET AOB Object -> [AOB]ABREV =[AWE]OBJET (AOBJET) !Other
  PRG ADC Processing
  PUBLI AWE Publication name
  SUBPRG ASU Subprograms
  TYPOBJ M*15 Type [menu 906: 1=Object,2=Sub-program]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWE]UPDUSR (AUTILIS) !Other
  USERP AUS User -> [AUS]CODUSR =[AWE]USERP (AUTILIS) !Other
  VARIANTE A*10 Transaction
  VERGEN A*5 Version

## AWINBOUT (AWT) - Window button dictionary
Keys (first = PK; D = duplicates allowed): AWT0 WIN+NUM+CODBOUT
Fields:
  ACTBOUT ACT Action -> [ACT]ACTION =[AWT]ACTBOUT (ACTION) !Block
  AUUID AUUID Single identifier
  CODACTBOUT ACV Activity code -> [ACV]CODACT =[AWT]CODACTBOUT (ACTIV) !Block
  CODBOUT A*3 Button code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWT]CREUSR (AUTILIS) !Other
  NUM C*3 Number
  TXTBOUT ATX Button text
  TYPBOUT M*15 Type [menu 88: 1=Button,2=Menu,3=Line]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWT]UPDUSR (AUTILIS) !Other
  VALBOUT M*15 Validating/invalidating [menu 927: 1=Non validating,2=Validating]
  WIN FEN Window -> [AWI]AWI0 =[AWT]WIN (AWINDOW) !Delete

## AWINBRO (AWB) - Browser window dictionary
Keys (first = PK; D = duplicates allowed): AWB0 WIN
Fields:
  ABRLIS ABR(9) Abbreviation
  ACTLIS ACV(9) Activity code -> [ACV]CODACT =[AWB]ACTLIS (ACTIV) !Block
  AFLBRO M*15 Browser display [menu 942: 1=Small,2=Average,3=Large]
  AUUID AUUID Single identifier
  BROLIS M*4(9) Browser [menu 1: 1=No,2=Yes]
  CHGLIS M*4(9) Preloading [menu 918: 1=No,2=Partial,3=Total]
  CLELIS ANX(9) Index
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWB]CREUSR (AUTILIS) !Other
  DERLU M*4 Last read [menu 1: 1=No,2=Yes]
  EXPLIS A*60(9) Link expression
  FIRLIS M*4 In first position [menu 1: 1=No,2=Yes]
  FLELIS M*4(9) Pointers [menu 1: 1=No,2=Yes]
  INTLIS ATX(9) Description
  NBLIS C*3 No. of lists
  OBJLIS AOB(9) Object -> [AOB]ABREV =[AWB]OBJLIS (AOBJET) !Block
  ORDLIS M*10(9) Sign [menu 90: 1=Ascending,2=Descending]
  ROWLIS C*4(9) Sequence
  TRELIS M*4(9) Hierarchical list [menu 919: 1=Simple,2=Hierarchical,3=Selection,4=Recursive,5=Simple selection]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWB]UPDUSR (AUTILIS) !Other
  WIN FEN Window -> [AWI]AWI0 =[AWB]WIN (AWINDOW) !Delete

## AWINDOW (AWI) - Window dictionary
Keys (first = PK; D = duplicates allowed): AWI0 WIN; AWI1 OBJ+WIN; AWI2 OBJ+TRN+WIN
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[AWI]ACS (ACCCOD) !Block
  ACTMSK ACV(15) Activity code -> [ACV]CODACT =[AWI]ACTMSK (ACTIV) !Block
  ACTSTD ACT(20) Actions -> [ACT]ACTION =[AWI]ACTSTD (ACTION) !Block
  AUUID AUUID Single identifier
  BSTD M*4(20) Buttons [menu 1: 1=No,2=Yes]
  CNS ACN Inquiry -> [ACN]ACN0 =[AWI]CNS (ACONSULT) !RTZ
  CODACT ACV Activity code -> [ACV]CODACT =[AWI]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWI]CREUSR (AUTILIS) !Other
  DES ATX Description
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLGMSK M*4(15) Input [menu 1: 1=No,2=Yes]
  FVT M*4 VT window [menu 1: 1=No,2=Yes]
  INTFOLD A*60(15) Evaluated title
  INTMSK ATX(15) Tab titles
  LIBEL DES Menu title
  MDL M*4 Window template [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  MSKENT AMK Header screen -> [AMK]CODMSK =[AWI]MSKENT (AMSK) !Block
  NBMSK C*2 Numbers of masks
  NOMMSK AMK(15) Tabs -> [AMK]CODMSK =[AWI]NOMMSK (AMSK) !Block
  OBJ AOB Object -> [AOB]ABREV =[AWI]OBJ (AOBJET) !Block
  ROWMSK C*2(15) Sequence
  TRN A*10 Transaction
  TYP M*15 Window type [menu 87: 1=Full screen,2=Dialog box,3=Message box,4=Selecting]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDFLG M*15 Validated flag [menu 1: 1=No,2=Yes]
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWI]UPDUSR (AUTILIS) !Other
  WIN FEN Window -> [AWI]AWI0 =[AWI]WIN (AWINDOW) !Delete
  WINTYP M*15 Window type [menu 923: 1=Miscellaneous,2=Object,3=Inquiry,4=Inquiry criteria,5=Selection table]

## AWINPAR (AWP) - Window parameters
Keys (first = PK; D = duplicates allowed): AWP0 WIN+NUM+NOPAR+PARAM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWP]CREUSR (AUTILIS) !Other
  NOPAR C*2 Parameter no.
  NUM C*3 Number
  PARAM AAR Parameter -> [AAR]CODPAR =[AWP]PARAM (ACTCODPAR) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWP]UPDUSR (AUTILIS) !Other
  VALEUR A*40 Value
  WIN FEN Window -> [AWI]AWI0 =[AWP]WIN (AWINDOW) !Delete

## AWRKHISDES (AWO) - Workflow history
Keys (first = PK; D = duplicates allowed): AWO0 CHRONO+EMAIL; AWO1 LNKHTP (D)
Fields:
  AUUID AUUID Single identifier
  CHRONO VCR Sequence no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWO]CREUSR (AUTILIS) !Other
  EMAIL MAI Email address
  ENVOI M*4 Copy [menu 1: 1=No,2=Yes]
  LNKHTP A*10 Http line
  SUIVI M*20 Milestone [menu 2920: 1=No,2=Yes,3=With signature]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWO]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[AWO]USER (AUTILIS) !Other

## AWRKHISJOI (AWJ) - Workflow history
Keys (first = PK; D = duplicates allowed): AWJ0 CHRONO+JOINUM
Fields:
  AUUID AUUID Single identifier
  CHRONO VCR Sequence no.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWJ]CREUSR (AUTILIS) !Other
  JOINAM FIC*250 Name of attachment
  JOINUM L*8 No. attachment
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWJ]UPDUSR (AUTILIS) !Other

## AWRKHISMES (AWG) - Worksflow message history
Notes: differs in V9.0 P12 (diff: AT3_AWRKHISMES.htm); differs in V10 P1 (diff: ATD_AWRKHISMES.htm)
Keys (first = PK; D = duplicates allowed): AWG0 CHRONO; AWG1 REFGRP+NUMGRP+CHRONO
Fields:
  AUUID AUUID Single identifier
  CATJOI M*15 Category [menu 96: 1=Confidential,2=Internal,3=External,4=External 2]
  CHRONO VCR Sequence no.
  CLEOBJ A*80 Return key
  CONTXT A*250 Return
  CONTXTDSKTOP A*250 Representations
  CONTXTMOBILE A*250 Mobile phone
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWG]CREUSR (AUTILIS) !Other
  DATENV D Issue date
  DEBUG M*4 Debug mode [menu 1: 1=No,2=Yes]
  FLGENV M*4 Sent flag [menu 1: 1=No,2=Yes]
  GRPENV M*4 Grouping [menu 1: 1=No,2=Yes]
  MAIL MAI Sender
  NUMGRP VCR No. of group
  OBJET A*250 Object
  OBJJOI AOB Object -> [AOB]ABREV =[AWG]OBJJOI (AOBJET) !Block
  REFGRP VCR Group reference
  REQIMP M*20 Message importance [menu 7864: 1=Low,2=Normal,3=High]
  REQREC M*4 Request read receipt [menu 1: 1=No,2=Yes]
  TEXTE AC0*5 Text
  TIMENV HM Issue time
  TYPJOI ADI Type of attachment -> [ADI]CODE =902;TYPJOI (ATABDIV) !Block
  TYPMES M*10 Send by server [menu 940: 1=Any,2=Server,3=Client]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWG]UPDUSR (AUTILIS) !Other
  USER AUS Sender -> [AUS]CODUSR =[AWG]USER (AUTILIS) !Block

## AWRKHISSUI (AWS) - Workflow tracking archive
Notes: differs in V9.0 P12 (diff: AT3_AWRKHISSUI.htm); differs in V10 P1 (diff: ATD_AWRKHISSUI.htm)
Keys (first = PK; D = duplicates allowed): AWS0 CHRONO+DEST; AWS1 NUMORG+CHRONO+DEST; AWS2 DEST+CHRONO; AWS3 CHRONO+EMAIL (D); AWS4 NUMGRP+CHRONO+USRTOP (D); AWS5 TYPEVT+CLEOBJ+IDENTGRP+NUMORG+LEVSIG (D); AWS6 CODWRK+CODEVT+FLGSIG+DEST (D)
Fields:
  ABROBJ AOB Object -> [AOB]ABREV =[AWS]ABROBJ (AOBJET) !RTZ
  ACTSIG ADI Answer -> [ADI]CODE =54;ACTSIG (ATABDIV) !Block
  AUUID AUUID Single identifier
  CHRONO VCR Sequence no.
  CLEDEC ID1 Original key
  CLEOBJ ID1 Release key
  CODEVT A*15 Event code
  CODWRK AWA Workflow code -> [AWA]AWA0 =[AWS]CODWRK (AWRKPAR) !Block
  CONTXT A*250 Return icon
  CONTXTDSKTOP A*250 Representations
  CONTXTMOBILE A*250 Mobile phone
  CPY CPY Company -> [CPY]CPY0 =[AWS]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWS]CREUSR (AUTILIS) !Other
  DATENV D Issue date
  DATMAXSIG D Signature leadtime
  DATREL D Reminder date
  DATSIG D Signature date
  DELEGUE M*4 Delegate [menu 1: 1=No,2=Yes]
  DEST AUS Recipient -> [AUS]CODUSR =[AWS]DEST (AUTILIS) !Block
  EMAIL MAI Recipient e-mail
  EMETTEUR AUS Sender -> [AUS]CODUSR =[AWS]EMETTEUR (AUTILIS) !Block
  ENVOI M*10 Send mail [menu 2919: 1=No,2=Yes,3=Copy]
  FLGSIG M*20 Signature flag [menu 2922: 1=Cancelled,2=To be read,3=To be signed,4=Read,5=Signed]
  IDENTGRP ID1 Line identifier
  IDENTREF ID1 Triggering table
  IDENTRET ID1 Identifying return
  LEVSIG C*2 Signature level
  MAIENV MAI Email transmission
  MAISIG MAI Email signature
  NATURE ADI Type of workflow -> [ADI]CODE =50;NATURE (ATABDIV) !Block
  NBRREL C*2 No. reminder
  NBRUSR C*4 No. of signers
  NUMGRP VCR Workflow no.
  NUMORG VCR Origin chrono
  OPERATION A*20 Action on
  REACOD ADI Reason code -> [ADI]CODE =REANUM;REACOD (ATABDIV) !RTZ
  REANUM ADV Reason no. -> [ADV]CODE =[AWS]REANUM (ATABTAB) !Block
  REASON DES Response reason
  TEXSUI A*250 Tracked text
  TIMENV HS Issue time
  TIMSIG HS Signature time
  TYPEVT M*15 Event type [menu 988: 1=Miscellaneous,2=Object,3=Function start,4=Report,5=End of task,6=Task cancellation,7=Time management,8=Import/export,9=Signature,10=Manual]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWS]UPDUSR (AUTILIS) !Other
  USRORG AUS Original recipient -> [AUS]CODUSR =[AWS]USRORG (AUTILIS) !Block
  USRSIG AUS Signer -> [AUS]CODUSR =[AWS]USRSIG (AUTILIS) !Block
  USRSIG1 AUS Signer 1 -> [AUS]CODUSR =[AWS]USRSIG1 (AUTILIS) !Block
  USRSIG2 AUS Signer 2 -> [AUS]CODUSR =[AWS]USRSIG2 (AUTILIS) !Block
  USRSIG3 AUS Signer 3 -> [AUS]CODUSR =[AWS]USRSIG3 (AUTILIS) !Block
  USRSIG4 AUS Signer 4 -> [AUS]CODUSR =[AWS]USRSIG4 (AUTILIS) !Block
  USRSIG5 AUS Signer 5 -> [AUS]CODUSR =[AWS]USRSIG5 (AUTILIS) !Block
  USRSIG6 AUS Signer 6 -> [AUS]CODUSR =[AWS]USRSIG6 (AUTILIS) !Block
  USRSIG7 AUS Signer 7 -> [AUS]CODUSR =[AWS]USRSIG7 (AUTILIS) !Block
  USRSIG8 AUS Signer 8 -> [AUS]CODUSR =[AWS]USRSIG8 (AUTILIS) !Block
  USRSIG9 AUS Signer 9 -> [AUS]CODUSR =[AWS]USRSIG9 (AUTILIS) !Block
  USRTOP AUS First recipient -> [AUS]CODUSR =[AWS]USRTOP (AUTILIS) !Block
  VALCTX1 ID1 Context 1
  VALCTX10 ID1 Context 10
  VALCTX11 ID1 Context 11
  VALCTX12 ID1 Context 12
  VALCTX13 ID1 Context 13
  VALCTX14 ID1 Context 14
  VALCTX15 ID1 Context 15
  VALCTX2 ID1 Context 2
  VALCTX3 ID1 Context 3
  VALCTX4 ID1 Context 4
  VALCTX5 ID1 Context 5
  VALCTX6 ID1 Context 6
  VALCTX7 ID1 Context 7
  VALCTX8 ID1 Context 8
  VALCTX9 ID1 Context 9

## AWRKLNK (AWM) - Data models
Keys (first = PK; D = duplicates allowed): AWM0 MODELE; AWM1 CODSTR+MODELE
Fields:
  ACCSTR AVA Access code
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AWM]CODACT (ACTIV) !Block
  CODSTR ACLA Class code -> [ACLA]ACLA0 =[AWM]CODSTR (ACLASSE) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWM]CREUSR (AUTILIS) !Other
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FCT AFC Function -> [AFC]CODINT =[AWM]FCT (AFONCTION) !Block
  FCYSTR AVA Site
  FLDCPY AFR*20 Company field
  FLDFCY AFR*20 Site field
  FLDLEG AFR*20 Legislation field
  FLGADLV M*4 Deliverable definition [menu 1: 1=No,2=Yes]
  FLGAPH M*4 Template [menu 1: 1=No,2=Yes]
  FLGEXA M*4 Indexing [menu 1: 1=No,2=Yes]
  FLGSTR M*4 Structure [menu 1: 1=No,2=Yes]
  FLGWRK M*4 Workflow [menu 1: 1=No,2=Yes]
  INTITMOD ATX Description
  MODELE AWM Template code -> [AWM]AWM0 =[AWM]MODELE (AWRKLNK) !Delete
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBROPT C*4 No. of options
  OPTCND AFR*50(20) Option condition
  OPTCOD A*1(20) Option code
  OPTERR ATX(20) Error message
  OPTLIB ATX(20) Option title
  TABREF ATB Main table -> [ATB]CODFIC =[AWM]TABREF (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWM]UPDUSR (AUTILIS) !Other

## AWRKPAR (AWA) - Workflow rules
Notes: differs in V9.0 P12 (diff: AT3_AWRKPAR.htm); differs in V10 P1 (diff: ATD_AWRKPAR.htm)
Keys (first = PK; D = duplicates allowed): AWA0 CODE; AWA1 TYPEVT+CODEVT+CODE; AWA2 CATEG+CODE
Fields:
  ABRLIG ABR Abbreviation line
  ALLCATJOI M*4 Each category [menu 1: 1=No,2=Yes]
  ALLTYPJOI M*4 All types [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BAKFCT AFC Return function -> [AFC]CODINT =[AWA]BAKFCT (AFONCTION) !Block
  BAKLNK A*60 Link key
  BAKLNKMOBILE A*250 Keys
  BAKLNKSYRA A*250 Keys
  BAKMEN M*4 Menu return [menu 1: 1=No,2=Yes]
  BAKMOBILE ASW Mobile phone -> [ASW]ASW0 =[AWA]BAKMOBILE (ASHW) !Block
  BAKSYRA ASW Representations -> [ASW]ASW0 =[AWA]BAKSYRA (ASHW) !Block
  CATEG ADI Category -> [ADI]CODE =51;CATEG (ATABDIV) !Block
  CATJOI M*15 Category [menu 96: 1=Confidential,2=Internal,3=External,4=External 2]
  CODE AWA Workflow code -> [AWA]AWA0 =[AWA]CODE (AWRKPAR) !Delete
  CODEVT A*15 Event code
  CONDITION AFR*250(5) Conditions
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWA]CREUSR (AUTILIS) !Other
  DEBUG M*4 Debug mode [menu 1: 1=No,2=Yes]
  ENAACT M*4 Trigger action [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENAMES M*4 Trigger mail [menu 1: 1=No,2=Yes]
  ENASUI M*4 Trigger tracking [menu 1: 1=No,2=Yes]
  FORIMP AFR*80 Importance
  GROUPE A*80 Regrouping lines
  GRPENV M*4 Grouping [menu 1: 1=No,2=Yes]
  INTERV M*4 Message can be edited [menu 1: 1=No,2=Yes]
  INTIT AX3 Description
  JOINT AFR*250 Attached document
  JOIOBJ M*4 Attachment [menu 1: 1=No,2=Yes]
  MODELE AWM Data model -> [AWM]AWM0 =[AWA]MODELE (AWRKLNK) !Block
  NBCOND C*2 No. of conditions
  OBJET AFR*250 Object
  OPERATION A*20 Operations
  REGLE AWR Assignment rule -> [AWR]AWR0 ="";REGLE (AWRKREG) !Block
  REQREC M*4 Request read receipt [menu 1: 1=No,2=Yes]
  RETOUR M*4 Return icon [menu 1: 1=No,2=Yes]
  TABLIG ATB Table line -> [ATB]CODFIC =[AWA]TABLIG (ATABLE) !Block
  TEXLIG AFR*250 Line text
  TEXTE AC0*5 Text
  TRACE M*4 Linked trace file [menu 1: 1=No,2=Yes]
  TYPCND MM*10(5) Type [menu 40: 1=***,2=Header,3=Line]
  TYPDEC M*4 End of transaction [menu 1: 1=No,2=Yes]
  TYPEVT M*15 Event type [menu 988: 1=Miscellaneous,2=Object,3=Function start,4=Report,5=End of task,6=Task cancellation,7=Time management,8=Import/export,9=Signature,10=Manual]
  TYPJOI ADI Type of attachment -> [ADI]CODE =902;TYPJOI (ATABDIV) !Block
  TYPMES M*10 Send by server [menu 940: 1=Any,2=Server,3=Client]
  TYPWRK MM*10 Workflow type [menu 40: 1=***,2=Header,3=Line]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWA]UPDUSR (AUTILIS) !Other

## AWRKPARC (AWC) - Workflow rules (actions)
Keys (first = PK; D = duplicates allowed): AWC0 CODE+NUMACT
Fields:
  ACTION ACT Action code -> [ACT]ACTION =[AWC]ACTION (ACTION) !Block
  AUUID AUUID Single identifier
  CODE AWA Workflow code -> [AWA]AWA0 =[AWC]CODE (AWRKPAR) !Delete
  CODPAR AAR(20) Parameter code -> [AAR]CODPAR =[AWC]CODPAR (ACTCODPAR) !RTZ
  CONACT AFR*250 Conditions
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWC]CREUSR (AUTILIS) !Other
  DECACT MM*20 Triggering [menu 2923: 1=Workflow start,2=Workflow end,3=During signature,4=Line,5=Before line,6=Before group]
  NUMACT C*4 Order information
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWC]UPDUSR (AUTILIS) !Other
  VALPAR A*30(20) Parameter value

## AWRKPARF (AWF) - Workflow rules (signature)
Keys (first = PK; D = duplicates allowed): AWF0 CODE
Fields:
  ACTSIG ADI(10) Answer -> [ADI]CODE =54;ACTSIG (ATABDIV) !Block
  AUUID AUUID Single identifier
  CNDSIG AFR*80(10) Conditions
  CODE AWA Code -> [AWA]AWA0 =[AWF]CODE (AWRKPAR) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWF]CREUSR (AUTILIS) !Other
  DELSIG AFR*80 Due date
  EXPVAL AFR*80(10) Value
  FLDMAJ AFR*20(10) Update field
  FLGSIG M*4 Signature [menu 1: 1=No,2=Yes]
  MODSIG M*4(10) Changeable [menu 1: 1=No,2=Yes]
  NBRSIG C*2 No. of actions
  NBRVAR C*2 No. of values
  OPESIG ADI(10) Action on -> [ADI]CODE =55;OPESIG (ATABDIV) !Block
  REANUM ADV(10) Response reason -> [ADV]CODE =[AWF]REANUM (ATABTAB) !Block
  TEXSUI AFR*250 Tracked text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWF]UPDUSR (AUTILIS) !Other
  VARCTX AFR*80(15) Context

## AWRKPARH (AWH) - Workflow rules (recipient)
Keys (first = PK; D = duplicates allowed): AWH0 CODE
Fields:
  AUUID AUUID Single identifier
  CNDDES AFR*80(10) Condition
  CODE AWA Workflow code -> [AWA]AWA0 =[AWH]CODE (AWRKPAR) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWH]CREUSR (AUTILIS) !Other
  DESTIN AFR*80(10) Recipient
  ENVOI M*10(10) Send mail [menu 2919: 1=No,2=Yes,3=Copy]
  FNCDES M*15(10) Function [menu 233: 1=Managing Director,2=Sales Manager,3=Technical Manager,4=Financial and Legal Manager,5=Site Manager,6=Company manager,7=Manager,8=Staff manager,9=Accountant,10=Other,11=Liquidator,12=Official receiver]
  NATURE ADI(10) Types -> [ADI]CODE =50;NATURE(indice) (ATABDIV) !Block
  NBDEST C*2 Number of recipients
  OPTDEL M*15(10) Delegate option [menu 2918: 1=No,2=All,3=Cascade,4=First available]
  SUIVI M*20(10) Milestone [menu 2920: 1=No,2=Yes,3=With signature]
  TYPDES M*15(10) Type [menu 76: 1=User,2=Business partner]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWH]UPDUSR (AUTILIS) !Other

## AWRKPARX (AWX) - Simplified workflow
Keys (first = PK; D = duplicates allowed): AWX0 CODE
Fields:
  ANDOR M*15(5) Operator [menu 56: 1=And,2=Or]
  AUUID AUUID Single identifier
  CODE AWA Workflow code -> [AWA]AWA0 =[AWX]CODE (AWRKPAR) !Delete
  CODEVT A*10 Event code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWX]CREUSR (AUTILIS) !Other
  DESTIN AFR*80(2) Recipients
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENVOI M*4(2) Send mail [menu 1: 1=No,2=Yes]
  EXP1 AFR*200 Expression
  FLD A*15(5) Field
  FNCDES M*15(2) Function [menu 233: 1=Managing Director,2=Sales Manager,3=Technical Manager,4=Financial and Legal Manager,5=Site Manager,6=Company manager,7=Manager,8=Staff manager,9=Accountant,10=Other,11=Liquidator,12=Official receiver]
  INTIT AX3 Description
  OBJET AFR*250 Object
  OPE M*15(5) Operator [menu 7815: 1=Indifferent,2=Equal to,3=Different,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like,9=Modified,10=Increased,11=Reduced]
  OPERATION A*20 Operations
  RETOUR M*4 Return icon [menu 1: 1=No,2=Yes]
  SUIVI M*4(2) Milestone [menu 1: 1=No,2=Yes]
  TEXTE AC0*5 Text
  TRACE M*4 Linked trace file [menu 1: 1=No,2=Yes]
  TYPDES M*15(2) Type [menu 76: 1=User,2=Business partner]
  TYPEVT M*15 Event type [menu 988: 1=Miscellaneous,2=Object,3=Function start,4=Report,5=End of task,6=Task cancellation,7=Time management,8=Import/export,9=Signature,10=Manual]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWX]UPDUSR (AUTILIS) !Other
  VALEUR AVV*10(5) Value
  VALI A*80(5) Value

## AWRKREG (AWR) - Assignment rules
Keys (first = PK; D = duplicates allowed): AWR0 CPY+REGLE; AWR1 REGLE+CPY; AWR2 MODELE+REGLE+CPY
Fields:
  ABRFLD ABR(10) Abbreviation
  ABRLIG ABR Abbreviation line
  ACS ACS Access code -> [ACS]ACS0 =[AWR]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[AWR]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWR]CREUSR (AUTILIS) !Other
  DEFFLD AFR*30(10) Default value
  EXPFLD AFR*200(10) Criteria
  INTFLD AFR*50(10) Description
  INTIT AX3 Description
  LIBFLD C*4(10) Local menu no.
  LNGFLD DCB*4(10) Length
  LNKFLD MM*15(10) Link [menu 49: 1=No,2=Long,3=Short]
  MODELE AWM Data model -> [AWM]AWM0 =[AWR]MODELE (AWRKLNK) !Block
  NBRFLD ABS Field nb
  NBRUSR C*2 Number of signatures
  OPEFLD MM*15(10) Operator [menu 55: 1=All,2=Equal,3=Not equal to,4=Greater than,5=Greater than or equal to,6=Less than,7=Less than or equal to,8=Like]
  PARFLD AFR*30(10) Parameter
  REGLE AWR Rule code -> [AWR]AWR0 =CPY;REGLE (AWRKREG) !Delete
  SYNFLD MM*15(10) Synthesis operator [menu 2921: 1=Mini,2=Maxi,3=Sum,4=Average]
  TABFLD ATB(10) Table to browse -> [ATB]CODFIC =[AWR]TABFLD (ATABLE) !Block
  TABLIG ATB Table line -> [ATB]CODFIC =[AWR]TABLIG (ATABLE) !Block
  TYPFLD ATY(10) Data type -> [ATY]CODTYP =[AWR]TYPFLD (ATYPE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWR]UPDUSR (AUTILIS) !Other

## AWRKREGVAL (AWV) - User assignment
Keys (first = PK; D = duplicates allowed): AWV0 REGLE+CPY+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[AWV]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWV]CREUSR (AUTILIS) !Other
  FLGFOR M*4 Formula/user [menu 1: 1=No,2=Yes]
  NUMLIG C*4 Line no.
  REGLE AWR Rule code -> [AWR]AWR0 =CPY;REGLE (AWRKREG) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWV]UPDUSR (AUTILIS) !Other
  USER AFR*30 User code act:AWR
  USRDEF AFR*30 User code act:AWR
  VALREG A*30(10) Values

## AWRKTAB (AWK) - Data models
Keys (first = PK; D = duplicates allowed): AWK0 MODELE+NUMLIG
Fields:
  ABRLNK ABR Linked abbreviation
  ABRORI ABR Abbreviation origin
  AUUID AUUID Single identifier
  CLELNK ANX Link key
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWK]CREUSR (AUTILIS) !BSRA
  EXPLNK A*250 Link expression
  EXPSEL AFR*250 Selection
  MODELE AWM Template code -> [AWM]AWM0 =[AWK]MODELE (AWRKLNK) !Delete
  NUMLIG C*2 Line no.
  STRLNK ACLA Class code -> [ACLA]ACLA0 =[AWK]STRLNK (ACLASSE) !Other
  TABLNK ATB Linked table -> [ATB]CODFIC =[AWK]TABLNK (ATABLE) !Block
  TABORI ATB Origin table -> [ATB]CODFIC =[AWK]TABORI (ATABLE) !Block
  TYPLNK M*5 Link type [menu 2916: 1=0,1,2=0,n,3=1,1,4=1,n]
  TYPTAB C*2 Table type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWK]UPDUSR (AUTILIS) !BSRA

## AWRKTRN (AWW) - Workflow workbench
Keys (first = PK; D = duplicates allowed): AWW0 WRKTRN
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[AWW]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AWW]CREUSR (AUTILIS) !Other
  INTIT AX3 Description
  NBRLIG C*3 Number of lines
  NBRMSK C*2 No. of tabs
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AWW]UPDUSR (AUTILIS) !Other
  WRKTRN AWW Transaction code -> [AWW]AWW0 =[AWW]WRKTRN (AWRKTRN) !Delete

## AWRKTRND (AWD) - Workflow workbench
Keys (first = PK; D = duplicates allowed): AWD0 WRKTRN+NUMMSK
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWD]CREUSR (AUTILIS) !Other
  CRISTY AFR*250(5) Condition
  FLDCOL AVA(70) Fields
  FLDINT AX3(70) Titles
  INTLNG AX3 Long title
  INTSHO AX1 Short description
  NBRCOL C*2 No. of columns
  NBRSTY C*2 Number of styles
  NUMMSK C*2 Number
  ORDFLD A*100 Sort order
  SELWRK AFR*250 Filter
  STYLES ASY(5) Style -> [ASY]ASY0 =[AWD]STYLES (ASTYLE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWD]UPDUSR (AUTILIS) !Other
  WRKTRN AWW Transaction code -> [AWW]AWW0 =[AWD]WRKTRN (AWRKTRN) !Delete

## AWRKUSR (AWU) - User delegates
Keys (first = PK; D = duplicates allowed): AWU0 USER+NUMDEL
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AWU]CREUSR (AUTILIS) !Other
  NATURE ADI Type of workflow -> [ADI]CODE =50;NATURE (ATABDIV) !Block
  NUMDEL C*2 Delegate no.
  TYPDEL M*15 Type of delegate [menu 2917: 1=Copy for information,2=With authority,3=Exceptional]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AWU]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[AWU]USER (AUTILIS) !Block
  USRDEL AUS User delegate -> [AUS]CODUSR =[AWU]USRDEL (AUTILIS) !Block
  VLYEND D Validity end date
  VLYSTR D Validity start date

## AWSDL (AXL) - Web services
Keys (first = PK; D = duplicates allowed): AXL0 CWSDL
Fields:
  ABRWSDL A*3 Abbreviation
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AXL]CREUSR (AUTILIS) !Other
  CWSDL A*10 Code
  DGENWSDL D Posting date
  HGENWSDL A*10 Posting time
  LWSDL A*30 Description
  NAMWSDL A*30 Name
  PGENWSDL AUS Validater -> [AUS]CODUSR =[AXL]PGENWSDL (AUTILIS) !Other
  PREFSP A*10 Prefix namespace
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AXL]UPDUSR (AUTILIS) !Other
  WSDLDEF AC0*3 Definition

## AWSDL1 (AX1) - Web services structure
Keys (first = PK; D = duplicates allowed): AX10 CWSDL+TWSDL+NWSDL
Fields:
  ADABR A*4 Abbreviation
  ADCONT A*10 Control
  ADDIM C*4 Dimension
  ADELT M*15 Element type [menu 7801: 1=Mask,2=Element,3=Group,4=Table]
  ADFORM A*30 Format
  ADLON C*4 Length
  ADMSK A*8 Mask
  ADNAM A*10 Name
  ADTYP M*15 Data type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime]
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AX1]CREUSR (AUTILIS) !Other
  CWSDL A*10 Code
  ELTMES A*30 Element
  LNIV C*4 Level
  LON C*4 Length
  MESSERV A*30 Message
  MSKSERV M*4 To generate [menu 1: 1=No,2=Yes]
  NAMMES A*30 Message
  NAMSERV A*30 Web service
  NIV C*4 Level
  NOM A*40 Name
  NOMAF A*40 Name
  NWSDL C*2 Line number
  OPERSERV A*30 Action on
  PARTMES A*30 Component
  TWSDL A*1 Type
  TYP A*30 Type
  TYPSERV A*10 Type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AX1]UPDUSR (AUTILIS) !Other
  VWSDL A*150 Line

## AYTACT (AYA) - Web action
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYA0 FCYCOD+ACTCOD
Fields:
  ACTCOD AYA Action code -> [AYA]AYA0 =FCYCOD;ACTCOD (AYTACT) !Delete
  ACTMAPRET AYA Return map. action -> [AYA]AYA0 =FCYCOD;ACTMAPRET (AYTACT) !Block
  ACTREFRESH M*4 Revision [menu 1: 1=No,2=Yes]
  ACTTYP M*15 Action type [menu 7936: 1=Standard,2=Login,3=Logout]
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYA]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENTSUPBEF M*4 Stat deletion [menu 1: 1=No,2=Yes]
  ENTSUPCOD AYE(10) Entity to delete -> [AYE]AYE0 =FCYCOD;ENTSUPCOD(indice) (AYTENT) !Block
  ENTSUPNBR ABS No.
  FCYCOD AYS Site -> [AYS]AYS0 =[AYA]FCYCOD (AYTFCY) !Block
  FICXML FIC*200 XML file
  INTCOD AYI Interface code -> [AYI]AYI0 =FCYCOD;INTCOD (AYTINT) !Block
  INTIT AX3 Description
  LOGMOD M*4 Journal [menu 1: 1=No,2=Yes]
  OPTOUT MM*15 Return process [menu 7918: 1=Web site field,2=Customization,3=XSL processor]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WSOACT M*15 Activate button [menu 7920: 1=Read,2=Create,3=Delete,4=Save,5=Other]
  WSOACTBTN A*10 Button code
  WSOTYPPAR M*10 Type of parameter [menu 7940: 1=Keys,2=Data]

## AYTADVPAR (AYU) - Advanced setup
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYU0 FCYCOD+OBJTYP+OBJCOD+LIN
Fields:
  AUUID AUUID Single identifier
  CODACT ACV Activity code -> [ACV]CODACT =[AYU]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYU]FCYCOD (AYTFCY) !Block
  LIN C*4 Line no.
  OBJCOD AYR Code
  OBJTYP M*15 Type [menu 7910: 1=None,2=Web sites,3=Web pages,4=Web site profiles,5=Field tokens,6=Entity,7=Block tokens,8=Conditioned block tokens,9=Web action,10=Dynamic links,11=Special field tokens,12=Web message,13=Interface,14=Advanced param.,15=List of values]
  PARCOD A*20 Parameter
  PARVAL AYV Parameter value
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTBASKED (AYK) - Basket line
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYK0 NUM+BASKLIN
Fields:
  AUUID AUUID Single identifier
  BAKFLG M*4 Selected [menu 1: 1=No,2=Yes]
  BASKLIN C*4 Line number
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AYK]CREUSR (AUTILIS) !Other
  ITMDES DES
  ITMREF A*30 Product
  NUM VCR Document no.
  PRIX MD1 Price 1
  QTY QTY Quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AYK]UPDUSR (AUTILIS) !Other

## AYTDOC (AYY) - Html document
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYY2 LAN+DOCCOD; AYY0 DOCCOD+LAN; AYY1 CAT+BRWX3
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CAT ADI Category -> [ADI]CODE =920;CAT (ATABDIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES A*30 Description
  DESCR A*200 Description
  DOCCOD AYY Html document -> [AYY]AYY2 =[AYY]DOCCOD (AYTDOC) !BSRA
  LAN LAN Language -> [TLA]TLA0 =[AYY]LAN (TABLAN) !Block
  TEXTE AC0*10 Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTELTBLC (AYB) - Blocks
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYB0 FCYCOD+BLCCOD
Fields:
  AUUID AUUID Single identifier
  BLCCOD AYB Block code -> [AYB]AYB0 =FCYCOD;BLCCOD (AYTELTBLC) !Delete
  BLCNBRLIN C*4 No. lines/block
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYB]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENTCOD AYE Entity code -> [AYE]AYE0 =FCYCOD;ENTCOD (AYTENT) !Block
  FCYCOD AYS Site -> [AYS]AYS0 =[AYB]FCYCOD (AYTFCY) !Block
  INTIT AX3 Description
  INTOPTIMI M*20 Interface optimization [menu 7933: 19 values, see local-menus.md]
  LINNBROBC C*4 No. cells/line
  LINSTY A*200(5) Style per line
  LINSTYNBR ABS No.
  OPTDSY M*15 No data [menu 7915: 1=Do not display anything,2=HTML code without token,3=HTML code with token]
  SELDYNALT M*4 Modifiable selection [menu 1: 1=No,2=Yes]
  SELTYP M*15 Selection type [menu 7916: 1=None,2=Code,3=Query,4=Last link clicked,5=Detail]
  SRTDYNALT M*4 Modif sorting [menu 1: 1=No,2=Yes]
  SRTTYP M*15 Sorting type [menu 7917: 1=None,2=Field,3=Random]
  TYP M*15 Block type [menu 7914: 1=Single-record,2=Multi-record]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTELTBLCW (AYW) - Conditioned blocks
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYW0 FCYCOD+BLCWHNCOD
Fields:
  AUUID AUUID Single identifier
  BLCCOD AYB Block -> [AYB]AYB0 =FCYCOD;BLCCOD (AYTELTBLC) !Block
  BLCPAG M*15 Pagination criteria [menu 7919: 1=First page,2=Last page,3=Other pages]
  BLCWHNCOD AYW Cond. block code -> [AYW]AYW0 =FCYCOD;BLCWHNCOD (AYTELTBLCW) !Delete
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYW]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLKCOD AYL Dynamic link -> [AYL]AYL0 =FCYCOD;DLKCOD (AYTELTDLK) !Block
  FCYCOD AYS Site -> [AYS]AYS0 =[AYW]FCYCOD (AYTFCY) !Block
  INTIT AX3 Description
  PAGCOD AYG Web page -> [AYG]AYG0 =FCYCOD;PAGCOD (AYTPAG) !Block
  PRFCOD AYD(5) Web site profile -> [AYD]AYD0 =FCYCOD;PRFCOD(indice) (AYTPRF) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WHNACT M*20 Action [menu 7921: 1=Hide block,2=Dispaly block]
  WHNTYP M*20 Criteria type [menu 7922: 1=Formula,2=Empty Block,3=Paging of a Block,4=Last dynamic link used,5=Previous page,6=User logged in,7=Profile,8=Empty gadget,9=Selected line,10=Current page]

## AYTELTDLK (AYL) - Dynamic links
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYL0 FCYCOD+DLKCOD
Fields:
  ACTCOD AYA Web action -> [AYA]AYA0 =FCYCOD;ACTCOD (AYTACT) !Block
  ACTVERCHP M*4 Control web fields [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYL]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLKCOD AYL Dynamic link code -> [AYL]AYL0 =FCYCOD;DLKCOD (AYTELTDLK) !Delete
  DLKERR AYG Page if error -> [AYG]AYG0 =FCYCOD;DLKERR (AYTPAG) !Block
  ENTCOD AYE Entity code -> [AYE]AYE0 =FCYCOD;ENTCOD (AYTENT) !Block
  FCYCOD AYS Site -> [AYS]AYS0 =[AYL]FCYCOD (AYTFCY) !Block
  INTIT AX3 Description
  LOGMOD M*4 Journal [menu 1: 1=No,2=Yes]
  PAGCOD AYG Web page -> [AYG]AYG0 =FCYCOD;PAGCOD (AYTPAG) !Block
  PAGSAM M*4 Indentical page [menu 1: 1=No,2=Yes]
  PAR AYR(10) Parameter
  PARNBR ABS No.
  PARVAL AYV(10) Parameter value
  POSTFORCE M*4 Force http post [menu 1: 1=No,2=Yes]
  SELBLCOPT M*25 Sel main block [menu 7924: 1=Replaces the selection of the main block,2=Is added to the selection of the main block,3=Is added to all the current selections]
  SELTYP M*15 Selection type [menu 7916: 1=None,2=Code,3=Query,4=Last link clicked,5=Detail]
  SRTTYP M*15 Sorting type [menu 7917: 1=None,2=Field,3=Random]
  SUIDLK AYL(5) Dyn. chained link -> [AYL]AYL0 =FCYCOD;SUIDLK(indice) (AYTELTDLK) !Block
  SUINBR ABS No.
  SUIPRG M*4 Programmed sequence [menu 1: 1=No,2=Yes]
  SUIPRGENT AYE Entity -> [AYE]AYE0 =FCYCOD;SUIPRGENT (AYTENT) !Block
  SUIPRGFLD AYF Field -> [AYF]AYF0 =FCYCOD;SUIPRGFLD (AYTELTFLD) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTELTFLD (AYF) - Field token
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYF0 FCYCOD+FIECOD
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYF]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENASPE M*4 Special fields [menu 1: 1=No,2=Yes]
  EXT A*5 Extension
  EXTFCYOPT M*4 Site extension [menu 1: 1=No,2=Yes]
  FCYCOD AYS Site -> [AYS]AYS0 =[AYF]FCYCOD (AYTFCY) !Block
  FIECOD AYF Field code -> [AYF]AYF0 =FCYCOD;FIECOD (AYTELTFLD) !Delete
  FLADLK AYL Dynamic link -> [AYL]AYL0 =FCYCOD;FLADLK (AYTELTDLK) !Block
  FLAINT AYI Interface code -> [AYI]AYI0 =FCYCOD;FLAINT (AYTINT) !Block
  FLASIZ C*4 Text file size
  FLATIT M*4 Display graph [menu 1: 1=No,2=Yes]
  FLATYPVUE APP Type of view -> [APP]APP0 =1;FLATYPVUE (APTLPAR) !Block
  FLAVUE APV Dashboard view -> [APV]APV0 =[AYF]FLAVUE (APTLVW) !Block
  INTIT AX3 Description
  LANCOD LAN Web language -> [TLA]TLA0 =[AYF]LANCOD (TABLAN) !Block act:AYL
  LANFMT A*30 Format act:AYL
  LANNBR ABS No.
  LSTMEN AYC List of values -> [AYC]AYC0 =FCYCOD;LSTMEN (AYTMEN) !Block
  NOLIB MNL Local menu no.
  RESRAC M*20 Root directory [menu 7937: 1=None,2=HTML design,3=X_FILAPP,4=X_FILES,5=X_TEND]
  RESSUBREP FIC*200 Relative path
  TYP M*15 Data type [menu 7931: 1=Text,2=Integer,3=Decimal,4=Currency,5=Date,6=Image access,7=Attachment access,8=Local menu,9=Flash]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALDEF M*10 Default value [menu 7941: 1=Standard,2=Constant,3=Description]
  VALVAL A*250 Value

## AYTELTSPE (AYX) - Special fields
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYX0 FCYCOD+SPXCOD
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYX]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYX]FCYCOD (AYTFCY) !Block
  SPXCOD A*60 Code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTENT (AYE) - Entity
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYE0 FCYCOD+ENTCOD
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYE]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENTCOD AYE Entity code -> [AYE]AYE0 =FCYCOD;ENTCOD (AYTENT) !Delete
  FCYCOD AYS Site -> [AYS]AYS0 =[AYE]FCYCOD (AYTFCY) !Block
  INTCOD AYI Interface -> [AYI]AYI0 =FCYCOD;INTCOD (AYTINT) !Block
  INTIT AX3 Description
  TYP M*15 Type [menu 7913: 1=Action,2=Session,3=Data access]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTFCY (AYS) - Websites
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYS0 FCYCOD
Fields:
  AUUID AUUID Single identifier
  BRWDEG M*4 Report [menu 1: 1=No,2=Yes]
  CODACT ACV Activity code -> [ACV]CODACT =[AYS]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTSDEF M*4 Default values [menu 1: 1=No,2=Yes]
  CTSDIC M*4 Web dictionary [menu 1: 1=No,2=Yes]
  CTSHTM M*4 HTML pages [menu 1: 1=No,2=Yes]
  DIRLAN M*4 Language folder [menu 1: 1=No,2=Yes]
  EXTDEFIMG A*5 Image extension
  EXTDEFPJ A*5 Attachment extension
  FCYCOD AYS Site -> [AYS]AYS0 =[AYS]FCYCOD (AYTFCY) !Delete
  FCYPUB M*4 Publish site [menu 1: 1=No,2=Yes]
  HCEAPP M*8 APP directory [menu 7942: 1=Never,2=Always,3=1 mn,4=15 mns,5=30 mns,6=1 h,7=4 hs,8=8 hs,9=12 hs,10=1 day,11=7 days]
  HCEDEF M*4 Default values [menu 1: 1=No,2=Yes]
  HCEFIL M*8 File directory [menu 7942: 1=Never,2=Always,3=1 mn,4=15 mns,5=30 mns,6=1 h,7=4 hs,8=8 hs,9=12 hs,10=1 day,11=7 days]
  HCEFLA M*8 Flash directory [menu 7942: 1=Never,2=Always,3=1 mn,4=15 mns,5=30 mns,6=1 h,7=4 hs,8=8 hs,9=12 hs,10=1 day,11=7 days]
  HCEHTM M*8 HTML directory [menu 7942: 1=Never,2=Always,3=1 mn,4=15 mns,5=30 mns,6=1 h,7=4 hs,8=8 hs,9=12 hs,10=1 day,11=7 days]
  HCEXTD M*8 Web directory [menu 7942: 1=Never,2=Always,3=1 mn,4=15 mns,5=30 mns,6=1 h,7=4 hs,8=8 hs,9=12 hs,10=1 day,11=7 days]
  IMGDEF FIC*200 Default image
  INTIT AX3 Description
  LANADS LAN Folder language -> [TLA]TLA0 =[AYS]LANADS (TABLAN) !Block act:AYL
  LANCOD LAN Web language -> [TLA]TLA0 =[AYS]LANCOD (TABLAN) !Block act:AYL
  LANDEF M*4 Default language [menu 1: 1=No,2=Yes] act:AYL
  LANFMTCUR A*20 Currency format act:AYL
  LANFMTDAT A*30 Date format act:AYL
  LANFMTDEC A*10 Decimal format act:AYL
  LANFMTINT A*10 Whole nbr format act:AYL
  LANNBR ABS No.
  LNKADS AYO(5) Web service pool -> [AYO]AYO0 =[AYS]LNKADS (AYTPOOWEB) !Block
  LNKADSDEF M*4(5) Pool by default [menu 1: 1=No,2=Yes]
  LNKBUSINT M*4(5) Internal bus [menu 1: 1=No,2=Yes]
  LNKNBR ABS No.
  LOCFIL M*15 File directory [menu 7939: 1=X3 server,2=Web X3 server]
  LOCFLA M*15 Flash directory [menu 7939: 1=X3 server,2=Web X3 server]
  LOCHTM M*15 HTML directory [menu 7939: 1=X3 server,2=Web X3 server]
  LOGMOD M*4 Journal [menu 1: 1=No,2=Yes]
  MAICOD MAI(5) Webmaster email
  MCEFLG M*4 Site under maintenance [menu 1: 1=No,2=Yes]
  PAGERR AYG Error page -> [AYG]AYG0 =FCYCOD;PAGERR (AYTPAG) !Block
  PAGLOG AYG Identification page -> [AYG]AYG0 =FCYCOD;PAGLOG (AYTPAG) !Block
  PAGMCE AYG Maintenance page -> [AYG]AYG0 =FCYCOD;PAGMCE (AYTPAG) !Block
  PAGRECNX AYG Reconnection page -> [AYG]AYG0 =FCYCOD;PAGRECNX (AYTPAG) !Block
  PAGSTR AYG Home page -> [AYG]AYG0 =FCYCOD;PAGSTR (AYTPAG) !Block
  PAR AYR(10) Parameter
  PARNBR ABS No.
  PARVAL AYV(10) Parameter value
  PRFENA M*4 Manage profiles [menu 1: 1=No,2=Yes]
  PRODEF MM*15 Protocol [menu 7911: 1=Http (standard),2=Https (secure),3=Web site]
  SCTROO M*15 Root directory [menu 7937: 1=None,2=HTML design,3=X_FILAPP,4=X_FILES,5=X_TEND]
  SCTSUBREP FIC*200 Relative path
  TIMALL DCB*14 Date time
  TIMAYA DCB*14 Date time
  TIMAYB DCB*14 Date time
  TIMAYC DCB*14 Date time
  TIMAYD DCB*14 Date time
  TIMAYE DCB*14 Date time
  TIMAYF DCB*14 Date time
  TIMAYG DCB*14 Date time
  TIMAYI DCB*14 Date time
  TIMAYL DCB*14 Date time
  TIMAYM DCB*14 Date time
  TIMAYO DCB*14 Not used
  TIMAYS DCB*14 Date time
  TIMAYU DCB*14 Date time
  TIMAYW DCB*14 Date time
  TIMAYX DCB*14 Date time
  TIMPDT DCB*14(5) Prod time stamp
  TIMPER DCB*14(5) Perso time stamp
  TOOLMOD M*4 Tools [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRTIMOUT C*4 Session timeout (mn.)

## AYTFRM (AYZ) - Form
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYZ0 FRMCOD; AYZ1 TYP+FRMCOD
Fields:
  AUUID AUUID Single identifier
  CMT AC0*4 Comment
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHEURE HS Time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYZ]FCYCOD (AYTFCY) !Other
  FRMCOD AYZ Form -> [AYZ]AYZ0 =FRMCOD (AYTFRM) !Delete
  MAICOD MAI Email transmission
  PARCOD A*20(40) Parameter
  PARNBR C*4 No. of parameters
  PARVAL A*50(40) Parameter value
  PCT AB0*4 Image
  STATUT M*20 Status [menu 7927: 19 values, see local-menus.md]
  TTL A*250 Title
  TYP ADI Form type -> [ADI]CODE =917;TYP (ATABDIV) !Block
  TYPBLB AT Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTINT (AYI) - Interface
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYI0 FCYCOD+INTCOD; AYI1 WEBSRCCOD (D)
Fields:
  ACSMOD M*4 Protected access [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYI]CODACT (ACTIV) !Block
  CODFIC ATB Table -> [ATB]CODFIC =[AYI]CODFIC (ATABLE) !Block
  CODVUE AVW View -> [AVW]AVW0 =[AYI]CODVUE (AVIEW) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DSYERR M*4 Error dis. [menu 1: 1=No,2=Yes]
  DSYINF M*4 Information dis. [menu 1: 1=No,2=Yes]
  DSYWRN M*4 Warning dis. [menu 1: 1=No,2=Yes]
  FCYCOD AYS Site -> [AYS]AYS0 =[AYI]FCYCOD (AYTFCY) !Block
  INTCOD AYI Interface code -> [AYI]AYI0 =FCYCOD;INTCOD (AYTINT) !Delete
  INTIT AX3 Description
  INVISIBLE M*4 Invisible fields [menu 1: 1=No,2=Yes]
  LNKADS A*10 Web service pool
  LNKADSDEF M*4 Pool by default [menu 1: 1=No,2=Yes]
  OBJET AOB Object -> [AOB]ABREV =[AYI]OBJET (AOBJET) !Other
  OPTIMI M*20(10) Optimization [menu 7933: 19 values, see local-menus.md]
  OPTIMINBR C*4 No.
  PRG ADC Processing
  SUBPRG ASU Subprograms
  TYP M*20 Interface type [menu 7912: 21 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VARIANTE A*10 Transaction
  WEBSRCCOD AWE Publication name

## AYTLINES (AYN) - Lines by types
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYN0 FCYCOD+LINCODTYP+LINCOD+LINTYP+LINNUM
Fields:
  ALLSTAR M*4 Char. * for all [menu 1: 1=No,2=Yes]
  ANDOR M*15 Operator [menu 56: 1=And,2=Or]
  AUUID AUUID Single identifier
  BRKLFT C*4 No. left bracket
  BRKRGT C*4 No. right bracket
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AYN]CREUSR (AUTILIS) !Other
  CRIOBY M*4 Mandatory criteria [menu 1: 1=No,2=Yes]
  DLKCOD AYL Dynamic link -> [AYL]AYL0 =FCYCOD;DLKCOD (AYTELTDLK) !Block
  ENTCOD AYE Entity -> [AYE]AYE0 =FCYCOD;ENTCOD (AYTENT) !Block
  FCYCOD AYS Site -> [AYS]AYS0 =[AYN]FCYCOD (AYTFCY) !Block
  FIECOD AYF Field -> [AYF]AYF0 =FCYCOD;FIECOD (AYTELTFLD) !Block
  FIELNKENT AYE Linked entity -> [AYE]AYE0 =FCYCOD;FIELNKENT (AYTENT) !Block
  INTFLD A*12 Interface field
  INTFLDGRP APU Interface group
  INTFLDIND C*4 Interf. field occ
  INTTYPMLT M*4 Multiple type rel. [menu 1: 1=No,2=Yes]
  LINCOD AYN Code in capital letters
  LINCODSTD AYN Code
  LINCODTYP C*4 Code type
  LINNUM C*4 Number
  LINTYP C*4 Line type
  MENADI ADI Misc table code -> [ADI]CODE =MENADV;MENADI (ATABDIV) !Block
  MENADISHO M*4 Short description [menu 1: 1=No,2=Yes]
  MENADV ADV Miscellaneous table -> [ADV]CODE =[AYN]MENADV (ATABTAB) !Block
  MENCHP C*4 Chapter
  MENCHPNUM C*4 Number
  MENCOD L*8 Code
  MENCODPAR L*8 Parent code
  MENLIBORI M*15 Description [menu 7934: 1=Message,2=Miscellaneous table]
  MENTYP C*2 Key type
  OPE M*15 Operator [menu 7926: 1=Indifferent,2==,3=<>,4=>,5=>=,6=<,7=<=,8=Starts with,9=Contains,10=Does not contain]
  PARCOD AYF Parameter -> [AYF]AYF0 =FCYCOD;PARCOD (AYTELTFLD) !Block
  SRTORD M*10 Sort order [menu 90: 1=Ascending,2=Descending]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AYN]UPDUSR (AUTILIS) !Other
  VA2BLCCOD AYB Block -> [AYB]AYB0 =FCYCOD;VA2BLCCOD (AYTELTBLC) !Block
  VA2FIECOD AYF Field -> [AYF]AYF0 =FCYCOD;VA2FIECOD (AYTELTFLD) !Block
  VA2FIELNKE AYE Entity -> [AYE]AYE0 =FCYCOD;VA2FIELNKE (AYTENT) !Block
  VALBLCCOD AYB Block -> [AYB]AYB0 =FCYCOD;VALBLCCOD (AYTELTBLC) !Block
  VALENTCOD AYE Entity -> [AYE]AYE0 =FCYCOD;VALENTCOD (AYTENT) !Block
  VALEUR AYR Value
  VALFIECOD AYF Field -> [AYF]AYF0 =FCYCOD;VALFIECOD (AYTELTFLD) !Block
  VALFIELNKE AYE Linked entity -> [AYE]AYE0 =FCYCOD;VALFIELNKE (AYTENT) !Block
  VALTYP M*15 Value type [menu 7925: 1=Constant,2=Field token,3=Web field,4=Web field mandat.,5=Access code,6=Entry,7=Block]

## AYTMEN (AYC) - List of values
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYC0 FCYCOD+MENCOD
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYC]CODACT (ACTIV) !Block
  CPTCOD L*8 Sequence number
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEPFLG M*4 Dependency management [menu 1: 1=No,2=Yes]
  DEPNIV C*4 Level
  FCYCOD AYS Site -> [AYS]AYS0 =[AYC]FCYCOD (AYTFCY) !Block
  FIECOD AYF(10) Field -> [AYF]AYF0 =FCYCOD;FIECOD (AYTELTFLD) !Block
  FIENBR ABS No. of fields
  GESADISHO M*4 Short description [menu 1: 1=No,2=Yes]
  GESADV ADV Miscellaneous table -> [ADV]CODE =[AYC]GESADV (ATABTAB) !Block
  GESCHP C*4 Chapter
  GESOPT M*15 Management [menu 7935: 1=Manual,2=Automatic,3=Batch]
  GESORI M*15 Type [menu 7934: 1=Message,2=Miscellaneous table]
  INTIT AX3 Description
  MENCOD AYC List code -> [AYC]AYC0 =FCYCOD;MENCOD (AYTMEN) !Delete
  RESRAC M*20 Root directory [menu 7937: 1=None,2=HTML design,3=X_FILAPP,4=X_FILES,5=X_TEND]
  RESSUBFIC FIC*200 File
  RESTIMSTP M*4 Check update [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTMES (AYM) - Messages
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYM0 FCYCOD+MESCOD; AYM1 CAT+BRWX3
Fields:
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CAT A*20 Category
  CODACT ACV Activity code -> [ACV]CODACT =[AYM]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYM]FCYCOD (AYTFCY) !Block
  INTIT AX3 Description
  LANCHP C*4 Chapter
  LANNUM C*4(2) Number
  MESCOD AYM Message code -> [AYM]AYM0 =FCYCOD;MESCOD (AYTMES) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## AYTPAG (AYG) - Web pages
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYG0 FCYCOD+PAGCOD
Fields:
  ACSMOD M*4 Protected access [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BLCBCK AYB Backgrd block -> [AYB]AYB0 =[AYG]BLCBCK (AYTELTBLC) !Block
  BLCMAI AYB Main block -> [AYB]AYB0 =[AYG]BLCMAI (AYTELTBLC) !Block
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYG]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYG]FCYCOD (AYTFCY) !Block
  FICDEF FIC*200 File by dafualt
  FICLAN FIC*200 File act:AYL
  FICLANCOD LAN Web language -> [TLA]TLA0 =[AYG]FICLANCOD (TABLAN) !Block act:AYL
  FICLANNBR ABS No.
  INTIT AX3 Description
  LOGMOD M*4 Journal [menu 1: 1=No,2=Yes]
  PAGCOD AYG Web page -> [AYG]AYG0 =FCYCOD;PAGCOD (AYTPAG) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEBPRO M*30 Protocol [menu 7911: 1=Http (standard),2=Https (secure),3=Web site]

## AYTPOOWEB (AYO) - Web services pools
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYO0 POOCOD; AY1 POOX3+POOCOD
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[AYO]CREUSR (AUTILIS) !Other
  POOCOD AYO Pool code -> [AYO]AYO0 =[AYO]POOCOD (AYTPOOWEB) !Delete
  POODES DES Description
  POOSEC M*4 Secured connection [menu 1: 1=No,2=Yes]
  POOTIMOUT L*8 Time-out
  POOX3 A*200 X3 pool code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[AYO]UPDUSR (AUTILIS) !Other
  USR AUS User code -> [AUS]CODUSR =[AYO]USR (AUTILIS) !Other
  USRLAN LAN Language -> [TLA]TLA0 =[AYO]USRLAN (TABLAN) !Other
  USRMDP A*10 Password

## AYTPRF (AYD) - Web site profile
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYD0 FCYCOD+PRFCOD
Fields:
  ALLACS M*4 Global access [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BRWX3 AY9 Browser key
  CODACT ACV Activity code -> [ACV]CODACT =[AYD]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FCYCOD AYS Site -> [AYS]AYS0 =[AYD]FCYCOD (AYTFCY) !Block
  INTCOD AYI(80) Interface -> [AYI]AYI0 =FCYCOD;INTCOD(indice) (AYTINT) !Block
  INTIT AX3 Description
  INTNBR ABS No.
  PAGCOD AYG(99) Web page -> [AYG]AYG0 =FCYCOD;PAGCOD(indice) (AYTPAG) !Block
  PAGERR AYG Error page -> [AYG]AYG0 =FCYCOD;PAGERR (AYTPAG) !Block act:AYT
  PAGNBR ABS No.
  PRFCOD AYD Profile code -> [AYD]AYD0 =FCYCOD;PRFCOD (AYTPRF) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRTIMOUT C*4 Session timeout (mn.)

## AYTPRFUSR (AYH) - Safe X3 WAS profile
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYH0 CODPRF
Fields:
  AUUID AUUID Single identifier
  CODPRF AYH Profile code -> [AYH]AYH0 =[AYH]CODPRF (AYTPRFUSR) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AYH]CREUSR (AUTILIS) !Other
  FCYXTDCOD AYS(20) Website -> [AYS]AYS0 =FCYXTDCOD (AYTFCY) !Delete
  INTPRF AX3 Description
  NBFCY C*4 Number
  PRFXTDCOD AYD(20) Web site profile -> [AYD]AYD0 =FCYXTDCOD;PRFXTDCOD (AYTPRF) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AYH]UPDUSR (AUTILIS) !Other

## AYTTEST (AYT) - Tests
Notes: activity code AYT
Keys (first = PK; D = duplicates allowed): AYT0 COD1+COD2
Fields:
  AUUID AUUID Single identifier
  AXXRUB1 AXX Standard text
  AXXRUB2 AXX Standard text
  CAT1 A*10 Category
  CAT2 A*10 Category
  CAT3 A*10 Category
  CAT4 A*10 Category
  CMT AC0*4 Comment
  COD1 A*20 Code 1
  COD2 A*20 Code 2
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREHEURE HS Time
  CREUSR A*5 Creation user
  DECIM DCB*9.2 Decimal
  MAICOD MAI Email transmission
  PARCOD A*20(40) Parameter
  PARNBR C*4 No. of parameters
  PARVAL A*50(40) Parameter value
  PCT AB0*5 Image
  PRIX MD1 Price 1
  RUB1 A*25 Text
  RUB2 A*25 Text
  STATUT M*20 Status [menu 7927: 19 values, see local-menus.md]
  TTL A*250 Title
  TYP ADI Form type -> [ADI]CODE =917;TYP (ATABDIV) !Block
  TYPBLB AT Type
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## BID (BID) - Bank ID statement
Notes: differs in V9.0 P12 (diff: AT3_BID.htm)
Keys (first = PK; D = duplicates allowed): BID0 BPATYP+BPANUM+BIDNUM+BPAADD; BID2 BPATYP+BPANUM+BPAADD (D); BID1 BPATYP+BPANUM+BVRNUM (D)
Fields:
  ACCNONREI M*4 Nonresident [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BICCOD A*11 BIC code act:VII
  BIDNUM BID Bank account number
  BIDNUMFLG M*4 By default [menu 1: 1=No,2=Yes]
  BNF PAB Beneficiary
  BPAADD ADR Address
  BPANUM BPA Entity
  BPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  BVRNUM A*11 ISR customer no. act:KSW
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[BID]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[BID]CRY (TABCOUNTRY) !Block
  CUR CUR Currency -> [TCU]TCU0 =[BID]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  IBAN A*4 IBAN prefix
  MIDBICCOD A*11 Intermediary bank BIC code act:VII
  MIDCRY CRY Intermediary bank country -> [TCY]TCY0 =[BID]MIDCRY (TABCOUNTRY) !Block act:VII
  MIDPAB1 PAB Intermediary bank name act:VII
  MIDPAB2 PAB Intermediary bank address 1 act:VII
  MIDPAB3 PAB Intermediary bank address 1 act:VII
  MIDPAB4 PAB Intermediary bank address 3 act:VII
  PAB1 PAB Paying bank
  PAB2 PAB Paying bank 2 act:VII
  PAB3 PAB Paying bank 3 act:VII
  PAB4 PAB Paying bank 4 act:VII
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[BID]UPDUSR (AUTILIS) !Other

## BPADDRESS (BPA) - Addresses
Keys (first = PK; D = duplicates allowed): BPA0 BPATYP+BPANUM+BPAADD
Fields:
  ADRVAL M*4 Validated [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPAADDFLG M*4 By default [menu 1: 1=No,2=Yes]
  BPAADDLIG ADL(3) Address line
  BPABID BID By default
  BPADES DES Description
  BPANUM BPA Entity
  BPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[BPA]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[BPA]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  EXPNUM L*8 Export number
  EXTNUM A*30 External identifier
  FAX TEL Fax
  FCYWEB A*250 Website
  MOB TEL Mobile phone
  POSCOD POS Postal code
  SAT SAT County
  TEL TEL(5) Telephone
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[BPA]UPDUSR (AUTILIS) !Other
  WEB MAI(5) Internet address

## CCMIMPPRH (CCMIPRH) - Impact analysis-Purchase req
Notes: activity code CCMNC; differs in V9.0 P12 (diff: AT3_CCMIMPPRH.htm)
Keys (first = PK; D = duplicates allowed): CCMPRH0 CRID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Created on
  CREUSR AUS Created by -> [AUS]CODUSR =[CCMIPRH]CREUSR (AUTILIS) !Other
  CRID CCMCRID Request ID
  FOLDCUR CUR Base currency -> [TCU]TCU0 =[CCMIPRH]FOLDCUR (TABCUR) !Block
  HOLD M*4 Hold [menu 1: 1=No,2=Yes]
  IMPACTANAL C*4 Impact analysis
  IMPLEMENT M*4 Planning complete [menu 1: 1=No,2=Yes]
  PRHAMT MD8 Total amount +tax
  PRHAMTEX MD8 Total amount -tax
  PRHPLASTA M*15 Plan status [menu 2045: 1=In planning,2=Being implemented,3=Completed,4=Not applicable]
  PRHQTY QTY Total quantity
  PRHREQNO L*8 Number of requests
  PRHSUP L*8 Number of suppliers
  TOTALLINES L*8 Lines
  UPDDATTIM ADATIM Updated on
  UPDUSR AUS Updated by -> [AUS]CODUSR =[CCMIPRH]UPDUSR (AUTILIS) !Other

## COMPANY (CPY) - Company
Notes: differs in V9.0 P12 (diff: AT3_COMPANY.htm); differs in V10 P1 (diff: ATD_COMPANY.htm)
Keys (first = PK; D = duplicates allowed): CPY0 CPY; CPY1 LEG+CPY (D)
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[CPY]ACCCOD (GACCCODE) !BSRA
  ACCCUR CUR Accounting currency -> [TCU]TCU0 =[CPY]ACCCUR (TABCUR) !Block
  ACM GCM Account core model -> [GCM]GCM0 =[CPY]ACM (GACM) !Block
  AGTPCP C*4 Collection agent act:KAG
  AUSFINSRV A*10 Financial department act:KAT
  AUUID AUUID Single identifier
  BDFECOCOD PBDECO Economic reason -> [PBDECO]PBDECO0 =BDFECOCOD;LEG (PBDECOCOD) !Block
  BIDNUM BID Bank acct. number
  BPAADD ADR Default address
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CNTNAM AIN Contact -> [AIN]AIN0 =[CPY]CNTNAM (CONTACTCRM) !Block
  COMMTYPE M*20(9) Communication type [menu 2427: 1=SAFT,2=Electronic invoice] act:EFAT
  CPY CPY Company -> [CPY]CPY0 =[CPY]CPY (COMPANY) !Delete
  CPYLEGFLG M*4 Legal company [menu 1: 1=No,2=Yes]
  CPYLOG A*10 Legal form
  CPYNAM NAM Company name
  CPYSHO SHO Short description
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[CPY]CREUSR (AUTILIS) !Other
  CRN CRN Company tax ID number
  CRY CRY Country -> [TCY]TCY0 =[CPY]CRY (TABCOUNTRY) !Block
  DACDIE M*4 Enter dimensions ascending [menu 1: 1=No,2=Yes] act:ANA
  DCLDIRBALPAY M*4 Direct decl. site bal [menu 1: 1=No,2=Yes]
  DIE DIE Dimension type code -> [DIE]DIE0 =[CPY]DIE (GDIE) !Block act:ANA
  DIVCOD A*20 Division code act:KUS
  EECNUM EEC Tax number
  ENDDAT D(9) End date act:EFAT
  GERCODELMA5 A*11(8) ELMA5 sender ID act:KDE
  GERDEFVAL M*4(8) Default value [menu 1: 1=No,2=Yes] act:KDEAT
  GEREECNUM A*20(8) Tax number act:KDEAT
  GERPTP A*20 Participant code act:KDE
  GERTAXCEN BPR(8) Tax center -> [BPR]BPR0 =[CPY]GERTAXCEN (BPARTNER) !Block act:KDEAT
  GERTAXIDT A*20(8) Tax identifier act:KDEAT
  GRUCOD A*10 Consolidation act:CSL
  KACT A*20 Cy's pr. activity act:KPO
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MAIFCY FCY Main site -> [FCY]FCY0 =[CPY]MAIFCY (FACILITY) !Block
  NAF NAF SIC code
  NID NID Identification no.
  NUMADD C*3 Additional number act:KDE
  OBYDIE M*4 Mandatory dimension type [menu 1: 1=No,2=Yes] act:ANA
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Block
  PORAMTITMINV DCB*9.2 Simp inv itm act:KPO
  PORAMTSERINV DCB*9.2 Simp inv ser act:KPO
  PORCPYACT ADI Company activity -> [ADI]CODE =395;PORCPYACT (ATABDIV) !Block act:KPO
  PORCPYACTDET ADI Detailed activity -> [ADI]CODE =395;PORCPYACTDET (ATABDIV) !Block act:KPO
  PORCPYACTTYP M*15 Activity type [menu 3646: 1=Other,2=Retail] act:KPO
  PORCTFACN A*9 Certified expert act:KPO
  PORDCLPER M*30 Periodicity [menu 2226: 1=Day,2=Week,3=Month,4=Quarter,5=Year] act:KPO
  PORFINDPR A*9 Financial department act:KPO
  PORHQR M*15 Head office [menu 3618: 1=Main,2=Annex R-1,3=Annex R-2] act:KPO
  PORLRC A*9 Legal representative act:KPO
  PORRESFISCDA CPY Invoicing company -> [CPY]CPY0 =[CPY]PORRESFISCDA (COMPANY) !Block act:KPO
  PORSIMINVISS M*25 Simplified invoice [menu 1: 1=No,2=Yes] act:KPO
  RGCAMT DCB*11.4 Registered capital act:EUR
  RGCCUR CUR Capital currency -> [TCU]TCU0 =[CPY]RGCCUR (TABCUR) !Block act:EUR
  RTZFLG M*4 Retained [menu 1: 1=No,2=Yes] act:KIT
  SCINUM A*35 SEPA Creditor ID act:SDD
  SFINUM SFI Disc. invoicing element -> [SFI]SFI0 =[CPY]SFINUM (SFOOTINV) !Block act:LTA
  SPABPCTSD DCB*13.2 Customer threshold act:KSP
  SPABPSTSD DCB*13.2 Supplier threshold act:KSP
  SPAYEATSD DCB*13.2 Yearly 347 threshold act:KSP
  SSTCPY A*25 Sage Sales Tax company act:LTA
  SSTTAXACT M*4 Activation [menu 1: 1=No,2=Yes] act:LTA
  STAFED ADI Federal state -> [ADI]CODE =80;STAFED (ATABDIV) !Block act:KDE
  STRDAT D(9) Start date act:EFAT
  STRPER D First fiscal year
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[CPY]UPDUSR (AUTILIS) !Other
  VACCPY A*10 Tax rule act:KAG

## CONTACT (CNT) - Contacts
Notes: differs in V10 P1 (diff: ATD_CONTACT.htm)
Keys (first = PK; D = duplicates allowed): CNT0 BPATYP+BPANUM+CCNCRM; CNT1 CCNCRM+BPATYP+BPANUM; CNT2 CCNCRM (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPANUM BPA Entity
  BPATYP M*15 Entity type [menu 943: 1=Business partner,2=Company,3=Site,4=User,5=Accounts,6=Leads,7=Building,8=Place]
  CCNCRM AIN Code -> [AIN]AIN0 =[CNT]CCNCRM (CONTACTCRM) !Block
  CNTFNC M*15 Function [menu 233: 1=Managing Director,2=Sales Manager,3=Technical Manager,4=Financial and Legal Manager,5=Site Manager,6=Company manager,7=Manager,8=Staff manager,9=Accountant,10=Other,11=Liquidator,12=Official receiver]
  CNTMSS ADI Role -> [ADI]CODE =906;CNTMSS (ATABDIV) !RTZ
  CNTSRV A*30 Department
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[CNT]CREUSR (AUTILIS) !Other
  DPO M*4 Data protection [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FAX TEL Fax
  MOB TEL Mobile phone
  TEL TEL Telephone
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[CNT]UPDUSR (AUTILIS) !Other
  WEB MAI Email

## CONTACTCRM (AIN) - Contact relationships
Notes: differs in V10 P1 (diff: ATD_CONTACTCRM.htm)
Keys (first = PK; D = duplicates allowed): AIN0 CNTNUM; AIN1 CNTFULNAM (D); AIN2 CNTTYP+CNTNUM
Fields:
  ADD ADL(3) Address
  AUUID AUUID Single identifier
  CNTBIR D Date of birth
  CNTCSP ADI Category -> [ADI]CODE =907;CNTCSP (ATABDIV) !Block
  CNTEMA MAI Email
  CNTETS TEL Telephone
  CNTFAX TEL Fax
  CNTFBDMAG M*4 Mailing prohibited [menu 1: 1=No,2=Yes]
  CNTFNA A*20 First name
  CNTFULNAM A*60 Search key
  CNTLAN LAN Language -> [TLA]TLA0 =[AIN]CNTLAN (TABLAN) !Block
  CNTLNA NAM Last name
  CNTMOB TEL Mobile phone
  CNTNUM AIN Code -> [AIN]AIN0 =[AIN]CNTNUM (CONTACTCRM) !Delete
  CNTTTL M*20 Title [menu 941: 1=Mr,2=Mrs,3=Ms]
  CNTTYP M*15 Type [menu 7811: 1=Standard,2=Lead]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[AIN]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[AIN]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  EXPNUM L*8 Export number
  RDEPITNUM A*10 Residence permit act:KMA
  SAT SAT County
  SSCNUM DCB*19.8 Social security fund act:KMA
  UIDCRDNUM A*10 ID card number act:KMA
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[AIN]UPDUSR (AUTILIS) !Other
  ZIP POS Postal code

## FACGROUP (FGR) - Site grouping
Keys (first = PK; D = duplicates allowed): FGR0 CPY+FCY; FGR1 FCY+CPY
Fields:
  AUUID AUUID Single identifier
  CPY AGF Company -> [AGF]AGF0 =[FGR]CPY (AGRPFCY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[FGR]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[FGR]FCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[FGR]UPDUSR (AUTILIS) !Other

## FACILITY (FCY) - Sites
Notes: differs in V9.0 P12 (diff: AT3_FACILITY.htm); differs in V10 P1 (diff: ATD_FACILITY.htm)
Keys (first = PK; D = duplicates allowed): FCY0 FCY; FCY1 LEGCPY+FCY
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GCACFCY;ACCCOD;[V]GSUPCLE (GACCCODE) !Block act:CPT
  AUUID AUUID Single identifier
  BIDNUM BID Bank acct. number
  BPAADD ADR Default address
  BPADCL A*10 Declaring site address act:HRPAY
  BPASGE A*10 Headquarters address act:HRPAY
  BPTNUM A*10 Carrier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHEF A*10 Supervisors act:HRPAY
  CLLCVT A*10 Collective agreement act:HRPAY
  CNTDDS A*10 TDS contact act:HRPAY
  CNTNAM AIN Contact -> [AIN]AIN0 =[FCY]CNTNAM (CONTACTCRM) !Block
  CODCRA A*10 CRAM code act:HRPAY
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[FCY]CREUSR (AUTILIS) !Other
  CRN CRT Site registration number
  CRY CRY Country -> [TCY]TCY0 =[FCY]CRY (TABCOUNTRY) !Block
  DADFCY FCY DAS2 site -> [FCY]FCY0 =[FCY]DADFCY (FACILITY) !Other act:DAS
  DADFLG M*4 DAS2 [menu 1: 1=No,2=Yes] act:DAS
  DIE A*10 Dimension type code act:ANA
  ENDHOU HM End act:TRSNE
  FCY FCY Site -> [FCY]FCY0 =[FCY]FCY (FACILITY) !Delete
  FCYNAM NAM Name
  FCYSHO SHO Short description
  FINFLG M*4 Accounting [menu 1: 1=No,2=Yes]
  FINRSPFCY FCY Financial site -> [FCY]FCY0 =[FCY]FINRSPFCY (FACILITY) !Other
  FLGAPP C*4 Apprenticeship tax act:HRPAY
  FLGFOR C*4 Prof. training act:HRPAY
  FLGPEC C*4 Housing levy act:HRPAY
  GEOCOD GEO Geographic code act:KUS
  HRMDADFCY A*10 DADS site act:HRPAY
  HRMDADFLG C*4 DADS act:HRPAY
  HRMPAYBAN A*10 Bank act:HRPAY
  HRMTAXWAG C*4 Tax/salaries act:HRPAY
  INSCTYFLG A*1 City interior flag act:KUS
  IVYFCY FCY Stock count site -> [FCY]FCY0 =[FCY]IVYFCY (FACILITY) !Other act:FAS
  IVYFLG M*4 Count [menu 1: 1=No,2=Yes] act:FAS
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  LEGCPY CPY Legal company -> [CPY]CPY0 =[FCY]LEGCPY (COMPANY) !Block
  MFGFLG M*4 Manufacturing [menu 1: 1=No,2=Yes]
  MFGWRH WRH Cons wareh -> [WRH]WRH0 =[FCY]MFGWRH (WAREHOUSE) !Block act:WRH
  MFPWRH WRH WO receipt warehouse -> [WRH]WRH0 =[FCY]MFPWRH (WAREHOUSE) !Block act:WRH
  MFRWRH WRH Reintegration whs -> [WRH]WRH0 =[FCY]MFRWRH (WAREHOUSE) !Block act:WRH
  NAF NAF SIC code
  PAYBAN BAN Payment bank -> [BAN]BAN0 =[FCY]PAYBAN (BANK) !Block
  PAYFLG C*4 Payroll act:HRPAY
  PRF A*10 Profile act:HRPAY
  PURFLG M*4 Purchase [menu 1: 1=No,2=Yes]
  RCPWRH WRH Receipt warehouse -> [WRH]WRH0 =[FCY]RCPWRH (WAREHOUSE) !Block act:WRH
  REGPRH C*4 Industrial tribunal act:HRPAY
  RSKWRK A*10 Risk act:HRPAY
  RTNWRH WRH Deliv return whs -> [WRH]WRH0 =[FCY]RTNWRH (WAREHOUSE) !Block act:WRH
  SALFLG M*4 Sales [menu 1: 1=No,2=Yes]
  SCCWRH WRH Sb-c cons warehouse -> [WRH]WRH0 =[FCY]SCCWRH (WAREHOUSE) !Block act:WRH
  SCOWRH WRH Sub-ctrt ship wareh -> [WRH]WRH0 =[FCY]SCOWRH (WAREHOUSE) !Block act:WRH
  SECPRH C*4 Derogation polling subdivision act:HRPAY
  SHIWRH WRH Shipping warehouse -> [WRH]WRH0 =[FCY]SHIWRH (WAREHOUSE) !Block act:WRH
  SPAOPEIGIC M*4 IGIC operations [menu 1: 1=No,2=Yes] act:KSP
  SRV A*10 Department act:HRPAY
  STRHOU HM Start act:TRSNE
  TRAWRH WRH Int rcpt warehouse -> [WRH]WRH0 =[FCY]TRAWRH (WAREHOUSE) !Block act:WRH
  TRFWRH WRH Int issue warehouse -> [WRH]WRH0 =[FCY]TRFWRH (WAREHOUSE) !Block act:WRH
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[FCY]UPDUSR (AUTILIS) !Other
  UVYCOD UVY Unavailable -> [TUV]UVY0 =[FCY]UVYCOD (TABUNAVAIL) !Block
  UVYDAY M*4(7) Unavail. (everyday) [menu 1: 1=No,2=Yes]
  WRHFLG M*4 Warehouse [menu 1: 1=No,2=Yes]
  WRHGES M*4 Warehouse management [menu 1: 1=No,2=Yes] act:WRH

## GTABACC (GTC) - Inquiry screens
Keys (first = PK; D = duplicates allowed): GTC0 CNSCOD+COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[GTC]ACS (ACCCOD) !Block
  AFFGRA M*15 Default display [menu 2936: 1=Table,2=Graph]
  AUUID AUUID Single identifier
  CNSCOD ACN Inquiry type -> [ACN]ACN0 =[GTC]CNSCOD (ACONSULT) !Delete
  COD GTC Code -> [GTC]GTC0 =CNSCOD;COD (GTABACC) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[GTC]CREUSR (AUTILIS) !Other
  DAC C*4(80) Input
  DEFGRA M*15 Default graph [menu 2933: 1=Bars,2=Lines,3=Areas,4=Sectors]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  FLD AVA(80) Field
  FSHGRA M*15 Representation [menu 2939: 1=Multiple,2=Cumulation,3=Comparison,4=Month,5=Week,6=Day]
  GRA M*15(80) Graph type [menu 2937: 1=Value,2=Default,3=Description,4=None]
  INTIT AX3 Description
  NBRCOL C*2 No. of fixed columns
  NBRFLD C*2 Field nb
  NBRLIG C*4 Number of lines
  POSGRA M*15 Position [menu 2931: 1=To the right,2=To the left,3=Above,4=Below]
  REP M*15(80) Representation [menu 2938: 1=Default,2=Bar,3=Line]
  REPGRA M*15 Representation [menu 2930: 1=Character,2=Character or graph,3=Character and graph,4=Graph]
  TYPGRA M*15 Type [menu 2932: 1=Simple graph,2=Multiple graph,3=Planning calendar,4=XSL,5=Gantt,6=Query tool]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[GTC]UPDUSR (AUTILIS) !Other

## PARSTA1 (PS1) - Statistical triggers
Keys (first = PK; D = duplicates allowed): PS10 COD
Fields:
  ABRLNK ABR(10) Abbreviation
  AUUID AUUID Single identifier
  CLELNK ANX(10) Link key
  COD PS1 Code -> [PS1]PS10 =[PS1]COD (PARSTA1) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[PS1]CODACT (ACTIV) !Block
  CPYFLD AVA Company field
  CPYTBL ABR Table
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation author -> [AUS]CODUSR =[PS1]CREUSR (AUTILIS) !Other
  CRI AFR*80(5) Criteria
  DATFLD AVA Date field
  DATTBL ABR Table
  EXPLNK AFR*60(10) Link expression
  EXPNUM L*8 Export number
  FCYFLD AVA Site field
  FCYTBL ABR Table
  INTIT AX3 Description
  INTSHO AX1 Short description
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRCRI C*2 Number
  NBRTBL C*2 Number of tables
  NBRVAR C*2 Number
  RLGTBL ATB Triggering table -> [ATB]CODFIC =[PS1]RLGTBL (ATABLE) !Block
  TBL ATB(10) Linked tables -> [ATB]CODFIC =[PS1]TBL (ATABLE) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change author -> [AUS]CODUSR =[PS1]UPDUSR (AUTILIS) !Other
  VARCUR AFR*30(10) Currency
  VARFOR AFR*160(10) Expression
  VARINTIT AX3(10) Description
  VARNAM AVA(10) Variable

## PARSTA2 (PS2) - Statistical parameters
Keys (first = PK; D = duplicates allowed): PS20 COD; PS21 UPDCOD (D)
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[PS2]ACS (ACCCOD) !Block
  AMTFRM AFR*60(10) Formulas
  AUUID AUUID Single identifier
  COD PS2 Code -> [PS2]PS20 =[PS2]COD (PARSTA2) !Delete
  CODACT ACV Activity code -> [ACV]CODACT =[PS2]CODACT (ACTIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation author -> [AUS]CODUSR =[PS2]CREUSR (AUTILIS) !Other
  CRI AFR*200(5) Criteria
  CUMFRM M*4(10) Totals [menu 986: 1=Normal,2=Rolling total,3=% of total,4=% accumulated]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FLDGRP A*4 Group act:STT
  FLDIND C*4 Index act:STT
  FLDINTIT AX3 Description act:STT
  FLDLNG DCB*9.2 Length act:STT
  FLDLON C*4 Length act:STT
  FLDNAM AVA Field act:STT
  FLDPOS C*4 Position act:STT
  FLDTYP M*15 Type [menu 30: 1=Local menu,2=Short integer,3=Long integer,4=Decimal,5=Floating,6=Double,7=Alphanumeric,8=Date,9=Image file,10=Text file,11=UUID,12=Datetime] act:STT
  FMTFRM DCB*8(10) Format
  FONCTION AFC Function -> [AFC]CODINT =[PS2]FONCTION (AFONCTION) !Delete
  INTIT AX3 Description
  INTITFRM AX3(10) Description
  INTSHO AX1 Short description
  LSTDAT D Update date
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  NBRFLD C*2 Field nb
  NBRFRM C*2 No. formulas
  OBJ AOB Object -> [AOB]ABREV =[PS2]OBJ (AOBJET) !Block
  PERPRG ADC Processing
  PERTYP M*15 Periodicity [menu 52: 1=Daily,2=Weekly,3=2-week period,4=Monthly,5=Quarterly,6=Yearly,7=Decade]
  RLG PS1 Trigger -> [PS1]PS10 =[PS2]RLG (PARSTA1) !Block
  RPT ARP Report -> [ARP]ARP0 =[PS2]RPT (AREPORT) !Block
  SCRDEF GTC Default screen -> [GTC]GTC0 ="STA";SCRDEF (GTABACC) !Block
  TBL ATB Table -> [ATB]CODFIC =[PS2]TBL (ATABLE) !Block act:STT
  TBLABR ABR Abbreviation act:STT
  TIM C*4 Data retention days
  TYP M*15 Type [menu 51: 1=Real time,2=Batch]
  UPDCOD A*5 Update code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDLEV M*15 Level [menu 45: 1=Folder,2=Company,3=Site]
  UPDUSR AUS Change author -> [AUS]CODUSR =[PS2]UPDUSR (AUTILIS) !Other
  VLYEND D Validity end date
  VLYSTR D Validity start date

## PARSTALIG (PSL) - Statistical report line parameters
Keys (first = PK; D = duplicates allowed): PSL0 COD+NUMLIG
Fields:
  AMTFOR AFR*250 Formulas
  AUUID AUUID Single identifier
  CNV M*4 Conversion [menu 1: 1=No,2=Yes]
  COD PS2 Code -> [PS2]PS20 =[PSL]COD (PARSTA2) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSL]CREUSR (AUTILIS) !Other
  DEVDES AFR*250 Destination currency
  DEVORG AFR*250 Source currency
  FRTFLG M*4 Forecast [menu 1: 1=No,2=Yes]
  INTITVAR AXX Amounts
  NUMLIG C*2 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSL]UPDUSR (AUTILIS) !Other
  VARNAM A*10 Variable

## POSCOD (POS) - Postal codes
Keys (first = PK; D = duplicates allowed): POS0 CRY+POSCOD+POSCTY+POSCTYCOD; POS1 CRY+POSCTY+POSCOD (D); POS2 CRY+POSCTYSEA+POSCOD (D)
Fields:
  AUUID AUUID Single identifier
  BURDIS A*40 Distributor office act:KFR
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[POS]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[POS]CRY (TABCOUNTRY) !Block
  EXPNUM L*8 Export number
  GEOCOD GEO Geographic code act:KUS
  POSCOD POS Postal code
  POSCTY CTY City
  POSCTYCOD A*10 Municipality code
  POSCTYSEA A*40 City (search)
  POSUPDFLG A*1 Flag
  SATCOD SAT Subdivision
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[POS]UPDUSR (AUTILIS) !Other

## PRTSCRWRK (PSW) - Screen print work
Keys (first = PK; D = duplicates allowed): PSW0 CREUSR+PRONUM+PRONUMSEQ+RECCOD+RECSEQ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[PSW]CREUSR (AUTILIS) !Other
  LIN A*250 Data
  PRONUM A*10 Process number
  PRONUMSEQ L*8 Sequence number
  PRTFLG M*4 Flag [menu 1: 1=No,2=Yes]
  RECCOD L*8 Code
  RECSEQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSW]UPDUSR (AUTILIS) !Other

## STAT (SAT) - Statistics
Keys (first = PK; D = duplicates allowed): SAT0 COD+CPY+FCY+DAT+CRI1+CRI2+CRI3+CRI4+CRI5+CRI6+CRI7+CRI8
Fields:
  AMT DCB*11.2 Amounts act:STA
  AUUID AUUID Single identifier
  COD A*10 Code
  CPY CPY Company -> [CPY]CPY0 =[SAT]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SAT]CREUSR (AUTILIS) !Other
  CRI1 A*20 Criteria act:ST1
  CRI2 A*20 Criteria act:ST2
  CRI3 A*20 Criteria act:ST3
  CRI4 A*20 Criteria act:ST4
  CRI5 A*20 Criteria act:ST5
  CRI6 A*20 Criteria act:ST6
  CRI7 A*20 Criteria act:ST7
  CRI8 A*20 Criteria act:ST8
  DAT D Date
  DES1 DES Description act:ST1
  DES2 DES Description act:ST2
  DES3 DES Description act:ST3
  DES4 DES Description act:ST4
  DES5 DES Description act:ST5
  DES6 DES Description act:ST6
  DES7 DES Description act:ST7
  DES8 DES Description act:ST8
  FCY FCY Site -> [FCY]FCY0 =[SAT]FCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SAT]UPDUSR (AUTILIS) !Other

## STATPRV (SAP) - Statistical forecasts
Keys (first = PK; D = duplicates allowed): SAP0 COD+CPY+FCY+DAT+CRI1+CRI2+CRI3+CRI4+CRI5+CRI6+CRI7+CRI8
Fields:
  AMT DCB*11.2 Amounts act:STA
  AUUID AUUID Single identifier
  COD PS2 Code -> [PS2]PS20 =[SAP]COD (PARSTA2) !Delete
  CPY CPY Company -> [CPY]CPY0 =[SAP]CPY (COMPANY) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SAP]CREUSR (AUTILIS) !Other
  CRI1 A*20 Criteria act:ST1
  CRI2 A*20 Criteria act:ST2
  CRI3 A*20 Criteria act:ST3
  CRI4 A*20 Criteria act:ST4
  CRI5 A*20 Criteria act:ST5
  CRI6 A*20 Criteria act:ST6
  CRI7 A*20 Criteria act:ST7
  CRI8 A*20 Criteria act:ST8
  DAT D Date
  FCY FCY Site -> [FCY]FCY0 =[SAP]FCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SAP]UPDUSR (AUTILIS) !Other

## TABCHANGE (TCH) - Currency rate table
Keys (first = PK; D = duplicates allowed): TCH0 CHGTYP+CURDEN+CUR+CHGSTRDAT; TCH1 CHGTYP+CURDEN+CHGSTRDAT+CUR
Fields:
  AUUID AUUID Single identifier
  CHGDIV RCU Divisor
  CHGRAT RCU Rate
  CHGSTRDAT D Rate date
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TCH]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TCH]CUR (TABCUR) !Block
  CURDEN CUR Destination currency -> [TCU]TCU0 =[TCH]CURDEN (TABCUR) !Block
  REVCOURS RCU Reverse
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TCH]UPDUSR (AUTILIS) !Other

## TABCOEFF (TCO) - Coefficients table
Keys (first = PK; D = duplicates allowed): TCO0 UOM1+UOM2
Fields:
  AUUID AUUID Single identifier
  COEAX1 AX1 Short description
  COEAX2 AX3 Description
  COEUOM COE Coefficient
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TCO]CREUSR (AUTILIS) !Other
  REV M*4 Reverse [menu 1: 1=No,2=Yes]
  UOM1 UOM Unit 1 -> [TUN]TUN0 =[TCO]UOM1 (TABUNIT) !Block
  UOM2 UOM Unit 2 -> [TUN]TUN0 =[TCO]UOM2 (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TCO]UPDUSR (AUTILIS) !Other

## TABCOUAFF (TCA) - Sequence No assignments
Keys (first = PK; D = duplicates allowed): TCA0 MODULE+LEG+CPY
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM(30) Sequence number -> [ANM]ANM0 =[TCA]CODNUM (ACODNUM) !Block
  CPY CPY Company -> [CPY]CPY0 =[TCA]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4(30) Manual sequence no. [menu 1: 1=No,2=Yes]
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABCOUNTRY (TCY) - Country table
Notes: differs in V9.0 P12 (diff: AT3_TABCOUNTRY.htm); differs in V10 P1 (diff: ATD_TABCOUNTRY.htm)
Keys (first = PK; D = duplicates allowed): TCY0 CRY
Fields:
  ADRCODFMT A*30 Address format
  ADRNAM A*20(3) Header address
  AUUID AUUID Single identifier
  BANLNG C*4 Length of bank
  BIDCLS FEN Bank detail window -> [AWI]AWI0 =[TCY]BIDCLS (AWINDOW) !Block
  BIDCRY A*30 Print format
  BIDCTL M*4 Bank control [menu 1: 1=No,2=Yes]
  BIDFMT A*30 Bank acct. no. fmt.
  CINSEE A*5 Federal ID code
  CONTINENT ADI Continent -> [ADI]CODE =918;CONTINENT (ATABDIV) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TCY]CREUSR (AUTILIS) !Other
  CRNFMT A*30 Company tax ID no. form
  CRNFMTFLG M*4 Company tax ID no. form [menu 1: 1=No,2=Yes]
  CRNOBL M*4 Company tax ID mandatory [menu 1: 1=No,2=Yes]
  CRTFMT A*30 Site tax ID number format
  CRTFMTFLG M*4 Site tax ID number format [menu 1: 1=No,2=Yes]
  CRTOBL M*4 Site tax ID mandatory [menu 1: 1=No,2=Yes]
  CRY CRY Country -> [TCY]TCY0 =[TCY]CRY (TABCOUNTRY) !Delete
  CRYDES AXX Name
  CRYVATNUM A*3 Tax number
  CTLPRG ADC Control script
  CTYCODFMT A*30 City format
  CTYNUMFMT A*30 City code format
  CTYUPP M*4 Upper-case letters [menu 1: 1=No,2=Yes]
  CUR CUR Currency -> [TCU]TCU0 =[TCY]CUR (TABCUR) !Block
  EECCOD A*3 Intrastat country code
  EECDAT D EU entry date
  EECDATOUT D EU withdrawal date
  EECFLG M*4 EU member [menu 1: 1=No,2=Yes]
  EECFMT A*30 VAT format
  EECFMTFLG M*4 VAT format [menu 1: 1=No,2=Yes]
  ETAT M*15 Subdivision entry [menu 7831: 1=None,2=Subdivision 1,3=Subdivision 2]
  ETATCTL M*4 Subdivision control [menu 1: 1=No,2=Yes]
  ETATFLG M*4 Subdivision 1 [menu 1: 1=No,2=Yes]
  ETATFLG2 M*4 Subdivision 2 [menu 1: 1=No,2=Yes]
  ETATFMT A*30 Subdivision format
  ETATFMT2 A*30 Subdivision format
  ETATNAM AX3 Subdivision title
  ETATNAM2 AX3 Subdivision title
  FLGDUE M*4 Involved in DUE [menu 1: 1=No,2=Yes]
  FLGSEPA M*10 SEPA area [menu 1: 1=No,2=Yes]
  FLIBAN M*4 IBAN management [menu 1: 1=No,2=Yes]
  ISO A*2 ISO-3166-1 alpha-2
  ISOA3 A*3 ISO-3166-1 alpha-3
  ISONUM A*3 ISO-3166-1 numeric
  LAN LAN Language -> [TLA]TLA0 =[TCY]LAN (TABLAN) !Block
  MINZIP C*2 Controlled length
  NAFFMT A*30 SIC code format
  NAFFMTFLG M*4 SIC code format [menu 1: 1=No,2=Yes]
  NIDFMT A*30 Unique number
  NIDFMTFLG M*4 Ident format [menu 1: 1=No,2=Yes]
  PABFMT A*30 Domicile format
  POSCODCRY A*30 Print format
  POSCODCTL M*4 Postal code control [menu 1: 1=No,2=Yes]
  POSCODFMT A*30 Postal code format
  POSOBL M*4 Mandatory postal code [menu 1: 1=No,2=Yes]
  SOCNUMFLG1 C*4 SS no. format act:FHRPA
  SOCNUMFLG2 C*4 SS no. format 2 act:FHRPA
  SOCNUMFMT A*10 SS no. format act:FHRPA
  SOCNUMFMT2 A*10 SS no. format 2 act:FHRPA
  SUBDIVFMT A*30 State format
  TELFMT A*30 Phone number format
  TELREG A*10 Control
  TELTCY A*10 Control
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TCY]UPDUSR (AUTILIS) !Other

## TABCUR (TCU) - Currency table
Keys (first = PK; D = duplicates allowed): TCU0 CUR
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =[V]GCACCUR;ACCCOD;[V]GSUPCLE (GACCCODE) !Block act:CPT
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TCU]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[TCU]CUR (TABCUR) !Delete
  CURDES DES
  CURENDDAT D Currency end date
  CURFMT1 A*10 Format 11.2
  CURFMT2 A*10 Format 6.2
  CURFMT3 A*10 Format 13.2
  CURRND DCB*5.5 Rounding
  CURSHO SHO
  CURSYM A*10 Monetary symbol
  DECNBR C*1 Number of decimals
  DIE DIE Dimension type code -> [DIE]DIE0 =[TCU]DIE (GDIE) !Block act:ANA
  EURDAT D Euro changeover date
  EURFLG M*4 Euro [menu 1: 1=No,2=Yes]
  EURRAT DCB*11 Euro rate
  INTDES AX3 Description
  INTSHO AX1 Short description
  ISOCOD A*3 ISO code
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TCU]UPDUSR (AUTILIS) !Other

## TABFOR (TFO) - Formula table
Keys (first = PK; D = duplicates allowed): TFO0 FORTYP+FORCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TFO]CREUSR (AUTILIS) !Other
  DES AX3 Description
  DESSHO AX1 Short description
  FORCOD FOR Formula code -> [TFO]TFO0 =FORTYP;FORCOD (TABFOR) !Other
  FORFOR AFF*250(20) Formula
  FORNUM A*3 Formula type
  FORTYP M*15 Formula type [menu 213: 56 values, see local-menus.md]
  LEG ADI(20) Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TFO]UPDUSR (AUTILIS) !Other

## TABFORLEG (TFOLEG) - Formulas per legislation
Keys (first = PK; D = duplicates allowed): TFOLEG0 FORCOD+LEG
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TFOLEG]CREUSR (AUTILIS) !Other
  DES AX3 Description
  DESSHO AX1 Short description
  FORCOD TFOLEG Formula code -> [TFOLEG]TFOLEG0 =FORCOD;LEG (TABFORLEG) !Delete
  FORFOR AFF*250 Formula
  FORNUM A*3 Formula type
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TFOLEG]UPDUSR (AUTILIS) !Other

## TABLAN (TLA) - Language table
Notes: differs in V9.0 P12 (diff: AT3_TABLAN.htm)
Keys (first = PK; D = duplicates allowed): TLA0 LAN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TLA]CREUSR (AUTILIS) !Other
  INTDES AX3 Description
  INTSHO AX1 Short description
  LAN LAN Language -> [TLA]TLA0 =[TLA]LAN (TABLAN) !Delete
  LANCNV M*15 Conversion [menu 201: 1=No Conversion,2=French,3=English,4=German,5=Italian,6=Spanish,7=Portuguese,8=Turkish]
  LANCON M*4 Connection language [menu 1: 1=No,2=Yes]
  LANISO A*10 ISO code
  LANMAIN LAN Primary language -> [TLA]TLA0 =[TLA]LANMAIN (TABLAN) !Block
  LANRPL LAN Backup language -> [TLA]TLA0 =[TLA]LANRPL (TABLAN) !Block
  LANSTD M*4 Standard language [menu 1: 1=No,2=Yes]
  LANUNI M*4 Unicode language [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TLA]UPDUSR (AUTILIS) !Other

## TABSUBDIV (ATU) - Geographic subdivisions
Keys (first = PK; D = duplicates allowed): ATU0 CRY+TYP+COD
Fields:
  AUUID AUUID Single identifier
  COD SAT Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[ATU]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[ATU]CRY (TABCOUNTRY) !Delete
  CRYTYP A*10 Key
  INTIT AXX Description
  TYP M*15 Subdivision [menu 7831: 1=None,2=Subdivision 1,3=Subdivision 2]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[ATU]UPDUSR (AUTILIS) !Other

## TABUNIT (TUN) - Table of units of measure
Keys (first = PK; D = duplicates allowed): TUN0 UOM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[TUN]CREUSR (AUTILIS) !Other
  DES AX3 Description
  DESSHO AX1 Short description
  UOM UOM Unit -> [TUN]TUN0 =[TUN]UOM (TABUNIT) !Delete
  UOMDEC C*1 Decimals
  UOMSYM A*5 Symbol
  UOMTYP M*15 Unit type [menu 230: 1=Length,2=Area,3=Volume,4=Weight,5=Time,6=Each,7=Packing,8=Other]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[TUN]UPDUSR (AUTILIS) !Other

