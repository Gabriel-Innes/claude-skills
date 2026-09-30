# TX module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## TXAUDD - Tax Tracking Item Class (view TX0012)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE+ITEMCLASS
Fields (NAME type description [values]):
  SEQUENCE BCD*10.0 Sequence
  ITEMCLASS Integer Item Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESCRIPTIO String*60 Description
  SBASEAMT BCD*10.3 Base Amt in Source Currency
  HBASEAMT BCD*10.3 Base Amt in Func. Currency
  TAXRATE BCD*8.5 Tax Rate
  SCURNTAX BCD*10.3 Tax Amt in Source Currency
  HCURNTAX BCD*10.3 Tax Amt in Func. Currrency
  TBASEAMT BCD*10.3 Base Amt in Tax Reporting Currency
  TCURNTAX BCD*10.3 Tax Amt in Tax Reporting Currency

## TXAUDH - Tax Tracking (view TX0011)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE; AUTHORITY+TYPE+FISCYEAR+FISCPERIOD+CUSTVEND+DOCDATE+SRCEAPP+DOCTYPE+DOCNUMBER+SEQUENCE; AUTHORITY+TYPE+CUSTVEND+DOCDATE+SRCEAPP+DOCTYPE+DOCNUMBER+SEQUENCE [D]
Fields (NAME type description [values]):
  SEQUENCE BCD*10.0
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AUTHORITY String*12 Tax Authority
  TYPE Integer Transaction Type [1=Sales,2=Purchases]
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  CUSTVEND String*12 Customer/Vendor ID
  DOCDATE Date Document Date
  SRCEAPP String*2 Source Application
  DOCTYPE String*2 Document Type
  DOCNUMBER String*22 Document No.
  POSTDATE Date Posting Date
  BUYERCLASS Integer Cust/Vend Tax Class
  COUNTRY String*30 Country Code
  REPORTDATE Date Report Date
  DESCRIPTIO String*60 Description
  ISFOREIGN Boolean Foreign Invoice
  HCURN String*3 Home Currency Code
  RATETYPE String*2 Rate Type
  SCURN String*3 Source Currency Code
  RATEDATE Date Rate Date
  RATE BCD*8.7 Rate
  CUSTVENDNM String*60 Customer/Vendor Name
  SDECIMAL Integer Decimals in Source Currency
  SINVAMT BCD*10.3 Invoice Amt in Source Currency
  HINVAMT BCD*10.3 Invoice Amt in Func. Currency
  RECOVERABL Boolean Recoverable
  EXPSEPARTE Boolean Expense Separately
  RATERECOV BCD*8.5 Recoverable Rate
  SRECOVRAMT BCD*10.3 Recov. Amt in Source Currency
  HRECOVRAMT BCD*10.3 Recov. Amt in Func. Currency
  TCURN String*3 Tax Reporting Currency Code
  TDECIMAL Integer Decimals in Tax Reporting Currency
  TRATETYPE String*2 Tax Reporting Rate Type
  TRATEDATE Date Tax Reporting Rate Date
  TRATE BCD*8.7 Tax Reporting Rate
  RATEOP Integer Rate Operation [1=Multiply,2=Divide  ]
  TRATEOP Integer Tax Reporting Rate Operation [1=Multiply,2=Divide  ]
  TRECOVRAMT BCD*10.3 Recov. Amt in Tax Reporting Currency

## TXAUTH - Tax Authorities (view TX0002)
Keys (first = PK; D=dups allowed, M=modifiable): AUTHORITY
Fields (NAME type description [values]):
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  SCURN String*3 Tax Reporting Currency
  MAXTAX BCD*10.3 Maximum Tax Allowable
  MINTAX BCD*10.3 No Tax Charged Below
  TXBASE Integer Tax Base [1=Selling price,2=Standard cost,3=Most recent cost,4=Alternate amount 1,5=Alternate amount 2]
  INCLUDABLE Boolean Allow Tax In Price [0=No,1=Yes]
  LIABTIMING Integer
  LIABILITY String*45 Tax Liability Account
  DEFER String*45
  DEFERRECOV String*45
  DISCBASE Boolean
  AUDITLEVEL Integer Report Level [1=At invoice level,0=No reporting]
  RECOVERABL Boolean Tax Recoverable [0=No,1=Yes]
  RATERECOV BCD*8.5 Recoverable Rate
  ACCTRECOV String*45 Recoverable Tax Account
  EXPSEPARTE Boolean Expense Separately [0=No,1=Yes]
  ACCTEXP String*45 Expense Account
  LASTMAINT Date Last Maintained
  TAXTYPE Integer Tax Type [10=Federal Tax,20=State Tax,30=County Tax,40=City Tax,0=Other,60=GST,70=PST,80=HST,90=VAT]
  TXRTGCTL Integer Report Tax on Retainage Document [0=No Reporting,1=At Time of Retainage Document,2=At Time of Original Document]

## TXCLASS - Tax Classes (view TX0001)
Keys (first = PK; D=dups allowed, M=modifiable): AUTHORITY+CLASSTYPE+CLASSAXIS+CLASS
Fields (NAME type description [values]):
  AUTHORITY String*12 Tax Authority
  CLASSTYPE Integer Transaction Type [1=Sales,2=Purchases]
  CLASSAXIS Integer Class Type [1=Customers,2=Items]
  CLASS Integer Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  EXEMPT Boolean Exempt [0=No,1=Yes]

## TXGRP - Tax Groups (view TX0003)
Keys (first = PK; D=dups allowed, M=modifiable): GROUPID+TTYPE
Fields (NAME type description [values]):
  GROUPID String*12 Tax Group
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  SRCCURN String*3 Tax Reporting Currency
  AUTHORITY1 String*12 Tax Authority 1
  AUTHORITY2 String*12 Tax Authority 2
  AUTHORITY3 String*12 Tax Authority 3
  AUTHORITY4 String*12 Tax Authority 4
  AUTHORITY5 String*12 Tax Authority 5
  TAXABLE1 Boolean Taxable 1 [0=No,1=Yes]
  TAXABLE2 Boolean Taxable 2 [0=No,1=Yes]
  TAXABLE3 Boolean Taxable 3 [0=No,1=Yes]
  TAXABLE4 Boolean Taxable 4 [0=No,1=Yes]
  TAXABLE5 Boolean Taxable 5 [0=No,1=Yes]
  CALCMETHOD Integer Tax Calculation Method [1=Calculate tax by summary,2=Calculate tax by detail]
  LASTMAINT Date Last Maintained
  SURTAX1 Boolean Surtax 1 [0=No,1=Yes]
  SURTAX2 Boolean Surtax 2 [0=No,1=Yes]
  SURTAX3 Boolean Surtax 3 [0=No,1=Yes]
  SURTAX4 Boolean Surtax 4 [0=No,1=Yes]
  SURTAX5 Boolean Surtax 5 [0=No,1=Yes]
  SURAUTH1 String*12 Surtax On Authority 1
  SURAUTH2 String*12 Surtax On Authority 2
  SURAUTH3 String*12 Surtax On Authority 3
  SURAUTH4 String*12 Surtax On Authority 4
  SURAUTH5 String*12 Surtax On Authority 5
  TRATETYPE String*2 Tax Reporting Rate Type

## TXRATE - Tax Rates (view TX0004)
Keys (first = PK; D=dups allowed, M=modifiable): AUTHORITY+TTYPE+BUYERCLASS
Fields (NAME type description [values]):
  AUTHORITY String*12 Tax Authority
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  BUYERCLASS Integer Buyer Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMRATE1 BCD*8.5 Item Rate 1
  ITEMRATE2 BCD*8.5 Item Rate 2
  ITEMRATE3 BCD*8.5 Item Rate 3
  ITEMRATE4 BCD*8.5 Item Rate 4
  ITEMRATE5 BCD*8.5 Item Rate 5
  ITEMRATE6 BCD*8.5 Item Rate 6
  ITEMRATE7 BCD*8.5 Item Rate 7
  ITEMRATE8 BCD*8.5 Item Rate 8
  ITEMRATE9 BCD*8.5 Item Rate 9
  ITEMRATE10 BCD*8.5 Item Rate 10
  LASTMAINT Date Last Maintained

## TXRSTRT - Tax Services Restart (view TX0021)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Restart Key is View Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Restart Free Format Data

## TXSTATED - Tax State Details (view TX0014)
Keys (first = PK; D=dups allowed, M=modifiable): GROUPID+TTYPE+VERSION+TXAUTHNUM
Fields (NAME type description [values]):
  GROUPID String*12 Tax Group
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  VERSION Long Version
  TXAUTHNUM Integer Tax Authority Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AUTHORITY String*12 Tax Authority
  DESC String*60 Description
  AUDITLEVEL Integer Report Level [1=At invoice level,0=No reporting]
  TAXABLE Integer Taxable [0=No,1=Yes]
  SURTAX Integer Surtax [0=No,1=Yes]
  SURAUTH String*12 Surtax On Authority
  MINTAX BCD*10.3 Maximum Tax Allowable
  MAXTAX BCD*10.3 No Tax Charged Below
  TXBASE Integer Tax Base [1=Selling price,2=Standard cost,3=Most recent cost,4=Alternate amount 1,5=Alternate amount 2]
  INCLUDABLE Integer Allow Tax In Price [0=No,1=Yes]
  TXRTGCTL Integer Report Tax on Retainage Document [0=No Reporting,1=At Time of Retainage Document,2=At Time of Original Document]
  RECOVERABL Integer Tax Recoverable [0=No,1=Yes]
  RATERECOV BCD*8.5 Recoverable Rate
  ACCTRECOV String*45 Recoverable Tax Account
  EXPSEPARTE Integer Expense Separately [0=No,1=Yes]
  ACCTEXP String*45 Expense Account
  LIABILITY String*45 Tax Liability Account
  HCLASS01 Integer Header Class 1 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS02 Integer Header Class 2 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS03 Integer Header Class 3 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS04 Integer Header Class 4 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS05 Integer Header Class 5 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS06 Integer Header Class 6 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS07 Integer Header Class 7 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS08 Integer Header Class 8 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS09 Integer Header Class 9 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  HCLASS10 Integer Header Class10 [0=Undefined,1=Exists,2=Exempt,3=Rates Defined]
  DCLASS01 Integer Detail Class 1 [0=Undefined,1=Exists,2=Exempt]
  DCLASS02 Integer Detail Class 2 [0=Undefined,1=Exists,2=Exempt]
  DCLASS03 Integer Detail Class 3 [0=Undefined,1=Exists,2=Exempt]
  DCLASS04 Integer Detail Class 4 [0=Undefined,1=Exists,2=Exempt]
  DCLASS05 Integer Detail Class 5 [0=Undefined,1=Exists,2=Exempt]
  DCLASS06 Integer Detail Class 6 [0=Undefined,1=Exists,2=Exempt]
  DCLASS07 Integer Detail Class 7 [0=Undefined,1=Exists,2=Exempt]
  DCLASS08 Integer Detail Class 8 [0=Undefined,1=Exists,2=Exempt]
  DCLASS09 Integer Detail Class 9 [0=Undefined,1=Exists,2=Exempt]
  DCLASS10 Integer Detail Class10 [0=Undefined,1=Exists,2=Exempt]
  HCLS01DESC String*60 Header Class 1 Description
  HCLS02DESC String*60 Header Class 2 Description
  HCLS03DESC String*60 Header Class 3 Description
  HCLS04DESC String*60 Header Class 4 Description
  HCLS05DESC String*60 Header Class 5 Description
  HCLS06DESC String*60 Header Class 6 Description
  HCLS07DESC String*60 Header Class 7 Description
  HCLS08DESC String*60 Header Class 8 Description
  HCLS09DESC String*60 Header Class 9 Description
  HCLS10DESC String*60 Header Class10 Description
  DCLS01DESC String*60 Detail Class 1 Description
  DCLS02DESC String*60 Detail Class 2 Description
  DCLS03DESC String*60 Detail Class 3 Description
  DCLS04DESC String*60 Detail Class 4 Description
  DCLS05DESC String*60 Detail Class 5 Description
  DCLS06DESC String*60 Detail Class 6 Description
  DCLS07DESC String*60 Detail Class 7 Description
  DCLS08DESC String*60 Detail Class 8 Description
  DCLS09DESC String*60 Detail Class 9 Description
  DCLS10DESC String*60 Detail Class10 Description
  TXRATE0101 BCD*8.5 Buyer Class 1 Item Class 1 Rate
  TXRATE0102 BCD*8.5 Buyer Class 1 Item Class 2 Rate
  TXRATE0103 BCD*8.5 Buyer Class 1 Item Class 3 Rate
  TXRATE0104 BCD*8.5 Buyer Class 1 Item Class 4 Rate
  TXRATE0105 BCD*8.5 Buyer Class 1 Item Class 5 Rate
  TXRATE0106 BCD*8.5 Buyer Class 1 Item Class 6 Rate
  TXRATE0107 BCD*8.5 Buyer Class 1 Item Class 7 Rate
  TXRATE0108 BCD*8.5 Buyer Class 1 Item Class 8 Rate
  TXRATE0109 BCD*8.5 Buyer Class 1 Item Class 9 Rate
  TXRATE0110 BCD*8.5 Buyer Class 1 Item Class10 Rate
  TXRATE0201 BCD*8.5 Buyer Class 2 Item Class 1 Rate
  TXRATE0202 BCD*8.5 Buyer Class 2 Item Class 2 Rate
  TXRATE0203 BCD*8.5 Buyer Class 2 Item Class 3 Rate
  TXRATE0204 BCD*8.5 Buyer Class 2 Item Class 4 Rate
  TXRATE0205 BCD*8.5 Buyer Class 2 Item Class 5 Rate
  TXRATE0206 BCD*8.5 Buyer Class 2 Item Class 6 Rate
  TXRATE0207 BCD*8.5 Buyer Class 2 Item Class 7 Rate
  TXRATE0208 BCD*8.5 Buyer Class 2 Item Class 8 Rate
  TXRATE0209 BCD*8.5 Buyer Class 2 Item Class 9 Rate
  TXRATE0210 BCD*8.5 Buyer Class 2 Item Class10 Rate
  TXRATE0301 BCD*8.5 Buyer Class 3 Item Class 1 Rate
  TXRATE0302 BCD*8.5 Buyer Class 3 Item Class 2 Rate
  TXRATE0303 BCD*8.5 Buyer Class 3 Item Class 3 Rate
  TXRATE0304 BCD*8.5 Buyer Class 3 Item Class 4 Rate
  TXRATE0305 BCD*8.5 Buyer Class 3 Item Class 5 Rate
  TXRATE0306 BCD*8.5 Buyer Class 3 Item Class 6 Rate
  TXRATE0307 BCD*8.5 Buyer Class 3 Item Class 7 Rate
  TXRATE0308 BCD*8.5 Buyer Class 3 Item Class 8 Rate
  TXRATE0309 BCD*8.5 Buyer Class 3 Item Class 9 Rate
  TXRATE0310 BCD*8.5 Buyer Class 3 Item Class10 Rate
  TXRATE0401 BCD*8.5 Buyer Class 4 Item Class 1 Rate
  TXRATE0402 BCD*8.5 Buyer Class 4 Item Class 2 Rate
  TXRATE0403 BCD*8.5 Buyer Class 4 Item Class 3 Rate
  TXRATE0404 BCD*8.5 Buyer Class 4 Item Class 4 Rate
  TXRATE0405 BCD*8.5 Buyer Class 4 Item Class 5 Rate
  TXRATE0406 BCD*8.5 Buyer Class 4 Item Class 6 Rate
  TXRATE0407 BCD*8.5 Buyer Class 4 Item Class 7 Rate
  TXRATE0408 BCD*8.5 Buyer Class 4 Item Class 8 Rate
  TXRATE0409 BCD*8.5 Buyer Class 4 Item Class 9 Rate
  TXRATE0410 BCD*8.5 Buyer Class 4 Item Class10 Rate
  TXRATE0501 BCD*8.5 Buyer Class 5 Item Class 1 Rate
  TXRATE0502 BCD*8.5 Buyer Class 5 Item Class 2 Rate
  TXRATE0503 BCD*8.5 Buyer Class 5 Item Class 3 Rate
  TXRATE0504 BCD*8.5 Buyer Class 5 Item Class 4 Rate
  TXRATE0505 BCD*8.5 Buyer Class 5 Item Class 5 Rate
  TXRATE0506 BCD*8.5 Buyer Class 5 Item Class 6 Rate
  TXRATE0507 BCD*8.5 Buyer Class 5 Item Class 7 Rate
  TXRATE0508 BCD*8.5 Buyer Class 5 Item Class 8 Rate
  TXRATE0509 BCD*8.5 Buyer Class 5 Item Class 9 Rate
  TXRATE0510 BCD*8.5 Buyer Class 5 Item Class10 Rate
  TXRATE0601 BCD*8.5 Buyer Class 6 Item Class 1 Rate
  TXRATE0602 BCD*8.5 Buyer Class 6 Item Class 2 Rate
  TXRATE0603 BCD*8.5 Buyer Class 6 Item Class 3 Rate
  TXRATE0604 BCD*8.5 Buyer Class 6 Item Class 4 Rate
  TXRATE0605 BCD*8.5 Buyer Class 6 Item Class 5 Rate
  TXRATE0606 BCD*8.5 Buyer Class 6 Item Class 6 Rate
  TXRATE0607 BCD*8.5 Buyer Class 6 Item Class 7 Rate
  TXRATE0608 BCD*8.5 Buyer Class 6 Item Class 8 Rate
  TXRATE0609 BCD*8.5 Buyer Class 6 Item Class 9 Rate
  TXRATE0610 BCD*8.5 Buyer Class 6 Item Class10 Rate
  TXRATE0701 BCD*8.5 Buyer Class 7 Item Class 1 Rate
  TXRATE0702 BCD*8.5 Buyer Class 7 Item Class 2 Rate
  TXRATE0703 BCD*8.5 Buyer Class 7 Item Class 3 Rate
  TXRATE0704 BCD*8.5 Buyer Class 7 Item Class 4 Rate
  TXRATE0705 BCD*8.5 Buyer Class 7 Item Class 5 Rate
  TXRATE0706 BCD*8.5 Buyer Class 7 Item Class 6 Rate
  TXRATE0707 BCD*8.5 Buyer Class 7 Item Class 7 Rate
  TXRATE0708 BCD*8.5 Buyer Class 7 Item Class 8 Rate
  TXRATE0709 BCD*8.5 Buyer Class 7 Item Class 9 Rate
  TXRATE0710 BCD*8.5 Buyer Class 7 Item Class10 Rate
  TXRATE0801 BCD*8.5 Buyer Class 8 Item Class 1 Rate
  TXRATE0802 BCD*8.5 Buyer Class 8 Item Class 2 Rate
  TXRATE0803 BCD*8.5 Buyer Class 8 Item Class 3 Rate
  TXRATE0804 BCD*8.5 Buyer Class 8 Item Class 4 Rate
  TXRATE0805 BCD*8.5 Buyer Class 8 Item Class 5 Rate
  TXRATE0806 BCD*8.5 Buyer Class 8 Item Class 6 Rate
  TXRATE0807 BCD*8.5 Buyer Class 8 Item Class 7 Rate
  TXRATE0808 BCD*8.5 Buyer Class 8 Item Class 8 Rate
  TXRATE0809 BCD*8.5 Buyer Class 8 Item Class 9 Rate
  TXRATE0810 BCD*8.5 Buyer Class 8 Item Class10 Rate
  TXRATE0901 BCD*8.5 Buyer Class 9 Item Class 1 Rate
  TXRATE0902 BCD*8.5 Buyer Class 9 Item Class 2 Rate
  TXRATE0903 BCD*8.5 Buyer Class 9 Item Class 3 Rate
  TXRATE0904 BCD*8.5 Buyer Class 9 Item Class 4 Rate
  TXRATE0905 BCD*8.5 Buyer Class 9 Item Class 5 Rate
  TXRATE0906 BCD*8.5 Buyer Class 9 Item Class 6 Rate
  TXRATE0907 BCD*8.5 Buyer Class 9 Item Class 7 Rate
  TXRATE0908 BCD*8.5 Buyer Class 9 Item Class 8 Rate
  TXRATE0909 BCD*8.5 Buyer Class 9 Item Class 9 Rate
  TXRATE0910 BCD*8.5 Buyer Class 9 Item Class10 Rate
  TXRATE1001 BCD*8.5 Buyer Class10 Item Class 1 Rate
  TXRATE1002 BCD*8.5 Buyer Class10 Item Class 2 Rate
  TXRATE1003 BCD*8.5 Buyer Class10 Item Class 3 Rate
  TXRATE1004 BCD*8.5 Buyer Class10 Item Class 4 Rate
  TXRATE1005 BCD*8.5 Buyer Class10 Item Class 5 Rate
  TXRATE1006 BCD*8.5 Buyer Class10 Item Class 6 Rate
  TXRATE1007 BCD*8.5 Buyer Class10 Item Class 7 Rate
  TXRATE1008 BCD*8.5 Buyer Class10 Item Class 8 Rate
  TXRATE1009 BCD*8.5 Buyer Class10 Item Class 9 Rate
  TXRATE1010 BCD*8.5 Buyer Class10 Item Class10 Rate

## TXSTATEH - Tax State Headers (view TX0013)
Keys (first = PK; D=dups allowed, M=modifiable): GROUPID+TTYPE+VERSION; GROUPID+TTYPE+HASHMETRIC [D]
Fields (NAME type description [values]):
  GROUPID String*12 Tax Group
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  VERSION Long Version
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HASHMETRIC Binary*96 Hash Metric
  CREATEDATE Date Creation Date
  DESC String*60 Description
  CALCMETHOD Integer Tax Calculation Method [1=Calculate tax by summary,2=Calculate tax by detail]
  SRCCURN String*3 Tax Reporting Currency
  TRATETYPE String*2 Tax Reporting Rate Type
  CNTTXAUTH Integer Number of Authorities
