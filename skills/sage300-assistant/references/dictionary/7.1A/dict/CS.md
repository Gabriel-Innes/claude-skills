# CS module - compiled AOM dictionary

## CSAUTH - User Authorizations (view AS0002)
Keys (first = PK; D=dups allowed, M=modifiable): USERID+COMPANYID+PGMID
Fields (NAME type description [values]):
  USERID String*8 User ID
  COMPANYID String*6 Company ID
  PGMID String*2 Program ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PROFILEID String*8 Group ID

## CSCCD - Currency Codes (view CS0003)
Keys (first = PK; D=dups allowed, M=modifiable): CURID
Fields (NAME type description [values]):
  CURID String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CURNAME String*60 Description
  SYMBOL String*4 Symbol
  DECIMALS Integer Decimal Places [0=0,1=1,2=2,3=3]
  SYMBOLPOS Integer Symbol Position [1=Before with space,2=Before without space,3=After with space,4=After without space]
  THOUSSEP String*1 Thousands Separator
  DECSEP String*1 Decimal Separator
  NEGDISP Integer Negative Display [1=Trailing -,2=Leading -,3=Brackets ()]

## CSCOM - Company Profile (view CS0001)
Keys (first = PK; D=dups allowed, M=modifiable): ORGID
Fields (NAME type description [values]):
  ORGID String*6 Database ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONAME String*60 Name
  ADDR01 String*60 Address
  ADDR02 String*60 Address Line 2
  ADDR03 String*60 Address Line 3
  ADDR04 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State/Province
  POSTAL String*20 Zip/Postal Code
  COUNTRY String*30 Country
  LOCTYPE String*6 Location Type
  LOCCODE String*30 Location Code
  PHONEFMT Boolean Format Phone Number
  PHONE String*30 Telephone
  FAX String*30 Fax Number
  CONTACT String*60 Contact
  CNTRYCODE String*6 Country Code
  BRANCH String*6 Branch
  PERDFSC Integer Number of Fiscal Periods [12=12,13=13]
  QTR4PERD Integer Quarter with 4 Periods [1=1,2=2,3=3,4=4]
  HOMECUR String*3 Functional Currency
  MULTICURSW Boolean Multicurrency [0=No,1=Yes]
  RATETYPE String*2 Default Rate Type
  WARNDAYS Integer Warning Date Range
  EUROCURSW Boolean Euro
  REPORTCUR String*3 Reporting Currency
  HNDLCKFSC Integer Locked Fiscal Period [0=None,1=Warning,2=Error]
  HNDINAACCT Integer Inactive G/L Account [0=None,1=Warning,2=Error]
  HNDNEXACCT Integer Non-existent G/L Account [0=None,1=Warning,2=Error]
  GNLSSMTHD Integer Gain/Loss Accounting Method [1=Realized and Unrealized Gain/Loss,2=Recognized Gain/Loss]
  TAXNBR String*20 Tax Number
  LEGALNAME String*60 Legal Name
  BRN String*30 Business Registration Number
  EMAILHOST String*50 E-mail Host
  EMAILUSER String*50 E-mail Username
  EMAILPSWD Binary*100 E-mail Password
  EMAILPORT Integer E-mail Port
  EMAILSSL Boolean E-mail SSL Flag
  EMAILADDR String*50 E-mail From Address
  USESMTP Boolean Use SMTP
  CCADDR String*250 E-mail Cc Address
  BCCADDR String*250 E-mail Bcc Address
  SFPAORG Binary*240 Payments Acceptance Organization
  SFPACOMP Binary*32 Payments Acceptance Company
  SFPACNTRY Integer Payments Acceptance Country [0=None,1=Australia,2=Bahrain,3=Botswana,4=Canada,5=Cayman Islands,6=China,7=Colombia,8=Costa Rica,9=Dominican Republic,10=El Salvador,11=Guadeloupe and dependencies,12=Guatemala,13=Honduras,14=Hong Kong,15=India,16=Indonesia,17=Jamaica,18=Jordan,19=Kenya,20=Kuwait,21=Malaysia,22=Martinique,23=Mauritius,24=Mexico,25=Mozambique,26=New Zealand,27=Nicaragua,28=Oman,29=Panama,30=Philippines,31=Qatar,32=Saudi Arabia,33=Senegal,34=Singapore,35=South Africa,36=South Korea,37=Thailand,38=The Bahamas,39=United Arab Emirates,40=United States of America]
  EMAILMTHD Integer E-mail Send Method [0=Basic Authentication SMTP,1=Microsoft Graph]

## CSCRD - Currency Rates (view CS0006)
Keys (first = PK; D=dups allowed, M=modifiable): HOMECUR+RATETYPE+SOURCECUR+RATEDATE
Fields (NAME type description [values]):
  HOMECUR String*3 To Currency
  RATETYPE String*2 Rate Type
  SOURCECUR String*3 From Currency
  RATEDATE Date Rate Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RATE BCD*8.7 Rate
  SPREAD BCD*8.7 Spread
  DATEMATCH Integer Date Matching [1=Exact,2=Later,3=Earlier]
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]

## CSCRH - Currency Tables (view CS0005)
Keys (first = PK; D=dups allowed, M=modifiable): HOMECUR+RATETYPE
Fields (NAME type description [values]):
  HOMECUR String*3 To Currency
  RATETYPE String*2 Rate Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TABLEDESC String*60 Table Description
  DATEMATCH Integer Date Matching [1=Exact,2=Later,3=Earlier]
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATESRCE String*60 Source of Rates

## CSCRT - Rate Types (view CS0004)
Keys (first = PK; D=dups allowed, M=modifiable): RATETYPE
Fields (NAME type description [values]):
  RATETYPE String*2 Rate Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RATEDESC String*60 Description

## CSEUR - Euro Conversion Rates (view CS0010)
Keys (first = PK; D=dups allowed, M=modifiable): CURID; BLOCKMASTE+CURID
Fields (NAME type description [values]):
  CURID String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CURNAME String*60 Name
  RATE BCD*8.7 Rate
  ENTRYDATE Date Entry Date
  EXITDATE Date Exit Date
  BLOCKMASTE String*3 Block Master

## CSFSC - Fiscal Calendars (view CS0002)
Keys (first = PK; D=dups allowed, M=modifiable): FSCYEAR
Fields (NAME type description [values]):
  FSCYEAR String*4 Fiscal Year
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PERIODS Integer Number of Fiscal Periods [12=12,13=13]
  QTR4PERD Integer Quarter with 4 Periods [1=1,2=2,3=3,4=4]
  ACTIVE Boolean Active
  BGNDATE1 Date Fiscal Period 1 Start Date
  BGNDATE2 Date Fiscal Period 2 Start Date
  BGNDATE3 Date Fiscal Period 3 Start Date
  BGNDATE4 Date Fiscal Period 4 Start Date
  BGNDATE5 Date Fiscal Period 5 Start Date
  BGNDATE6 Date Fiscal Period 6 Start Date
  BGNDATE7 Date Fiscal Period 7 Start Date
  BGNDATE8 Date Fiscal Period 8 Start Date
  BGNDATE9 Date Fiscal Period 9 Start Date
  BGNDATE10 Date Fiscal Period 10 Start Date
  BGNDATE11 Date Fiscal Period 11 Start Date
  BGNDATE12 Date Fiscal Period 12 Start Date
  BGNDATE13 Date Fiscal Period 13 Start Date
  ENDDATE1 Date Fiscal Period 1 End Date
  ENDDATE2 Date Fiscal Period 2 End Date
  ENDDATE3 Date Fiscal Period 3 End Date
  ENDDATE4 Date Fiscal Period 4 End Date
  ENDDATE5 Date Fiscal Period 5 End Date
  ENDDATE6 Date Fiscal Period 6 End Date
  ENDDATE7 Date Fiscal Period 7 End Date
  ENDDATE8 Date Fiscal Period 8 End Date
  ENDDATE9 Date Fiscal Period 9 End Date
  ENDDATE10 Date Fiscal Period 10 End Date
  ENDDATE11 Date Fiscal Period 11 End Date
  ENDDATE12 Date Fiscal Period 12 End Date
  ENDDATE13 Date Fiscal Period 13 End Date
  STATUSADJ Integer Adjustment Period Status [1=Unlocked,0=Locked]
  STATUSCLS Integer Closing Period Status [1=Unlocked,0=Locked]

## CSFSCST - Fiscal Statuses (view CS0060)
Keys (first = PK; D=dups allowed, M=modifiable): FSCYEAR+PGMID
Fields (NAME type description [values]):
  FSCYEAR String*4 Fiscal Year
  PGMID String*2 Application
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATUS1 Integer Period 1 Status [1=Unlocked,0=Locked]
  STATUS2 Integer Period 2 Status [1=Unlocked,0=Locked]
  STATUS3 Integer Period 3 Status [1=Unlocked,0=Locked]
  STATUS4 Integer Period 4 Status [1=Unlocked,0=Locked]
  STATUS5 Integer Period 5 Status [1=Unlocked,0=Locked]
  STATUS6 Integer Period 6 Status [1=Unlocked,0=Locked]
  STATUS7 Integer Period 7 Status [1=Unlocked,0=Locked]
  STATUS8 Integer Period 8 Status [1=Unlocked,0=Locked]
  STATUS9 Integer Period 9 Status [1=Unlocked,0=Locked]
  STATUS10 Integer Period 10 Status [1=Unlocked,0=Locked]
  STATUS11 Integer Period 11 Status [1=Unlocked,0=Locked]
  STATUS12 Integer Period 12 Status [1=Unlocked,0=Locked]
  STATUS13 Integer Period 13 Status [1=Unlocked,0=Locked]

## CSOPT - Optional Tables (view CS0007)
Keys (first = PK; D=dups allowed, M=modifiable): TABLE+CODE
Fields (NAME type description [values]):
  TABLE String*8 Optional Table
  CODE String*30 Optional Table Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA String*40 Optional Data
  LENGTH Integer Maximum Code Length

## CSOPTCC - Opt. Fields Conversion Creation (view CS0015)
Keys (first = PK; D=dups allowed, M=modifiable): OPTFIELD
Fields (NAME type description [values]):
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FDESC String*60 Description
  TYPE Integer Type [1=Text,100=Amount,3=Date]
  LENGTH Integer Length
  OTABLE String*8 Old Optional Table ID
  ALLOWNULL Boolean Allow Blank [0=N/A,1=N/A]
  CREATED Boolean Optional Field Created [0=No,1=Yes]

## CSOPTCM - Opt. Fields Conversion Mapping (view CS0014)
Keys (first = PK; D=dups allowed, M=modifiable): PGMID+PGMVER+CONVINIID
Fields (NAME type description [values]):
  PGMID String*2 Application ID
  PGMVER String*3 Application Version
  CONVINIID String*10 Conversion ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OTITLE String*60 Old Optional Field Title
  OTYPE Integer Old Optional Field Type [1=Text,100=Amount,3=Date]
  OLENGTH Integer Old Optional Field Length
  OTABLE String*8 Old Optional Table ID
  NOPTFIELD String*12 New Optional Field ID
  NDEFVAL String*60 Default Optional Field Value

## CSOPTFD - Optional Field Values (view CS0012)
Keys (first = PK; D=dups allowed, M=modifiable): OPTFIELD+VALUE; OPTFIELD+SORTEDVAL
Fields (NAME type description [values]):
  OPTFIELD String*12 Optional Field
  VALUE String*60 Value
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SORTEDVAL String*60 Sorted Value
  VDESC String*60 Description
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=N/A,1=N/A]
  VALIDATE Boolean Validate [0=No,1=Yes]

## CSOPTFH - Optional Fields (view CS0011)
Keys (first = PK; D=dups allowed, M=modifiable): OPTFIELD
Fields (NAME type description [values]):
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FDESC String*60 Description
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=N/A,1=N/A]
  VALIDATE Boolean Validate [0=No,1=Yes]
  VALUES Long Values

## CSPFLOW - Process Flows (view CS0040)
Keys (first = PK; D=dups allowed, M=modifiable): USERID+PFLOW
Fields (NAME type description [values]):
  USERID String*8 User ID
  PFLOW String*128 Process Flow Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## CSPKGASN - CSPKGASN
Keys (first = PK; D=dups allowed, M=modifiable): ID+SCRNID+CMPID
Fields (NAME type description [values]):
  ID String*36
  SCRNID String*36
  CMPID String*6
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRIORITY Long
  STATUS Integer

## CSPKGD - CSPKGD
Keys (first = PK; D=dups allowed, M=modifiable): ID+SCRNID
Fields (NAME type description [values]):
  ID String*36
  SCRNID String*36
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60
  DESC String*255

## CSPKGH - CSPKGH
Keys (first = PK; D=dups allowed, M=modifiable): ID
Fields (NAME type description [values]):
  ID String*36
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*255
  VERSION String*18
  VENDOR String*60

## CSSEC - Security Groups (view AS0001)
Keys (first = PK; D=dups allowed, M=modifiable): PGMID+PGMVER+PROFILEID+RESOURCEID
Fields (NAME type description [values]):
  PGMID String*2 Program ID
  PGMVER String*3 Program Version
  PROFILEID String*8 Group ID
  RESOURCEID String*10 Resource ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PROFDESC String*60 Group Description

## CSSEQN - Sequence number dispenser (view CS0020)
Keys (first = PK; D=dups allowed, M=modifiable): KEYFIELD
Fields (NAME type description [values]):
  KEYFIELD Integer Placeholder
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTSEQUEN BCD*10.0 Next Sequence Number

## CSSKAP - Schedule Application Links (view CS0032)
Keys (first = PK; D=dups allowed, M=modifiable): SCHEDKEY+SCHEDLINK; APPLICATIO+AOPCODE+SCHEDKEY+SCHEDLINK
Fields (NAME type description [values]):
  SCHEDKEY String*12 Schedule Code
  SCHEDLINK BCD*10.0 Schedule Link
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  APPLICATIO String*2 Application
  AOPCODE String*4 Application Type
  AOPERATION String*60 Job Types
  ADESCRIPTI String*80 Description

## CSSKTB - Schedules (view CS0030)
Keys (first = PK; D=dups allowed, M=modifiable): SCHEDKEY
Fields (NAME type description [values]):
  SCHEDKEY String*12 Schedule Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SCHEDDESC String*60 Description
  INTERVAL Integer Interval [1=Daily,2=Weekly,3=Semimonthly,4=Monthly,5=Annual,11=Once]
  FREQUENCY Integer Frequency [1=Weekdays,2=Weekly,3=First and Date,4=Date and Last,5=Every]
  PHASE Integer Phase
  WEEKDAY Integer Weekday [1=Sunday,2=Monday,3=Tuesday,4=Wednesday,5=Thursday,6=Friday,7=Saturday]
  MONTHDAY Integer Day of Month [1=1st,2=2nd,3=3rd,4=4th,5=5th,6=6th,7=7th,8=8th,9=9th,10=10th,11=11th,12=12th,13=13th,14=14th,15=15th,16=16th,17=17th,18=18th,19=19th,20=20th,21=21st,22=22nd,23=23rd,24=24th,25=25th,26=26th,27=27th,28=28th,29=29th,30=30th,31=31st,99=Last]
  WEEK Integer Week in Month [1=First,2=Second,3=Third,4=Fourth,99=Last]
  MONTH Integer Month [1=January,2=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December]
  WDFSUN Integer Sunday Call [0=No,1=Yes]
  WDFMON Integer Monday Call [0=No,1=Yes]
  WDFTUE Integer Tuesday Call [0=No,1=Yes]
  WDFWED Integer Wednesday Call [0=No,1=Yes]
  WDFTHU Integer Thursday Call [0=No,1=Yes]
  WDFFRI Integer Friday Call [0=No,1=Yes]
  WDFSAT Integer Saturday Call [0=No,1=Yes]
  LASTDATE Date Last Run Date
  ACTIVEDATE Date Schedule Start Date
  REMINDLEAD Integer Remind in Advance
  USERMODE Integer User Mode [1=No Users,2=Specific User,3=All Users]
  USERID String*8 User ID

## CSUICSH - UI Cust. Profile Headers (view AS0005)
Keys (first = PK; D=dups allowed, M=modifiable): PROFILEID
Fields (NAME type description [values]):
  PROFILEID String*20 Profile ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PROFDESC String*60 Profile Description

## CSUICST - UI Cust. Profile Details (view AS0006)
Keys (first = PK; D=dups allowed, M=modifiable): PROFILEID+UIKEY+PGMID+PGMVER+CTRLTOHIDE
Fields (NAME type description [values]):
  PROFILEID String*20 Profile ID
  UIKEY String*35 Screen
  PGMID String*2 Program ID
  PGMVER String*3 Program Version
  CTRLTOHIDE String*40 Control to Hide
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## CSUSCST - User UI Customizations (view AS0007)
Keys (first = PK; D=dups allowed, M=modifiable): USERID+COMPANYID+PROFILEID
Fields (NAME type description [values]):
  USERID String*8 User ID
  COMPANYID String*6 Company ID
  PROFILEID String*20 Profile ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
