# ZI module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## ZIAPDSD - AI Distribution Sets Detail (view ZI0015)
Keys (first = PK; D=dups allowed, M=modifiable): SRCCOMPID+DISTSET+DESCOMPID+ROUTENO+ACCTID
Fields (NAME type description [values]):
  SRCCOMPID String*6 Originator
  DISTSET String*6 Distribution Set
  DESCOMPID String*6 Destination
  ROUTENO Integer Route Number
  ACCTID String*45 G/L Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  PERCENT BCD*5.5 Percentage
  AMOUNT BCD*10.3 Amount

## ZIAPDSH - AI Distribution Sets Header (view ZI0014)
Keys (first = PK; D=dups allowed, M=modifiable): SRCCOMPID+DISTSET
Fields (NAME type description [values]):
  SRCCOMPID String*6 Originator
  DISTSET String*6 Distribution Set
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELASTMN Date Date Last Maintained
  CODETYPE Integer Code Type
  CODEMETH Integer Distr. Method [1=Spread Evenly,2=Fixed Percentage,3=Manual,4=Fixed Amount]
  CNTENTR BCD*4.0 Distributions Entered
  TOTPERC BCD*6.5 Total Percentage
  TOTAMT BCD*10.3 Total Amount
  SRCCUR String*3 Source Currency

## ZIAPTAX - AI Tax Accounts (view ZI0032)
Keys (first = PK; D=dups allowed, M=modifiable): SRCCOMPID+CODETAX+DESCOMPID
Fields (NAME type description [values]):
  SRCCOMPID String*6 Originator
  CODETAX String*12 Tax Authority
  DESCOMPID String*6 Destination
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTID String*45 Tax Account

## ZIGLAMF - Accounts (view ZI0029)
Keys (first = PK; D=dups allowed, M=modifiable): COMPID+ACCTID
Fields (NAME type description [values]):
  COMPID String*6 Company ID
  ACCTID String*45 Account ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTDESC String*60 Description
  ACCTTYPE String*1 Type
  ACCTBAL String*1 Normal Balance DR/CR
  ACTIVESW Integer Active [0=No,1=Yes]
  CONSLDSW Integer Consolidate Journals [0=Detail,1=Consolidated,2=Prohibited]
  QTYSW Integer Quantities Allowed [0=No,1=Yes]
  UOM String*6 Unit of Measure
  ALLOCSW Integer Allocations Allowed [0=No Allocation,1=Allocated by Account Balance,2=Allocated by Account Quantity]
  MCSW Integer Multicurrency [0=No,1=Yes]
  SPECSW Integer Specific Currency [0=All Currencies,1=Specific Currencies]
  CTRLACCTSW Integer Control Account [0=No,1=Yes]
  ABRKID String*6 Structure Code
  ACCTFMTTD String*45 Formatted Account ID
  DEFCURNCOD String*3 Default Currency Code

## ZIGLPS1 - GL Posting Journal Temp (view ZI0012)
Keys (first = PK; D=dups allowed, M=modifiable): ID; DESCOMPID+BTCHENTRY+TRANSNBR [D,M]
Fields (NAME type description [values]):
  ID BCD*4.0 ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESCOMPID String*6 Destination
  BATCHID String*6 Orig. Batch Number
  BTCHENTRY String*5 Orig. Entry Number
  TRANSNBR String*10 Orig. Line Number
  ACCTID String*45 G/L Account
  AMOUNT BCD*10.3 Amount
  QTY BCD*10.3 Quantity
  LEVEL Integer Route Level
  HCURNCODE String*3 Functional Currency
  SCURNCODE String*3 Source Currency
  RATETYPE String*2 Rate Type
  TRANSAMT BCD*10.3 Functional Amount
  HCURDEC Integer Source Company Currency Decimal
  UOM String*6
  CONVRATE BCD*8.7 Currency Rate for Conversion
  SCURNDEC String*1 Currency Decimals
  RATEOPER String*1 Rate Operator
  DATEMTCHCD String*1 Rate Date Match
  RATESPREAD BCD*8.7 Spread Allowed
  RATEDATE Date Rate Date
  SWPSTSRCE Integer Same as ICT Entry

## ZIGLPST - GL Posting (view ZI0013)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHFROM
Fields (NAME type description [values]):
  ALLBTCHSW Integer Post All Batches Switch [0=Post a range of batches,1=Post all batches]
  BATCHFROM String*6 From Batch Number
  BATCHTO String*6 To Batch Number

## ZILARC1 - Selected Companies (view ZI0024)
Keys (first = PK; D=dups allowed, M=modifiable): USERID+COMPID
Fields (NAME type description [values]):
  USERID String*8 User ID
  COMPID String*6 Company
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWINCLUDE Integer Include [0=No,1=Yes]
  SWALL Integer Select All [0=No,1=Yes]
  YEAR String*4 Year
  PERDENDDT Date Period End Date

## ZILARC2 - Loan Accounts Recon. (view ZI0025)
Keys (first = PK; D=dups allowed, M=modifiable): COMPORIG+ACCTORIG+COMPDES+ACCTDES; COMPDES+ACCTDES+COMPORIG+ACCTORIG [D,M]; USERID [D,M]
Fields (NAME type description [values]):
  COMPORIG String*6 Originator
  ACCTORIG String*45 Originating Account
  COMPDES String*6 Destination
  ACCTDES String*45 Destination Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USERID String*8 User ID
  CURORIG String*3 Originating Currency
  CURDES String*3 Destination Currency
  RATETPORIG String*2 Originating Rate Type
  RATETPDES String*2 Destination Rate Type
  DECIORIG String*1 Originating Decimals
  DECIDES String*1 Destination Decimals
  AMTORIG BCD*10.3 Originating Amount
  AMTDES BCD*10.3 Destination Amount
  SWINACTIVE Integer Inactive Company Switch

## ZIORGS - Company Names (view ZI0003)
Keys (first = PK; D=dups allowed, M=modifiable): COMPID
Fields (NAME type description [values]):
  COMPID String*6 Company ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPNAME String*60 Company Name
  FUNCCUR String*3 Functional Currency
  APPLIC Long Activated Applications
  SWMULTI Integer Multicurrency
  SYSCOMPID String*6 System Company ID

## ZIROUTD - Route Details (view ZI0005)
Keys (first = PK; D=dups allowed, M=modifiable): ORGCOMPID+DESCOMPID+ROUTENO+LEVEL; LEVCOMPID [D,M]
Fields (NAME type description [values]):
  ORGCOMPID String*6 Originator
  DESCOMPID String*6 Destination
  ROUTENO Integer Route Number
  LEVEL Integer Level
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LEVCOMPID String*6 Level Company ID
  PRECMPA String*45 Previous Company Account
  NXTCMPA String*45 Next Company Account
  FUNCCUR String*3 Functional Currency
  CURRATETP String*2 Rate Type
  SWPSTSRCE Integer Keep Source Currency [0=Exclude Source Currency in G/L Posting,1=Include Source Currency in G/L Posting]

## ZIROUTH - Route Headers (view ZI0004)
Keys (first = PK; D=dups allowed, M=modifiable): ORGCOMPID+DESCOMPID+ROUTENO; ORGCOMPID [D,M]; DESCOMPID [D,M]
Fields (NAME type description [values]):
  ORGCOMPID String*6 Originator
  DESCOMPID String*6 Destination
  ROUTENO Integer Route Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ROUTENAME String*60 Route Description
  CNTLEVELS Long No. Of Levels
  STATUS Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Date Last Maintained
  DATEINACTV Date Inactive Date

## ZIRSTRT - Intercompany Transactions Restart (view ZI0030)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Restart Key is View Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Restart Free Format Data

## ZISTP - Options (view ZI0001)
Keys (first = PK; D=dups allowed, M=modifiable): ID
Fields (NAME type description [values]):
  ID String*5 Record ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FUNCCUR String*3 Home Currency
  MULTICUR Integer Multicurrency

## ZISTP2 - Company Setup (view ZI0002)
Keys (first = PK; D=dups allowed, M=modifiable): COMPID
Fields (NAME type description [values]):
  COMPID String*6 Company ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPDESC String*60 Company Name
  APCLRACCNT String*45 AP Clearing Account
  PSTAP Integer Post AP Batches [0=Yes,1=No]
  PSTGL Integer Post GL Batches [0=Yes,1=No]
  SYSCOMPID String*6 System Company ID
  FUNCCUR String*3 Functional Currency
  SWMULTI Integer Multicurrency [0=No,1=Yes]
  SWSTATUS Integer Company Status [0=Inactive,1=Active]
  APPLIC Long Activated Applications
  GLQTYDEC BCD*4.0 G/L Options Quantity Decimals

## ZIUNPST - UnPosted Batches (view ZI0023)
Keys (first = PK; D=dups allowed, M=modifiable): MODULE+SEQNO+COMPID+CNTBTCH
Fields (NAME type description [values]):
  MODULE String*2 Module
  SEQNO Integer Sequence Number
  COMPID String*6 Company
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPNAME String*60 Company Name
  BDRTOTAL BCD*10.3 Debit Total
  BCRTOTAL BCD*10.3 Credit Total
  BTCHTYPE Integer Batch Type
  BTCHSTAT Integer Batch Status
  LSTEDIT Date Last Edit Date
  USERID String*8 User ID
  SWMULTI Integer Multi Currency Comp
  DECIMALS Integer Decimals
  FUNCCUR String*3 Functional Currency
  ENTRYCNT BCD*4.0 No. of Entries
