# ZC module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## ZCEAUD - Export Audit (view ZC0009)
Keys (first = PK; D=dups allowed, M=modifiable): EXPSEQNR; UNITID+PROCESS [D,M]; PROCESS+UNITID [D,M]
Fields (NAME type description [values]):
  EXPSEQNR String*4 Export Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  UNITID String*4 Process Unit ID
  PROCESS String*8 Process ID
  DESTCURN String*3 Destination Currency
  EXPSEGS Integer Export Segments [0=No,1=Yes]
  EXPSRC Integer Export Source Codes [0=No,1=Yes]
  EXPACCTS Integer Export Accounts [0=No,1=Yes]
  EXPBUDS Integer Export Budgets [0=No,1=Yes]
  EXPTRANS Integer Export Transactions [0=No,1=Yes]
  EXPMAP Integer Export Mapping Table [0=No,1=Yes]
  EXPBUD1 Integer Export Budget Set 1 [0=No,1=Yes]
  EXPBUD2 Integer Export Budget Set 2 [0=No,1=Yes]
  EXPBUD3 Integer Export Budget Set 3 [0=No,1=Yes]
  EXPBUD4 Integer Export Budget Set 4 [0=No,1=Yes]
  EXPBUD5 Integer Export Budget Set 5 [0=No,1=Yes]
  MAPTBL String*8 Mapping Table
  EXPMETH Integer Export Method [0=Net Changes,1=Transactions By Posting Sequence,2=Transactions By Fiscal Period,3=Balances]
  MAPMETH Integer Mapping Method [0=Generate Error For Unmapped Accounts,1=Only Map Accounts In Table,2=Only Transfer Mapped Accounts]
  USESEGS Integer Use Segments [0=No,1=Yes]
  USESRCCODE Integer Use Source Codes [0=No,1=Yes]
  FISCYR String*4 Fiscal Year
  FISCPERD String*2 Fiscal Period
  PSEQFR BCD*4.0 From Posting Sequence
  PSEQTO BCD*4.0 To Posting Sequence
  PSEQHI BCD*4.0 Highest Posting Sequence
  PSEQLO BCD*4.0 Lowest Posting Sequence
  FISCYRHI String*4 Highest Fiscal Year
  FISCPERDHI String*2 Highest Fiscal Period
  FISCYRLO String*4 Lowest Fiscal Year
  FISCPERDLO String*2 Lowest Fiscal Period
  TOTTRNFILE Integer Total Tran. Files In Export
  TOTTRNRECS Long Total Tran. Records In Export
  TOTACCRECS Long Total Account Records In Export
  TOTSRCRECS Long Total Src Code Records In Export
  TOTSEGRECS Long Total Segment Records In Export
  TOTBDGRECS Long Total Budget Records In Export
  MULTICURN Integer Export Was For Multi Curr. Co. [0=Single,1=Multi]
  EXPDATE Date Date Exported
  EXPUSER String*8 User That Did Export
  EXPCOMP String*6 Exporting Company
  SRCCURN String*3 Func. Currency Of Exporting Co.
  VERSION String*3 Program Version
  EXPOPTFLD Integer Export Opt. Field from G/L Setup [0=No,1=Yes]
  TOTOFDRECS Long Total G/L Setup Opt. Flds In Export
  EXPACTOPT Integer Export Account Opt. Fields [0=No,1=Yes]
  EXPTRANOPT Integer Export Trans. Opt. Fields [0=No,1=Yes]
  EXPCSOFDS Integer Export Opt. Field from C/S Setup [0=No,1=Yes]
  TOTCSOFDS Long Total C/S Setup Opt. Flds In Export
  EXPACCTGRP Integer Export Account Groups [0=No,1=Yes]
  TOTAGPRECS Long Total Account Groups In Export
  PRINTED Integer Record Printed [0=No,1=Yes]

## ZCESPD - G/L Consol. Export Detail (view ZC0002)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS+OLDLEDG+OLDTYPE
Fields (NAME type description [values]):
  PROCESS String*8 Process Code
  OLDLEDG String*2 Old Source Ledger
  OLDTYPE String*2 Old Source Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OLDDESC String*60 Reserved
  NEWLEDG String*2 New Source Ledger
  NEWTYPE String*2 New Source Type
  NEWDESC String*60 Reserved
  OPTYPE Integer Option [0=Substitution,1=Exclusion]
  OPRTN Integer (Reserved)

## ZCESPH - G/L Consol. Export Header (view ZC0001)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS
Fields (NAME type description [values]):
  PROCESS String*8 Process ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESCR String*60 Description
  SRCID String*4 Source Unit ID
  SELMETH Integer Selection Method
  SPECSEG Integer Specify Segments [0=No,1=Yes]
  SEGNUM String*6 Segment Number
  SEGFR String*15 Segment From
  SEGTO String*15 Segment To
  USEMAP Integer Use Mapping Table [0=No,1=Yes]
  MAPERR Integer Generate Error If Unmapped [0=No,1=Yes]
  MAPACCT Integer Only Map Whats In Table [0=No,1=Yes]
  MAPTRNSF Integer Only Transfer Whats Mapped [0=No,1=Yes]
  MAPTBL String*8 Mapping Table
  CONSBUD Integer Consolidate Budgets [0=No,1=Yes]
  EXPMETH Integer Export Method [0=Net Changes,3=Balances,1=Transactions By Posting Sequence,2=Transactions By Fiscal Period]
  TXDESC String*60 Net Chg. G/L Description
  SUBSRC Integer Substitute Source Codes [0=No,1=Yes]
  TRSRCLEDG String*2 Default Transaction Ledger
  DSRCLEDG String*2 Default Source Ledger
  DSRCTYPE String*2 Default Source Type
  PERDOFFS Integer Period Offset
  EXPTRANS Integer Export Transactions [0=No,1=Yes]
  EXPACCTS Integer Export Accounts [0=No,1=Yes]
  EXPACTACC Integer Export Inactive Accounts [0=No,1=Yes]
  ACTINACT Integer Set Inactive Accounts To Active [0=No,1=Yes]
  EXPSRC Integer Export Source Codes [0=No,1=Yes]
  EXPSEGS Integer Export Segments [0=No,1=Yes]
  EXPBUDS Integer Export Budgets [0=No,1=Yes]
  EXPBUD1 Integer Export Budget 1 [0=No,1=Yes]
  EXPBUD2 Integer Export Budget 2 [0=No,1=Yes]
  EXPBUD3 Integer Export Budget 3 [0=No,1=Yes]
  EXPBUD4 Integer Export Budget 4 [0=No,1=Yes]
  EXPBUD5 Integer Export Budget 5 [0=No,1=Yes]
  EXPBDFRYR String*4 Export Budget From Year
  EXPBDTOYR String*4 Export Budget To Year
  EXPMAP Integer Export Mapping Table Changes [0=No,1=Yes]
  EORIGAUD Integer Export Orig. Audit Trail [0=No,1=Yes]
  CZRTRANS Integer Create Trans. With Zero Value [0=No,1=Yes]
  MAXTRANS Integer Max. Trans. Per File
  TRANBALACC String*45 Entry Balancing Acct.
  MULTICURN Integer Multi Currency Destination Co. [0=No,1=Yes]
  EXPOTHCUR Integer Export In Another Currency [0=No,1=Yes]
  OVRRIDEMC Integer Override Multi Currency [0=No,1=Yes]
  MCSW Integer Multi Currency Switch [0=No,1=Yes]
  SPECSW Integer Specified Currency Switch [0=All Currency,1=Specific Currency]
  EXPCURRID String*3 Currency Code
  RATETYPE String*2 Dflt Currency Rate Type
  XCHGPROF String*45 Exchange Gain Acct.
  XCHGLOS String*45 Exchange Loss Acct.
  BUDRATTYP String*2 Rate Type For Budgets
  UNITBALACC String*45 Unit Balancing Acct.
  TDATEUSE Integer Trans. Currency XChange Date [0=Fiscal Period,1=Transaction Date,2=User Specified]
  BDATEUSE Integer Buds. Currency XChange Date [0=No,1=Yes]
  RUNTEDIT Integer Allow Runtime Edit [0=No,1=Yes]
  LASTYR String*4 Last Fiscal Year Exported
  LASTPERD String*2 Last Fiscal Period Exported
  EXPSEQNO Integer Export Sequence Number
  LOCALEXP Integer Retain Orig. G/L Ref And Desc. [0=No,1=Yes]
  TRANSCURN Integer Translation Currency [0=Functional Currency,1=Source Currency]
  EXPACTOPT Integer Export Account Opt. Fields [0=No,1=Yes]
  EXPTRANOPT Integer Export Trans. Opt. Fields [0=No,1=Yes]
  EXPOPTFLD Integer Export Opt. Flds from G/L Setup [0=No,1=Yes]
  EXPCSOFDS Integer Export Opt. Flds from C/S Setup [0=No,1=Yes]
  EXPACCTGRP Integer Export Account Groups [0=No,1=Yes]

## ZCETBD - Temporary Export For Budgets (view ZC0004)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS+DACCTID+DFSCSYR+DFSCSDSG
Fields (NAME type description [values]):
  PROCESS String*8 Process ID
  DACCTID String*45 Destination Account Number
  DFSCSYR String*4 Destination Fiscal Year
  DFSCSDSG String*1 Destination Fiscal
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DFSCSCURN String*3 Destination Currency
  DCURNTYPE String*1 S-Source, E-Equivalent, F-Functional
  DCURNDEC String*1 Destination No. Of Decimals In Currency
  DRATEDATE Date Destination Rate Date
  DRATETYPE String*2 Destination Rate Type
  DNETPERD1 BCD*10.3 Destination Budget For Period 1
  DNETPERD2 BCD*10.3 Destination Budget For Period 2
  DNETPERD3 BCD*10.3 Destination Budget For Period 3
  DNETPERD4 BCD*10.3 Destination Budget For Period 4
  DNETPERD5 BCD*10.3 Destination Budget For Period 5
  DNETPERD6 BCD*10.3 Destination Budget For Period 6
  DNETPERD7 BCD*10.3 Destination Budget For Period 7
  DNETPERD8 BCD*10.3 Destination Budget For Period 8
  DNETPERD9 BCD*10.3 Destination Budget For Period 9
  DNETPERD10 BCD*10.3 Destination Budget For Period 10
  DNETPERD11 BCD*10.3 Destination Budget For Period 11
  DNETPERD12 BCD*10.3 Destination Budget For Period 12
  DNETPERD13 BCD*10.3 Destination Budget For Period 13
  DNETPERD14 BCD*10.3 Destination Budget For Period 14
  DNETPERD15 BCD*10.3 Destination Budget For Period 15
  SACCTID String*45 Source Account Number
  SFSCSYR String*4 Source Fiscal Year
  SFSCSDSG String*1 Source Fiscal
  SFSCSCURN String*3 Source Currency
  SCURNTYPE String*1 S-Source, E-Equivalent, F-Functional
  SCURNDEC String*1 Source No. Of Decimals In Currency
  SNETPERD1 BCD*10.3 Source Budget For Period 1
  SNETPERD2 BCD*10.3 Source Budget For Period 2
  SNETPERD3 BCD*10.3 Source Budget For Period 3
  SNETPERD4 BCD*10.3 Source Budget For Period 4
  SNETPERD5 BCD*10.3 Source Budget For Period 5
  SNETPERD6 BCD*10.3 Source Budget For Period 6
  SNETPERD7 BCD*10.3 Source Budget For Period 7
  SNETPERD8 BCD*10.3 Source Budget For Period 8
  SNETPERD9 BCD*10.3 Source Budget For Period 9
  SNETPERD10 BCD*10.3 Source Budget For Period 10
  SNETPERD11 BCD*10.3 Source Budget For Period 11
  SNETPERD12 BCD*10.3 Source Budget For Period 12
  SNETPERD13 BCD*10.3 Source Budget For Period 13
  SNETPERD14 BCD*10.3 Source Budget For Period 14
  SNETPERD15 BCD*10.3 Source Budget For Period 15

## ZCETPS - Temporary Posting Sequence (view ZC0013)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS+ENTRY+PSEQ+FISCYR+FISCPERD+LEVEL
Fields (NAME type description [values]):
  PROCESS String*8 Process ID
  ENTRY Long Generated Entry Number
  PSEQ BCD*4.0 Posting Sequence
  FISCYR String*4 Fiscal Year
  FISCPERD String*2 Fiscal Period
  LEVEL Integer Level
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESTAMT BCD*10.3 Destination Amount
  USERID String*8 User ID
  SRCLEDG String*2 Source Ledger
  SRCTYPE String*2 Source Type
  BUFFLEN Integer Buffer Length
  BUFFER1 String*250 First Buffer For Post.Seq. Info
  BUFFER2 String*250 Second Buffer For Post.Seq. Info
  SRCAMT BCD*10.3 Source Ledger Amount
  VALUES Long Optional Field Count

## ZCIAUD - Import Audit (view ZC0010)
Keys (first = PK; D=dups allowed, M=modifiable): IMPSEQNR; UNITID+EXPSEQNR [D,M]; UNITID+FISCYR+FISCPERD [D,M]; IMPDATE [D,M]
Fields (NAME type description [values]):
  IMPSEQNR Long Import Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPSEQNR String*4 Export Sequence Number
  UNITID String*4 Process Unit ID
  PROCESS String*8 Process ID
  DESTCURN String*3 Destination Currency
  IMPSEGS Integer Import Segments [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPSRC Integer Import Source Codes [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPACCTS Integer Import Accounts [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPBUDS Integer Import Budgets [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPTRANS Integer Import Transactions [0=No,1=Imported Successfully,2=Not Available,3=Different Method,4=Different Period,5=Missing,6=Aborted,7=Previously Imported]
  IMPMAP Integer Import Mapping Table [0=No,1=Yes,2=Not Available,3=Missing,4=Aborted]
  IMPBUD1 Integer Import Budget Set 1 [0=No,1=Yes]
  IMPBUD2 Integer Import Budget Set 2 [0=No,1=Yes]
  IMPBUD3 Integer Import Budget Set 3 [0=No,1=Yes]
  IMPBUD4 Integer Import Budget Set 4 [0=No,1=Yes]
  IMPBUD5 Integer Import Budget Set 5 [0=No,1=Yes]
  MAPTBL String*8 Mapping Table
  IMPMETH Integer Export Method [0=Net Changes,1=Transactions By Posting Sequence,2=Transactions By Fiscal Period,3=Balances,4=N/A]
  MAPMETH Integer Mapping Method [0=Generate Error For Unmapped Accounts,1=Only Map Accounts In Table,2=Only Transfer Mapped Accounts]
  USESEGS Integer Use Segments [0=No,1=Yes]
  USESRCCODE Integer Use Source Codes [0=No,1=Yes]
  FISCYR String*4 Fiscal Year
  FISCPERD String*2 Fiscal Period
  PSEQFR BCD*4.0 From Posting Sequence
  PSEQTO BCD*4.0 To Posting Sequence
  PSEQHI BCD*4.0 Highest Posting Sequence
  PSEQLO BCD*4.0 Lowest Posting Sequence
  FISCYRHI String*4 Highest Fiscal Year
  FISCPERDHI String*2 Highest Fiscal Period
  FISCYRLO String*4 Lowest Fiscal Year
  FISCPERDLO String*2 Lowest Fiscal Period
  TOTTRNFILE Integer Total Trans. Files In Import
  TOTTRNRECS Long Total Trans. Records In Import
  TOTACCRECS Long Total Account Records In Import
  TOTSRCRECS Long Total Src Code Records In Import
  TOTSEGRECS Long Total Segment Records In Import
  TOTBDGRECS Long Total Budget Records In Import
  MULTICURN Integer Export Was For Multi Curr. Co. [0=Single,1=Multi]
  EXPDATE Date Date Exported
  IMPUSER String*8 User That Did Import
  EXPCOMP String*6 Exporting Company
  SRCCURN String*3 Func. Currency Of Exporting Co.
  VERSION String*3 Program Version
  IMPOFDS Integer Import Opt. Flds from G/L Setup [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  TOTOFDRECS Long Total Opt. Flds Recs In Import
  IMPACTOPT Integer Import Account Opt. Fields [0=No,1=Yes]
  IMPTRANOPT Integer Import Trans. Opt. Fields [0=No,1=Yes]
  IMPCSOFDS Integer Import Opt. Field from C/S Setup [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  TOTCSOFDS Long Total C/S Setup Opt. Flds In Import
  IMPACCTGRP Integer Import Account Groups [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  TOTAGPRECS Long Total Account Groups In Import
  PRINTED Integer Record Printed [0=No,1=Yes]
  IMPDATE Date Date Actually Imported
  FIRBTCH String*6 First Batch Created For Import
  LSTBTCH String*6 Last Batch Created For Import
  CLRSEL Integer Clear Deselected Data [0=No,1=Yes]
  DUPL Integer Duplication Type [0=None,1=Same Posting Seq.,2=Same Fiscal Period]
  IMPSTATE Integer Import State [0=Aborted,1=Deleted,2=Imported]

## ZCIMPT - Import Options (view ZC0008)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS+UNITID+EXPSEQNO
Fields (NAME type description [values]):
  PROCESS String*8 Export Process
  UNITID String*4 Source Unit ID
  EXPSEQNO String*4 Export Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IMPSEQNO Long Import Sequence Number
  IMPMETH Integer Import Method [0=Net Changes,3=Balances,2=Fiscal Period,1=Posting Sequence,4=All Data]
  FISCYR String*4 Fiscal Year
  FISCPERD String*2 Fiscal Period
  CANIMPORT Integer Can Entry Be Imported [0=No,1=Yes,2=Not In Unit Maint.,3=Out Of Sequence,4=Same Sequence,5=Bad Currency]
  IMPORTYN Integer Import Entry [0=No,1=Yes,2=N/A]
  DESCR String*60 Export Process Description
  UNITCURN String*3 Currency Per Import Unit Maint.
  EXPMETH Integer Export Method [0=Net Changes,1=Transactions By Posting Sequence,2=Transactions By Fiscal Period,3=Balances,4=N/A]
  EXPYR String*4 Export Year
  EXPPERD String*2 Export Period
  EXPSEQFR BCD*4.0 First Export Posting Sequence
  EXPSEQTO BCD*4.0 Last Export Posting Sequence
  EXPDUPLIC Integer Possible Duplication [0=None,1=Same Posting Seq.,2=Same Fiscal Period]
  IMPSEGS Integer Import Segment Codes [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPSRC Integer Import Source Codes [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPACCTS Integer Import Accounts [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPBUDS Integer Import Budgets [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPTRANS Integer Import Transactions [0=No,1=Yes,2=N/A,3=Different Method,4=Different Period,5=Missing,6=Aborted,7=Previously Imported]
  IMPMAP Integer Import Mapping Table Changes [0=No,1=Yes,2=N/A,3=Missing,4=Aborted]
  STIMPORT Integer Store Import Entry [0=No,1=Yes,2=Not In Unit Maint.,3=Out Of Sequence,4=Same Sequence,5=Bad Currency]
  STACCTS Integer Store Import Accounts [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STSRC Integer Store Import Source Codes [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STSEGS Integer Store Import Segment Codes [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STBUDS Integer Store Import Budgets [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STTRANS Integer Store Import Transactions [0=No,1=Yes,2=N/A,3=Different Method,4=Different Period,5=Missing,6=Aborted,7=Previously Imported]
  CNTIMP Integer Import Switch [0=Build Container,1=Import]
  IMPOFDS Integer Import Opt. Flds from G/L Setup [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STOFDS Integer Store Import Opt. Fld(G/L Setup) [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPACTOPT Integer Import Account Opt. Fields [0=No,1=Yes,2=N/A]
  IMPTRANOPT Integer Import Trans. Opt. Fields [0=No,1=Yes,2=N/A]
  STCSOFDS Integer Store Import Opt. Fld(C/S Setup) [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPCSOFDS Integer Import Opt. Flds from C/s Setup [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  STACCTGRPS Integer Store Import Account Groups [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]
  IMPACCTGRP Integer Import Account Groups Fields [0=No,1=Yes,2=N/A,3=Missing,4=Aborted,5=Previously Imported]

## ZCIUMN - Import Unit Maintenance (view ZC0006)
Keys (first = PK; D=dups allowed, M=modifiable): UNITID
Fields (NAME type description [values]):
  UNITID String*4 Import ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Unit Description
  SRCCURN String*3 Source Currency
  CURNDESC String*60 Reserved
  EXPMETH Integer Export Method [0=Net Changes,1=Transactions By Posting Sequence,2=Transactions By Fiscal Period,3=Balances,4=Not Available]
  FISCYR String*4 Last Import Fiscal Year
  FISCPERD String*2 Last Import Fiscal Period
  FPOSTSEQ BCD*4.0 Last Import First Post. Seq
  LPOSTSEQ BCD*4.0 Last Import Last Post. Seq
  IMPACCT Integer Last Import Accounts [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPSRC Integer Last Import Source Codes [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPSEGS Integer Last Import Segments [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPBUDS Integer Last Import Budgets [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPTRANS Integer Last Import Transactions [0=No,1=Imported Successfully,2=Not Available,3=Different Method,4=Different Period,5=Missing,6=Aborted,7=Previously Imported]
  IMPMAP Integer Last Import Mapping Table [0=No,1=Yes,2=Not Available,3=Missing,4=Aborted]
  IMPOFDS Integer Last Import G/L Optional Fields [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPCSOFDS Integer Last Import C/S Optional Fields [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]
  IMPACCTGRP Integer Last Import Account Group Codes [0=No,1=Imported Successfully,2=Not Available,3=Missing,4=Aborted,5=Previously Imported]

## ZCMAPT - Mapping Table Details (view ZC0003)
Keys (first = PK; D=dups allowed, M=modifiable): TBLID+SRCACCT; TBLID+STAT [D,M]
Fields (NAME type description [values]):
  TBLID String*8 Mapping Table ID
  SRCACCT String*45 Source Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STAT Integer Status [0=No Change,1=Edited]
  TBLDESC String*60 Table Description
  SRCADESC String*60 Reserved
  DESTACCT String*45 Destination Account
  DESTADESC String*60 Destination Acct. Description
  SRCSTCODE String*6 Source Structure Number
  DESTSTCODE String*6 Destination Structure Number
  CLOSESEG String*6 Post To Segment ID
  POSTTYPE Integer Destination Posting Type [0=Detail,1=Consolidate,2=N/A]
  RATETYPE String*2 Transaction Rate Type
  RATEDESC String*60 Reserved
  MCSW Integer Multi Currency [0=No,1=Yes,2=N/A]
  SPECSW Integer Specified Currency [0=All currency,1=Specific currency,2=N/A]
  ACTIVESW Integer Account Status [0=Inactive,1=Active,2=N/A]

## ZCRSTRT - Restart (view ZC0016)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## ZCSEGS - Segment Number Substitution (view ZC0014)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESS+SEGNO
Fields (NAME type description [values]):
  PROCESS String*8 Export Process ID
  SEGNO String*6 Source Segment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEGDESC String*60 Reserved
  NEWSEGNO String*6 Target Segment Number

## ZCSEQS - Sequence Numbers (view ZC0011)
Keys (first = PK; D=dups allowed, M=modifiable): RECID
Fields (NAME type description [values]):
  RECID String*4 Record ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPSEQNR Long Export Sequence Number
  IMPSEQNR Long Import Sequence Number
  FISCYR String*4 Last Fiscal Year
  FISCPERD String*2 Last Fiscal Period
  LASTPSEQ BCD*4.0 Last Posting Sequence

## ZCXMAP - Mapping Tables (view ZC0012)
Keys (first = PK; D=dups allowed, M=modifiable): TBLID
Fields (NAME type description [values]):
  TBLID String*8 Mapping Table ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TBLDESC String*60 Table Description
