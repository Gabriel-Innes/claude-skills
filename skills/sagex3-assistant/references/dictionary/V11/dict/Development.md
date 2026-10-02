<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Development module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## ABATABTD2 (A22) - Batch server (recurring tasks)
Keys (first = PK; D = duplicates allowed): ABD0 CODABT+CODTAC+LIG+NUM
Fields:
  AUUID AUUID Single identifier
  CODABT ABA Recurring task code -> [ABA]CODABT =[A22]CODABT (ABATABT) !Delete
  CODTAC ABT Task code -> [ABT]CODTAC =[A22]CODTAC (ABATTAC) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[A22]CREUSR (AUTILIS) !Other
  DEB A*15(80) Start values
  FIN A*30(80) End values
  LIG C*3 Line number
  NUM C*4 Number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[A22]UPDUSR (AUTILIS) !Other

## ABATRQT2 (A11) - Batch server (queries)
Keys (first = PK; D = duplicates allowed): NUMREQ NUMREQ; PRIO DAT+HEURE+NUMREQ
Fields:
  AUUID AUUID Single identifier
  CODABT ABA Recurring task code -> [ABA]CODABT =[A11]CODABT (ABATABT) !Delete
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[A11]CREUSR (AUTILIS) !Other
  DAT D Date
  DEB A*15(80) Start values
  DFIN D End date
  DOSSIER ADS Folder -> [ADS]DOSSIER =[A11]DOSSIER (ADOSSIER) !Delete
  EPUR M*4 Purge [menu 1: 1=No,2=Yes]
  ETAT A*12 Processing
  FIN A*30(80) End values
  FLAG M*15 Status [menu 21: 1=Standby,2=In progress,3=Finished,4=Held,5=Kill,6=Canceled,7=Error,8=Overdue,9=Warning]
  FLGV3 C*4 V3 flag
  FRQ L*8 Frequency (min)
  FRQFIN HM End time
  GRP ABG Group -> [ABG]ABG0 =[A11]GRP (ABATGRP) !Delete
  HDEB HS Start time
  HEURE HM Time
  HFIN HS Time
  IMPETX C*2 Printer
  JOB FIC*30 Batch file
  MESSAGE M*4 User message [menu 1: 1=No,2=Yes]
  MONO M*4 Single-user [menu 1: 1=No,2=Yes]
  MOTINT DES Reason for interruption
  NUMGRP L*8 Order no.
  NUMREQ L*8 Query no.
  ONE M*4 One single query [menu 1: 1=No,2=Yes]
  PRIO C*2 Priority
  PROCESS A*10 Process no.
  SERVICE A*10 Port
  TACHE ABT Task code -> [ABT]CODTAC =[A11]TACHE (ABATTAC) !Delete
  TIMOUT L*8 Time-out
  TYPTAC M*15 Task type [menu 20: 1=Processing,2=Script]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[A11]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[A11]USER (AUTILIS) !Other
  USRINT AUS User -> [AUS]CODUSR =[A11]USRINT (AUTILIS) !Other

## ATRADIS (TAT) - Import/export tracking
Notes: activity code DIS
Keys (first = PK; D = duplicates allowed): ATS0 NUMERO; ATS1 LANGUE+EXTDAT (D); ATS2 LANGUE+INTDAT (D); ATS3 LANGUE+NUMERO
Fields:
  ADE A*50 Destination
  AUUID AUUID Single identifier
  COMMENT A*240 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TAT]CREUSR (AUTILIS) !Other
  DES A*30 Description
  EXTDAT D Extraction date
  EXTUSR AUS User -> [AUS]CODUSR =[TAT]EXTUSR (AUTILIS) !Block
  INTDAT D Integration date
  INTUSR AUS User -> [AUS]CODUSR =[TAT]INTUSR (AUTILIS) !Block
  LANGUE LAN Language -> [TLA]TLA0 =[TAT]LANGUE (TABLAN) !Block
  LANGUE2 LAN Extraction language -> [TLA]TLA0 =[TAT]LANGUE2 (TABLAN) !Block
  NUMERO L*8 Number
  SEQFILE1 A*30 File1 import/export
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TAT]UPDUSR (AUTILIS) !Other

## BOSIMP (BOSI) - Subcontract BOM
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): BOS0 ITMREF+BOMALT+BOMALTTYP+BOMSEQ+CPNITMREF
Fields:
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMENDDAT D Valid to
  BOMOFS C*4 Subcontract LT
  BOMQTY QTY UOM link quantity
  BOMSEQ C*4 Sequence
  BOMSHO SHO Link description
  BOMSTRDAT D Valid from
  BOMSTUCOE COE UOM-STK factor
  BOMUOM UOM UOM -> [TUN]TUN0 =[BOSI]BOMUOM (TABUNIT) !Block
  CPNITMREF ITM Subcontract -> [ITM]ITM0 =[BOSI]CPNITMREF (ITMMASTER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BOSI]CREUSR (AUTILIS) !Other
  ITMREF ITM Parent product -> [ITM]ITM0 =[BOSI]ITMREF (ITMMASTER) !Block
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  QTYRND M*15 Quantity rounding [menu 293: 1=Round to the nearest,2=Greater than,3=Less than]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BOSI]UPDUSR (AUTILIS) !Other

