# AP module - compiled AOM dictionary

## APADV - Payment Advices (view AP0060)
Keys (first = PK; D=dups allowed, M=modifiable): SRCEAPPL+APPLRUNN+BANKCODE+SORTCODE+PAYEECDE+UNIQCNTR
Fields (NAME type description [values]):
  SRCEAPPL String*2 Source Application
  APPLRUNN String*10 Application Run Number
  BANKCODE String*8 Bank Code
  SORTCODE BCD*10.0 Sort Code
  PAYEECDE String*12 Payee Code
  UNIQCNTR BCD*4.0 Unique Counter
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REFNUM String*60 Reference Number
  INVCDATE Date Invoice Date
  GROSSAMT BCD*10.3 Gross Amount
  DISCTAKN BCD*10.3 Discount Taken
  NETAMTPD BCD*10.3 Net Amount Paid
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  CURCODE String*3 Currency
  CURDEC Integer Currency Decimals
  GLREF String*60 G/L Reference
  GLDESC String*60 G/L Description
  GLACCT String*45 G/L Account
  IDRMITTO String*6 Remit-To Location

## APAGED - Aged Documents (view AP0125)
Keys (first = PK; D=dups allowed, M=modifiable): AGESEQ+RECORDNO+IDVEND+IDINVC+ADJNO+RECTYPE+CNTSEQ
Fields (NAME type description [values]):
  AGESEQ Long Aging Sequence Number
  RECORDNO Long Record Number
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  ADJNO Long Adjustment Sequence Number
  RECTYPE Integer Record Type [0=Document,1=Applied Detail,2=Retainage Document]
  CNTSEQ Long Detail Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*18 Check Number
  TRXTYPETXT Integer Document Type
  TRXTYPEID Integer Transaction Type
  DATEINVC Date Document Date
  DATEBUS Date Posting Date
  DATEDUE Date Due Date
  SWPYSTTS Integer Payment Status [0=Normal,1=On Hold,2=Forced]
  IDMEMOXREF String*22 Reference Document No.
  AMTINVCTC BCD*10.3 Invoice Amount (Source)
  AMTINVCHC BCD*10.3 Invoice Amount (Functional)
  AMTPAIDTC BCD*10.3 Amount Paid (Source)
  AMTPAIDHC BCD*10.3 Amount Paid (Functional)
  AMTDUE1TC BCD*10.3 Current Amount Due (Source)
  AMTDUE1HC BCD*10.3 Current Amount Due (Functional)
  AMTDUE2TC BCD*10.3 Period 1 Amount Due (Source)
  AMTDUE2HC BCD*10.3 Period 1 Amount Due (Functional)
  AMTDUE3TC BCD*10.3 Period 2 Amount Due (Source)
  AMTDUE3HC BCD*10.3 Period 2 Amount Due (Functional)
  AMTDUE4TC BCD*10.3 Period 3 Amount Due (Source)
  AMTDUE4HC BCD*10.3 Period 3 Amount Due (Functional)
  AMTDUE5TC BCD*10.3 Period 4 Amount Due (Source)
  AMTDUE5HC BCD*10.3 Period 4 Amount Due (Functional)
  AMTDUE6TC BCD*10.3 Period 5 Amount Due (Source)
  AMTDUE6HC BCD*10.3 Period 5 Amount Due (Functional)
  AMTDUE7TC BCD*10.3 Period 6 Amount Due (Source)
  AMTDUE7HC BCD*10.3 Period 6 Amount Due (Functional)
  AMTDUE8TC BCD*10.3 Period 7 Amount Due (Source)
  AMTDUE8HC BCD*10.3 Period 7 Amount Due (Functional)
  AMTDUE9TC BCD*10.3 Period 9 Amount Due (Source)
  AMTDUE9HC BCD*10.3 Period 9 Amount Due (Functional)
  TOTBKWDTC BCD*10.3 Total Backward Aging (Source)
  TOTBKWDHC BCD*10.3 Total Backward Aging (Functional)
  TOTFWDTC BCD*10.3 Total Forward Aging (Source)
  TOTFWDHC BCD*10.3 Total Forward Aging (Functional)
  AMTBALDUET BCD*10.3 Vendor Balance Due (Source)
  AMTBALDUEH BCD*10.3 Vendor Balance Due (Functional)
  DOCTYPE Integer Document Type
  SWNONRCVBL Integer Misc. Payment Flag
  RTGDATEDUE Date Date Retainage Due
  SORTVALUE1 String*60 Sort Field Value 1
  SORTVALUE2 String*60 Sort Field Value 2
  SORTVALUE3 String*60 Sort Field Value 3
  SORTVALUE4 String*60 Sort Field Value 4
  SORTTYPE1 Integer Sort Field Type 1
  SORTTYPE2 Integer Sort Field Type 2
  SORTTYPE3 Integer Sort Field Type 3
  SORTTYPE4 Integer Sort Field Type 4

## APBTA - Payment and Adjustment Batches (view AP0030)
Keys (first = PK; D=dups allowed, M=modifiable): PAYMTYPE+CNTBTCH; SWPRECHKRG [D,M]; PAYMTYPE+BATCHSTAT+CNTBTCH [M]
Fields (NAME type description [values]):
  PAYMTYPE String*2 Batch Selector
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEBTCH Date Batch Date
  BATCHDESC String*60 Description
  CNTENTER BCD*4.0 Number of Entries
  AMTENTER BCD*10.3 Batch Total
  BATCHTYPE Integer Batch Type [1=Entered,2=Imported,3=Generated,4=System,5=External]
  BATCHSTAT Integer Batch Status [1=Open,3=Posted,4=Deleted,5=Post In Progress,7=Ready To Post,8=Check Creation In Progress]
  IDBANK String*8 Bank Code
  SWPRTDEP Integer Reserved
  CODECURN String*3 Bank Currency Code
  DATERATE Date Bank Rate Date
  CNTLSTRMIT BCD*4.0 Last Entry Number
  RATETYPE String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  CNTDEPNBR BCD*5.0 Reserved
  CNTDEPSEQ Long Reserved
  FUNCAMOUNT BCD*10.3 Func. Batch Total
  POSTSEQNBR BCD*5.0 Posting Sequence No.
  NBRERRORS BCD*5.0 Number of Errors
  DATELSTEDT Date Date Last Edited
  CODECHKTYP Integer Reserved
  PAYMFORM String*6 Reserved
  SWBTCHEDIT Integer Batch Edited [0=No,1=Yes]
  SWPRECHKRG Integer Payment Register Print status [0=Not printed,1=Printed]
  CNTCHKPRNT BCD*4.0 Number of Printed Checks
  CNTREAPPLY BCD*4.0 Number of Reapplies
  SWPRINTED Integer Batch Printed Flag [0=No,1=Yes]
  RATEOP Integer Bank Rate Operator
  SWRATE Integer Bank Rate Overridden [0=No,1=Yes]
  SRCEAPPL String*2 Source Application

## APCCS - 1099 / CPRS Amounts (view AP0013)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+CLASFCID+CNTYEAR+CNTMONTH
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  CLASFCID String*6 Code
  CNTYEAR String*4 Year
  CNTMONTH String*2 Month
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LSTPYMDATE Date Last Payment Date
  PAYMNTCNT BCD*4.0 Number of Payments
  WITHHOLDNG BCD*4.0 Reserved
  PAYMNTAMT BCD*10.3 Payment Amount
  WITHHLDAMT BCD*10.3 Reserved

## APCLX - 1099 / CPRS Codes (view AP0007)
Keys (first = PK; D=dups allowed, M=modifiable): CLASSID
Fields (NAME type description [values]):
  CLASSID String*6 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CLASSDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELASTMN Date Date Last Maintained
  SWWITHH Integer Reserved
  WITHHOLDG String*60 Reserved
  TAXGROUP String*12 Reserved
  TAXSTAT1 Integer Reserved
  TAXSTAT2 Integer Reserved
  TAXSTAT3 Integer Reserved
  TAXSTAT4 Integer Reserved
  TAXSTAT5 Integer Reserved
  MINAMT BCD*10.3 Minimum Amount to Report
  TAXRPTSW Integer Tax Reporting Type [0=,1=1099,2=CPRS]
  CATEGORY Integer Amount Type [0=,3080=Bond Premium,3090=Bond Premium on Tax-Exempt Bond,3100=Bond Premium on Treasury Obligations,1090=Crop Insurance Proceeds,1070=Direct Sales for Resale,3020=Early Withdrawal Penalty,1130=Excess Golden Parachute Payments,1040=Federal Income Tax Withheld,1160=Fish Purchased for Resale,1050=Fishing Boat Proceeds,1100=Gross Proceeds Paid to an Attorney,3010=Interest Income,3030=Interest on U.S. Savings Bonds and Treasury Obligations,3040=Investment Expenses,3070=Market Discount,1060=Medical and Health Care Payments,2010=Nonemployee Compensation,1140=Nonqualified Deferred Compensation,1030=Other Income,1010=Rents,1020=Royalties,1120=Section 409A Deferrals,3060=Specified Private Activity Bond Interest,1170=State Income,1150=State Tax Withheld,1080=Substitute payments in lieu of Interest,3050=Tax-Exempt Interest]

## APCMMTP - Comment Types (view AP0136)
Keys (first = PK; D=dups allowed, M=modifiable): CMNTTYPE
Fields (NAME type description [values]):
  CMNTTYPE String*8 Comment Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTVSW Integer Status [0=Inactive,1=Active]
  INACTDATE Date Inactive Date
  DTELSTMTN Date Date Last Maintained
  ALERTLOC Integer Alert Location [10=AR,20=AP,30=IC,40=OE,50=PO,99=ALL]
  ALERTCOL String*6 Alert Color

## APDPO - Days Payable Outstanding (view AP0138)
Keys (first = PK; D=dups allowed, M=modifiable): SESSDATE
Fields (NAME type description [values]):
  SESSDATE Date Session Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMTINVC BCD*10.3 Net Purchase of the Day
  AMTBAL BCD*10.3 Net Balance of the Day

## APDSD - Distribution Set Details (view AP0008)
Keys (first = PK; D=dups allowed, M=modifiable): DISTSET+CNTLINE
Fields (NAME type description [values]):
  DISTSET String*6 Distribution Set
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTID String*6 Distribution Code
  TEXTDESC String*60 Description
  IDGLACCT String*45 G/L Account
  SWDISCABL Integer Discountable [0=No,1=Yes]
  DISTPCT BCD*5.5 Percentage
  DISTAMT BCD*10.3 Amount

## APDSH - Distribution Sets (view AP0009)
Keys (first = PK; D=dups allowed, M=modifiable): DISTSET
Fields (NAME type description [values]):
  DISTSET String*6 Distribution Set
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELASTMN Date Date Last Maintained
  CODETYPE Integer Code Type [1=Purchase]
  CODEMETH Integer Distribution Method [1=Spread Evenly,2=Fixed Percentage,3=Manual,4=Fixed Amount]
  CNTENTR BCD*4.0 Distributions Entered
  CURNCODE String*3 Currency

## APGLREF - G/L Reference Integration (view AP0121)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [100=Invoice,101=Invoice Detail,200=Debit Note,201=Debit Note Detail,300=Credit Note,301=Credit Note Detail,400=Payment,401=Payment Detail,402=Payment Advance Credit Claim,500=Prepayment,600=Apply Document,601=Apply Document Detail,700=Miscellaneous Payment,701=Miscellaneous Payment Detail,800=Miscellaneous Adjustment,801=Miscellaneous Adjustment Detail,900=Adjustment,901=Adjustment Detail,1000=Revaluation,1100=Reverse Check]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description,1=G/L Detail Reference,2=G/L Detail Description,3=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5={ Left Parenthesis,6=} Right Parenthesis,7=# Number Sign,8=Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Comment,11=Contract,12=Description,13=Detail Description,14=Detail Reference,15=Distribution Code,16=Document Number,17=Document Type,18=Entry Number,19=Invoice Number,20=Order Number,21=Payee,22=Payment Code,23=Posting Sequence,24=Project,25=Purchase Order Number,26=Reference,27=Remit To,28=Remit-To Location,29=Resource,30=Reversal Date,31=Reversal Description,32=Tax Group,33=Transaction Type,34=Vendor Name,35=Vendor Number,36=Vendor Short Name]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Comment,11=Contract,12=Description,13=Detail Description,14=Detail Reference,15=Distribution Code,16=Document Number,17=Document Type,18=Entry Number,19=Invoice Number,20=Order Number,21=Payee,22=Payment Code,23=Posting Sequence,24=Project,25=Purchase Order Number,26=Reference,27=Remit To,28=Remit-To Location,29=Resource,30=Reversal Date,31=Reversal Description,32=Tax Group,33=Transaction Type,34=Vendor Name,35=Vendor Number,36=Vendor Short Name]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Comment,11=Contract,12=Description,13=Detail Description,14=Detail Reference,15=Distribution Code,16=Document Number,17=Document Type,18=Entry Number,19=Invoice Number,20=Order Number,21=Payee,22=Payment Code,23=Posting Sequence,24=Project,25=Purchase Order Number,26=Reference,27=Remit To,28=Remit-To Location,29=Resource,30=Reversal Date,31=Reversal Description,32=Tax Group,33=Transaction Type,34=Vendor Name,35=Vendor Number,36=Vendor Short Name]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Comment,11=Contract,12=Description,13=Detail Description,14=Detail Reference,15=Distribution Code,16=Document Number,17=Document Type,18=Entry Number,19=Invoice Number,20=Order Number,21=Payee,22=Payment Code,23=Posting Sequence,24=Project,25=Purchase Order Number,26=Reference,27=Remit To,28=Remit-To Location,29=Resource,30=Reversal Date,31=Reversal Description,32=Tax Group,33=Transaction Type,34=Vendor Name,35=Vendor Number,36=Vendor Short Name]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Comment,11=Contract,12=Description,13=Detail Description,14=Detail Reference,15=Distribution Code,16=Document Number,17=Document Type,18=Entry Number,19=Invoice Number,20=Order Number,21=Payee,22=Payment Code,23=Posting Sequence,24=Project,25=Purchase Order Number,26=Reference,27=Remit To,28=Remit-To Location,29=Resource,30=Reversal Date,31=Reversal Description,32=Tax Group,33=Transaction Type,34=Vendor Name,35=Vendor Number,36=Vendor Short Name]

## APIBC - Invoice Batches (view AP0020)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH; BTCHSTTS+CNTBTCH [M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEBTCH Date Batch Date
  BTCHDESC String*60 Description
  CNTINVCENT BCD*4.0 Number of Entries
  AMTENTR BCD*10.3 Batch Total
  BTCHTYPE Integer Batch Type [1=Entered,2=Imported,3=Generated,4=Recurring,5=External,6=Retainage]
  BTCHSTTS Integer Batch Status [1=Open,3=Posted,4=Deleted,5=Post In Progress,7=Ready To Post]
  INVCTYPE Integer Invoice Type [1=Summary]
  CNTLSTITEM BCD*4.0 Last Entry Number
  POSTSEQNBR BCD*5.0 Posting Sequence No.
  NBRERRORS BCD*5.0 Number of Errors
  DTELSTEDIT Date Date Last Edited
  SWPRINTED Integer Batch Printed Flag [0=No,1=Yes]
  SRCEAPPL String*2 Source Application
  SWICT Integer ICT Related [0=No,1=Yes]

## APIBD - Invoice Details (view AP0022)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDDIST String*6 Distribution Code
  TEXTDESC String*60 Distribution Description
  SWMANLDIST Integer Reserved
  AMTTOTTAX BCD*10.3 Tax Total
  SWMANLTX Integer Manual Tax Entry [0=No,1=Yes]
  BASETAX1 BCD*10.3 Base Tax 1
  BASETAX2 BCD*10.3 Base Tax 2
  BASETAX3 BCD*10.3 Base Tax 3
  BASETAX4 BCD*10.3 Base Tax 4
  BASETAX5 BCD*10.3 Base Tax 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  RATETAX1 BCD*8.5 Tax Rate 1
  RATETAX2 BCD*8.5 Tax Rate 2
  RATETAX3 BCD*8.5 Tax Rate 3
  RATETAX4 BCD*8.5 Tax Rate 4
  RATETAX5 BCD*8.5 Tax Rate 5
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  IDGLACCT String*45 G/L Account
  IDACCTTAX String*45 Retainage Allocated Tax Account
  ID1099CLAS String*6 Reserved
  AMTDIST BCD*10.3 Distributed Amount
  AMTDISTNET BCD*10.3 Distributed Amount Before Taxes
  AMTINCLTAX BCD*10.3 Tax Amount Included in Price
  AMTGLDIST BCD*10.3 G/L Distributed Amount
  AMTTAXREC1 BCD*10.3 Recoverable Tax Amount 1
  AMTTAXREC2 BCD*10.3 Recoverable Tax Amount 2
  AMTTAXREC3 BCD*10.3 Recoverable Tax Amount 3
  AMTTAXREC4 BCD*10.3 Recoverable Tax Amount 4
  AMTTAXREC5 BCD*10.3 Recoverable Tax Amount 5
  AMTTAXEXP1 BCD*10.3 Expense Sep. Tax Amount 1
  AMTTAXEXP2 BCD*10.3 Expense Sep. Tax Amount 2
  AMTTAXEXP3 BCD*10.3 Expense Sep. Tax Amount 3
  AMTTAXEXP4 BCD*10.3 Expense Sep. Tax Amount 4
  AMTTAXEXP5 BCD*10.3 Expense Sep. Tax Amount 5
  AMTTAXTOBE BCD*10.3 Tax Allocated Total
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=]
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  SWIBT Integer Comment Attached [0=No,1=Yes]
  SWDISCABL Integer Discountable [0=No,1=Yes]
  OCNTLINE BCD*3.0 Original Line Identifier
  RTGAMT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Percent Retained
  RTGDAYS Integer Days Retained
  RTGDATEDUE Date Retainage Due Date
  SWRTGDDTOV Integer Retainage Due Date Override [0=No,1=Yes]
  SWRTGAMTOV Integer Retainage Amount Override [0=No,1=Yes]
  VALUES Long Optional Fields
  DESCOMP String*6 Destination
  ROUTE Integer Route No.
  RTGDISTTC BCD*10.3 Retainage Distribution Amount
  RTGINVDIST BCD*10.3 Invoiced Retainage Distribution
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Tax
  TXEXP1RC BCD*10.3 Tax Reporting Expensed Tax 1
  TXEXP2RC BCD*10.3 Tax Reporting Expensed Tax 2
  TXEXP3RC BCD*10.3 Tax Reporting Expensed Tax 3
  TXEXP4RC BCD*10.3 Tax Reporting Expensed Tax 4
  TXEXP5RC BCD*10.3 Tax Reporting Expensed Tax 5
  TXREC1RC BCD*10.3 Tax Reporting Recoverable Tax 1
  TXREC2RC BCD*10.3 Tax Reporting Recoverable Tax 2
  TXREC3RC BCD*10.3 Tax Reporting Recoverable Tax 3
  TXREC4RC BCD*10.3 Tax Reporting Recoverable Tax 4
  TXREC5RC BCD*10.3 Tax Reporting Recoverable Tax 5
  TXBSERT1TC BCD*10.3 Retainage Tax Base 1
  TXBSERT2TC BCD*10.3 Retainage Tax Base 2
  TXBSERT3TC BCD*10.3 Retainage Tax Base 3
  TXBSERT4TC BCD*10.3 Retainage Tax Base 4
  TXBSERT5TC BCD*10.3 Retainage Tax Base 5
  TXAMTRT1TC BCD*10.3 Retainage Tax Amount 1
  TXAMTRT2TC BCD*10.3 Retainage Tax Amount 2
  TXAMTRT3TC BCD*10.3 Retainage Tax Amount 3
  TXAMTRT4TC BCD*10.3 Retainage Tax Amount 4
  TXAMTRT5TC BCD*10.3 Retainage Tax Amount 5
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  TXAMTRT1HC BCD*10.3 Func. Retainage Tax Amount 1
  TXAMTRT2HC BCD*10.3 Func. Retainage Tax Amount 2
  TXAMTRT3HC BCD*10.3 Func. Retainage Tax Amount 3
  TXAMTRT4HC BCD*10.3 Func. Retainage Tax Amount 4
  TXAMTRT5HC BCD*10.3 Func. Retainage Tax Amount 5
  TXREC1HC BCD*10.3 Func. Tax Recoverable Amount 1
  TXREC2HC BCD*10.3 Func. Tax Recoverable Amount 2
  TXREC3HC BCD*10.3 Func. Tax Recoverable Amount 3
  TXREC4HC BCD*10.3 Func. Tax Recoverable Amount 4
  TXREC5HC BCD*10.3 Func. Tax Recoverable Amount 5
  TXEXP1HC BCD*10.3 Func. Tax Expense Sep. Amount 1
  TXEXP2HC BCD*10.3 Func. Tax Expense Sep. Amount 2
  TXEXP3HC BCD*10.3 Func. Tax Expense Sep. Amount 3
  TXEXP4HC BCD*10.3 Func. Tax Expense Sep. Amount 4
  TXEXP5HC BCD*10.3 Func. Tax Expense Sep. Amount 5
  TXALLHC BCD*10.3 Func. Tax Allocated Total
  TXALL1HC BCD*10.3 Func. Tax Allocated Amount 1
  TXALL2HC BCD*10.3 Func. Tax Allocated Amount 2
  TXALL3HC BCD*10.3 Func. Tax Allocated Amount 3
  TXALL4HC BCD*10.3 Func. Tax Allocated Amount 4
  TXALL5HC BCD*10.3 Func. Tax Allocated Amount 5
  TXALL1TC BCD*10.3 Tax Allocated Amount 1
  TXALL2TC BCD*10.3 Tax Allocated Amount 2
  TXALL3TC BCD*10.3 Tax Allocated Amount 3
  TXALL4TC BCD*10.3 Tax Allocated Amount 4
  TXALL5TC BCD*10.3 Tax Allocated Amount 5
  AMTCOSTHC BCD*10.6 Func. Cost
  AMTDISTHC BCD*10.3 Func. Distributed Amount
  DISTNETHC BCD*10.3 Func. Distribution Net of Taxes
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  TXALLRTHC BCD*10.3 Func. Retainage Tax Allocated
  TXALLRTTC BCD*10.3 Retainage Tax Allocated
  TXEXPRTHC BCD*10.3 Func. Retainage Tax Expensed
  TXEXPRTTC BCD*10.3 Retainage Tax Expensed
  SWFAS Integer Fixed Asset [0=No,1=Yes]
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXTX1TC BCD*10.3 Reverse Charge Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charge Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charge Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charge Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charge Amount 5
  SWCAXABLE1 Integer Reverse Chargeable 1 [0=No,1=Yes]
  SWCAXABLE2 Integer Reverse Chargeable 2 [0=No,1=Yes]
  SWCAXABLE3 Integer Reverse Chargeable 3 [0=No,1=Yes]
  SWCAXABLE4 Integer Reverse Chargeable 4 [0=No,1=Yes]
  SWCAXABLE5 Integer Reverse Chargeable 5 [0=No,1=Yes]

## APIBDA - Invoice Detail Sage Fixed Assets Fields (view AP0180)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORGID String*6 Orgid
  FASDB String*32 Database
  FASCMP String*32 Company/Org.
  FASTMPL String*25 Template
  TEXTDESC String*80 Asset Description
  SWSEPQTY Integer Separate Quantity Switch [0=No,1=Yes]
  QTY BCD*10.5 Quantity
  UOM String*10 Unit of Measure
  AMTTC BCD*10.3 Asset Value
  AMTHC BCD*10.3 Func. Asset Value

## APIBDO - Invoice Detail Optional Fields (view AP0401)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE+OPTFIELD; OPTFIELD+CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
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

## APIBH - Invoices (view AP0021)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM; ORIGCOMP+IDVEND+IDINVC [D,M]; ORIGCOMP+IDVEND+AMTTOTDIST [D,M]; ORIGCOMP+IDVEND+DATEINVC [D,M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  IDRMITTO String*6 Remit-To Location
  TEXTTRX Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest]
  IDTRX Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,32=Credit Note - Summary Entered,40=Interest Charge]
  INVCSTTS Integer Reserved
  ORDRNBR String*22 Order Number
  PONBR String*22 PO Number
  INVCDESC String*60 Invoice Description
  SWPRTINVC Integer Reserved
  INVCAPPLTO String*22 Apply-to Document
  IDACCTSET String*6 Account Set
  DATEINVC Date Document Date
  DATEASOF Date As of Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  CODECURN String*3 Currency Code
  RATETYPE String*2 Rate Type
  SWMANRTE Integer Rate Overridden [0=No,1=Yes]
  EXCHRATEHC BCD*8.7 Exchange Rate
  ORIGRATEHC BCD*8.7 Apply-to Exchange Rate
  TERMCODE String*6 Terms
  SWTERMOVRD Integer Terms Overridden [0=No,1=Yes]
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  PCTDISC BCD*5.5 Discount Percentage
  AMTDISCAVL BCD*10.3 Discount Amount Available
  LASTLINE BCD*3.0 Number of Details
  SWTAXBL Integer Taxable [0=No,1=Yes]
  SWCALCTX Integer Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  CODETAXGRP String*12 Tax Group
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  BASETAX1 BCD*10.3 Tax Base 1
  BASETAX2 BCD*10.3 Tax Base 2
  BASETAX3 BCD*10.3 Tax Base 3
  BASETAX4 BCD*10.3 Tax Base 4
  BASETAX5 BCD*10.3 Tax Base 5
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMT1099 BCD*10.3 1099/CPRS Amount
  AMTDISTSET BCD*10.3 Distribution Set Amount
  AMTTAXDIST BCD*10.3 Total Distributed Tax
  AMTINVCTOT BCD*10.3 Document Total Before Taxes
  AMTALLOCTX BCD*10.3 Distributed Allocated Taxes
  CNTPAYMSCH BCD*3.0 Number of Scheduled Payments
  AMTTOTDIST BCD*10.3 Distributed Total Before Taxes
  AMTGROSDST BCD*10.3 Distributed Total Including Tax
  IDPPD String*22 Prepayment Number
  TEXTRMIT String*60 Location Name
  TEXTSTE1 String*60 Address Line 1
  TEXTSTE2 String*60 Address Line 2
  TEXTSTE3 String*60 Address Line 3
  TEXTSTE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  NAMECTAC String*60 Contact Name
  TEXTPHON String*30 Phone Number
  TEXTFAX String*30 Fax Number
  DATERATE Date Rate Date
  AMTRECTAX BCD*10.3 Recoverable Taxes
  CODEPAYPPD BCD*3.0 Reserved
  CODEVNDGRP String*6 Vendor Group Code
  TERMSDESC String*60 Terms Description
  IDDISTSET String*6 Distribution Set
  ID1099CLAS String*6 1099/CPRS Code
  AMTTAXTOT BCD*10.3 Tax Total
  AMTGROSTOT BCD*10.3 Document Total Including Tax
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  AMTEXPTAX BCD*10.3 Expensed Separately Taxes
  AMTAXTOBE BCD*10.3 Tax Amount to be Allocated
  TAXOUTBAL BCD*10.3 Reserved
  CODEOPER Integer Currency Code Operator [1=Multiply,2=Divide]
  ACCTREC1 String*45 Recoverable Account 1
  ACCTREC2 String*45 Recoverable Account 2
  ACCTREC3 String*45 Recoverable Account 3
  ACCTREC4 String*45 Recoverable Account 4
  ACCTREC5 String*45 Recoverable Account 5
  ACCTEXP1 String*45 Expense Sep. Account 1
  ACCTEXP2 String*45 Expense Sep. Account 2
  ACCTEXP3 String*45 Expense Sep. Account 3
  ACCTEXP4 String*45 Expense Sep. Account 4
  ACCTEXP5 String*45 Expense Sep. Account 5
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  SWJOB Integer Job Related [0=No,1=Yes]
  AMTRECDIST BCD*10.3 Dist. Recoverable Taxes
  AMTEXPDIST BCD*10.3 Dist. Exp. Separately Taxes
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  EMAIL String*50 E-mail
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  CTACEMAIL String*50 Contact's E-mail
  AMTPPD BCD*10.3 Prepayment Amount
  IDSTDINVC String*16 Recurring Payable Code
  DATEPRCS Date Date Generated
  AMTDSBWTAX BCD*10.3 Discount Base With Tax
  AMTDSBNTAX BCD*10.3 Discount Base Without Tax
  AMTDSCBASE BCD*10.3 Discount Base
  SWRTGINVC Integer Retainage Invoice [0=No,1=Yes]
  RTGAPPLYTO String*22 Original Doc. No.
  SWRTG Integer Has Retainage [0=No,1=Yes]
  RTGAMT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Percent Retained
  RTGDAYS Integer Days Retained
  RTGDATEDUE Date Retainage Due Date
  RTGTERMS String*6 Retainage Terms Code
  SWRTGDDTOV Integer Retainage Due Date Override [0=No,1=Yes]
  SWRTGAMTOV Integer Retainage Amount Override [0=No,1=Yes]
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  SWTXBSECTL Integer Tax Base Control [0=Enter,1=Calculate,2=Distribute]
  VALUES Long Optional Fields
  ORIGCOMP String*6 Originator
  DETAILCNT Long Number of Details
  SRCEAPPL String*2 Source Application
  SWHOLD Integer On Hold [0=No,1=Yes]
  APVERSION String*3 A/P Version Created In
  TAXVERSION Long Tax State Version
  SWTXRTGRPT Integer Report Retainage Tax
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=Enter,1=Calculate,2=Distribute]
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operator [1=Multiply,2=Divide]
  SWRATERC Integer Tax Reporting Rate Override [0=No,1=Yes]
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Tax
  TXEXPRC BCD*10.3 Tax Reporting Expensed Tax
  TXRECRC BCD*10.3 Tax Reporting Recoverable Tax
  TXBSERT1TC BCD*10.3 Retainage Tax Base 1
  TXBSERT2TC BCD*10.3 Retainage Tax Base 2
  TXBSERT3TC BCD*10.3 Retainage Tax Base 3
  TXBSERT4TC BCD*10.3 Retainage Tax Base 4
  TXBSERT5TC BCD*10.3 Retainage Tax Base 5
  TXAMTRT1TC BCD*10.3 Retainage Tax Amount 1
  TXAMTRT2TC BCD*10.3 Retainage Tax Amount 2
  TXAMTRT3TC BCD*10.3 Retainage Tax Amount 3
  TXAMTRT4TC BCD*10.3 Retainage Tax Amount 4
  TXAMTRT5TC BCD*10.3 Retainage Tax Amount 5
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  AMTGROSHC BCD*10.3 Func. Distribution w/ Tax Total
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  AMTDISCHC BCD*10.3 Func. Discount Amount
  AMT1099HC BCD*10.3 Func. 1099/CPRS Amount
  AMTPPDHC BCD*10.3 Func. Prepayment Amount
  AMTDUETC BCD*10.3 Amount Due
  AMTDUEHC BCD*10.3 Func. Amount Due
  TEXTVEN String*60 Vendor Name
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  IDN String*30 Import Declaration Number
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXBS1TC BCD*10.3 Reverse Charges Base 1
  AMTCXBS2TC BCD*10.3 Reverse Charges Base 2
  AMTCXBS3TC BCD*10.3 Reverse Charges Base 3
  AMTCXBS4TC BCD*10.3 Reverse Charges Base 4
  AMTCXBS5TC BCD*10.3 Reverse Charges Base 5
  AMTCXTX1TC BCD*10.3 Reverse Charges Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charges Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charges Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charges Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charges Amount 5

## APIBHO - Invoice Optional Fields (view AP0402)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+OPTFIELD; OPTFIELD+CNTBTCH+CNTITEM
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
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

## APIBS - Invoice Payment Schedules (view AP0023)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTPAYM
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTPAYM BCD*3.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEDUE Date Due Date
  AMTDUE BCD*10.3 Amount Due
  DATEDISC Date Discount Date
  AMTDISC BCD*10.3 Discount Amount
  AMTDUEHC BCD*10.3 Func. Amount Due
  AMTDISCHC BCD*10.3 Func. Discount Amount

## APIBT - Invoice Detail Comments (view AP0024)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTLINE String*250 Comment
  SWPRTINVC Integer Reserved

## APINTCK - Integrity Checker (view AP0045)
Keys (first = PK; D=dups allowed, M=modifiable): RECID
Fields (NAME type description [values]):
  RECID Integer Record ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHKORPHAN Boolean Check Orphans
  FIXORPHAN Boolean Fix Orphans
  CHKSETUP Boolean Check Setup Tables
  FIXSETUP Boolean Fix Setup Tables
  CHKBATCH Boolean Check Open Batches
  FIXBATCH Boolean Fix Open Batches
  CHKVENDOC Boolean Check Vendor Documents
  FIXVENDOC Boolean Fix Vendor Documents
  FRVENDOC String*12 From Vendor
  TOVENDOC String*12 To Vendor
  CHKJOURNAL Boolean Check Posting Journal
  FIXJOURNAL Boolean Fix Posting Journal

## APJTR - Job Costing Transactions (view AP0204)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTSEQENCE Long Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEBUS Date Posting Date
  DOCTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Prepayment,6=Unapplied Cash,13=Retainage Invoice,14=Retainage Debit Note,15=Retainage Credit Note]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Discount,3=Write-Off,4=Apply From,5=Apply To,6=Payment Reversal,7=Rounding,8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Payment,20=Retainage Rounding,21=Retainage Exchange Gain/Loss,22=Retainage Unrealized Exchange Gain/Loss]
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  IDDIST String*6 Distribution Code
  IDGLACCT String*45 G/L Account
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOSTHC BCD*10.6 Functional Cost
  AMTCOSTTC BCD*10.6 Vendor Cost
  AMTHC BCD*10.3 Functional Amount
  AMTTC BCD*10.3 Vendor Amount
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  CODETAX1 String*12 Tax Auth. 1
  CODETAX2 String*12 Tax Auth. 2
  CODETAX3 String*12 Tax Auth. 3
  CODETAX4 String*12 Tax Auth. 4
  CODETAX5 String*12 Tax Auth. 5
  AMTTAX1HC BCD*10.3 Func. Tax Amount 1
  AMTTAX2HC BCD*10.3 Func. Tax Amount 2
  AMTTAX3HC BCD*10.3 Func. Tax Amount 3
  AMTTAX4HC BCD*10.3 Func. Tax Amount 4
  AMTTAX5HC BCD*10.3 Func. Tax Amount 5
  AMTTAX1TC BCD*10.3 Vend. Tax Amount 1
  AMTTAX2TC BCD*10.3 Vend. Tax Amount 2
  AMTTAX3TC BCD*10.3 Vend. Tax Amount 3
  AMTTAX4TC BCD*10.3 Vend. Tax Amount 4
  AMTTAX5TC BCD*10.3 Vend. Tax Amount 5
  AMTRECTXHC BCD*10.3 Functional Recoverable Taxes
  AMTRECTXTC BCD*10.3 Vendor Recoverable Taxes
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGAMTTC BCD*10.3 Vend. Curr. Retainage Amount
  RTGDATEDUE Date Retainage Due Date

## APMSG - E-mail Messages (view AP0120)
Keys (first = PK; D=dups allowed, M=modifiable): MSGTYPE+MSGID
Fields (NAME type description [values]):
  MSGTYPE Integer Message Type [0=E-mail]
  MSGID String*16 Message ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTIVESW Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DTELSTMNTN Date Date Last Maintained
  SUBJECT String*250 E-mail Subject
  BODY1 String*250 E-mail Body Text (1 of 10)
  BODY2 String*250 E-mail Body Text (2 of 10)
  BODY3 String*250 E-mail Body Text (3 of 10)
  BODY4 String*250 E-mail Body Text (4 of 10)
  BODY5 String*250 E-mail Body Text (5 of 10)
  BODY6 String*250 E-mail Body Text (6 of 10)
  BODY7 String*250 E-mail Body Text (7 of 10)
  BODY8 String*250 E-mail Body Text (8 of 10)
  BODY9 String*250 E-mail Body Text (9 of 10)
  BODY10 String*250 E-mail Body Text (10 of 10)

## APOBL - Documents (view AP0025)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC; SWPAID+IDORDERNBR+IDVEND+IDINVC [M]; SWPAID+IDPONBR+IDVEND+IDINVC [D,M]; DATEINVCDU+IDVEND+IDINVC [D,M]; SWPAID+IDVEND+IDPREPAY [D,M]; IDVEND+DATEINVC [D,M]; SWRTGOUT+IDVEND+IDINVC [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*18 Check Number
  IDORDERNBR String*22 Order Number
  IDPONBR String*22 PO Number
  DATEINVCDU Date Due Date
  IDRMITTO String*6 Remit-To Location
  IDTRXTYPE Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,26=Debit Note - Advance Credit Claim,32=Credit Note - Summary Entered,40=Interest Charge,50=Prepayment - Posted,51=Payment - Posted]
  TXTTRXTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,10=Prepayment,11=Payment]
  DATEBTCH Date Batch Date
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  IDVENDGRP String*6 Group Code
  DESCINVC String*60 Doc. Description
  DATEINVC Date Doc. Date
  DATEASOF Date Invoice as-of Date
  CODETERM String*6 Terms
  DATEDISC Date Discount Date
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  SWRATEOVRD Integer Rate Overridden [0=No,1=Yes]
  EXCHRATEHC BCD*8.7 Exchange Rate
  AMTINVCHC BCD*10.3 Func. Currency Invoice Amount
  AMTDUEHC BCD*10.3 Func. Currency Amount Due
  AMTTXBLHC BCD*10.3 Func. Currency Taxable Amount
  AMTNONTXHC BCD*10.3 Func. Currency Non-Taxable Amt.
  AMTTAXHC BCD*10.3 Func. Currency Tax Amount
  AMTDISCHC BCD*10.3 Func. Currency Discount Amount
  AMTINVCTC BCD*10.3 Vend. Currency Invoice Amount
  AMTDUETC BCD*10.3 Vend. Currency Amount Due
  AMTTXBLTC BCD*10.3 Vend. Currency Taxable Amount
  AMTNONTXTC BCD*10.3 Vend. Currency Non-Taxable Amt.
  AMTTAXTC BCD*10.3 Vend. Currency Tax Amount
  AMTDISCTC BCD*10.3 Vend. Currency Discount Amount
  SWPAID Integer Fully Paid [0=No,1=Yes]
  DATELSTACT Date Last Activity Date
  DATELSTSTM Date Last Statement Date
  CNTTOTPAYM BCD*3.0 Number of Scheduled Payments
  CNTLSTPAYM BCD*3.0 Reserved - Last Payment Number Paid
  CNTLSTPYST BCD*3.0 Payment Number on Last Statement
  AMTREMIT BCD*10.3 Reserved - Payment Amount
  CNTLASTSCH BCD*3.0 Last Applied Payment Seq. No.
  SWTAXOVRD Integer Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  CODETAX1 String*12 Tax Auth. 1
  CODETAX2 String*12 Tax Auth. 2
  CODETAX3 String*12 Tax Auth. 3
  CODETAX4 String*12 Tax Auth. 4
  CODETAX5 String*12 Tax Auth. 5
  AMTBASE1HC BCD*10.3 Func. Base Amount 1
  AMTBASE2HC BCD*10.3 Func. Base Amount 2
  AMTBASE3HC BCD*10.3 Func. Base Amount 3
  AMTBASE4HC BCD*10.3 Func. Base Amount 4
  AMTBASE5HC BCD*10.3 Func. Base Amount 5
  AMTTAX1HC BCD*10.3 Func. Tax Amount 1
  AMTTAX2HC BCD*10.3 Func. Tax Amount 2
  AMTTAX3HC BCD*10.3 Func. Tax Amount 3
  AMTTAX4HC BCD*10.3 Func. Tax Amount 4
  AMTTAX5HC BCD*10.3 Func. Tax Amount 5
  AMTBASE1TC BCD*10.3 Vend. Base Amount 1
  AMTBASE2TC BCD*10.3 Vend. Base Amount 2
  AMTBASE3TC BCD*10.3 Vend. Base Amount 3
  AMTBASE4TC BCD*10.3 Vend. Base Amount 4
  AMTBASE5TC BCD*10.3 Vend. Base Amount 5
  AMTTAX1TC BCD*10.3 Vend. Tax Amount 1
  AMTTAX2TC BCD*10.3 Vend. Tax Amount 2
  AMTTAX3TC BCD*10.3 Vend. Tax Amount 3
  AMTTAX4TC BCD*10.3 Vend. Tax Amount 4
  AMTTAX5TC BCD*10.3 Vend. Tax Amount 5
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDPREPAY String*22 Prepay Invoice Number
  DATEBUS Date Posting Date
  ID1099CLAS String*6 1099/CPRS Code
  AMT1099ORG BCD*10.3 1099/CPRS Original Amount
  AMT1099REM BCD*10.3 1099/CPRS Remaining Amount
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  YPLASTACT String*6 Last Activity Year/Period
  IDBANK String*8 Bank Code
  LONGSERIAL ??? Check Serial Number
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  SWJOB Integer Job Related [0=No,1=Yes]
  SWRTG Integer Has Retainage [0=No,1=Yes]
  SWRTGOUT Integer Retainage Outstanding [0=No,1=Yes]
  RTGDATEDUE Date Date Retainage Due
  RTGOAMTHC BCD*10.3 Func. Curr. Orig. Rtng. Amt.
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGOAMTTC BCD*10.3 Vend. Curr. Orig. Rtng. Amt.
  RTGAMTTC BCD*10.3 Vend. Curr. Retainage Amount
  RTGTERMS String*6 Retainage Terms Code
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGAPPLYTO String*22 Original Doc. No.
  VALUES Long Optional Fields
  SRCEAPPL String*2 Source Application
  SWPYSTTS Integer Payment Status [0=Normal,1=On Hold,2=Forced]
  DATEPYSTTS Date Date Payment Status Changed
  APVERSION String*3 A/P Version Created In
  TYPEBTCH String*2 Batch Type
  CNTOBLJ Long Number of OBLJ Details
  CODECURNRC String*3 Tax Reporting Currency Code
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operator
  SWRATERC Integer Tax Reporting Rate Override [0=No,1=Yes]
  SWTXRTGRPT Integer Report Retainage Tax
  CODETAXGRP String*12 Tax Group
  TAXVERSION Long Tax State Version
  SWTXBSECTL Integer Tax Base Calculate Method
  SWTXCTLRC Integer Tax Reporting Calculate Method
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
  TXBSERT1TC BCD*10.3 Tax Base 1
  TXBSERT2TC BCD*10.3 Tax Base 2
  TXBSERT3TC BCD*10.3 Tax Base 3
  TXBSERT4TC BCD*10.3 Tax Base 4
  TXBSERT5TC BCD*10.3 Tax Base 5
  TXAMTRT1TC BCD*10.3 Tax Amount 1
  TXAMTRT2TC BCD*10.3 Tax Amount 2
  TXAMTRT3TC BCD*10.3 Tax Amount 3
  TXAMTRT4TC BCD*10.3 Tax Amount 4
  TXAMTRT5TC BCD*10.3 Tax Amount 5
  DATEFRSTBK Date Earliest Backdated Activity Date
  DATELSTRVL Date Last Revaluation Date
  ORATE BCD*8.7 Orig. Exchange Rate
  ORATETYPE String*2 Orig. Rate Type
  ORATEDATE Date Orig. Rate Date
  ORATEOP Integer Orig. Rate Operator
  OSWRATE Integer Orig. Rate Override Flag [0=No,1=Yes]
  IDACCTSET String*6 Account Set
  DATEPAID Date Date Paid
  SWNONRCVBL Integer Misc. Payment Flag
  OAMTWHT1TC BCD*10.3 Orig Est Tax Withheld Amount 1
  OAMTWHT2TC BCD*10.3 Orig Est Tax Withheld Amount 2
  OAMTWHT3TC BCD*10.3 Orig Est Tax Withheld Amount 3
  OAMTWHT4TC BCD*10.3 Orig Est Tax Withheld Amount 4
  OAMTWHT5TC BCD*10.3 Orig Est Tax Withheld Amount 5

## APOBLJ - Open Document Details (view AP0200)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+CNTLINE
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  IDDIST String*6 Distribution Code
  IDGLACCT String*45 G/L Account
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  AMTINVCHC BCD*10.3 Func. Currency Invoice Amount
  AMTDUEHC BCD*10.3 Func. Currency Amount Due
  AMTINVCTC BCD*10.3 Vend. Currency Invoice Amount
  AMTDUETC BCD*10.3 Vend. Currency Amount Due
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  SWDISCABL Integer Discountable [0=No,1=Yes]
  RTGDATEDUE Date Date Retainage Due
  RTGOAMTHC BCD*10.3 Func. Curr. Orig. Rtng. Amt.
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGOAMTTC BCD*10.3 Vend. Curr. Orig. Rtng. Amt.
  RTGAMTTC BCD*10.3 Vend. Curr. Retainage Amount
  VALUES Long Optional Fields
  RTGDISTTC BCD*10.3 Retainage Distribution Amount
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
  TXRATE1 BCD*8.5 Tax Rate 1
  TXRATE2 BCD*8.5 Tax Rate 2
  TXRATE3 BCD*8.5 Tax Rate 3
  TXRATE4 BCD*8.5 Tax Rate 4
  TXRATE5 BCD*8.5 Tax Rate 5
  TXBSERT1TC BCD*10.3 Vend. Retainage Tax Base 1
  TXBSERT2TC BCD*10.3 Vend. Retainage Tax Base 2
  TXBSERT3TC BCD*10.3 Vend. Retainage Tax Base 3
  TXBSERT4TC BCD*10.3 Vend. Retainage Tax Base 4
  TXBSERT5TC BCD*10.3 Vend. Retainage Tax Base 5
  TXAMTRT1TC BCD*10.3 Vend. Retainage Tax Amount 1
  TXAMTRT2TC BCD*10.3 Vend. Retainage Tax Amount 2
  TXAMTRT3TC BCD*10.3 Vend. Retainage Tax Amount 3
  TXAMTRT4TC BCD*10.3 Vend. Retainage Tax Amount 4
  TXAMTRT5TC BCD*10.3 Vend. Retainage Tax Amount 5
  TXAMTRT1HC BCD*10.3 Func. Retainage Tax Amount 1
  TXAMTRT2HC BCD*10.3 Func. Retainage Tax Amount 2
  TXAMTRT3HC BCD*10.3 Func. Retainage Tax Amount 3
  TXAMTRT4HC BCD*10.3 Func. Retainage Tax Amount 4
  TXAMTRT5HC BCD*10.3 Func. Retainage Tax Amount 5
  TXALLRTHC BCD*10.3 Func. Retainage Tax Allocated
  TXALLRTTC BCD*10.3 Vend. Retainage Tax Allocated
  TXEXPRTHC BCD*10.3 Func. Retainage Tax Expensed
  TXEXPRTTC BCD*10.3 Vend. Retainage Tax Expensed
  TXALLACCT String*45 Allocated Tax Account
  CNTLASTSEQ Long Last Applied Payment Seq. No.
  OAMTWHT1TC BCD*10.3 Orig Est Tax Withheld Amount 1
  OAMTWHT2TC BCD*10.3 Orig Est Tax Withheld Amount 2
  OAMTWHT3TC BCD*10.3 Orig Est Tax Withheld Amount 3
  OAMTWHT4TC BCD*10.3 Orig Est Tax Withheld Amount 4
  OAMTWHT5TC BCD*10.3 Orig Est Tax Withheld Amount 5

## APOBLJO - Open Doc. Detail Optional Fields (view AP0515)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+CNTLINE+OPTFIELD; OPTFIELD+IDVEND+IDINVC+CNTLINE
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTLINE BCD*3.0 Line Number
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

## APOBLJP - Document Detail Payments (view AP0171)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+CNTLINE+CNTSEQENCE; IDBANK+IDVEND+IDRMIT+LONGSERIAL+DATERMIT [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQENCE Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNBR Long Transaction Number
  DATEBUS Date Posting Date
  TRANSTYPE Integer Document Type [6=Debit Note Applied To,7=Applied Debit Note,8=Credit Note Applied To,9=Applied Credit Note,10=Prepayment,11=Payment,12=Discount,14=Adjustment,16=Exchange Gain/Loss,17=Rounding,18=Retainage,19=Tax Withheld]
  TRXTYPE Integer Transaction Type [41=Debit Note Applied To,42=Applied Debit Note,43=Credit Note Applied To,44=Applied Credit Note,58=Prepayment - Applied,59=Prepayment - Reversed,51=Payment - Posted,52=Payment - Applied,53=Payment - Reversed,61=Discount - Posted,63=Discount - Reversed,81=Adjustment - Posted,83=Adjustment - Reversed,65=Exchange Gain/Loss - Posted,67=Exchange Gain/Loss - Reversed,69=Unrealized Exchange Gain/Loss,91=Rounding - Posted,93=Rounding - Reversed,100=Retainage - Invoiced,101=Retainage - Adjusted,102=Retainage - Revalued,103=Retainage - Exchange Gain/Loss,104=Retainage - Rounding,94=Payment - Invoice Reversed,105=Tax Withheld - Posted,106=Tax Withheld - Reversed]
  TYPEBTCH String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  DATEBTCH Date Batch Date
  QTYINVC BCD*10.5 Quantity
  AMTPAYMHC BCD*10.3 Func. Payment Amount
  AMTPAYMTC BCD*10.3 Vend. Payment Amount
  TXTOTRTHC BCD*10.3 Func. Retainage Tax Invoiced
  TXTOTRTTC BCD*10.3 Vend. Retainage Tax Invoiced
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEEXCHHC BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  IDMEMOXREF String*22 Reference Document Number
  IDBANK String*8 Bank Code
  IDRMIT String*18 Check/Receipt Number
  DATERMIT Date Payment Date
  LONGSERIAL ??? Serial Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  CODE1099 String*6 1099/CPRS Code
  AMT1099 BCD*10.3 1099/CPRS Amount
  CODETAX String*12 Tax Authority

## APOBLO - Open Document Optional Fields (view AP0403)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+OPTFIELD; OPTFIELD+IDVEND+IDINVC
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
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

## APOBP - Document Payments (view AP0027)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+CNTPAYMNBR+IDRMIT+DATEBUS+TRANSTYPE+CNTSEQNCE; IDBANK+CNTBTCH+CNTITEM+IDVEND+IDINVC+CNTPAYMNBR [D,M]; IDPREPAID+IDINVC+CNTPAYMNBR [D,M]; IDBANK+IDVEND+IDRMIT+LONGSERIAL+DATERMIT [D,M]; IDBANK+IDVEND+IDRMIT+LONGSERIAL+DATERMIT+CNTSEQNCE [D,M]; IDVEND+IDINVC+CNTPAYMNBR+DATEBUS [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTPAYMNBR BCD*3.0 Payment Number
  IDRMIT String*18 Check Number
  DATEBUS Date Posting Date
  TRANSTYPE Integer Document Type [6=Debit Note Applied To,7=Applied Debit Note,8=Credit Note Applied To,9=Applied Credit Note,10=Prepayment,11=Payment,12=Discount,14=Adjustment,16=Exchange Gain/Loss,17=Rounding,18=Retainage,19=Tax Withheld]
  CNTSEQNCE BCD*3.0 Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTBTCH BCD*5.0 Batch Number
  DATEBTCH Date Batch Date
  AMTPAYMHC BCD*10.3 Func. Payment Amount
  AMTPAYMTC BCD*10.3 Vend. Payment Amount
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEEXCHHC BCD*8.7 Exchange Rate
  SWOVRDRATE Integer Rate Overridden [0=No,1=Yes]
  IDBANK String*8 Bank Code
  TRXTYPE Integer Transaction Type [41=Debit Note Applied To,42=Applied Debit Note,43=Credit Note Applied To,44=Applied Credit Note,58=Prepayment - Applied,59=Prepayment - Reversed,51=Payment - Posted,52=Payment - Applied,53=Payment - Reversed,61=Discount - Posted,63=Discount - Reversed,81=Adjustment - Posted,83=Adjustment - Reversed,65=Exchange Gain/Loss - Posted,67=Exchange Gain/Loss - Reversed,91=Rounding - Posted,93=Rounding - Reversed,69=Unrealized Exchange Gain/Loss,100=Retainage - Invoiced,101=Retainage - Adjusted,102=Retainage - Revalued,103=Retainage - Exchange Gain/Loss,104=Retainage - Rounding,94=Payment - Invoice Reversed,105=Tax Withheld - Posted,106=Tax Withheld - Reversed]
  IDMEMOXREF String*22 Reference Document No.
  IDPREPAID String*22 Reserved:Matching Document No.
  IDRMITVEND String*12 Remitting Vendor No.
  DATERMIT Date Check Date
  CNTITEM BCD*4.0 Entry Number
  FISCYR String*4 Year
  FISCPER String*2 Period
  LONGSERIAL ??? Check Serial Number
  CODE1099 String*6 1099/CPRS Code
  AMT1099 BCD*10.3 1099/CPRS Amount
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  CODETAX String*12 Tax Authority

## APOBS - Document Sched. Payments (view AP0026)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDINVC+CNTPAYM; IDINVC+CNTPAYM [D,M]; IDVEND+IDORDRNBR+IDINVC+CNTPAYM [D,M]; IDVEND+IDPONBR+IDINVC+CNTPAYM [D,M]; IDVEND+DATEDUE+IDINVC+CNTPAYM [D,M]; IDVEND+AMTPYMRMTC+DATEDUE+IDINVC+CNTPAYM [D,M]; SWPAID+IDINVC+CNTPAYM [D,M]; IDVEND+DATEINVC+IDINVC+CNTPAYM [D,M]; SWPAID+IDPREPAID [D,M]; SWPAID+IDVEND+IDINVC+CNTPAYM [D,M]; IDVEND+RTGAPPLYTO+IDINVC+CNTPAYM [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*18 Check Number
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  SWPAID Integer Fully Paid [0=No,1=Yes]
  AMTDUEHC BCD*10.3 Original Amount (Func.)
  AMTDISCHC BCD*10.3 Original Discount (Func.)
  AMTDCSRMHC BCD*10.3 Remaining Discount (Func.)
  AMTPYMRMHC BCD*10.3 Remaining Amount (Func.)
  AMTDUETC BCD*10.3 Original Amount
  AMTDISCTC BCD*10.3 Original Discount
  AMTDSCRMTC BCD*10.3 Remaining Discount
  AMTPYMRMTC BCD*10.3 Remaining Amount
  IDORDRNBR String*22 Order Number
  IDPONBR String*22 PO Number
  IDGRP String*6 Group Code
  IDPREPAID String*22 Prepay Invoice Number
  IDTRXTYPE Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,26=Debit Note - Advance Credit Claim,32=Credit Note - Summary Entered,40=Interest Charge,50=Prepayment - Posted,51=Payment - Posted]
  TXTTRXTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,10=Prepayment,11=Payment]
  DATEINVC Date Document Date
  DATEACTV Date Activation Date
  DAYSTOPAY Integer Number of Days to Pay
  SWJOB Integer Job Related [0=No,1=Yes]
  AMTPYMLMTC BCD*10.3 Payment Limit
  RTGAPPLYTO String*22 Original Doc. No.

## APOFD - Optional Fields (view AP0500)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Vendors and Vendor Groups,1=Remit-To Locations,2=Invoices,3=Invoice Details,4=Payments,5=Adjustments,6=Revaluation]
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
  SWCONTROL Integer Payables Control [99=Not Applicable]
  SWRTG Integer Retainage [99=Not Applicable]
  SWDISCOUNT Integer Purchase Discount [99=Not Applicable]
  SWTAXRECOV Integer Recoverable Tax [99=Not Applicable]
  SWTAXEXP Integer Expense Tax [99=Not Applicable]
  SWREXCHG Integer Exchange Gain [99=Not Applicable]
  SWREXCHL Integer Exchange Loss [99=Not Applicable]
  SWUREXCHG Integer Unrealized Exchange Gain [99=Not Applicable]
  SWUREXCHL Integer Unrealized Exchange Loss [99=Not Applicable]
  SWROUND Integer Rounding [99=Not Applicable]
  SWDISTRIB Integer Distribution [99=Not Applicable]
  SWPREPAY Integer Prepayment [99=Not Applicable]
  SWMISCPAY Integer Miscellaneous Payment [99=Not Applicable]
  SWBANK Integer Bank [99=Not Applicable]
  SWADJ Integer Adjustment [99=Not Applicable]
  SWLABOUR Integer Labor [99=Not Applicable]
  SWOHEAD Integer Overhead [99=Not Applicable]
  SWPM Integer External Cost Transactions [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## APOFH - Optional Field Locations (view AP0501)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Vendors and Vendor Groups,1=Remit-To Locations,2=Invoices,3=Invoice Details,4=Payments,5=Adjustments,6=Revaluation]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## APP01 - Company Options (view AP0001)
Keys (first = PK; D=dups allowed, M=modifiable): IDP01
Fields (NAME type description [values]):
  IDP01 String*6 Options Record Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  SWMULTCURN Integer Multicurrency [0=No,1=Yes]
  SWEDITIMPT Integer Edit Imports [0=No,1=Yes]
  SWFRCLST Integer Force Listing of Batches [0=No,1=Yes]
  CNTARCVDAY BCD*3.0 Reserved
  SWEDITVNDR Integer Edit Vendor Statistics [0=No,1=Yes]
  CODETAXVND Integer Inc. Tax in Vendor Statistics [0=No,1=Yes]
  CODECLDRVN Integer Vendor Statistics Year Type [1=Calendar Year,2=Fiscal Year]
  CODEPERDVN Integer Vendor Statistics Period Type [1=Weekly,2=Seven days,3=Bi-weekly,4=Four weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Fiscal Period]
  SWBNKVNDR Integer Reserved
  CMNTDAYS BCD*3.0 Default No. Days to Keep Comments
  CNTRVALSEQ BCD*5.0 Next Revaluation Posting Sequence
  NAMECTAC String*60 Contact Name
  TEXTPHON String*30 Telephone Number
  TEXTFAX String*30 Fax Number
  SWKEEPDTLS Integer Keep History
  SWACCUVNDR Integer Keep Vendor Statistics [0=No,1=Yes]
  SWCALCTAX Integer Default Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  SWEDITSUB Integer Edit External Batches [0=No,1=Yes]
  SWTXBSECTL Integer Default Tax Base Control [0=Enter,1=Calculate,2=Distribute]
  SWTXCTLRC Integer Default Tax Reporting Control [0=Enter,1=Calculate,2=Distribute]
  SWTXDTLCLS Integer Default Detail Tax Class [0=Default to Vendor Tax Class,1=Default to 1]

## APP02 - Invoicing Options (view AP0002)
Keys (first = PK; D=dups allowed, M=modifiable): RECID02
Fields (NAME type description [values]):
  RECID02 String*6 Options Record Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  INVCBTCH BCD*5.0 Next Invoice Batch Number
  VCHRNBR BCD*5.0 Reserved
  SWALOWDISC Integer Reserved
  SWUSE1099 Integer Use 1099/CPRS Reporting [0=No,1=Yes]
  CLASLABEL String*10 Reserved
  CNTNEXTINV BCD*5.0 Next Invoice Posting Seq. Number
  SWCOAWARN Integer Reserved
  SWPOSTPRNT Integer Reserved
  SWALOWIVED Integer Reserved
  SWEDIT1099 Integer Edit 1099/CPRS Amounts [0=No,1=Yes]
  SW1099COPY Integer Copy 1099/CPRS Amount from Total [0=No,1=Yes]
  SWDATEBUS Integer Default Posting Date [0=Document Date,1=Batch Date,2=Session Date]

## APP03 - Payment and Aging Options (view AP0003)
Keys (first = PK; D=dups allowed, M=modifiable): RECID03
Fields (NAME type description [values]):
  RECID03 String*6 Options Record Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  DRCTBTCH BCD*5.0 Next Payment Batch Number
  MANLBTCH BCD*5.0 Reserved
  ADJBTCH BCD*5.0 Next Adjustment Batch Number
  ADJTRX BCD*5.0 Reserved
  PAYMRUN BCD*5.0 Reserved
  SWCHKPRNT Integer Reserved
  SWDOCORDR Integer Default Order of Open Documents [1=Document Number,2=PO Number,3=Due Date,4=Order Number,5=Document Date,6=Current Balance,7=Original Doc. No.]
  SWPAYMBANK Integer Reserved
  AGINPRD1 BCD*3.0 Aging Period 1
  AGINPRD2 BCD*3.0 Aging Period 2
  AGINPRD3 BCD*3.0 Aging Period 3
  SWAGECR Integer Age Credit Notes & Debit Notes [1=As Current,2=By Date]
  DTPREREG Date Date Last Preregistered
  TMPREREG Time Time Last Preregistered
  DTDRCTCHK Date Date Last Direct Check
  TMDRCTCHK Time Time Last Direct Check
  DTSYSCHK Date Date Last Sys. Check
  TMSYSCHK Time Time Last Sys. Check
  SWSYSBTCH Integer Allow Edit of System Batches [0=No,1=Yes]
  SWFORCREG Integer Reserved
  IDDFLTBANK String*8 Default Bank Code
  DFLTRATE String*2 Reserved
  PAYMCODE String*12 Payment Code
  CNTPPDBTCH BCD*5.0 Next Prepayment Number
  CNTSYSBTCH BCD*5.0 Reserved
  CNTNXTPAYM BCD*5.0 Next Payment Posting Sequence
  CNTNXTADJM BCD*5.0 Next Adjustment Posting Sequence
  SWPAYMBTCH Integer Allow Adjustments in Payment Batch [0=No,1=Yes]
  PPDPREFIX String*6 Prepayment Prefix
  PPDPFXLEN BCD*2.0 Prepayment Number Length
  SWAGEUAPL Integer Age Unapplied Cash & Prepayments [1=As Current,2=By Date]
  CNTNXTUAPL BCD*5.0 Reserved
  ADPFX String*6 Adjustment Prefix
  ADPFXLEN BCD*2.0 Adjustment Number Length
  ADNEXTSEQ BCD*5.0 Next Adjustment Number
  RPPFX String*6 Recurring Payable Prefix
  RPPFXLEN BCD*2.0 Recurring Payable Number Length
  RPNEXTSEQ BCD*5.0 Next Recurring Payable Number
  RMITTYPE Integer Default Transaction Type [1=Payment,2=Prepayment,3=Apply Document,4=Misc. Payment]
  PYPFX String*6 Payment Prefix
  PYPFXLEN BCD*2.0 Payment Number Length
  PYNEXTSEQ BCD*5.0 Next Payment Number
  RIPFX String*6 Retainage Invoice Prefix
  RIPFXLEN BCD*2.0 Retainage Invoice Number Length
  RINEXTSEQ BCD*5.0 Next Retainage Invoice Number
  RCPFX String*6 Retainage Credit Note Prefix
  RCPFXLEN BCD*2.0 Retainage Credit Note No. Length
  RCNEXTSEQ BCD*5.0 Next Retainage Credit Note No.
  RDPFX String*6 Retainage Debit Note Prefix
  RDPFXLEN BCD*2.0 Retainage Debit Note No. Length
  RDNEXTSEQ BCD*5.0 Next Retainage Debit Note No.
  SWRTG Integer Use Retainage [0=No,1=Yes]
  SWRTGBASE Integer Retainage Base [0=Document Total After Taxes,1=Document Total Before Taxes]
  RTGSCHDKEY String*12 Retainage Schedule
  RTGSCHDLNK BCD*10.0 Retainage Schedule Link
  RTGLASTRUN Date Date Retainage Sched. Last Run
  RTGDAYS Integer Days Retained
  RTGPERCENT BCD*5.5 Percent Retained
  RTGADVDAYS Integer Days Before Retainage Due
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  SWTXRTGRPT Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  SWCHNGRMIT Integer Allow Edit of Remit-To Info. [0=No,1=Yes]
  SWCHKDUP Integer Check for Duplicate Checks [0=None,1=Warning,2=Error]
  SWSHPYPND Integer Include Pending Transactions [0=None,1=Payments,2=Payments and Adjustments,3=All Transactions]
  SWDATEBUS Integer Default Posting Date [0=Document Date,1=Batch Date,2=Session Date]
  SORTCHKBY Integer Sort Checks By [0=Transaction Entry Number,1=Vendor Number,2=Payee Name,3=Payee Country,4=Payee Zip/Postal Code]

## APP04 - Integration Options (view AP0004)
Keys (first = PK; D=dups allowed, M=modifiable): RECID04
Fields (NAME type description [values]):
  RECID04 String*6 Options Record Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  SESSNBR BCD*5.0 Reserved
  SWGLPSTDFR Integer Defer G/L Transactions [0=During Posting,1=On Request Using Create G/L Batch Icon]
  SWGLAPDBTH Integer Create G/L Transactions By [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  SWGLPSTCON Integer Consolidate G/L Transactions [0=Do Not Consolidate,1=Consolidate by Post Seq., Account and Fiscal Period,2=Consolidate by Post Seq., Account, Fiscal Period and Source]
  CODEGLREF Integer RESERVED: G/L Reference Field
  CODEGLDESC Integer RESERVED: G/L Description Field
  CNTLASPAYM BCD*5.0 Last Payment Posting Seq. to G/L
  CNTLASINVC BCD*5.0 Last Invoice Posting Seq. to G/L
  CNTLASRVAL BCD*5.0 Last Reval. Posting Seq. to G/L
  CNTLASADJM BCD*5.0 Last Adj. Posting Seq. to G/L
  SRCTYPEIN String*2 G/L Src code - Invoice
  SRCTYPEDB String*2 G/L Src code - Debit Note
  SRCTYPECR String*2 G/L Src code - Credit Note
  SRCTYPEIT String*2 G/L Src code - Interest
  SRCTYPEPY String*2 G/L Src code - Payment
  SRCTYPEED String*2 G/L Src code - Discount
  SRCTYPEGL String*2 G/L Src code - Revaluation
  SRCTYPEAD String*2 G/L Src code - Adjustment
  SRCTYPECO String*2 G/L Src code - Consolidation
  SRCTYPEPI String*2 G/L Src code - Prepayment
  SRCTYPERD String*2 G/L Src code - Rounding
  SRCTYPEPYR String*2 G/L Src code - Payment Reversal

## APP05 - Vendor Options (view AP0139)
Keys (first = PK; D=dups allowed, M=modifiable): RECID05
Fields (NAME type description [values]):
  RECID05 String*6 Vendor Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEMNTN Date Date Last Maintained
  CMNTDAYS BCD*3.0 Default No. Days for Expiry
  FLUPDAYS BCD*3.0 Default No. Days for Follow Up
  CMNTTYPE String*8 Default Comment Type
  SWCMNTTYPE Integer Allow Blank Comment Type [0=No,1=Yes]

## APPJAID - Posting Journal Generated AP Details (view AP0517)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE+GENTYPE
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  CNTSEQENCE Long Sequence No.
  GENTYPE Integer Generation Type [1=AI to AP]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*6 Generated Company
  GCNTBTCH BCD*5.0 Generated Batch No.
  GCNTITEM BCD*4.0 Generated Entry No.
  GCNTLINE BCD*3.0 Generated Line No.
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Project/Category Resource
  BILLDATE Date Billing Date
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLCURN String*3 Billing Currency
  BILLRATE BCD*10.6 Billing Rate
  IDITEM String*16 Item Number
  AMTCOST BCD*10.6 Cost
  QTYINVC BCD*10.5 Quantity
  UNITMEAS String*10 Unit of Measure
  IDDIST String*6 Distribution Code
  TEXTDESC String*60 Description
  IDGLACCT String*45 G/L Account
  AMTDIST BCD*10.3 Distributed Amount
  AMTDISTNET BCD*10.3 Distributed Amount Before Taxes
  AMTINCLTAX BCD*10.3 Tax Amount Included in Price
  AMTTOTTAX BCD*10.3 Total Tax Amount
  AMTTAXTOBE BCD*10.3 Tax Amount to be Allocated
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  RATETAX1 BCD*8.5 Tax Rate 1
  RATETAX2 BCD*8.5 Tax Rate 2
  RATETAX3 BCD*8.5 Tax Rate 3
  RATETAX4 BCD*8.5 Tax Rate 4
  RATETAX5 BCD*8.5 Tax Rate 5
  AMTTAXREC1 BCD*10.3 Recoverable Tax Amount 1
  AMTTAXREC2 BCD*10.3 Recoverable Tax Amount 2
  AMTTAXREC3 BCD*10.3 Recoverable Tax Amount 3
  AMTTAXREC4 BCD*10.3 Recoverable Tax Amount 4
  AMTTAXREC5 BCD*10.3 Recoverable Tax Amount 5
  AMTTAXEXP1 BCD*10.3 Expense Sep. Tax Amount 1
  AMTTAXEXP2 BCD*10.3 Expense Sep. Tax Amount 2
  AMTTAXEXP3 BCD*10.3 Expense Sep. Tax Amount 3
  AMTTAXEXP4 BCD*10.3 Expense Sep. Tax Amount 4
  AMTTAXEXP5 BCD*10.3 Expense Sep. Tax Amount 5
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5

## APPJAIH - Posting Journal Generated AP Entries (view AP0516)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*6 Generated Company
  GCNTBTCH BCD*5.0 Generated Batch No.
  GCNTITEM BCD*4.0 Generated Entry No.
  TEXTTRX Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest]
  IDTRX Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,32=Credit Note - Summary Entered,40=Interest Charge]
  INVCDESC String*60 Invoice Description
  IDVEND String*12 Vendor Number
  CODEVNDGRP String*6 Vendor Group Code
  IDACCTSET String*6 Account Set
  IDRMITTO String*6 Remit-To Location
  IDINVC String*22 Document Number
  INVCAPPLTO String*22 Apply-to Document
  ORDRNBR String*22 Order Number
  PONBR String*22 PO Number
  SWJOB Integer Job Related [0=No,1=Yes]
  DATEINVC Date Invoice Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  HCODECURN String*3 Currency Code (Functional)
  CODECURN String*3 Currency Code (Source)
  RATETYPE String*2 Rate Type
  CODEOPER Integer Rate Operator [1=Multiply,2=Divide]
  EXCHRATEHC BCD*8.7 Exchange Rate
  DATERATE Date Rate Date
  TERMCODE String*6 Terms
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  PCTDISC BCD*5.5 Discount Percentage
  AMTDSCBASE BCD*10.3 Discount Base
  AMTDISCAVL BCD*10.3 Discount Amount Available
  AMTDSBWTAX BCD*10.3 Discount Base With Tax
  AMTDSBNTAX BCD*10.3 Discount Base Without Tax
  CODETAXGRP String*12 Tax Group
  SWTAXBL Integer Taxable [0=No,1=Yes]
  SWCALCTX Integer Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  AMTINVCTOT BCD*10.3 Document Total Before Taxes
  AMTGROSTOT BCD*10.3 Document Total Including Tax
  AMTTAXTOT BCD*10.3 Total Tax Amount
  AMTRECTAX BCD*10.3 Recoverable Taxes
  AMTEXPTAX BCD*10.3 Expensed Separately Taxes
  AMTAXTOBE BCD*10.3 Tax Amount to be Allocated
  ID1099CLAS String*6 1099/CPRS Code
  AMT1099 BCD*10.3 1099/CPRS Amount
  IDDISTSET String*6 Distribution Set
  AMTDISTSET BCD*10.3 Distribution Set Amount
  VALUES Long Optional Fields
  DATEBUS Date Posting Date
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  VENDNAME String*60 Vendor Name
  RMITNAME String*60 Remit-To Name

## APPJD - Posting Journal Details (view AP0510)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE; TYPEBTCH+POSTSEQNCE+FISCYR+FISCPER+IDACCT+CODECURN+SRCETYPE+IDINVC [D,M]
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  CNTSEQENCE Long Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDVEND String*12 Vendor No.
  IDINVC String*22 Document No.
  CNTPAYM BCD*3.0 Payment No.
  TRANSTYPE Integer Document Type
  IDTRANS Integer Transaction Type
  DATEBUS Date Posting Date
  DATEINVC Date Document Date
  DATEDISC Date Discount Date
  DATEDUE Date Due Date
  IDBANK String*8 Bank Code
  IDRMIT String*18 Check/Receipt No.
  LONGSERIAL ??? Serial Number
  CNTLINE BCD*3.0 Line No.
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDACCT String*45 G/L Account
  ACCTTYPE Integer Account Type [1=Accounts Payable,2=Offset,6=Tax Summary,7=Bank]
  SRCETYPE String*2 G/L Source Type
  GLREF String*60 G/L Reference
  GLDESC String*60 G/L Description
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEEXCHHC BCD*8.7 Exchange Rate
  SWTAXTYPE Integer Tax Type [0=None,1=Recoverable,2=Expense Separately,3=Allocated,4=Reverse Charge,5=Tax Withheld]
  IDDIST String*6 Distribution Code
  AMTEXTNDHC BCD*10.3 Extended Amount (Functional)
  AMTEXTNDTC BCD*10.3 Extended Amount (Source)
  BASETAXHC BCD*10.3 Tax Base (Functional)
  BASETAXTC BCD*10.3 Tax Base (Source)
  AMTTAXHC BCD*10.3 Tax Amount (Functional)
  AMTTAXTC BCD*10.3 Tax Amount (Source)
  GLBATCH String*6 G/L Batch No.
  GLENTRY String*5 G/L Entry No.
  CNTADJNBR BCD*5.0 Adjustment Number
  AMTADJHCUR BCD*10.3 Adj. Amount/RV asof (Functional)
  AMTADJTCUR BCD*10.3 Adj. Amount/RV asof (Source)
  AMTDSCHCUR BCD*10.3 Discount Amount (Functional)
  AMTDSCTCUR BCD*10.3 Discount Amount (Source)
  RTGDATEDUE Date Date Retainage Due
  SWRTGRATE Integer Retainage Exchange Rate
  RTGAMTTC BCD*10.3 Retainage Amount (Source)
  RTGAMTHC BCD*10.3 Retainage Amount (Functional)
  VALUES Long Optional Fields
  DESCOMP String*6 Destination
  ROUTE Integer Route No.
  GLCOMMENT String*250 G/L Comment
  RATEDOC BCD*8.7 Document's Exchange Rate

## APPJDO - Posting Journal Detail Optional Fields (view AP0513)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE+OPTFIELD; OPTFIELD+TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  CNTSEQENCE Long Sequence No.
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

## APPJGID - Posting Journal Generated GL Details (view AP0519)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+CNTSEQENCE+GENTYPE+BATCHNBR+JOURNALID+TRANSNBR
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  CNTSEQENCE Long Sequence No.
  GENTYPE Integer Generation Type [1=AI to GI,4=Recoverable Tax,3=Expensed Separately Tax,2=Allocated Tax,5=Balance,6=Exch. Rounding]
  BATCHNBR String*6 Generated Batch No.
  JOURNALID String*5 Generated Entry No.
  TRANSNBR String*10 Generated Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSDATE Date Transaction Date
  TRANSREF String*60 Reference
  TRANSDESC String*60 Description
  DESCOMP String*6 Destination
  ROUTE Integer Route No.
  ACCTID String*45 G/L Account
  SRCELDGR String*2 Source Ledger
  SRCETYPE String*2 Source Type
  SCURNAMT BCD*10.3 Source Amount
  TRANSAMT BCD*10.3 Functional Amount
  TRANSQTY BCD*10.3 Quantity
  VALUES Long Optional Fields

## APPJH - Posting Journal Entries (view AP0511)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDVEND String*12 Vendor No.
  IDINVC String*22 Document No.
  CNTPAYM BCD*3.0 Payment No.
  TRANSTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,10=Prepayment,11=Payment,14=Adjustment,16=Exchange Gain/Loss]
  TRXTYPE Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,32=Credit Note - Summary Entered,40=Interest Charge,81=Adjustment - Posted,57=Prepayment - Posted,58=Prepayment - Applied,43=Credit Note Applied To,44=Applied Credit Note,51=Payment - Posted,52=Payment - Applied,53=Payment - Reversed,69=Unrealized Exchange Gain/Loss,65=Exchange Gain/Loss - Posted,94=Payment - Invoice Reversed]
  IDGRP String*6 Group Code
  IDACCTSET String*6 Account Set
  CODETAXGRP String*12 Tax Group
  CODETERM String*6 Terms Code
  IDRMITTO String*6 Remit-To Location Code
  DATEINVC Date Document Date
  DATEDISC Date Discount Date
  DATEDUE Date Due Date
  DATEBTCH Date Batch Date
  PCTDISC BCD*5.5 Discount Percentage
  SWNONRCVBL Integer Misc. Payment Flag
  SWSTATUS Integer Payment Edited Flag [0=No,1=Yes]
  GLBATCH String*6 G/L Batch No.
  GLENTRY String*5 G/L Entry No.
  CNTADJNBR BCD*5.0 Adjustment Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDINVCAPPL String*22 Apply-To Doc. No.
  DESC String*60 Description
  IDBANK String*8 Bank Code
  IDRMIT String*18 Check/Receipt No.
  LONGSERIAL ??? Serial Number
  MISCRMITTO String*60 Misc. Payment Remit-To
  CODECURNTC String*3 Currency Code (Source)
  RATETYPETC String*2 Rate Type (Source->Functional)
  RATEDATETC Date Rate Date (Source->Functional)
  RATEEXCHTC BCD*8.7 Exchange Rate (Source->Functional)
  RATEOPTC Integer Rate Operator (Source->Functional)
  SWRATETC Integer Rate Override (Source)
  CODECURNBC String*3 Currency Code (Bank)
  RATETYPEBC String*2 Rate Type (Bank->Functional)
  RATEDATEBC Date Rate Date (Bank->Functional)
  RATEEXCHBC BCD*8.7 Exchange Rate (Bank->Functional)
  RATEOPBC Integer Rate Operator (Bank->Functional)
  SWRATEBC Integer Rate Override (Bank)
  AMTINVCTC BCD*10.3 Document Total Less Retainage (Source)
  SWJOB Integer Job Related
  SWRTG Integer Retainage Invoice Flag [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms Code
  RTGDATEDUE Date Date Retainage Due
  SWRTGRATE Integer Retainage Exchange Rate
  RTGAPPLYTO String*22 Original Doc. No.
  RTGAMTTC BCD*10.3 Retainage Amount (Source)
  RTGAMTHC BCD*10.3 Retainage Amount (Functional)
  VALUES Long Optional Fields
  ORIGCOMP String*6 Originator
  IDDISTSET String*6 Distribution Set
  AMTTC BCD*10.3 Check Amount Vend. Curr.
  AMTHC BCD*10.3 Check Amount Func. Curr.
  AMTBC BCD*10.3 Payment Amount
  PAYMCODE String*12 Payment Code
  PAYMTYPE Integer Payment Type [0=,1=Cash,2=Check,3=Credit Card,4=Other]
  TEXTREF String*60 Reference
  DATEBUS Date Posting Date
  REVINVC Integer Reverse Invoice
  IDN String*30 Import Declaration Number
  ENTEREDBY String*8 Entered By

## APPJHO - Posting Journal Entry Optional Fields (view AP0514)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM+OPTFIELD; OPTFIELD+TYPEBTCH+POSTSEQNCE+CNTBTCH+CNTITEM
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
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

## APPJS - Posting Journals (view AP0512)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEPOSTED Date System Date
  DATEBUS Date Date Posted in A/P
  SWPRINTED Integer Printed? [0=No,1=Yes]
  SWPOSTGL Integer Posted to G/L? [0=No,1=Yes]
  DATEPOSTGL Date Date Posted to G/L
  SWGLCONSL Integer Consolidated for G/L?
  PGMVER String*3 Program Version

## APPOOP - Create Open Document List (view AP0048)
Keys (first = PK; D=dups allowed, M=modifiable): PAYMTYPE+CNTBTCH+CNTRMIT+CNTKEY
Fields (NAME type description [values]):
  PAYMTYPE String*2 Payment Type
  CNTBTCH BCD*5.0 Batch Number
  CNTRMIT BCD*4.0 Entry Number
  CNTKEY BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PAYMSCHD BCD*3.0 Number of Payments Scheduled
  PROTYPE Integer Process Type [1=Select]
  SHOWTYPE Integer Show Type [1=All,2=Invoice,3=Debit Note,4=Credit Note,5=Prepayment]
  ORDERBY Integer Order By [1=Document Number,2=PO Number,3=Due Date,4=Order Number,5=Document Date,6=Current Balance,7=Original Doc. No.]
  IDVEND String*12 Vendor Number
  IDINVC String*22 Invoice Number
  IDRMIT String*18 Check Number
  VENDPO String*22 PO Number
  ORDRNBR String*22 Order Number
  TRXTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,10=Prepayment]
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  DATEINVC Date Invoice Date
  AMTDUE BCD*10.3 Payment Schedule Amount Due
  AMTNET BCD*10.3 Payment Schedule Amount Net
  AMTDISC BCD*10.3 Payment Schedule Amount Disc
  PAYMAMT BCD*10.3 Payment Amount
  DISCAMT BCD*10.3 Discount Amount Taken
  APPLY String*1 Apply
  MODE Integer Mode [0=Select,1=Direct]
  IDTRXTYPE Integer Transaction Type [12=Invoice - Summary Entered,13=Invoice - Recurring Charge,22=Debit Note - Summary Entered,32=Credit Note - Summary Entered,40=Interest Charge,50=Prepayment - Posted]
  ADJAMT BCD*10.3 Adjustment Amount
  STDOCSTR String*22 Starting Document Number
  STDOCDTE Date Starting Date
  STDOCAMT BCD*10.3 Starting Amount
  AMTRMIT BCD*10.3 Remit Amount
  OBSDISC BCD*10.3 Payment Sched. Discount Avail.
  TCPLINE BCD*3.0 TCP Line Number
  STRTVEND String*12 Starting Vendor Number
  ORIGAPLY String*1 Original Apply
  PNDPAYTOT BCD*10.3 Pending Payment Amount
  PNDDSCTOT BCD*10.3 Pending Discount Amount
  PNDADJTOT BCD*10.3 Pending Adjustment Amount
  AMTPNDBAL BCD*10.3 Pending Balance
  AMTORIGDOC BCD*10.3 Original Document Total
  SWJOB Integer Job Related [0=No,1=Yes]
  RTGAPPLYTO String*22 Original Doc. No.
  SWHOLD Integer On Hold [0=No,1=Yes]
  TEXTDESC String*60 Description
  TEXTREF String*60 Reference
  AMTWHD1TC BCD*10.3 Tax Withheld Amount 1
  AMTWHD2TC BCD*10.3 Tax Withheld Amount 2
  AMTWHD3TC BCD*10.3 Tax Withheld Amount 3
  AMTWHD4TC BCD*10.3 Tax Withheld Amount 4
  AMTWHD5TC BCD*10.3 Tax Withheld Amount 5
  AMTWHDTOT BCD*10.3 Tax Withheld Amount Total
  PNDWHD1TOT BCD*10.3 Pending Tax Withheld Amount 1
  PNDWHD2TOT BCD*10.3 Pending Tax Withheld Amount 2
  PNDWHD3TOT BCD*10.3 Pending Tax Withheld Amount 3
  PNDWHD4TOT BCD*10.3 Pending Tax Withheld Amount 4
  PNDWHD5TOT BCD*10.3 Pending Tax Withheld Amount 5
  PNDWHDTOT BCD*10.3 Pending Tax Withheld Total
  CODETAX1 String*12 Document Tax Authority 1
  CODETAX2 String*12 Document Tax Authority 2
  CODETAX3 String*12 Document Tax Authority 3
  CODETAX4 String*12 Document Tax Authority 4
  CODETAX5 String*12 Document Tax Authority 5

## APPTER - Posting Error Messages (view AP0038)
Keys (first = PK; D=dups allowed, M=modifiable): CODEBATCH+POSTINGSEQ+CNTBATCH+CNTITEM+CNTLINE+CNTERROR+CNTSEQ
Fields (NAME type description [values]):
  CODEBATCH String*2 Batch Type
  POSTINGSEQ BCD*5.0 Posting Sequence No.
  CNTBATCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  CNTERROR BCD*4.0 Error Number
  CNTSEQ BCD*3.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CODEMSG String*7 Message Number
  ERRDESC String*250 Error Description
  ERRCODEPYM String*2 Error Batch Type
  CNTERRBTCH BCD*5.0 Error Batch Number
  CNTERRITEM BCD*4.0 Error Entry Number
  CNTERRLINE BCD*3.0 Error Line Number
  CNTERRSEQ BCD*3.0 Error Sequence Number

## APPTP - Payment Codes (view AP0010)
Keys (first = PK; D=dups allowed, M=modifiable): PAYMCODE
Fields (NAME type description [values]):
  PAYMCODE String*12 Payment Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTVSW Integer Status [0=Inactive,1=Active]
  INACTDATE Date Inactive Date
  DTELSTMTN Date Date Last Maintained
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,4=Other]

## APPYM - Posted Payments (view AP0029)
Keys (first = PK; D=dups allowed, M=modifiable): IDBANK+IDVEND+IDRMIT+LONGSERIAL+DATERMIT; IDBANK+CNTBTCH+CNTITEM [D,M]; IDVEND+IDRMIT+DATEBATCH [D,M]; IDBANK+IDRMIT+LONGSERIAL [D,M]; IDVEND+DATERMIT+IDRMIT [D,M]
Fields (NAME type description [values]):
  IDBANK String*8 Bank Code
  IDVEND String*12 Vendor Number
  IDRMIT String*18 Check Number
  LONGSERIAL ??? Check Serial Number
  DATERMIT Date Check Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEBATCH Date Batch Date
  AMTRMITTC BCD*10.3 Check Amount Vend. Curr.
  AMTPAYM BCD*10.3 Payment Amount
  AMTDISC BCD*10.3 Discount Amount
  PAYMCODE String*12 Payment Code
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  SWOVRDRATE Integer Bank Rate Overridden [0=No,1=Yes]
  TEXTRETRN String*60 Reason for Reversal
  AMTROUNDER BCD*10.3 Amount of Rounding Error
  DATERATE Date Bank Rate Date
  CNTFISCYR String*4 Fiscal Year
  CNTFISCPER String*2 Fiscal Period
  TEXTPAYOR String*60 Remit To
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  SWCHKCLRD Integer Check Cleared [0=Outstanding,1=Cleared,2=Reversed]
  AMTRMITHC BCD*10.3 Check Amount Func. Curr.
  AMTADJ BCD*10.3 Amount Adjusted
  DATECLRD Date Date Cleared
  DATERVRSD Date Date Reversed
  TRXTYPETXT Integer Document Type [5=Unapplied Cash,10=Prepayment,11=Payment]
  IDINVC String*22 Document No.
  RATEOP Integer Rate Operator
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,4=Other]
  CUID Long Client Unique ID
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  IDACCT String*45 G/L Account
  SWNONRCVBL Integer Misc. Payment Flag
  SWJOB Integer Job Related [0=No,1=Yes]
  IDINVCMTCH String*22 Invoice Number
  SWTXAMTCTL Integer Calculate Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  SWTXBSECTL Integer Calculate Tax Base Control [0=Enter,1=Calculate,2=Distribute]
  CODETAXGRP String*12 Tax Group
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TXBSE1TC BCD*10.3 Tax Base 1
  TXBSE2TC BCD*10.3 Tax Base 2
  TXBSE3TC BCD*10.3 Tax Base 3
  TXBSE4TC BCD*10.3 Tax Base 4
  TXBSE5TC BCD*10.3 Tax Base 5
  TXAMT1TC BCD*10.3 Tax Amount 1
  TXAMT2TC BCD*10.3 Tax Amount 2
  TXAMT3TC BCD*10.3 Tax Amount 3
  TXAMT4TC BCD*10.3 Tax Amount 4
  TXAMT5TC BCD*10.3 Tax Amount 5
  TXTOTTC BCD*10.3 Tax Total
  AMTNETTC BCD*10.3 Dist. Amount Net of Taxes
  TXALLTC BCD*10.3 Tax Allocated Total
  TXEXPTC BCD*10.3 Tax Expensed Total
  TXRECTC BCD*10.3 Tax Recoverable Total
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=Enter,1=Calculate,2=Distribute]
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operator
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Total
  TXEXPRC BCD*10.3 Tax Reporting Expensed Total
  TXRECRC BCD*10.3 Tax Reporting Recoverable Total
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  TXTOTHC BCD*10.3 Func. Tax Total
  AMTNETHC BCD*10.3 Func. Dist. Amount Net of Taxes
  TXALLHC BCD*10.3 Func. Tax Allocated Total
  TXEXPHC BCD*10.3 Func. Tax Expensed Total
  TXRECHC BCD*10.3 Func. Tax Recoverable Total
  CNTACC Long Number of Advance Credit Claims
  AMTACCTC BCD*10.3 Total Advance Credit Claim
  AMTACCHC BCD*10.3 Func. Total Advance Credit Claim
  DATEBUS Date Posting Date
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5
  AMTCXBS1TC BCD*10.3 Reverse Charges Base 1
  AMTCXBS2TC BCD*10.3 Reverse Charges Base 2
  AMTCXBS3TC BCD*10.3 Reverse Charges Base 3
  AMTCXBS4TC BCD*10.3 Reverse Charges Base 4
  AMTCXBS5TC BCD*10.3 Reverse Charges Base 5
  AMTCXTX1TC BCD*10.3 Reverse Charges Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charges Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charges Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charges Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charges Amount 5

## APRAS - Account Sets (view AP0006)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTSET
Fields (NAME type description [values]):
  ACCTSET String*6 Account Set Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELASTMN Date Date Last Maintained
  IDACCTAP String*45 Payables Control Account
  SUSPACCT String*45 Reserved
  DISCACCT String*45 Discounts Account
  PPAYACCT String*45 Prepayment Account
  CURRCODE String*3 Currency Code for Account
  URLZGNACT String*45 Unrealized Exchange Gain Account
  URLZLSACT String*45 Unrealized Exchange Loss Account
  RLZGNACT String*45 Exchange Gain Account
  RLZLSACT String*45 Exchange Loss Account
  ADJSTACT String*45 Reserved
  RTGACCT String*45 Retainage Account
  RNDACCT String*45 Exchange Rounding Account

## APRDC - Distribution Codes (view AP0005)
Keys (first = PK; D=dups allowed, M=modifiable): DISTID
Fields (NAME type description [values]):
  DISTID String*6 Distribution Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  IDGLACCT String*45 G/L Account
  IDACCTTAX String*45 Reserved
  SWDISCABL Integer Discountable [0=No,1=Yes]

## APRPD - Recurring Payable Details (view AP0065)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDRECURR+CNTLINE
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDRECURR String*16 Recurring Payable Code
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDDISTCODE String*6 Distribution Code
  DESC String*60 Distribution Description
  IDGLACCT String*45 G/L Account
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMTDIST BCD*10.3 Distributed Amount
  AMTDISTNET BCD*10.3 Distributed Amount Before Taxes
  AMTTAXINCL BCD*10.3 Dist. Tax included in Price
  AMTTAXEXCL BCD*10.3 Dist. Tax excluded from Price
  AMTTOTTAX BCD*10.3 Tax Amount Total
  BASETAX1 BCD*10.3 Tax Base 1
  BASETAX2 BCD*10.3 Tax Base 2
  BASETAX3 BCD*10.3 Tax Base 3
  BASETAX4 BCD*10.3 Tax Base 4
  BASETAX5 BCD*10.3 Tax Base 5
  SWDISCABL Integer Discountable [0=No,1=Yes]
  VALUES Long Optional Fields
  COMMENT String*250 Comment
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=]
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXTX1TC BCD*10.3 Reverse Charge Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charge Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charge Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charge Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charge Amount 5

## APRPDO - Recurring Payable Detail Fields (view AP0404)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDRECURR+CNTLINE+OPTFIELD; OPTFIELD+IDVEND+IDRECURR+CNTLINE
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDRECURR String*16 Recurring Payable Code
  CNTLINE BCD*3.0 Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Optional Field Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## APRPH - Recurring Payables (view AP0064)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDRECURR; IDRECURR+IDVEND; SCHEDKEY+SCHEDLINK [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDRECURR String*16 Recurring Payable Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELSTMTN Date Date Last Maintained
  DATEEFF Date Effective Date
  EXPIRETYPE Integer Expiration Type [0=No Expiration,1=Specific Date,2=Maximum Amount,3=Number of Invoices]
  DATEEXPIRE Date Expiration Date
  MAXCOUNT Integer Maximum Number of Invoices
  MAXAMT BCD*10.3 Maximum Total Invoice Amount
  LASTDATE Date Last Invoice Date Posted
  LASTAMT BCD*10.3 Last Invoice Amount Posted
  YTDCOUNT Integer YTD Number of Invoices
  YTDAMT BCD*10.3 YTD Total Invoice Amount
  ORDERNBR String*22 Order Number
  PONBR String*22 PO Number
  INVCDESC String*60 Invoice Description
  IDRMITTO String*6 Remit-To Location
  CODECURN String*3 Currency Code
  RATETYPE String*2 Rate Type
  TERMSCODE String*6 Terms
  DISTMETHOD Integer Reserved
  IDDISTSET String*6 Distribution Set
  AMTDISTSET BCD*10.3 Distribution Amount
  TAXGRP String*12 Tax Group
  SWCALCTAX Integer Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Inclusive 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Inclusive 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Inclusive 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Inclusive 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Inclusive 5 [0=No,1=Yes]
  AMTTAX1 BCD*10.3 Tax Amount 1
  AMTTAX2 BCD*10.3 Tax Amount 2
  AMTTAX3 BCD*10.3 Tax Amount 3
  AMTTAX4 BCD*10.3 Tax Amount 4
  AMTTAX5 BCD*10.3 Tax Amount 5
  AMTDISTNET BCD*10.3 Distributed Total Before Taxes
  AMTDIST BCD*10.3 Invoice Subtotal
  CODE1099 String*6 1099/CPRS Code
  AMT1099 BCD*10.3 1099/CPRS Amount
  LASTLINE BCD*3.0 Last Detail Seq. No.
  SCHEDKEY String*12 Schedule
  SCHEDLINK BCD*10.0 Schedule Link
  AMTTOTAL BCD*10.3 Document Total
  BASETAX1 BCD*10.3 Tax Base 1
  BASETAX2 BCD*10.3 Tax Base 2
  BASETAX3 BCD*10.3 Tax Base 3
  BASETAX4 BCD*10.3 Tax Base 4
  BASETAX5 BCD*10.3 Tax Base 5
  SWTAXBL Integer Invoice Taxable [0=No,1=Yes]
  SWTXBSECTL Integer Tax Base Control [0=Enter,1=Calculate,2=Distribute]
  AMTTAXINCL BCD*10.3 Total Dist. Tax incl. in Price
  AMTTAXEXCL BCD*10.3 Total Dist. Tax excl. from Price
  AMTTAXTOT BCD*10.3 Total Tax Amount
  VALUES Long Optional Fields
  SWJOB Integer Job Related [0=No,1=Yes]
  DATENEXT Date Next Scheduled Date
  DATELSTGEN Date Last Invoice Date Generated
  OPENCOUNT Integer Unposted Number of Invoices
  OPENAMOUNT BCD*10.3 Unposted Total Invoice Amount
  POSTCOUNT Integer Posted Number of Invoices
  POSTAMOUNT BCD*10.3 Posted Total Invoice Amount
  LSTIDINVC String*22 Last Invoice Number Posted
  LSTCNTBTCH BCD*5.0 Last Batch Number Posted
  LSTCNTITEM BCD*4.0 Last Entry Number Posted
  LSTPOSTSEQ BCD*5.0 Last Posting Sequence Number
  IDACCTSET String*6 Account Set
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXBS1TC BCD*10.3 Reverse Charges Base 1
  AMTCXBS2TC BCD*10.3 Reverse Charges Base 2
  AMTCXBS3TC BCD*10.3 Reverse Charges Base 3
  AMTCXBS4TC BCD*10.3 Reverse Charges Base 4
  AMTCXBS5TC BCD*10.3 Reverse Charges Base 5
  AMTCXTX1TC BCD*10.3 Reverse Charges Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charges Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charges Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charges Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charges Amount 5

## APRPHO - Recurring Payable Optional Fields (view AP0405)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDRECURR+OPTFIELD; OPTFIELD+IDVEND+IDRECURR
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDRECURR String*16 Recurring Payable Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Optional Field Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## APRSTRT - Restart (view AP0061)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## APRTA - Terms (view AP0012)
Keys (first = PK; D=dups allowed, M=modifiable): TERMSCODE
Fields (NAME type description [values]):
  TERMSCODE String*6 Terms Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CODEDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  DATELASTMN Date Date Last Maintained
  SWMULTPAYM Integer Use Payment Schedule [0=No,1=Yes]
  CODEVAT Integer Calc. Base for Discount with Tax [1=Included,2=Excluded]
  CODEDISTYP Integer Method of Calc for Discount Date [1=Days From Invoice Date,2=End of Next Month,3=Day of Next Month,4=Days from Day of Next Month,5=Disc Date Table]
  DISDAYSTR1 BCD*2.0 Discount Table Starting Day 1
  DISDAYSTR2 BCD*2.0 Discount Table Starting Day 2
  DISDAYSTR3 BCD*2.0 Discount Table Starting Day 3
  DISDAYSTR4 BCD*2.0 Discount Table Starting Day 4
  DISDAYEND1 BCD*2.0 Discount Table Ending Day 1
  DISDAYEND2 BCD*2.0 Discount Table Ending Day 2
  DISDAYEND3 BCD*2.0 Discount Table Ending Day 3
  DISDAYEND4 BCD*2.0 Discount Table Ending Day 4
  DISMTHADD1 BCD*2.0 Discount Table Add Months 1
  DISMTHADD2 BCD*2.0 Discount Table Add Months 2
  DISMTHADD3 BCD*2.0 Discount Table Add Months 3
  DISMTHADD4 BCD*2.0 Discount Table Add Months 4
  DISDAYUSE1 BCD*2.0 Discount Table Day of Month 1
  DISDAYUSE2 BCD*2.0 Discount Table Day of Month 2
  DISDAYUSE3 BCD*2.0 Discount Table Day of Month 3
  DISDAYUSE4 BCD*2.0 Discount Table Day of Month 4
  CODEDUETYP Integer Method of Calc for Due Date [1=Days From Invoice Date,2=End of Next Month,3=Day of Next Month,4=Days from Day of Next Month,5=Due Date Table]
  DUEDAYSTR1 BCD*2.0 Due Table Starting Day 1
  DUEDAYSTR2 BCD*2.0 Due Table Starting Day 2
  DUEDAYSTR3 BCD*2.0 Due Table Starting Day 3
  DUEDAYSTR4 BCD*2.0 Due Table Starting Day 4
  DUEDAYEND1 BCD*2.0 Due Table Ending Day 1
  DUEDAYEND2 BCD*2.0 Due Table Ending Day 2
  DUEDAYEND3 BCD*2.0 Due Table Ending Day 3
  DUEDAYEND4 BCD*2.0 Due Table Ending Day 4
  DUEMTHADD1 BCD*2.0 Due Table Add Months 1
  DUEMTHADD2 BCD*2.0 Due Table Add Months 2
  DUEMTHADD3 BCD*2.0 Due Table Add Months 3
  DUEMTHADD4 BCD*2.0 Due Table Add Months 4
  DUEDAYUSE1 BCD*2.0 Due Table Day of Month 1
  DUEDAYUSE2 BCD*2.0 Due Table Day of Month 2
  DUEDAYUSE3 BCD*2.0 Due Table Day of Month 3
  DUEDAYUSE4 BCD*2.0 Due Table Day of Month 4
  CNTENTERED BCD*4.0 Number of Payments
  PCTDUETOT BCD*5.5 Total Percentage Due

## APRTB - Terms Payment Schedule (view AP0011)
Keys (first = PK; D=dups allowed, M=modifiable): TERMSCODE+PAYMNBR
Fields (NAME type description [values]):
  TERMSCODE String*6 Terms Code
  PAYMNBR BCD*3.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  PCTPAYMDUE BCD*5.5 Percentage Due
  DISCTYPE Integer Reserved
  PCTDISC BCD*5.5 Discount Percent
  DISNBRDAYS BCD*2.0 Discount Number of Days
  DISCDAY BCD*2.0 Discount Day of Month
  DUETYPE Integer Reserved
  DUENBRDAYS BCD*2.0 Due Number of Days
  DUEDAY BCD*2.0 Due Day of Month

## APRTG - Retainage Open Documents (view AP0311)
Keys (first = PK; D=dups allowed, M=modifiable): RTGSEQ+IDVEND+IDINVC
Fields (NAME type description [values]):
  RTGSEQ Long Sequence Number
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RTGDATEDUE Date Date Retainage Due
  DATEINVC Date Invoice Date
  TXTTRXTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,10=Prepayment,11=Payment]
  AMTDUE1 BCD*10.3 Current Amount Due
  AMTDUE2 BCD*10.3 Period 1 Amount Due
  AMTDUE3 BCD*10.3 Period 2 Amount Due
  AMTDUE4 BCD*10.3 Period 3 Amount Due
  AMTDUE5 BCD*10.3 Period 4 Amount Due
  TOTAMTBKWD BCD*10.3 Total Backward Aging
  TOTAMTFWD BCD*10.3 Total Forward Aging
  RTGAMTTC BCD*10.3 Amount Retained - Vend. Curr.
  RTGAMTHC BCD*10.3 Amount Retained - Func. Curr.

## APRVL - Revaluation Details (view AP0063)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUTDATE Date Through Date
  CONVDATE Date Rate Date
  CONVRATE BCD*8.7 Exchange Rate
  CURTBLTYPE String*2 Rate Type
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  SWRATEOVRD Integer Rate Overridden [0=No,1=Yes]
  VALUES Long Optional Fields
  ADJFRMDATE Date Earliest Backdated Activity Date

## APRVLLOG - Revaluation History (view AP0181)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE+RVLDATE+CNTSEQENCE
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency Code
  RVLDATE Date Revaluation Date
  CNTSEQENCE Long Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONVDATE Date Rate Date
  CONVRATE BCD*8.7 Exchange Rate
  CURTBLTYPE String*2 Rate Type
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  SWRATEOVRD Integer Rate Overridden [0=No,1=Yes]
  SWRVMETHOD Integer Revaluation Method [1=Realized and Unrealized Gain/Loss Revaluation,2=Recognized Gain/Loss Revaluation]
  ADJFRMDATE Date Earliest Backdated Activity Date
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  DATEPOSTED Date System Date
  APVERSION String*3 A/P Version Created In

## APRVLO - Revaluation Optional Fields (view AP0410)
Keys (first = PK; D=dups allowed, M=modifiable): CURNCYCODE+OPTFIELD; OPTFIELD+CURNCYCODE
Fields (NAME type description [values]):
  CURNCYCODE String*3 Currency Code
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

## APSLD - Selection Criteria Details (view AP0036)
Keys (first = PK; D=dups allowed, M=modifiable): IDSELECT+IDVENDOR
Fields (NAME type description [values]):
  IDSELECT String*6 Selection Criteria
  IDVENDOR String*12 Exclude Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## APSLH - Selection Criteria Header (view AP0035)
Keys (first = PK; D=dups allowed, M=modifiable): IDSELECT
Fields (NAME type description [values]):
  IDSELECT String*6 Selection Criteria
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASMNT Date Date Last Maintained
  SWDOCSPROC Integer Documents to Process [0=Process all documents,1=Process forced documents only]
  SWSELLBY Integer Select Documents by [0=Due Date,1=Discount Date,2=Due Date or Discount Date]
  DATEDUE Date Date Due
  DTEDISCFRM Date From Discount Date
  IDGRPFROM String*6 From Group Code
  IDGRPTHRU String*6 Thru Group Code
  IDVENDFROM String*12 From Vendor Number
  IDVENDTHRU String*12 Thru Vendor Number
  ACCTSETFR String*6 From Account Set
  ACCTSETTHR String*6 Thru Account Set
  SWVENDEXCL Integer Exclude Vendor [0=No,1=Yes]
  IDBANKASGN String*8 Reserved
  CODECURNTC String*3 Vendor Currency Code
  IDBANKPAYM String*8 Payment Bank Code
  CODECURNPY String*3 Bank Currency Code
  AMTBNKLIMT BCD*10.3 Reserved
  AMTMINCHK BCD*10.3 Minimum Payment Amount
  AMTMAXCHK BCD*10.3 Maximum Payment Amount
  SWBANKMTCH Integer Bank Match [0=Vendors with any bank code,1=Vendors with payment bank code only]
  DATECHECK Date Payment Date
  DATEINACT Date Inactive Date
  SWACTV Integer Status [0=Inactive,1=Active]
  CODERATETC String*2 Vendor Rate Type
  CODERATEBC String*2 Bank Rate Type
  EXCHRATETC BCD*8.7 Vendor Exchange Rate
  EXCHRATEBC BCD*8.7 Bank Exchange Rate
  RATEDATETC Date Vendor Rate Date
  RATEDATEBC Date Bank Rate Date
  CSVFILE String*100 CSV Filename
  TEXTDESC String*60 Description
  DTEDISCTHR Date Thru Discount Date
  DTEBATCH Date Batch Date
  RATEOPTC Integer Vendor Rate Operator
  RATEOPBC Integer Bank Rate Operator
  SWRATETC Integer Vendor Rate Overridden
  SWRATEBC Integer Bank Rate Overridden
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  IDSELECTED String*6 Generated Selection Criteria
  VALUES Long Optional Fields
  PMCODEFROM String*12 From Payment Code
  PMCODETHRU String*12 Thru Payment Code
  OPTFIELD String*12 Optional Field
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  VALUEFROM String*60 From Optional Field Value
  VALUETHRU String*60 Thru Optional Field Value

## APSLHO - Selection Criteria Opt. Fields (view AP0411)
Keys (first = PK; D=dups allowed, M=modifiable): IDSELECT+OPTFIELD; OPTFIELD+IDSELECT
Fields (NAME type description [values]):
  IDSELECT String*6 Selection Criteria
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

## APSLVEN - Selected Vendors (view AP0420)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+RECORDNO+IDVEND
Fields (NAME type description [values]):
  SELSEQ Long Sequence Number
  RECORDNO Long Record Number
  IDVEND String*12 Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (vendor),4=Email (contact),5=Email (multiple contacts)]
  SORTVALUE1 String*60 Sort Field Value 1
  SORTVALUE2 String*60 Sort Field Value 2
  SORTVALUE3 String*60 Sort Field Value 3
  SORTVALUE4 String*60 Sort Field Value 4
  SORTTYPE1 Integer Sort Field Type 1
  SORTTYPE2 Integer Sort Field Type 2
  SORTTYPE3 Integer Sort Field Type 3
  SORTTYPE4 Integer Sort Field Type 4

## APTCC - Advance Credits (view AP0170)
Keys (first = PK; D=dups allowed, M=modifiable): BTCHTYPE+CNTBTCH+CNTENTR+CNTLINE
Fields (NAME type description [values]):
  BTCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTENTR BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNBR String*22 Document Number
  TEXTDESC String*60 Description
  TEXTREF String*60 Reference
  AMTACCTC BCD*10.3 Claim Amount
  AMTACCHC BCD*10.3 Func. Claim Amount

## APTCN - Miscellaneous Payments (view AP0032)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHTYPE+CNTBTCH+CNTRMIT+CNTLINE
Fields (NAME type description [values]):
  BATCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTRMIT BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDDISTCODE String*6 Distribution Code
  IDACCT String*45 Account Number
  GLREF String*60 G/L Reference
  GLDESC String*60 G/L Description
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
  TXBSE1TC BCD*10.3 Tax Base 1
  TXBSE2TC BCD*10.3 Tax Base 2
  TXBSE3TC BCD*10.3 Tax Base 3
  TXBSE4TC BCD*10.3 Tax Base 4
  TXBSE5TC BCD*10.3 Tax Base 5
  RATETAX1 BCD*8.5 Tax Rate 1
  RATETAX2 BCD*8.5 Tax Rate 2
  RATETAX3 BCD*8.5 Tax Rate 3
  RATETAX4 BCD*8.5 Tax Rate 4
  RATETAX5 BCD*8.5 Tax Rate 5
  TXAMT1TC BCD*10.3 Tax Amount 1
  TXAMT2TC BCD*10.3 Tax Amount 2
  TXAMT3TC BCD*10.3 Tax Amount 3
  TXAMT4TC BCD*10.3 Tax Amount 4
  TXAMT5TC BCD*10.3 Tax Amount 5
  TXTOTTC BCD*10.3 Tax Total
  AMTDISTTC BCD*10.3 Dist. Amount
  AMTNETTC BCD*10.3 Dist. Amount Net of Taxes
  AMTDISTHC BCD*10.3 Func. Dist. Amount
  AMTNETHC BCD*10.3 Func. Dist. Amount Net of Taxes
  TXALLTC BCD*10.3 Tax Allocated Total
  TXALL1TC BCD*10.3 Tax Allocated Amount 1
  TXALL2TC BCD*10.3 Tax Allocated Amount 2
  TXALL3TC BCD*10.3 Tax Allocated Amount 3
  TXALL4TC BCD*10.3 Tax Allocated Amount 4
  TXALL5TC BCD*10.3 Tax Allocated Amount 5
  TXREC1TC BCD*10.3 Tax Recoverable 1
  TXREC2TC BCD*10.3 Tax Recoverable 2
  TXREC3TC BCD*10.3 Tax Recoverable 3
  TXREC4TC BCD*10.3 Tax Recoverable 4
  TXREC5TC BCD*10.3 Tax Recoverable 5
  TXEXP1TC BCD*10.3 Tax Expensed 1
  TXEXP2TC BCD*10.3 Tax Expensed 2
  TXEXP3TC BCD*10.3 Tax Expensed 3
  TXEXP4TC BCD*10.3 Tax Expensed 4
  TXEXP5TC BCD*10.3 Tax Expensed 5
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Amount
  TXREC1RC BCD*10.3 Tax Reporting Recoverable Amt 1
  TXREC2RC BCD*10.3 Tax Reporting Recoverable Amt 2
  TXREC3RC BCD*10.3 Tax Reporting Recoverable Amt 3
  TXREC4RC BCD*10.3 Tax Reporting Recoverable Amt 4
  TXREC5RC BCD*10.3 Tax Reporting Recoverable Amt 5
  TXEXP1RC BCD*10.3 Tax Reporting Expensed Amount 1
  TXEXP2RC BCD*10.3 Tax Reporting Expensed Amount 2
  TXEXP3RC BCD*10.3 Tax Reporting Expensed Amount 3
  TXEXP4RC BCD*10.3 Tax Reporting Expensed Amount 4
  TXEXP5RC BCD*10.3 Tax Reporting Expensed Amount 5
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  TXALLHC BCD*10.3 Func. Tax Allocated Total
  TXALL1HC BCD*10.3 Func. Tax Allocated Amount 1
  TXALL2HC BCD*10.3 Func. Tax Allocated Amount 2
  TXALL3HC BCD*10.3 Func. Tax Allocated Amount 3
  TXALL4HC BCD*10.3 Func. Tax Allocated Amount 4
  TXALL5HC BCD*10.3 Func. Tax Allocated Amount 5
  TXREC1HC BCD*10.3 Func. Tax Recoverable 1
  TXREC2HC BCD*10.3 Func. Tax Recoverable 2
  TXREC3HC BCD*10.3 Func. Tax Recoverable 3
  TXREC4HC BCD*10.3 Func. Tax Recoverable 4
  TXREC5HC BCD*10.3 Func. Tax Recoverable 5
  TXEXP1HC BCD*10.3 Func. Tax Expensed 1
  TXEXP2HC BCD*10.3 Func. Tax Expensed 2
  TXEXP3HC BCD*10.3 Func. Tax Expensed 3
  TXEXP4HC BCD*10.3 Func. Tax Expensed 4
  TXEXP5HC BCD*10.3 Func. Tax Expensed 5
  TXTOTHC BCD*10.3 Func. Tax Total
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=]
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXTX1TC BCD*10.3 Reverse Charge Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charge Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charge Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charge Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charge Amount 5

## APTCP - Applied Payments (view AP0033)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHTYPE+CNTBTCH+CNTRMIT+CNTLINE; IDVEND+IDINVC+CNTPAYM [D,M]; BATCHTYPE+CNTBTCH+CNTRMIT+IDINVC+CNTPAYM [M]
Fields (NAME type description [values]):
  BATCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTRMIT BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  TRXTYPE Integer Transaction Type [51=Payment - Posted,57=Prepayment - Posted,81=Adjustment - Posted]
  PYMTRESL String*2 Payment Resolution
  AMTPAYM BCD*10.3 Payment Amount
  AMTERNDISC BCD*10.3 Discount Amount Taken
  CNTLASTSEQ BCD*3.0 Next Adj. Seq. No.
  AMTADJTOT BCD*10.3 Adjustments Total
  CNTADJ BCD*5.0 Generated Adjustment Number
  TEXTADJ String*60 Description
  GLREF String*60 Reference
  IDPPD String*22 Generated PP No.
  IDDOCMTCH String*22 PP Matching Doc. No.
  CDAPPLYTO Integer PP Matching Doc. Type [1=(None),2=Document Number,3=PO Number,4=Order Number]
  DATEACTVPP Date Activation Date
  ADJTOTDBTC BCD*10.3 Adj. Debit Amt. - Vend. Curr
  ADJTOTCRTC BCD*10.3 Adj. Credit Amt. - Vend. Curr
  SWJOB Integer Job Related [0=No,1=Yes]
  AMTPAYMTOT BCD*10.3 Job Total Payment Amount
  AMTDISCTOT BCD*10.3 Job Total Discount Amount
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  RTGTOTDBTC BCD*10.3 Rtg. Debit Amt. - Vend. Curr
  RTGTOTCRTC BCD*10.3 Rtg. Credit Amt. - Vend. Curr
  RTGAMT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGTERMS String*6 Retainage Terms Code
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  AMTPAYMHC BCD*10.3 Func. Payment Amount
  AMTDISCHC BCD*10.3 Func. Discount Amount
  AMTADJHC BCD*10.3 Func. Adjustments Total
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  DOCTYPE Integer Document Type
  AMTWHD1TC BCD*10.3 Vend. Tax Withheld Amount 1
  AMTWHD2TC BCD*10.3 Vend. Tax Withheld Amount 2
  AMTWHD3TC BCD*10.3 Vend. Tax Withheld Amount 3
  AMTWHD4TC BCD*10.3 Vend. Tax Withheld Amount 4
  AMTWHD5TC BCD*10.3 Vend. Tax Withheld Amount 5
  AMTWHD1HC BCD*10.3 Func. Tax Withheld Amount 1
  AMTWHD2HC BCD*10.3 Func. Tax Withheld Amount 2
  AMTWHD3HC BCD*10.3 Func. Tax Withheld Amount 3
  AMTWHD4HC BCD*10.3 Func. Tax Withheld Amount 4
  AMTWHD5HC BCD*10.3 Func. Tax Withheld Amount 5
  AMTWHD1DT BCD*10.3 Job Total Tax Withheld Amt 1
  AMTWHD2DT BCD*10.3 Job Total Tax Withheld Amt 2
  AMTWHD3DT BCD*10.3 Job Total Tax Withheld Amt 3
  AMTWHD4DT BCD*10.3 Job Total Tax Withheld Amt 4
  AMTWHD5DT BCD*10.3 Job Total Tax Withheld Amt 5

## APTCR - Payments/Adjustments (view AP0031)
Keys (first = PK; D=dups allowed, M=modifiable): BTCHTYPE+CNTBTCH+CNTENTR
Fields (NAME type description [values]):
  BTCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTENTR BCD*4.0 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*18 Check Number
  IDVEND String*12 Vendor Number
  DATERMIT Date Payment Date/Adjustment Date
  TEXTRMIT String*60 Entry Description
  NAMERMIT String*60 Vendor / Payee Name
  AMTRMIT BCD*10.3 Check Amount in Bank Curr.
  AMTRMITTC BCD*10.3 Check Amount in Vendor Curr.
  RATEEXCHTC BCD*8.7 Vendor Exchange Rate
  SWRATETC Integer Vendor Rate Overridden [0=No,1=Yes]
  CNTPAYMENT BCD*3.0 Number of Payments Entered
  AMTPPAYTC BCD*10.3 Total Prepay Vendor Curr.
  AMTDISCTC BCD*10.3 Total Discount Vendor Curr.
  PAYMCODE String*12 Payment Code
  CODECURN String*3 Vendor Currency Code
  RATETYPEHC String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  SWRATEHC Integer Bank Rate Overridden [0=No,1=Yes]
  RMITTYPE Integer Payment Trans. Type [1=Payment,2=Prepayment,3=Apply Document,4=Misc. Payment,5=Adjustment]
  DOCTYPE Integer Document Type [1=(None),2=Document Number,3=PO Number,4=Order Number,5=Prepayment,7=Credit Note]
  CNTLSTLINE BCD*3.0 Last Line Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  DATERATETC Date Vendor Rate Date
  RATETYPETC String*2 Vendor Rate Type
  AMTADJTCUR BCD*10.3 Total Payment Adj. Vendor Curr.
  DATERATEHC Date Bank Rate Date
  REMREAPLTC BCD*10.3 Total Reapply Remaining Vendor Curr.
  ADJTOTDBHC BCD*10.3 Adj. Debit Amt. Func. Curr.
  AMTRMITHC BCD*10.3 Check Amount Func. Curr.
  DOCNBR String*22 Document Number
  PAYMSTTS Integer Payment Edited [0=No,1=Yes,2=Deleted]
  SWPRNTRMIT Integer Check Print Required [0=No,1=Yes]
  IDRMITTO String*6 Vendor Remit-To Location
  TXTRMITREF String*60 Entry Reference
  ADJTOTCRHC BCD*10.3 Adj. Credit Amt. Func. Curr.
  AMTADJHCUR BCD*10.3 Total Adj. Amt. Func. Curr.
  CNTDEPSSEQ ??? Check Sequence No.
  SWPRINTED Integer Check Printed Status [0=Not printed,1=Printed]
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  CHECKLANG String*3 Payment Language [1=ENG,2=FRA,3=ESN,4=AUS,5=MEX,6=CHN,7=CHT]
  OPERBANK Integer Bank Rate Operator [1=Multiply,2=Divide]
  OPERVEND Integer Vendor Rate Operator [1=Multiply,2=Divide]
  ADJTOTDBTC BCD*10.3 Adj. Debit Amt. Vendor Curr.
  ADJTOTCRTC BCD*10.3 Adj. Credit Amt. Vendor Curr.
  DATEACTVPP Date Prepay Activation Date
  SWJOB Integer Job Related [0=No,1=Yes]
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  IDINVCMTCH String*22 Matching Document Number
  VALUES Long Optional Fields
  SRCEAPPL String*2 Source Application
  IDBANK String*8 Bank Code
  CODECURNBC String*3 Bank Currency Code
  PAYMTYPE Integer Payment Type [0=,1=Cash,2=Check,3=Credit Card,4=Other]
  CASHACCT String*45 Cash Account
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  CODE1099 String*6 1099/CPRS Code
  AMT1099 BCD*10.3 1099/CPRS Amount
  SWTXAMTCTL Integer Calculate Tax Amount Control [0=Enter,1=Calculate,2=Distribute]
  SWTXBSECTL Integer Calculate Tax Base Control [0=Enter,1=Calculate,2=Distribute]
  CODETAXGRP String*12 Tax Group
  TAXVERSION Long Tax State Version
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
  TXBSE1TC BCD*10.3 Tax Base 1
  TXBSE2TC BCD*10.3 Tax Base 2
  TXBSE3TC BCD*10.3 Tax Base 3
  TXBSE4TC BCD*10.3 Tax Base 4
  TXBSE5TC BCD*10.3 Tax Base 5
  TXAMT1TC BCD*10.3 Tax Amount 1
  TXAMT2TC BCD*10.3 Tax Amount 2
  TXAMT3TC BCD*10.3 Tax Amount 3
  TXAMT4TC BCD*10.3 Tax Amount 4
  TXAMT5TC BCD*10.3 Tax Amount 5
  TXTOTTC BCD*10.3 Tax Total
  AMTNETTC BCD*10.3 Dist. Amount Net of Taxes
  TXALLTC BCD*10.3 Tax Allocated Total
  TXEXPTC BCD*10.3 Tax Expensed Total
  TXRECTC BCD*10.3 Tax Recoverable Total
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=Enter,1=Calculate,2=Distribute]
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPRC Integer Tax Reporting Rate Operator [1=Multiply,2=Divide]
  SWRATERC Integer Tax Reporting Rate Override [0=No,1=Yes]
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Total
  TXEXPRC BCD*10.3 Tax Reporting Expensed Total
  TXRECRC BCD*10.3 Tax Reporting Recoverable Total
  AMTPPAYHC BCD*10.3 Total Prepay Func. Curr.
  AMTDISCHC BCD*10.3 Total Discount Func. Curr.
  REMREAPLHC BCD*10.3 Total Reapply Remaining Func. Curr.
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  TXTOTHC BCD*10.3 Func. Tax Total
  AMTNETHC BCD*10.3 Func. Dist. Amount Net of Taxes
  TXALLHC BCD*10.3 Func. Tax Allocated Total
  TXEXPHC BCD*10.3 Func. Tax Expensed Total
  TXRECHC BCD*10.3 Func. Tax Recoverable Total
  APVERSION String*3 A/P Version Created In
  CNTACC Long Number of Advance Credit Claims
  AMTACCTC BCD*10.3 Total Advance Credit Claim
  AMTACCHC BCD*10.3 Func. Total Advance Credit Claim
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  IDACCTSET String*6 Account Set
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  AMTCXBS1TC BCD*10.3 Reverse Charges Base 1
  AMTCXBS2TC BCD*10.3 Reverse Charges Base 2
  AMTCXBS3TC BCD*10.3 Reverse Charges Base 3
  AMTCXBS4TC BCD*10.3 Reverse Charges Base 4
  AMTCXBS5TC BCD*10.3 Reverse Charges Base 5
  AMTCXTX1TC BCD*10.3 Reverse Charges Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charges Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charges Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charges Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charges Amount 5
  AMTGROSDST BCD*10.3 Misc Payment Document Total

## APTCRO - Payment/Adjustment Optional Fields (view AP0406)
Keys (first = PK; D=dups allowed, M=modifiable): BTCHTYPE+CNTBTCH+CNTENTR+OPTFIELD; OPTFIELD+BTCHTYPE+CNTBTCH+CNTENTR
Fields (NAME type description [values]):
  BTCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTENTR BCD*4.0 Entry Number
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

## APTCT - Payment Tax Withholdings (view AP0069)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHTYPE+CNTBTCH+CNTENTR+AUTHORITY
Fields (NAME type description [values]):
  BATCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTENTR BCD*4.0 Entry Number
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMTWHDTC BCD*10.3 Vend Withheld Amount
  AMTWHDHC BCD*10.3 Func Withheld Amount

## APTCU - Adjustment G/L Distributions (view AP0034)
Keys (first = PK; D=dups allowed, M=modifiable): BATCHTYPE+CNTBTCH+CNTRMIT+CNTLINE+CNTSEQ
Fields (NAME type description [values]):
  BATCHTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTRMIT BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQ BCD*3.0 Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CODTRXTYPE Integer Transaction Type
  AMTDIST BCD*10.3 Distribution Amount
  IDDISTCODE String*6 Distribution Code
  IDACCT String*45 Distribution G/L Account
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=]
  AMTDISC BCD*10.3 Discount Taken
  AMTPAYM BCD*10.3 Applied Amount
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  RTGAMT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  AMTDISTHC BCD*10.3 Func. Distribution Amount
  AMTDISCHC BCD*10.3 Func. Discount Amount
  AMTPAYMHC BCD*10.3 Func. Applied Amount
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  TEXTDESC String*60 Description
  TEXTREF String*60 Reference
  DOCLINE BCD*3.0 Apply Line Number
  AMTWHD1TC BCD*10.3 Vend. Tax Withheld Amount 1
  AMTWHD2TC BCD*10.3 Vend. Tax Withheld Amount 2
  AMTWHD3TC BCD*10.3 Vend. Tax Withheld Amount 3
  AMTWHD4TC BCD*10.3 Vend. Tax Withheld Amount 4
  AMTWHD5TC BCD*10.3 Vend. Tax Withheld Amount 5
  AMTWHD1HC BCD*10.3 Func. Tax Withheld Amount 1
  AMTWHD2HC BCD*10.3 Func. Tax Withheld Amount 2
  AMTWHD3HC BCD*10.3 Func. Tax Withheld Amount 3
  AMTWHD4HC BCD*10.3 Func. Tax Withheld Amount 4
  AMTWHD5HC BCD*10.3 Func. Tax Withheld Amount 5

## APTRK - Payment G/L Distributions (view AP0037)
Keys (first = PK; D=dups allowed, M=modifiable): IDBANK+CNTBTCH+CNTENTRY+CNTLINE+CNTSEQ; IDVEND+IDINVC+CNTPAYM+IDRMIT+LONGSERIAL+TRXTYPE+CNTSEQOBP [D,M]
Fields (NAME type description [values]):
  IDBANK String*8 Bank Code
  CNTBTCH BCD*5.0 Batch Number
  CNTENTRY BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQ BCD*3.0 Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDVEND String*12 Vendor Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  IDRMIT String*18 Check Number
  TRXTYPE Integer Document Type
  CNTSEQOBP BCD*3.0 Applied Payment Sequence No.
  DATEBTCH Date Batch Date
  AMTDISTTC BCD*10.3 Vend. Distributed Amount
  AMTDISTHC BCD*10.3 Func. Distributed Amount
  IDDISTCODE String*6 Distribution Code
  IDACCT String*45 G/L Account
  TEXTGLREF String*60 G/L Reference
  TEXTGLDESC String*60 G/L Description
  CNTADJREF BCD*5.0 Adjustment Number
  LONGSERIAL ??? Check Serial Number
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
  TXBSE1TC BCD*10.3 Tax Base 1
  TXBSE2TC BCD*10.3 Tax Base 2
  TXBSE3TC BCD*10.3 Tax Base 3
  TXBSE4TC BCD*10.3 Tax Base 4
  TXBSE5TC BCD*10.3 Tax Base 5
  RATETAX1 BCD*8.5 Tax Rate 1
  RATETAX2 BCD*8.5 Tax Rate 2
  RATETAX3 BCD*8.5 Tax Rate 3
  RATETAX4 BCD*8.5 Tax Rate 4
  RATETAX5 BCD*8.5 Tax Rate 5
  TXAMT1TC BCD*10.3 Tax Amount 1
  TXAMT2TC BCD*10.3 Tax Amount 2
  TXAMT3TC BCD*10.3 Tax Amount 3
  TXAMT4TC BCD*10.3 Tax Amount 4
  TXAMT5TC BCD*10.3 Tax Amount 5
  TXTOTTC BCD*10.3 Tax Total
  AMTNETTC BCD*10.3 Dist. Amount Net of Taxes
  AMTNETHC BCD*10.3 Func. Dist. Amount Net of Taxes
  TXALLTC BCD*10.3 Tax Allocated Total
  TXALL1TC BCD*10.3 Tax Allocated Amount 1
  TXALL2TC BCD*10.3 Tax Allocated Amount 2
  TXALL3TC BCD*10.3 Tax Allocated Amount 3
  TXALL4TC BCD*10.3 Tax Allocated Amount 4
  TXALL5TC BCD*10.3 Tax Allocated Amount 5
  TXREC1TC BCD*10.3 Tax Recoverable 1
  TXREC2TC BCD*10.3 Tax Recoverable 2
  TXREC3TC BCD*10.3 Tax Recoverable 3
  TXREC4TC BCD*10.3 Tax Recoverable 4
  TXREC5TC BCD*10.3 Tax Recoverable 5
  TXEXP1TC BCD*10.3 Tax Expensed 1
  TXEXP2TC BCD*10.3 Tax Expensed 2
  TXEXP3TC BCD*10.3 Tax Expensed 3
  TXEXP4TC BCD*10.3 Tax Expensed 4
  TXEXP5TC BCD*10.3 Tax Expensed 5
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
  TXALLRC BCD*10.3 Tax Reporting Allocated Amount
  TXREC1RC BCD*10.3 Tax Reporting Recoverable Amt 1
  TXREC2RC BCD*10.3 Tax Reporting Recoverable Amt 2
  TXREC3RC BCD*10.3 Tax Reporting Recoverable Amt 3
  TXREC4RC BCD*10.3 Tax Reporting Recoverable Amt 4
  TXREC5RC BCD*10.3 Tax Reporting Recoverable Amt 5
  TXEXP1RC BCD*10.3 Tax Reporting Expensed Amount 1
  TXEXP2RC BCD*10.3 Tax Reporting Expensed Amount 2
  TXEXP3RC BCD*10.3 Tax Reporting Expensed Amount 3
  TXEXP4RC BCD*10.3 Tax Reporting Expensed Amount 4
  TXEXP5RC BCD*10.3 Tax Reporting Expensed Amount 5
  TXBSE1HC BCD*10.3 Func. Tax Base 1
  TXBSE2HC BCD*10.3 Func. Tax Base 2
  TXBSE3HC BCD*10.3 Func. Tax Base 3
  TXBSE4HC BCD*10.3 Func. Tax Base 4
  TXBSE5HC BCD*10.3 Func. Tax Base 5
  TXAMT1HC BCD*10.3 Func. Tax Amount 1
  TXAMT2HC BCD*10.3 Func. Tax Amount 2
  TXAMT3HC BCD*10.3 Func. Tax Amount 3
  TXAMT4HC BCD*10.3 Func. Tax Amount 4
  TXAMT5HC BCD*10.3 Func. Tax Amount 5
  TXALLHC BCD*10.3 Func. Tax Allocated Total
  TXALL1HC BCD*10.3 Func. Tax Allocated Amount 1
  TXALL2HC BCD*10.3 Func. Tax Allocated Amount 2
  TXALL3HC BCD*10.3 Func. Tax Allocated Amount 3
  TXALL4HC BCD*10.3 Func. Tax Allocated Amount 4
  TXALL5HC BCD*10.3 Func. Tax Allocated Amount 5
  TXREC1HC BCD*10.3 Func. Tax Recoverable 1
  TXREC2HC BCD*10.3 Func. Tax Recoverable 2
  TXREC3HC BCD*10.3 Func. Tax Recoverable 3
  TXREC4HC BCD*10.3 Func. Tax Recoverable 4
  TXREC5HC BCD*10.3 Func. Tax Recoverable 5
  TXEXP1HC BCD*10.3 Func. Tax Expensed 1
  TXEXP2HC BCD*10.3 Func. Tax Expensed 2
  TXEXP3HC BCD*10.3 Func. Tax Expensed 3
  TXEXP4HC BCD*10.3 Func. Tax Expensed 4
  TXEXP5HC BCD*10.3 Func. Tax Expensed 5
  TXTOTHC BCD*10.3 Func. Tax Total
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  BILLRATE BCD*10.6 Billing Rate
  BILLCURN String*3 Billing Currency
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5
  AMTCXTX1TC BCD*10.3 Reverse Charge Amount 1
  AMTCXTX2TC BCD*10.3 Reverse Charge Amount 2
  AMTCXTX3TC BCD*10.3 Reverse Charge Amount 3
  AMTCXTX4TC BCD*10.3 Reverse Charge Amount 4
  AMTCXTX5TC BCD*10.3 Reverse Charge Amount 5
  AMTWHT1HC BCD*10.3 Func. Tax Withheld 1
  AMTWHT2HC BCD*10.3 Func. Tax Withheld 2
  AMTWHT3HC BCD*10.3 Func. Tax Withheld 3
  AMTWHT4HC BCD*10.3 Func. Tax Withheld 4
  AMTWHT5HC BCD*10.3 Func. Tax Withheld 5
  AMTWHT1RC BCD*10.3 Tax Reporting Tax Withheld 1
  AMTWHT2RC BCD*10.3 Tax Reporting Tax Withheld 2
  AMTWHT3RC BCD*10.3 Tax Reporting Tax Withheld 3
  AMTWHT4RC BCD*10.3 Tax Reporting Tax Withheld 4
  AMTWHT5RC BCD*10.3 Tax Reporting Tax Withheld 5

## APVCM - Vendor Comments (view AP0014)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+DATEENTR+CNTUNIQ; VENDORID+DATEENTR+REVCOM [M]
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  DATEENTR Date Date Entered
  CNTUNIQ BCD*3.0 Comment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEEXPR Date Expiration Date
  DATEFLUP Date Follow-up Date
  TEXTCMNT1 String*250 Comments (1 of 10)
  TEXTCMNT2 String*250 Comments (2 of 10)
  TEXTCMNT3 String*250 Comments (3 of 10)
  TEXTCMNT4 String*250 Comments (4 of 10)
  TEXTCMNT5 String*250 Comments (5 of 10)
  TEXTCMNT6 String*250 Comments (6 of 10)
  TEXTCMNT7 String*250 Comments (7 of 10)
  TEXTCMNT8 String*250 Comments (8 of 10)
  TEXTCMNT9 String*250 Comments (9 of 10)
  TEXTCMNT10 String*250 Comments (10 of 10)
  REVCOM BCD*3.0 Reverse Count
  CMNTTYPE String*8 Comment Type
  USERID String*8 User ID

## APVCMD - Vendor Comment Details (view AP0135)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+CNTUNIQ+DETAILNUM
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  CNTUNIQ BCD*3.0 Comment Number
  DETAILNUM Integer Comment Detail
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTCMNT String*250 Comment

## APVEN - Vendors (view AP0015)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID; SHORTNAME [D,M]; IDGRP [D,M]
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHORTNAME String*10 Short Name
  IDGRP String*6 Group Code
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  SWHOLD Integer On Hold [0=Not On Hold,1=On Hold]
  DATESTART Date Start Date
  IDPPNT String*12 Participant ID
  VENDNAME String*60 Vendor Name
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  NAMECTAC String*60 Contact Name
  TEXTPHON1 String*30 Phone Number
  TEXTPHON2 String*30 Fax Number
  PRIMRMIT String*6 Primary Remit-To Location
  IDACCTSET String*6 Account Set
  CURNCODE String*3 Currency Code
  RATETYPE String*2 Rate Type
  BANKID String*8 Bank Code
  PRTSEPCHKS Integer Print Separate Checks [0=Do Not Print Separate Checks,1=Print Separate Checks]
  DISTSETID String*6 Distribution Set
  DISTCODE String*6 Distribution Code
  GLACCNT String*45 G/L Account
  TERMSCODE String*6 Terms
  DUPINVCCD Integer Reserved
  DUPAMTCODE Integer Duplicate Amount Code [0=None,1=Warning,2=Error]
  DUPDATECD Integer Duplicate Date Code [0=None,1=Warning,2=Error]
  CODETAXGRP String*12 Tax Group
  TAXCLASS1 Integer Tax Class Code 1
  TAXCLASS2 Integer Tax Class Code 2
  TAXCLASS3 Integer Tax Class Code 3
  TAXCLASS4 Integer Tax Class Code 4
  TAXCLASS5 Integer Tax Class Code 5
  TAXRPTSW Integer Tax Reporting Type [0=None,1=1099,2=CPRS]
  SUBJTOWTHH Integer Reserved
  TAXNBR String*20 1099/CPRS Tax Number
  TAXIDTYPE Integer Tax Type [0=Unknown,1=Social Security Number,2=Employer ID Number,3=GST Registration Number,4=Business Number,5=Social Insurance Number]
  TAXNOTE2SW Integer Reserved
  CLASID String*6 1099/CPRS Code
  AMTCRLIMT BCD*10.3 Credit Limit
  AMTBALDUET BCD*10.3 Balance Due in Vendor Currency
  AMTBALDUEH BCD*10.3 Balance Due in Func. Currency
  AMTPPDINVT BCD*10.3 Total Prepaid Invoice Vend. Curr.
  AMTPPDINVH BCD*10.3 Total Prepaid Invoice Func. Curr.
  DTLASTRVAL Date Date of Last Revaluation
  AMTBALLARV BCD*10.3 Last Revaluation Balance
  CNTOPENINV BCD*4.0 Number of Open Invoices
  CNTPPDINVC BCD*4.0 Number of Prepaid Invoices
  CNTINVPAID BCD*4.0 Number of Paid Invoices
  DAYSTOPAY BCD*4.0 Number of Days to Pay
  DATEINVCHI Date Date of Largest Invoice
  DATEBALHI Date Date of Highest Balance
  DATEINVHIL Date Date of Largest Invoice Last Yr.
  DATEBALHIL Date Date of Highest Balance Last Yr.
  DATELASTAC Date Date of Last Activity
  DATELASTIV Date Date of Last Invoice
  DATELASTCR Date Date of Last Credit Note
  DATELASTDR Date Date of Last Debit Note
  DATELASTPA Date Date of Last Payment
  DATELASTDI Date Date of Last Discount
  DATELSTADJ Date Date of Last Adjustment
  IDINVCHI String*22 Number of Largest Invoice
  IDINVCHILY String*22 Number of Largest Invoice Last Yr.
  AMTINVHIT BCD*10.3 Largest Invoice - Vend. Curr.
  AMTBALHIT BCD*10.3 Highest Balance - Vend. Curr.
  AMTWTHTCUR BCD*10.3 Reserved
  AMTINVHILT BCD*10.3 Larg. Inv. Last Yr. Vend. Curr.
  AMTBALHILT BCD*10.3 High Bal. Last Yr. - Vend. Curr.
  AMTWTHLYTC BCD*10.3 Reserved
  AMTLASTIVT BCD*10.3 Last Invoice Amt - Vend. Curr.
  AMTLASTCRT BCD*10.3 Last Cr. Note Amt. - Vend. Curr.
  AMTLASTDRT BCD*10.3 Last Dr. Note Amt. - Vend. Curr.
  AMTLASTPYT BCD*10.3 Last Payment - Vend. Curr.
  AMTLASTDIT BCD*10.3 Last Discount Amt. - Vend. Curr.
  AMTLASTADT BCD*10.3 Last Adj. Amt. - Vend. Curr.
  AMTINVHIH BCD*10.3 Largest Invoice - Func. Curr.
  AMTBALHIH BCD*10.3 Highest Balance - Func. Curr.
  AMTWTHHCUR BCD*10.3 Reserved
  AMTINVHILH BCD*10.3 Larg. Inv. Last Yr. Func. Curr.
  AMTBALHILH BCD*10.3 High Bal. Last Yr. Func. Curr.
  AMTWTHLYHC BCD*10.3 Reserved
  AMTLASTIVH BCD*10.3 Last Invoice Amt. - Func. Curr.
  AMTLASTCRH BCD*10.3 Last Cr. Note Amt. - Func. Curr.
  AMTLASTDRH BCD*10.3 Last Dr. Note Amt. - Func. Curr.
  AMTLASTPYH BCD*10.3 Last Payment - Func. Curr.
  AMTLASTDIH BCD*10.3 Last Discount Amt. - Func. Curr.
  AMTLASTADH BCD*10.3 Last Adj. Amt. - Func. Curr.
  PAYMCODE String*12 Payment Code
  IDTAXREGI1 String*20 Tax Registration Code 1
  IDTAXREGI2 String*20 Tax Registration Code 2
  IDTAXREGI3 String*20 Tax Registration Code 3
  IDTAXREGI4 String*20 Tax Registration Code 4
  IDTAXREGI5 String*20 Tax Registration Code 5
  SWDISTBY Integer Distribution Type [0=Distribution Set,1=Distribution Code,2=G/L Account,3=None]
  CODECHECK String*3 Check Language [1=ENG,2=FRA,3=ESN,4=AUS,5=MEX,6=CHN,7=CHT]
  AVGDAYSPAY BCD*5.1 Average Days to Pay
  AVGPAYMENT BCD*10.3 Reserved
  AMTINVPDHC BCD*10.3 Total Invoices Paid - Func. Curr.
  AMTINVPDTC BCD*10.3 Total Invoices Paid - Vend. Curr.
  CNTNBRCHKS BCD*4.0 Total Number of Payments
  SWTXINC1 Integer Tax Included 1 [0=No,1=Yes]
  SWTXINC2 Integer Tax Included 2 [0=No,1=Yes]
  SWTXINC3 Integer Tax Included 3 [0=No,1=Yes]
  SWTXINC4 Integer Tax Included 4 [0=No,1=Yes]
  SWTXINC5 Integer Tax Included 5 [0=No,1=Yes]
  EMAIL1 String*50 Contact's E-mail
  EMAIL2 String*50 E-mail
  WEBSITE String*100 Web Site
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (vendor),4=Email (contact),5=Email (multiple contacts)]
  RTGPERCENT BCD*5.5 Percent Retained
  RTGDAYS Integer Days Retained
  RTGTERMS String*6 Retainage Terms Code
  RTGAMTTC BCD*10.3 Amount Retained - Vend. Curr.
  RTGAMTHC BCD*10.3 Amount Retained - Func. Curr.
  VALUES Long Optional Fields
  NEXTCUID Long Next Client Unique ID
  LEGALNAME String*60 Legal Name
  CHK1099AMT Integer Zero 1099 Amount Warning [0=None,1=Warning]
  IDCUST String*12 Customer Number
  BRN String*30 Business Registration Number

## APVENC - Vendor Contacts (view AP0220)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+IDCONTACT; IDCONTACT+VENDORID
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  IDCONTACT String*24 Contact Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## APVENCF - Vendor Contact Forms (view AP0221)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+IDCONTACT+IDAPP+IDFORM; IDCONTACT+IDAPP+IDFORM+VENDORID
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  IDCONTACT String*24 Contact Code
  IDAPP String*2 Application ID
  IDFORM Integer Form ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SELECTED Boolean Selected

## APVENO - Vendor Optional Field Values (view AP0407)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+OPTFIELD; OPTFIELD+VENDORID
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
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

## APVGR - Vendor Groups (view AP0016)
Keys (first = PK; D=dups allowed, M=modifiable): GROUPID
Fields (NAME type description [values]):
  GROUPID String*6 Group Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESCRIPTN String*60 Description
  ACTIVESW Integer Status [0=Inactive,1=Active]
  INACTIVEDT Date Inactive Date
  LSTMNTDATE Date Date Last Maintained
  ACCTSETID String*6 Account Set
  CURNCODE String*3 Currency Code
  RATETYPEID String*2 Rate Type
  BANKID String*8 Bank Code
  PRTSEPCHKS Integer Print Separate Checks [0=No,1=Yes]
  DISTSETID String*6 Distribution Set
  DISTCODE String*6 Distribution Code
  GLACCTID String*45 General Ledger Account No.
  TERMCODE String*6 Terms
  DUPLINVC Integer Reserved
  DUPLAMT Integer Duplicate Amount Code [0=None,1=Warning,2=Error]
  DUPLDATE Integer Duplicate Date Code [0=None,1=Warning,2=Error]
  TAXGRP String*12 Tax Group
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRPTSW Integer Tax Reporting Type [0=None,1=1099,2=CPRS]
  SUBJWTHHSW Integer Reserved
  CLASSID String*6 1099/CPRS Code
  PAYMCODE String*12 Payment Code
  SWDISTBY Integer Distribution Type [0=Distribution Set,1=Distribution Code,2=G/L Account,3=None]
  SWTXINC1 Integer Tax Included 1 [0=No,1=Yes]
  SWTXINC2 Integer Tax Included 2 [0=No,1=Yes]
  SWTXINC3 Integer Tax Included 3 [0=No,1=Yes]
  SWTXINC4 Integer Tax Included 4 [0=No,1=Yes]
  SWTXINC5 Integer Tax Included 5 [0=No,1=Yes]
  VALUES Long Optional Fields

## APVGRO - Vendor Group Optional Field Values (view AP0408)
Keys (first = PK; D=dups allowed, M=modifiable): GROUPID+OPTFIELD; OPTFIELD+GROUPID
Fields (NAME type description [values]):
  GROUPID String*6 Group Code
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

## APVGS - Vendor Group Statistics (view AP0017)
Keys (first = PK; D=dups allowed, M=modifiable): IDGRP+CNTYR+CNTPERD
Fields (NAME type description [values]):
  IDGRP String*6 Group code
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*4.0 Number of Invoices
  CNTCR BCD*4.0 Number of Credit Notes
  CNTDR BCD*4.0 Number of Debit Notes
  CNTPAYM BCD*4.0 Number of Payments
  CNTDISC BCD*4.0 Number of Discounts
  CNTLOST BCD*4.0 Number of Discounts Lost
  CNTADJ BCD*4.0 Number of Adjustments
  CNTINVCPD BCD*4.0 Number of Paid Invoices
  CNTDTOPAY BCD*4.0 Number of Days to Pay
  AMTINVCHC BCD*10.3 Total Invoices Amount
  AMTCRHC BCD*10.3 Total Credit Note Amount
  AMTDRHC BCD*10.3 Total Debit Note Amount
  AMTPAYMHC BCD*10.3 Total Payment Amount
  AMTDISCHC BCD*10.3 Total Discount Amount
  AMTLOSTHC BCD*10.3 Total Discount Amount Lost
  AMTADJHC BCD*10.3 Total Adjustment Amount
  AMTINVPDHC BCD*10.3 Total Amount of Paid Invoices
  AVGDAYSPAY BCD*5.1 Average Days to Pay
  AVGPAYMENT BCD*10.3 Reserved

## APVNR - Remit-To Locations (view AP0018)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDVENDRMIT
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDVENDRMIT String*6 Remit-To Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  DATELASTIV Date Date of Last Activity
  RMITNAME String*60 Description
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  NAMECTAC String*60 Contact Name
  TEXTPHON1 String*30 Phone Number
  TEXTPHON2 String*30 Fax Number
  CODECHCKLG String*3 Check Language [1=ENG,2=FRA,3=ESN,4=AUS,5=MEX,6=CHN,7=CHT]
  EMAIL String*50 E-mail
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  CTACEMAIL String*50 Contact's E-mail
  VALUES Long Optional Fields

## APVNRO - Remit-To Location Optional Field Values (view AP0409)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+IDVENDRMIT+OPTFIELD; OPTFIELD+IDVEND+IDVENDRMIT
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  IDVENDRMIT String*6 Remit-To Location
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

## APVSM - Vendor Statistics (view AP0019)
Keys (first = PK; D=dups allowed, M=modifiable): VENDORID+CNTYR+CNTPERD
Fields (NAME type description [values]):
  VENDORID String*12 Vendor Number
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*3.0 Number of Invoices
  CNTCR BCD*3.0 Number of Credit Notes
  CNTDR BCD*3.0 Number of Debit Notes
  CNTPAYM BCD*3.0 Number of Payments
  CNTDISC BCD*3.0 Number of Discounts
  CNTLOST BCD*3.0 Number of Discounts Lost
  CNTADJ BCD*3.0 Number of Adjustments
  CNTINVCPD BCD*3.0 Number of Paid Invoices
  CNTDTOPAY BCD*3.0 Number of Days to Pay
  AMTINVCHC BCD*10.3 Total Invoices in Func. Currency
  AMTCRHC BCD*10.3 Total Credits in Func. Currency
  AMTDRHC BCD*10.3 Total Debits in Func. Currency
  AMTPAYMHC BCD*10.3 Total Payments in Func. Currency
  AMTDISCHC BCD*10.3 Total Discounts in Func. Curr.
  AMTLOSTHC BCD*10.3 Total Discounts Lost - Func. Curr.
  AMTADJHC BCD*10.3 Total Adjustments in Func. Curr.
  AMTPURHC BCD*10.3 Reserved
  AMTINVPDHC BCD*10.3 Total Invoices Pd. in Func. Curr.
  AMTINVCTC BCD*10.3 Total Invoices in Vend. Curr.
  AMTCRTC BCD*10.3 Total Credits in Vend. Curr.
  AMTDRTC BCD*10.3 Total Debits in Vend. Curr.
  AMTPAYMTC BCD*10.3 Total Payments in Vend. Curr.
  AMTDISCTC BCD*10.3 Total Discounts in Vend. Curr.
  AMTLOSTTC BCD*10.3 Total Discounts Lost in Vend. Curr.
  AMTADJTC BCD*10.3 Total Adjustments in Vend. Curr.
  AMTPURTC BCD*10.3 Reserved
  AMTINPDTC BCD*10.3 Total Invoices Pd. in Vend. Curr.
  AMTBLRVLTC BCD*10.3 Revaluation Bal. in Vend. Curr.
  CNTPUR BCD*3.0 Reserved
  AVGDAYSPAY BCD*5.1 Average Days to Pay
