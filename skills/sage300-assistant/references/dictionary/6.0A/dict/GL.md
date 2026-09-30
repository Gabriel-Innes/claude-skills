# GL module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## GL01 - General Ledger Options (view GL0005)
Keys (first = PK; D=dups allowed, M=modifiable): OPTIONID
Fields (NAME type description [values]):
  OPTIONID String*4 GL option key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PHONENBR String*30 Company phone number
  FAX String*30 Company fax number
  COMPANYID String*6 Organization ID
  CONTACT String*60 Client contact name
  CLOSESEG String*6 RESERVED Closing Segment Number
  ACCTSEG String*6 Main Acct Segment ID
  ABRKDFLT String*6 Default Structure Code
  ABRKDELM String*1 Structure Code delimiter
  SWBTCHEDIT Integer Batch edit allowed [1=All Fields,2=Fiscal Period, Year, Trans Date,3=No Edit]
  SWPROVPST Integer Provisional posting allowed [0=Provisional posting not allowed,1=Provisional posting allowed]
  SWPRTPBTCH Integer Print Batches prior to Post [0=Printing not required,1=Printing required]
  CODELOCK1 Integer Budget 1 lock [0=Unlocked,1=Locked]
  CODELOCK2 Integer Budget 2 lock [0=Unlocked,1=Locked]
  CODELOCK3 Integer Budget 3 lock [0=Unlocked,1=Locked]
  CODELOCK4 Integer Budget 4 lock [0=Unlocked,1=Locked]
  CODELOCK5 Integer Budget 5 lock [0=Unlocked,1=Locked]
  LOCKFILL String*8 RESERVED Space for more locks
  SWQTY Integer Quantity History allowed [0=Do not allow quantities,1=Quantities allowed]
  QTYDEC BCD*4.0 Number of decimals for qty
  YRSHIST BCD*4.0 Years of Summary History Kept
  YRACCTDEL BCD*4.0 RESERVED Yrs chkd for acct del
  NEXTBTCHNO BCD*4.0 Last Issued Batch Number
  PSTSQ BCD*4.0 Next actual post seq #
  PROVPSTSQ BCD*4.0 Next provisional post seq #
  PJRNLPRGTO BCD*4.0 RESERVED Prov jrnl purged to
  BTCHPSTTO BCD*4.0 RESERVED Last Batch Posted
  JRNLPRGTO BCD*4.0 RESERVED Purge to batch
  YRCLSLST BCD*4.0 Last closed year
  YRLSTACTL BCD*4.0 Oldest year of Fiscal Sets
  PRDNOPSTPR BCD*4.0 RESERVED Period no post prior
  YRNOPSTPR BCD*4.0 Oldest year of Trans. Detail
  REACCT String*45 Default retained earning acct
  SWMC Integer Multicurrency Activated Switch [0=Inactive,1=Active]
  DFLRATETYP String*2 Default currency rate type
  SWACCTGRP Integer Account group switch [0=Do not allow account groups,1=Account groups allowed]
  SWPRVYRPST Integer Allow previous year posting [0=Do not allow previous yr posting,1=Previous yr posting allowed]
  YRSTRANDTL BCD*4.0 Years of detail history kept
  HSTCLRACCT String*45 RESERVED Acct history clearing acct
  RPACCT String*45 Transition rounding account
  SRCETYPE String*2 Source Type
  SWUSESEC Integer Use GL Security [0=No,1=Yes]
  SWDEFACCSS Integer Default Access [0=All Accounts,1=No Accounts]

## GLABK - Account Segments (view GL0022)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTBLKID
Fields (NAME type description [values]):
  ACCTBLKID String*6 Segment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATUSACTV String*1 Segment Status
  ABLKTYPE String*1 Segment Type
  ABLKDESC String*60 Segment Description
  ABLKLEN BCD*4.0 Segment Length
  ABLKVALUE String*15 RESERVED Account segment initial value
  ABRKUSAGE BCD*4.0 RESERVED Structure Code usage count
  AVHUSAGE BCD*4.0 RESERVED Account seg validation usage ct
  ARHUSAGE BCD*4.0 RESERVED Account seg replacement usage ct
  DATEEFF Date RESERVED Date account segment effective
  REQDSW Integer RESERVED Account segment required switch
  CLOSESW Integer Close by account segment switch
  ABLKDELM String*1 RESERVED Account segment delimiter
  NUMOFKEY Binary*1 Alternate Key Index

## GLABRX - Structure Codes (view GL0023)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTBRKID
Fields (NAME type description [values]):
  ACCTBRKID String*6 Structure Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ABRKDESC String*60 Description
  ABRKID1 String*6 Segment Number 1
  ABRKSTRT1 String*2 Segment 1 Starting Position
  ABRKVSEQ1 String*2 RESERVED Acct seg 1 validation seq #
  ABRKLEN1 BCD*4.0 Segment 1 Length
  ABRKID2 String*6 Segment Number 2
  ABRKSTRT2 String*2 Segment 2 Starting Position
  ABRKVSEQ2 String*2 RESERVED Acct seg 2 validation seq #
  ABRKLEN2 BCD*4.0 Segment 2 Length
  ABRKID3 String*6 Segment Number 3
  ABRKSTRT3 String*2 Segment 3 Starting Position
  ABRKVSEQ3 String*2 RESERVED Acct seg 3 validation seq #
  ABRKLEN3 BCD*4.0 Segment 3 Length
  ABRKID4 String*6 Segment Number 4
  ABRKSTRT4 String*2 Segment 4 Starting Position
  ABRKVSEQ4 String*2 RESERVED Acct seg 4 validation seq #
  ABRKLEN4 BCD*4.0 Segment 4 Length
  ABRKID5 String*6 Segment Number 5
  ABRKSTRT5 String*2 Segment 5 Starting Position
  ABRKVSEQ5 String*2 RESERVED Acct seg 5 validation seq #
  ABRKLEN5 BCD*4.0 Segment 5 Length
  ABRKID6 String*6 Segment Number 6
  ABRKSTRT6 String*2 Segment 6 Starting Position
  ABRKVSEQ6 String*2 RESERVED Acct seg 6 validation seq #
  ABRKLEN6 BCD*4.0 Segment 6 Length
  ABRKID7 String*6 Segment Number 7
  ABRKSTRT7 String*2 Segment 7 Starting Position
  ABRKVSEQ7 String*2 RESERVED Acct seg 7 validation seq #
  ABRKLEN7 BCD*4.0 Segment 7 Length
  ABRKID8 String*6 Segment Number 8
  ABRKSTRT8 String*2 Segment 8 Starting Position
  ABRKVSEQ8 String*2 RESERVED Acct seg 8 validation seq #
  ABRKLEN8 BCD*4.0 Segment 8 Length
  ABRKID9 String*6 Segment Number 9
  ABRKSTRT9 String*2 Segment 9 Starting Position
  ABRKVSEQ9 String*2 RESERVED Acct seg 9 validation seq #
  ABRKLEN9 BCD*4.0 Segment 9 Length
  ABRKID10 String*6 Segment Number 10
  ABRKSTRT10 String*2 Segment 10 Starting Position
  ABRKVSEQ10 String*2 RESERVED Acct seg 10 validation seq #
  ABRKLEN10 BCD*4.0 Segment 10 Length
  ABRKTITLE String*30 RESERVED Structure Code title
  ABRKTYPE String*1 RESERVED Structure Code type
  ACCTTYPE String*1 RESERVED Account type
  PAHUSAGE BCD*4.0 RESERVED PAH usage count
  ASTUSAGE BCD*4.0 RESERVED AST usage count
  ADHUSAGE BCD*4.0 RESERVED ADH usage count
  AITUSAGE BCD*4.0 RESERVED AIT usage count
  ASDUSAGE BCD*4.0 RESERVED ASD usage count
  DATEEFF Date RESERVED Effective start date
  ABLKDELM1 String*1 RESERVED Acct seg 1 delimiter
  ABLKDELM2 String*1 RESERVED Acct seg 2 delimiter
  ABLKDELM3 String*1 RESERVED Acct seg 3 delimiter
  ABLKDELM4 String*1 RESERVED Acct seg 4 delimiter
  ABLKDELM5 String*1 RESERVED Acct seg 5 delimiter
  ABLKDELM6 String*1 RESERVED Acct seg 6 delimiter
  ABLKDELM7 String*1 RESERVED Acct seg 7 delimiter
  ABLKDELM8 String*1 RESERVED Acct seg 8 delimiter
  ABLKDELM9 String*1 RESERVED Acct seg 9 delimiter
  ABLKDELM10 String*1 RESERVED Acct seg 10 delimiter

## GLACGRP - Account Groups (view GL0055)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTGRPCOD; SORTCODE+ACCTGRPCOD [D,M]
Fields (NAME type description [values]):
  ACCTGRPCOD String*12 Account Group Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTGRPDES String*60 Account Group Description
  SORTCODE String*12 Account Group Sort Code
  GRPCOD Integer Group Category [0=                              ,10=Cash and Cash Equivalents     ,20=Accounts Receivable           ,30=Inventory                     ,40=Other Current Assets          ,50=Fixed Assets                  ,60=Accumulated Depreciation      ,70=Other Assets                  ,80=Accounts Payable              ,90=Other Current Liabilities     ,100=Long Term Liabilities         ,110=Other Liabilities             ,120=Share Capital                 ,130=Shareholders' Equity          ,140=Revenue                       ,150=Cost of Sales                 ,160=Other Revenue                 ,170=Other Expenses                ,180=Depreciation Expense          ,190=Gains/Losses                  ,200=Interest Expense              ,210=Income Taxes                  ]

## GLACHD - Rollup Groups (view GL0057)
Keys (first = PK; D=dups allowed, M=modifiable): PARENT+CHILD; CHILD+PARENT
Fields (NAME type description [values]):
  PARENT String*45 Rollup Account
  CHILD String*45 Member Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## GLACHDU - Rollup Group Processor (view GL0059)
Keys (first = PK; D=dups allowed, M=modifiable): PARENT+CHILD
Fields (NAME type description [values]):
  PARENT String*45 Rollup Account
  CHILD String*45 Member Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPSW Integer Delete / Add switches

## GLADSD - Rollup Group Relationship (view GL0058)
Keys (first = PK; D=dups allowed, M=modifiable): ANCESTOR+DESCENDANT; DESCENDANT+ANCESTOR
Fields (NAME type description [values]):
  ANCESTOR String*45 Rollup Account at any level
  DESCENDANT String*45 Member Account at any level
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REFCOUNT Long Reference Count

## GLAFS - Account Fiscal Sets (view GL0103)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+FSCSYR+FSCSDSG+FSCSCURN+CURNTYPE; FSCSDSG [D,M]
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  FSCSYR String*4 Fiscal set year
  FSCSDSG String*1 Fiscal set Designator
  FSCSCURN String*3 Currency code
  CURNTYPE String*1 Currency type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWRVL Integer RESERVED Revaluation switch
  CODERVL String*6 RESERVED Revaluation code
  SCURNDEC String*1 Source currency decimals
  OPENBAL BCD*10.3 Beginning balance
  NETPERD1 BCD*10.3 Period 01 net amount
  NETPERD2 BCD*10.3 Period 02 net amount
  NETPERD3 BCD*10.3 Period 03 net amount
  NETPERD4 BCD*10.3 Period 04 net amount
  NETPERD5 BCD*10.3 Period 05 net amount
  NETPERD6 BCD*10.3 Period 06 net amount
  NETPERD7 BCD*10.3 Period 07 net amount
  NETPERD8 BCD*10.3 Period 08 net amount
  NETPERD9 BCD*10.3 Period 09 net amount
  NETPERD10 BCD*10.3 Period 10 net amount
  NETPERD11 BCD*10.3 Period 11 net amount
  NETPERD12 BCD*10.3 Period 12 net amount
  NETPERD13 BCD*10.3 Period 13 net amount
  NETPERD14 BCD*10.3 Period 14 net amount
  NETPERD15 BCD*10.3 Period 15 net amount
  ACTIVITYSW Integer Activity switch [0=Inactive,1=Periods Active,2=Balance Forward Active]

## GLAIS - Account Allocation Instructions (view GL0004)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+ACCTIDDIST
Fields (NAME type description [values]):
  ACCTID String*45 Account
  ACCTIDDIST String*45 Distribution Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  REF String*60 Journal Reference
  ALLOCPCT BCD*8.7 Allocation Percent

## GLAMF - Accounts (view GL0001)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID; ACCTGRPCOD+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL01+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL02+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL03+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL04+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL05+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL06+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL07+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL08+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL09+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACSEGVAL10+ACCTSEGVAL+ABRKID+ACCTID [D,M]; ACCTFMTTD [D,M]; ACCTGRPSCD+ACCTGRPCOD+ACCTSEGVAL+ABRKID+ACCTID [D,M]
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CREATEDATE Date Date Created
  ACCTDESC String*60 Description
  ACCTTYPE String*1 Type
  ACCTBAL String*1 Normal Balance DR/CR
  ACTIVESW Integer Status [0=Inactive,1=Active]
  CONSLDSW Integer Post to Account [0=Detail,1=Consolidated,2=Prohibited]
  QTYSW Integer Quantities Allowed [0=No,1=Yes]
  UOM String*6 Unit of Measure
  ALLOCSW Integer Allocations Allowed [0=No Allocation,1=Allocated by Account Balance,2=Allocated by Account Quantity]
  ACCTOFSET String*45 Alloc Offset Account
  ACCTSRTY String*2 Alloc Source Type
  MCSW Integer Multicurrency [0=No,1=Yes]
  SPECSW Integer Specific Currency [0=All Currencies,1=Specific Currencies]
  ACCTGRPCOD String*12 Account Group Code
  CTRLACCTSW Integer Control Account [0=No,1=Yes]
  SRCELDGID String*2 Reserved
  ALLOCTOT BCD*8.7 Allocation Percent Total
  ABRKID String*6 Structure Code
  YRACCTCLOS BCD*4.0 Year Last Closed
  ACCTFMTTD String*45 Account Number
  ACSEGVAL01 String*15 Account Segment Code 1
  ACSEGVAL02 String*15 Account Segment Code 2
  ACSEGVAL03 String*15 Account Segment Code 3
  ACSEGVAL04 String*15 Account Segment Code 4
  ACSEGVAL05 String*15 Account Segment Code 5
  ACSEGVAL06 String*15 Account Segment Code 6
  ACSEGVAL07 String*15 Account Segment Code 7
  ACSEGVAL08 String*15 Account Segment Code 8
  ACSEGVAL09 String*15 Account Segment Code 9
  ACSEGVAL10 String*15 Account Segment Code 10
  ACCTSEGVAL String*15 Segment Code
  ACCTGRPSCD String*12 Account Group Sort Code
  POSTOSEGID String*6 Post to Segment ID
  DEFCURNCOD String*3 Default Currency Code
  OVALUES Long Optional Fields
  TOVALUES Long Transaction Optional Fields
  ROLLUPSW Integer Rollup Switch [0=No,1=Yes]

## GLAMFO - Account Optional Fields (view GL0400)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+OPTFIELD; OPTFIELD+ACCTID
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLAMFTO - Account Trans. Optional Fields (view GL0401)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+OPTFIELD; OPTFIELD+ACCTID
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## GLASV - Segment Codes (view GL0021)
Keys (first = PK; D=dups allowed, M=modifiable): IDSEG+SEGVAL
Fields (NAME type description [values]):
  IDSEG String*6 Segment Number
  SEGVAL String*15 Segment Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEGVALDESC String*60 Segment Code Description
  ACCTRETERN String*45 Closing Account

## GLAVC - Account Valid Currencies (view GL0012)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+CURNID; CURNID+ACCTID
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  CURNID String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REVALSW Integer Revaluation Switch [0=Do not revalue,1=Revalue]
  REVALID String*6 Revaluation Code

## GLBCTL - Batches (view GL0008)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHID; BATCHSTAT+BATCHID [M]
Fields (NAME type description [values]):
  BATCHID String*6 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACTIVESW Integer Active Switch [0=Inactive,1=Active]
  BTCHDESC String*60 Description
  SRCELEDGR String*2 Source Ledger
  DATECREAT Date Date Created
  DATEEDIT Date Date Last Edited
  BATCHTYPE String*1 Type
  BATCHSTAT String*1 Status
  POSTNGSEQ BCD*4.0 Posting Sequence
  DEBITTOT BCD*10.3 Debits
  CREDITTOT BCD*10.3 Credits
  QTYTOTAL BCD*10.3 Quantity Total
  ENTRYCNT BCD*4.0 Number of Entries
  NEXTENTRY BCD*4.0 Next Entry Number
  ERRORCNT BCD*4.0 No. of Errors
  ORIGSTATUS String*1 Original Status
  SWPRINTED Integer Printed [0=No,1=Yes]
  SWICT Integer ICT Related [0=No,1=Yes]
  SWRVRECOG Integer Revaluation(Recognized) Batch [0=No,1=Yes]

## GLCAS - Control Account Subledgers (view GL0107)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+SRCELDGID
Fields (NAME type description [values]):
  ACCTID String*45 Account
  SRCELDGID String*2 Subledger
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## GLCHAGP - Account Group-Sort Orders (view GL0056)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTGRPCOD; SORTCODE+ACCTGRPCOD [D,M]
Fields (NAME type description [values]):
  ACCTGRPCOD String*12 Account Group Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SORTCODE String*12 New Sort Code

## GLGSACC - Account Permissions (view GL0053)
Keys (first = PK; D=dups allowed, M=modifiable): USER+LINE
Fields (NAME type description [values]):
  USER String*8 User ID
  LINE Long Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWCANSEE Integer Allow [0=No,1=Yes]
  BEGINAC String*45 From Account
  ENDAC String*45 To Account

## GLGSSEG - Segment Permissions (view GL0052)
Keys (first = PK; D=dups allowed, M=modifiable): USER+LINE
Fields (NAME type description [values]):
  USER String*8 User ID
  LINE Long Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWCANSEE Integer Allow [0=No,1=Yes]
  SEGID String*6 Segment
  BEGINID String*15 From Segment
  ENDID String*15 To Segment

## GLGSUSR - Users (view GL0054)
Keys (first = PK; D=dups allowed, M=modifiable): USER
Fields (NAME type description [values]):
  USER String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HASDTLREC Integer Has Restriction Records Switch [0=No,1=Yes]

## GLJAL - Auto Allocation Processor (view GL0029)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY Integer Key Id
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Batch description
  CODESEGSEL String*1 Account/segment selection code
  CODESEG String*6 Account segment selected
  IDACCTFROM String*45 From Account Number
  IDACCTTO String*45 To Account Number
  DATETRANS Date Transaction date for details
  CNTPERD String*2 Posting period for Account Bal
  CNTYEAR String*4 Posting year for Account Bal
  ALLOCATEBY Integer Allocate By Switch
  QTYFRYEAR String*4 Select from year for Acct Qty
  QTYTOYEAR String*4 Select to year for Acct Qty
  QTYFRPERD String*2 Select from period for Acct Qty
  QTYTOPERD String*2 Select to period for Acct Qty
  PROCESSCMD Integer Process switches [0=Process Auto Allocation,1=Insert Optional Fields]
  VALUES Long Optional Fields

## GLJALO - Auto Alloc. Optional Fields (view GL0409)
Keys (first = PK; D=dups allowed, M=modifiable): KEY+OPTFIELD; OPTFIELD+KEY
Fields (NAME type description [values]):
  KEY Integer Key Id
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLJEC - Journal Comments (view GL0007)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHNBR+JOURNALID+TRANSNBR
Fields (NAME type description [values]):
  BATCHNBR String*6 Batch Number
  JOURNALID String*5 Entry Number
  TRANSNBR String*10 Transaction Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  JECOMMENT String*250 Comments

## GLJED - Journal Details (view GL0010)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHNBR+JOURNALID+TRANSNBR
Fields (NAME type description [values]):
  BATCHNBR String*6 Batch Number
  JOURNALID String*5 Entry Number
  TRANSNBR String*10 Transaction Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTID String*45 Account Number
  COMPANYID String*8 Company ID
  TRANSAMT BCD*10.3 Amount
  TRANSQTY BCD*10.3 Quantity
  SCURNDEC String*1 Source Currency Decimals
  SCURNAMT BCD*10.3 Source Currency Amount
  HCURNCODE String*3 Home Currency
  RATETYPE String*2 Currency Rate Table
  SCURNCODE String*3 Source Currency
  RATEDATE Date Currency Rate Date
  CONVRATE BCD*8.7 Currency Rate
  RATESPREAD BCD*8.7 Currency Rate Spread
  DATEMTCHCD String*1 Currency Rate Date Matching
  RATEOPER String*1 Currency Rate Operator
  TRANSDESC String*60 Description
  TRANSREF String*60 Reference
  TRANSDATE Date Journal Date
  SRCELDGR String*2 Source Ledger
  SRCETYPE String*2 Source Type
  VALUES Long Optional Fields
  DESCOMP String*6 Destination
  ROUTE Integer Route No.

## GLJEDO - Journal Detail Optional Fields (view GL0402)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHNBR+JOURNALID+TRANSNBR+OPTFIELD; OPTFIELD+BATCHNBR+JOURNALID+TRANSNBR
Fields (NAME type description [values]):
  BATCHNBR String*6 Batch Number
  JOURNALID String*5 Entry Number
  TRANSNBR String*10 Transaction Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLJEH - Journal Headers (view GL0006)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHID+BTCHENTRY
Fields (NAME type description [values]):
  BATCHID String*6 Batch Number
  BTCHENTRY String*5 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRCELEDGER String*2 Source Ledger
  SRCETYPE String*2 Source Type
  FSCSYR String*4 Fiscal Year
  FSCSPERD String*2 Fiscal Period
  SWEDIT Integer RESERVED Journal Edit
  SWREVERSE Integer Auto Reversal [0=Auto Reversal Off,1=Next Period,2=Specific Period]
  JRNLDESC String*60 Description
  JRNLDR BCD*10.3 Debits
  JRNLCR BCD*10.3 Credits
  JRNLQTY BCD*10.3 Quantity
  DATEENTRY Date Entry Date
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  DRILAPP String*2 Drill Down Application Source
  REVYR String*4 Specific Reversal Year
  REVPERD String*2 Specific Reversal Period
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  ORIGCOMP String*6 Originator
  DETAILCNT BCD*4.0 Number of Details

## GLOFD - Optional Fields (view GL0500)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Accounts,1=Transaction Details]
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## GLOFH - Optional Field Locations (view GL0501)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Accounts,1=Transaction Details]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## GLPACHD - Rollup Member Preview (view GL0063)
Keys (first = PK; D=dups allowed, M=modifiable): PARENT+ACCTID
Fields (NAME type description [values]):
  PARENT String*45 Source Account
  ACCTID String*45 Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPSW Integer Add / Delete [0=Yes,1=No]

## GLPAMF - Create Accounts Input Criteria (view GL0049)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY Integer Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATESW Integer State
  RECCOUNT Long total records
  FRBRKID String*6 From Accounts with Structure Code
  CRBRKID String*6 Create Using Structure Code
  SELECTBY Integer Select By
  FRACCTID String*45 From Account Number
  TOACCTID String*45 To Account Number
  FRGRPCOD String*12 From Account Group Code
  TOGRPCOD String*12 To Account Group Code
  FRGRPSCD String*12 From Account Group Sort Code
  TOGRPSCD String*12 To Account Group Sort Code
  IDSEG String*6 Segment Id
  SEGVAL String*15 Segment Code
  DFCTRL Integer Default Subledger Details
  DFMCSW Integer Default Currency Options
  INCLEXIST Integer Include Existing Accounts
  CRNEW1 Integer Create New For Segment 1
  FRSEGVAL1 String*15 From Segment 1
  TOSEGVAL1 String*15 To Segment 1
  DFSEGVAL1 String*15 Default Option From Segment 1
  CRNEW2 Integer Create New For Segment 2
  FRSEGVAL2 String*15 From Segment 2
  TOSEGVAL2 String*15 To Segment 2
  DFSEGVAL2 String*15 Default Option From Segment 2
  CRNEW3 Integer Create New For Segment 3
  FRSEGVAL3 String*15 From Segment 3
  TOSEGVAL3 String*15 To Segment 3
  DFSEGVAL3 String*15 Default Option From Segment 3
  CRNEW4 Integer Create New For Segment 4
  FRSEGVAL4 String*15 From Segment 4
  TOSEGVAL4 String*15 To Segment 4
  DFSEGVAL4 String*15 Default Option From Segment 4
  CRNEW5 Integer Create New For Segment 5
  FRSEGVAL5 String*15 From Segment 5
  TOSEGVAL5 String*15 To Segment 5
  DFSEGVAL5 String*15 Default Option From Segment 5
  CRNEW6 Integer Create New For Segment 6
  FRSEGVAL6 String*15 From Segment 6
  TOSEGVAL6 String*15 To Segment 6
  DFSEGVAL6 String*15 Default Option From Segment 6
  CRNEW7 Integer Create New For Segment 7
  FRSEGVAL7 String*15 From Segment 7
  TOSEGVAL7 String*15 To Segment 7
  DFSEGVAL7 String*15 Default Option From Segment 7
  CRNEW8 Integer Create New For Segment 8
  FRSEGVAL8 String*15 From Segment 8
  TOSEGVAL8 String*15 To Segment 8
  DFSEGVAL8 String*15 Default Option From Segment 8
  CRNEW9 Integer Create New For Segment 9
  FRSEGVAL9 String*15 From Segment 9
  TOSEGVAL9 String*15 To Segment 9
  DFSEGVAL9 String*15 Default Option From Segment 9
  CRNEW10 Integer Create New For Segment 10
  FRSEGVAL10 String*15 From Segment 10
  TOSEGVAL10 String*15 To Segment 10
  DFSEGVAL10 String*15 Default Option From Segment 10
  FRORDER String*20 Segment Order of the Selected Account Structure
  CRORDER String*20 Segment Order of the Created Account Structure

## GLPERR - Posting Errors (view GL0015)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR+ERRORCNT
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  ERRORCNT BCD*4.0 Error increment
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MSGCODE String*7 unused
  ERRDESC String*250 Description of error
  ERRBATCH String*6 Error Batch Number
  ERRENTRY String*5 Error Batch Entry Number
  ERRTRANS BCD*4.0 Error Batch Trans Number

## GLPJC - Posting Journal Comments (view GL0017)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMMENT String*250 Journal detail comment
  REFERENCE String*60 Journal detail reference

## GLPJD - Posting Journal Details (view GL0016)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR; ACCTID [D,M]; POSTINGSEQ+BATCHNBR+ENTRYNBR+FISCALYR+FISCALPERD+TRANSNBR [D,M]
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  JRNLDATE Date Journal date
  FISCALYR String*4 Fiscal year
  FISCALPERD String*2 Fiscal period
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  EDITALLOWD Integer Reserved
  CONSOLIDAT Integer Consolidation occurred on post [0=No,1=Yes]
  ACCTID String*45 Account Number
  COMPANYID String*8 Company ID
  JNLDTLDESC String*60 Journal detail description
  JNLDTLREF String*60 Journal detail reference
  TRANSAMT BCD*10.3 Journal transaction amount
  TRANSQTY BCD*10.3 Journal transaction quantity
  SCURNDEC String*1 Nbr of source currency decimals
  SCURNAMT BCD*10.3 Source currency amount
  HCURNCODE String*3 Home currency code
  RATETYPE String*2 Currency rate table type
  SCURNCODE String*3 Source currency code
  RATEDATE Date Date of currency rate selected
  CONVRATE BCD*8.7 Currency rate for conversion
  RATESPREAD BCD*8.7 Currency rate spread allowed
  DATEMTCHCD String*1 Code for rate date matching
  RATEOPER String*1 Currency rate operator
  CODESTATUS Integer Printed status code [0=Not Printed,1=Printed]
  DATEENTRY Date Entry Date
  RPTAMT BCD*10.3 Report currency amount
  VALUES Long Optional Fields
  ORIGCOMP String*6 Originator
  SWREVERSE Integer Auto Reversal [0=Auto Reversal Off,1=Next Period,2=Specific Period]
  DESCOMP String*6 Destination
  ROUTE Integer Route No.

## GLPJDO - Posting Journal Optional Fields (view GL0404)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR+OPTFIELD; OPTFIELD+POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal Entry Number
  TRANSNBR BCD*4.0 Journal Transaction Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## GLPJID - Posting Journal ICT Generated Details (view GL0109)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+OBATCHNBR+OENTRYNBR+OTRANSNBR+LEVEL+LEVCOMP+BATCHNBR+ENTRYNBR+TRANSNBR; POSTINGSEQ+OBATCHNBR+OENTRYNBR+LEVCOMP+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]; LEVCOMP+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]; LEVCOMP+ACCTID+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  OBATCHNBR String*6 Original Batch Number
  OENTRYNBR String*5 Original Entry Number
  OTRANSNBR BCD*4.0 Original Transaction Number
  LEVEL Integer Route Level
  LEVCOMP String*6 Company
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Entry Number
  TRANSNBR BCD*4.0 Transaction Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSDATE Date Transaction Date
  TRANSREF String*60 Reference
  TRANSDESC String*60 Description
  ACCTID String*45 Account Number
  SRCELDGR String*2 Source Ledger
  SRCETYPE String*2 Source Type
  SCURNCODE String*3 Source Currency
  SCURNDEC String*1 Source Currency Decimals
  RATEDATE Date Rate Date
  DATEMTCHCD String*1 Rate Date Matching
  RATETYPE String*2 Rate Type
  RATEOPER String*1 Rate Operator
  CONVRATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  TRANSQTY BCD*10.3 Quantity
  SCURNAMT BCD*10.3 Source Currency Amount
  TRANSAMT BCD*10.3 Amount
  VALUES Long Optional Fields

## GLPJIH - Posting Journal ICT Generated Headers (view GL0108)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+OBATCHNBR+OENTRYNBR+LEVCOMP+BATCHNBR+ENTRYNBR; LEVCOMP+BATCHNBR+ENTRYNBR [D,M]
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  OBATCHNBR String*6 Original Batch Number
  OENTRYNBR String*5 Original Entry Number
  LEVCOMP String*6 Company
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HCURNCODE String*3 Home Currency
  DATEENTRY Date Entry Date
  JRNLDESC String*60 Description
  FSCSYR String*4 Fiscal Year
  FSCSPERD String*2 Fiscal Period
  SWREVERSE Integer Auto Reverse [0=Auto Reversal Off,1=Next Period,2=Specific Period]
  REVYR String*4 Specific Reverse Year
  REVPERD String*2 Specific Reverse Period

## GLPOST - Posted Transactions (view GL0018)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+FISCALYR+FISCALPERD+SRCECURN+SRCELEDGER+SRCETYPE+POSTINGSEQ+CNTDETAIL; JRNLDATE+POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]; POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]; ACCTID+POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR [D,M]
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  FISCALYR String*4 Fiscal Year
  FISCALPERD String*2 Fiscal Period
  SRCECURN String*3 Source Currency Code
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  CNTDETAIL BCD*4.0 Detail Count
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  JRNLDATE Date Journal Date
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal Entry Number
  TRANSNBR BCD*4.0 Journal Transaction Number
  EDITALLOWD Integer Reserved
  CONSOLIDAT Integer Consolidation Occurred on Post [0=No,1=Yes]
  COMPANYID String*8 Company ID
  JNLDTLDESC String*60 Journal Detail Description
  JNLDTLREF String*60 Journal Detail Reference
  TRANSAMT BCD*10.3 Journal Transaction Amount
  TRANSQTY BCD*10.3 Journal Transaction Quantity
  SCURNDEC String*1 Nbr of Source Currency Decimals
  SCURNAMT BCD*10.3 Source Currency Amount
  HCURNCODE String*3 Home Currency Code
  RATETYPE String*2 Currency Rate Table Type
  SCURNCODE String*3 Source Currency Code
  RATEDATE Date Date of Currency Rate Selected
  CONVRATE BCD*8.7 Currency Rate for Conversion
  RATESPREAD BCD*8.7 Currency Rate Spread Allowed
  DATEMTCHCD String*1 Code for Rate Date Matching
  RATEOPER String*1 Currency Rate Operator
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  DRILAPP String*2 Drill Down Application Source
  RPTAMT BCD*10.3 Report Currency Amount
  VALUES Long Optional Fields

## GLPOSTO - Posted Trans. Optional Fields (view GL0405)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+FISCALYR+FISCALPERD+SRCECURN+SRCELEDGER+SRCETYPE+POSTINGSEQ+CNTDETAIL+OPTFIELD; OPTFIELD+ACCTID+FISCALYR+FISCALPERD+SRCECURN+SRCELEDGER+SRCETYPE+POSTINGSEQ+CNTDETAIL
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  FISCALYR String*4 Fiscal year
  FISCALPERD String*2 Fiscal period
  SRCECURN String*3 Source currency code
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  POSTINGSEQ BCD*4.0 Posting sequence number
  CNTDETAIL BCD*4.0 Detail count
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## GLPPC - Prov. Posting Journal Comments (view GL0028)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Prov. Posting Sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMMENT String*250 Journal detail comment
  REFERENCE String*60 Journal detail reference

## GLPPD - Prov. Posting Journal Details (view GL0014)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR; ACCTID [D,M]; POSTINGSEQ+BATCHNBR+ENTRYNBR+FISCALYR+FISCALPERD+TRANSNBR [D,M]
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Prov. Posting sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  JRNLDATE Date Journal date
  FISCALYR String*4 Fiscal year
  FISCALPERD String*2 Fiscal period
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  EDITALLOWD Integer Reserved
  CONSOLIDAT Integer Consolidation occurred on post [0=No,1=Yes]
  ACCTID String*45 Account Number
  COMPANYID String*8 Company ID
  JNLDTLDESC String*60 Journal detail description
  JNLDTLREF String*60 Journal detail reference
  TRANSAMT BCD*10.3 Journal transaction amount
  TRANSQTY BCD*10.3 Journal transaction quantity
  SCURNDEC String*1 Nbr of source currency decimals
  SCURNAMT BCD*10.3 Source currency amount
  HCURNCODE String*3 Home currency code
  RATETYPE String*2 Currency rate table type
  SCURNCODE String*3 Source currency code
  RATEDATE Date Date of currency rate selected
  CONVRATE BCD*8.7 Currency rate for conversion
  RATESPREAD BCD*8.7 Currency rate spread allowed
  DATEMTCHCD String*1 Code for rate date matching
  RATEOPER String*1 Currency rate operator
  CODESTATUS Integer Printed status code [0=Not Printed,1=Printed]
  DATEENTRY Date Entry Date
  RPTAMT BCD*10.3 Report currency amount
  VALUES Long Optional Fields

## GLPPDO - Prov. Post Journal Opt. Fields (view GL0406)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR+OPTFIELD; OPTFIELD+POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Prov. Posting Sequence Number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal Entry Number
  TRANSNBR BCD*4.0 Journal Transaction Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## GLPPER - Provisional Posting Errors (view GL0013)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR+TRANSNBR+ERRORCNT
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Prov. Posting sequence number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal entry number
  TRANSNBR BCD*4.0 Journal transaction number
  ERRORCNT BCD*4.0 Error increment
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MSGCODE String*7 unused
  ERRDESC String*250 Description of error

## GLRED - Recurring Entry Details (view GL0042)
Keys (first = PK; D=dups allowed, M=modifiable): RECID+TRANSNBR
Fields (NAME type description [values]):
  RECID String*16 Recurring Entry Code
  TRANSNBR String*10 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTID String*45 Account Number
  COMPANYID String*8 Company ID
  TRANSAMT BCD*10.3 Amount
  TRANSQTY BCD*10.3 Quantity
  SCURNDEC String*1 Source Currency Decimals
  SCURNAMT BCD*10.3 Source Currency Amount
  HCURNCODE String*3 Home Currency
  RATETYPE String*2 Currency Rate Table
  SCURNCODE String*3 Source Currency
  RATEDATE Date Currency Rate Date
  CONVRATE BCD*8.7 Currency Rate
  RATESPREAD BCD*8.7 Currency Rate Spread
  DATEMTCHCD String*1 Currency Rate Date Matching
  RATEOPER String*1 Currency Rate Operator
  TRANSDESC String*60 Description
  TRANSREF String*60 Reference
  TRANSDATE Date Recurring Entry Date
  SRCELDGR String*2 Source Ledger
  SRCETYPE String*2 Source Type
  COMMENT String*250 Comment
  ZEROSRCFG Boolean Zero Source Amount Flag
  VALUES Long Optional Fields

## GLREDO - Recur. Entry Optional Fields (view GL0403)
Keys (first = PK; D=dups allowed, M=modifiable): RECID+TRANSNBR+OPTFIELD; OPTFIELD+RECID+TRANSNBR
Fields (NAME type description [values]):
  RECID String*16 Recurring Entry Code
  TRANSNBR String*10 Sequence Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLREH - Recurring Journal Headers (view GL0041)
Keys (first = PK; D=dups allowed, M=modifiable): RECID; SCHEDKEY+SCHEDLINK [D,M]
Fields (NAME type description [values]):
  RECID String*16 Recurring Entry Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECDESC String*60 Recurring Entry Description
  DATESTART Date Start Date
  SWEXPIRE Integer Expiration Type [0=No Expiration Date,1=Specific Date]
  DATEEXPIRY Date Expiration Date
  DATERUN Date Last Run Date
  SWACTIVE Integer Status [0=Inactive,1=Active]
  DATEINACT Date Inactive Date
  DATEMAINT Date Last Maintained Date
  SRCELEDGER String*2 Source Ledger
  SRCETYPE String*2 Source Type
  SWREVERSE Integer Auto Reversal [0=Auto Reversal Off,1=Auto Reversal On]
  JRNLDESC String*60 Journal Entry Description
  SWEXRATE Integer Exchange Rate Switch [0=Use recurring entry rate,1=Use current rate]
  RDACCT String*45 Rounding Account
  RECDR BCD*10.3 Debits
  RECCR BCD*10.3 Credits
  RECQTY BCD*10.3 Quantity
  NCOUNT Integer Reserved
  SCHEDKEY String*12 Schedule
  SCHEDLINK BCD*10.0 Schedule Link
  ZEROSRCCNT BCD*10.0 Zero Source Amount Counter

## GLRPOST - Rollup Posted Transactions (view GL0066)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+FISCALYR+FISCALPERD+SRCECURN+SRCELEDGER+SRCETYPE+POSTINGSEQ+CNTDETAIL
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  FISCALYR String*4 Fiscal Year
  FISCALPERD String*2 Fiscal Period
  SRCECURN String*3 Source Currency Code
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  CNTDETAIL BCD*4.0 Detail Count
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  JRNLDATE Date Journal Date
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal Entry Number
  TRANSNBR BCD*4.0 Journal Transaction Number
  EDITALLOWD Integer Reserved
  CONSOLIDAT Integer Consolidation Occurred on Post [0=No,1=Yes]
  COMPANYID String*8 Company ID
  JNLDTLDESC String*60 Journal Detail Description
  JNLDTLREF String*60 Journal Detail Reference
  TRANSAMT BCD*10.3 Journal Transaction Amount
  TRANSQTY BCD*10.3 Journal Transaction Quantity
  SCURNDEC String*1 Nbr of Source Currency Decimals
  SCURNAMT BCD*10.3 Source Currency Amount
  HCURNCODE String*3 Home Currency Code
  RATETYPE String*2 Currency Rate Table Type
  SCURNCODE String*3 Source Currency Code
  RATEDATE Date Date of Currency Rate Selected
  CONVRATE BCD*8.7 Currency Rate for Conversion
  RATESPREAD BCD*8.7 Currency Rate Spread Allowed
  DATEMTCHCD String*1 Code for Rate Date Matching
  RATEOPER String*1 Currency Rate Operator
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  DRILAPP String*2 Drill Down Application Source
  RPTAMT BCD*10.3 Report Currency Amount
  VALUES Long Optional Fields
  FMTACCTD String*45 Formatted Account Number
  DACCTID String*45 Trans. Account Number
  DFMTACCTD String*45 Trans. Formatted Account Number

## GLRSTRT - General Ledger Restart (view GL0040)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Restart Key is View Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Restart Free Format Data

## GLRVAL - Revaluation Codes (view GL0020)
Keys (first = PK; D=dups allowed, M=modifiable): RVALID
Fields (NAME type description [values]):
  RVALID String*6 Revaluation Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  NETCHGSW Integer Revalue By [0=Balances   ,1=Net Changes]
  RATETYPE String*2 Rate Type
  SRCELDGR String*2 Source Code ID
  SRCETYPE String*2 Source Type
  ACCTGAIN String*45 Unrealized/Ex.Gain Acct ID
  ACCTLOSS String*45 Unrealized/Ex.Loss Acct ID
  RACCTGAIN String*45 Exchange Gain Acct ID
  RACCTLOSS String*45 Exchange Loss Acct ID

## GLRVL - Revaluation Details (view GL0104)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE+DFLTRVLCD
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency code to revalue
  DFLTRVLCD String*6 Default revaluation code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BATCHDESC String*60 Batch Description
  FORCEREVAL Integer Force revaluation switch [0=Revalue accounts which wish it,1=Force accounts which do not wish it]
  SGMTSLCT String*1 Select segment type
  SGMTID String*6 Select segment ID
  FROMACCTID String*45 From Account Number
  TOACCTID String*45 To Account Number
  FROMPERIOD String*2 From fiscal period
  TOPERIOD String*2 To fiscal period
  FSCSYR String*4 Fiscal year
  JRNLDATE Date Journal date
  CONVDATE Date Date used for conversion
  CONVRATE BCD*8.7 Conversion rate
  ACCTGAIN String*45 Unreal. Ex. Gain Account
  ACCTLOSS String*45 Unreal. Ex. Loss Account
  GVALUES Long Unreal. Ex. Gain Optional Flds
  LVALUES Long Unreal. Ex. Loss Optional Flds

## GLRVLGO - Reval. Dtls Gain Optional Flds (view GL0410)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE+DFLTRVLCD+OPTFIELD; OPTFIELD+CURNCYCODE+DFLTRVLCD
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency code to revalue
  DFLTRVLCD String*6 Default revaluation code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLRVLLO - Reval. Dtls Loss Optional Flds (view GL0411)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE+DFLTRVLCD+OPTFIELD; OPTFIELD+CURNCYCODE+DFLTRVLCD
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency code to revalue
  DFLTRVLCD String*6 Default revaluation code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLRVNET - Recognized Revaluation Restart (view GL0061)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+FSCSYR
Fields (NAME type description [values]):
  ACCTID String*45 Account
  FSCSYR String*4 Fiscal set year
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NETOBAL BCD*10.3 Net open balance
  NETEQV1 BCD*10.3 Period 01 net amount
  NETEQV2 BCD*10.3 Period 02 net amount
  NETEQV3 BCD*10.3 Period 03 net amount
  NETEQV4 BCD*10.3 Period 04 net amount
  NETEQV5 BCD*10.3 Period 05 net amount
  NETEQV6 BCD*10.3 Period 06 net amount
  NETEQV7 BCD*10.3 Period 07 net amount
  NETEQV8 BCD*10.3 Period 08 net amount
  NETEQV9 BCD*10.3 Period 09 net amount
  NETEQV10 BCD*10.3 Period 10 net amount
  NETEQV11 BCD*10.3 Period 11 net amount
  NETEQV12 BCD*10.3 Period 12 net amount
  NETEQV13 BCD*10.3 Period 13 net amount

## GLRVRAT - Recognized Reval. Rate Restart (view GL0062)
Keys (first = PK; D=dups allowed, M=modifiable): FSCSCURN+ACCTID+FSCSYR
Fields (NAME type description [values]):
  FSCSCURN String*3 Currency
  ACCTID String*45 Account
  FSCSYR String*4 Fiscal set year
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RVLRATE1 BCD*8.7 Period 01 rate
  RVLRATE2 BCD*8.7 Period 02 rate
  RVLRATE3 BCD*8.7 Period 03 rate
  RVLRATE4 BCD*8.7 Period 04 rate
  RVLRATE5 BCD*8.7 Period 05 rate
  RVLRATE6 BCD*8.7 Period 06 rate
  RVLRATE7 BCD*8.7 Period 07 rate
  RVLRATE8 BCD*8.7 Period 08 rate
  RVLRATE9 BCD*8.7 Period 09 rate
  RVLRATE10 BCD*8.7 Period 10 rate
  RVLRATE11 BCD*8.7 Period 11 rate
  RVLRATE12 BCD*8.7 Period 12 rate
  RVLRATE13 BCD*8.7 Period 13 rate

## GLSJN - Source Journal Profiles (view GL0019)
Keys (first = PK; D=dups allowed, M=modifiable): SRCEJRNL
Fields (NAME type description [values]):
  SRCEJRNL String*60 Source Journal Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRCELDGR01 String*2 Source Code ID 01
  SRCETYPE01 String*2 Source Type 01
  SRCELDGR02 String*2 Source Code ID 02
  SRCETYPE02 String*2 Source Type 02
  SRCELDGR03 String*2 Source Code ID 03
  SRCETYPE03 String*2 Source Type 03
  SRCELDGR04 String*2 Source Code ID 04
  SRCETYPE04 String*2 Source Type 04
  SRCELDGR05 String*2 Source Code ID 05
  SRCETYPE05 String*2 Source Type 05
  SRCELDGR06 String*2 Source Code ID 06
  SRCETYPE06 String*2 Source Type 06
  SRCELDGR07 String*2 Source Code ID 07
  SRCETYPE07 String*2 Source Type 07
  SRCELDGR08 String*2 Source Code ID 08
  SRCETYPE08 String*2 Source Type 08
  SRCELDGR09 String*2 Source Code ID 09
  SRCETYPE09 String*2 Source Type 09
  SRCELDGR10 String*2 Source Code ID 10
  SRCETYPE10 String*2 Source Type 10
  SRCELDGR11 String*2 Source Code ID 11
  SRCETYPE11 String*2 Source Type 11
  SRCELDGR12 String*2 Source Code ID 12
  SRCETYPE12 String*2 Source Type 12
  SRCELDGR13 String*2 Source Code ID 13
  SRCETYPE13 String*2 Source Type 13
  SRCELDGR14 String*2 Source Code ID 14
  SRCETYPE14 String*2 Source Type 14
  SRCELDGR15 String*2 Source Code ID 15
  SRCETYPE15 String*2 Source Type 15
  SRCELDGR16 String*2 Source Code ID 16
  SRCETYPE16 String*2 Source Type 16
  SRCELDGR17 String*2 Source Code ID 17
  SRCETYPE17 String*2 Source Type 17
  SRCELDGR18 String*2 Source Code ID 18
  SRCETYPE18 String*2 Source Type 18
  SRCELDGR19 String*2 Source Code ID 19
  SRCETYPE19 String*2 Source Type 19
  SRCELDGR20 String*2 Source Code ID 20
  SRCETYPE20 String*2 Source Type 20
  SRCELDGR21 String*2 Source Code ID 21
  SRCETYPE21 String*2 Source Type 21
  SRCELDGR22 String*2 Source Code ID 22
  SRCETYPE22 String*2 Source Type 22
  SRCELDGR23 String*2 Source Code ID 23
  SRCETYPE23 String*2 Source Type 23
  SRCELDGR24 String*2 Source Code ID 24
  SRCETYPE24 String*2 Source Type 24
  SRCELDGR25 String*2 Source Code ID 25
  SRCETYPE25 String*2 Source Type 25
  SRCELDGR26 String*2 Source Code ID 26
  SRCETYPE26 String*2 Source Type 26
  SRCELDGR27 String*2 Source Code ID 27
  SRCETYPE27 String*2 Source Type 27
  SRCELDGR28 String*2 Source Code ID 28
  SRCETYPE28 String*2 Source Type 28
  SRCELDGR29 String*2 Source Code ID 29
  SRCETYPE29 String*2 Source Type 29
  SRCELDGR30 String*2 Source Code ID 30
  SRCETYPE30 String*2 Source Type 30
  SRCELDGR31 String*2 Source Code ID 31
  SRCETYPE31 String*2 Source Type 31
  SRCELDGR32 String*2 Source Code ID 32
  SRCETYPE32 String*2 Source Type 32
  SRCELDGR33 String*2 Source Code ID 33
  SRCETYPE33 String*2 Source Type 33
  SRCELDGR34 String*2 Source Code ID 34
  SRCETYPE34 String*2 Source Type 34
  SRCELDGR35 String*2 Source Code ID 35
  SRCETYPE35 String*2 Source Type 35
  SRCELDGR36 String*2 Source Code ID 36
  SRCETYPE36 String*2 Source Type 36
  SRCELDGR37 String*2 Source Code ID 37
  SRCETYPE37 String*2 Source Type 37
  SRCELDGR38 String*2 Source Code ID 38
  SRCETYPE38 String*2 Source Type 38
  SRCELDGR39 String*2 Source Code ID 39
  SRCETYPE39 String*2 Source Type 39
  SRCELDGR40 String*2 Source Code ID 40
  SRCETYPE40 String*2 Source Type 40
  SRCELDGR41 String*2 Source Code ID 41
  SRCETYPE41 String*2 Source Type 41
  SRCELDGR42 String*2 Source Code ID 42
  SRCETYPE42 String*2 Source Type 42
  SRCELDGR43 String*2 Source Code ID 43
  SRCETYPE43 String*2 Source Type 43
  SRCELDGR44 String*2 Source Code ID 44
  SRCETYPE44 String*2 Source Type 44
  SRCELDGR45 String*2 Source Code ID 45
  SRCETYPE45 String*2 Source Type 45
  SRCELDGR46 String*2 Source Code ID 46
  SRCETYPE46 String*2 Source Type 46
  SRCELDGR47 String*2 Source Code ID 47
  SRCETYPE47 String*2 Source Type 47
  SRCELDGR48 String*2 Source Code ID 48
  SRCETYPE48 String*2 Source Type 48
  SRCELDGR49 String*2 Source Code ID 49
  SRCETYPE49 String*2 Source Type 49
  SRCELDGR50 String*2 Source Code ID 50
  SRCETYPE50 String*2 Source Type 50
  CARETNAME String*8 RESERVED-Functional Report Name
  CARETSNAM String*8 RESERVED-Source Report Name

## GLSRCE - Source Codes (view GL0002)
Keys (first = PK; D=dups allowed, M=modifiable): SRCELEDGER+SRCETYPE
Fields (NAME type description [values]):
  SRCELEDGER String*2 Source Ledger
  SRCETYPE String*2 Source Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRCEDESC String*60 Description

## GLWAMF - Preview Accounts (view GL0046)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID; ACCTGRPCOD+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL01+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL02+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL03+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL04+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL05+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL06+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL07+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL08+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL09+ACCTSEGVAL+ACCTID [D,M]; ACSEGVAL10+ACCTSEGVAL+ACCTID [D,M]; ACCTFMTTD [D,M]; ACCTGRPSCD+ACCTGRPCOD+ACCTSEGVAL+ACCTID [D,M]
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTDESC String*60 Description
  ACCTTYPE String*1 Type
  ACCTBAL String*1 Normal Balance DR/CR
  ACTIVESW Integer Status [0=Inactive,1=Active]
  CONSLDSW Integer Consolidate Journals [0=Detail,1=Consolidated,2=Prohibited]
  QTYSW Integer Quantities Allowed [0=No,1=Yes]
  UOM String*6 Unit of Measure
  ALLOCSW Integer Allocations Allowed
  ACCTOFSET String*45 Alloc Offset Account
  ACCTSRTY String*2 Alloc Source Type
  MCSW Integer Multicurrency [0=No,1=Yes]
  SPECSW Integer Specific Currency [0=All Currencies,1=Specific Currencies]
  ACCTGRPCOD String*12 Account Group Code
  CTRLACCTSW Integer Control Account [0=No,1=Yes]
  SRCELDGID String*2 Reserved
  ALLOCTOT BCD*8.7 Allocation Percent Total
  ABRKID String*6 Structure Code
  YRACCTCLOS BCD*4.0 Year Last Closed
  ACCTFMTTD String*45 Account Number
  ACSEGVAL01 String*15 Account Segment Code 1
  ACSEGVAL02 String*15 Account Segment Code 2
  ACSEGVAL03 String*15 Account Segment Code 3
  ACSEGVAL04 String*15 Account Segment Code 4
  ACSEGVAL05 String*15 Account Segment Code 5
  ACSEGVAL06 String*15 Account Segment Code 6
  ACSEGVAL07 String*15 Account Segment Code 7
  ACSEGVAL08 String*15 Account Segment Code 8
  ACSEGVAL09 String*15 Account Segment Code 9
  ACSEGVAL10 String*15 Account Segment Code 10
  ACCTSEGVAL String*15 Segment Code
  ACCTGRPSCD String*12 Account Group Sort Code
  POSTOSEGID String*6 Post to Segment ID
  POSTOSGCPY Integer Post to Segment ID Copy
  DEFCURNCOD String*3 Default Currency Code
  PROCESSSW Integer Process Switch [0=No,1=Yes]
  CREATESW Integer Create Switch [0=No,1=Yes]
  OVALUES Long Optional Fields
  TOVALUES Long Transaction Optional Fields

## GLWAMFO - Account Optional Fields (view GL0407)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+OPTFIELD; OPTFIELD+ACCTID
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## GLWAMTO - Account Trans. Optional Fields (view GL0408)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+OPTFIELD; OPTFIELD+ACCTID
Fields (NAME type description [values]):
  ACCTID String*45 Unformatted Account
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## GLWAVC - Preview A/C Valid Currencies (view GL0047)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+CURNID
Fields (NAME type description [values]):
  ACCTID String*45 Account Number
  CURNID String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REVALSW Integer Revaluation Switch [0=No,1=Yes]
  REVALID String*6 Revaluation Code

## GLWCAS - Preview Control A/C Subledgers (view GL0048)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTID+SRCELDGID
Fields (NAME type description [values]):
  ACCTID String*45 Account
  SRCELDGID String*2 Subledger
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
