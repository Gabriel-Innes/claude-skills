# BK module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## BKACCT - Banks (view BK0001)
Keys (first = PK; D=dups allowed, M=modifiable): BANK
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Description
  ADDR1 String*60 Address Line 1
  ADDR2 String*60 Address Line 2
  ADDR3 String*60 Address Line 3
  ADDR4 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State/Province
  COUNTRY String*30 Country
  POSTAL String*20 Zip/Postal Code
  CONTACT String*60 Contact
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  TRANSIT String*12 Transit Number
  MULTICUR Boolean Multicurrency [0=No,1=Yes]
  CURNSTMT String*3 Statement Currency
  INACTIVE Boolean Status [0=Active,1=Inactive]
  INACTDATE Date Inactive Date
  BKACCT String*22 Bank Account Number
  IDACCT String*45 Bank Account
  IDACCTERR String*45 Write-Off Account
  ERRSPREAD BCD*10.3 Error Spread
  LSTMNTND Date Last Maintained
  RECFY String*4 Fiscal Year
  RECFP Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  RECLSTFY String*4 Last Reconciliation Year
  RECLSTFP Integer Last Reconciliation Period
  RECLSTDATE Date Last Reconciliation Date
  RECLSTBAL BCD*10.3 Last Closing Statement Balance
  RECDATE Date Reconciliation Date
  RECSTMTDAT Date Statement Date
  RECSTMTBAL BCD*10.3 Statement Balance
  RECINTRANS BCD*10.3 Deposits in Transit
  RECOUTSTND BCD*10.3 Checks Outstanding
  RECBKENT BCD*10.3 Total Not Posted Bank Entries
  RECDEPOSIT BCD*10.3 Total Deposits
  RECCHECK BCD*10.3 Total Checks
  RECFCDEP BCD*10.3 Deposits To Fiscal Period
  RECFCCHK BCD*10.3 Checks To Fiscal Period
  RECFCDEPIT BCD*10.3 Deposits In Transit To Fisc.Per.
  RECFCCHKOS BCD*10.3 Checks Outstanding To Fisc.Per.
  RECRECALC Boolean Calculate Fiscal Period Data [0=Fiscal balances are up to date.,1=Fiscal balances need to be recalculated.]
  RECLSMDATE Date Last Statement Date
  RECFCBKENT BCD*10.3 Difference of Bank Entries To Fiscal Period
  RECFCENTRE BCD*10.3 Total Not Posted Bank Entries To Fiscal Period
  IDACCTCCC String*45 Credit Card Charges Account
  CCCSPREAD BCD*10.3 Credit Card Charge Spread
  EXSPREAD BCD*10.3 Exchange Rate Difference Spread
  RECWTERR BCD*10.3 Total Withdrawal Bank Errors
  RECWTWO BCD*10.3 Total Withdrawal Write Offs
  RECWTGAIN BCD*10.3 Total Withdrawal Exchange Gain
  RECWTLOSS BCD*10.3 Total Withdrawal Exchange Loss
  RECWTCCC BCD*10.3 Total Withdrawal Credit Card Charges
  RECWTCLR BCD*10.3 Total Withdrawal Cleared
  RECWTFUNAM BCD*10.3 Withdrawal Total
  RECWPERR BCD*10.3 Fiscal Withdrawal Bank Errors
  RECWPWO BCD*10.3 Fiscal Withdrawal Write Offs
  RECWPGAIN BCD*10.3 Fiscal Withdrawal Exchange Gain
  RECWPLOSS BCD*10.3 Fiscal Withdrawal Exchange Loss
  RECWPCCC BCD*10.3 Fiscal Withdrawal Credit Card Charges
  RECWPCLR BCD*10.3 Fiscal Withdrawal Cleared
  RECWPFUNAM BCD*10.3 Fiscal Withdrawal Total
  RECDTERR BCD*10.3 Total Deposit Bank Errors
  RECDTWO BCD*10.3 Total Deposit Write Offs
  RECDTGAIN BCD*10.3 Total Deposit Exchange Gain
  RECDTLOSS BCD*10.3 Total Deposit Exchange Loss
  RECDTCCC BCD*10.3 Total Deposit Credit Card Charges
  RECDTCLR BCD*10.3 Total Deposit Cleared
  RECDTFUNAM BCD*10.3 Deposit Total
  RECDPERR BCD*10.3 Fiscal Deposit Bank Errors
  RECDPWO BCD*10.3 Fiscal Deposit Write Offs
  RECDPGAIN BCD*10.3 Fiscal Deposit Exchange Gain
  RECDPLOSS BCD*10.3 Fiscal Deposit Exchange Loss
  RECDPCCC BCD*10.3 Fiscal Deposit Credit Card Charges
  RECDPCLR BCD*10.3 Fiscal Deposit Cleared
  RECDPFUNAM BCD*10.3 Fiscal Deposit Total
  RECWFCLR BCD*10.3 Fiscal Withdrawal Cleared To Future
  RECDFCLR BCD*10.3 Fiscal Deposit Cleared To Future
  FUNWTAMT BCD*10.3 Withdrawal Functional Total
  FUNWPAMT BCD*10.3 Fiscal Withdrawal Functional Total
  FUNDTAMT BCD*10.3 Deposit Functional Total
  FUNDPAMT BCD*10.3 Fiscal Deposit Functional Total
  CODETXGRP String*12 Tax Group Code
  TAXAUTH1 String*12 Tax Authorization 1
  TAXAUTH2 String*12 Tax Authorization 2
  TAXAUTH3 String*12 Tax Authorization 3
  TAXAUTH4 String*12 Tax Authorization 4
  TAXAUTH5 String*12 Tax Authorization 5
  TXVCLSS1 Integer Vendor Tax Class 1
  TXVCLSS2 Integer Vendor Tax Class 2
  TXVCLSS3 Integer Vendor Tax Class 3
  TXVCLSS4 Integer Vendor Tax Class 4
  TXVCLSS5 Integer Vendor Tax Class 5
  AGEPURGE Integer Days Before Eligible for Clearing
  POSTDATE Date Reconciliation Date
  LSTPOSTDAT Date Last Reconciliation Date
  LSTSTMTBAL BCD*10.3 Last Available Statement Balance
  RECCOMMENT String*60 Default Reconciliation Description
  RECWEXDIFF BCD*10.3 Withdrawals Cleared with Exch. Rate Diff.
  RECDEXDIFF BCD*10.3 Deposit Cleared with Exchange Rate Diff

## BKCCTYP - Credit Card Types (view BK0240)
Keys (first = PK; D=dups allowed, M=modifiable): CCTYPE
Fields (NAME type description [values]):
  CCTYPE String*12 Credit Card Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Boolean Status [0=Active,1=Inactive]
  LASTMAINT Date Last Maintained
  INACTDATE Date Inactive Date

## BKCUR - Bank Currencies (view BK0002)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+CURN
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  CURN String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RTYPCHK String*2 Check Rate Type
  RTYPDEP String*2 Deposit Rate Type
  GAINACCT String*45 Exchange Gain Account
  LOSSACCT String*45 Exchange Loss Account
  ROUNDACCT String*45 Rounding Account

## BKDCHK - Bank Services Integrity Check (view BK0100)
Keys (first = PK; D=dups allowed, M=modifiable): CHECKNBR
Fields (NAME type description [values]):
  CHECKNBR String*4 Integrity Check Option Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATECHK Date Date
  FROMBANK String*8 From Bank
  TOBANK String*8 To Bank
  DATACHK Integer Data Check [0=Don't Check,1=Check,2=Fix]
  ORPHANCHK Integer Orphan Check [0=Don't Check,1=Check,2=Fix]
  RESTART Integer Restart Recovery [0=Don't Check,1=Check,2=Fix]
  LOGTOFILE Boolean Log error [0=Don't log result,1=Log result to file]
  CONTROL Integer Journal Control [0=Don't Check,1=Check,2=Fix]

## BKDISTD - Bank Distribution Set Detail (view BK0440)
Keys (first = PK; D=dups allowed, M=modifiable): DSETCODE+LINE; DISTCODE+DSETCODE [D,M]
Fields (NAME type description [values]):
  DSETCODE String*6 Distribution Set Code
  LINE Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTCODE String*6 Distribution Code
  ACCT String*45 G/L Account
  AMOUNT BCD*10.3 Amount

## BKDISTH - Bank Distribution Set Header (view BK0445)
Keys (first = PK; D=dups allowed, M=modifiable): DSETCODE
Fields (NAME type description [values]):
  DSETCODE String*6 Distribution Set Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  LSTMNTND Date Last Maintained
  INACTIVE Boolean Status [0=Active,1=Inactive]
  INACTDATE Date Inactive Date
  DISTCUR String*3 Currency
  LINES Long Number of Lines

## BKENTD - Bank Entries (view BK0460)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINE
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINE Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTCODE String*6 Distribution Code
  REFERENCE String*60 Reference
  COMMENT String*60 Description
  AMOUNT BCD*10.3 Amount
  SRCEAMT BCD*10.3 Source Amount
  GLACCOUNT String*45 G/L Account
  ENTRYTYPE Integer Entry Type [0=User-entered,10=Unmatched OFX,19=Unmatched OFX correction,20=Unmatched OFX error]
  BIGCOMMENT String*250 Comments
  SWTAXBL Integer Taxable [0=No,1=Yes]
  TXAMTCALC Integer Tax Amount Calculation [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLSS1 Integer Tax Vendor Class 1
  TAXVCLSS2 Integer Tax Vendor Class 2
  TAXVCLSS3 Integer Tax Vendor Class 3
  TAXVCLSS4 Integer Tax Vendor Class 4
  TAXVCLSS5 Integer Tax Vendor Class 5
  TAXICLSS1 Integer Tax Item Class 1
  TAXICLSS2 Integer Tax Item Class 2
  TAXICLSS3 Integer Tax Item Class 3
  TAXICLSS4 Integer Tax Item Class 4
  TAXICLSS5 Integer Tax Item Class 5
  TAXINCL1 Integer Tax Include 1 [0=No,1=Yes]
  TAXINCL2 Integer Tax Include 2 [0=No,1=Yes]
  TAXINCL3 Integer Tax Include 3 [0=No,1=Yes]
  TAXINCL4 Integer Tax Include 4 [0=No,1=Yes]
  TAXINCL5 Integer Tax Include 5 [0=No,1=Yes]
  BASETAX1 BCD*10.3 Tax Base Amount 1
  BASETAX2 BCD*10.3 Tax Base Amount 2
  BASETAX3 BCD*10.3 Tax Base Amount 3
  BASETAX4 BCD*10.3 Tax Base Amount 4
  BASETAX5 BCD*10.3 Tax Base Amount 5
  TXCALCBASE Integer Tax Base Calculation Method [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMTTXBL BCD*10.3 Taxable AMount
  AMTNOTTXBL BCD*10.3 Non Taxable Amount
  AMTTAXTOT BCD*10.3 Tax Total
  AMTDOCTOT BCD*10.3 Document Total Before Tax
  AMTNETTOT BCD*10.3 Document Total Including Tax
  AMTDIST BCD*10.3 Tax Distribution amount
  AMTINCLUDE BCD*10.3 Total Included Amount
  AMTNETDIST BCD*10.3 Tax Net Distribution Amount
  AMTEXCLUDE BCD*10.3 Total Excluded Amount
  AMTGRODIST BCD*10.3 Tax Gross Distribution Amount
  AMTEXPENS1 BCD*10.3 Tax Expense Amount 1
  AMTEXPENS2 BCD*10.3 Tax Expense Amount 2
  AMTEXPENS3 BCD*10.3 Tax Expense Amount 3
  AMTEXPENS4 BCD*10.3 Tax Expense Amount 4
  AMTEXPENS5 BCD*10.3 Tax Expense Amount 5
  AMTRECVRB1 BCD*10.3 Tax Recoverable Amount 1
  AMTRECVRB2 BCD*10.3 Tax Recoverable Amount 2
  AMTRECVRB3 BCD*10.3 Tax Recoverable Amount 3
  AMTRECVRB4 BCD*10.3 Tax Recoverable Amount 4
  AMTRECVRB5 BCD*10.3 Tax Recoverable Amount 5
  AMTALLOC1 BCD*10.3 Tax Allocated Amount 1
  AMTALLOC2 BCD*10.3 Tax Allocated Amount 2
  AMTALLOC3 BCD*10.3 Tax Allocated Amount 3
  AMTALLOC4 BCD*10.3 Tax Allocated Amount 4
  AMTALLOC5 BCD*10.3 Tax Allocated Amount 5
  TOTAMTALOC BCD*10.3 Total Tax Allocated Amount
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXEXPNS1RC BCD*10.3 Tax Reporting Expensed 1
  TXEXPNS2RC BCD*10.3 Tax Reporting Expensed 2
  TXEXPNS3RC BCD*10.3 Tax Reporting Expensed 3
  TXEXPNS4RC BCD*10.3 Tax Reporting Expensed 4
  TXEXPNS5RC BCD*10.3 Tax Reporting Expensed 5
  TXRECVB1RC BCD*10.3 Tax Reporting Recoverable Amount 1
  TXRECVB2RC BCD*10.3 Tax Reporting Recoverable Amount 2
  TXRECVB3RC BCD*10.3 Tax Reporting Recoverable Amount 3
  TXRECVB4RC BCD*10.3 Tax Reporting Recoverable Amount 4
  TXRECVB5RC BCD*10.3 Tax Reporting Recoverable Amount 5
  TXALLOC1RC BCD*10.3 Tax Reporting Allocated Amount 1
  TXALLOC2RC BCD*10.3 Tax Reporting Allocated Amount 2
  TXALLOC3RC BCD*10.3 Tax Reporting Allocated Amount 3
  TXALLOC4RC BCD*10.3 Tax Reporting Allocated Amount 4
  TXALLOC5RC BCD*10.3 Tax Reporting Allocated Amount 5
  TXALOCRC BCD*10.3 Total Tax Reporting Allocated Amount
  TXTOTRC BCD*10.3 Total Tax Reporting Amount
  FUNNETTAX BCD*10.3 Functional Net of Tax
  FUNGRODIS BCD*10.3 Functional Gross Distribution Amount
  TAXVERSION Long Tax Version
  TXCALCRMET Integer Tax Calculation Reporting Method [0=No,1=Yes]
  CODECURNRC String*3 Tax Reporting Currency Code
  RATERC BCD*8.7 Tax Reporting Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide,0=Not Specified]
  EXPNSACNT1 String*45 Tax Expense Account 1
  EXPNSACNT2 String*45 Tax Expense Account 2
  EXPNSACNT3 String*45 Tax Expense Account 3
  EXPNSACNT4 String*45 Tax Expense Account 4
  EXPNSACNT5 String*45 Tax Expense Account 5
  RECBLACNT1 String*45 Tax Recoverable Account 1
  RECBLACNT2 String*45 Tax Recoverable Account 2
  RECBLACNT3 String*45 Tax Recoverable Account 3
  RECBLACNT4 String*45 Tax Recoverable Account 4
  RECBLACNT5 String*45 Tax Recoverable Account 5
  TAXRATE1 BCD*8.7 Tax Rate 1
  TAXRATE2 BCD*8.7 Tax Rate 2
  TAXRATE3 BCD*8.7 Tax Rate 3
  TAXRATE4 BCD*8.7 Tax Rate 4
  TAXRATE5 BCD*8.7 Tax Rate 5
  SRCECURN String*3 Reserved
  POSTDATE Date Reserved
  RATE BCD*8.7 Reserved
  RATEOP Integer Reserved
  FUNTXAMT1 BCD*10.3 Functional Tax Amount 1
  FUNTXAMT2 BCD*10.3 Functional Tax Amount 2
  FUNTXAMT3 BCD*10.3 Functional Tax Amount 3
  FUNTXAMT4 BCD*10.3 Functional Tax Amount 4
  FUNTXAMT5 BCD*10.3 Functional Tax Amount 5
  FUNTXBSE1 BCD*10.3 Functional Tax Base Amount 1
  FUNTXBSE2 BCD*10.3 Functional Tax Base Amount 2
  FUNTXBSE3 BCD*10.3 Functional Tax Base Amount 3
  FUNTXBSE4 BCD*10.3 Functional Tax Base Amount 4
  FUNTXBSE5 BCD*10.3 Functional Tax Base Amount 5
  FUNTOTTAX BCD*10.3 Functional Tax Total
  FUNTXEXP1 BCD*10.3 Functional Expensed Amount 1
  FUNTXEXP2 BCD*10.3 Functional Expensed Amount 2
  FUNTXEXP3 BCD*10.3 Functional Expensed Amount 3
  FUNTXEXP4 BCD*10.3 Functional Expensed Amount 4
  FUNTXEXP5 BCD*10.3 Functional Expensed Amount 5
  FUNTXRCB1 BCD*10.3 Functional Recoverable Amount 1
  FUNTXRCB2 BCD*10.3 Functional Recoverable Amount 2
  FUNTXRCB3 BCD*10.3 Functional Recoverable Amount 3
  FUNTXRCB4 BCD*10.3 Functional Recoverable Amount 4
  FUNTXRCB5 BCD*10.3 Functional Recoverable Amount 5
  FUNTXALOC1 BCD*10.3 Functional Allocated Amount 1
  FUNTXALOC2 BCD*10.3 Functional Allocated Amount 2
  FUNTXALOC3 BCD*10.3 Functional Allocated Amount 3
  FUNTXALOC4 BCD*10.3 Functional Allocated Amount 4
  FUNTXALOC5 BCD*10.3 Functional Allocated Amount 5
  FUNAMTALOC BCD*10.3 Functional Total Tax Allocated

## BKENTH - Bank Entries Header (view BK0450)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; ENTRYNBR; BANK+ENTRYNBR [D,M]; ENTRYNBR+POSTYEAR+POSTPERIOD [D,M]; BANK+SERIAL [D,M]
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ENTRYNBR String*22 Bank Entry Number
  BANK String*8 Bank Code
  TRANSDATE Date Date Created
  TRANSTYPE Integer Bank Entry Type [1=Withdrawals,2=Deposits]
  REFERENCE String*60 Entry Description
  COMMENT String*60 Comment(Reserved)
  TOTSRCEAMT BCD*10.3 Entry Total Without Tax
  TOTFUNCAMT BCD*10.3 Func. Entry Total Without Tax
  TOTSRCEGRO BCD*10.3 Entry Total
  TOTFUNCGRO BCD*10.3 Func. Entry Total
  RATETYPE String*2 Exchange Rate Type
  SRCECURN String*3 Bank Entry Currency
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEOP Integer Rate Operation [1=Multiply,2=Divide,0=Not Specified]
  POSTDATE Date Bank Entry Date
  POSTYEAR String*4 Bank Entry Year
  POSTPERIOD Integer Bank Entry Period
  COMPLETED Integer Completed Status [0=Not Completed,10=Completed]
  BIGCOMMENT String*250 Comments
  STATUS Integer Status [0=Not posted,1=Posted,2=Reversed,3=Cleared]
  RECDATE Date Reconcilation Date
  RECYEAR String*4 Reconcilation Year
  RECPERIOD Integer Reconcilation Period
  LINES Long Number of Lines
  SERIAL Long Bank Entry Serial Number
  RUNID Long Run Id
  TYPE Integer Payment Type [1=Check,5=Credit Card,6=Cash,7=Other]
  OFXTID String*50 OFX Transaction ID
  ENTRYTYPE Integer Entry Type [0=User-entered,10=Unmatched OFX,19=Unmatched OFX correction,20=Unmatched OFX error]
  DSETCODE String*6 Distribution Set
  PSTSEQ BCD*5.0 Posting Sequence

## BKFORM - Check Stocks (view BK0008)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+FORMID
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  FORMID String*6 Check Stock Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  CHECK BCD*5.0 Next Check Number
  STKTYPE Integer Stock Type [1=Combined Check and Advice,2=Checks Then Advices,3=Checks Only,4=Advices Only]
  FORMSPEC1 String*20 Check Form
  FORMSPEC2 String*20 Advice Form
  ADVICE BCD*5.0 Advice Lines Per Page
  LANGUAGE Integer Language [5658=English,7092=French,5845=Spanish,738=Australian,15719=Mexican,2857=Chinese (Simplified),2863=Chinese (Traditional)]

## BKGLREF - Bank G/L Integration (view BK0470)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDIST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [1=Transfers,2=Bank Entry,3=Bank Entry Detail,4=Bank Reconciliation]
  GLDIST Integer G/L Transaction field [1=G/L Entry Description,2=G/L Detail Reference,3=G/L Detail Description,4=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXAMPLE String*250 Transaction Entry Description
  SEPARATOR Integer Separator [1=*  Asterisk,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=.  Period,6={  Left Parenthesis,7=}  Right Parenthesis,8=#  Number Sign,9=   Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Posting Sequence,2=Reference,3=Description,4=Comment,5=Withdrawal Number,6=Payee ID,7=Payee Name,8=Batch Number,9=Deposit Number,10=Transfer Number,11=From Bank,12=To Bank,13=Bank Code,14=Distribution Code,15=Entry Number,16=Entry Description,17=Bank Entry Type,18=Reconciliation Description,19=Reconciliation Status,20=From Bank Account,21=To Bank Account]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Posting Sequence,2=Reference,3=Description,4=Comment,5=Withdrawal Number,6=Payee ID,7=Payee Name,8=Batch Number,9=Deposit Number,10=Transfer Number,11=From Bank,12=To Bank,13=Bank Code,14=Distribution Code,15=Entry Number,16=Entry Description,17=Bank Entry Type,18=Reconciliation Description,19=Reconciliation Status,20=From Bank Account,21=To Bank Account]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Posting Sequence,2=Reference,3=Description,4=Comment,5=Withdrawal Number,6=Payee ID,7=Payee Name,8=Batch Number,9=Deposit Number,10=Transfer Number,11=From Bank,12=To Bank,13=Bank Code,14=Distribution Code,15=Entry Number,16=Entry Description,17=Bank Entry Type,18=Reconciliation Description,19=Reconciliation Status,20=From Bank Account,21=To Bank Account]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Posting Sequence,2=Reference,3=Description,4=Comment,5=Withdrawal Number,6=Payee ID,7=Payee Name,8=Batch Number,9=Deposit Number,10=Transfer Number,11=From Bank,12=To Bank,13=Bank Code,14=Distribution Code,15=Entry Number,16=Entry Description,17=Bank Entry Type,18=Reconciliation Description,19=Reconciliation Status,20=From Bank Account,21=To Bank Account]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Posting Sequence,2=Reference,3=Description,4=Comment,5=Withdrawal Number,6=Payee ID,7=Payee Name,8=Batch Number,9=Deposit Number,10=Transfer Number,11=From Bank,12=To Bank,13=Bank Code,14=Distribution Code,15=Entry Number,16=Entry Description,17=Bank Entry Type,18=Reconciliation Description,19=Reconciliation Status,20=From Bank Account,21=To Bank Account]
  SEGCOUNT Integer Segment Counter

## BKJCTL - Bank Posting Journal Control (view BK0020)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FROMBANK String*8 From Bank
  TOBANK String*8 To Bank
  POSTDATE Date Date Posted to GL
  POSTUSER String*8 Posting User
  POSTSTAT Integer Posting Status [1=Posting,2=Pending print,3=Printed,5=Pending purge,4=Purging]
  PRINTDATE Date Last Date Journal Printed
  GLDEFER Boolean Create G/L Batches [0=During Posting,1=On Request Using Create G/L Batch Icon]
  GLCONSOL Integer Consolidate G/L Batches [1=Post all details,2=Account/Fiscal Period/Source Code,3=Account/Fiscal Period]
  GLAPPEND Integer Create G/L Transactions By [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  GLBATCH BCD*10.0 G/L Batch Number
  GLTRANS Boolean G/L Batch Transferred
  POSTTYPE Integer Posting Type [1=Reconciliation,2=Transfer,3=Bank Entries]
  BANKSEQ Long Bank Sequence

## BKJENTD - Bank Entries Journal Detail (view BK0660)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+SEQUENCENO+LINE
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  SEQUENCENO Long Sequence Number
  LINE Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTCODE String*6 Distribution Code
  REFERENCE String*60 Reference
  COMMENT String*60 Description
  AMOUNT BCD*10.3 Amount
  SRCEAMT BCD*10.3 Source Amount
  GLACCOUNT String*45 G/L Account
  ENTRYTYPE Integer Entry Type
  BIGCOMMENT String*250 Comments
  SWTAXBL Integer Taxable [0=No,1=Yes]
  TXAMTCALC Integer Tax Amount Calculation [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLSS1 Integer Tax Vendor Class 1
  TAXVCLSS2 Integer Tax Vendor Class 2
  TAXVCLSS3 Integer Tax Vendor Class 3
  TAXVCLSS4 Integer Tax Vendor Class 4
  TAXVCLSS5 Integer Tax Vendor Class 5
  TAXICLSS1 Integer Tax Item Class 1
  TAXICLSS2 Integer Tax Item Class 2
  TAXICLSS3 Integer Tax Item Class 3
  TAXICLSS4 Integer Tax Item Class 4
  TAXICLSS5 Integer Tax Item Class 5
  TAXINCL1 Integer Tax Include 1 [0=No,1=Yes]
  TAXINCL2 Integer Tax Include 2 [0=No,1=Yes]
  TAXINCL3 Integer Tax Include 3 [0=No,1=Yes]
  TAXINCL4 Integer Tax Include 4 [0=No,1=Yes]
  TAXINCL5 Integer Tax Include 5 [0=No,1=Yes]
  BASETAX1 BCD*10.3 Tax Base Amount 1
  BASETAX2 BCD*10.3 Tax Base Amount 2
  BASETAX3 BCD*10.3 Tax Base Amount 3
  BASETAX4 BCD*10.3 Tax Base Amount 4
  BASETAX5 BCD*10.3 Tax Base Amount 5
  TXCALCBASE Integer Tax Base Calculation Method [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMTTXBL BCD*10.3 Taxable AMount
  AMTNOTTXBL BCD*10.3 Non Taxable Amount
  AMTTAXTOT BCD*10.3 Tax Total
  AMTDOCTOT BCD*10.3 Document Total Before Tax
  AMTNETTOT BCD*10.3 Document Total Including Tax
  AMTDIST BCD*10.3 Tax Distribution amount
  AMTINCLUDE BCD*10.3 Total Included Amount
  AMTNETDIST BCD*10.3 Tax Net Distribution Amount
  AMTEXCLUDE BCD*10.3 Total Excluded Amount
  AMTGRODIST BCD*10.3 Tax Gross Distribution Amount
  AMTEXPENS1 BCD*10.3 Tax Expense Amount 1
  AMTEXPENS2 BCD*10.3 Tax Expense Amount 2
  AMTEXPENS3 BCD*10.3 Tax Expense Amount 3
  AMTEXPENS4 BCD*10.3 Tax Expense Amount 4
  AMTEXPENS5 BCD*10.3 Tax Expense Amount 5
  AMTRECVRB1 BCD*10.3 Tax Recoverable Amount 1
  AMTRECVRB2 BCD*10.3 Tax Recoverable Amount 2
  AMTRECVRB3 BCD*10.3 Tax Recoverable Amount 3
  AMTRECVRB4 BCD*10.3 Tax Recoverable Amount 4
  AMTRECVRB5 BCD*10.3 Tax Recoverable Amount 5
  AMTALLOC1 BCD*10.3 Tax Allocated Amount 1
  AMTALLOC2 BCD*10.3 Tax Allocated Amount 2
  AMTALLOC3 BCD*10.3 Tax Allocated Amount 3
  AMTALLOC4 BCD*10.3 Tax Allocated Amount 4
  AMTALLOC5 BCD*10.3 Tax Allocated Amount 5
  TOTAMTALOC BCD*10.3 Total Tax Allocated Amount
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXEXPNS1RC BCD*10.3 Tax Reporting Expensed 1
  TXEXPNS2RC BCD*10.3 Tax Reporting Expensed 2
  TXEXPNS3RC BCD*10.3 Tax Reporting Expensed 3
  TXEXPNS4RC BCD*10.3 Tax Reporting Expensed 4
  TXEXPNS5RC BCD*10.3 Tax Reporting Expensed 5
  TXRECVB1RC BCD*10.3 Tax Reporting Recoverable Amount 1
  TXRECVB2RC BCD*10.3 Tax Reporting Recoverable Amount 2
  TXRECVB3RC BCD*10.3 Tax Reporting Recoverable Amount 3
  TXRECVB4RC BCD*10.3 Tax Reporting Recoverable Amount 4
  TXRECVB5RC BCD*10.3 Tax Reporting Recoverable Amount 5
  TXALLOC1RC BCD*10.3 Tax Reporting Allocated Amount 1
  TXALLOC2RC BCD*10.3 Tax Reporting Allocated Amount 2
  TXALLOC3RC BCD*10.3 Tax Reporting Allocated Amount 3
  TXALLOC4RC BCD*10.3 Tax Reporting Allocated Amount 4
  TXALLOC5RC BCD*10.3 Tax Reporting Allocated Amount 5
  TXALOCRC BCD*10.3 Total Tax Reporting Allocated Amount
  TXTOTRC BCD*10.3 Total Tax Reporting Amount
  FUNNETTAX BCD*10.3 Functional Net of Tax
  FUNGRODIS BCD*10.3 Functional Gross Distribution Amount
  TAXVERSION Long Tax Version
  TXCALCRMET Integer Tax Calculation Reporting Method [0=No,1=Yes]
  CODECURNRC String*3 Tax Reporting Currency Code
  RATERC BCD*8.7 Tax Reporting Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operation
  EXPNSACNT1 String*45 Tax Expense Account 1
  EXPNSACNT2 String*45 Tax Expense Account 2
  EXPNSACNT3 String*45 Tax Expense Account 3
  EXPNSACNT4 String*45 Tax Expense Account 4
  EXPNSACNT5 String*45 Tax Expense Account 5
  RECBLACNT1 String*45 Tax Recoverable Account 1
  RECBLACNT2 String*45 Tax Recoverable Account 2
  RECBLACNT3 String*45 Tax Recoverable Account 3
  RECBLACNT4 String*45 Tax Recoverable Account 4
  RECBLACNT5 String*45 Tax Recoverable Account 5
  TAXRATE1 BCD*8.7 Tax Rate 1
  TAXRATE2 BCD*8.7 Tax Rate 2
  TAXRATE3 BCD*8.7 Tax Rate 3
  TAXRATE4 BCD*8.7 Tax Rate 4
  TAXRATE5 BCD*8.7 Tax Rate 5
  SRCECURN String*3 Reserved
  POSTDATE Date Reserved
  RATE BCD*8.7 Reserved
  RATEOP Integer Reserved
  FUNTXAMT1 BCD*10.3 Functional Tax Amount 1
  FUNTXAMT2 BCD*10.3 Functional Tax Amount 2
  FUNTXAMT3 BCD*10.3 Functional Tax Amount 3
  FUNTXAMT4 BCD*10.3 Functional Tax Amount 4
  FUNTXAMT5 BCD*10.3 Functional Tax Amount 5
  FUNTXBSE1 BCD*10.3 Functional Tax Base Amount 1
  FUNTXBSE2 BCD*10.3 Functional Tax Base Amount 2
  FUNTXBSE3 BCD*10.3 Functional Tax Base Amount 3
  FUNTXBSE4 BCD*10.3 Functional Tax Base Amount 4
  FUNTXBSE5 BCD*10.3 Functional Tax Base Amount 5
  FUNTOTTAX BCD*10.3 Functional Tax Total
  FUNTXEXP1 BCD*10.3 Functional Expensed Amount 1
  FUNTXEXP2 BCD*10.3 Functional Expensed Amount 2
  FUNTXEXP3 BCD*10.3 Functional Expensed Amount 3
  FUNTXEXP4 BCD*10.3 Functional Expensed Amount 4
  FUNTXEXP5 BCD*10.3 Functional Expensed Amount 5
  FUNTXRCB1 BCD*10.3 Functional Recoverable Amount 1
  FUNTXRCB2 BCD*10.3 Functional Recoverable Amount 2
  FUNTXRCB3 BCD*10.3 Functional Recoverable Amount 3
  FUNTXRCB4 BCD*10.3 Functional Recoverable Amount 4
  FUNTXRCB5 BCD*10.3 Functional Recoverable Amount 5
  FUNTXALOC1 BCD*10.3 Functional Allocated Amount 1
  FUNTXALOC2 BCD*10.3 Functional Allocated Amount 2
  FUNTXALOC3 BCD*10.3 Functional Allocated Amount 3
  FUNTXALOC4 BCD*10.3 Functional Allocated Amount 4
  FUNTXALOC5 BCD*10.3 Functional Allocated Amount 5
  FUNAMTALOC BCD*10.3 Functional Total Tax Allocated
  ENTRYAMT BCD*10.3 Statement Amount
  SRCEGROAMT BCD*10.3 Gross Source Amount
  FUNCGROAMT BCD*10.3 Gross Amount
  DISTCODED String*60 Distribution Code Description
  GLACCOUNTD String*60 G/L Account Description
  BANK String*8 Bank
  LINEONE Long Line
  TXGRPDESC String*60 Tax Group Description
  PROCESSCMD Integer Tax Process Command
  TXAU1DESC String*60 Tax Authority Description 1
  TXAU2DESC String*60 Tax Authority Description 2
  TXAU3DESC String*60 Tax Authority Description 3
  TXAU4DESC String*60 Tax Authority Description 4
  TXAU5DESC String*60 Tax Authority Description 5
  VCLS1DESC String*60 Vendor Tax Class Description 1
  VCLS2DESC String*60 Vendor Tax Class Description 2
  VCLS3DESC String*60 Vendor Tax Class Description 3
  VCLS4DESC String*60 Vendor Tax Class Description 4
  VCLS5DESC String*60 Vendor Tax Class Description 5
  ICLS1DESC String*60 Item Tax Class Description 1
  ICLS2DESC String*60 Item Tax Class Description 2
  ICLS3DESC String*60 Item Tax Class Description 3
  ICLS4DESC String*60 Item Tax Class Description 4
  ICLS5DESC String*60 Item Tax Class Description 5
  CURNRCDESC String*60 Tax Reporting Currency Description
  RATERCDESC String*60 Tax Reporting RateType Description
  RATETYPE String*2 Reserved
  RATEDATE Date Reserved
  RATESPREAD BCD*8.7 Reserved

## BKJENTH - Bank Entries Journal Header (view BK0665)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+SEQUENCENO
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ENTRYNBR String*22 Bank Entry Number
  BANK String*8 Bank Code
  TRANSDATE Date Date Created
  TRANSTYPE Integer Bank Entry Type
  REFERENCE String*60 Entry Description
  COMMENT String*60 Comment(Reserved)
  TOTSRCEAMT BCD*10.3 Total Source Amount
  TOTFUNCAMT BCD*10.3 Total Functional Amount
  TOTSRCEGRO BCD*10.3 Total Gross Source Amt
  TOTFUNCGRO BCD*10.3 Total Gross Functional Amt
  RATETYPE String*2 Exchange Rate Type
  SRCECURN String*3 Bank Entry Currency
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEOP Integer Rate Operation
  POSTDATE Date Bank Entry Date
  POSTYEAR String*4 Bank Entry Year
  POSTPERIOD Integer Bank Entry Period
  COMPLETED Integer Completed Status
  BIGCOMMENT String*250 Comments
  STATUS Integer Status
  RECDATE Date Reconcilation Date
  RECYEAR String*4 Reconcilation Year
  RECPERIOD Integer Reconcilation Period
  LINES Long Number of Lines
  SERIAL Long Bank Entry Serial Number
  RUNID Long Run Id
  TYPE Integer Payment Type
  OFXTID String*50 OFX Transaction ID
  ENTRYTYPE Integer Entry Type
  DSETCODE String*6 Distribution Set
  BANKD String*60 Bank Name
  BKACCT String*22 Bank Account
  BKSTMTCUR String*3 Bank Statement Currency
  DSETCODED String*60 Distribution Set Desc
  TOTSTMTAMT BCD*10.3 Total Statement Amount
  TRANSCUR String*3 Bank Entry Currency
  RECPENT BCD*10.3 Fiscal Entry Amount
  RECPENTREC BCD*10.3 Reconciled Entry Amount
  DEFENTNUM String*22 Default New Document Number
  PROCESSCMD Integer Process Command
  AGERECLD Integer Aging Recon. days
  RETENTNO Integer Keep Input Entry No.

## BKJERR - Bank Posting Error Journal (view BK0012)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+BANK+UNIQUE
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  BANK String*8 Bank Code
  UNIQUE Long Error Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ERRTEXT String*132 Description

## BKJRNL - Bank Posting Journal (view BK0011)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+BANK; PSTSEQ+BANKSEQ
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  BANK String*8 Bank Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Description
  ADDR1 String*60 Address Line 1
  ADDR2 String*60 Address Line 2
  ADDR3 String*60 Address Line 3
  ADDR4 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State
  COUNTRY String*30 Country
  POSTAL String*20 Zip/Postal Code
  CONTACT String*60 Contact
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  TRANSIT String*12 Transit Number
  MULTICUR Boolean Multicurrency Switch
  CURNSTMT String*3 Statement Currency
  INACTIVE Boolean Inactive Switch
  INACTDATE Date Date Inactived
  BKACCT String*22 Bank Account Number
  IDACCT String*45 Bank G/L Account
  IDACCTERR String*45 Bank Error G/L Account
  ERRSPREAD BCD*10.3 Error Spread
  LSTMNTND Date Last Maintained
  RECFY String*4 Fiscal Year
  RECFP Integer Fiscal Period
  RECLSTFY String*4 Last Fiscal Year
  RECLSTFP Integer Last Fiscal Period
  RECLSTDATE Date Last Reconciliation Date
  RECLSTBAL BCD*10.3 Last Closing Statement Balance
  RECDATE Date Reconciliation Date
  RECSTMTDAT Date Statement Date
  RECSTMTBAL BCD*10.3 Closing Statement Balance
  RECINTRANS BCD*10.3 Deposits in Transit
  RECOUTSTND BCD*10.3 Checks Outstanding
  RECBKERRPN BCD*10.3 Bank Error Pending Amount
  RECBKENT BCD*10.3 Bank Entries Amount
  RECBKERR BCD*10.3 Bank Error Amount
  RECEXGAIN BCD*10.3 Exchange Amount Gained
  RECEXLOSS BCD*10.3 Exchange Amount Lost
  RECDEPOSIT BCD*10.3 Total Deposits
  RECCHECK BCD*10.3 Total Checks
  RECFCDEP BCD*10.3 Deposits To Fiscal Period
  RECFCCHK BCD*10.3 Checks To Fiscal Period
  RECFCDEPIT BCD*10.3 Deposits In Transit To Fiscal Period
  RECFCCHKOS BCD*10.3 Checks Outstanding To Fiscal Period
  RECRECALC Boolean Recalculate Fiscal Period Data
  ADJBOOKBAL BCD*10.3 Adjusted Book Balance
  ADJSTMTBAL BCD*10.3 Adjusted Statement Balance
  BALANCES Boolean Bank Reconciliation Balanced
  ADJBALDIFF BCD*10.3 Adjusted Balance Difference
  CHKSERIAL Long Next Check Serial Number
  NXTDEPOSIT BCD*5.0 Next Deposit Number
  DEPSERIAL Long Next Deposit Serial Number
  RECAVAIL BCD*10.3 Current Balance
  RECBOOKBAL BCD*10.3 Reconciliation Book Balance
  RECLSMDATE Date Last Statement Date
  RECFCBKENT BCD*10.3 Bank Entries To Fiscal Period
  RECFCGAIN BCD*10.3 Exchange Gain To Fiscal Period
  RECFCLOSS BCD*10.3 Exchange Loss To Fiscal Period
  RECFCERRPN BCD*10.3 Bank Error Pending To Fiscal Period
  RECFCERR BCD*10.3 Bank Error To Fiscal Period
  RECFCENTRE BCD*10.3 Reconciled Entries To Fiscal Period
  IDACCTCCC String*45 Credit Card Charge G/L Account
  CCCSPREAD BCD*10.3 Credit Card Charge Spread
  EXSPREAD BCD*10.3 Exchange Rate Difference Spread
  RECWTERR BCD*10.3 Total Withdrawal Bank Errors
  RECWTWO BCD*10.3 Total Withdrawal Write Offs
  RECWTGAIN BCD*10.3 Total Withdrawal Exchange Gain
  RECWTLOSS BCD*10.3 Total Withdrawal Exchange Loss
  RECWTCCC BCD*10.3 Total Withdrawal Credit Card Charges
  RECWTCLR BCD*10.3 Total Withdrawal Cleared
  RECWTFUNAM BCD*10.3 Total Withdrawal Functional Amounts
  RECWPERR BCD*10.3 Fiscal Withdrawal Bank Errors
  RECWPWO BCD*10.3 Fiscal Withdrawal Write Offs
  RECWPGAIN BCD*10.3 Fiscal Withdrawal Exchange Gain
  RECWPLOSS BCD*10.3 Fiscal Withdrawal Exchange Loss
  RECWPCCC BCD*10.3 Fiscal Withdrawal Credit Card Charges
  RECWPCLR BCD*10.3 Fiscal Withdrawal Cleared
  RECWPFUNAM BCD*10.3 Fiscal Withdrawal Functional Amounts
  RECDTERR BCD*10.3 Total Deposit Bank Errors
  RECDTWO BCD*10.3 Total Deposit Write Offs
  RECDTGAIN BCD*10.3 Total Deposit Exchange Gain
  RECDTLOSS BCD*10.3 Total Deposit Exchange Loss
  RECDTCCC BCD*10.3 Total Deposit Credit Card Charges
  RECDTCLR BCD*10.3 Total Deposit Cleared
  RECDTFUNAM BCD*10.3 Total Deposit Functional Amounts
  RECDPERR BCD*10.3 Fiscal Deposit Bank Errors
  RECDPWO BCD*10.3 Fiscal Deposit Write Offs
  RECDPGAIN BCD*10.3 Fiscal Deposit Exchange Gain
  RECDPLOSS BCD*10.3 Fiscal Deposit Exchange Loss
  RECDPCCC BCD*10.3 Fiscal Deposit Credit Card Charges
  RECDPCLR BCD*10.3 Fiscal Deposit Cleared
  RECDPFUNAM BCD*10.3 Fiscal Deposit Functional Amounts
  CURRTYPE Integer Bank Statement Type
  RECTWO BCD*10.3 Total Write Offs
  RECTCCC BCD*10.3 Total Credit Card Charges
  RECPWO BCD*10.3 Fiscal Period Write Off
  RECPCCC BCD*10.3 Fiscal Period Credit Card Charges
  RECWTWOSUM BCD*10.3 Sum of Withdrawal Total Write Offs
  RECDTWOSUM BCD*10.3 Sum of Deposit Total Write Offs
  RECWPWOSUM BCD*10.3 Sum of Withdrawal Fiscal Write Offs
  RECDPWOSUM BCD*10.3 Sum of Deposit Fiscal Write Offs
  CURFUNC String*3 Functional Currency
  BANKSEQ Long Bank Sequence
  CODETXGRP String*12 Tax Group Code
  TAXAUTH1 String*12 Tax Authorization 1
  TAXAUTH2 String*12 Tax Authorization 2
  TAXAUTH3 String*12 Tax Authorization 3
  TAXAUTH4 String*12 Tax Authorization 4
  TAXAUTH5 String*12 Tax Authorization 5
  TXVCLSS1 Integer Vendor Tax Class 1
  TXVCLSS2 Integer Vendor Tax Class 2
  TXVCLSS3 Integer Vendor Tax Class 3
  TXVCLSS4 Integer Vendor Tax Class 4
  TXVCLSS5 Integer Vendor Tax Class 5
  RECWRCLR BCD*10.3 Withdrawals Cleared To Current
  RECDRCLR BCD*10.3 Deposits Cleared To Current
  POSTDATE Date Posting Date
  LSTPOSTDAT Date Last Reconciliation Posting Date
  RECCOMMENT String*60 Default Reconciliation Description
  RECWEXDIFF BCD*10.3 Checks Cleared with Exch. Rate Diff.
  RECDEXDIFF BCD*10.3 Deposit Cleared with Exchange Rate Diff
  LSTSTMTBAL BCD*10.3 Last Available Statement Balance

## BKJTFR - Transfer Audit (view BK0033)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+KEYSEQ; TRANSFERNR+PSTSEQ+KEYSEQ; OBANK+PSTSEQ+KEYSEQ; DBANK+PSTSEQ+KEYSEQ
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  KEYSEQ BCD*5.0 Key Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSFERNR String*22 Transfer Number
  DATE Date Date
  GLACCOUNT String*45 Transfer Adjustment G/L Account
  DESC String*60 Description
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  OBANK String*8 Transfer Bank Code
  ODESC String*60 Transfer Bank
  OGLACCOUNT String*45 Transfer Bank G/L Account
  OSRCECURN String*3 Transfer Source Currency
  ORATEDATE Date Transfer Rate Date
  ORATETYPE String*2 Transfer Rate Type
  ORATE BCD*8.7 Transfer Rate Factor
  ORATESPREA BCD*8.7 Transfer Rate Spread
  ORATEOP Integer Transfer Rate Operator
  OSAMOUNT BCD*10.3 Transfer Source Amount
  OFAMOUNT BCD*10.3 Transfer Functional Amount
  DBANK String*8 Deposit Bank Code
  DDESC String*60 Deposit Bank
  DGLACCOUNT String*45 Deposit Bank G/L Account
  DSRCECURN String*3 Deposit Source Currency
  DRATEDATE Date Deposit Rate Date
  DRATETYPE String*2 Deposit Rate Type
  DRATE BCD*8.7 Deposit Rate Factor
  DRATESPREA BCD*8.7 Deposit Rate Spread
  DRATEOP Integer Deposit Rate Operator
  DSAMOUNT BCD*10.3 Deposit Source Amount
  DFAMOUNT BCD*10.3 Deposit Functional Amount
  TRATE BCD*8.7 Source Rate Factor
  TRATEOP Integer Source Rate Operator [1=Multiply,2=Divide]
  TSRCECURN String*3 Source Source Currency
  TSAMOUNT BCD*10.3 Source Source Amount
  TFAMOUNT BCD*10.3 Source Functional Amount
  OCURNSTMT String*3 Transfer Currency Statement
  OMULTICUR Boolean Transfer Multicurrency?
  DCURNSTMT String*3 Deposit Currency Statement
  DMULTICUR Boolean Deposit Multicurrency?
  OSRCECURND String*60 Transfer Bank Currency Description
  DSRCECURND String*60 Deposit Bank Currency Description
  FUNCTCURN String*3 Functional Currency
  POSTDATE Date Post Date

## BKJTFRD - Transfer Audit Charge (view BK0645)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+KEYSEQ+LINE
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  KEYSEQ BCD*5.0 Key Sequence
  LINE Integer Charge Line [0=Originating Bank,1=Destination Bank]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BANK String*8 Charge Bank
  TYPE String*6 Transfer Charge Distrib. Code
  GLACCOUNT String*45 Transfer Charge G/L Account
  SRCECURN String*3 Transfer Charge Source Currency
  SRCEAMT BCD*10.3 Transfer Charge Source Amount
  RATETYPE String*2 Exchange Rate Type
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  FAMOUNT BCD*10.3 Transfer Charge Functional Amt.
  GLACCHG Boolean Transfer Charge G/L Override
  GLACCOUNTD String*60 Charge G/L Description
  SWTAXBL Integer Taxable [0=No,1=Yes]
  TXAMTCALC Integer Tax Amount Calculation [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLSS1 Integer Tax Vendor Class 1
  TAXVCLSS2 Integer Tax Vendor Class 2
  TAXVCLSS3 Integer Tax Vendor Class 3
  TAXVCLSS4 Integer Tax Vendor Class 4
  TAXVCLSS5 Integer Tax Vendor Class 5
  TAXICLSS1 Integer Tax Item Class 1
  TAXICLSS2 Integer Tax Item Class 2
  TAXICLSS3 Integer Tax Item Class 3
  TAXICLSS4 Integer Tax Item Class 4
  TAXICLSS5 Integer Tax Item Class 5
  TAXINCL1 Integer Tax Include 1 [0=No,1=Yes]
  TAXINCL2 Integer Tax Include 2 [0=No,1=Yes]
  TAXINCL3 Integer Tax Include 3 [0=No,1=Yes]
  TAXINCL4 Integer Tax Include 4 [0=No,1=Yes]
  TAXINCL5 Integer Tax Include 5 [0=No,1=Yes]
  BASETAX1 BCD*10.3 Tax Base Amount 1
  BASETAX2 BCD*10.3 Tax Base Amount 2
  BASETAX3 BCD*10.3 Tax Base Amount 3
  BASETAX4 BCD*10.3 Tax Base Amount 4
  BASETAX5 BCD*10.3 Tax Base Amount 5
  BASETAXRC1 BCD*10.3 Tax Base Retainage amount1
  BASETAXRC2 BCD*10.3 Tax Base Retainage amount2
  BASETAXRC3 BCD*10.3 Tax Base Retainage amount3
  BASETAXRC4 BCD*10.3 Tax Base Retainage amount4
  BASETAXRC5 BCD*10.3 Tax Base Retainage amount5
  TXCALCBASE Integer Tax Base Calculation Method [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMTTXBL BCD*10.3 Taxable AMount
  AMTNOTTXBL BCD*10.3 Non Taxable Amount
  AMTTAXTOT BCD*10.3 Tax Total
  AMTDOCTOT BCD*10.3 Document Total Before Tax
  AMTNETTOT BCD*10.3 Document Total Including Tax
  AMTDIST BCD*10.3 Tax Distribution amount
  AMTINCLUDE BCD*10.3 Total Included Amount
  AMTEXCLUDE BCD*10.3 Total Excluded Amount
  AMTNETDIST BCD*10.3 Tax Net Distribution Amount
  AMTGRODIST BCD*10.3 Tax Gross Distribution Amount
  AMTEXPENS1 BCD*10.3 Tax Expense Amount 1
  AMTEXPENS2 BCD*10.3 Tax Expense Amount 2
  AMTEXPENS3 BCD*10.3 Tax Expense Amount 3
  AMTEXPENS4 BCD*10.3 Tax Expense Amount 4
  AMTEXPENS5 BCD*10.3 Tax Expense Amount 5
  AMTRECVRB1 BCD*10.3 Tax Recoverable AMount 1
  AMTRECVRB2 BCD*10.3 Tax Recoverable AMount 2
  AMTRECVRB3 BCD*10.3 Tax Recoverable AMount 3
  AMTRECVRB4 BCD*10.3 Tax Recoverable AMount 4
  AMTRECVRB5 BCD*10.3 Tax Recoverable AMount 5
  TOTAMTALOC BCD*10.3 Total Tax Allocated Amount
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXALOCRC BCD*10.3 Total Tax Reporting Alloc. Amt.
  TXEXPNSRC BCD*10.3 Tax Reporting Expensed Amount
  TXRECVBRC BCD*10.3 Tax Reporting Recoverable Amount
  TXTOTRC BCD*10.3 Total Tax Reporting Amount
  TAXVERSION Long Tax Version
  TXCALCRMET Integer Tax Calculation Reporting Method [0=No,1=Yes]
  EXPNSACNT1 String*45 Tax Expense Account 1
  EXPNSACNT2 String*45 Tax Expense Account 2
  EXPNSACNT3 String*45 Tax Expense Account 3
  EXPNSACNT4 String*45 Tax Expense Account 4
  EXPNSACNT5 String*45 Tax Expense Account 5
  RECBLACNT1 String*45 Tax Recoverable Account 1
  RECBLACNT2 String*45 Tax Recoverable Account 2
  RECBLACNT3 String*45 Tax Recoverable Account 3
  RECBLACNT4 String*45 Tax Recoverable Account 4
  RECBLACNT5 String*45 Tax Recoverable Account 5
  CODECURNRC String*3 Tax Reporting Currency Code
  TXGRPDESC String*60 Tax Group Description
  TXAU1DESC String*60 Tax Authority Description 1
  TXAU2DESC String*60 Tax Authority Description 2
  TXAU3DESC String*60 Tax Authority Description 3
  TXAU4DESC String*60 Tax Authority Description 4
  TXAU5DESC String*60 Tax Authority Description 5
  VCLS1DESC String*60 Vendor Tax Class Description 1
  VCLS2DESC String*60 Vendor Tax Class Description 2
  VCLS3DESC String*60 Vendor Tax Class Description 3
  VCLS4DESC String*60 Vendor Tax Class Description 4
  VCLS5DESC String*60 Vendor Tax Class Description 5
  ICLS1DESC String*60 Item Tax Class Description 1
  ICLS2DESC String*60 Item Tax Class Description 2
  ICLS3DESC String*60 Item Tax Class Description 3
  ICLS4DESC String*60 Item Tax Class Description 4
  ICLS5DESC String*60 Item Tax Class Description 5
  FUNGRODIS BCD*10.3 Func. Gross Distribution Amount
  FUNTXEXP1 BCD*10.3 Functional Expensed Amount 1
  FUNTXEXP2 BCD*10.3 Functional Expensed Amount 2
  FUNTXEXP3 BCD*10.3 Functional Expensed Amount 3
  FUNTXEXP4 BCD*10.3 Functional Expensed Amount 4
  FUNTXEXP5 BCD*10.3 Functional Expensed Amount 5
  FUNTXRCB1 BCD*10.3 Functional Recoverable Amount 1
  FUNTXRCB2 BCD*10.3 Functional Recoverable Amount 2
  FUNTXRCB3 BCD*10.3 Functional Recoverable Amount 3
  FUNTXRCB4 BCD*10.3 Functional Recoverable Amount 4
  FUNTXRCB5 BCD*10.3 Functional Recoverable Amount 5
  RATERC BCD*8.7 Tax Reporting Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operation
  CURNRCDESC String*60 Tax Reporting Currency Desc.
  RATERCDESC String*60 Tax Reporting RateType Desc.
  TAXRATE1 BCD*8.7 Tax Rate 1
  TAXRATE2 BCD*8.7 Tax Rate 2
  TAXRATE3 BCD*8.7 Tax Rate 3
  TAXRATE4 BCD*8.7 Tax Rate 4
  TAXRATE5 BCD*8.7 Tax Rate 5
  FUNNETTAX BCD*10.3 Functional Net of Tax
  FUNAMTALOC BCD*10.3 Functional Total Tax Allocated
  FUNTOTTAX BCD*10.3 Functional Tax Total
  AMTALLOC1 BCD*10.3 Tax Allocated Amount 1
  AMTALLOC2 BCD*10.3 Tax Allocated Amount 2
  AMTALLOC3 BCD*10.3 Tax Allocated Amount 3
  AMTALLOC4 BCD*10.3 Tax Allocated Amount 4
  AMTALLOC5 BCD*10.3 Tax Allocated Amount 5
  TXEXPNS1RC BCD*10.3 Tax Reporting Expensed 1
  TXEXPNS2RC BCD*10.3 Tax Reporting Expensed 2
  TXEXPNS3RC BCD*10.3 Tax Reporting Expensed 3
  TXEXPNS4RC BCD*10.3 Tax Reporting Expensed 4
  TXEXPNS5RC BCD*10.3 Tax Reporting Expensed 5
  TXRECVB1RC BCD*10.3 Tax Reporting Recoverable Amt. 1
  TXRECVB2RC BCD*10.3 Tax Reporting Recoverable Amt. 2
  TXRECVB3RC BCD*10.3 Tax Reporting Recoverable Amt. 3
  TXRECVB4RC BCD*10.3 Tax Reporting Recoverable Amt. 4
  TXRECVB5RC BCD*10.3 Tax Reporting Recoverable Amt. 5
  TXALLOC1RC BCD*10.3 Tax Reporting Allocated Amount 1
  TXALLOC2RC BCD*10.3 Tax Reporting Allocated Amount 2
  TXALLOC3RC BCD*10.3 Tax Reporting Allocated Amount 3
  TXALLOC4RC BCD*10.3 Tax Reporting Allocated Amount 4
  TXALLOC5RC BCD*10.3 Tax Reporting Allocated Amount 5
  FUNTXALOC1 BCD*10.3 Functional Allocated Amount 1
  FUNTXALOC2 BCD*10.3 Functional Allocated Amount 2
  FUNTXALOC3 BCD*10.3 Functional Allocated Amount 3
  FUNTXALOC4 BCD*10.3 Functional Allocated Amount 4
  FUNTXALOC5 BCD*10.3 Functional Allocated Amount 5

## BKJTRAND - Bank Journal Transaction Details (view BK0650)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+BANK+SERIAL+LINE
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  BANK String*8 Bank Code
  SERIAL Long Transaction Header Serial
  LINE Long Transaction Detail Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRCEAPP String*2 Source Application
  STATUS Integer Transaction Detail Status [1=Not Posted,2=Void,3=Outstanding,4=Reversed,5=Cleared,6=Cleared with bank error,7=Non-negotiable,8=Continuation,9=Printed,10=Cleared with write-off,11=Cleared with exchange rate difference,12=Cleared with credit card charge]
  TRANSTYPE Integer Transaction Type [1=Withdrawals,2=Deposits]
  TYPE Integer Detail Transaction Type [1=Check,2=EFT,3=Transfer,4=Service Charge,5=Credit Card,6=Cash,7=Other]
  IDREMIT String*24 Remittance ID
  DATEREMIT Date Transaction Date
  BTCHNBR BCD*5.0 Batch Number
  ENTRYNBR BCD*4.0 Entry Number
  POSTSEQ BCD*5.0 Posting Sequence Number
  REFERENCE String*60 Transaction Reference
  COMMENT String*60 Transaction Description
  PAYORID String*12 Payer Code
  PAYORNAME String*60 Payee Name
  VENDORNAME String*60 Vendor Name
  SRCEAMOUNT BCD*10.3 Source Transaction Amount
  FUNCAMOUNT BCD*10.3 Functional Transaction Amount
  RATETYPE String*2 Exchange Rate Type
  SRCECURN String*3 Receipt Currency
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEOP Integer Rate Operation [1=Multiply,2=Divide,0=Not Specified]
  DISTCODE String*6 Distribution Code
  GLACCOUNT String*45 G/L Account
  GLACCTOVR Boolean GL Account Override
  DDTYPE Integer Drilldown Type
  DDLINK BCD*10.0 Drilldown Link
  RECSTATUS Integer Reconciliation Status [1=Not Posted,2=Void,3=Outstanding,4=Reversed,5=Cleared,6=Cleared with bank error,7=Non-negotiable,8=Continuation,9=Printed,10=Cleared with write-off,11=Cleared with exchange rate difference,12=Cleared with credit card charge]
  RECSTATCHG Date Status Change Date
  RECCOMMENT String*60 Reconciliation Description
  RECCLEARED BCD*10.3 Cleared Amount
  POSTDATE Date Reconciliation Posting Date
  POSTYEAR String*4 Reconciliation Posting Year
  POSTPERIOD Integer Reconciliation Posting Period
  RECONCILED Boolean Reconciled
  RECPENDING BCD*10.3 Remaining In Transit Amount
  RECERR BCD*10.3 Reconciliation Error
  RECERRPEND BCD*10.3 Reconciliation Error Pending
  RECEXGAIN BCD*10.3 Reconciliation Exchange Gain
  RECEXLOSS BCD*10.3 Reconciliation Exchange Loss
  RECSUGGEST Integer Reconciliation Suggestion [1=Not Posted,2=Void,3=Outstanding,4=Reversed,5=Cleared,6=Cleared with bank error,7=Non-negotiable,8=Continuation,9=Printed,10=Cleared with write-off,11=Cleared with exchange rate difference,12=Cleared with credit card charge]
  RECAMOUNT BCD*10.3 Transaction Amount
  RECOUTSTND BCD*10.3 Outstanding Amount
  RECTARGET Integer Reconciliation Target
  RECCCC BCD*10.3 Reconciliation Credit Card Charge
  RECWOSUM BCD*10.3 Write-Off Amount
  CURFUNC String*3 Functional Currency
  CURSTMT String*3 Statement Currency
  SUMAMOUNT BCD*10.3 Summated Transaction Amount
  RECSPREAD BCD*10.3 Reconciliation Spread
  RECPAMOUNT BCD*10.3 Fiscal Transaction Remaining In Transit
  RECPOUTSTD BCD*10.3 Fiscal Outstanding Amount
  RECPWO BCD*10.3 Fiscal Write Offs
  RECPERR BCD*10.3 Fiscal Bank Errors
  RECPGAIN BCD*10.3 Fiscal Exchange Gain
  RECPLOSS BCD*10.3 Fiscal Exchange Loss
  RECPCCC BCD*10.3 Fiscal Credit Card Charge
  RECPCLR BCD*10.3 Fiscal Cleared
  RECPFUNAM BCD*10.3 Fiscal Functional Amount
  RECPORIG BCD*10.3 Fiscal Original Transaction Amount
  RECTBOOK BCD*10.3 Total Book Amount
  RECPBOOK BCD*10.3 Fiscal Book Amount
  RECTREMAIN BCD*10.3 Total Remaining Amount
  RECPREMAIN BCD*10.3 Fiscal Remaining Amount
  RECRWOSUM BCD*10.3 Fiscal Write-Off To This Period
  RECFCLR BCD*10.3 Fiscal Cleared To Future
  RECRCLR BCD*10.3 Fiscal Cleared To Current
  RECWOSUMR BCD*10.3 Current Period's Write-Off
  RECFCLRR BCD*10.3 Posted Fiscal Cleared To Future
  PAYMCODE String*12 Payment Code
  CHKFORM String*6 Check Stock Code
  OFXTID String*50 OFX Transaction ID
  RECDELTAF BCD*10.3 Future Reconciliation Delta
  FSCYEAR String*4 Fiscal Year
  FSCPERIOD Integer Fiscal Period
  REVDATE Date Reversal/Return Date
  SRCEDOCNUM String*22 Source Document Number
  CANREVINVC Integer Can Reverse Invoice [0=No,1=Yes]
  REVINVC Integer Reverse Invoice [0=No,1=Yes]
  COMPLETED Integer Reconciled and Journaled Transaction [0=Not Completed,10=Completed]
  ENTRYTYPE Integer Entry Type
  RECDELTA BCD*10.3 Reconciliation Amount Delta
  POSTED Date Document Posted Date

## BKJTRANH - Bank Journal Transaction Header (view BK0655)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+BANK+SERIAL; PSTSEQ+BANK+TRANSTYPE+SERIAL
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  BANK String*8 Bank Code
  SERIAL Long Transaction Header Serial
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*5.0 Transaction Number
  SRCEAPP String*2 Source Application
  TRANSTYPE Integer Transaction Type [1=Withdrawals,2=Deposits]
  OLDSERIAL Long Old Serial Number
  ENTRYTYPE Integer Entry Type [1=Bank Entered,2=Miscellaneous,3=Subledger,4=Transfer,5=Returned Customer Check,6=Alignment,7=Non Negotiable]
  REFERENCE String*60 Transaction Reference
  DESC String*60 Transaction Description
  TRANSDATE Date Transaction Date
  FSCYEAR String*4 Fiscal Year
  FSCPERIOD Integer Fiscal Period
  PRINTED Integer Transaction Slip Printed [0=No,1=Yes]
  TOTAMOUNT BCD*10.3 Transaction Total
  TOTBALAMT BCD*10.3 Transaction Remaining Balance Amount
  TOTCLEARED BCD*10.3 Fiscal Transaction Total
  NXTLINE Long Next Transaction Detail Line
  LINES Long Lines
  LINESPOST Long Lines In Transit
  LINESREC Long Lines Reconciled
  STATUS Integer Transaction Status [1=Not posted,2=Partially Outstanding,3=Outstanding,4=Partially reconciled,5=Reconciled,6=Pending Journal,7=Posted,8=Purged]
  RECERR BCD*10.3 Reconciliation Error
  RECERRPEND BCD*10.3 Reconciliation Error Pending
  RECEXGAIN BCD*10.3 Reconciliation Exchange Gain
  RECEXLOSS BCD*10.3 Reconciliation Exchange Loss
  RECAMOUNT BCD*10.3 Reconciliation Deposit Amount
  RECOUTSTND BCD*10.3 Reconciliation In Transit Amt
  SUMMARY Integer Transaction Recorded in Summary [0=Detail,1=Summary,2=Transfer,3=Bank Error]
  RECCCC BCD*10.3 Reconciliation Credit Card Charge
  RECCLEARED BCD*10.3 Amount Cleared
  RECFUNCAMT BCD*10.3 Functional Transaction Amount
  TOTFUNCAMT BCD*10.3 Functional Transaction Total
  TOCLEAR BCD*10.3 Reconciliation Cleared Amount
  TOWRITEOFF BCD*10.3 Write-Off Amount
  TOREMAIN BCD*10.3 In Transit Amount
  VARIANCE Integer Variance Type [0=None,1=Outstanding amount,2=Amount to write off,3=Bank error,4=Exchange rate difference,5=Credit card charge]
  LINESREVIN Long Lines Can Reverse Invoice
  POSTDATE Date Default Posting Date
  RECSTATUS Integer Default Reconciliation Status [1=Not Posted,2=Void,3=Outstanding,4=Reversed,5=Cleared,6=Cleared with bank error,7=Non-negotiable,8=Continuation,9=Printed,10=Cleared with write-off,11=Cleared with exchange rate difference,12=Cleared with credit card charge,13=Deleted]
  RECCOMMENT String*60 Default Reconciliation Desc.
  LINESJOUR Long Lines Journalled
  LINESPUR Long Lines Purged
  TOCLEARF BCD*10.3 Clear To Future Period
  RECFCLR BCD*10.3 Fiscal Cleared To Future
  RECRCLR BCD*10.3 Fiscal Cleared To Current
  COMPLETED Integer Reconciled and Journaled Transaction [0=Not Completed,10=Completed]
  RECWOSUMR BCD*10.3 Current Period's Write-Off
  TOCLEARR BCD*10.3 Clear To Reconciliation Period
  RECRWOSUM BCD*10.3 Fiscal Write-Off To This Period
  RECPREM BCD*10.3 Fiscal Remaining Outstanding
  RECTWO BCD*10.3 Total Delta Write Offs
  RECTERR BCD*10.3 Total Delta Bank Errors
  RECTGAIN BCD*10.3 Total Delta Exchange Gain
  RECTLOSS BCD*10.3 Total Delta Exchange Loss
  RECTCCC BCD*10.3 Total Delta Credit Card Charge
  RECTCLR BCD*10.3 Total Delta Cleared
  RECTFUNAM BCD*10.3 Total Delta Functional Amount
  CURFUNC String*3 Functional Currency
  CURSTMT String*3 Statement Currency
  RECWOSUM BCD*10.3 Reconciliation Write Off Sum
  POSTYEAR String*4 Reconciliation posting Year
  POSTPERIOD Integer Reconciliation posting Period
  RECDELTA BCD*10.3 Reconciliation Delta
  RECFCMISC BCD*10.3 Fiscal Miscellaneous Entry
  RECFCWMISC BCD*10.3 Withdrawal Misc. Entries To Fiscal Period
  RECFCDMISC BCD*10.3 Deposit Misc. Entries To Fiscal Period
  RECFWMISC BCD*10.3 Withdrawal Misc. Entries To Future Period
  RECFDMISC BCD*10.3 Deposit Misc. Entries To Future Period
  PAYORNAME String*60 Payment Payee Name
  VENDORNAME String*60 Payment Vendor Name
  ENTRYNBR String*22 Bank Entry/Transfer Number
  LINESPROC Long Lines Processed
  REVINVC Integer Reverse Invoice [0=No,1=Yes]
  GLACCOUNT String*45 G/L Account of Discrepancy

## BKJZGL - G/L Audit Summary (view BK0018)
Keys (first = PK; D=dups allowed, M=modifiable): PSTSEQ+KEYSEQ+DTLSEQ; SRCECURN+GLACCOUNT+PSTSEQ+KEYSEQ+DTLSEQ; GLACCOUNT+SRCECURN+PSTSEQ+KEYSEQ+DTLSEQ
Fields (NAME type description [values]):
  PSTSEQ BCD*5.0 Posting Sequence
  KEYSEQ BCD*5.0 Key Sequence
  DTLSEQ BCD*5.0 Detail Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GLACCOUNT String*45 G/L Account
  GLACCOUNTD String*60 G/L Account Description
  DESC String*60 Description
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  COMPONENT Integer Component [1=Transfer,2=Deposit,3=Transfer Charge,4=Deposit Charge,5=Adjustment,6=Transfer Charge Offset,7=Deposit Charge Offset,8=Bank Entries,9=Bank Reconciliation]
  SRCECURN String*3 Source Currency
  SAMOUNT BCD*10.3 Source Amount
  FAMOUNT BCD*10.3 Functional Amount

## BKOPT - Bank Options (view BK0010)
Keys (first = PK; D=dups allowed, M=modifiable): OPTIONNBR
Fields (NAME type description [values]):
  OPTIONNBR String*4 Bank Option
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NXTSEQ BCD*5.0 Next Posting Sequence
  GLDEFER Boolean Create G/L Batches [0=During Posting,1=On Request Using Create G/L Batch Icon]
  GLCONSOL Integer Consolidate G/L Batches [1=Do Not Consolidate,3=Consolidate by Account and Fiscal Period,2=Consolidate by Account, Fiscal Period, and Source]
  GLAPPEND Integer Create G/L Transactions By [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  TFRACCT String*45 Transfer Adjustment G/L Account
  TFRNUMBER BCD*10.0 Next Bank Transfer Number
  OFXNOPOST Boolean Suppress Unmatched OFX Posting
  CONTACT String*60 Contact Name
  PHONE String*30 Telephone
  FAX String*30 Fax Number
  BANK String*8 Default Bank Code
  SWRDATE Integer Clear in Future Period list [0=None,1=Warning,2=Error]
  SWDMETH Integer Deposit Write-Off Method [0=None,1=Prorate,2=Top Down]
  TFRDISTCOD String*6 Default Distribution Code
  TFRSRVCACT String*45 Default G/L Account
  TFRPFX String*6 Bank Transfer Prefix
  TFRDOCLEN BCD*2.0 Bank Transfer Length
  ENTRYPFX String*6 Bank Entry Prefix
  ENTDOCLEN BCD*2.0 Bank Entry Length
  ENTRYNUM BCD*10.0 Next Bank Entry Number
  SEQTFR Long Next Bank Transfer Doc. Seq.
  SEQENTRY Long Next Bank Entry Doc. Seq.
  SWRECONCIL Integer Reconcile List [0=Bank Services Balance,1=General Ledger Balance]
  NEXTRUNID Long Next Run Id

## BKREG - Bank Check Register (view BK0009)
Keys (first = PK; D=dups allowed, M=modifiable): SRCEAPP+APPRUNNUM+BANK+SORTCODE+PAYEEID; SRCEAPP+APPRUNNUM+BANK+LANGUAGE+SORTCODE
Fields (NAME type description [values]):
  SRCEAPP String*2 Source Application
  APPRUNNUM String*10 Application Run Number
  BANK String*8 Bank Code
  SORTCODE BCD*10.0 Sort Code
  PAYEEID String*12 Payee Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SERIAL Long Serial Number
  CHECK BCD*5.0 Check Number
  STATUS Integer Check Status [-2=Not Printed,-1=Advice Not Printed,9=Printed,999=Posted]
  CHKTYPE Integer Check Type [1=Check,2=EFT]
  CHKFORM String*6 Check Stock Code
  PAYEENAME String*60 Payee Name
  VENDORNAME String*60 Vendor Name
  REFERENCE String*60 Check Reference
  COMMENT String*60 Check Description
  POSTED Date Date Check Printed
  CHKDATE Date Check Date
  ISSUED BCD*10.3 Check Amount
  SISSUED BCD*10.3 Check Source Amount
  RATETYPE String*2 Exchange Rate Type
  SRCECURN String*3 Payment Currency
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEOP Integer Rate Operation [1=Multiply,2=Divide,0=Not Specified]
  EXTRA Binary*102 Extra Application Data
  LANGUAGE String*3 Language Code
  ADVICE BCD*5.0 Advice Lines
  FSCYEAR String*4 Fiscal Year
  FSCPERIOD Integer Fiscal Period
  LANGCODE Integer Language [5658=English,7092=French,5845=Spanish,738=Australian,15719=Mexican,2857=Chinese (Simplified),2863=Chinese (Traditional)]
  SDECIMALS Integer Source Currency Decimals
  DDTYPE Integer Drilldown Type
  DDLINK BCD*10.0 Drilldown Link
  PAYMCODE String*12 Payment Code
  SRCEDOCNUM String*22 Source Document Number
  CANREVINVC Integer Can Reverse Invoice [0=No,1=Yes]

## BKRSTRT - Bank Process Restart (view BK0820)
Keys (first = PK; D=dups allowed, M=modifiable): COMPANY+PROCESS
Fields (NAME type description [values]):
  COMPANY String*6 Company ID
  PROCESS String*8 Process Name
  AUDTDATE Date Date
  AUDTTIME Time Time
  AUDTUSER String*8 User
  AUDTORG String*6
  PARAMETERS Binary*255 Restart State
  MESSAGE String*255 Message

## BKTNUM - Bank Transaction Numbers (view BK0021)
Keys (first = PK; D=dups allowed, M=modifiable): BANK
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NXTDEPOSIT BCD*5.0 Next Deposit Slip Number
  DEPSERIAL Long Next Deposit Uniquifier
  NEXTSERIAL Long Next Serial Number

## BKTRAND - Bank Transaction Details (view BK0840)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+SERIAL+LINE; BANK+SERIAL+POSTYEAR+POSTPERIOD+LINE [D,M]; BANK+SERIAL+FSCYEAR+FSCPERIOD+LINE [D,M]; BANK+SERIAL+DATEREMIT+IDREMIT+LINE [D,M]; BANK+SERIAL+IDREMIT+DATEREMIT+LINE [D,M]; BANK+DATEREMIT+IDREMIT+SERIAL+LINE [D,M]; BANK+IDREMIT+DATEREMIT+SERIAL+LINE [D,M]
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  SERIAL Long Transaction Header Serial
  LINE Long Transaction Detail Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRCEAPP String*2 Source Application
  STATUS Integer Transaction Detail Status [1=Not Posted,2=Void,3=Outstanding,6=Cleared with bank error,4=Reversed,7=Non-negotiable,8=Continuation,9=Printed]
  TRANSTYPE Integer Transaction Type [1=Withdrawals,2=Deposits]
  TYPE Integer Detail Transaction Type [1=Check,2=EFT,3=Transfer,4=Service Charge,5=Credit Card,6=Cash,7=Other]
  IDREMIT String*24 Remittance ID
  DATEREMIT Date Transaction Date
  BTCHNBR BCD*5.0 Batch Number
  ENTRYNBR BCD*4.0 Entry Number
  POSTSEQ BCD*5.0 Posting Sequence Number
  REFERENCE String*60 Transaction Reference
  COMMENT String*60 Transaction Description
  PAYORID String*12 Payer Code
  PAYORNAME String*60 Payee Name
  VENDORNAME String*60 Vendor Name
  SRCEAMOUNT BCD*10.3 Source Transaction Amount
  FUNCAMOUNT BCD*10.3 Functional Transaction Amount
  RATETYPE String*2 Exchange Rate Type
  SRCECURN String*3 Receipt Currency
  RATEDATE Date Exchange Rate Date
  RATE BCD*8.7 Exchange Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEOP Integer Rate Operation [1=Multiply,2=Divide,0=Not Specified]
  DISTCODE String*6 Distribution Code
  GLACCOUNT String*45 G/L Account
  DDTYPE Integer Drilldown Type
  DDLINK BCD*10.0 Drilldown Link
  RECSTATUS Integer Reconciliation Status [1=Not Posted,2=Void,3=Outstanding]
  RECSTATCHG Date Status Change Date
  RECCOMMENT String*60 Reconciliation Description
  RECCLEARED BCD*10.3 Cleared Amount
  POSTDATE Date Reconciliation Posting Date
  POSTYEAR String*4 Reconciliation Posting Year
  POSTPERIOD Integer Reconciliation Posting Period [0=  ]
  RECONCILED Boolean Reconciled
  RECPENDING BCD*10.3 Remaining In Transit Amount
  PAYMCODE String*12 Payment Code
  CHKFORM String*6 Check Stock Code
  OFXTID String*50 OFX Transaction ID
  FSCYEAR String*4 Fiscal Year
  FSCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12,13=13]
  REVDATE Date Reversal/Return Date
  SRCEDOCNUM String*22 Source Document Number
  CANREVINVC Integer Can Reverse Invoice [0=No,1=Yes]
  REVINVC Integer Reverse Invoice [0=No,1=Yes]
  COMPLETED Integer Reconciled and Journaled Transaction [0=Not Completed,10=Completed]
  PSTSEQ BCD*5.0 Posting Sequence
  ENTRYTYPE Integer Entry Type
  POSTED Date Document Posted Date
  LSTRECSTAT Integer Last Reconciliation Status

## BKTRANH - Bank Transaction Header (view BK0845)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+SERIAL; BANK+TRANSTYPE+OLDSERIAL [D]; BANK+FSCYEAR+FSCPERIOD+SERIAL [D,M]; BANK+COMPLETED+TRANSDATE+SERIAL [D,M]; BANK+TRANSNUM+SERIAL [D,M]; BANK+COMPLETED+TRANSNUM+SERIAL [D,M]
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  SERIAL Long Transaction Header Serial
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*5.0 Transaction Number
  SRCEAPP String*2 Source Application
  TRANSTYPE Integer Transaction Type [1=Withdrawals,2=Deposits]
  OLDSERIAL Long Old Serial Number
  ENTRYTYPE Integer Entry Type [1=Bank Entered,2=Miscellaneous,3=Subledger,4=Transfer,5=Returned Customer Check,6=Alignment,7=Non Negotiable]
  REFERENCE String*60 Transaction Reference
  DESC String*60 Transaction Description
  TRANSDATE Date Transaction Date
  FSCYEAR String*4 Fiscal Year
  FSCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  PRINTED Integer Transaction Slip Printed [0=No,1=Yes]
  TOTAMOUNT BCD*10.3 Transaction Total
  TOTBALAMT BCD*10.3 Transaction Total in Statement
  TOTCLEARED BCD*10.3 Fiscal Transaction Total
  NXTLINE Long Next Transaction Detail Line
  LINES Long Lines
  LINESPOST Long Lines Outstanding
  LINESREC Long Lines Reconciled
  STATUS Integer Transaction Status [1=Not posted,2=Partially Outstanding,3=Outstanding,4=Partially reconciled,5=Reconciled,6=Pending Journal,7=Posted,8=Purged]
  RECERR BCD*10.3 Reconciliation Error
  RECERRPEND BCD*10.3 Reconciliation Error Pending
  RECEXGAIN BCD*10.3 Reconciliation Exchange Gain
  RECEXLOSS BCD*10.3 Reconciliation Exchange Loss
  RECAMOUNT BCD*10.3 Reconciliation Amount
  RECOUTSTND BCD*10.3 Reconciliation Outstanding Amt
  SUMMARY Integer Transaction Recorded in Summary [0=Detail,1=Summary,2=Transfer,3=Bank Error]
  RECCCC BCD*10.3 Reconciliation Credit Card Charge
  RECCLEARED BCD*10.3 Amount Cleared
  RECFUNCAMT BCD*10.3 Functional Transaction Amount
  TOTFUNCAMT BCD*10.3 Functional Transaction Total
  TOCLEAR BCD*10.3 Reconciliation Cleared Amount
  TOWRITEOFF BCD*10.3 Write-Off Amount
  TOREMAIN BCD*10.3 Outstanding Amount
  VARIANCE Integer Variance Type [0=None]
  LINESREVIN Long Lines Can Reverse Invoice
  POSTDATE Date Reconciliation Date
  RECSTATUS Integer Reconciliation Status [1=Not Posted,2=Void,9=Printed,7=Non-negotiable,8=Continuation]
  RECCOMMENT String*60 Reconciliation Description
  LINESJOUR Long Lines Journalled
  LINESPUR Long Lines Purged
  LINESPROC Long Lines Processed
  TOCLEARF BCD*10.3 Clear To Future Period
  RECFCLR BCD*10.3 Fiscal Cleared To Future
  RECRCLR BCD*10.3 Fiscal Cleared To Current
  COMPLETED Integer Reconciled and Journaled Transaction [0=Not Completed,10=Completed]
  PAYORNAME String*60 Payment Payee Name
  VENDORNAME String*60 Payment Vendor Name
  ENTRYNBR String*22 Bank Entry/Transfer Number
  LINESCCC Long Lines Credit Card
  LINESEXCH Long Lines Exchange Difference
  REVINVC Integer Reverse Invoice [0=No,1=Yes]

## BKTRANR - Bank Transaction Reversals (view BK0855)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+SEQUENCE
Fields (NAME type description [values]):
  BANK String*8 Bank Code
  SEQUENCE Long Detail Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWREVDOC Integer Reverse Document [0=No,1=Yes,2=Reversed]
  SWREVINVC Integer Reverse Invoice [3=Not Applicable,0=No,1=Yes,2=Reversed]
  REVDATE Date Reversal Date
  REVFISCYR String*4 Reversal Fiscal Year
  REVFISCPER Integer Reversal Fiscal Period
  REASON String*60 Reversal Reason
  SERIAL Long Transaction Header Serial
  LINE Long Transaction Detail Line
  SRCEAPP String*2 Source Application
  TRANSTYPE Integer Transaction Type
  ENTRYTYPE Integer Header Type
  DETAILTYPE Integer Detail Type
  IDREMIT String*24 Remittance ID
  DDTYPE Integer Drilldown Type
  DDLINK BCD*10.0 Drilldown Link
  DATEREMIT Date Remittance Date
  FUNCAMOUNT BCD*10.3 Transaction Functional Amount
  SRCEAMOUNT BCD*10.3 Transaction Source Amount
  SRCECURN String*3 Transaction Source Currency
  PAYORID String*12 Payor Code
  PAYORNAME String*60 Payor Name

## BKTT - Bank Distribution Codes (view BK0003)
Keys (first = PK; D=dups allowed, M=modifiable): TYPE
Fields (NAME type description [values]):
  TYPE String*6 Distribution Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  ACCT String*45 G/L Account
  LSTMNTND Date Last Maintained
  INACTIVE Boolean Status [0=Active,1=Inactive]
  INACTDATE Date Inactive Date

## BKTTX - Bank Distribution Codes Tax Details (view BK0860)
Keys (first = PK; D=dups allowed, M=modifiable): TYPE+AUTHORITY
Fields (NAME type description [values]):
  TYPE String*6 Distribution Code
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TXCLASS Integer Item Tax Class
  INCLUDED Integer Tax Included [0=No,1=Yes]

## BKUNMAT - OFX Transactions (view BK0870)
Keys (first = PK; D=dups allowed, M=modifiable): BANK+UNIQUE
Fields (NAME type description [values]):
  BANK String*8  Bank Code
  UNIQUE Long  Unique ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SERIAL Long  Serial Number of Bank Transaction
  LINE Long  Line Number of Bank Transaction
  DATE Date  Posted Date
  TYPE String*6  Distribution Code
  NUMBER String*12  Withdrawal Number
  REFERENCE String*60  Reference
  COMMENT String*60  Comment
  AMOUNT BCD*10.3  Amount
  SRCEAMT BCD*10.3  Source Amount
  STMTCURN String*3  Statement Currency
  AMTINSTMT Boolean  Is Amount in Statment Currency? [0=No,1=Yes]
  PAYEEID String*12  Payee Code
  PAYEENAME String*60  Payee Name
  RATETYPE String*2  Rate Type
  SRCECURN String*3  Source Currency
  RATEDATE Date  Rate Date
  RATE BCD*8.7  Rate
  RATESPREAD BCD*8.7  Rate Spread
  RATEOP Integer  Rate Operator [1=Multiply,2=Divide,0=Not Specified]
  GLACCOUNT String*45  G/L Account
  POSTNOW Boolean  Post Now? [0=No,1=Yes]
  ENTRYTYPE Integer  Entry Type [0=User-entered]
  TRXTYPE Integer  Distribution Code [1=Withdrawal,2=Deposit]
  OFXTID String*50  OFX Transaction ID
  RECYEAR String*4  Reconciliation Year
  RECPERIOD Integer  Reconciliation Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  RECONCILED Boolean  Match Found? [0=No,1=Yes]
