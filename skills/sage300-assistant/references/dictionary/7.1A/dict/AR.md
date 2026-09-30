# AR module - compiled AOM dictionary

## ARADV - Payment Advices (view AR0460)
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

## ARAGED - Aged Documents (view AR0125)
Keys (first = PK; D=dups allowed, M=modifiable): AGESEQ+RECORDNO+IDCUST+IDINVC+ADJNO+RECTYPE+CNTSEQ
Fields (NAME type description [values]):
  AGESEQ Long Aging Sequence Number
  RECORDNO Long Record Number
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  ADJNO Long Adjustment Sequence Number
  RECTYPE Integer Record Type [0=Document,1=Applied Detail,2=Retainage Document]
  CNTSEQ Long Detail Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*24 Check/Receipt Number
  TRXTYPETXT Integer Document Type
  TRXTYPEID Integer Transaction Type
  DATEINVC Date Document Date
  DATEBUS Date Posting Date
  DATEDUE Date Due Date
  IDMEMOXREF String*22 Reference Document No.
  AMTINVCTC BCD*10.3 Invoice Amount (Source)
  AMTINVCHC BCD*10.3 Invoice Amount (Functional)
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
  AMTBALDUET BCD*10.3 Customer Balance Due (Source)
  AMTBALDUEH BCD*10.3 Customer Balance Due (Functional)
  DOCTYPE Integer Document Type
  SWNONRCVBL Integer Misc. Receipt Flag
  RTGDATEDUE Date Date Retainage Due
  SORTVALUE1 String*60 Sort Field Value 1
  SORTVALUE2 String*60 Sort Field Value 2
  SORTVALUE3 String*60 Sort Field Value 3
  SORTVALUE4 String*60 Sort Field Value 4
  SORTTYPE1 Integer Sort Field Type 1
  SORTTYPE2 Integer Sort Field Type 2
  SORTTYPE3 Integer Sort Field Type 3
  SORTTYPE4 Integer Sort Field Type 4

## ARBTA - Receipt and Adjustment Batches (view AR0041)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPYMTYP+CNTBTCH; CODEPYMTYP+BATCHSTAT+CNTBTCH [M]
Fields (NAME type description [values]):
  CODEPYMTYP String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEBTCH Date Batch Date
  BATCHDESC String*60 Description
  CNTENTER BCD*4.0 Number of Entries
  AMTENTER BCD*10.3 Batch Total
  BATCHTYPE Integer Batch Type [1=Entered,2=Imported,3=Generated,4=External]
  BATCHSTAT Integer Batch Status [1=Open,3=Posted,4=Deleted,5=Post In Progress,7=Ready To Post]
  IDBANK String*8 Bank Code
  CODECURN String*3 Default Bank Currency
  DATERATE Date Bank Rate Date
  CNTLASTITM BCD*4.0 Last Entry Number
  RATETYPE String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  DEPSTNBR BCD*8.0 Deposit Number
  DEPSEQ ??? Deposit Serial Number
  ADJUSTAMT BCD*10.3 Func. Adjustment Amount
  REAPLYAMT BCD*10.3 Func. Applied Doc. Amount
  FUNCAMOUNT BCD*10.3 Func. Batch Total
  POSTSEQNBR BCD*5.0 Posting Sequence No.
  NBRERRORS BCD*5.0 Number of Errors
  DATELSTEDT Date Date Last Edited
  TYPECLASS Integer Batch Type Class [0=Adjustment,1=Write Off,2=Payment]
  SWPRINTED Integer Batch Printed Flag [0=No,1=Yes]
  RATEOP Integer Bank Rate Operator [1=Multiply,2=Divide]
  SWRATE Integer Bank Rate Overridden [0=No,1=Yes]
  SRCEAPPL String*2 Source Application
  CNTREAPPLY BCD*4.0 Number of Reapplies

## ARCCRECD - Create Credit Card Receipts Dtl (view AR0211)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTPAYM
Fields (NAME type description [values]):
  IDCUST String*12 Customer
  IDINVC String*22 Document
  CNTPAYM BCD*3.0 Payment
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  YPPROCCODE String*12 Processing Code
  CUSTNAME String*60 Customer Name
  AMTDIST BCD*10.3 Amount Due
  AMTDISC BCD*10.3 Discount Amount
  AMTPAYM BCD*10.3 Payment Amount
  DATEINVC Date Document Date
  DATEDISC Date Discount Date
  DATEDUE Date Due Date
  CODECURN String*3 Currency
  STATUS Integer Status [0=SPS Transaction Not Started,1=SPS Sales Transaction Pending,2=SPS Sales Transaction Completed]
  SWAPPLY Integer Apply? [0=No,1=Yes,98=Pending]

## ARCMM - Customer Comments (view AR0021)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+DATEENTR+CNTUNIQ; IDCUST+DATEENTR+REVCOM [M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
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

## ARCMMD - Customer Comment Details (view AR0135)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+CNTUNIQ+DETAILNUM
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  CNTUNIQ BCD*3.0 Comment Number
  DETAILNUM Integer Comment Detail
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTCMNT String*250 Comment

## ARCMMTP - Comment Types (view AR0094)
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

## ARCSM - Customer Statistics (view AR0022)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+CNTYR+CNTPERD
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*3.0 Number of Invoices
  CNTCR BCD*3.0 Number of Credits
  CNTDR BCD*3.0 Number of Debits
  CNTPAYM BCD*3.0 Number of Receipts
  CNTDISC BCD*3.0 Number of Discounts
  CNTADJ BCD*3.0 Number of Adjustments
  CNTWROF BCD*3.0 Number of Write-Offs
  CNTINTT BCD*3.0 Number of Interest Charges
  CNTRIF BCD*3.0 Number of Returned Checks
  CNTINVCPD BCD*3.0 Number of Invoices Paid
  CNTDTOPAY BCD*3.0 Number of Days to Pay
  AMTINVCHC BCD*10.3 Total Invoices in Func. Curr.
  AMTCRHC BCD*10.3 Total Credits in Func. Curr.
  AMTDRHC BCD*10.3 Total Debits in Func. Curr.
  AMTPAYMHC BCD*10.3 Total Receipts in Func. Curr.
  AMTDISCHC BCD*10.3 Total Discounts in Func. Curr.
  AMTADJHC BCD*10.3 Total Adjustments in Func. Curr.
  AMTWROFHC BCD*10.3 Total Write-Offs in Func. Curr.
  AMTINTTHC BCD*10.3 Total Interest in Func. Curr.
  AMTRIFHC BCD*10.3 Total Ret'd Checks in Func. Curr.
  AMTINVPDHC BCD*10.3 Total Invoices Pd. in Func. Curr.
  AMTINVCTC BCD*10.3 Total Invoices in Cust. Curr.
  AMTCRTC BCD*10.3 Total Credits in Cust. Curr.
  AMTDRTC BCD*10.3 Total Debits in Cust. Curr.
  AMTPAYMTC BCD*10.3 Total Receipts in Cust. Curr.
  AMTDISCTC BCD*10.3 Total Discounts in Cust. Curr.
  AMTADJTC BCD*10.3 Total Adjustments in Cust. Curr.
  AMTWROFTC BCD*10.3 Total Write-Offs in Cust. Curr.
  AMTINTTTC BCD*10.3 Total Interest in Cust. Curr.
  AMTRIFTC BCD*10.3 Total Ret'd Checks in Cust. Curr.
  AMTINVPDTC BCD*10.3 Total Invoices Pd. in Cust. Curr.
  AMTBARVALT BCD*10.3 Revaluation Bal. in Func. Curr.
  AVGDAYSPAY BCD*5.1 Average Days to Pay
  CNTRF BCD*3.0 Number of Refunds
  AMTRFHC BCD*10.3 Total Refunds in Func. Curr.
  AMTRFTC BCD*10.3 Total Refunds in Cust. Curr.

## ARCSP - Ship-To Locations (view AR0023)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDCUSTSHPT; IDCUSTSHPT+IDCUST
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDCUSTSHPT String*6 Ship-To Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  DATELASTIV Date Reserved
  NAMELOCN String*60 Description
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
  CODETERR String*6 Territory Code
  CODETAXGRP String*12 Tax Group
  IDTAXREGI1 String*20 Tax Registration No. 1
  IDTAXREGI2 String*20 Tax Registration No. 2
  IDTAXREGI3 String*20 Tax Registration No. 3
  IDTAXREGI4 String*20 Tax Registration No. 4
  IDTAXREGI5 String*20 Tax Registration No. 5
  TAXSTTS1 Integer Tax Class Code 1
  TAXSTTS2 Integer Tax Class Code 2
  TAXSTTS3 Integer Tax Class Code 3
  TAXSTTS4 Integer Tax Class Code 4
  TAXSTTS5 Integer Tax Class Code 5
  SHIPVIA String*15 Reserved
  SPCLINST String*60 Special Instructions
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  PRICLIST String*6 Customer Price List
  FOB String*60 Free On Board
  SHPVIACODE String*6 Ship Via Code
  SHPVIADESC String*60 Ship Via Description
  EMAIL String*50 E-mail
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  CTACEMAIL String*50 Contact's E-mail
  VALUES Long Optional Fields
  LOCATION String*6 Inventory Location

## ARCSPO - Ship-To Locations Optional Field Values (view AR0412)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDCUSTSHPT+OPTFIELD; OPTFIELD+IDCUST+IDCUSTSHPT
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDCUSTSHPT String*6 Ship-To Location Code
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

## ARCUS - Customers (view AR0024)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST; TEXTSNAM [D,M]; IDGRP [D,M]; IDNATACCT [D,M]; IDBILLCYCL [D,M]; IDNATACCT+IDACCTSET [D,M]; IDNATACCT+IDBILLCYCL [D,M]; IDNATACCT+IDSVCCHRG [D,M]; IDNATACCT+SWBALFWD [D,M]; IDNATACCT+IDGRP [D,M]; IDACCTSET+IDCUST [M]; CODECURN+IDSVCCHRG+IDCUST [M]; CODETERM+IDCUST [M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTSNAM String*10 Short Name
  IDGRP String*6 Group Code
  IDNATACCT String*12 National Account
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  SWHOLD Integer On Hold [0=No,1=Yes]
  DATESTART Date Start Date
  IDPPNT String*12 Reserved
  CODEDAB String*9 Credit Bureau Number
  CODEDABRTG String*5 Credit Bureau Rating
  DATEDAB Date Credit Bureau Date
  NAMECUST String*60 Customer Name
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
  CODETERR String*6 Territory Code
  IDACCTSET String*6 Account Set
  IDAUTOCASH String*6 Autocash Profile
  IDBILLCYCL String*6 Billing Cycle
  IDSVCCHRG String*6 Interest Profile
  IDDLNQ String*6 Reserved
  CODECURN String*3 Currency Code
  SWPRTSTMT Integer Print Statements [0=No,1=Yes]
  SWPRTDLNQ Integer Reserved
  SWBALFWD Integer Account Type [0=Open Item,1=Balance Forward]
  CODETERM String*6 Terms
  IDRATETYPE String*2 Rate Type
  CODETAXGRP String*12 Tax Group
  IDTAXREGI1 String*20 Tax Registration No. 1
  IDTAXREGI2 String*20 Tax Registration No. 2
  IDTAXREGI3 String*20 Tax Registration No. 3
  IDTAXREGI4 String*20 Tax Registration No. 4
  IDTAXREGI5 String*20 Tax Registration No. 5
  TAXSTTS1 Integer Tax Class Code 1
  TAXSTTS2 Integer Tax Class Code 2
  TAXSTTS3 Integer Tax Class Code 3
  TAXSTTS4 Integer Tax Class Code 4
  TAXSTTS5 Integer Tax Class Code 5
  AMTCRLIMT BCD*10.3 Credit Limit (Cust. Curr.)
  AMTBALDUET BCD*10.3 Balance Due in Cust. Curr.
  AMTBALDUEH BCD*10.3 Balance Due in Func. Curr.
  DATELASTST Date Date of Last Statement
  AMTLASTSTT BCD*10.3 Last Statement Total Cust. Curr.
  AMTLASTSTH BCD*10.3 Reserved
  DTBEGBALFW Date Date of Last Bal. Fwd. Statement
  AMTBALFWDT BCD*10.3 Beginning Bal. on Last Statement
  AMTBALFWDH BCD*10.3 Reserved
  DTLASTRVAL Date Date of Last Revaluation
  AMTBALLARV BCD*10.3 Last Revaluation Balance
  CNTOPENINV BCD*4.0 Number of Open Documents
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
  DATELASTPA Date Date of Last Receipt
  DATELASTDI Date Date of Last Discount
  DATELASTAD Date Date of Last Adjustment
  DATELASTWR Date Date of Last Write-Off
  DATELASTRI Date Date of Last Returned Check
  DATELASTIN Date Date of Last Interest Charge
  DATELASTDQ Date Reserved
  IDINVCHI String*22 Largest Invoice Number
  IDINVCHILY String*22 Largest Invoice Number Last Yr.
  AMTINVHIT BCD*10.3 Largest Invoice - Cust. Curr.
  AMTBALHIT BCD*10.3 Highest Balance - Cust. Curr.
  AMTINVHILT BCD*10.3 Lgst. Inv. Last Yr. Cust. Curr.
  AMTBALHILT BCD*10.3 High Bal. Last Yr. - Cust. Curr.
  AMTLASTIVT BCD*10.3 Last Invoice Amt. - Cust. Curr.
  AMTLASTCRT BCD*10.3 Last Cr. Note Amt. - Cust. Curr.
  AMTLASTDRT BCD*10.3 Last Dr. Note Amt. - Cust. Curr.
  AMTLASTPYT BCD*10.3 Last Receipt - Cust. Curr.
  AMTLASTDIT BCD*10.3 Last Discount Amt. - Cust. Curr.
  AMTLASTADT BCD*10.3 Last Adj. Amt. - Cust. Curr.
  AMTLASTWRT BCD*10.3 Last Write-Off Amt. Cust. Curr.
  AMTLASTRIT BCD*10.3 Last Ret'd. Chk. Amt. Cust. Curr
  AMTLASTINT BCD*10.3 Last Int. Charge - Cust. Curr.
  AMTINVHIH BCD*10.3 Largest Invoice - Func. Curr.
  AMTBALHIH BCD*10.3 Highest Balance - Func. Curr.
  AMTINVHILH BCD*10.3 Lgst. Inv. Last Yr. Func. Curr.
  AMTBALHILH BCD*10.3 High Bal. Last Yr. - Func. Curr.
  AMTLASTIVH BCD*10.3 Last Invoice Amt. - Func. Curr.
  AMTLASTCRH BCD*10.3 Last Cr. Note Amt. - Func. Curr.
  AMTLASTDRH BCD*10.3 Last Dr. Note Amt. - Func. Curr.
  AMTLASTPYH BCD*10.3 Last Receipt - Func. Curr.
  AMTLASTDIH BCD*10.3 Last Discount Amt. - Func. Curr.
  AMTLASTADH BCD*10.3 Last Adj. Amt. - Func. Curr.
  AMTLASTWRH BCD*10.3 Last Write-Off Amt. Func. Curr.
  AMTLASTRIH BCD*10.3 Last Ret'd. Chk. Amt. Func. Curr
  AMTLASTINH BCD*10.3 Last Int. Charge - Func. Curr.
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  PRICLIST String*6 Customer Price List
  CUSTTYPE Integer Customer Discount Type [0=Base,1=A,2=B,3=C,4=D,5=E]
  AMTPDUE BCD*10.3 Amount Past Due
  EMAIL1 String*50 Contact's E-mail
  EMAIL2 String*50 E-mail
  WEBSITE String*100 Web Site
  BILLMETHOD Integer Billing Method
  PAYMCODE String*12 Payment Code
  FOB String*60 Free On Board
  SHPVIACODE String*6 Ship Via Code
  SHPVIADESC String*60 Ship Via Description
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (customer),4=Email (contact),5=Email (multiple contacts)]
  PRIMSHIPTO String*6 Primary Ship-To Location
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  SWPARTSHIP Integer Allow Partial Shipments [0=No,1=Yes]
  SWWEBSHOP Integer Allow Web Store Shopping [0=No,1=Yes]
  RTGPERCENT BCD*5.5 Percent Retained
  RTGDAYS Integer Days Retained
  RTGTERMS String*6 Retainage Terms Code
  RTGAMTTC BCD*10.3 Amount Retained - Cust. Curr.
  RTGAMTHC BCD*10.3 Amount Retained - Func. Curr.
  VALUES Long Optional Fields
  CNTPPDINVC BCD*4.0 Number of Open Prepayments
  AMTPPDINVT BCD*10.3 Amount Prepaid - Cust. Curr.
  AMTPPDINVH BCD*10.3 Amount Prepaid - Func. Curr.
  DATELASTRF Date Date of Last Refund.
  AMTLASTRFT BCD*10.3 Last Refund Amt. - Cust. Curr.
  AMTLASTRFH BCD*10.3 Last Refund Amt. - Func. Curr.
  CODECHECK String*3 Check Language [1=ENG,2=FRA,3=ESN,4=AUS,5=MEX,6=CHN,7=CHT]
  NEXTCUID Long Next Client Unique ID
  LOCATION String*6 Inventory Location
  SWCHKLIMIT Integer Check Credit Limit [0=No,1=Yes]
  SWCHKOVER Integer Check Overdue Amounts [0=No,1=Yes]
  OVERDAYS Integer Days Overdue
  OVERAMT BCD*10.3 Amount Overdue
  SWBACKORDR Integer Allow Backorder Quantities [0=No,1=Yes]
  SWCHKDUPPO Integer Check for Duplicate POs [0=None,1=Warning,2=Error]
  CATEGORY Integer Sage Billing and Payment Customer [0=No,1=Yes]
  BRN String*30 Business Registration Number

## ARCUSC - Customer Contacts (view AR0220)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDCONTACT; IDCONTACT+IDCUST
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDCONTACT String*24 Contact Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ARCUSCF - Customer Contact Forms (view AR0221)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDCONTACT+IDAPP+IDFORM; IDCONTACT+IDAPP+IDFORM+IDCUST
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDCONTACT String*24 Contact Code
  IDAPP String*2 Application ID
  IDFORM Integer Form ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SELECTED Boolean Selected

## ARCUSO - Customer Optional Field Values (view AR0400)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+OPTFIELD; OPTFIELD+IDCUST
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
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

## ARDRO - Days Receivable Outstanding Processor (view AR0138)
Keys (first = PK; D=dups allowed, M=modifiable): SESSDATE
Fields (NAME type description [values]):
  SESSDATE Date Session Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMTINVC BCD*10.3 Net Purchase of the Day
  AMTBAL BCD*10.3 Net Balance of the Day

## ARDUN - Dunning Messages (view AR0008)
Keys (first = PK; D=dups allowed, M=modifiable): CODESTMT
Fields (NAME type description [values]):
  CODESTMT String*8 Dunning Message Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTIVESW Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DTELSTMNTN Date Date Last Maintained
  TEXTSTMT1 String*45 Current Message
  TEXTSTMT2 String*45 Period 1 Message
  TEXTSTMT3 String*45 Period 2 Message
  TEXTSTMT4 String*45 Period 3 Message
  TEXTSTMT5 String*45 Over Period 3 Message

## ARGLREF - G/L Reference Integration (view AR0146)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [100=Invoice,101=Invoice Detail,200=Debit Note,201=Debit Note Detail,300=Credit Note,301=Credit Note Detail,400=Receipt,401=Receipt Detail,402=Receipt Advance Credit Claim,500=Prepayment,600=Unapplied Cash,700=Apply Document,701=Apply Document Detail,800=Miscellaneous Receipt,801=Miscellaneous Receipt Detail,900=Miscellaneous Adjustment,901=Miscellaneous Adjustment Detail,1000=Adjustment,1001=Adjustment Detail,1100=Refund,1101=Refund Detail,1200=Revaluation,1300=Return Customer Check]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description,1=G/L Detail Reference,2=G/L Detail Description,3=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5={ Left Parenthesis,6=} Right Parenthesis,7=# Number Sign,8=Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Check/Receipt Number,11=Comment,12=Contract,13=Customer Name,14=Customer Number,15=Customer Short Name,39=Deposit Number,16=Description,17=Detail Description,18=Detail Reference,19=Distribution Code,20=Document Number,21=Document Type,22=Entry Number,23=Invoice Number,24=Item Number/Distribution Code,25=Order Number,26=Payer,27=Payment Code,28=Payment Type,29=Posting Sequence,30=Project,31=Purchase Order Number,32=Reference,33=Resource,34=Reversal Date,35=Reversal Description,36=Ship-To Location,37=Tax Group,38=Transaction Type]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Check/Receipt Number,11=Comment,12=Contract,13=Customer Name,14=Customer Number,15=Customer Short Name,39=Deposit Number,16=Description,17=Detail Description,18=Detail Reference,19=Distribution Code,20=Document Number,21=Document Type,22=Entry Number,23=Invoice Number,24=Item Number/Distribution Code,25=Order Number,26=Payer,27=Payment Code,28=Payment Type,29=Posting Sequence,30=Project,31=Purchase Order Number,32=Reference,33=Resource,34=Reversal Date,35=Reversal Description,36=Ship-To Location,37=Tax Group,38=Transaction Type]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Check/Receipt Number,11=Comment,12=Contract,13=Customer Name,14=Customer Number,15=Customer Short Name,39=Deposit Number,16=Description,17=Detail Description,18=Detail Reference,19=Distribution Code,20=Document Number,21=Document Type,22=Entry Number,23=Invoice Number,24=Item Number/Distribution Code,25=Order Number,26=Payer,27=Payment Code,28=Payment Type,29=Posting Sequence,30=Project,31=Purchase Order Number,32=Reference,33=Resource,34=Reversal Date,35=Reversal Description,36=Ship-To Location,37=Tax Group,38=Transaction Type]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Check/Receipt Number,11=Comment,12=Contract,13=Customer Name,14=Customer Number,15=Customer Short Name,39=Deposit Number,16=Description,17=Detail Description,18=Detail Reference,19=Distribution Code,20=Document Number,21=Document Type,22=Entry Number,23=Invoice Number,24=Item Number/Distribution Code,25=Order Number,26=Payer,27=Payment Code,28=Payment Type,29=Posting Sequence,30=Project,31=Purchase Order Number,32=Reference,33=Resource,34=Reversal Date,35=Reversal Description,36=Ship-To Location,37=Tax Group,38=Transaction Type]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Adjustment Number,2=Apply By Document Type,3=Apply-To Document Number,4=Bank Code,5=Batch Number,6=Batch Type,7=Category,8=Check Date,9=Check Number,10=Check/Receipt Number,11=Comment,12=Contract,13=Customer Name,14=Customer Number,15=Customer Short Name,39=Deposit Number,16=Description,17=Detail Description,18=Detail Reference,19=Distribution Code,20=Document Number,21=Document Type,22=Entry Number,23=Invoice Number,24=Item Number/Distribution Code,25=Order Number,26=Payer,27=Payment Code,28=Payment Type,29=Posting Sequence,30=Project,31=Purchase Order Number,32=Reference,33=Resource,34=Reversal Date,35=Reversal Description,36=Ship-To Location,37=Tax Group,38=Transaction Type]

## ARGRO - Customer Groups (view AR0025)
Keys (first = PK; D=dups allowed, M=modifiable): IDGRP
Fields (NAME type description [values]):
  IDGRP String*6 Group Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  IDACCTSET String*6 Account Set
  IDAUTOCASH String*6 Autocash Profile
  IDBILLCYCL String*6 Billing Cycle
  IDSVCCHG String*6 Interest Profile
  IDDLNQ String*6 Reserved
  SWBALFWD Integer Account Type [0=Open Item,1=Balance Forward]
  CODETERM String*6 Terms
  RATETYPE String*2 Rate Type
  SWCROVRD Integer Allow Edit of Credit Limit [0=No,1=Yes]
  CDCRLMCUR1 String*3 Credit Limit 1 Currency
  AMCRLMCUR1 BCD*10.3 Credit Limit 1 Amount
  CDCRLMCUR2 String*3 Credit Limit 2 Currency
  AMCRLMCUR2 BCD*10.3 Credit Limit 2 Amount
  CDCRLMCUR3 String*3 Credit Limit 3 Currency
  AMCRLMCUR3 BCD*10.3 Credit Limit 3 Amount
  CDCRLMCUR4 String*3 Credit Limit 4 Currency
  AMCRLMCUR4 BCD*10.3 Credit Limit 4 Amount
  CDCRLMCUR5 String*3 Credit Limit 5 Currency
  AMCRLMCUR5 BCD*10.3 Credit Limit 5 Amount
  VALUES Long Optional Fields
  CODETAXGRP String*12 Tax Group
  TAXSTTS1 Integer Tax Class Code 1
  TAXSTTS2 Integer Tax Class Code 2
  TAXSTTS3 Integer Tax Class Code 3
  TAXSTTS4 Integer Tax Class Code 4
  TAXSTTS5 Integer Tax Class Code 5
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  SWPRTSTMT Integer Print Statements [0=No,1=Yes]
  SWCHKLIMIT Integer Check Credit Limit [0=No,1=Yes]
  SWCHKOVER Integer Check Overdue Amounts [0=No,1=Yes]
  OVERDAYS Integer Days Overdue
  OVERAMT1 BCD*10.3 Amount Overdue 1
  OVERAMT2 BCD*10.3 Amount Overdue 2
  OVERAMT3 BCD*10.3 Amount Overdue 3
  OVERAMT4 BCD*10.3 Amount Overdue 4
  OVERAMT5 BCD*10.3 Amount Overdue 5

## ARGROO - Customer Group Optional Field Values (view AR0410)
Keys (first = PK; D=dups allowed, M=modifiable): IDGRP+OPTFIELD; OPTFIELD+IDGRP
Fields (NAME type description [values]):
  IDGRP String*6 Customer Group
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

## ARGSM - Customer Group Statistics (view AR0026)
Keys (first = PK; D=dups allowed, M=modifiable): IDGRP+CNTYR+CNTPERD
Fields (NAME type description [values]):
  IDGRP String*6 Group Code
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*4.0 Number of Invoices
  CNTCR BCD*4.0 Number of Credit Notes
  CNTDR BCD*4.0 Number of Debit Notes
  CNTPAYM BCD*4.0 Number of Receipts
  CNTDISC BCD*4.0 Number of Discounts
  CNTADJ BCD*4.0 Number of Adjustments
  CNTWROF BCD*4.0 Number of Write-Offs
  CNTINTT BCD*4.0 Number of Interest Charges
  CNTRIF BCD*4.0 Number of Returned Checks
  CNTINVCPD BCD*4.0 Number of Paid Invoices
  CNTDTOPAY BCD*4.0 Number of Days to Pay
  AMTINVCHC BCD*10.3 Total Invoice Amount
  AMTCRHC BCD*10.3 Total Credit Note Amount
  AMTDRHC BCD*10.3 Total Debit Note Amount
  AMTPAYMHC BCD*10.3 Total Receipt Amount
  AMTDISCHC BCD*10.3 Total Discount Amount
  AMTADJHC BCD*10.3 Total Adjustment Amount
  AMTWROFHC BCD*10.3 Total Write-Off Amount
  AMTINTTHC BCD*10.3 Total Interest Amount
  AMTRIFHC BCD*10.3 Total Amount of Returned Checks
  AMTINVPDHC BCD*10.3 Total Amount of Paid Invoices
  AVGDAYSPAY BCD*5.1 Average Days to Pay
  CNTRF BCD*3.0 Number of Refunds
  AMTRFHC BCD*10.3 Total Refund Amount

## ARIBC - Invoice Batches (view AR0031)
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
  BTCHTYPE Integer Batch Type [1=Entered,2=Imported,3=Recurring,4=Generated,5=External,6=Retainage]
  BTCHSTTS Integer Batch Status [1=Open,3=Posted,4=Deleted,5=Post In Progress,7=Ready To Post]
  INVCTYPE Integer Default Invoice Type [1=Item,2=Summary]
  CNTLSTITEM BCD*4.0 Last Entry Number
  POSTSEQNBR BCD*5.0 Posting Sequence No.
  NBRERRORS BCD*5.0 Number of Errors
  DTELSTEDIT Date Date Last Edited
  SWPRINTED Integer Batch Printed Flag [0=No,1=Yes]
  SRCEAPPL String*2 Source Application

## ARIBD - Invoice Details (view AR0033)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDINVC String*22 Reserved
  IDITEM String*16 Item Number
  IDDIST String*6 Distribution Code
  TEXTDESC String*60 Description
  SWMANLITEM Integer Reserved
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  AMTPRIC BCD*10.6 Price
  AMTEXTN BCD*10.3 Extended Amount w/ TIP
  AMTCOGS BCD*10.3 COGS Amount
  AMTTXBL BCD*10.3 Extended Amount w/o TIP
  TOTTAX BCD*10.3 Tax Total
  SWMANLTX Integer Reserved
  BASETAX1 BCD*10.3 Tax Base 1
  BASETAX2 BCD*10.3 Tax Base 2
  BASETAX3 BCD*10.3 Tax Base 3
  BASETAX4 BCD*10.3 Tax Base 4
  BASETAX5 BCD*10.3 Tax Base 5
  TAXSTTS1 Integer Tax Class 1
  TAXSTTS2 Integer Tax Class 2
  TAXSTTS3 Integer Tax Class 3
  TAXSTTS4 Integer Tax Class 4
  TAXSTTS5 Integer Tax Class 5
  SWTAXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTAXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTAXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTAXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTAXINCL5 Integer Tax Included 5 [0=No,1=Yes]
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
  IDACCTREV String*45 Revenue Account
  IDACCTINV String*45 Inventory Account
  IDACCTCOGS String*45 COGS Account
  IDJOBPROJ String*30 Reserved
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLDATE Date Billing Date
  SWIBT Integer Comment Attached [0=No,1=Yes]
  SWDISCABL Integer Discountable [0=No,1=Yes]
  OCNTLINE BCD*3.0 Original Line Identifier
  RTGAMT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Percent Retained
  RTGDAYS Integer Days Retained
  RTGDATEDUE Date Retainage Due Date
  SWRTGDDTOV Integer Retainage Due Date Override [0=No,1=Yes]
  SWRTGAMTOV Integer Retainage Amount Override [0=No,1=Yes]
  VALUES Long Values
  RTGDISTTC BCD*10.3 Retainage Distribution Amount
  RTGCOGSTC BCD*10.3 Retainage COGS Amount
  RTGALTBTC BCD*10.3 Retainage Alternate Base Amount
  RTGINVDIST BCD*10.3 Invoiced Retainage Distribution
  RTGINVCOGS BCD*10.3 Invoiced Retainage COGS
  RTGINVALTB BCD*10.3 Invoiced Retainage Alternate Base
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
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
  DISTNETHC BCD*10.3 Func. Distribution Net of Taxes
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  AMTCOGSHC BCD*10.3 Func. COGS Amount
  AMTCOSTHC BCD*10.6 Func. Cost
  AMTPRICHC BCD*10.6 Func. Price
  AMTEXTNHC BCD*10.3 Func. Extended Amount w/ TIP
  EDN String*30 Export Declaration Number
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5

## ARIBDO - Invoice Detail Optional Fields (view AR0401)
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

## ARIBH - Invoices (view AR0032)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM; IDCUST+IDINVC [D,M]; IDINVC [D,M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  IDSHPT String*6 Ship-To Location Code
  SHIPVIA String*15 Reserved
  SPECINST String*60 Special Instructions
  TEXTTRX Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note]
  IDTRX Integer Transaction Type [11=Invoice - Item Issued,12=Invoice - Summary Entered,13=Invoice - Recurring Charge,14=Invoice - Summary Issued,15=Invoice - Item Entered,21=Debit Note - Item Issued,22=Debit Note - Summary Entered,24=Debit Note - Summary Issued,25=Debit Note - Item Entered,31=Credit Note - Item Issued,32=Credit Note - Summary Entered,34=Credit Note - Summary Issued,35=Credit Note - Item Entered,40=Interest Charge]
  INVCSTTS Integer Reserved
  ORDRNBR String*22 Order Number
  CUSTPO String*22 PO Number
  JOBNBR String*15 Reserved
  INVCDESC String*60 Invoice Description
  SWPRTINVC Integer Invoice Printed [0=No,1=Yes]
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
  SWTERMOVRD Integer Terms Code Overridden [0=No,1=Yes]
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  PCTDISC BCD*5.5 Discount Percentage
  AMTDISCAVL BCD*10.3 Discount Amount Available
  LASTLINE BCD*3.0 Number of Details
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  SWTAXBL Integer Taxable [0=No,1=Yes]
  SWMANTX Integer Do Not Calc. Tax [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXSTTS1 Integer Tax Class 1
  TAXSTTS2 Integer Tax Class 2
  TAXSTTS3 Integer Tax Class 3
  TAXSTTS4 Integer Tax Class 4
  TAXSTTS5 Integer Tax Class 5
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
  AMTTXBL BCD*10.3 Taxable Amount
  AMTNOTTXBL BCD*10.3 Non-Taxable Amount
  AMTTAXTOT BCD*10.3 Tax Total
  AMTINVCTOT BCD*10.3 Document Total Before Tax
  AMTPPD BCD*10.3 Prepayment Amount
  AMTPAYMTOT BCD*3.0 Number of Scheduled Payments
  AMTPYMSCHD BCD*10.3 Total Payment Amount Scheduled
  AMTNETTOT BCD*10.3 Document Total Including Tax
  IDSTDINVC String*16 Recurring Charge Code
  DATEPRCS Date Date Generated
  IDPPD String*22 Prepayment Number
  IDBILL String*6 Recurring Billing Cycle
  SHPTOLOC String*60 Ship-To Location Name
  SHPTOSTE1 String*60 Ship-To Address Line 1
  SHPTOSTE2 String*60 Ship-To Address Line 2
  SHPTOSTE3 String*60 Ship-To Address Line 3
  SHPTOSTE4 String*60 Ship-To Address Line 4
  SHPTOCITY String*30 Ship-To City
  SHPTOSTTE String*30 Ship-To State/Prov.
  SHPTOPOST String*20 Ship-To Zip/Postal Code
  SHPTOCTRY String*30 Ship-To Country
  SHPTOCTAC String*60 Ship-To Contact Name
  SHPTOPHON String*30 Ship-To Phone Number
  SHPTOFAX String*30 Ship-To Fax Number
  DATERATE Date Rate Date
  SWPROCPPD Integer Cust/Natl Over Credit Flag [0=Neither over credit limit,1=Customer over credit limit,2=National over credit limit,3=Both over credit limit]
  CUROPER Integer Rate Operator [1=Multiply,2=Divide]
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  SHPVIACODE String*6 Ship Via Code
  SHPVIADESC String*60 Ship Via Description
  SWJOB Integer Job Related [0=No,1=Yes]
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  EMAIL String*50 Ship-To E-mail
  CTACPHONE String*30 Ship-To Contact's Phone
  CTACFAX String*30 Ship-To Contact's Fax
  CTACEMAIL String*50 Ship-To Contact's E-mail
  AMTDSBWTAX BCD*10.3 Discount Base With Tax
  AMTDSBNTAX BCD*10.3 Discount Base Without Tax
  AMTDSCBASE BCD*10.3 Discount Base
  INVCTYPE Integer Invoice Type [1=Item,2=Summary]
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
  VALUES Long Optional Fields
  SRCEAPPL String*2 Source Application
  ARVERSION String*3 A/R Version Created In
  TAXVERSION Long Tax State Version
  SWTXRTGRPT Integer Report Retainage Tax
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=No,1=Yes]
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
  DISTNETHC BCD*10.3 Func. Distribution w/o Tax Total
  AMTPPDHC BCD*10.3 Func. Prepayment Amount
  AMTDUEHC BCD*10.3 Func. Amount Due
  SWPRTLBL Integer Label Printed [0=No,1=Yes]
  IDSHIPNBR String*22 Shipment Number
  SWOECOST Integer Do O/E Costing and Consolidation [0=No,1=Yes]
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  EDN String*30 Export Declaration Number
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5
  SFPAURL String*100 SF Payments Acceptance URL
  SFPAID String*36 SF Payments Acceptance ID

## ARIBHO - Invoice Optional Fields (view AR0402)
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

## ARIBS - Invoice Payment Schedules (view AR0034)
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

## ARIBT - Invoice Detail Comments (view AR0035)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTLINE String*250 Comments
  SWPRTSTM Integer Print Comment [0=No,1=Yes]

## ARINTCK - Integrity Checker (view AR0057)
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
  CHKCUSDOC Boolean Check Customer Documents
  FIXCUSDOC Boolean Fix Customer Documents
  FRCUSDOC String*12 From Customer
  TOCUSDOC String*12 To Customer
  CHKJOURNAL Boolean Check Posting Journal
  FIXJOURNAL Boolean Fix Posting Journal

## ARITD - Item Pricing (view AR0009)
Keys (first = PK; D=dups allowed, M=modifiable): IDITEM+CODECURN+UNITMEAS; IDITEM+UNITMEAS+CODECURN
Fields (NAME type description [values]):
  IDITEM String*16 Item Number
  CODECURN String*3 Currency Code
  UNITMEAS String*10 Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RATEWGT BCD*10.5 Reserved
  AMTCOST BCD*10.6 Item Cost
  AMTPRICE BCD*10.6 Item Price
  AMTBASETAX BCD*10.3 Tax Base

## ARITH - Items (view AR0010)
Keys (first = PK; D=dups allowed, M=modifiable): IDITEM; CODECMDY [D,M]
Fields (NAME type description [values]):
  IDITEM String*16 Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CODECMDY String*16 Commodity Code
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  IDDIST String*6 Distribution Code
  TEXTCMNT String*250 Comment
  SWDISCABL Integer Discountable [0=No,1=Yes]
  IDACCTREV String*45 Revenue Account
  IDACCTINV String*45 Inventory Account
  IDACCTCOGS String*45 COGS Account
  TARIFFCODE String*20 Tariff Code

## ARITS - Item Statistics (view AR0027)
Keys (first = PK; D=dups allowed, M=modifiable): IDITEM+IDUOM+CNTYR+CNTPERD; CNTYR+CNTPERD [D]
Fields (NAME type description [values]):
  IDITEM String*16 Item Number
  IDUOM String*10 Unit of Measure
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTSALE Date Date of Last Sale
  CNTINVC BCD*4.0 Number of Sales
  CNTCR BCD*4.0 Number of Returns
  SALEDAYS BCD*4.0 Reserved
  AMTINVC BCD*10.3 Total Amount Sold
  AMTCR BCD*10.3 Total Amount Returned
  AMTCOG BCD*10.3 Total Cost of Goods Sold
  AMTGRO BCD*10.3 Total Gross Margin
  AVGDAY BCD*5.1 Reserved
  QTYSOLD BCD*10.5 Quantity Sold

## ARITT - Item Tax Classes (view AR0011)
Keys (first = PK; D=dups allowed, M=modifiable): IDITEM+CODETAX
Fields (NAME type description [values]):
  IDITEM String*16 Item Number
  CODETAX String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXSTTS Integer Tax Class
  SWTAXINCL Integer Tax Included [0=No,1=Yes]

## ARJTR - Job Costing Transactions (view AR0204)
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
  TRANSTYPE Integer Transaction Type [1=Posted,2=Discount,3=Write-Off,4=Apply From,5=Apply To,6=Receipt Reversal,7=Rounding,8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Receipt,20=Retainage Rounding,21=Retainage Exchange Gain/Loss,22=Retainage Unrealized Exchange Gain/Loss,29=Refund,30=Refund Reversal]
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  IDDIST String*6 Distribution Code
  IDGLACCT String*45 G/L Account
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOSTHC BCD*10.6 Functional Cost
  AMTCOSTTC BCD*10.6 Customer Cost
  AMTHC BCD*10.3 Functional Amount
  AMTTC BCD*10.3 Customer Amount
  BILLDATE Date Billing Date
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
  AMTTAX1TC BCD*10.3 Cust. Tax Amount 1
  AMTTAX2TC BCD*10.3 Cust. Tax Amount 2
  AMTTAX3TC BCD*10.3 Cust. Tax Amount 3
  AMTTAX4TC BCD*10.3 Cust. Tax Amount 4
  AMTTAX5TC BCD*10.3 Cust. Tax Amount 5
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGAMTTC BCD*10.3 Cust. Curr. Retainage Amount
  RTGDATEDUE Date Retainage Due Date

## ARMSG - E-mail Messages (view AR0120)
Keys (first = PK; D=dups allowed, M=modifiable): MSGTYPE+MSGID
Fields (NAME type description [values]):
  MSGTYPE Integer Message Type [0=Invoice (E-mail),1=Statement (E-mail),2=Letter (E-mail),6=Receipt (E-mail)]
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

## ARNAT - National Accounts (view AR0028)
Keys (first = PK; D=dups allowed, M=modifiable): IDNATACCT; IDGRP [D,M]
Fields (NAME type description [values]):
  IDNATACCT String*12 National Account Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDGRP String*6 Group Code
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELSTMTN Date Date Last Maintained
  SWHOLD Integer On Hold [0=No,1=Yes]
  CODEDAB String*9 Credit Bureau Number
  DABRTG String*5 Credit Bureau Rating
  DATEDAB Date Credit Bureau Date
  NAMEACCT String*60 National Account Name
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTATE String*30 State/Prov.
  CODEPOST String*20 Zip/Postal Code
  CODECTRY String*30 Country
  NAMECTAC String*60 Contact Name
  TEXTPHON1 String*30 Phone Number
  TEXTPHON2 String*30 Fax Number
  IDACCTSET String*6 Account Set
  IDAUTOCASH String*6 Autocash Profile
  IDBILLCYCL String*6 Billing Cycle
  IDSVCCHRG String*6 Interest Profile
  IDDLNQ String*6 Reserved
  CODECURN String*3 Currency Code
  SWPRTSTMT Integer Print Statements [0=No,1=Yes]
  SWPRTDLNQ Integer Reserved
  SWBALFWD Integer Account Type [0=Open Item,1=Balance Forward]
  IDRATETYPE String*2 Rate Type
  AMTCRLIMIT BCD*10.3 Credit Limit
  AMTBALDUTC BCD*10.3 Balance Due in Cust. Currency
  AMTBALDUHC BCD*10.3 Balance Due in Func. Currency
  DATELSTSTM Date Date of Last Statement
  AMTLSTSTTC BCD*10.3 Last Statement Total Cust. Curr.
  AMTLSTSTHC BCD*10.3 Last Statement Total Func. Curr.
  DATEBALFWD Date Date Balance Forward Begins
  AMTBLFWDTC BCD*10.3 Balance Forward Cust. Curr.
  AMTBLFWDHC BCD*10.3 Balance Forward Func. Curr.
  DATERVAL Date Reserved
  AMTLSTRVAL BCD*10.3 Reserved
  CNTOPENINV BCD*4.0 Number of Open Documents
  CNTINVPAID BCD*4.0 Number of Paid Invoices
  CNTDAYSPAY BCD*4.0 Number of Days to Pay
  DATEINVCHI Date Date of Largest Invoice
  DATEBALHI Date Date of Highest Balance
  DATEINVHIL Date Date of Largest Invoice Last Yr.
  DATEBALHIL Date Date of Highest Bal. Last Yr.
  DATELASTAC Date Date of Last Activity
  DATELASTIN Date Date of Last Invoice
  DATELASTCR Date Date of Last Credit Note
  DATELASTDR Date Date of Last Debit Note
  DATELASTPA Date Date of Last Receipt
  DATELASTDI Date Date of Last Discount
  DATELASTAD Date Date of Last Adjustment
  DATELASTWR Date Date of Last Write-Off
  DATELASTRI Date Date of Last Returned Check
  DATELSTINT Date Date of Last Interest Charge
  DATELASTDL Date Reserved
  IDINVCHIGH String*22 Largest Invoice Number
  IDINVCHILY String*22 Largest Invoice Number Last Yr.
  AMTINVHITC BCD*10.3 Largest Invoice - Cust. Curr.
  AMTBALHITC BCD*10.3 Highest Balance - Cust. Curr.
  AMTINVHLIT BCD*10.3 Lgst. Inv. Last Yr. Cust. Curr.
  AMTBALHILT BCD*10.3 High Bal. Last Yr. - Cust. Curr.
  AMTINVTC BCD*10.3 Last Invoice Amt. - Cust. Curr.
  AMTCRTC BCD*10.3 Last Cr. Note Amt. - Cust. Curr.
  AMTDRTC BCD*10.3 Last Dr. Note Amt. - Cust. Curr.
  AMTPAYMTC BCD*10.3 Last Receipt - Cust. Curr.
  AMTDISCTC BCD*10.3 Last Discount Amt. - Cust. Curr.
  AMTADJTC BCD*10.3 Last Adj. Amt. - Cust. Curr.
  AMTWROFTC BCD*10.3 Last Write-Off Amt. Cust. Curr.
  AMTRIFTC BCD*10.3 Last Ret'd. Chk. Amt. Cust. Curr.
  AMTINTTTC BCD*10.3 Last Int. Charge - Cust. Curr.
  AMTINVHIHC BCD*10.3 Largest Invoice - Func. Curr.
  AMTBALHIHC BCD*10.3 Highest Balance - Func. Curr.
  AMTINVHILH BCD*10.3 Lgst. Inv. Last Yr. Func. Curr.
  AMTBALHILH BCD*10.3 High Bal. Last Yr. - Func. Curr.
  AMTINVHC BCD*10.3 Last Invoice Amt. - Func. Curr.
  AMTCRHC BCD*10.3 Last Cr. Note Amt. - Func. Curr.
  AMTDRHC BCD*10.3 Last Dr. Note Amt. - Func. Curr.
  AMTPAYMHC BCD*10.3 Last Receipt - Func. Curr.
  AMTDISCHC BCD*10.3 Last Discount Amt. - Func. Curr.
  AMTADJHC BCD*10.3 Last Adj. Amt. - Func. Curr.
  AMTWROFHC BCD*10.3 Last Write-Off Amt. Func. Curr.
  AMTRIFHC BCD*10.3 Last Ret'd. Chk. Amt. Func. Curr
  AMTINTTHC BCD*10.3 Last Int. Charge - Func. Curr.
  EMAIL String*50 E-mail
  WEBSITE String*100 Web Site
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  CTACEMAIL String*50 Contact's E-mail
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (national account),4=Email (contact),5=Email (multiple contacts)]
  RTGAMTTC BCD*10.3 Amount Retained - Cust. Curr.
  RTGAMTHC BCD*10.3 Amount Retained - Func. Curr.
  VALUES Long Optional Fields
  DATELASTRF Date Date of Last Refund.
  AMTLASTRFT BCD*10.3 Last Refund Amt. - Cust. Curr.
  AMTLASTRFH BCD*10.3 Last Refund Amt. - Func. Curr.
  SWCHKLIMIT Integer Check Credit Limit [0=No,1=Yes]
  SWCHKOVER Integer Check Overdue Amounts [0=No,1=Yes]
  OVERDAYS Integer Days Overdue
  OVERAMT BCD*10.3 Amount Overdue

## ARNATC - National Account Contacts (view AR0225)
Keys (first = PK; D=dups allowed, M=modifiable): IDNATACCT+IDCONTACT; IDCONTACT+IDNATACCT
Fields (NAME type description [values]):
  IDNATACCT String*12 National Account Number
  IDCONTACT String*24 Contact Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ARNATCF - National Account Contact Forms (view AR0226)
Keys (first = PK; D=dups allowed, M=modifiable): IDNATACCT+IDCONTACT+IDAPP+IDFORM; IDCONTACT+IDAPP+IDFORM+IDNATACCT
Fields (NAME type description [values]):
  IDNATACCT String*12 National Account Number
  IDCONTACT String*24 Contact Code
  IDAPP String*2 Application ID
  IDFORM Integer Form ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SELECTED Boolean Selected

## ARNATO - National Account Optional Field Values (view AR0411)
Keys (first = PK; D=dups allowed, M=modifiable): IDNATACCT+OPTFIELD; OPTFIELD+IDNATACCT
Fields (NAME type description [values]):
  IDNATACCT String*12 National Account
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

## ARNSM - National Account Statistics (view AR0029)
Keys (first = PK; D=dups allowed, M=modifiable): IDNATLACCT+CNTYR+CNTPERD
Fields (NAME type description [values]):
  IDNATLACCT String*12 National Account Number
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*3.0 Number of Invoices
  CNTCR BCD*3.0 Number of Credit Notes
  CNTDR BCD*3.0 Number of Debit Notes
  CNTPAYM BCD*3.0 Number of Receipts
  CNTDISC BCD*3.0 Number of Discounts
  CNTADJ BCD*3.0 Number of Adjustments
  CNTWROF BCD*3.0 Number of Write-Offs
  CNTINTT BCD*3.0 Number of Interest Charges
  CNTRIF BCD*3.0 Number of Returned Checks
  CNTINVCPD BCD*3.0 Number of Invoices Paid
  CNTDYTOPY BCD*3.0 Number of Days to Pay
  AMTINVHCUR BCD*10.3 Total Invoices in Func. Currency
  AMTCRHCUR BCD*10.3 Total Credits in Func. Currency
  AMTDRHCUR BCD*10.3 Total Debits in Func. Currency
  AMTPYMHCUR BCD*10.3 Total Receipts in Func. Currency
  AMTDSCHCUR BCD*10.3 Total Discounts in Func. Curr.
  AMTADJHCUR BCD*10.3 Total Adjustments in Func. Curr.
  AMTWRFHCUR BCD*10.3 Total Write-Offs in Func. Curren
  AMTINTHCUR BCD*10.3 Total Interest in Func. Curr.
  AMTRIFHCUR BCD*10.3 Total Ret'd. Checks Func. Curr.
  AMTINVPD BCD*10.3 Total Invoices Paid Func. Curr.
  AMTINVTCUR BCD*10.3 Total Invoices in Cust. Curr.
  AMTCRTCUR BCD*10.3 Total Credits in Cust. Curr.
  AMTDRTCUR BCD*10.3 Total Debits in Cust. Curr.
  AMTPYMTCUR BCD*10.3 Total Receipts in Cust. Curr.
  AMTDSCTCUR BCD*10.3 Total Discounts in Cust. Curr.
  AMTADJTCUR BCD*10.3 Total Adjustments in Cust. Curr.
  AMTWRFTCUR BCD*10.3 Total Write-Offs in Cust. Curr.
  AMTINTTCUR BCD*10.3 Total Interest in Cust. Curr.
  AMTRIFTCUR BCD*10.3 Total Ret'd. Checks Cust. Curr.
  AMTINVPTHC BCD*10.3 Total Invoices Paid Cust. Curr.
  CNTRF BCD*3.0 Number of Refunds
  AMTRFHC BCD*10.3 Total Refunds in Func. Currency
  AMTRFTC BCD*10.3 Total Refunds in Cust. Currency

## AROBL - Documents (view AR0036)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC; IDINVC; IDORDERNBR+IDCUST+SWPAID+IDINVC [D,M]; IDCUSTPO+IDCUST+SWPAID+IDINVC [D,M]; DATEDUE+IDCUST+IDINVC [D,M]; IDNATACCT+IDCUST+IDINVC [D,M]; SWPAID+IDCUST+IDPREPAID+IDINVC [M]; IDCUST+DATEINVC [D,M]; SWRTGOUT+IDCUST+IDINVC [D,M]; IDSHIPNBR+IDCUST+SWPAID+IDINVC [D,M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*24 Check/Receipt No.
  IDORDERNBR String*22 Order Number
  IDCUSTPO String*22 PO Number
  DATEDUE Date Due Date
  IDNATACCT String*12 National Account Number
  IDCUSTSHPT String*6 Ship-To Location
  TRXTYPEID Integer Transaction Type [1=Unapplied Cash - Posted,11=Invoice - Item Issued,12=Invoice - Summary Entered,13=Invoice - Recurring Charge,14=Invoice - Summary Issued,15=Invoice - Item Entered,21=Debit Note - Item Issued,22=Debit Note - Summary Entered,24=Debit Note - Summary Issued,25=Debit Note - Item Entered,26=Debit Note - Advance Credit Claim,31=Credit Note - Item Issued,32=Credit Note - Summary Entered,34=Credit Note - Summary Issued,35=Credit Note - Item Entered,40=Interest Charge,50=Prepayment - Posted,51=Receipt - Posted,73=Refund - Posted]
  TRXTYPETXT Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Unapplied Cash,10=Prepayment,11=Receipt,19=Refund]
  DATEBTCH Date Batch Date
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  IDGRP String*6 Group Code
  DESCINVC String*60 Document Description
  DATEINVC Date Document Date
  DATEASOF Date As-of Date
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
  AMTINVCTC BCD*10.3 Cust. Currency Invoice Amount
  AMTDUETC BCD*10.3 Cust. Currency Amount Due
  AMTTXBLTC BCD*10.3 Cust. Currency Taxable Amount
  AMTNONTXTC BCD*10.3 Cust. Currency Non-Taxable Amt.
  AMTTAXTC BCD*10.3 Cust. Currency Tax Amount
  AMTDISCTC BCD*10.3 Cust. Currency Discount Amount
  SWPAID Integer Fully Paid [0=No,1=Yes]
  DATELSTACT Date Last Activity Date
  DATELSTSTM Date Last Statement Date
  DATELSTDLQ Date Reserved
  CODEDLQSTS Integer Reserved
  CNTTOTPAYM BCD*3.0 Number of Scheduled Payments
  CNTLSTPAID BCD*3.0 Reserved - Last Payment Number Paid
  CNTLSTPYST BCD*3.0 Payment Number on Last Statement
  AMTREMIT BCD*10.3 Reserved - Receipt Amount
  CNTLASTSEQ BCD*3.0 Last Applied Payment Seq. No.
  SWTAXINPUT Integer Do Not Calc. Tax [0=No,1=Yes]
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
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
  AMTBASE1TC BCD*10.3 Cust. Base Amount 1
  AMTBASE2TC BCD*10.3 Cust. Base Amount 2
  AMTBASE3TC BCD*10.3 Cust. Base Amount 3
  AMTBASE4TC BCD*10.3 Cust. Base Amount 4
  AMTBASE5TC BCD*10.3 Cust. Base Amount 5
  AMTTAX1TC BCD*10.3 Cust. Tax Amount 1
  AMTTAX2TC BCD*10.3 Cust. Tax Amount 2
  AMTTAX3TC BCD*10.3 Cust. Tax Amount 3
  AMTTAX4TC BCD*10.3 Cust. Tax Amount 4
  AMTTAX5TC BCD*10.3 Cust. Tax Amount 5
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDPREPAID String*22 Prepay. Apply-to Doc. No.
  DATEBUS Date Posting Date
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  YPLASTACT String*6 Last Activity Year/Period
  IDBANK String*8 Bank Code
  DEPSTNBR BCD*8.0 Deposit Number
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  SWJOB Integer Job Related [0=No,1=Yes]
  SWRTG Integer Has Retainage [0=No,1=Yes]
  SWRTGOUT Integer Retainage Outstanding [0=No,1=Yes]
  RTGDATEDUE Date Date Retainage Due
  RTGOAMTHC BCD*10.3 Func. Curr. Orig. Rtng. Amt.
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGOAMTTC BCD*10.3 Cust. Curr. Orig. Rtng. Amt.
  RTGAMTTC BCD*10.3 Cust. Curr. Retainage Amount
  RTGTERMS String*6 Retainage Terms Code
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGAPPLYTO String*22 Original Doc. No.
  VALUES Long Optional Fields
  SRCEAPPL String*2 Source Application
  ARVERSION String*3 A/R Version Created In
  INVCTYPE Integer Invoice Type [0=Not Applicable,1=Item,2=Summary]
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
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
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=No,1=Yes]
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
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
  IDSHIPNBR String*22 Shipment Number
  DATEFRSTBK Date Earliest Backdated Activity Date
  DATELSTRVL Date Last Revaluation Date
  ORATE BCD*8.7 Orig. Exchange Rate
  ORATETYPE String*2 Orig. Rate Type
  ORATEDATE Date Orig. Rate Date
  ORATEOP Integer Orig. Rate Operator
  OSWRATE Integer Orig. Rate Override Flag [0=No,1=Yes]
  IDACCTSET String*6 Account Set
  DATEPAID Date Date Paid
  SWNONRCVBL Integer Misc. Receipt Flag
  CODETERR String*6 Territoty Code
  OAMTWHT1TC BCD*10.3 Orig Est Tax Withheld Amount 1
  OAMTWHT2TC BCD*10.3 Orig Est Tax Withheld Amount 2
  OAMTWHT3TC BCD*10.3 Orig Est Tax Withheld Amount 3
  OAMTWHT4TC BCD*10.3 Orig Est Tax Withheld Amount 4
  OAMTWHT5TC BCD*10.3 Orig Est Tax Withheld Amount 5

## AROBLJ - Open Document Details (view AR0200)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTLINE
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
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
  AMTINVCTC BCD*10.3 Cust. Currency Invoice Amount
  AMTDUETC BCD*10.3 Cust. Currency Amount Due
  AMTINVCHC BCD*10.3 Func. Currency Invoice Amount
  AMTDUEHC BCD*10.3 Func. Currency Amount Due
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  SWDISCABL Integer Discountable [0=No,1=Yes]
  RTGDATEDUE Date Date Retainage Due
  RTGOAMTHC BCD*10.3 Func. Curr. Orig. Rtng. Amt.
  RTGAMTHC BCD*10.3 Func. Curr. Retainage Amount
  RTGOAMTTC BCD*10.3 Cust. Curr. Orig. Rtng. Amt.
  RTGAMTTC BCD*10.3 Cust. Curr. Retainage Amount
  VALUES Long Optional Fields
  RTGDISTTC BCD*10.3 Retainage Distribution Amount
  RTGCOGSTC BCD*10.3 Retainage COGS Amount
  RTGALTBTC BCD*10.3 Retainage Alternate Base Amount
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
  TXBSERT1TC BCD*10.3 Cust. Retainage Tax Base 1
  TXBSERT2TC BCD*10.3 Cust. Retainage Tax Base 2
  TXBSERT3TC BCD*10.3 Cust. Retainage Tax Base 3
  TXBSERT4TC BCD*10.3 Cust. Retainage Tax Base 4
  TXBSERT5TC BCD*10.3 Cust. Retainage Tax Base 5
  TXAMTRT1TC BCD*10.3 Cust. Retainage Tax Amount 1
  TXAMTRT2TC BCD*10.3 Cust. Retainage Tax Amount 2
  TXAMTRT3TC BCD*10.3 Cust. Retainage Tax Amount 3
  TXAMTRT4TC BCD*10.3 Cust. Retainage Tax Amount 4
  TXAMTRT5TC BCD*10.3 Cust. Retainage Tax Amount 5
  TXAMTRT1HC BCD*10.3 Func. Retainage Tax Amount 1
  TXAMTRT2HC BCD*10.3 Func. Retainage Tax Amount 2
  TXAMTRT3HC BCD*10.3 Func. Retainage Tax Amount 3
  TXAMTRT4HC BCD*10.3 Func. Retainage Tax Amount 4
  TXAMTRT5HC BCD*10.3 Func. Retainage Tax Amount 5
  CNTLASTSEQ Long Last Applied Payment Seq. No.
  OAMTWHT1TC BCD*10.3 Orig Est Tax Withheld Amount 1
  OAMTWHT2TC BCD*10.3 Orig Est Tax Withheld Amount 2
  OAMTWHT3TC BCD*10.3 Orig Est Tax Withheld Amount 3
  OAMTWHT4TC BCD*10.3 Orig Est Tax Withheld Amount 4
  OAMTWHT5TC BCD*10.3 Orig Est Tax Withheld Amount 5

## AROBLJO - Open Doc. Detail Optional Fields (view AR0515)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTLINE+OPTFIELD; OPTFIELD+IDCUST+IDINVC+CNTLINE
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
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

## AROBLJP - Document Detail Payments (view AR0088)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTLINE+CNTSEQENCE; IDBANK+IDCUSTRMIT+IDRMIT+DATERMIT [D,M]; IDCUST+PYMCUID+IDINVC+CNTLINE [D,M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQENCE Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNBR Long Transaction Number
  DATEBUS Date Posting Date
  TRANSTYPE Integer Document Type [5=Unapplied Cash,6=Debit Note Applied To,7=Applied Debit Note,8=Credit Note Applied To,9=Applied Credit Note,10=Prepayment,11=Receipt,12=Discount,14=Adjustment,16=Exchange Gain/Loss,17=Rounding,19=Refund,18=Retainage,20=Tax Withheld]
  TRXTYPE Integer Transaction Type [3=Unapplied Cash - Applied,4=Unapplied Cash - Reversed,41=Debit Note Applied To,42=Applied Debit Note,43=Credit Note Applied To,44=Applied Credit Note,51=Receipt - Posted,52=Receipt - Applied,53=Receipt - Reversed,58=Prepayment - Applied,59=Prepayment - Reversed,61=Discount - Posted,63=Discount - Reversed,65=Exchange Gain/Loss - Posted,67=Exchange Gain/Loss - Reversed,91=Rounding - Posted,93=Rounding - Reversed,69=Unrealized Exchange Gain/Loss,80=Write-Off - Posted,81=Adjustment - Posted,83=Adjustment - Reversed,73=Refund - Posted,75=Refund - Reversed,100=Retainage - Invoiced,101=Retainage - Adjusted,102=Retainage - Revalued,103=Retainage - Exchange Gain/Loss,104=Retainage - Rounding,85=Receipt - Invoice Reversed,105=Tax Withheld - Posted,106=Tax Withheld - Reversed]
  TYPEBTCH String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  DATEBTCH Date Batch Date
  AMTPAYMHC BCD*10.3 Func. Receipt Amount
  AMTPAYMTC BCD*10.3 Cust. Receipt Amount
  TXTOTRTHC BCD*10.3 Func. Retainage Tax Invoiced
  TXTOTRTTC BCD*10.3 Cust. Retainage Tax Invoiced
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEEXCHHC BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  IDBANK String*8 Bank Code
  IDCUSTRMIT String*12 Remitting Customer Number
  IDRMIT String*24 Check/Receipt No.
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
  DATERMIT Date Receipt Date
  PYMCUID Long Payment CUID
  IDMEMOXREF String*22 Reference Document Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  CODETAX String*12 Tax Authority

## AROBLO - Open Document Optional Fields (view AR0403)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+OPTFIELD; OPTFIELD+IDCUST+IDINVC
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
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

## AROBP - Document Payments (view AR0038)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTPAYMNBR+IDRMIT+DATEBUS+TRANSTYPE+CNTSEQNCE; IDBANK+CNTBTCH+CNTITEM+IDCUST+IDINVC+CNTPAYMNBR [D,M]; IDINVC+CNTPAYMNBR [D,M]; IDCUST+IDMEMOXREF [D,M]; IDBANK+IDCUSTRMIT+IDRMIT+DATERMIT [D,M]; IDCUST+IDINVC+CNTPAYMNBR+DATEBUS [D,M]; IDCUST+PYMCUID+IDINVC+CNTPAYMNBR [D,M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTPAYMNBR BCD*3.0 Payment Number
  IDRMIT String*24 Check/Receipt No.
  DATEBUS Date Posting Date
  TRANSTYPE Integer Document Type [5=Unapplied Cash,6=Debit Note Applied To,7=Applied Debit Note,8=Credit Note Applied To,9=Applied Credit Note,10=Prepayment,11=Receipt,12=Discount,14=Adjustment,16=Exchange Gain/Loss,17=Rounding,19=Refund,18=Retainage,20=Tax Withheld]
  CNTSEQNCE BCD*3.0 Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEPSTNBR BCD*8.0 Deposit Number
  CNTBTCH BCD*5.0 Batch Number
  DATEBTCH Date Batch Date
  AMTPAYMHC BCD*10.3 Func. Receipt Amount
  AMTPAYMTC BCD*10.3 Cust. Receipt Amount
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEEXCHHC BCD*8.7 Exchange Rate
  SWOVRDRATE Integer Rate Overridden [0=No,1=Yes]
  IDBANK String*8 Bank Code
  TRXTYPE Integer Transaction Type [3=Unapplied Cash - Applied,4=Unapplied Cash - Reversed,41=Debit Note Applied To,42=Applied Debit Note,43=Credit Note Applied To,44=Applied Credit Note,51=Receipt - Posted,52=Receipt - Applied,53=Receipt - Reversed,58=Prepayment - Applied,59=Prepayment - Reversed,61=Discount - Posted,63=Discount - Reversed,65=Exchange Gain/Loss - Posted,67=Exchange Gain/Loss - Reversed,91=Rounding - Posted,93=Rounding - Reversed,69=Unrealized Exchange Gain/Loss,80=Write-Off - Posted,81=Adjustment - Posted,83=Adjustment - Reversed,73=Refund - Posted,75=Refund - Reversed,100=Retainage - Invoiced,101=Retainage - Adjusted,102=Retainage - Revalued,103=Retainage - Exchange Gain/Loss,104=Retainage - Rounding,85=Receipt - Invoice Reversed,105=Tax Withheld - Posted,106=Tax Withheld - Reversed]
  IDMEMOXREF String*22 Reference Document No.
  SWINVCDEL Integer Delete Invoice Switch
  DATELSTSTM Date Last Statement Date
  IDPREPAID String*22 Prepay. Apply-to Doc. No.
  IDCUSTRMIT String*12 Remitting Customer No.
  DATERMIT Date Receipt Date
  CNTITEM BCD*4.0 Entry Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  STMTSEQ Long Statement Run No.
  PYMCUID Long Payment CUID
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
  CODETAX String*12 Tax Authority

## AROBS - Document Sched. Payments (view AR0037)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTPAYM; IDINVC+CNTPAYM [D,M]; IDCUST+IDORDRNBR+IDINVC+CNTPAYM [D,M]; IDCUST+IDCUSTPO+IDINVC+CNTPAYM [D,M]; IDCUST+DATEDUE+IDINVC+CNTPAYM [D,M]; IDNATACCT+IDCUST+IDINVC+CNTPAYM [D,M]; IDCUST+AMTPYMRMTC+DATEDUE+IDINVC+CNTPAYM [D,M]; SWPAID+IDINVC+CNTPAYM [D,M]; IDCUST+DATEINVC+IDINVC+CNTPAYM [D,M]; SWPAID+IDPREPAID [D,M]; SWPAID+IDCUST+IDINVC+CNTPAYM [D,M]; SWPAID+IDNATACCT+IDINVC+CNTPAYM [D,M]; IDCUST+IDSHIPNBR+IDINVC+CNTPAYM [D,M]; IDCUST+RTGAPPLYTO+IDINVC+CNTPAYM [D,M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*24 Receipt Number
  DATEDUE Date Due Date
  DATEDISC Date Discount Date
  SWPAID Integer Fully Paid Switch [0=No,1=Yes]
  DLNQSTTS Integer Reserved
  AMTDUEHC BCD*10.3 Original Amount (Func.)
  AMTDISCHC BCD*10.3 Original Discount (Func.)
  AMTDCSRMHC BCD*10.3 Remaining Discount (Func.)
  AMTPYMRMHC BCD*10.3 Remaining Amount (Func.)
  AMTDUETC BCD*10.3 Original Amount
  AMTDISCTC BCD*10.3 Original Discount
  AMTDSCRMTC BCD*10.3 Remaining Discount
  AMTPYMRMTC BCD*10.3 Remaining Amount
  IDORDRNBR String*22 Order Number
  IDCUSTPO String*22 PO Number
  IDNATACCT String*12 National Account Number
  IDGRP String*6 Group Code
  IDPREPAID String*22 Prepay. Apply-to Doc. No.
  IDTRXTYPE Integer Transaction Type [1=Unapplied Cash - Posted,11=Invoice - Item Issued,12=Invoice - Summary Entered,13=Invoice - Recurring Charge,14=Invoice - Summary Issued,15=Invoice - Item Entered,21=Debit Note - Item Issued,22=Debit Note - Summary Entered,24=Debit Note - Summary Issued,25=Debit Note - Item Entered,26=Debit Note - Advance Credit Claim,31=Credit Note - Item Issued,32=Credit Note - Summary Entered,34=Credit Note - Summary Issued,35=Credit Note - Item Entered,40=Interest Charge,50=Prepayment - Posted,51=Receipt - Posted,73=Refund - Posted]
  TXTTRXTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Unapplied Cash,10=Prepayment,11=Receipt,19=Refund]
  DATEINVC Date Document Date
  DAYSTOPAY Integer Number of Days to Pay
  SWJOB Integer Job Related [0=No,1=Yes]
  IDSHIPNBR String*22 Shipment Number
  RTGAPPLYTO String*22 Original Doc. No.

## AROFD - Optional Fields (view AR0500)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Customers, National Accounts, and Customer Groups,1=Ship-To Locations,2=Invoices,3=Invoice Details,4=Receipts,5=Adjustments,6=Revaluation,7=Refunds]
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
  SWCONTROL Integer Receivables Control [99=Not Applicable]
  SWRTG Integer Retainage [99=Not Applicable]
  SWDISCOUNT Integer Receipt Discount [99=Not Applicable]
  SWTAXLIAB Integer Tax Liability [99=Not Applicable]
  SWREXCHG Integer Exchange Gain [99=Not Applicable]
  SWREXCHL Integer Exchange Loss [99=Not Applicable]
  SWUREXCHG Integer Unrealized Exchange Gain [99=Not Applicable]
  SWUREXCHL Integer Unrealized Exchange Loss [99=Not Applicable]
  SWROUND Integer Rounding [99=Not Applicable]
  SWREVENUE Integer Revenue [99=Not Applicable]
  SWPREPAY Integer Prepayment [99=Not Applicable]
  SWMISCRCPT Integer Miscellaneous Receipt [99=Not Applicable]
  SWBANK Integer Bank [99=Not Applicable]
  SWADJ Integer Adjustment [99=Not Applicable]
  SWIC Integer Inventory Control [99=Not Applicable]
  SWCOGS Integer Cost of Goods Sold [99=Not Applicable]
  SWPM Integer Billings / Costs [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]
  SWLABOUR Integer Labor [99=Not Applicable]
  SWOHEAD Integer Overhead [99=Not Applicable]

## AROFH - Optional Field Locations (view AR0501)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Customers, National Accounts, and Customer Groups,1=Ship-To Locations,2=Invoices,3=Invoice Details,4=Receipts,5=Adjustments,6=Revaluation,7=Refunds]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## AROFPD - Function Parameters Detail (view AR0503)
Keys (first = PK; D=dups allowed, M=modifiable): FUNCTION+OPTFIELD; OPTFIELD+FUNCTION
Fields (NAME type description [values]):
  FUNCTION Integer Function [10=Create Interest Batch Header,11=Create Interest Batch Detail,20=Create Write-Off Batch Header]
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

## AROFPH - Function Parameters Header (view AR0504)
Keys (first = PK; D=dups allowed, M=modifiable): FUNCTION
Fields (NAME type description [values]):
  FUNCTION Integer Function [10=Create Interest Batch Header,11=Create Interest Batch Detail,20=Create Write-Off Batch Header]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Optional Fields

## ARPJD - Posting Journal Details (view AR0407)
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
  IDCUST String*12 Customer No.
  IDINVC String*22 Document No.
  CNTPAYM BCD*3.0 Payment No.
  TRANSTYPE Integer Document Type
  IDTRANS Integer Transaction Type
  DATEBUS Date Posting Date
  DATEINVC Date Document Date
  DATEDISC Date Discount Date
  DATEDUE Date Due Date
  IDBANK String*8 Bank Code
  IDRMIT String*24 Check/Receipt No.
  CNTLINE BCD*3.0 Line No.
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDACCT String*45 G/L Account
  ACCTTYPE Integer Account Type [1=Accounts Receivable,2=Offset,3=Inventory,4=Cost of Goods Sold,6=Tax Summary,7=Bank,11=Revenue,12=Tax Withheld]
  SRCETYPE String*2 G/L Source Type
  GLREF String*60 G/L Reference
  GLDESC String*60 G/L Description
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEEXCHHC BCD*8.7 Exchange Rate
  TYPEDETL Integer COGS/INVENTORY Flag
  IDITEM String*16 Item Number
  IDDIST String*6 Distribution Code
  ITEMDESC String*60 Item Description
  QTYINVC BCD*10.5 Invoice Quantity
  AMTCOSTHC BCD*10.6 Cost Amount (Functional)
  AMTCOSTTC BCD*10.6 Cost Amount (Source)
  AMTEXTNDHC BCD*10.3 Extended Amount (Functional)
  AMTEXTNDTC BCD*10.3 Extended Amount (Source)
  BASETAXHC BCD*10.3 Tax Base (Functional)
  BASETAXTC BCD*10.3 Tax Base (Source)
  AMTTAXHC BCD*10.3 Tax Amount (Functional)
  AMTTAXTC BCD*10.3 Tax Amount (Source)
  UNITMEAS String*10 Unit of Measure
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
  LONGSERIAL ??? Serial Number
  PAYMCODE String*12 Payment Code
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,5=SPS Credit Card,4=Other]
  GLCOMMENT String*250 G/L Comment
  RATEDOC BCD*8.7 Document's Exchange Rate
  EDN String*30 Export Declaration Number

## ARPJDO - Posting Journal Detail Optional Fields (view AR0413)
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

## ARPJH - Posting Journal Entries (view AR0408)
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
  IDCUST String*12 Customer No.
  IDINVC String*22 Document No.
  CNTPAYM BCD*3.0 Payment No.
  TRANSTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Unapplied Cash,10=Prepayment,11=Receipt,14=Adjustment,16=Exchange Gain/Loss,19=Refund]
  TRXTYPE Integer Transaction Type [11=Invoice - Item Issued,12=Invoice - Summary Entered,13=Invoice - Recurring Charge,14=Invoice - Summary Issued,15=Invoice - Item Entered,21=Debit Note - Item Issued,22=Debit Note - Summary Entered,24=Debit Note - Summary Issued,25=Debit Note - Item Entered,31=Credit Note - Item Issued,32=Credit Note - Summary Entered,34=Credit Note - Summary Issued,35=Credit Note - Item Entered,40=Interest Charge,81=Adjustment - Posted,80=Write-Off - Posted,2=Unapplied Cash - Posted,57=Prepayment - Posted,3=Unapplied Cash - Applied,58=Prepayment - Applied,43=Credit Note Applied To,44=Applied Credit Note,51=Receipt - Posted,52=Receipt - Applied,53=Receipt - Reversed,69=Unrealized Exchange Gain/Loss,73=Refund - Posted,75=Refund - Reversed,65=Exchange Gain/Loss - Posted,85=Receipt - Invoice Reversed]
  IDGRP String*6 Group Code
  IDACCTSET String*6 Account Set
  CODETAXGRP String*12 Tax Group
  CODETERM String*6 Terms Code
  IDBILLCYC String*6 Billing Cycle
  IDCUSTSHP String*6 Ship-To Location Code
  DATEINVC Date Document Date
  DATEDISC Date Discount Date
  DATEDUE Date Due Date
  DATEBTCH Date Batch Date
  PCTDISC BCD*5.5 Discount Percentage
  SWNONRCVBL Integer Misc. Receipt Flag
  GLBATCH String*6 G/L Batch No.
  GLENTRY String*5 G/L Entry No.
  CNTADJNBR BCD*5.0 Adjustment Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDINVCAPPL String*22 Apply-To Doc. No.
  DESC String*60 Description
  IDBANK String*8 Bank Code
  IDRMIT String*24 Check/Receipt No.
  DATEDEPST Date Deposit Date
  DEPSTNBR BCD*8.0 Deposit Number
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
  NAMERMIT String*60 Name on Check
  AMTTC BCD*10.3 Customer Amount
  AMTHC BCD*10.3 Functional Amount
  AMTBC BCD*10.3 Bank Amount
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
  PAYMCODE String*12 Payment Code
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,5=SPS Credit Card,4=Other]
  TEXTREF String*60 Reference
  DATEBUS Date Posting Date
  REVINVC Integer Reverse Invoice
  ENTEREDBY String*8 Entered By
  EDN String*30 Export Declaration Number

## ARPJHO - Posting Journal Entry Optional Fields (view AR0414)
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

## ARPJS - Posting Journals (view AR0409)
Keys (first = PK; D=dups allowed, M=modifiable): TYPEBTCH+POSTSEQNCE
Fields (NAME type description [values]):
  TYPEBTCH String*2 Batch Type
  POSTSEQNCE BCD*5.0 Posting Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEPOSTED Date System Date
  DATEBUS Date Date Posted in A/R
  SWPRINTED Integer Printed? [0=No,1=Yes]
  SWPOSTGL Integer Posted to G/L? [0=No,1=Yes]
  DATEPOSTGL Date Date Posted to G/L
  SWGLCONSL Integer Consolidated for G/L?
  PGMVER String*3 Program Version

## ARPOOP - Create Open Document List (view AR0061)
Keys (first = PK; D=dups allowed, M=modifiable): PAYMTYPE+CNTBTCH+CNTITEM+CNTKEY
Fields (NAME type description [values]):
  PAYMTYPE String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTKEY BCD*3.0 Count key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PAYMSCHD BCD*3.0 Count payments scheduled
  PROTYPE Integer Process Type [1=Select,2=Autocash]
  SHOWTYPE Integer Show Type [1=All,2=Invoice,3=Debit Note,4=Credit Note]
  ORDERBY Integer Order By [1=Document Number,2=PO Number,3=Due Date,4=Order Number,7=Shipment Number,5=Document Date,6=Current Balance,8=Original Doc. No.]
  IDCUST String*12 ID Customer
  IDINVC String*22 ID Invc
  IDRMIT String*24 Receipt ID
  CUSTPO String*22 PO Number
  ORDRNBR String*22 Order Number
  IDSHIPNBR String*22 Shipment Number
  TRXTYPE Integer Text transaction type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Unapplied Cash,10=Prepayment,11=Receipt]
  DATEDUE Date Due Date
  DATEDISC Date Discount date
  DATEINVC Date Invoice date
  AMTDUE BCD*10.3 Payment Amount Due
  AMTNET BCD*10.3 Payment Amount Net
  AMTDISC BCD*10.3 Payment Amount Discount
  PAYMAMT BCD*10.3 Receipt Amount
  DISCAMT BCD*10.3 Discount Taken Amount
  APPLY String*1 Apply
  MODE Integer Reserved
  IDTRXTYPE Integer Text Transaction Type [11=Invoice - Item Issued,13=Invoice - Recurring Charge,14=Invoice - Summary Issued,21=Debit Note - Item Issued,24=Debit Note - Summary Issued,31=Credit Note - Item Issued,34=Credit Note - Summary Issued,40=Interest Charge,1=Unapplied Cash - Posted,50=Prepayment - Posted]
  ADJAMT BCD*10.3 Adjustment Amount
  STDOCSTR String*22 Starting Doc. Number
  STDOCDTE Date Starting Date
  STDOCAMT BCD*10.3 Starting Amount
  AMTRMIT BCD*10.3 Receipt Amount
  OBSDISC BCD*10.3 Payment Discount Available
  TCPLINE BCD*3.0 TCP line count
  STRTCUST String*12 Starting Customer No.
  ORIGAPLY String*1 Original Apply
  PNDPAYTOT BCD*10.3 Pending Receipt Amount
  PNDDSCTOT BCD*10.3 Pending Discount Amount
  PNDADJTOT BCD*10.3 Pending Adjustment Amount
  PENDNGBAL BCD*10.3 Pending Balance
  ORGDOCAMT BCD*10.3 Original Document Amount
  SWJOB Integer Job Related [0=No,1=Yes]
  RTGAPPLYTO String*22 Original Doc. No.
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

## ARPTER - Posting Error Messages (view AR0062)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPAYM+POSTINGSEQ+CNTBATCH+CNTITEM+CNTLINE+ERRORCNT+CNTSEQ
Fields (NAME type description [values]):
  CODEPAYM String*2 Batch Type Code
  POSTINGSEQ BCD*5.0 Posting Sequence No.
  CNTBATCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  ERRORCNT BCD*4.0 Error Number
  CNTSEQ BCD*3.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MSGCODE String*7 Message Number
  ERRDESC String*250 Error Description
  ERRCODEPYM String*2 Error Batch Type
  ERRBATCH BCD*5.0 Error Batch Number
  ERRITEM BCD*4.0 Error Entry Number
  ERRLINE BCD*3.0 Error Line Number
  ERRSEQ BCD*3.0 Error Sequence Number

## ARPTP - Payment Codes (view AR0012)
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
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,5=SPS Credit Card,4=Other]

## ARPYM - Payments (view AR0139)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDINVC+CNTSEQ; IDBANK+CHECKNUM+LONGSERIAL [D,M]; IDCUST+CUID [M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTSEQ Long Seq. No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PAYMCODE String*12 Payment Code
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,5=SPS Credit Card]
  DOCDATE Date Document Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDBANK String*8 Bank Code
  CHECKNUM BCD*8.0 Check Number
  LONGSERIAL ??? Check Serial Number
  IDACCT String*45 GL Account to be Credited
  NAMERMIT String*60 Name on Check
  CHECKLANG String*3 Check Language
  CODECURN String*3 Payment Currency
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEEXCH BCD*8.7 Exchange Rate
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  SWRATE Integer Rate Override Flag [0=No,1=Yes]
  AMTPC BCD*10.3 Payment Amount
  AMTTC BCD*10.3 Customer Amount
  AMTHC BCD*10.3 Functional Amount
  POSTSEQNBR BCD*5.0 Posting Sequence Number
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  SWSTATUS Integer Payment Status [0=Outstanding,1=Cleared,2=Reversed]
  DATECLRD Date Date Cleared
  DATERVRSD Date Date Reversed
  TEXTRETRN String*60 Reason for Return
  TRXTYPETXT Integer Document Type [19=Refund]
  CUID Long Client Unique ID
  DATEBUS Date Posting Date
  CCTRANID String*36 Credit Card Transaction Number
  PROCESSCOD String*12 Processing Code
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5

## ARR01 - Company Options (view AR0001)
Keys (first = PK; D=dups allowed, M=modifiable): IDR01
Fields (NAME type description [values]):
  IDR01 String*3 Company Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  NAMECTAC String*60 Contact Name
  TEXTPHON String*30 Telephone Number
  TEXTFAX String*30 Fax Number
  SWMULTCURN Integer Multicurrency [0=No,1=Yes]
  SWRCURCHG Integer Process Recurring Charges [0=No,1=Yes]
  SWEDITIMPT Integer Edit Imported Batches [0=No,1=Yes]
  SWFRCLST Integer Force Listing of Batches [0=No,1=Yes]
  CNTARCVDAY BCD*3.0 Reserved
  SWEDITCUST Integer Edit Cust. Statistics [0=No,1=Yes]
  CODETAXCUS Integer Inc. Tax in Cust. Statistics [0=Not Included,1=Included]
  CODECLDRCU Integer Cust. Statistics Year Type [1=Calendar Year,2=Fiscal Year]
  CODEPERDCU Integer Cust. Statistics Period Type [1=Weekly,2=Seven days,3=Bi-weekly,4=Four weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Fiscal Period]
  SWACCUITEM Integer Keep Item Statistics [0=No,1=Yes]
  SWEDITITEM Integer Edit Item Statistics [0=No,1=Yes]
  CODETAXITM Integer Inc. Tax in Item Statistics [0=Not Included,1=Included]
  CODECLDRIT Integer Item Statistics Year Type [1=Calendar Year,2=Fiscal Year]
  CODEPERDIT Integer Item Statistics Period Type [1=Weekly,2=Seven days,3=Bi-weekly,4=Four weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Fiscal Period]
  SWACCUSLSP Integer Keep Salesperson Statistics [0=No,1=Yes]
  SWEDITSLSP Integer Edit Salesperson Statistics [0=No,1=Yes]
  CODETAXSAP Integer Inc. Tax in Sales Statistics [0=Not Included,1=Included]
  CODECLDRSA Integer Sales Statistics Year Type [1=Calendar Year,2=Fiscal Year]
  CODEPERDSA Integer Sales Statistics Period Type [1=Weekly,2=Seven days,3=Bi-weekly,4=Four weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Fiscal Period]
  ATRRVALSEQ BCD*5.0 Next Revaluation Posting Seq.
  SWKEEPDTLS Integer Keep History
  SWACCUCUS Integer Keep Customer Statistics [0=No,1=Yes]
  SWEDITSUB Integer Edit External Batches [0=No,1=Yes]

## ARR02 - Invoicing Options (view AR0002)
Keys (first = PK; D=dups allowed, M=modifiable): IDR02
Fields (NAME type description [values]):
  IDR02 String*3 Invoicing Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  INVCBTCH BCD*5.0 Next Invoice Batch Number
  TEXTIVPF String*6 Invoice Prefix
  CNTIVPFLEN BCD*2.0 Invoice Number Length
  CNTIVSEQ BCD*5.0 Next Invoice Number
  TEXTCRPF String*6 Credit Note Prefix
  CNTCRPFLEN BCD*2.0 Credit Note Number Length
  CNTCRSEQ BCD*5.0 Next Credit Note Number
  TEXTDRPF String*6 Debit Note Prefix
  CNTDRPFLEN BCD*2.0 Debit Note Number Length
  CNTDRSEQ BCD*5.0 Next Debit Note Number
  TEXTITPF String*6 Interest Invoice Prefix
  CNTITPFLEN BCD*2.0 Interest Invoice Number Length
  CNTITSEQ BCD*5.0 Next Interest Invoice Number
  TEXTRCPF String*6 Recurring Charge Prefix
  CNTRCPFLEN BCD*2.0 Recurring Charge Number Length
  CNTRCSEQ BCD*5.0 Next Recurring Charge Number
  SWPRTINVC Integer Invoice Printing [0=No,1=Yes]
  SWALOWDISC Integer Reserved
  SWALOWIVED Integer Edit After Invoice Printed [0=No,1=Yes]
  SWALOWIVPS Integer Reserved
  SWUSEITCMT Integer Use Item Comment as Default [0=No,1=Yes]
  SWDPLYITCS Integer Show Item Cost [0=No,1=Yes]
  ATRINVCSEQ BCD*5.0 Next Invoice Posting Seq.Number
  SWMANTAX Integer Manual Tax Processing Default [0=No,1=Yes]
  INVCTYPE Integer Default Invoice Type [1=Item,2=Summary]
  SWUSESDOCS Integer Use Separate Numbers [0=No,1=Yes]
  TEXTRIPF String*6 Retainage Invoice Prefix
  CNTRIPFLEN BCD*2.0 Retainage Invoice Length
  CNTRISEQ BCD*5.0 Next Retainage Invoice
  TEXTRXPF String*6 Retainage Credit Note Prefix
  CNTRXPFLEN BCD*2.0 Retainage Credit Note Length
  CNTRXSEQ BCD*5.0 Next Retainage Credit Note
  TEXTRDPF String*6 Retainage Debit Note Prefix
  CNTRDPFLEN BCD*2.0 Retainage Debit Note Length
  CNTRDSEQ BCD*5.0 Next Retainage Debit Note
  SWRTG Integer Use Retainage [0=No,1=Yes]
  SWRTGBASE Integer Retainage Base [0=Document Total After Taxes,1=Document Total Before Taxes]
  RTGSCHDKEY String*12 Retainage Schedule
  RTGSCHDLNK BCD*10.0 Retainage Schedule Link
  RTGLASTRUN Date Date Retainage Sched. Last Run
  RTGDAYS Integer Days Retained
  RTGPERCENT BCD*5.5 Percent Retained
  RTGADVDAYS Integer Days Before Retainage Due
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  SWARPEND Integer Include Pending A/R Trans. [0=No,1=Yes]
  SWOEPEND Integer Include Pending O/E Trans. [0=No,1=Yes]
  SWXXPEND Integer Include Pending Other Trans. [0=No,1=Yes]
  SWTXCTLRC Integer Default Tax Reporting Control [0=No,1=Yes]
  SWTXRTGRPT Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  SWTXDTLCLS Integer Default Detail Tax Class [0=Default to Customer Tax Class,1=Default to 1]
  SWDATEBUS Integer Default Posting Date [0=Document Date,1=Batch Date,2=Session Date]

## ARR03 - Receipt and Adjustment Options (view AR0003)
Keys (first = PK; D=dups allowed, M=modifiable): IDR03
Fields (NAME type description [values]):
  IDR03 String*3 Receipt/Adjustment Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEMNTN Date Date Last Maintained
  PAYMBTCH BCD*5.0 Next Receipt Batch Number
  ADJBTCH BCD*5.0 Next Adjustment Batch Number
  ADJTRX BCD*5.0 Reserved
  PAYMCODE String*12 Default Payment Code
  BANKID String*8 Default Bank Code
  PRTDEPS Integer Allow Printing of Deposit Slips [0=No,1=Yes]
  PAYMEDIT Integer Edit After Dep. Slip Printed [0=No,1=Yes]
  PAYMPOST Integer Force Printing of Deposit Slips [0=No,1=Yes]
  OBLORDR Integer Default Order of Open Documents [1=Document Number,2=PO Number,3=Due Date,4=Order Number,5=Document Date,6=Current Balance,7=Shipment Number,8=Original Doc. No.]
  ATRPAYMSEQ BCD*5.0 Next Receipt Posting Seq.
  ATRADJSEQ BCD*5.0 Next Adjustment Posting Seq.
  PPDPREFIX String*6 Prepayment Prefix
  PPDPFXLEN BCD*2.0 Prepayment Number Length
  CNTPPDSEQ BCD*5.0 Next Prepayment Number
  UCPREFIX String*6 Unapplied Cash Prefix
  UCPFXLEN BCD*2.0 Unapplied Cash Number Length
  CNTUCSEQ BCD*5.0 Next Unapplied Cash Number
  DFRATETYPE String*2 Reserved
  SWALOWADJ Integer Allow Adj. in Receipt Batch [0=No,1=Yes]
  ADPREFIX String*6 Adjustment Prefix
  ADPFXLEN BCD*2.0 Adjustment Number Length
  CNTADSEQ BCD*5.0 Next Adjustment Number
  RMITTYPE Integer Default Transaction Type [1=Receipt,2=Prepayment,3=Unapplied Cash,4=Apply Document,5=Misc. Receipt]
  STMTSEQ Long Next Statement Number
  PYPREFIX String*6 Receipt Prefix
  PYPFXLEN BCD*2.0 Receipt Number Length
  CNTPYSEQ BCD*5.0 Next Receipt Number
  RFBTCH BCD*5.0 Next Refund Batch Number
  RFPREFIX String*6 Refund Prefix
  RFPFXLEN BCD*2.0 Refund Number Length
  CNTRFSEQ BCD*5.0 Next Refund Number
  ATRRFSEQ BCD*5.0 Next Refund Posting Seq.
  SWALOWRCED Integer Edit After Receipt Printed [0=No,1=Yes]
  SWCREATDEP Integer Create Deposit Automatically [0=No,1=Yes]
  SWCHKDUP Integer Check for Duplicate Checks [0=None,1=Warning,2=Error]
  SWSHRCPND Integer Include Pending Transactions [0=None,1=Receipts,2=Receipts and Adjustments,3=All Transactions]
  SWDATEBUS Integer Default Posting Date [0=Document Date,1=Batch Date,2=Session Date]
  SORTCHKBY Integer Sort Checks By [0=Transaction Entry Number,1=Customer Number,2=Payee Name,3=Payee Country,4=Payee Zip/Postal Code]
  SFPABANKID String*8 Payments Acceptance Default Bank ID
  SFPADATE Date Payments Acceptance Retrieval Date
  SFPATIME Time Payments Acceptance Retrieval Time

## ARR04 - Statement Processing Options (view AR0004)
Keys (first = PK; D=dups allowed, M=modifiable): IDR04
Fields (NAME type description [values]):
  IDR04 String*3 Statement Processing Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEMNTN Date Date Last Maintained
  AGINPERD1 BCD*3.0 Aging Period 1
  AGINPERD2 BCD*3.0 Aging Period 2
  AGINPERD3 BCD*3.0 Aging Period 3
  AGECR Integer Age Credit Notes and Debit Notes [1=As Current,2=By Date]
  AGEUAPL Integer Age Unapplied Cash & Prepayments [1=As Current,2=By Date]
  PRTZEROBAL Integer Print Zero-Balance Statements [0=No,1=Yes]

## ARR05 - Customer and Ship-To Options (view AR0005)
Keys (first = PK; D=dups allowed, M=modifiable): IDR05
Fields (NAME type description [values]):
  IDR05 String*3 Cust./Ship-To Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEMNTN Date Date Last Maintained
  CMNTDAYS BCD*3.0 Default No. Days for Expiry
  FLUPDAYS BCD*3.0 Default No. Days for Follow Up
  CMNTTYPE String*8 Default Comment Type
  SWCMNTTYPE Integer Allow Blank Comment Type [0=No,1=Yes]

## ARR06 - G/L Integration Options (view AR0006)
Keys (first = PK; D=dups allowed, M=modifiable): IDR06
Fields (NAME type description [values]):
  IDR06 String*3 Integration Options Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Date Last Maintained
  SWGLPSTDFR Integer Defer Create G/L Batch [0=During Posting,1=On Request Using Create G/L Batch Icon]
  SWGLAPDBTH Integer Create G/L Transactions By [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  SWGLPSTCON Integer Consolidate G/L Transactions [0=Do Not Consolidate,1=Consolidate by Post Seq., Account and Fiscal Period,2=Consolidate by Post Seq., Account, Fiscal Period and Source]
  CODEGLREF Integer RESERVED: G/L Reference Field
  CODEGLDESC Integer RESERVED: G/L Description Field
  GLPAYMPOST BCD*5.0 Last Receipt Posting Seq. to G/L
  GLINVCPOST BCD*5.0 Last Invoice Posting Seq. to G/L
  GLADJPOST BCD*5.0 Last Adj. Posting Seq. to G/L
  GLRVALPOST BCD*5.0 Last Reval. Posting Seq. to G/L
  GLRFPOST BCD*5.0 Last Refund Posting Seq. to G/L
  SRCTYPEIN String*2 G/L Src code - Invoice
  SRCTYPEDB String*2 G/L Src code - Debit Note
  SRCTYPECR String*2 G/L Src code - Credit Note
  SRCTYPEIT String*2 G/L Src code - Interest
  SRCTYPEPY String*2 G/L Src code - Payment Received
  SRCTYPEED String*2 G/L Src code - Discount
  SRCTYPEGL String*2 G/L Src code - Revaluation
  SRCTYPEAD String*2 G/L Src code - Adjustment
  SRCTYPECO String*2 G/L Src code - Consolidation
  SRCTYPEWO String*2 G/L Src code - Write-Off
  SRCTYPEPI String*2 G/L Src code - Prepayment
  SRCTYPEUC String*2 G/L Src code - Unapplied Cash
  SRCTYPERF String*2 G/L Src code - Refund
  SRCTYPERD String*2 G/L Src code - Rounding
  SRCTYPEPYR String*2 G/L Src code - Payment Reversal
  SRCTYPERFR String*2 G/L Src code - Refund Reversal

## ARRAS - Account Sets (view AR0013)
Keys (first = PK; D=dups allowed, M=modifiable): IDACCTSET
Fields (NAME type description [values]):
  IDACCTSET String*6 Account Set
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTVSW Integer Status [0=Inactive,1=Active]
  DATEAINAC Date Inactive Date
  LASTMNTN Date Date Last Maintained
  ARIDACCT String*45 Receivables Control Account
  IDSUSP String*45 Reserved
  CASHLIAB String*45 Prepayment Liability Account
  ACCTDISC String*45 Discounts Account
  ACCTWROF String*45 Write-Offs Account
  CURNCODE String*3 Currency Code
  UNRLGAIN String*45 Unrealized Exchange Gain Account
  UNRLLOSS String*45 Unrealized Exchange Loss Account
  RLZDGAIN String*45 Exchange Gain Account
  RLZDLOSS String*45 Exchange Loss Account
  ACCTADJ String*45 Reserved
  RTGACCT String*45 Retainage Account
  RNDACCT String*45 Exchange Rounding Account

## ARRBC - Billing Cycles (view AR0014)
Keys (first = PK; D=dups allowed, M=modifiable): IDCYCL
Fields (NAME type description [values]):
  IDCYCL String*6 Billing Cycle
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTVSW Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  LASTMNTN Date Date Last Maintained
  LASTSTMT Date Date Statements Last Printed
  LASTINTT Date Date Int. Invoices Last Posted
  LASTSTD Date Reserved
  DAYSCYCL BCD*2.0 Billing Cycle Frequency
  NAME String*60 Remit-To Name
  STREET1 String*60 Remit-To Address 1
  STREET2 String*60 Remit-To Address 2
  STREET3 String*60 Remit-To Address 3
  STREET4 String*60 Remit-To Address 4
  CITY String*30 Remit-To City
  STATE String*30 Remit-To State/Prov.
  POSTCODE String*20 Remit-To Zip/Postal Code
  CNTYCODE String*30 Remit-To Country

## ARRDC - Distribution Codes (view AR0015)
Keys (first = PK; D=dups allowed, M=modifiable): IDDIST
Fields (NAME type description [values]):
  IDDIST String*6 Distribution Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  IDACCTREV String*45 Revenue Account
  IDACCTINV String*45 Inventory Account
  IDACCTCOGS String*45 Cost of Goods Sold Account
  SWDISCABL Integer Discountable [0=No,1=Yes]

## ARRFB - Refund Batches (view AR0140)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH; BTCHSTTS+CNTBTCH [M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BTCHDATE Date Batch Date
  BTCHDESC String*60 Batch Description
  BTCHTYPE Integer Batch Type [1=Entered,2=Imported,3=Generated,4=External]
  BTCHSTTS Integer Batch Status [1=Open,3=Posted,4=Deleted,5=Post In Progress,7=Ready To Post,8=Check Creation In Progress]
  ENTRYCNT BCD*4.0 Number of Entries
  ENTRYTOT BCD*10.3 Total of Entries
  LASTENTRY BCD*4.0 Last Entry Number
  POSTSEQNBR BCD*5.0 Posting Sequence No.
  NBRERRORS BCD*5.0 Number of Errors
  DATECREATE Date Date Created
  DATELSTEDT Date Date Last Edited
  SWPRINTED Integer Batch Printed Flag [0=No,1=Yes]
  SRCEAPPL String*2 Source Application
  CNTCHKPRNT BCD*4.0 Number of Printed Checks

## ARRFD - Refund Details (view AR0142)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE; IDINVC+CNTPAYM+CNTBTCH+CNTITEM [M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,5=SPS Credit Card]
  IDBANK String*8 C.C. Bank Account
  LONGSERIAL Long C.C. Bank Serial Number
  CODECURN String*3 C.C. Payment Currency
  RATETYPE String*2 C.C. Rate Type
  RATEDATE Date C.C. Rate Date
  RATEEXCH BCD*8.7 C.C. Exchange Rate
  RATEOP Integer C.C. Rate Operator [1=Multiply,2=Divide]
  SWRATE Integer C.C. Rate Override Flag [0=No,1=Yes]
  AMTPC BCD*10.3 Amount (Payment)
  AMTTC BCD*10.3 Amount (Customer)
  AMTHC BCD*10.3 Amount (Functional)
  SWJOB Integer Job Related [0=No,1=Yes]
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  AMTJOB BCD*10.3 Job Applied Amount

## ARRFDJ - Refund Detail Jobs (view AR0145)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM+CNTLINE+CNTSEQ; CNTBTCH+CNTITEM+CNTLINE+OCNTLINE [M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQ BCD*3.0 Seq. No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OCNTLINE BCD*3.0 Original Line Number
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  TRANSNBR Long Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  AMTTC BCD*10.3 Refund Amount in Cust. Curr.

## ARRFH - Refund Entries (view AR0141)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+CNTITEM; IDCUST [D,M]; IDINVC [D,M]
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCDESC String*60 Document Description
  DOCDATE Date Document Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  AMTTC BCD*10.3 Refund Amount (Customer)
  AMTHC BCD*10.3 Refund Amount (Functional)
  CODECURN String*3 Customer Currency
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEEXCH BCD*8.7 Exchange Rate
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  SWRATE Integer Rate Override Flag [0=No,1=Yes]
  DATECREATE Date Date Created
  DATELSTEDT Date Date Last Edited
  DETAILCNT Long Number of Details
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  VALUES Long Number of Optional Fields
  SRCEAPPL String*2 Source Application
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  IDBANKCA String*8 Cash Bank Account
  IDACCTCA String*45 Cash GL Account
  CODECURNCA String*3 Cash Payment Currency
  RATETYPECA String*2 Cash Rate Type
  RATEDATECA Date Cash Rate Date
  RATEEXCHCA BCD*8.7 Cash Exchange Rate
  RATEOPCA Integer Cash Rate Operator [1=Multiply,2=Divide]
  SWRATECA Integer Cash Rate Override Flag [0=No,1=Yes]
  AMTPCCA BCD*10.3 Cash Amount (Payment)
  AMTTCCA BCD*10.3 Cash Amount (Customer)
  AMTHCCA BCD*10.3 Cash Amount (Functional)
  IDBANKCK String*8 Check Bank Account
  SWPRINT Integer Check Printing Required [0=No,1=Yes]
  SWPRINTED Integer Check Has Been Printed [0=Not Printed,1=Printed]
  CHECKNUM BCD*8.0 Check Number
  LONGSERIAL ??? Check Serial Number
  CODECURNCK String*3 Check Payment Currency
  RATETYPECK String*2 Check Rate Type
  RATEDATECK Date Check Rate Date
  RATEEXCHCK BCD*8.7 Check Exchange Rate
  RATEOPCK Integer Check Rate Operator [1=Multiply,2=Divide]
  SWRATECK Integer Check Rate Override Flag [0=No,1=Yes]
  AMTPCCK BCD*10.3 Check Amount (Payment)
  AMTTCCK BCD*10.3 Check Amount (Customer)
  AMTHCCK BCD*10.3 Check Amount (Functional)
  NAMERMIT String*60 Remit-To Name
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  CHECKLANG String*3 Check Language [1=ENG,2=FRA,3=ESN,4=AUS,5=MEX,6=CHN,7=CHT]
  AMTTCCC BCD*10.3 C.C. Amount (Customer)
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  CCSPSCNT Long Number of SPS C.C. Details
  CCORIGID String*36 Original C.C. Transaction Number
  CCPREVID String*36 Previous C.C. Transaction Number
  CCPREVSTTS Integer Previous C.C. Process Status [0=SPS Transaction Not Started,9=SPS Credit Transaction Pending,10=SPS Credit Transaction Completed,7=SPS Void Transaction Pending,8=SPS Void Transaction Completed]
  CCTRANID String*36 Current C.C. Transaction Number
  CCTRANSTTS Integer Current C.C. Process Status [0=SPS Transaction Not Started,9=SPS Credit Transaction Pending,10=SPS Credit Transaction Completed,7=SPS Void Transaction Pending,8=SPS Void Transaction Completed]
  PROCESSCOD String*12 Processing Code

## ARRFHO - Refund Optional Fields (view AR0143)
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

## ARRRD - Receipt G/L Distributions (view AR0054)
Keys (first = PK; D=dups allowed, M=modifiable): IDBANK+CNTBTCH+CNTITEM+CNTLINE+CNTSEQRRD; IDCUST+IDINVC+CNTPAYM+IDRMIT+TRXTYPE+CNTSEQOBP [D,M]; IDBANK+DEPSEQ+DEPLINE [D,M]
Fields (NAME type description [values]):
  IDBANK String*8 Bank Code
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  CNTSEQRRD BCD*3.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  IDRMIT String*24 Check/Receipt No.
  TRXTYPE Integer Transaction Type
  CNTSEQOBP BCD*3.0 Applied Payment Sequence No.
  DATEBTCH Date Batch Date
  AMTDISTTC BCD*10.3 Distributed Amount (Source)
  AMTDISTHC BCD*10.3 Distributed Amount (Functional)
  IDDISTCODE String*6 Distribution Code
  IDACCT String*45 G/L Account
  TEXTGLREF String*60 G/L Reference
  TEXTGLDESC String*60 G/L Description
  CNTADJREF BCD*5.0 Adjustment Number
  DEPSTNBR BCD*8.0 Deposit Number
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
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
  AMTCOGS BCD*10.3 COGS Amount
  ALTBASETAX BCD*10.3 Alternate Tax Base Amount
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
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
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLDATE Date Billing Date
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5
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

## ARRRH - Posted Receipts (view AR0040)
Keys (first = PK; D=dups allowed, M=modifiable): IDBANK+IDCUST+IDRMIT+DEPSEQ+DEPLINE+DATERMIT; IDCUST+IDRMIT [D,M]; IDBANK+CNTBTCH+CNTITEM [D,M]; IDCUST+IDRMIT+DATEBTCH [D,M]; IDBANK+DEPSEQ+DEPLINE [D,M]; IDCUST+DATERMIT+IDRMIT [D,M]; IDINVCMTCH [D,M]
Fields (NAME type description [values]):
  IDBANK String*8 Bank Code
  IDCUST String*12 Customer Number
  IDRMIT String*24 Check/Receipt No.
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
  DATERMIT Date Receipt Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEPSTNBR BCD*8.0 Deposit Number
  DATEBTCH Date Batch Date
  AMTRMITTC BCD*10.3 Cust. Receipt Amount
  AMTPAYM BCD*10.3 Bank Receipt Amount
  AMTDISC BCD*10.3 Cust. Discount Amount
  PAYMCODE String*12 Payment Code
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  SWOVRDRATE Integer Bank Rate Override [0=No,1=Yes]
  TEXTRETRN String*60 Reason for Return
  DATELSTMTN Date Date Last Maintained
  DATELSTSTM Date Last Statement Date
  AMTROUNDER BCD*10.3 Amount of Rounding Error
  DATERATE Date Bank to Func. Rate Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  NAMERMIT String*60 Payer
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  SWCHKCLRD Integer Check Cleared [0=Outstanding,1=Cleared,2=Returned]
  AMTRMITHC BCD*10.3 Func. Receipt Amount
  AMTADJ BCD*10.3 Cust. Adjustment Amount
  DATECLRD Date Date Cleared
  DATERVRSD Date Date Returned
  TRXTYPETXT Integer Document Type [5=Unapplied Cash,10=Prepayment,11=Receipt]
  IDINVC String*22 Document No.
  RATEOP Integer Rate Operator
  PAYMTYPE Integer Payment Type [1=Cash,2=Check,3=Credit Card,5=SPS Credit Card,4=Other]
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  SWNONRCVBL Integer Misc. Receipt Flag
  SWJOB Integer Job Related [0=No,1=Yes]
  IDINVCMTCH String*22 Invoice Number
  SWTXAMTCTL Integer Calculate Tax [0=No,1=Yes]
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
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=No,1=Yes]
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
  CNTACC Long Number of Advance Credit Claims
  AMTACCTC BCD*10.3 Total Advance Credit Claim
  AMTACCHC BCD*10.3 Func. Total Advance Credit Claim
  DATEBUS Date Posting Date
  CCTRANID String*36 Credit Card Transaction Number
  PROCESSCOD String*12 Processing Code
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5

## ARRSTRT - Restart (view AR0078)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## ARRTA - Terms Codes (view AR0016)
Keys (first = PK; D=dups allowed, M=modifiable): CODETERM
Fields (NAME type description [values]):
  CODETERM String*6 Terms Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTIVESW Integer Status [0=Inactive,1=Active]
  INACDATE Date Inactive Date
  LASTMNTN Date Date Last Maintained
  MULTIPAYM Integer Use Payment Schedule [0=No,1=Yes]
  VATCODEM Integer Calc.Base for Discount with Tax [1=Included,2=Excluded]
  DISCTYPE Integer Discount Type [1=Days From Invoice Date,2=End of Next Month,3=Day of Next Month,4=Days From Day of Next Month,5=Discount Date Table]
  DISCPCT BCD*5.5 Reserved
  DISCNBR BCD*2.0 Reserved
  DISCDAY BCD*2.0 Reserved
  DDAYSTRT1 BCD*2.0 Discount Table Starting Day 1
  DDAYSTRT2 BCD*2.0 Discount Table Starting Day 2
  DDAYSTRT3 BCD*2.0 Discount Table Starting Day 3
  DDAYSTRT4 BCD*2.0 Discount Table Starting Day 4
  DDAYEND1 BCD*2.0 Discount Table Ending Day 1
  DDAYEND2 BCD*2.0 Discount Table Ending Day 2
  DDAYEND3 BCD*2.0 Discount Table Ending Day 3
  DDAYEND4 BCD*2.0 Discount Table Ending Day 4
  DMNTHADD1 BCD*2.0 Discount Table Months Added 1
  DMNTHADD2 BCD*2.0 Discount Table Months Added 2
  DMNTHADD3 BCD*2.0 Discount Table Months Added 3
  DMNTHADD4 BCD*2.0 Discount Table Months Added 4
  DDAYUSE1 BCD*2.0 Discount Table Day of Month 1
  DDAYUSE2 BCD*2.0 Discount Table Day of Month 2
  DDAYUSE3 BCD*2.0 Discount Table Day of Month 3
  DDAYUSE4 BCD*2.0 Discount Table Day of Month 4
  DUETYPE Integer Due Date Type [1=Days From Invoice Date,2=End of Next Month,3=Day of Next Month,4=Days From Day of Next Month,5=Due Date Table]
  CNTDUEDAY BCD*2.0 Reserved
  DUENBRDAYS BCD*2.0 Reserved
  DUDAYST1 BCD*2.0 Due Date Table Starting Day 1
  DUDAYST2 BCD*2.0 Due Date Table Starting Day 2
  DUDAYST3 BCD*2.0 Due Date Table Starting Day 3
  DUDAYST4 BCD*2.0 Due Date Table Starting Day 4
  DUDAYEND1 BCD*2.0 Due Date Table Ending Day 1
  DUDAYEND2 BCD*2.0 Due Date Table Ending Day 2
  DUDAYEND3 BCD*2.0 Due Date Table Ending Day 3
  DUDAYEND4 BCD*2.0 Due Date Table Ending Day 4
  DUMNTHAD1 BCD*2.0 Due Date Table Months Added 1
  DUMNTHAD2 BCD*2.0 Due Date Table Months Added 2
  DUMNTHAD3 BCD*2.0 Due Date Table Months Added 3
  DUMNTHAD4 BCD*2.0 Due Date Table Months Added 4
  DUDAYUSE1 BCD*2.0 Due Date Table Day of Month 1
  DUDAYUSE2 BCD*2.0 Due Date Table Day of Month 2
  DUDAYUSE3 BCD*2.0 Due Date Table Day of Month 3
  DUDAYUSE4 BCD*2.0 Due Date Table Day of Month 4
  DTEDUESYNC Integer Reserved
  DTEDSCSYNC Integer Reserved
  CNTENTERED BCD*4.0 Number of Payments
  PCTDUETOT BCD*5.5 Total Percent Due

## ARRTB - Terms Payment Schedules (view AR0017)
Keys (first = PK; D=dups allowed, M=modifiable): CODETERM+CNTPAYM
Fields (NAME type description [values]):
  CODETERM String*6 Terms Code
  CNTPAYM BCD*3.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEMNTN Date Date Last Maintained
  PCTDUE BCD*5.5 Percent Due
  DISCTYPE Integer Reserved
  PCTDISC BCD*5.5 Discount Percent
  NUMDAYS BCD*2.0 Discount Number of Days
  DISCDAY BCD*2.0 Discount Day of Month
  DUETYPE Integer Reserved
  DUEDAYS BCD*2.0 Due Number of Days
  DUEDAY BCD*2.0 Due Day of Month

## ARRTG - Retainage Open Documents (view AR0311)
Keys (first = PK; D=dups allowed, M=modifiable): RTGSEQ+IDCUST+IDINVC
Fields (NAME type description [values]):
  RTGSEQ Long Sequence Number
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RTGDATEDUE Date Date Retainage Due
  DATEINVC Date Document Date
  TRXTYPETXT Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Unapplied Cash,10=Prepayment,11=Receipt]
  AMTDUE1 BCD*10.3 Current Amount Due
  AMTDUE2 BCD*10.3 Period 1 Amount Due
  AMTDUE3 BCD*10.3 Period 2 Amount Due
  AMTDUE4 BCD*10.3 Period 3 Amount Due
  AMTDUE5 BCD*10.3 Period 4 Amount Due
  TOTAMTBKWD BCD*10.3 Total Backward Aging
  TOTAMTFWD BCD*10.3 Total Forward Aging
  RTGAMTTC BCD*10.3 Amount Retained - Cust. Curr.
  RTGAMTHC BCD*10.3 Amount Retained - Func. Curr.

## ARRVL - Revaluation Details (view AR0079)
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

## ARRVLLOG - Revaluation History (view AR0089)
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
  ARVERSION String*3 A/R Version Created In

## ARRVLO - Revaluation Optional Fields (view AR0415)
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

## ARSAP - Salespersons (view AR0018)
Keys (first = PK; D=dups allowed, M=modifiable): CODESLSP
Fields (NAME type description [values]):
  CODESLSP String*8 Salesperson
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  CODEEMPL String*15 Employee Number
  NAMEEMPL String*60 Name
  SWCOMM Integer Commissions Paid [0=No,1=Yes]
  AMTANLTARG BCD*10.3 Annual Sales Target
  SALESBASE1 BCD*10.3 Maximum Sales for Rate 1
  SALESBASE2 BCD*10.3 Maximum Sales for Rate 2
  SALESBASE3 BCD*10.3 Maximum Sales for Rate 3
  SALESBASE4 BCD*10.3 Maximum Sales for Rate 4
  SALESRATE1 BCD*5.5 Commission Rate 1
  SALESRATE2 BCD*5.5 Commission Rate 2
  SALESRATE3 BCD*5.5 Commission Rate 3
  SALESRATE4 BCD*5.5 Commission Rate 4
  SALESRATE5 BCD*5.5 Commission Rate 5
  SALESCOMM BCD*10.3 Commissionable Sales
  SALESCOST BCD*10.3 Cost of Commissionable Sales
  DATECLRD Date Date Last Cleared

## ARSFAUD - Payments Acceptance Receipt Audit (view AR0218)
Keys (first = PK; D=dups allowed, M=modifiable): SFPAID
Fields (NAME type description [values]):
  SFPAID String*36 SF Payments Transaction ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNBR String*22 Document Number

## ARSIA - Recurring Charges (view AR0046)
Keys (first = PK; D=dups allowed, M=modifiable): IDSTDINVC+IDCUST; IDCUST [D,M]; IDBILL [D,M]; SCHEDKEY+SCHEDLINK [D,M]
Fields (NAME type description [values]):
  IDSTDINVC String*16 Recurring Charge Code
  IDCUST String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDBILL String*6 Reserved
  TEXTDESC String*60 Description
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
  DATELSTMTN Date Date Last Maintained
  DATELSTPRC Date Last Invoice Date Generated
  DATEEFF Date Effective Date
  DATEEXPR Date Expiration Date
  AMTTOTCHRG BCD*10.3 Maximum Total Invoice Amount
  AMTINVC BCD*10.3 YTD Total Invoice Amount
  DATEINVDAY BCD*2.0 Reserved
  SWLASTDAY Integer Reserved
  IDCUSTSHPT String*6 Ship-To Location
  TEXTSHIP String*15 Reserved
  TEXTINST String*60 Special Instructions
  IDORDENBR String*22 Order Number
  IDCUSTPO String*22 PO Number
  IDJOBNBR String*22 Reserved
  INVCDESC String*60 Invoice Description
  SWPRTINVC Integer Reserved
  CODECURN String*3 Currency Code
  IDRATETYPE String*2 Rate Type
  CODETERM String*6 Terms
  CNTLSTLINE BCD*3.0 Last Line Number
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  SWTXBL Integer Taxable [0=No,1=Yes]
  SWMANLTX Integer Tax Override [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  CODETAX1 String*12 Tax Authority 1
  CODETAX2 String*12 Tax Authority 2
  CODETAX3 String*12 Tax Authority 3
  CODETAX4 String*12 Tax Authority 4
  CODETAX5 String*12 Tax Authority 5
  TAXSTTS1 Integer Tax Class 1
  TAXSTTS2 Integer Tax Class 2
  TAXSTTS3 Integer Tax Class 3
  TAXSTTS4 Integer Tax Class 4
  TAXSTTS5 Integer Tax Class 5
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
  AMTTXBL BCD*10.3 Taxable Amount
  AMTNOTTXBL BCD*10.3 Non-Taxable Amount
  AMTTAXTOTL BCD*10.3 Total Tax Amount
  AMTINVTOTL BCD*10.3 Last Invoice Amount Posted
  CNTPAYMTOT BCD*3.0 Reserved
  AMTPAYMSCD BCD*10.3 Invoice Subtotal
  MAXCOUNT Integer Maximum Number of Invoices
  YTDCOUNT Integer YTD Number of Invoices
  SCHEDKEY String*12 Schedule
  SCHEDLINK BCD*10.0 Schedule Link
  EXPIRETYPE Integer Expiration Type [0=No Expiration,1=Specific Date,2=Maximum Amount,3=Number of Invoices]
  SHPVIACODE String*6 Ship Via Code
  SHPVIADESC String*60 Ship Via Description
  AMTINVCTOT BCD*10.3 Invoice Total Before Tax
  AMTNETTOT BCD*10.3 Invoice Total Including Tax
  VALUES Long Number of Optional Fields
  AMTTAXTOT BCD*10.3 Total Tax Amount
  INVCTYPE Integer Invoice Type [1=Item,2=Summary]
  SWJOB Integer Job Related [0=No,1=Yes]
  DATENEXT Date Next Scheduled Date
  OPENCOUNT Integer Unposted Number of Invoices
  OPENAMOUNT BCD*10.3 Unposted Total Invoice Amount
  POSTCOUNT Integer Posted Number of Invoices
  POSTAMOUNT BCD*10.3 Posted Total Invoice Amount
  LSTDATEINV Date Last Invoice Date Posted
  LSTIDINVC String*22 Last Invoice Number Posted
  LSTCNTBTCH BCD*5.0 Last Batch Number Posted
  LSTCNTITEM BCD*4.0 Last Entry Number Posted
  LSTPOSTSEQ BCD*5.0 Last Posting Sequence Number
  IDACCTSET String*6 Account Set
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5

## ARSIAO - Recurring Charge Optional Fields (view AR0405)
Keys (first = PK; D=dups allowed, M=modifiable): IDSTDINVC+IDCUST+OPTFIELD; OPTFIELD+IDSTDINVC+IDCUST
Fields (NAME type description [values]):
  IDSTDINVC String*16 Recurring Charge Code
  IDCUST String*12 Customer Number
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

## ARSID - Recurring Charge Details (view AR0047)
Keys (first = PK; D=dups allowed, M=modifiable): IDSTDINVC+IDCUST+CNTLINE
Fields (NAME type description [values]):
  IDSTDINVC String*16 Recurring Charge Code
  IDCUST String*12 Customer Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDITEM String*16 Item Number
  IDDIST String*6 Distribution Code
  TEXTDESC String*60 Description
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  AMTPRIC BCD*10.6 Price
  AMTEXTN BCD*10.3 Extended Amount w/ TIP
  AMTCOGS BCD*10.3 COGS Amount
  AMTTXBL BCD*10.3 Extended Amount w/o TIP
  AMTTOTTX BCD*10.3 Total Tax Amount
  SWMANLTAX Integer Reserved
  BASETAX1 BCD*10.3 Tax Base 1
  BASETAX2 BCD*10.3 Tax Base 2
  BASETAX3 BCD*10.3 Tax Base 3
  BASETAX4 BCD*10.3 Tax Base 4
  BASETAX5 BCD*10.3 Tax Base 5
  TAXSTTS1 Integer Tax Class 1
  TAXSTTS2 Integer Tax Class 2
  TAXSTTS3 Integer Tax Class 3
  TAXSTTS4 Integer Tax Class 4
  TAXSTTS5 Integer Tax Class 5
  SWTXINCL1 Integer Tax Included 1 [0=No,1=Yes]
  SWTXINCL2 Integer Tax Included 2 [0=No,1=Yes]
  SWTXINCL3 Integer Tax Included 3 [0=No,1=Yes]
  SWTXINCL4 Integer Tax Included 4 [0=No,1=Yes]
  SWTXINCL5 Integer Tax Included 5 [0=No,1=Yes]
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
  IDACCTREV String*45 Revenue Account
  IDJOBPROJ String*30 Reserved
  AMTINVCTOT BCD*10.3 Distributed Amount Before Tax
  SWDISCABL Integer Discountable [0=No,1=Yes]
  VALUES Long Optional Fields
  COMMENT String*250 Comments
  SWPRTSTMT Integer Print Comment
  IDACCTINV String*45 Inventory Account
  IDACCTCOGS String*45 COGS Account
  ITEMCOST BCD*10.3 Item Cost
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  AMTWHT1TC BCD*10.3 Tax Withheld 1
  AMTWHT2TC BCD*10.3 Tax Withheld 2
  AMTWHT3TC BCD*10.3 Tax Withheld 3
  AMTWHT4TC BCD*10.3 Tax Withheld 4
  AMTWHT5TC BCD*10.3 Tax Withheld 5

## ARSIDO - Rec. Charge Detail Opt. Fields (view AR0404)
Keys (first = PK; D=dups allowed, M=modifiable): IDSTDINVC+IDCUST+CNTLINE+OPTFIELD; OPTFIELD+IDSTDINVC+IDCUST+CNTLINE
Fields (NAME type description [values]):
  IDSTDINVC String*16 Recurring Charge Code
  IDCUST String*12 Customer Number
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

## ARSLCUS - Selected customers (view AR0420)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+RECORDNO+IDCUST
Fields (NAME type description [values]):
  SELSEQ Long Sequence Number
  RECORDNO Long Record Number
  IDCUST String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DELMETHOD Integer Delivery Method
  SORTVALUE1 String*60 Sort Field Value 1
  SORTVALUE2 String*60 Sort Field Value 2
  SORTVALUE3 String*60 Sort Field Value 3
  SORTVALUE4 String*60 Sort Field Value 4
  SORTTYPE1 Integer Sort Field Type 1
  SORTTYPE2 Integer Sort Field Type 2
  SORTTYPE3 Integer Sort Field Type 3
  SORTTYPE4 Integer Sort Field Type 4

## ARSLLBL - Generated Labels (view AR0190)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+IDCUST+IDSHIPTO+IDINVC+INSTANCE
Fields (NAME type description [values]):
  SELSEQ Long Sequence Number
  IDCUST String*12 Customer Number
  IDSHIPTO String*6 Ship-To Location
  IDINVC String*22 Document Number
  INSTANCE Long Instance Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAMECUST String*60 Customer Name
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*20 Zip/Postal Code
  CODECTRY String*30 Country
  NAMECTAC String*60 Contact Name

## ARSLLST - Select Lists (view AR0097)
Keys (first = PK; D=dups allowed, M=modifiable): SEQNO+SWTYPE+KEYFIELD; SEQNO+SWTYPE+FIELD1+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD2+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD3+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD4+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD5+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD6+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD7+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD8+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD9+KEYFIELD [D,M]; SEQNO+SWTYPE+FIELD10+KEYFIELD [D,M]
Fields (NAME type description [values]):
  SEQNO Long Sequence No.
  SWTYPE Integer Type
  KEYFIELD String*60 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  FIELD1 String*60 Field 1
  FIELD2 String*60 Field 2
  FIELD3 String*60 Field 3
  FIELD4 String*60 Field 4
  FIELD5 String*60 Field 5
  FIELD6 String*60 Field 6
  FIELD7 String*60 Field 7
  FIELD8 String*60 Field 8
  FIELD9 String*60 Field 9
  FIELD10 String*60 Field 10
  FIELD11 String*60 Field 11
  FIELD12 String*60 Field 12
  FIELD13 String*60 Field 13
  FIELD14 String*60 Field 14
  FIELD15 String*60 Field 15
  FIELD16 String*60 Field 16
  FIELD17 String*60 Field 17
  FIELD18 String*60 Field 18

## ARSPS - Salesperson Statistics (view AR0030)
Keys (first = PK; D=dups allowed, M=modifiable): CODESLSP+CNTYR+CNTPERD
Fields (NAME type description [values]):
  CODESLSP String*8 Salesperson
  CNTYR String*4 Year
  CNTPERD String*2 Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTINVC BCD*4.0 Number of Invoices
  CNTCR BCD*4.0 Number of Credit Notes
  CNTDR BCD*4.0 Number of Debit Notes
  CNTPAYM BCD*4.0 Number of Receipts
  CNTDISC BCD*4.0 Number of Discounts
  CNTWROF BCD*4.0 Number of Write-Offs
  AMTINVC BCD*10.3 Total Invoice Amount
  AMTCR BCD*10.3 Total Credit Note Amount
  AMTDR BCD*10.3 Total Debit Note Amount
  AMTPAYM BCD*10.3 Total Receipt Amount
  AMTDISC BCD*10.3 Total Discount Amount
  AMTWROF BCD*10.3 Total Write-Off Amount

## ARSTCUS - Reprint Statement Customers (view AR0111)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDCUST; SWNATSTMT+IDCUST+STMTDATE [D,M]; STMTSEQ+IDNATACCT [D,M]
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDCUST String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SWPRINTED Integer Statement Printed Flag [0=No,1=Yes]
  SWNATSTMT Integer NAT Statement Switch [0=Customer Statements,1=National Acct. Statements,2=Letters or Labels]
  IDNATACCT String*12 National Account Number
  STMTDATE Date Statement Run Date
  TEXTSNAM String*10 Short Name
  IDGRP String*6 Group Code
  SWACTV Integer Status
  DATEINAC Date Inactive Date
  DATELASTMN Date Date Last Maintained
  SWHOLD Integer On Hold
  DATESTART Date Start Date
  IDPPNT String*12 Reserved
  CODEDAB String*9 Credit Bureau Number
  CODEDABRTG String*5 Credit Bureau Rating
  DATEDAB Date Credit Bureau Date
  NAMECUST String*60 Customer Name
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
  CODETERR String*6 Territory Code
  IDACCTSET String*6 Account Set
  IDAUTOCASH String*6 Autocash Profile
  IDBILLCYCL String*6 Billing Cycle
  IDSVCCHRG String*6 Interest Profile
  IDDLNQ String*6 Reserved
  CODECURN String*3 Currency Code
  SWPRTSTMT Integer Print Statements [0=No,1=Yes]
  SWPRTDLNQ Integer Reserved
  SWBALFWD Integer Account Type [0=Open Item,1=Balance Forward]
  CODETERM String*6 Terms
  IDRATETYPE String*2 Rate Type
  CODETAXGRP String*12 Tax Group
  IDTAXREGI1 String*20 Tax Registration No. 1
  IDTAXREGI2 String*20 Tax Registration No. 2
  IDTAXREGI3 String*20 Tax Registration No. 3
  IDTAXREGI4 String*20 Tax Registration No. 4
  IDTAXREGI5 String*20 Tax Registration No. 5
  TAXSTTS1 Integer Tax Class Code 1
  TAXSTTS2 Integer Tax Class Code 2
  TAXSTTS3 Integer Tax Class Code 3
  TAXSTTS4 Integer Tax Class Code 4
  TAXSTTS5 Integer Tax Class Code 5
  AMTCRLIMT BCD*10.3 Credit Limit (Cust. Curr.)
  AMTBALDUET BCD*10.3 Balance Due in Cust. Curr.
  AMTBALDUEH BCD*10.3 Balance Due in Func. Curr.
  DATELASTST Date Date of Last Statement
  AMTLASTSTT BCD*10.3 Last Statement Total Cust. Curr.
  AMTLASTSTH BCD*10.3 Reserved
  DTBEGBALFW Date Date of Last Bal. Fwd. Statement
  AMTBALFWDT BCD*10.3 Beginning Bal. on Last Statement
  AMTBALFWDH BCD*10.3 Reserved
  DTLASTRVAL Date Date of Last Revaluation
  AMTBALLARV BCD*10.3 Last Revaluation Balance
  CNTOPENINV BCD*4.0 Number of Open Documents
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
  DATELASTPA Date Date of Last Receipt
  DATELASTDI Date Date of Last Discount
  DATELASTAD Date Date of Last Adjustment
  DATELASTWR Date Date of Last Write-Off
  DATELASTRI Date Date of Last Returned Check
  DATELASTIN Date Date of Last Interest Charge
  DATELASTDQ Date Reserved
  IDINVCHI String*22 Largest Invoice Number
  IDINVCHILY String*22 Largest Invoice Number Last Yr.
  AMTINVHIT BCD*10.3 Largest Invoice - Cust. Curr.
  AMTBALHIT BCD*10.3 Highest Balance - Cust. Curr.
  AMTINVHILT BCD*10.3 Lgst. Inv. Last Yr. Cust. Curr.
  AMTBALHILT BCD*10.3 High Bal. Last Yr. - Cust. Curr.
  AMTLASTIVT BCD*10.3 Last Invoice Amt. - Cust. Curr.
  AMTLASTCRT BCD*10.3 Last Cr. Note Amt. - Cust. Curr.
  AMTLASTDRT BCD*10.3 Last Dr. Note Amt. - Cust. Curr.
  AMTLASTPYT BCD*10.3 Last Receipt - Cust. Curr.
  AMTLASTDIT BCD*10.3 Last Discount Amt. - Cust. Curr.
  AMTLASTADT BCD*10.3 Last Adj. Amt. - Cust. Curr.
  AMTLASTWRT BCD*10.3 Last Write-Off Amt. Cust. Curr.
  AMTLASTRIT BCD*10.3 Last Ret'd. Chk. Amt. Cust. Curr
  AMTLASTINT BCD*10.3 Last Int. Charge - Cust. Curr.
  AMTINVHIH BCD*10.3 Largest Invoice - Func. Curr.
  AMTBALHIH BCD*10.3 Highest Balance - Func. Curr.
  AMTINVHILH BCD*10.3 Lgst. Inv. Last Yr. Func. Curr.
  AMTBALHILH BCD*10.3 High Bal. Last Yr. - Func. Curr.
  AMTLASTIVH BCD*10.3 Last Invoice Amt. - Func. Curr.
  AMTLASTCRH BCD*10.3 Last Cr. Note Amt. - Func. Curr.
  AMTLASTDRH BCD*10.3 Last Dr. Note Amt. - Func. Curr.
  AMTLASTPYH BCD*10.3 Last Receipt - Func. Curr.
  AMTLASTDIH BCD*10.3 Last Discount Amt. - Func. Curr.
  AMTLASTADH BCD*10.3 Last Adj. Amt. - Func. Curr.
  AMTLASTWRH BCD*10.3 Last Write-Off Amt. Func. Curr.
  AMTLASTRIH BCD*10.3 Last Ret'd. Chk. Amt. Func. Curr
  AMTLASTINH BCD*10.3 Last Int. Charge - Func. Curr.
  CODESLSP1 String*8 Salesperson 1
  CODESLSP2 String*8 Salesperson 2
  CODESLSP3 String*8 Salesperson 3
  CODESLSP4 String*8 Salesperson 4
  CODESLSP5 String*8 Salesperson 5
  PCTSASPLT1 BCD*5.5 Sales-Split Percentage 1
  PCTSASPLT2 BCD*5.5 Sales-Split Percentage 2
  PCTSASPLT3 BCD*5.5 Sales-Split Percentage 3
  PCTSASPLT4 BCD*5.5 Sales-Split Percentage 4
  PCTSASPLT5 BCD*5.5 Sales-Split Percentage 5
  PRICLIST String*6 Customer Price List
  CUSTTYPE Integer Customer Discount Type [0=Base,1=A,2=B,3=C,4=D,5=E]
  AMTPDUE BCD*10.3 Amount Past Due
  TEXTSTMT String*45 Dunning Message
  EMAIL1 String*50 Contact's E-mail
  EMAIL2 String*50 Customer's E-mail
  WEBSITE String*100 Web Site
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (customer),4=Email (contact),5=Email (multiple contacts)]
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  SWPARTSHIP Integer Allow Partial Shipments [0=No,1=Yes]
  HAMTBGNBLF BCD*10.3 HDR Amount Beginning Balance Forward
  HAMTEBALFD BCD*10.3 HDR Amount Ending Balance Forward
  HAMTSTMTBL BCD*10.3 HDR Amount Statement Balance
  HAMTDUECUR BCD*10.3 HDR Amount Due Current Period
  HAMTDUEAG1 BCD*10.3 HDR Amount Due 1st Period
  HAMTDUEAG2 BCD*10.3 HDR Amount Due 2nd Period
  HAMTDUEAG3 BCD*10.3 HDR Amount Due 3rd Period
  HAMTDUEAG4 BCD*10.3 HDR Amount Due 4th Period
  HAMTDUEFWD BCD*10.3 HDR Amount Due Forward Balance
  RBCNAME String*60 Remit-To Name
  RBCSTREET1 String*60 Remit-To Address 1
  RBCSTREET2 String*60 Remit-To Address 2
  RBCSTREET3 String*60 Remit-To Address 3
  RBCSTREET4 String*60 Remit-To Address 4
  RBCCITY String*30 Remit-To City
  RBCSTATE String*30 Remit-To State/Prov.
  RBCPSTCDE String*20 Remit-To Zip/Postal Code
  RBCCNTYCDE String*30 Remit-To Country
  CUSDECIMAL Integer Customer Currency Decimal
  CURSYMBOL String*4 Customer Currency Symbol
  VALUES Long Optional Fields

## ARSTCUSO - Customer Statement Optional Fields (view AR0506)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDCUST+OPTFIELD; OPTFIELD+STMTSEQ+IDCUST
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDCUST String*12 Customer Number
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

## ARSTNAT - Reprint Statement NAT Customers (view AR0114)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDNATACCT; IDNATACCT+STMTDATE [D,M]
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDNATACCT String*12 National Account Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STMTDATE Date Statement Run Date
  SWPRINTED Integer Statement Printed Flag [0=No,1=Yes]
  NAMEACCT String*60 National Account Name
  TEXTSTRE1 String*60 NAT Address Line 1
  TEXTSTRE2 String*60 NAT Address Line 2
  TEXTSTRE3 String*60 NAT Address Line 3
  TEXTSTRE4 String*60 NAT Address Line 4
  NAMECITY String*30 NAT City
  CODESTATE String*30 NAT State/Prov.
  CODEPOST String*20 NAT Zip/Postal Code
  CODECTRY String*30 NAT Country
  NAMECTAC String*60 NAT Contact Name
  TEXTPHON1 String*30 NAT Phone Number
  TEXTPHON2 String*30 NAT Fax Number
  TEXTSTMT String*45 NAT Dunning Message
  EMAIL String*50 E-mail
  WEBSITE String*100 National Accounts's Web Site
  CTACPHONE String*30 Contact's Phone
  CTACFAX String*30 Contact's Fax
  CTACEMAIL String*50 Contact's E-mail
  DELMETHOD Integer Delivery Method [0=Mail,2=Email (national account),4=Email (contact),5=Email (multiple contacts)]
  SWBALFWD Integer Account Type
  AMTBGNBLF BCD*10.3 NAT Amount Beginning Balance Forward
  AMTEBALFD BCD*10.3 NAT Amount Ending Balance Forward
  AMTSTMTBL BCD*10.3 NAT Amount Statement Balance
  AMTDUECUR BCD*10.3 NAT Amount Due Current Period
  AMTDUEAG1 BCD*10.3 NAT Amount Due 1st Period
  AMTDUEAG2 BCD*10.3 NAT Amount Due 2nd Period
  AMTDUEAG3 BCD*10.3 NAT Amount Due 3rd Period
  AMTDUEAG4 BCD*10.3 NAT Amount Due 4th Period
  AMTDUEFWD BCD*10.3 NAT Amount Due Forward Balance
  AMTCRLIMIT BCD*10.3 Credit Limit
  CODECURN String*3 Currency Code

## ARSTOBL - Reprint Statement Customer Invoices (view AR0112)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDCUST+IDINVC
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STMTDATE Date Statement Run Date
  CODE String*1 Code
  RECTYPE String*1 Record Type
  IDRMIT String*24 Check/Receipt Number
  IDCUSTPO String*22 PO Number
  IDORDERNBR String*22 Order Number
  DATEINVC Date Document Date
  DATEDUE Date Due Date
  DESCINVC String*60 Document Description
  TRXTYPETXT Integer Document Type
  TRXTYPEID Integer Transaction Type
  AMTDUE BCD*10.3 Amount Due
  AMTDISC BCD*10.3 Discount Amount
  IDCUSTSHPT String*6 Ship-To Location
  CODETERM String*6 Terms
  DATELASTST Date Last Statement Date
  VALUES Long Optional Fields
  AMTINVC BCD*10.3 Invoice Amount

## ARSTOBLO - Statement Customer Invoice Optional Fields (view AR0507)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDCUST+IDINVC+OPTFIELD; OPTFIELD+STMTSEQ+IDCUST+IDINVC
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDCUST String*12 Customer Number
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

## ARSTOBP - Reprint Statement Customer Receipts (view AR0113)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ+IDCUST+IDINVC+CNTSEQ
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTSEQ Long Sequence No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STMTDATE Date Statement Run Date
  IDRMIT String*24 Check/Receipt No.
  DATEBUS Date Posting Date
  TRANSTYPE Integer Document Type
  AMTPAYMTC BCD*10.3 Cust. Receipt Amount
  TRXTYPE Integer Transaction Type
  IDMEMOXREF String*22 Reference Document Number

## ARSTRUN - Reprint Statement Header (view AR0110)
Keys (first = PK; D=dups allowed, M=modifiable): STMTSEQ; STMTDATE [D,M]
Fields (NAME type description [values]):
  STMTSEQ Long Statement Run Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STMTDATE Date Statement Run Date
  SWFINISH Integer Statement Run Completed Flag [0=No,1=Yes]
  DATECUTOFF Date Cutoff Date
  SWINVCDATE Integer Due Date / Invoice Date [0=Due Date,1=Doc Date]
  SWDEBIT Integer Include Debit Balances [0=No,1=Yes]
  SWCREDIT Integer Include Credit Balances [0=No,1=Yes]
  SWZEROBAL Integer Include Zero Balances [0=No,1=Yes]
  SWINCLPAID Integer Include Fully Paid Transactions [0=No,1=Yes]
  SWDETAIL Integer Include Details [0=Summary,1=Detail]
  SWTYPERUN Integer Run Type [0=Customer Statements,1=National Acct. Statements,2=Letters or Labels]
  SWDTLSRTBY Integer Detail Sort [0=Doc No.,1=Doc Date]
  IDDUNNING String*8 Dunning Message Code
  IDFROM1 String*60 Range 1 From
  IDTO1 String*60 Range 1 To
  INDEX1 Integer Range 1 Type
  IDFROM2 String*60 Range 2 From
  IDTO2 String*60 Range 2 To
  INDEX2 Integer Range 2 Type
  IDFROM3 String*60 Range 3 From
  IDTO3 String*60 Range 3 To
  INDEX3 Integer Range 3 Type
  IDFROM4 String*60 Range 4 From
  IDTO4 String*60 Range 4 To
  INDEX4 Integer Range 4 Type
  RPTNAME String*255 Report Name
  DELMETHOD Integer Delivery Method [1=Customer,0=Print Destination]
  SORTINDEX1 Integer Sort field 1
  SORTINDEX2 Integer Sort field 2
  SORTINDEX3 Integer Sort field 3
  SORTINDEX4 Integer Sort field 4
  AGEPERIOD1 BCD*3.0 Current
  AGEPERIOD2 BCD*3.0 First Period
  AGEPERIOD3 BCD*3.0 Second Period
  AGEPERIOD4 BCD*3.0 Third Period
  SWOVERDUE Integer Select Customers Based On Overdue Days [0=No,1=Yes]
  OVERDUEDAY Long Number of Overdue Days and Later
  STMTTYPE Integer Open Item Statement Type [0=Version 5.1, 5.2, and 5.3 Format,1=Balance Forward,2=Transaction Current Outstanding Balances,3=Transaction Opening Balances Showing Applied Details,4=Transaction Opening Balances and New Transactions]

## ARSVC - Interest Rates by Currency (view AR0019)
Keys (first = PK; D=dups allowed, M=modifiable): CODESVCCHR+CODECURN
Fields (NAME type description [values]):
  CODESVCCHR String*6 Interest Profile
  CODECURN String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMTMINCHG BCD*10.3 Minimum Interest Charge
  RTESVCCHRG BCD*8.7 Annual Interest Rate

## ARSVD - Interest Profiles (view AR0020)
Keys (first = PK; D=dups allowed, M=modifiable): CODESVCCHR
Fields (NAME type description [values]):
  CODESVCCHR String*6 Interest Profile
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTVSW Integer Status [0=Inactive,1=Active]
  INACDATE Date Inactive Date
  DATEMNTN Date Date Last Maintained
  IDACCTCHRG String*45 Interest Income Account
  TERMCODE String*6 Terms Code
  SVCTYPE Integer Calculate Interest By [1=Document,2=Balance]
  PDUEDAYS BCD*2.0 Number of Days Overdue
  RNDGUPSW Integer Round Up to Minimum [0=No,1=Yes]
  CHRGCMPDSW Integer Compound Interest [0=No,1=Yes]

## ARTCC - Advance Credits (view AR0170)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPAYM+CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CODEPAYM String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
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
  IDCUST String*12 Customer Number

## ARTCN - Miscellaneous Receipts (view AR0043)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPAYM+CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  CODEPAYM String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
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
  AMTCOGS BCD*10.3 COGS Amount
  ALTBASETAX BCD*10.3 Alternate Tax Base Amount
  TXAMT1RC BCD*10.3 Tax Reporting Amount 1
  TXAMT2RC BCD*10.3 Tax Reporting Amount 2
  TXAMT3RC BCD*10.3 Tax Reporting Amount 3
  TXAMT4RC BCD*10.3 Tax Reporting Amount 4
  TXAMT5RC BCD*10.3 Tax Reporting Amount 5
  TXTOTRC BCD*10.3 Tax Reporting Total
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
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CATEGORY String*16 Category Code
  RESOURCE String*24 Project/Category Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLDATE Date Billing Date
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5

## ARTCP - Applied Receipts/Adjustments (view AR0044)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPAYM+CNTBTCH+CNTITEM+CNTLINE; IDCUST+IDINVC+CNTPAYM [D,M]; CODEPAYM+CNTBTCH+CNTITEM+IDINVC+CNTPAYM [M]
Fields (NAME type description [values]):
  CODEPAYM String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  CNTLINE BCD*3.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDCUST String*12 Customer Number
  IDINVC String*22 Document Number
  CNTPAYM BCD*3.0 Payment Number
  TRXTYPE Integer Transaction Type [2=Unapplied Cash - Posted,51=Receipt - Posted,57=Prepayment - Posted,81=Adjustment - Posted,80=Write-Off - Posted]
  PYMTRESL String*2 Payment Resolution
  AMTPAYM BCD*10.3 Cust. Receipt Amount
  AMTERNDISC BCD*10.3 Cust. Discount Amount Taken
  CNTLASTSEQ BCD*3.0 Next Adj. Seq. No.
  AMTADJTOT BCD*10.3 Cust. Adjustment Total
  CNTADJ BCD*5.0 Adjustment Number
  TEXTADJ String*60 Description
  GLREF String*60 Reference
  IDPPD String*22 Generated PP/UC No.
  IDDOCMTCH String*22 PP Matching Doc. No.
  CDAPPLYTO Integer PP Matching Doc. Type [1=(None),2=Document Number,3=PO Number,4=Order Number,9=Shipment Number]
  AMTDBADJTC BCD*10.3 Total Cust. Debit Amount
  AMTCRADJTC BCD*10.3 Total Cust. Credit Amount
  DOCTYPE Integer Document Type
  SWJOB Integer Job Related [0=No,1=Yes]
  AMTPAYMTOT BCD*10.3 Job Total Payment Amount
  AMTDISCTOT BCD*10.3 Job Total Discount Amount
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  RTGTOTDBTC BCD*10.3 Rtg. Debit Amt. - Cust. Curr
  RTGTOTCRTC BCD*10.3 Rtg. Credit Amt. - Cust. Curr
  RTGAMT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGTERMS String*6 Retainage Terms Code
  SWRTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  AMTPAYMHC BCD*10.3 Func. Receipt Amount
  AMTDISCHC BCD*10.3 Func. Total Discount Amount
  AMTADJHC BCD*10.3 Func. Total Adjustment Amount
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  AMTWHD1TC BCD*10.3 Cust. Tax Withheld Amount 1
  AMTWHD2TC BCD*10.3 Cust. Tax Withheld Amount 2
  AMTWHD3TC BCD*10.3 Cust. Tax Withheld Amount 3
  AMTWHD4TC BCD*10.3 Cust. Tax Withheld Amount 4
  AMTWHD5TC BCD*10.3 Cust. Tax Withheld Amount 5
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

## ARTCR - Receipts/Adjustments (view AR0042)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPYMTYP+CNTBTCH+CNTITEM; CODEPYMTYP+IDCUST [D,M]; CODEPYMTYP+IDRMIT [D,M]; CODEPYMTYP+DOCNBR [D,M]
Fields (NAME type description [values]):
  CODEPYMTYP String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDRMIT String*24 Check/Receipt No.
  IDCUST String*12 Customer Number
  DATERMIT Date Receipt Date/Adjustment Date
  TEXTRMIT String*60 Entry Description
  TXTRMITREF String*60 Entry Reference
  AMTRMIT BCD*10.3 Bank Receipt Amount
  AMTRMITTC BCD*10.3 Cust. Receipt Amount
  RATEEXCHTC BCD*8.7 Cust. Exchange Rate
  SWRATETC Integer Cust. Rate Overridden [0=No,1=Yes]
  CNTPAYMETR BCD*3.0 Number of Documents Applied to
  AMTPAYMTC BCD*10.3 Total Cust. Amount Applied
  AMTDISCTC BCD*10.3 Total Cust. Discount Amount
  CODEPAYM String*12 Payment Code
  CODECURN String*3 Customer Currency Code
  RATETYPEHC String*2 Bank Rate Type
  RATEEXCHHC BCD*8.7 Bank Exchange Rate
  SWRATEHC Integer Bank Rate Overridden [0=No,1=Yes]
  RMITTYPE Integer Receipt Trans. Type [1=Receipt,2=Prepayment,3=Unapplied Cash,4=Apply Document,5=Misc. Receipt,6=Write-Off,7=Adjustment]
  DOCTYPE Integer Document Type [1=(None),2=Document Number,3=PO Number,4=Order Number,5=Prepayment,6=Unapplied Cash,7=Credit Note,8=Receipt]
  IDINVCMTCH String*22 Matching Document Number
  CNTLSTLINE BCD*3.0 Last Line Number
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  TEXTPAYOR String*60 Payer
  DATERATETC Date Cust. Rate Date
  RATETYPETC String*2 Cust. Rate Type
  AMTADJENT BCD*10.3 Cust. Adjustment Amount
  DATERATEHC Date Bank Rate Date
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,5=SPS Credit Card,4=Other]
  REMUNAPLTC BCD*10.3 Cust. Unapplied Amount
  REMUNAPL BCD*10.3 Bank Unapplied Amount
  AMTRMITHC BCD*10.3 Func. Receipt Amount
  DOCNBR String*22 Document Number
  AMTADJHC BCD*10.3 Func. Adjustment Amount
  OPERBANK Integer Bank Rate Operator [1=Multiply,2=Divide]
  OPERCUST Integer Customer Rate Operator [1=Multiply,2=Divide]
  AMTDISCHC BCD*10.3 Total Func. Discount Amount
  AMTDBADJHC BCD*10.3 Total Func. Debit Amount
  AMTCRADJHC BCD*10.3 Total Func. Credit Amount
  AMTDBADJTC BCD*10.3 Total Cust. Debit Amount
  AMTCRADJTC BCD*10.3 Total Cust. Credit Amount
  SWJOB Integer Job Related [0=No,1=Yes]
  APPLYMETH Integer Job Apply Method [0=Prorate by Amount,1=Top Down]
  ERRBATCH Long Error Batch
  ERRENTRY Long Error Entry
  VALUES Long Optional Fields
  SRCEAPPL String*2 Source Application
  IDBANK String*8 Bank Code
  CODECURNBC String*3 Bank Currency Code
  DRILLAPP String*2 Drill Down Application Source
  DRILLTYPE Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  SWPRINTED Integer Receipt Printed [0=No,1=Yes]
  SWTXAMTCTL Integer Calculate Tax [0=No,1=Yes]
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
  DEPSEQ ??? Deposit Serial Number
  DEPLINE Long Deposit Line Number
  CODECURNRC String*3 Tax Reporting Currency Code
  SWTXCTLRC Integer Tax Reporting Calculate Method [0=No,1=Yes]
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
  CNTACC Long Number of Advance Credit Claims
  AMTACCTC BCD*10.3 Total Advance Credit Claim
  AMTACCHC BCD*10.3 Func. Total Advance Credit Claim
  AMTPAYMHC BCD*10.3 Func. Total Cust. Amount Applied
  REMUNAPLHC BCD*10.3 Func Cust. Unapplied Amount
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
  ARVERSION String*3 A/R Version Created In
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  IDACCTSET String*6 Account Set
  CCPREVID String*36 Previous C.C. Transaction Number
  CCPREVSTTS Integer Previous C.C. Process Status [0=SPS Transaction Not Started,1=SPS Sales Transaction Pending,2=SPS Sales Transaction Completed,7=SPS Void Transaction Pending,8=SPS Void Transaction Completed]
  CCTRANID String*36 Current C.C. Transaction Number
  CCTRANSTTS Integer Current C.C. Process Status [0=SPS Transaction Not Started,1=SPS Sales Transaction Pending,2=SPS Sales Transaction Completed,7=SPS Void Transaction Pending,8=SPS Void Transaction Completed]
  PROCESSCOD String*12 Processing Code
  AMTWHT1TC BCD*10.3 Estimated Tax Withheld Amount 1
  AMTWHT2TC BCD*10.3 Estimated Tax Withheld Amount 2
  AMTWHT3TC BCD*10.3 Estimated Tax Withheld Amount 3
  AMTWHT4TC BCD*10.3 Estimated Tax Withheld Amount 4
  AMTWHT5TC BCD*10.3 Estimated Tax Withheld Amount 5

## ARTCRO - Receipt/Adjustment Optional Fields (view AR0406)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPYMTYP+CNTBTCH+CNTITEM+OPTFIELD; OPTFIELD+CODEPYMTYP+CNTBTCH+CNTITEM
Fields (NAME type description [values]):
  CODEPYMTYP String*2 Batch Type
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

## ARTCT - Receipt Tax Withholdings (view AR0085)
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
  AMTWHDTC BCD*10.3 Customer Withheld Amount
  AMTWHDHC BCD*10.3 Functional Withheld Amount

## ARTCU - Adjustment G/L Distributions (view AR0045)
Keys (first = PK; D=dups allowed, M=modifiable): CODEPAYM+CNTBTCH+CNTITEM+CNTLINE+CNTSEQ
Fields (NAME type description [values]):
  CODEPAYM String*2 Batch Type
  CNTBTCH BCD*5.0 Batch Number
  CNTITEM BCD*4.0 Entry Number
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
  AMTDISC BCD*10.3 Discount Amount
  AMTPAYM BCD*10.3 Applied Amount
  IDITEM String*16 Item Number
  UNITMEAS String*10 Unit of Measure
  QTYINVC BCD*10.5 Quantity
  AMTCOST BCD*10.6 Cost
  BILLDATE Date Billing Date
  RTGAMT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  AMTDISTHC BCD*10.3 Func. Distribution Amount
  AMTDISCHC BCD*10.3 Func. Discount Amount
  AMTPAYMHC BCD*10.3 Func. Applied Amount
  RTGAMTHC BCD*10.3 Func. Retainage Amount
  TEXTDESC String*60 Description
  TEXTREF String*60 Reference
  DOCLINE BCD*3.0 Document Line Number
  AMTWHD1TC BCD*10.3 Cust. Tax Withheld Amount 1
  AMTWHD2TC BCD*10.3 Cust. Tax Withheld Amount 2
  AMTWHD3TC BCD*10.3 Cust. Tax Withheld Amount 3
  AMTWHD4TC BCD*10.3 Cust. Tax Withheld Amount 4
  AMTWHD5TC BCD*10.3 Cust. Tax Withheld Amount 5
  AMTWHD1HC BCD*10.3 Func. Tax Withheld Amount 1
  AMTWHD2HC BCD*10.3 Func. Tax Withheld Amount 2
  AMTWHD3HC BCD*10.3 Func. Tax Withheld Amount 3
  AMTWHD4HC BCD*10.3 Func. Tax Withheld Amount 4
  AMTWHD5HC BCD*10.3 Func. Tax Withheld Amount 5

## ARUNPSTD - Unposted Details (view AR0096)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+TRANSTYPE+CNTBTCH+CNTITEM+CNTLINE
Fields (NAME type description [values]):
  SELSEQ Long Sequence No.
  TRANSTYPE Integer Trans. Type [0=Invoice,1=Debit Note,2=Credit Note,3=Interest,4=Receipt,5=Prepayment,6=Unapplied Cash,7=Apply Document,8=Misc. Receipt,9=Refund,10=Adjustment,11=Write-off]
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  CNTLINE BCD*3.0 Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTREF String*60 Reference
  TEXTDESC String*60 Description
  IDINVC String*22 Document No.
  CNTPAYM BCD*3.0 Payment No.
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CATEGORY String*16 Category
  RESOURCE String*24 Resource
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  IDITEM String*16 Item No.
  IDDIST String*6 Dist. Code
  UNITMEAS String*10 Unit of Measure
  IDACCTREV String*45 Revenue Account
  IDACCTINV String*45 Inventory Account
  IDACCTCOGS String*45 COGS Account
  QTYINVC BCD*10.5 Qunatity
  TRANSAMT BCD*10.3 Trans. Amt.
  TRANSAMTHC BCD*10.3 Trans. Amt. (Home)
  TAXAMT BCD*10.3 Tax Amount
  TAXAMTHC BCD*10.3 Tax Amount (Home)
  RTGAMT BCD*10.3 Rtg. Amount
  RTGAMTHC BCD*10.3 Rtg. Amount (Home)

## ARUNPSTH - Unposted Entries (view AR0095)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+TRANSTYPE+CNTBTCH+CNTITEM; SELSEQ+IDCUST+IDNATACCT+TRANSTYPE+CNTBTCH+CNTITEM [D,M]; SELSEQ+DATETRANS+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+DATETRANS+TRANSTYPE [D,M]; SELSEQ+ORDRNBR+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+ORDRNBR+TRANSTYPE [D,M]; SELSEQ+CUSTPO+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+CUSTPO+TRANSTYPE [D,M]; SELSEQ+SHIPNBR+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+SHIPNBR+TRANSTYPE [D,M]; SELSEQ+IDRMIT+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+IDRMIT+TRANSTYPE [D,M]; SELSEQ+IDINVC+TRANSTYPE [D,M]; SELSEQ+IDCUST+IDNATACCT+IDINVC+TRANSTYPE [D,M]
Fields (NAME type description [values]):
  SELSEQ Long Sequence No.
  TRANSTYPE Integer Trans. Type [0=Invoice,1=Debit Note,2=Credit Note,3=Interest,4=Receipt,5=Prepayment,6=Unapplied Cash,7=Apply Document,8=Misc. Receipt,9=Refund,10=Adjustment,11=Write-off]
  CNTBTCH BCD*5.0 Batch No.
  CNTITEM BCD*4.0 Entry No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BATCHSTAT Integer Batch Status [0=Open,1=Ready To Post,2=Post In Progress,3=Check Creation In Progress]
  SRCEAPPL String*2 Source Application
  ENTEREDBY String*8 Entered By
  TEXTREF String*60 Reference
  TEXTDESC String*60 Description
  IDCUST String*12 Customer No.
  IDNATACCT String*12 National Account
  IDINVC String*22 Document No.
  APPLYBY Integer Apply By [0=(None),1=Document No.,2=PO No.,3=Order No.,4=Shipment No.]
  INVCAPPLTO String*22 Apply To
  RTGAPPLYTO String*22 Original Doc. No.
  ORDRNBR String*22 Order No.
  CUSTPO String*22 PO Number
  SHIPNBR String*22 Shipment No.
  IDRMIT String*24 Check/Receipt No.
  PAYER String*60 Payer
  DATETRANS Date Trans. Date
  DATEBUS Date Posting Date
  FISCYR String*4 Fiscal Year
  FISCPER String*2 Fiscal Period
  SWJOB Integer Job Related [0=No,1=Yes]
  SWITEM Integer Has Item [0=No,1=Yes]
  SWRTG Integer Has Retainage [0=No,1=Yes]
  CODECURN String*3 Trans. Currency
  EXCHRATEHC BCD*8.7 Exchange Rate
  TRANSAMT BCD*10.3 Trans. Amt.
  TRANSAMTHC BCD*10.3 Trans. Amt. (Home)
  TAXAMT BCD*10.3 Tax Amt.
  TAXAMTHC BCD*10.3 Tax Amt. (Home)
  ADVAMT BCD*10.3 Prepay/Advance Amt.
  ADVAMTHC BCD*10.3 Prepay/Advance Amt. (Home)
  RTGAMT BCD*10.3 Rtg. Amt
  RTGAMTHC BCD*10.3 Rtg. Amt. (Home)
  UNAPLAMT BCD*10.3 Unapplied Amt.
  UNAPLAMTHC BCD*10.3 Unapplied Amt. (Home)

## ARURC - Update Recurring Chrgs Instrns (view AR0081)
Keys (first = PK; D=dups allowed, M=modifiable): CNTNUM
Fields (NAME type description [values]):
  CNTNUM Long Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCCODE String*16 Recurring Charge Code
  IDCUSTFR String*12 From Customer Number
  IDCUSTTO String*12 To Customer Number
  CHANGEBY Integer Change By Percentage Or Amount? [1=Percentage,2=Amount]
  INCDEC Integer Increase Or Decrease RC Value? [1=Increase,2=Decrease]
  CODECURN String*3 Customer Currency
  PCTCHANGE BCD*5.5 Percentage To Change By
  AMTCHANGE BCD*10.3 Money Amount To Change By
  DISTMETHOD Integer Money Distribution Method [1=All Details,2=Specific Distribution Code]
  IDDISTCODE String*6 Distribution Code
  PCTMAXCHG BCD*5.5 Percent To Change Max Amount By
  AMTMAXCHG BCD*10.3 Amount To Change Max. Amount By
  PROCESSED Integer Has Instruction Been Processed? [0=No,1=Yes]
  NUMSIARECS Long Number of RC Records Processed
