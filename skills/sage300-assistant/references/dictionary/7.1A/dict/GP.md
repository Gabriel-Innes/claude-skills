# GP module - compiled AOM dictionary

## GPGLBB - GL Subledger Transactions (view GP0100)
Keys (first = PK; D=dups allowed, M=modifiable): BSEQUENCE; SOURCEAPP+BSEQUENCE
Fields (NAME type description [values]):
  BSEQUENCE BCD*10.0 Batch Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SOURCEAPP String*2 Source Application
  DESC String*60 Description
  COMPANYID String*8 Company ID
  FUNCCUR String*3 Functional Currency
  FUNCCURDEC Integer Functional Currency Decimals
  NENTRIES BCD*10.0 Number of Entries
  NEXTENTRY BCD*10.0 Next Entry

## GPGLBD - GL Subledger Details (view GP0110)
Keys (first = PK; D=dups allowed, M=modifiable): BSEQUENCE+ESEQUENCE+DSEQUENCE
Fields (NAME type description [values]):
  BSEQUENCE BCD*10.0 Batch Sequence
  ESEQUENCE BCD*10.0 Entry Sequence
  DSEQUENCE BCD*10.0 Detail Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCOUNT String*45 Account Code
  SRCECUR String*3 Source Currency
  DESC String*60 Description
  REFERENCE String*60 Reference
  TRANSAMT BCD*10.3 Functional Amount
  TRANSQTY BCD*10.3 Quantity
  SRCEAMT BCD*10.3 Source Amount
  SRCEDEC Integer Source Currency Decimals
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  CONVRATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  RATEMTCHCD Integer Rate Matching Code [1=Exact,2=Later,3=Earlier]
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  TRANSDATE Date Transaction Date
  COMMENT String*250 Comment

## GPGLBH - GL Subledger Entries (view GP0120)
Keys (first = PK; D=dups allowed, M=modifiable): BSEQUENCE+ESEQUENCE; SOURCEAPP+SOURCETYPE+FISCYEAR+FISCPERIO+TRANSDATE+PSEQUENCE+BSEQUENCE+ESEQUENCE; SOURCEAPP+FISCYEAR+FISCPERIO+TRANSDATE+SOURCETYPE+PSEQUENCE+BSEQUENCE+ESEQUENCE; SOURCEAPP+BSEQUENCE+ESEQUENCE
Fields (NAME type description [values]):
  BSEQUENCE BCD*10.0 Batch Sequence
  ESEQUENCE BCD*10.0 Entry Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SOURCEAPP String*2 Source Application
  SOURCETYPE String*2 Transaction Type
  PSEQUENCE BCD*10.0 Posting Sequence
  ABATCHNUM BCD*5.0 Batch Number
  AENTRYNUM BCD*4.0 Entry Number
  DESC String*60 Description
  TRANSDATE Date Posting Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIO Integer Fiscal Period
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  DRILAPP String*2 Drill Down Application Source
  ENTEREDBY String*8 Entered By
  DOCDATE Date Document Date

## GPGLBO - GL Subledger Detail Opt. Fields (view GP0130)
Keys (first = PK; D=dups allowed, M=modifiable): BSEQUENCE+ESEQUENCE+DSEQUENCE+OPTFIELD; OPTFIELD+BSEQUENCE+ESEQUENCE+DSEQUENCE
Fields (NAME type description [values]):
  BSEQUENCE BCD*10.0 Batch Sequence
  ESEQUENCE BCD*10.0 Entry Sequence
  DSEQUENCE BCD*10.0 Detail Sequence
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

## GPRSTRT - GL Subledger Restart (view GP0140)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Restart Key is View Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Restart Free Format Data
