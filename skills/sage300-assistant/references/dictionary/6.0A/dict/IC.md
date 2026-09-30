# IC module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## ICACCT - Account Sets (view IC0100)
Keys (first = PK; D=dups allowed, M=modifiable): CNTLACCT
Fields (NAME type description [values]):
  CNTLACCT String*6 Account Set Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  COSTMETHOD Integer Costing Method [1=Moving Average,2=FIFO,3=LIFO,4=Standard Cost,5=Most Recent Cost,6=User-Specified,7=Serial,8=Lot]
  INVACCT String*45 Inventory Control Account
  PAYABLACCT String*45 Payables Clearing Account
  ADJWRTACCT String*45 Adjustment/Write-Off Account
  ASSMACCT String*45 Assembly Cost Credit Account
  NONSTKACCT String*45 Non-stock Clearing Account
  INACTIVE Boolean Status [0=Active,1=Inactive]
  DATELASTMN Date Date Last Maintained
  DATEINACTV Date Date Inactive
  TRANSACCT String*45 Transfer Clearing Account
  SHIPACCT String*45 Shipment Clearing Account
  DISEXPACCT String*45 Disassembly Expense Account
  PHINVAACCT String*45 Physical Inventory Adj. Acct.
  CRNCLRACCT String*45 Credit/Debit Note Clearing Acct.

## ICADED - Adjustment Details (view IC0110)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ+LINENO
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  LOCATION String*6 Location
  TRANSTYPE Integer Transaction Type [1=Quantity Increase,2=Quantity Decrease,3=Cost Increase,4=Cost Decrease,5=Both Increase,6=Both Decrease]
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  EXTCOST BCD*10.3 Cost Adjustment
  COMMENTS String*250 Comments
  WOFFACCT String*45 Adjustment/Write-Off Account
  ORIGACCT String*45 Original Write-Off Account
  COSTMETHOD Integer Costing Method
  MDALLOCATE Integer Bucket Type [1=Offset Bucket,2=Specific Bucket,3=Prorate]
  RECEIPT String*22 Document Number
  COSTDATE Date Cost Date
  COSTSEQNUM Long Costing Sequence Number
  STOCKITEM Boolean Stock Item
  MANITEMNO String*24 Manufacturer's Item Number
  DETAILNUM Integer Detail Line Number
  PMCONTRACT String*16 P/M Contract
  PMPROJECT String*16 P/M Project
  PMCATEGORY String*16 P/M Category
  PMOHACCT String*45 P/M Overhead Account
  PMOHAMT BCD*10.3 P/M Overhead Amount
  VALUES Long Optional Fields
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Lot Quantity
  SERIALCOST BCD*10.3 Serials' Cost
  LOTCOST BCD*10.3 Lots' Cost

## ICADEDL - Adjustment Detail Lot Numbers (view IC0113)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ+LINENO+LOTNUMF; LOTNUMF+ADJENSEQ+LINENO
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  COST BCD*10.3 Lot Cost

## ICADEDO - Adjustment Detail Opt. Fields (view IC0115)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ+LINENO+OPTFIELD; OPTFIELD+ADJENSEQ+LINENO
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
  LINENO Integer Line Number
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

## ICADEDS - Adjustment Detail Serial Numbers (view IC0117)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ+LINENO+SERIALNUMF; SERIALNUMF+ADJENSEQ+LINENO
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COST BCD*10.3 Serial Cost

## ICADEH - Adjustment Headers (view IC0120)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ; TRANSNUM [M]; STATUS+TRANSNUM [M]; DOCNUM; DOCUNIQ [D,M]; STATUS+DOCNUM [M]
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  DOCNUM String*22 Adjustment Number
  HDRDESC String*60 Description
  TRANSDATE Date Adjustment Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  REFERENCE String*60 Reference
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  DELETED Boolean Record Deleted [0=No,1=Yes]
  NEXTDTLNUM Integer Next Detail Line Number
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  JOBCOST Boolean Job Related [0=No,1=Yes]
  PMADJUSTNO String*16 P/M Adjustment Number
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## ICADEHO - Adjustment Header Opt. Fields (view IC0125)
Keys (first = PK; D=dups allowed, M=modifiable): ADJENSEQ+OPTFIELD; OPTFIELD+ADJENSEQ
Fields (NAME type description [values]):
  ADJENSEQ Long Sequence Number
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

## ICADJD - Adjustment Audit List Details (view IC0130)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type [1=Quantity Increase,2=Quantity Decrease,3=Cost Increase,4=Cost Decrease,5=Both Increase,6=Both Decrease]
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  QTY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  COST BCD*10.3 Extended Cost
  COMMENTS String*250 Comments
  ADJACCT String*45 Adjustment/Write-Off Account
  ICACCT String*45 Inventory Control Account
  RECPNUM String*22 Document Number
  BUCKETTYPE Integer Bucket Type [1=Offset Bucket,2=Specific Bucket,3=Prorate]
  PMCONTRACT String*16 P/M Contract
  PMPROJECT String*16 P/M Project
  PMCATEGORY String*16 P/M Category
  PMOHACCT String*45 P/M Overhead Account
  PMOHAMT BCD*10.3 P/M Overhead Amount
  VALUES Long Optional Fields

## ICADJDP - Adj. Audit List Det. Opt. Fields (view IC0131)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICADJH - Adjustment Audit List Headers (view IC0132)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; DOCNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  DOCNUM String*22 Adjustment Number
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  HDRDESC String*60 Description
  PRINTED Boolean Printed
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICADJHP - Adj. Audit List Hdr Opt. Fields (view IC0135)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICASCST - Assembly Component Costs (view IC0150)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+LINENO; DOCNUM+LINENO+ITEMNO+UNIT
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Unformatted Item Number
  UNITCOST BCD*10.6 Unit Cost
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  QUANTITY BCD*10.4 Quantity
  ASSMENSEQ Long Sequence Number
  COMPID Long Component ID
  PRNCOMPID Long Parent Component ID

## ICASEN - Assemblies (view IC0160)
Keys (first = PK; D=dups allowed, M=modifiable): ASSMENSEQ; TRANSNUM [M]; TRANSTYPE+ASSMENSEQ [M]; TRANSTYPE+DOCNUM [M]; STATUS+TRANSNUM [M]; DOCNUM; DOCUNIQ [D,M]; STATUS+DOCNUM [M]; MASTASSNUM+DOCNUM [M]; MASTASSNUM+MULTSEQ [D,M]
Fields (NAME type description [values]):
  ASSMENSEQ Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  DOCNUM String*22 Assembly Number
  TRANSDATE Date Transaction Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  REFERENCE String*60 Reference
  HDRDESC String*60 Description
  ITEMNO String*24 Item Number
  BOMNO String*6 BOM Number
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  TRANSTYPE Integer Transaction Type [1=Assembly,2=Disassembly]
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  DELETED Boolean Record Deleted [0=No,1=Yes]
  MANITEMNO String*24 Manufacturer's Item Number
  UNITCOST BCD*10.6 Unit Cost
  FROMASSNUM String*22 From Assembly Number
  FROMASSQTY BCD*10.4 From Assembly Quantity
  DISASSCOST BCD*10.3 Disassembly Cost
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  MASTASSNUM String*22 Master Assembly Number
  COMPASSMTD Integer Component Assembly Method [0=None,1=All Component Master Items,2=Component Master Items with Insufficient Quantity]
  USEDQTY BCD*10.4 Quantity Used
  NEEDQTYSTK BCD*10.4 Qty Needed (Stocking UOM)
  MULTLEVEL Integer Multilevel Level
  MULTSEQ Long Multilevel Seq. No.
  PRNMULTSEQ Long Multilevel Parent Seq. No.
  PRNASSNUM String*22 Multilevel Parent Assembly No.
  CMPMASTITM String*24 Component's Master Item No.
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  SITEMCOUNT Long Serial Items in Assembly
  LITEMCOUNT Long Lot Items in Assembly
  REMAINASSD BCD*10.4 Assembly Quantity Remaining

## ICASENL - Assembly Lot Details (view IC0162)
Keys (first = PK; D=dups allowed, M=modifiable): ASSMENSEQ+COMPID+PRNCOMPID+LOTNUMF; ASSMENSEQ+PRNCOMPID+COMPID+LOTNUMF; ASSMENSEQ+PRNLOTNUMF+COMPID+LOTNUMF [M]
Fields (NAME type description [values]):
  ASSMENSEQ Long Sequence Number
  COMPID Long Component ID
  PRNCOMPID Long Parent Component ID
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRNLOTNUMF String*40 Master Item Lot Number
  ITEMNO String*24 Item Number
  BOMNO String*6 BOM Number
  UNIT String*10 Unit of Measure
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM

## ICASENO - Assembly Optional Fields (view IC0165)
Keys (first = PK; D=dups allowed, M=modifiable): ASSMENSEQ+OPTFIELD; OPTFIELD+ASSMENSEQ
Fields (NAME type description [values]):
  ASSMENSEQ Long Sequence Number
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

## ICASENS - Assembly Serial Details (view IC0167)
Keys (first = PK; D=dups allowed, M=modifiable): ASSMENSEQ+COMPID+PRNCOMPID+SERIALNUMF; ASSMENSEQ+PRNCOMPID+COMPID+SERIALNUMF; ASSMENSEQ+PRNSERNUMF+COMPID+SERIALNUMF [M]
Fields (NAME type description [values]):
  ASSMENSEQ Long Sequence Number
  COMPID Long Component ID
  PRNCOMPID Long Parent Component ID
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRNSERNUMF String*40 Master Item Serial Number
  ITEMNO String*24 Item Number
  BOMNO String*6 BOM Number
  UNIT String*10 Unit of Measure

## ICASMDP - Asm Audit List Dtl Opt. Fields (view IC0170)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICASMHP - Asm Audit List Hdr Opt. Fields (view IC0172)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICASSMD - Assembly Audit List Details (view IC0180)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type [1=Master Item,2=Component Item]
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  BUILDQTY BCD*10.4 Build Quantity
  BUILDUNIT String*10 Unit of Measure
  BUILDCONV BCD*10.6 Conversion Factor
  STOCKQTY BCD*10.4 Stock Quantity
  STOCKUNIT String*10 Stocking Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  BUILDCOST BCD*10.3 Extended Cost
  VARBLCOST BCD*10.3 Variable Cost
  FIXEDCOST BCD*10.3 Fixed Cost
  ICACCT String*45 Inventory Control Account
  ASSMACCT String*45 Assembly Cost Credit Account
  COSTUNIT String*10 Costing Unit of Measure
  DISASSCOST BCD*10.3 Disassembly Cost
  DISEXPACCT String*45 Disassembly Expense Account
  VALUES Long Optional Fields

## ICASSMH - Assembly Audit List Headers (view IC0182)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; DOCNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  BOMNO String*6 BOM Number
  DOCNUM String*22 Assembly Number
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  LOCATION String*6 Location
  HDRDESC String*60 Description
  PRINTED Boolean Printed
  TRANSTYPE Integer Transaction Type
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICBOMD - Bills of Material Components (view IC0190)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+BOMNO+LINENO; COMPONENT [D,M]; COMPONENT+COMPBOMNO [D,M]; COMPONENT+ITEMNO+BOMNO+LINENO [D,M]
Fields (NAME type description [values]):
  ITEMNO String*24 Master Item Number
  BOMNO String*6 BOM Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item Number
  QTY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COMPBOMNO String*6 Component BOM Number
  COPYDETAIL Boolean Copy Detail [0=No,1=Yes]

## ICBOMH - Bills of Material (view IC0200)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+BOMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Unformatted Item Number
  BOMNO String*6 BOM Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REMARK String*80 Comments
  FIXEDCOST BCD*10.3 Fixed Cost
  BUILDQTY BCD*10.4 Build Quantity
  UNIT String*10 Unit of Measure
  VARBLCOST BCD*10.3 Variable Cost
  DESC String*60 Description
  STARTDATE Date Start Date
  ENDDATE Date End Date
  INACTIVE Boolean Status [0=Active,1=Inactive]
  DATEINACTV Date Date Inactive

## ICCATG - Categories (view IC0210)
Keys (first = PK; D=dups allowed, M=modifiable): CATEGORY
Fields (NAME type description [values]):
  CATEGORY String*6 Category Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  COGSACCT String*45 Cost of Goods Sold Account
  REVENUACCT String*45 Sales Account
  RETURNACCT String*45 Returns Account
  VARIANACCT String*45 Cost Variance Account
  COMMSNPAID Boolean Commission Paid [0=No,1=Yes]
  COMMSNRATE BCD*5.5 Commission Rate
  INACTIVE Boolean Status [0=Active,1=Inactive]
  DATELASTMN Date Date Last Maintained
  DEFPRICLST String*6 Default Price List Code
  DATEINACTV Date Date Inactive
  DAMAGEACCT String*45 Damaged Goods Account
  ICSEXPACCT String*45 Internal Usage Account

## ICCATTX - Category Tax Authorities (view IC0220)
Keys (first = PK; D=dups allowed, M=modifiable): CATEGORY+AUTHORITY
Fields (NAME type description [values]):
  CATEGORY String*6 Category
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PURCHTAXCL Integer Purchase Tax Class
  SALESTAXCL Integer Sales Tax Class

## ICCOST - Receipt Cost (view IC0260)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION+TRANSDATE+SEQUENCE; ITEMNO+LOCATION+RECEIPTNUM+TRANSDATE+SEQUENCE [D]; RECEIPTNUM+LINENUMBER+ITEMNO+LOCATION+TRANSDATE+SEQUENCE [D]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  TRANSDATE Date Transaction Date
  SEQUENCE Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REFERENCE String*60 Reference
  RECEIPTNUM String*22 Document Number
  LINENUMBER Integer Line Number
  QTY BCD*10.4 Original Quantity
  COST BCD*10.3 Original Cost
  SHIPQTY BCD*10.4 Quantity Shipped
  SHIPCOST BCD*10.3 Shipped Cost

## ICCUPR - Contract Pricing (view IC0274)
Keys (first = PK; D=dups allowed, M=modifiable): CUSTNO+PRICEBY+CATEGORY+ITEMNO+PRICELIST; PRICEBY+ITEMNO+CATEGORY+CUSTNO+PRICELIST [D,M]; ITEMNO+PRICEBY+CUSTNO+PRICELIST [D,M]; CATEGORY+PRICEBY+CUSTNO [D,M]
Fields (NAME type description [values]):
  CUSTNO String*12 Customer Number
  PRICEBY Integer Price By [1=Category Code,2=Item Number]
  CATEGORY String*6 Category Code
  ITEMNO String*24 Item Number
  PRICELIST String*6 Price List
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRE Date Expiration Date
  PRICETYPE Integer Price Type [1=Customer Type,2=Discount Percentage,3=Discount Amount,4=Cost Plus a Percentage,5=Cost Plus Fixed Amount,6=Fixed Price]
  CUSTTYPE Integer Customer Type [1=Base,2=A,3=B,4=C,5=D,6=E]
  DISCPER BCD*5.5 Discount Percentage
  DISCAMT BCD*10.6 Discount Amount
  COSTMETHOD Integer Costing Method [1=Markup Cost,2=Standard Cost,3=Most Recent Cost,4=Average Cost,5=Last Unit Cost]
  PLUSAMT BCD*10.6 Plus Amount
  PLUSPER BCD*5.5 Plus Percentage
  FIXPRICE BCD*10.6 Fixed Price
  STARTDATE Date Start Date
  USELOWEST Boolean Use Lowest Price [0=No,1=Yes]

## ICGLREF - G/L Reference Integration (view IC0281)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [100=Receipt,101=Receipt Detail,200=Shipment,201=Shipment Detail,300=Adjustment,301=Adjustment Detail,400=Transfer,401=Transfer Detail,500=Assemblies,600=Internal Usage,601=Internal Usage Detail]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description,1=G/L Detail Reference,2=G/L Detail Description,3=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5=( Left Parenthesis,6=) Right Parenthesis,7=# Number Sign,8=  Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Adjustment Number,2=Adjustment Type,3=Assembly Number,4=BOM Number,5=Category,6=Comment,7=Contact Name,8=Contract,9=Customer Name,10=Customer Number,11=Day End Number,12=Description,13=Detail Description,34=Document Number,14=Document Type,15=Entry Number,16=Entry Type,17=From Location,18=From Location Name,19=GIT Location,20=GIT Location Name,21=Item Number,22=Location,23=Location Name,24=Manufacturer's Item Number,25=Purchase Order Number,26=Project,27=Receipt Number,28=Reference,29=Shipment Number,30=Source Code,31=To Location,32=To Location Name,33=Transaction Type,35=Unformatted Item Number,36=Vendor Name,37=Vendor Number,38=Category,39=Internal Usage Number]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Adjustment Number,2=Adjustment Type,3=Assembly Number,4=BOM Number,5=Category,6=Comment,7=Contact Name,8=Contract,9=Customer Name,10=Customer Number,11=Day End Number,12=Description,13=Detail Description,34=Document Number,14=Document Type,15=Entry Number,16=Entry Type,17=From Location,18=From Location Name,19=GIT Location,20=GIT Location Name,21=Item Number,22=Location,23=Location Name,24=Manufacturer's Item Number,25=Purchase Order Number,26=Project,27=Receipt Number,28=Reference,29=Shipment Number,30=Source Code,31=To Location,32=To Location Name,33=Transaction Type,35=Unformatted Item Number,36=Vendor Name,37=Vendor Number,38=Category,39=Internal Usage Number]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Adjustment Number,2=Adjustment Type,3=Assembly Number,4=BOM Number,5=Category,6=Comment,7=Contact Name,8=Contract,9=Customer Name,10=Customer Number,11=Day End Number,12=Description,13=Detail Description,34=Document Number,14=Document Type,15=Entry Number,16=Entry Type,17=From Location,18=From Location Name,19=GIT Location,20=GIT Location Name,21=Item Number,22=Location,23=Location Name,24=Manufacturer's Item Number,25=Purchase Order Number,26=Project,27=Receipt Number,28=Reference,29=Shipment Number,30=Source Code,31=To Location,32=To Location Name,33=Transaction Type,35=Unformatted Item Number,36=Vendor Name,37=Vendor Number,38=Category,39=Internal Usage Number]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Adjustment Number,2=Adjustment Type,3=Assembly Number,4=BOM Number,5=Category,6=Comment,7=Contact Name,8=Contract,9=Customer Name,10=Customer Number,11=Day End Number,12=Description,13=Detail Description,34=Document Number,14=Document Type,15=Entry Number,16=Entry Type,17=From Location,18=From Location Name,19=GIT Location,20=GIT Location Name,21=Item Number,22=Location,23=Location Name,24=Manufacturer's Item Number,25=Purchase Order Number,26=Project,27=Receipt Number,28=Reference,29=Shipment Number,30=Source Code,31=To Location,32=To Location Name,33=Transaction Type,35=Unformatted Item Number,36=Vendor Name,37=Vendor Number,38=Category,39=Internal Usage Number]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Adjustment Number,2=Adjustment Type,3=Assembly Number,4=BOM Number,5=Category,6=Comment,7=Contact Name,8=Contract,9=Customer Name,10=Customer Number,11=Day End Number,12=Description,13=Detail Description,34=Document Number,14=Document Type,15=Entry Number,16=Entry Type,17=From Location,18=From Location Name,19=GIT Location,20=GIT Location Name,21=Item Number,22=Location,23=Location Name,24=Manufacturer's Item Number,25=Purchase Order Number,26=Project,27=Receipt Number,28=Reference,29=Shipment Number,30=Source Code,31=To Location,32=To Location Name,33=Transaction Type,35=Unformatted Item Number,36=Vendor Name,37=Vendor Number,38=Category,39=Internal Usage Number]

## ICHIST - Transaction History (view IC0280)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTSET+LOCATION+ITEMNO+FISCYEAR+FISCPERIOD+TRANSDATE+DAYENDSEQ+ENTRYSEQ+LINENO; ITEMNO+ACCTSET+LOCATION+FISCYEAR+FISCPERIOD [D]; LOCATION+ACCTSET+ITEMNO+FISCYEAR+FISCPERIOD [D]; DAYENDSEQ+ENTRYSEQ+LINENO [D,M]; ITEMNO+LOCATION+FISCYEAR+FISCPERIOD [D,M]; DOCNUM+ITEMNO+LOCATION+TRANSTYPE [D,M]
Fields (NAME type description [values]):
  ACCTSET String*6 Account Set Code
  LOCATION String*6 Location
  ITEMNO String*24 Item Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSDATE Date Transaction Date
  DAYENDSEQ Long Day End Number
  ENTRYSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY String*6 Category
  DOCNUM String*22 Document Number
  APP String*2 Source Application
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,3=Receipt Return,4=Shipment,5=Shipment Return,6=Adjustment Quantity Increase,7=Adjustment Quantity Decrease,8=Adjustment Cost Increase,9=Adjustment Cost Decrease,10=Adjustment Both Increase,11=Adjustment Both Decrease,12=Stock Transfer From,13=Stock Transfer To,14=Master Item Assembly,15=Component Item Assembly,16=Invoice,17=Credit Note,18=Debit Note,19=Shipment Adjustment,20=Internal Usage]
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  SRCCURR String*3 Source Currency
  EXRATE BCD*8.7 Exchange Rate
  SRCEXTCST BCD*10.3 Extended Cost - Source
  HOMEEXTCST BCD*10.3 Extended Cost - Functional
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  DRILAPP String*2 Drill Down Application Source
  JOBNO String*24
  DETAILNUM Integer Detail Number
  COMPNUM Long Detail Component Number
  DATEBUS Date Posting Date

## ICICED - Internal Usage Details (view IC0286)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  UNITCOST BCD*10.6 Unit Cost
  EXTCOST BCD*10.3 Extended Cost
  SERIALNO Boolean Serial Numbers
  COMMENTS String*250 Comments
  MANITEMNO String*24 Manufacturer's Item Number
  VALUES Long Optional Fields
  DETAILNUM Integer Detail Line Number
  GLACCT String*45 GL Account
  EMPLOYEENO String*60 Employee Number
  FASDETAIL Boolean FAS Attached [0=No,1=Yes]
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Lot Quantity

## ICICEDA - Internal Usage FAS Details (view IC0283)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+DETAILNUM
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  DETAILNUM Integer Detail Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FASDB String*32 Database
  FASCMP String*32 Company
  FASTMPL String*25 Template
  TEXTDESC String*80 Asset Description
  SEPQTY Boolean Separate Quantities [0=No,1=Yes]
  QUANTITY BCD*10.5 Quantity
  UOM String*10 Unit of Measure
  AMTHC BCD*10.3 Amount

## ICICEDL - Internal Usage Lot Numbers (view IC0282)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+LOTNUMF; LOTNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM

## ICICEDO - Internal Usage Detail Optional Fields (view IC0287)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+OPTFIELD; OPTFIELD+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
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

## ICICEDS - Internal Usage Serial Numbers (view IC0284)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+SERIALNUMF; SERIALNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ICICEH - Internal Usage Headers (view IC0288)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; TRANSNUM [M]; STATUS+TRANSNUM [M]; DOCNUM; DOCUNIQ [D,M]; STATUS+DOCNUM [M]
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  DOCNUM String*22 Internal Usage Number
  HDRDESC String*60 Description
  TRANSTYPE Integer Entry Type [1=Internal Usage,2=Return]
  TRANSDATE Date Internal Usage Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  REFERENCE String*60 Reference
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  NEXTDTLNUM Integer Next Detail Line Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  DELETED Boolean Record Deleted [0=No,1=Yes]
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  EMPLOYEENO String*60 Employee Number
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## ICICEHO - Internal Usage Optional Fields (view IC0289)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
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

## ICILOC - Location Details (view IC0290)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION; LOCATION+ITEMNO; LASTSERALC+ITEMNO+LOCATION [M]; LASTLOTALC+ITEMNO+LOCATION [M]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PICKINGSEQ String*10 Picking Sequence
  ACTIVE Boolean Allowed [0=No,1=Yes]
  DATEACTIVE Date Date Location Activated
  USED Boolean In Use [0=No,1=Yes]
  LASTUSED Date Date Last Used
  QTYONHAND BCD*10.4 Quantity on Hand (Last Day End)
  QTYONORDER BCD*10.4 Quantity on P/O
  QTYSALORDR BCD*10.4 Quantity on S/O
  QTYOFFSET BCD*10.4 Quantity Not in Cost File
  QTYSHNOCST BCD*10.4 Quantity Shipped Not Costed
  QTYRENOCST BCD*10.4 Quantity Received Not Costed
  QTYADNOCST BCD*10.4 Quantity Adjusted Not Costed
  NUMNOCST Long Number of Uncosted Transactions
  TOTALCOST BCD*10.3 Total Cost
  COSTOFFSET BCD*10.3 Cost Not in Cost File
  COSTUNIT String*10 Cost Unit of Measure
  COSTCONV BCD*10.6 Cost Unit Conversion Factor
  STDCOST BCD*10.6 Standard Cost
  LASTSTDCST BCD*10.6 Last Standard Cost
  LASTSTDDAT Date Last Standard Cost Date
  LASTSHIPDT Date Last Shipment Date
  DAYSTOSHIP BCD*10.4 Average Days To Ship
  UNITSSHIP BCD*10.4 Average Units Shipped
  SHIPMENTS Integer Shipments Used In Calculation
  LASTRCPTDT Date Last Receipt Date
  RECENTCOST BCD*10.6 Most Recent Cost
  COST1 BCD*10.6 User Defined Cost 1
  COST2 BCD*10.6 User Defined Cost 2
  LASTCOST BCD*10.6 Last Unit Cost
  QTYCOMMIT BCD*10.4 Quantity Committed
  LASTSERALC String*70 Last Allocated Serial
  LASTLOTALC String*70 Last Allocated Lot

## ICINCAD - Internal Usage Audit List Details (view IC0301)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  STOCKQTY BCD*10.4 Quantity in Stocking Unit
  STOCKUNIT String*10 Stocking Unit of Measure
  UNITCOST BCD*10.6 User-Specified Cost
  EXTCOST BCD*10.3 Extended Cost
  VARIANCE BCD*10.3 Variance
  COMMENTS String*250 Comments
  EMPLOYEENO String*60 Used By
  STOCKITEM Boolean Stock Item
  ICSEXPACCT String*45 Consumable Expense Account
  VARACCT String*45 Cost Variance Account
  ICACCT String*45 Inventory Control Account
  VALUES Long Optional Fields
  PMCONTRACT String*16 P/M Contract
  PMPROJECT String*16 P/M Project
  PMCATEGORY String*16 P/M Category
  PMDETAIL Long P/M Detail
  PMOHACCT String*45 P/M Overhead Account
  PMOHAMT BCD*10.3 P/M Overhead Amount

## ICINCAH - Internal Usage Audit List Headers (view IC0302)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; DOCNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  DOCNUM String*22 Internal Usage Number
  TRANSDATE Date Transaction Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  REFERENCE String*60 Reference
  HDRDESC String*60 Description
  EMPLOYEENO String*60 Used By
  PRINTED Boolean Printed
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICINCDP - Int. Usage Audit List Det. Opt. Flds (view IC0303)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICINCHP - Int. Usage Audit List Hdr Opt. Flds (view IC0304)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICIOTH - Manufacturer's Item Number (view IC0305)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+MANITEMNO; MANITEMNO+ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Unformatted Item Number
  MANITEMNO String*24 Manufacturer's Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Manufacturer's Item Description
  UNIT String*10 Unit of Measure
  COMMENT String*250 Comments

## ICITEM - Items (view IC0310)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO; CATEGORY+ITEMNO [M]; ALTSET+ITEMNO [M]; FMTITEMNO; DESC+ITEMNO [M]; ALLOWONWEB+ITEMNO [M]
Fields (NAME type description [values]):
  ITEMNO String*24 Unformatted Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ALTSET Long Alternate Item Set Number
  DESC String*60 Description
  DATELASTMN Date Date Last Maintained
  INACTIVE Boolean Status [0=Active,1=Inactive]
  ITEMBRKID String*6 Structure Code
  FMTITEMNO String*24 Item Number
  CATEGORY String*6 Category
  CNTLACCT String*6 Account Set Code
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  STOCKUNIT String*10 Stocking Unit of Measure
  DEFPRICLST String*6 Default Price List Code
  UNITWGT BCD*10.4 Unit Weight
  PICKINGSEQ String*10 Default Picking Sequence
  SERIALNO Boolean Serial Numbers [0=No,1=Yes]
  COMMODIM String*16 Commodity Number
  DATEINACTV Date Date Inactive
  SEGMENT1 String*24 Segment 1
  SEGMENT2 String*24 Segment 2
  SEGMENT3 String*24 Segment 3
  SEGMENT4 String*24 Segment 4
  SEGMENT5 String*24 Segment 5
  SEGMENT6 String*24 Segment 6
  SEGMENT7 String*24 Segment 7
  SEGMENT8 String*24 Segment 8
  SEGMENT9 String*24 Segment 9
  SEGMENT10 String*24 Segment 10
  COMMENT1 String*80 Comment 1
  COMMENT2 String*80 Comment 2
  COMMENT3 String*80 Comment 3
  COMMENT4 String*80 Comment 4
  ALLOWONWEB Boolean Allow Item in Web Store [0=No,1=Yes]
  KITTING Boolean Kitting Item [0=No,1=Yes]
  VALUES Long Optional Fields
  DEFKITNO String*6 Default Kit Number
  SELLABLE Boolean Sellable [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  SERIALMASK String*6 Serial Number Mask
  NEXTSERFMT String*40 Next Serial Number
  SUSEEXPDAY Boolean Use Serials Days to Expire [0=No,1=Yes]
  SEXPDAYS Integer Serials Days to Expire
  SDIFQTYOK Boolean Allow Different Serial Qty [0=No,1=Yes]
  SVALUES Long Serials Optional Fields
  SWARYCODE String*6 Default Serial Warranty Code
  SCONTCODE String*6 Default Serial Contract Code
  SCONTRECE Boolean Serial is on Cont. When Received [0=No,1=Yes]
  SWARYSOLD Boolean Serial is on Warr.When Sold [0=No,1=Yes]
  SWARYREG Boolean Serial is on Warr. When Registered [0=No,1=Yes]
  LOTITEM Boolean Lot Numbers [0=No,1=Yes]
  LOTMASK String*6 Lot Number Mask
  NEXTLOTFMT String*40 Next Lot Number
  LUSEEXPDAY Boolean Use Lots Days to Expire [0=No,1=Yes]
  LEXPDAYS Integer Lots Days to Expire
  LUSEQRNDAY Boolean Use Lots Days on Quarantine [0=No,1=Yes]
  LQRNDAYS Integer Lots Days on Quarantine
  LDIFQTYOK Boolean Allow Different Lot Qty [0=No,1=Yes]
  LVALUES Long Lots Optional Fields
  LWARYCODE String*6 Default Lot Warranty Code
  LCONTCODE String*6 Default Lot Contract Code
  LCONTRECE Boolean Lot is on Cont. When Received [0=No,1=Yes]
  LWARYSOLD Boolean Lot is on Warr.When Sold [0=No,1=Yes]

## ICITEMLO - Item Lot Optional Fields (view IC0312)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+OPTFIELD; OPTFIELD+ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
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

## ICITEMO - Item Optional Fields (view IC0313)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+OPTFIELD; OPTFIELD+ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
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

## ICITEMSO - Item Serial Optional Fields (view IC0314)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+OPTFIELD; OPTFIELD+ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
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

## ICITMAP - Item Mappings (view IC0315)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMPLUS; BLANK2000+ITM2000DUP [M]
Fields (NAME type description [values]):
  ITEMPLUS String*16 Non-Sage Accpac Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STRUCT2000 String*6 Sage Accpac Item Structure
  ITEM2000 String*24 Sage Accpac Item Number
  DESCPLUS String*40 Non-Sage Accpac Item Desc.
  BLANK2000 Boolean Item Structure and Number Blank?
  ITM2000DUP String*24 Unformatted Item Number

## ICITMC - Customer Item Numbers (view IC0319)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+CUSTNO; CUSTNO+CITEMNO [M]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  CUSTNO String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTNAME String*60 Customer Name
  CITEMNO String*24 Customer's Item Number
  CITEMDESC String*60 Customer's Item Description
  UNIT String*10 Unit of Measure
  COMMENT String*80 Comments
  INSTRUCTIO String*80 Instructions

## ICITMS - Item Structures (view IC0320)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMBRKID
Fields (NAME type description [values]):
  ITEMBRKID String*6 Structure Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  DELIM0 Integer Prefix [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT1 Integer Segment 1
  DELIM1 Integer Segment Separator 1 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT2 Integer Segment 2
  DELIM2 Integer Segment Separator 2 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT3 Integer Segment 3
  DELIM3 Integer Segment Separator 3 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT4 Integer Segment 4
  DELIM4 Integer Segment Separator 4 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT5 Integer Segment 5
  DELIM5 Integer Segment Separator 5 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT6 Integer Segment 6
  DELIM6 Integer Segment Separator 6 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT7 Integer Segment 7
  DELIM7 Integer Segment Separator 7 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT8 Integer Segment 8
  DELIM8 Integer Segment Separator 8 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT9 Integer Segment 9
  DELIM9 Integer Segment Separator 9 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]
  SEGMENT10 Integer Segment 10
  DELIM10 Integer Segment Separator 10 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign]

## ICITMTX - Item Tax Authorities (view IC0330)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+AUTHORITY
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PURCHTAXCL Integer Purchase Tax Class
  SALESTAXCL Integer Sales Tax Class

## ICITMV - Vendor Item Numbers (view IC0340)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+VENDTYPE; VENDTYPE+ITEMNO [D,M]; ITEMNO+VENDNUM+VENDTYPE [D,M]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  VENDTYPE Integer Vendor Type [1=Vendor 1,2=Vendor 2,3=Vendor 3,4=Vendor 4,5=Vendor 5,6=Vendor 6,7=Vendor 7,8=Vendor 8,9=Vendor 9]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VENDNUM String*12 Vendor Number
  VENDNAME String*60 Vendor Name
  VENDITEM String*24 Vendor Item Number
  VENDCONT String*60 Vendor Contact
  VENDCNCY String*3 Vendor Currency
  VENDCOST BCD*10.6 Vendor Cost
  VENDEXISTS Boolean Vendor Exists
  FACTOR BCD*10.6 Cost Unit Conv. Factor
  COSTUNIT String*10 Cost Unit

## ICIVAL - Item Valuation (view IC0352)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTSET+LOCATION+ITEMNO+FISCYEAR+FISCPERIOD+TRANSDATE+DAYENDSEQ+ENTRYSEQ+LINENO; LOCATION+ITEMNO [D,M]; DAYENDSEQ+ENTRYSEQ+LINENO [D,M]; ITEMNO+LOCATION+FISCYEAR+FISCPERIOD [D,M]; ACCTSET+LOCATION+ITEMNO+FISCYEAR+FISCPERIOD+TRANSTYPE+TRANSDATE+DOCNUM [D,M]
Fields (NAME type description [values]):
  ACCTSET String*6 Account Set Code
  LOCATION String*6 Location
  ITEMNO String*24 Item Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSDATE Date Transaction Date
  DAYENDSEQ Long Day End Number
  ENTRYSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY String*6 Category
  DOCNUM String*22 Document Number
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,3=Receipt Return,4=Shipment,5=Shipment Return,6=Adjustment Quantity Increase,7=Adjustment Quantity Decrease,8=Adjustment Cost Increase,9=Adjustment Cost Decrease,10=Adjustment Both Increase,11=Adjustment Both Decrease,12=Stock Transfer From,13=Stock Transfer To,14=Master Item Assembly,15=Component Item Assembly,16=Invoice,17=Credit Note,18=Debit Note,19=Shipment Adjustment,20=Internal Usage]
  UNIT String*10 Unit of Measure
  QUANTITY BCD*10.4 Transaction Quantity
  CONVERSION BCD*10.6 Conversion Factor
  TRANSCOST BCD*10.3 Transaction Cost
  STKQTY BCD*10.4 Quantity in Stocking UOM
  OPTAMT BCD*10.3 Optional Amount
  APP String*2 Application
  STOCKUNIT String*10 Stock Unit
  DEFPRICLST String*6 Default Price List
  TOTALCOST BCD*10.3 Total Cost
  RECENTCOST BCD*10.6 Recent Cost
  COST1 BCD*10.6 Cost 1 Name
  COST2 BCD*10.6 Cost 2 Name
  LASTCOST BCD*10.6 Last Cost
  STDCOST BCD*10.6 Standard Cost
  COSTUNIT String*10 Cost Unit
  COSTCONV BCD*10.6 Cost Conversion
  TOTALQTY BCD*10.4 Total Quantity
  PRICELIST String*6 Price List Code
  PRICEDECS Integer Decimals in Price
  BASEPRICE BCD*10.6 Base Price
  BASEUNIT String*10 Pricing Unit of Measure
  BASECONV BCD*10.6 Base Conversion Factor
  DETAILNUM Integer Detail Number
  COMPNUM Long Detail Component Number
  DATEBUS Date Posting Date

## ICKITD - Kitting Item Components (view IC0355)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+KITNO+LINENO; COMPONENT [D,M]
Fields (NAME type description [values]):
  ITEMNO String*24 Unformatted Item Number
  KITNO String*6 Kitting Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item Number
  QTY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost

## ICKITH - Kitting Items (view IC0356)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+KITNO
Fields (NAME type description [values]):
  ITEMNO String*24 Unformatted Item Number
  KITNO String*6 Kitting Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  REMARK String*80 Comments

## ICLBL - Label (view IC0360)
Keys (first = PK; D=dups allowed, M=modifiable): RECPNUM+SEQNUM+LINENO
Fields (NAME type description [values]):
  RECPNUM String*22 Receipt Number
  SEQNUM Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  NUMLABELS Integer Number of Labels
  PRINTED Boolean Printed [0=No,1=Yes]

## ICLOC - Locations (view IC0370)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Name
  ADDRESS1 String*60 Address Line 1
  ADDRESS2 String*60 Address Line 2
  ADDRESS3 String*60 Address Line 3
  ADDRESS4 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State
  ZIP String*20 Zip/Postal Code
  COUNTRY String*30 Country
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  CONTACT String*60 Contact
  SEGOVERRD Boolean Segment Override
  DATELASTMN Date Date Last Maintained
  INACTIVE Boolean Status [0=Active,1=Inactive]
  DATEINACTV Date Date Inactive
  SEGNUM1 String*6 Segment Number 1
  SEGVAL1 String*15 Segment Value  1
  SEGNUM2 String*6 Segment Number 2
  SEGVAL2 String*15 Segment Value  2
  SEGNUM3 String*6 Segment Number 3
  SEGVAL3 String*15 Segment Value  3
  SEGNUM4 String*6 Segment Number 4
  SEGVAL4 String*15 Segment Value  4
  SEGNUM5 String*6 Segment Number 5
  SEGVAL5 String*15 Segment Value  5
  SEGNUM6 String*6 Segment Number 6
  SEGVAL6 String*15 Segment Value  6
  SEGNUM7 String*6 Segment Number 7
  SEGVAL7 String*15 Segment Value  7
  SEGNUM8 String*6 Segment Number 8
  SEGVAL8 String*15 Segment Value  8
  SEGNUM9 String*6 Segment Number 9
  SEGVAL9 String*15 Segment Value  9
  EMAIL String*50 Location E-mail
  PHONEC String*30 Contact Phone
  FAXC String*30 Contact Fax
  EMAILC String*50 Contact E-mail
  LOCTYPE Integer Location Type [0=Physical,1=Logical]

## ICOFD - Optional Fields (view IC0377)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Items,1=Reorder Quantities,2=Receipts,3=Receipt Details,4=Shipments,5=Shipment Details,6=Adjustments,7=Adjustment Details,8=Transfers,9=Transfer Details,10=Assemblies,11=Internal Usage,12=Internal Usage Details,13=Item Serials,14=Item Lots]
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
  SWPAYCLR Integer Payables Clearing [99=Not Applicable]
  SWICCTL Integer Inventory Control [99=Not Applicable]
  SWNSCLR Integer Non-Stock Clearing [99=Not Applicable]
  SWCOGS Integer Cost of Goods Sold [99=Not Applicable]
  SWCV Integer Cost Variance [99=Not Applicable]
  SWADJWO Integer Adjustment Write-Off [99=Not Applicable]
  SWPMWIP Integer Work in Progress [99=Not Applicable]
  SWPMCOS Integer Cost of Sales [99=Not Applicable]
  SWPMOH Integer Overhead [99=Not Applicable]
  SWICCTLFR Integer Inventory Control(From Location) [99=Not Applicable]
  SWICCTLTO Integer Inventory Control(To Location) [99=Not Applicable]
  SWICCTLGIT Integer Inventory Control(GIT Location) [99=Not Applicable]
  SWTRCLR Integer Transfer Clearing [99=Not Applicable]
  SWICCTLMA Integer Inventory Control(Master Item) [99=Not Applicable]
  SWICCTLCO Integer Inventory Control(Component) [99=Not Applicable]
  SWACC Integer Assembly Cost Credit [99=Not Applicable]
  SWDE Integer Disassembly Expense [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]
  SWICSEXP Integer Internal Usage [99=Not Applicable]

## ICOFH - Optional Field Locations (view IC0378)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Items,1=Reorder Quantities,2=Receipts,3=Receipt Details,4=Shipments,5=Shipment Details,6=Adjustments,7=Adjustment Details,8=Transfers,9=Transfer Details,10=Assemblies,11=Internal Usage,12=Internal Usage Details,13=Item Serials,14=Item Lots]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## ICOPT - I/C Options (view IC0380)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTACT String*60 Contact Name
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  FRACTQTY Boolean Fractional Quantities
  NEGQTY Boolean Allow Negative Quantities
  TRANSHIST Boolean Keep Transaction History
  JOBCOST Boolean Interface With Job Cost
  REFCHOICE Integer G/L Reference Field [1=Document Number,2=Reference Number,3=Source Code/Day End Number/Entry Number,4=Header Description,5=Customer/Vendor Number,6=Customer/Vendor Name]
  DESCCHOICE Integer G/L Description Field [1=Document Number,2=Reference Number,3=Source Code/Day End Number/Entry Number,4=Header Description,5=Customer/Vendor Number,6=Customer/Vendor Name]
  WEIGHTUNIT String*10 Default Weight Unit of Measure
  COST1NAME String*10 Cost 1 Name
  COST2NAME String*10 Cost 2 Name
  DAYEND Integer Day End Transactions Outstanding
  TRANSNUM BCD*10.0 Next Transaction Number
  NXTALTSET Long Next Alternate Item Set Number
  GLDAYEND Long G/L Trans Created Thru Day End
  ADJENSEQ Long Next Adjustment Entry Seq.
  ASSMENSEQ Long Next Assembly Entry Seq.
  RECENSEQ Long Next Receipt Entry Seq.
  SHIPENSEQ Long Next Shipment Entry Seq.
  TRANFENSEQ Long Next Transfer Entry Seq.
  HISTENSEQ Long Next History Entry Seq.
  DAYENDSEQ Long Next Day End Posting Seq.
  MULTICURR Boolean Multicurrency
  DEFERGLPST Boolean Deferred G/L Posting
  APPENDGL Integer Append To G/L Batch [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  CONSOLGL Integer Consolidate G/L Batch [1=Do Not Consolidate,9=Consolidate Transaction Details by Account,2=Consolidate by Account and Fiscal Period,3=Consolidate by Account, Fiscal Period, and Source]
  STATCALNDR Integer Statistics Calendar [1=Calendar Year,2=Fiscal Year]
  STATPRD Integer Statistics Period [1=Weekly,2=Seven Days,3=Bi-weekly,4=Four Weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Annually,10=Fiscal Period]
  STATEDIT Boolean Edit Statistics
  CRTITEMLOC Boolean Allow Items at All Locations
  ADDCSTTYPE Integer Add'l. Cost on Rcpt. Returns [1=Leave,2=Prorate]
  RATETYPE String*2 Default Rate Type
  ITEMBRKID String*6 Default Item Structure
  STATACCUM Boolean Accumulate Item Statistics
  PSTTOCLOSD Boolean Post To Closed Fiscal Periods
  HYHEN Boolean Use Hyhen as Item Separator
  FWDSLASH Boolean Use Forward Slash as Item Separator
  BCKSLASH Boolean Use Back Slash as Item Separator
  ASTERISK Boolean Use Asterisk as Item Separator
  PERIOD Boolean Use Period as Item Separator
  LFTPARENS Boolean Use Left Parenthesis as Item Separator
  RGTPARENS Boolean Use Right Parenthesis as Item Separator
  POUNDSGN Boolean Use Pound Sign as Item Separator
  RECNONSTK Boolean Allow Receipt of Non-stock Items
  DELPROMPT Boolean Prompt to Delete during Posting
  COSTDURING Integer Cost During [1=Day End Processing,2=Posting]
  ASSNUMBERL Integer Assembly Number Length
  ASSPREFIXD String*6 Assembly Number Prefix
  ASSBODYD String*22 Next Assembly Number
  DASNUMBERL Integer Disassembly Number Length
  DASPREFIXD String*6 Disassembly Number Prefix
  DASBODYD String*22 Next Disassembly Number
  TRFNUMBERL Integer Transfer Number Length
  TRFPREFIXD String*6 Transfer Number Prefix
  TRFBODYD String*22 Next Transfer Number
  ADJNUMBERL Integer Adjustment Number Length
  ADJPREFIXD String*6 Adjustment Number Prefix
  ADJBODYD String*22 Next Adjustment Number
  SHPNUMBERL Integer Shipment Number Length
  SHPPREFIXD String*6 Shipment Number Prefix
  SHPBODYD String*22 Next Shipment Number
  SRTNUMBERL Integer Shipment Return Number Length
  SRTPREFIXD String*6 Shipment Return Number Prefix
  SRTBODYD String*22 Next Shipment Return Number
  RCPNUMBERL Integer Receipt Number Length
  RCPPREFIXD String*6 Receipt Number Prefix
  RCPBODYD String*22 Next Receipt Number
  TRCNUMBERL Integer Transit Receipt Number Length
  TRCPREFIXD String*6 Transit Receipt Number Prefix
  TRCBODYD String*22 Next Transit Receipt Number
  RECDESEQ Long Next Non-costed Receipt Day End Seq.
  GITLOC String*6 Default Goods in Transit Location
  DEFUOM Boolean Only Use Defined UOM
  AGING1 BCD*3.0 Aging Period 1
  AGING2 BCD*3.0 Aging Period 2
  AGING3 BCD*3.0 Aging Period 3
  SLAUDURING Integer Create Subledger/Audit During [1=Day End Processing,2=Posting]
  ICSENSEQ Long Next Internal Usage Entry Seq.
  ICSNUMBERL Integer Internal Usage Number Length
  ICSPREFIXD String*6 Internal Usage Number Prefix
  ICSBODYD String*22 Next Internal Usage Number
  SRCTYPERC String*2 I/C Receipts
  SRCTYPERR String*2 I/C Receipt Returns
  SRCTYPERA String*2 I/C Receipt Adjustments
  SRCTYPESH String*2 I/C Shipments
  SRCTYPESR String*2 I/C Shipment Returns
  SRCTYPETF String*2 I/C Transfers
  SRCTYPEAS String*2 I/C Assemblies
  SRCTYPEAD String*2 I/C Adjustments
  SRCTYPECO String*2 I/C Consolidated Entry
  SRCTYPEDA String*2 I/C Disassemblies
  SRCTYPEIN String*2 I/C Internal Usage
  DATEBUSDFT Integer Default Posting Date [1=Document Date,2=Session Date]
  SERIALMASK String*6 Serial Number Mask
  SUSEEXPDAY Boolean Use Serials Days to Expire
  SEXPDAYS Integer Serials Days to Expire
  SDIFQTYOK Boolean Allow Different Serial Qty
  SALCQTYORD Boolean Allow Serial Alloc on Qty Ord.
  SSORTBY Integer Sort Serials by [1=Serial Number,2=Stock Date,3=Expiry Date]
  SFIRST Integer Sort Serials First by [1=Earliest,2=Latest]
  SEXPLEVEL Integer Stop Allocation of Expired Serials [0=None,1=Warning,2=Error]
  SHYPHEN Boolean Serials Hyphen as Separator
  SFWDSLASH Boolean Serials Fwd Slash as Separator
  SBCKSLASH Boolean Serials Back Slash as Separator
  SASTERISK Boolean Serials Asterisk as Separator
  SPERIOD Boolean Serials Period as Separator
  SLFPARENS Boolean Serials Left Parenthesis as Sep
  SRGTPARENS Boolean Serials Right Parenthesis as Sep
  SPOUNDSIGN Boolean Serials Pound Sign as Separator
  SLFBRACKT Boolean Serials Left Bracket as Sep
  SRGTBRACKT Boolean Serials Right Bracket as Sep
  SLFBRACE Boolean Serials Left Brace as Sep
  SRGTBRACE Boolean Serials Right Brace as Sep
  LOTMASK String*6 Lot Number Mask
  LUSEEXPDAY Boolean Use Lots Days to Expire
  LEXPDAYS Integer Lots Days to Expire
  LUSEQRNDAY Boolean Use Lots Days on Quarantine
  LQRNDAYS Integer Lots Days on Quarantine
  LDIFQTYOK Boolean Allow Different Lot Qty
  LALCQTYORD Boolean Allow Lot Alloc on Qty Ord.
  LSORTBY Integer Sort Lots by [1=Lot Number,2=Stock Date,3=Expiry Date]
  LFIRST Integer Sort Lots First by [1=Earliest,2=Latest]
  LEXPLEVEL Integer Stop Allocation of Expired Lots [0=None,1=Warning,2=Error]
  LHYPHEN Boolean Lots Hyphen as Separator
  LFWDSLASH Boolean Lots Fwd Slash as Separator
  LBCKSLASH Boolean Lots Back Slash as Separator
  LASTERISK Boolean Lots Asterisk as Separator
  LPERIOD Boolean Lots Period as Separator
  LLFPARENS Boolean Lots Left Parenthesis as Sep
  LRGTPARENS Boolean Lots Right Parenthesis as Sep
  LPOUNDSIGN Boolean Lots Pound Sign as Separator
  LLFBRACKT Boolean Lots Left Bracket as Separator
  LRGTBRACKT Boolean Lots Right Bracket as Separator
  LLFBRACE Boolean Lots Left Brace as Separator
  LRGTBRACE Boolean Lots Right Brace as Separator
  RECALENSEQ BCD*10.0 Recall/Release Sequence Number
  RECNUMBERL Integer Recall Number Length
  RECPREFIXD String*6 Recall Number Prefix
  RECBODYD String*22 Next Recall Number
  RELNUMBERL Integer Release Number Length
  RELPREFIXD String*6 Release Number Prefix
  RELBODYD String*22 Next Release Number
  COMENSEQ BCD*10.0 Combine/Split Sequence Number
  COMNUMBERL Integer Combine Number Length
  COMPREFIXD String*6 Combine Number Prefix
  COMBODYD String*22 Next Combine Number
  SPLNUMBERL Integer Split Number Length
  SPLPREFIXD String*6 Split Number Prefix
  SPLBODYD String*22 Next Split Number
  RCNENSEQ BCD*10.0 Reconciliation Sequence Number
  RCNNUMBERL Integer Reconciliation Number Length
  RCNPREFIXD String*6 Reconciliation Number Prefix
  RCNBODYD String*22 Next Reconciliation Number

## ICPCOD - Price List Codes (view IC0390)
Keys (first = PK; D=dups allowed, M=modifiable): PRICELIST
Fields (NAME type description [values]):
  PRICELIST String*6 Price List Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  PRICETYPE Integer Selling Price Based on [1=Discount,2=Markup on Markup Cost,3=Markup on Standard Cost,4=Markup on Most Recent Cost,5=Markup on Average Cost,6=Markup on Last Cost]
  PRICEFMT Integer Discount/Markup on Price by [1=Percentage,2=Amount]
  PRCNTLVL1 BCD*5.5 Discount/Markup Percentage 1
  PRCNTLVL2 BCD*5.5 Discount/Markup Percentage 2
  PRCNTLVL3 BCD*5.5 Discount/Markup Percentage 3
  PRCNTLVL4 BCD*5.5 Discount/Markup Percentage 4
  PRCNTLVL5 BCD*5.5 Discount/Markup Percentage 5
  PRICEBASE Integer Price Determined by [1=Customer Type,2=Volume Discounts]
  PRICEQTY1 BCD*10.4 Quantity Level 1
  PRICEQTY2 BCD*10.4 Quantity Level 2
  PRICEQTY3 BCD*10.4 Quantity Level 3
  PRICEQTY4 BCD*10.4 Quantity Level 4
  PRICEQTY5 BCD*10.4 Quantity Level 5
  PRICEDECS Integer Decimals in Price [0= 0,1= 1,2= 2,3= 3,4= 4,5= 5,6= 6]
  ROUNDMETHD Integer Rounding Method [1=No Rounding,2=Round Up,3=Round Down]
  ROUNDAMT BCD*10.6 Round to a Multiple of
  AMOUNTLVL1 BCD*10.6 Discount/Markup Amount 1
  AMOUNTLVL2 BCD*10.6 Discount/Markup Amount 2
  AMOUNTLVL3 BCD*10.6 Discount/Markup Amount 3
  AMOUNTLVL4 BCD*10.6 Discount/Markup Amount 4
  AMOUNTLVL5 BCD*10.6 Discount/Markup Amount 5
  PRICEBY Integer Price By [1=Quantity,2=Weight]
  PRICEWGHT1 BCD*10.4 Weight Level 1
  PRICEWGHT2 BCD*10.4 Weight Level 2
  PRICEWGHT3 BCD*10.4 Weight Level 3
  PRICEWGHT4 BCD*10.4 Weight Level 4
  PRICEWGHT5 BCD*10.4 Weight Level 5
  CPRICETYPE Integer Price Check Type [0=None,1=Warning,2=Error,3=Approval]
  CCHECK Integer Check [1=Unit Price,2=Sales Margin]
  CCHECKBASE Integer Check Base [1=Cost Plus a Percentage,2=Cost Plus a Fixed Amount,3=Fixed Amount]
  CBASE Integer Cost/Margin Base [1=Markup Cost,2=Standard Cost,3=Most Recent Cost,4=Average Cost,5=Last Cost]

## ICPCODC - Price List Codes Checks (view IC0392)
Keys (first = PK; D=dups allowed, M=modifiable): PRICELIST+USERID
Fields (NAME type description [values]):
  PRICELIST String*6 Price List Code
  USERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXISTS Boolean Record Exists [0=No,1=Yes]
  CGTPERCENT BCD*5.5 Greater than Percentage
  CLTPERCENT BCD*5.5 Less than Percentage
  CGTAMOUNT BCD*10.6 Greater than Amount
  CLTAMOUNT BCD*10.6 Less than Amount

## ICPCTX - Price List Code Tax Authorities (view IC0395)
Keys (first = PK; D=dups allowed, M=modifiable): PRICELIST+AUTHORITY
Fields (NAME type description [values]):
  PRICELIST String*6 Price List Code
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXINCL Boolean Tax Included in Price [0=No,1=Yes]
  TAXCLASS Integer Customer Tax Class

## ICPRIC - Item Pricing (view IC0480)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+ITEMNO+PRICELIST; ITEMNO+CURRENCY+PRICELIST; CURRENCY+PRICELIST+ITEMNO
Fields (NAME type description [values]):
  CURRENCY String*3 Currency Code
  ITEMNO String*24 Unformatted Item Number
  PRICELIST String*6 Price List Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  PRICEDECS Integer Decimals in Price [0= 0,1= 1,2= 2,3= 3,4= 4,5= 5,6= 6]
  MARKUPCOST BCD*10.6 Markup Cost
  MARKUPUNIT String*10 Markup Unit of Measure
  MARKUPCONV BCD*10.6 Markup Conversion Factor
  PRICETYPE Integer Selling Price Based on [1=Discount,2=Markup on Markup Cost,3=Markup on Standard Cost,4=Markup on Most Recent Cost,5=Markup on Average Cost,6=Markup on Last Unit Cost]
  PRICEFMT Integer Discount/Markup Price by [1=Percentage,2=Amount]
  PRCNTLVL1 BCD*5.5 Discount/Markup Percentage 1
  PRCNTLVL2 BCD*5.5 Discount/Markup Percentage 2
  PRCNTLVL3 BCD*5.5 Discount/Markup Percentage 3
  PRCNTLVL4 BCD*5.5 Discount/Markup Percentage 4
  PRCNTLVL5 BCD*5.5 Discount/Markup Percentage 5
  PRICEBASE Integer Price Determined by [1=Customer Type,2=Volume Discounts]
  PRICEQTY1 BCD*10.4 Quantity Level 1
  PRICEQTY2 BCD*10.4 Quantity Level 2
  PRICEQTY3 BCD*10.4 Quantity Level 3
  PRICEQTY4 BCD*10.4 Quantity Level 4
  PRICEQTY5 BCD*10.4 Quantity Level 5
  MARKUP BCD*5.5 Markup Factor
  LASTMKPDT Date Last Markup Cost Change Date
  PREVMKPCST BCD*10.6 Previous Markup Cost
  LASTEXCHDT Date Last Exchange Rate Change Date
  PREVEXCHRT BCD*8.7 Previous Exchange Rate
  ROUNDMETHD Integer Rounding Method [1=No Rounding,2=Round Up,3=Round Down]
  ROUNDAMT BCD*10.6 Round to a Multiple of
  AMOUNTLVL1 BCD*10.6 Discount/Markup Amount 1
  AMOUNTLVL2 BCD*10.6 Discount/Markup Amount 2
  AMOUNTLVL3 BCD*10.6 Discount/Markup Amount 3
  AMOUNTLVL4 BCD*10.6 Discount/Markup Amount 4
  AMOUNTLVL5 BCD*10.6 Discount/Markup Amount 5
  PRICEBY Integer Price By [1=Quantity,2=Weight]
  MRKUPWUNIT String*10 Markup Weight Unit of Measure
  PRICEWGHT1 BCD*10.4 Weight Level 1
  PRICEWGHT2 BCD*10.4 Weight Level 2
  PRICEWGHT3 BCD*10.4 Weight Level 3
  PRICEWGHT4 BCD*10.4 Weight Level 4
  PRICEWGHT5 BCD*10.4 Weight Level 5
  CPRICETYPE Integer Price Check Type [0=None,1=Warning,2=Error,3=Approval]
  CCHECK Integer Check [1=Unit Price,2=Sales Margin]
  CCHECKBASE Integer Check Base [1=Cost Plus a Percentage,2=Cost Plus a Fixed Amount,3=Fixed Amount]
  CBASE Integer Cost/Margin Base [1=Markup Cost,2=Standard Cost,3=Most Recent Cost,4=Average Cost,5=Last Unit Cost]
  DEFBUNIT String*10 Default Base Unit
  DEFBWUNIT String*10 Default Base Weight Unit
  DEFSUNIT String*10 Default Sale Unit
  DEFSWUNIT String*10 Default Sale Weight Unit
  BPRICETYPE Integer Base Price Type [1=Base Price for Single Unit of Measure,2=Base Price for Multiple Units of Measure,3=Base Price Calculated Using a Cost]
  BDEFUSING Integer Default Base Price Using [0=No Default,1=Cost Plus a Percentage,2=Cost Plus an Amount]
  BLOCATION String*6 Base Location
  BBASE Integer Base Cost Base [1=Standard Cost,2=Most Recent Cost,3=Average Cost,4=Last Unit Cost]
  BPERCENT BCD*5.5 Base Percentage
  BAMOUNT BCD*10.6 Base Amount
  BRATETYPE String*2 Base Rate Type
  BRATEDATE Date Base Rate Date
  BEXCHRATE BCD*8.7 Base Exchange Rate
  BRATEOP Integer Base Rate Operator [1=Multiply,2=Divide]
  BRATEOVRRD Boolean Base Rate Overidden [0=No,1=Yes]
  SPRICETYPE Integer Sale Price Type [1=Sale Price for Single Unit of Measure,2=Sale Price for Multiple Units of Measure,3=Sale Price Calculated Using a Cost]
  SDEFUSING Integer Default Sale Price Using [0=No Default,1=Cost Plus a Percentage,2=Cost Plus an Amount]
  SLOCATION String*6 Sale Location
  SBASE Integer Sale Cost Base [1=Standard Cost,2=Most Recent Cost,3=Average Cost,4=Last Unit Cost]
  SPERCENT BCD*5.5 Sale Percentage
  SAMOUNT BCD*10.6 Sale Amount
  SRATETYPE String*2 Sale Rate Type
  SRATEDATE Date Sale Rate Date
  SEXCHRATE BCD*8.7 Sale Exchange Rate
  SRATEOP Integer Sale Rate Operator [1=Multiply,2=Divide]
  SRATEOVRRD Boolean Sale Rate Overidden [0=No,1=Yes]
  PRICESTART Date Price List Start Date
  PRICEEND Date Price List End Date

## ICPRICC - Pricing Price Checks (view IC0481)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+ITEMNO+PRICELIST+USERID
Fields (NAME type description [values]):
  CURRENCY String*3 Currency Code
  ITEMNO String*24 Unformatted Item Number
  PRICELIST String*6 Price List Code
  USERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXISTS Boolean Record Exists [0=No,1=Yes]
  CGTPERCENT BCD*5.5 Greater than Percentage
  CLTPERCENT BCD*5.5 Less than Percentage
  CGTAMOUNT BCD*10.6 Greater than Amount
  CLTAMOUNT BCD*10.6 Less than Amount

## ICPRICP - Item Pricing Details (view IC0482)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+ITEMNO+PRICELIST+DPRICETYPE+QTYUNIT+WEIGHTUNIT; ITEMNO+QTYUNIT [D,M]
Fields (NAME type description [values]):
  CURRENCY String*3 Currency Code
  ITEMNO String*24 Unformatted Item Number
  PRICELIST String*6 Price List Code
  DPRICETYPE Integer Price Detail Type [1=Base Price Quantity,2=Sale Price Quantity,3=Base Price Weight,4=Sale Price Weight,5=Base Price Using Cost,6=Sale Price Using Cost]
  QTYUNIT String*10 Quantity Unit
  WEIGHTUNIT String*10 Weight Unit
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  UNITPRICE BCD*10.6 Unit Price
  CONVERSION BCD*10.6 Conversion Factor
  SALESTART Date Sale Start
  SALEEND Date Sale End
  LASTPRICDT Date Last Price Change Date
  PREVPRICE BCD*10.6 Previous Price

## ICPRTX - Price List Tax Authorities (view IC0490)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+ITEMNO+PRICELIST+AUTHORITY; ITEMNO+CURRENCY+PRICELIST+AUTHORITY [D,M]
Fields (NAME type description [values]):
  CURRENCY String*3 Currency Code
  ITEMNO String*24 Item Number
  PRICELIST String*6 Price List Code
  AUTHORITY String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXINCL Boolean Tax Included in Price [0=No,1=Yes]
  TAXCLASS Integer Customer Tax Class

## ICPSCBD - Assembly Detail Costs (view IC0412)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+LINENO
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Unformatted Item Number
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  QTYBLDTOT BCD*10.4 Build Quantity
  BLDUNIT String*10 Building Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  QTYSTKTOT BCD*10.4 Stock Quantity
  STOCKUNIT String*10 Stocking Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  CTLACTSET String*6 Component Control Acct. Set
  COMPCTLAMT BCD*10.3 Component G/L Control Amt.
  COMPCTLACT String*45 Component G/L Control Acct.

## ICPSCBH - Assembly Header Costs (view IC0413)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Unformatted Item Number
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  QTYBLDTOT BCD*10.4 Build Quantity
  BLDUNIT String*10 Building Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  QTYSTKTOT BCD*10.4 Stock Quantity
  STOCKUNIT String*10 Stocking Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  CTLACTSET String*6 Master Control Acct. Set
  LOCDESC String*60 Location Desription
  MASTVARAMT BCD*10.3 Master Variable Cost
  MASTFIXAMT BCD*10.3 Master Fixed Cost
  MASTDISAMT BCD*10.3 Master Disassembly Expense
  MASTCTLAMT BCD*10.3 Master G/L Control Amt.
  MASTCTLACT String*45 Master G/L Control Acct.
  MASTASCACT String*45 Master Assembly Cost Acct.
  MASTDIEACT String*45 Master Disassembly Exp. Acct.

## ICPSCID - Internal Usage Detail Costs (view IC0417)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+LINENO
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Item Description
  STOCKITEM Boolean Stock Item
  STOCKUNIT String*10 Stocking Unit of Measure
  STOCKQTY BCD*10.4 Stock Quantity
  UNITCOST BCD*10.6 Unit Cost
  VARAMT BCD*10.3 Variance
  ICSEXPAMT BCD*10.3 Internal Usage Exp. Amt.
  NONSTCKAMT BCD*10.3 Non-stock Clearing Amt.
  ITEMCTLAMT BCD*10.3 Item G/L Control Amt.
  ITMSTATAMT BCD*10.3 Item Statistics Amt.
  CTLACTSET String*6 Item Control Acct. Set
  VARACT String*45 Variance Acct.
  ICSEXPACT String*45 Internal Usage Exp. Acct.
  NONSTCKACT String*45 Item G/L Non-stock Clr. Acct.
  ITEMCTLACT String*45 Item G/L Control Acct.
  STATYEAR String*4 Fiscal Year
  STATPERIOD Integer Fiscal Period

## ICPSCRD - Receipt Detail Costs (view IC0423)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSNUM+LINENO
Fields (NAME type description [values]):
  TRANSNUM BCD*10.0 Transaction Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Line Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  STOCKUNIT String*10 Stocking Unit of Measure
  QUANTITY BCD*10.4 Quantity
  STKQTY BCD*10.4 Stock Quantity
  UNITCSTHM BCD*10.6 Unit Cost - Functional
  NEWUNITCST BCD*10.6 New Unit Cost - Functional
  ITTOTCSTHM BCD*10.3 Item Cost - Functional
  ITTOTCSTSR BCD*10.3 Item Cost - Source
  DIFFCSTHM BCD*10.3 Cost - Functional
  DIFFCSTSRC BCD*10.3 Cost - Source
  DETCSTHM BCD*10.3 Extended Cost - Functional
  DETCSTSRC BCD*10.3 Extended Cost - Source
  DADDCSTHM BCD*10.3 Additional Cost - Functional
  DADDCSTSRC BCD*10.3 Additional Cost - Source
  CTLACTSET String*6 Item Control Acct. Set
  ITEMCTLACT String*45 Item G/L Control Acct.
  NSTKCLRACT String*45 Item G/L Non-stock Clr. Acct.
  PAYABLEACT String*45 Item G/L Payables Acct.
  STATYEAR String*4 Fiscal Year
  STATPERIOD Integer Fiscal Period

## ICPSCRH - Receipt Header Costs (view IC0426)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSNUM
Fields (NAME type description [values]):
  TRANSNUM BCD*10.0 Transaction Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TADDCSTHM BCD*10.3 Additional Cost - Func.
  TADDCSTSRC BCD*10.3 Additional Cost - Source
  TOTDIFCSTH BCD*10.3 Total Cost - Functional
  TOTDIFCSTS BCD*10.3 Total Cost - Source

## ICRCPD - Receipt Not Costed Details (view IC0550)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  EXTCOST BCD*10.3 Extended Cost
  UNTCST BCD*10.6 Unit Cost - Source
  COMMENTS String*250 Comments
  COSTSEQNUM Long Cost Bucket Number
  COSTDATE Date Cost Bucket Date
  STOCKITEM Boolean Stock Item
  VALUES Long Optional Fields

## ICRCPDL - Receipt Not Costed Detail Lot Numbers (view IC0553)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+LOTNUMF; LOTNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  QTYMOVED BCD*10.4 Lot Quantity Returned
  QTYMOVEDSQ BCD*10.4 Lot Qty Returned in Stocking UOM

## ICRCPDP - Rcpt Not Costed Dtl. Opt. Fields (view IC0555)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+OPTFIELD; OPTFIELD+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
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

## ICRCPDS - Receipt Not Costed Detail Serial Numbers (view IC0558)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+SERIALNUMF; SERIALNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MOVED Boolean Serial Returned?

## ICRCPH - Receipt Not Costed Headers (view IC0560)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; TRANSNUM; DOCUNIQ [D,M]
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSTYPE Integer Transaction Type
  VENDNUM String*12 Vendor Number
  PONUM String*22 Purchase Order Number
  RECPNUM String*22 Receipt Number
  RECPCUR String*3 Source Currency
  RECPRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVRRD Boolean Rate Override
  ADDCOST BCD*10.3 Additional Cost
  ADDCSTCUR String*3 Additional Cost Currency
  TOTCSTHM BCD*10.3 Total Receipt Cost - Func.
  TOTCSTSRC BCD*10.3 Total Receipt Cost - Source
  NUMDETAILS Integer Number of Details with Cost
  COMPLETE Boolean Receipt Complete
  HDRDESC String*60 Description
  ADDCSTTYPE Integer Addt'l. Cost Allocation Method
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  VALUES Long Optional Fields
  STATUS Integer Record Status [2=Posted,3=Costed]
  DATEBUS Date Posting Date

## ICRCPHP - Rcpt Not Costed Hdr Opt. Fields (view IC0565)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
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

## ICRECDP - Rcpt Audit List Dtl. Opt. Fields (view IC0567)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICRECHP - Rcpt Audit List Hdr Opt. Fields (view IC0568)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICRECPD - Receipt Audit List Details (view IC0575)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOCATION String*6 Location
  CATEGORY String*6 Category
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  QUANTITY BCD*10.4 Quantity Received
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  STOCKQTY BCD*10.4 Stock Quantity
  STOCKUNIT String*10 Stocking Unit of Measure
  UNITCST BCD*10.6 Unit Cost - Functional
  HMRECPCST BCD*10.3 Extended Cost - Functional
  SRCRECPCST BCD*10.3 Extended Cost - Source
  NEWUNITCST BCD*10.6 New Unit Cost - Functional
  ICACCT String*45 Inventory Control Account
  PAYABLACCT String*45 Payables Clearing Account
  COMMENTS String*250 Comments
  HMADDCST BCD*10.3 Additional Cost - Functional
  SRCADDCST BCD*10.3 Additional Cost - Source
  HMICAMT BCD*10.3 I/C Amount - Functional
  SRCICAMT BCD*10.3 I/C Amount - Source
  VALUES Long Optional Fields

## ICRECPH - Receipt Audit List Headers (view IC0570)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; RECPNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  HDRDESC String*60 Description
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Adjustment,3=Return,99=Sequence Header]
  VENDNUM String*12 Vendor Number
  PONUM String*22 Purchase Order Number
  RECPNUM String*22 Receipt Number
  RECPCUR String*3 Source Currency
  RECPRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVRRD Boolean Rate Override
  HMADDCST BCD*10.3 Additional Cost - Func.
  SRCADDCST BCD*10.3 Additional Cost - Source
  ADDCSTCUR String*3 Additional Cost Currency
  HMTOTALCST BCD*10.3 Total Cost - Functional
  SRCTOTLCST BCD*10.3 Total Cost - Source
  COMPLETE Boolean Receipt Complete
  PRINTED Boolean Printed
  ADDCSTTYPE Integer Addt'l. Cost Allocation Method
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICREED - Receipt Details (view IC0580)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  RECPQTY BCD*10.4 Quantity Received
  RETURNQTY BCD*10.4 Quantity Returned
  RECPUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  ADDCSTHM BCD*10.3 Prorated Add'l. Cost-Func.
  ADDCSTSRC BCD*10.3 Prorated Add'l. Cost-Src.
  UNITCOST BCD*10.6 Unit Cost
  ADJUNITCST BCD*10.6 Adjusted Unit Cost
  ADJCOST BCD*10.3 Adjusted Cost
  ADJCOSTHM BCD*10.3 Adjusted Cost-Functional
  RECPCOST BCD*10.3 Extended Cost
  RECPCOSTHM BCD*10.3 Extended Cost-Functional
  RETURNCOST BCD*10.3 Return Cost
  COSTDATE Date Costing Date
  COSTSEQNO Long Costing Sequence No.
  ORIGQTY BCD*10.4 Original Receipt Qty.
  ORIGUNTCST BCD*10.6 Original Unit Cost
  ORIGEXTCST BCD*10.3 Original Extended Cost
  ORIGEXTHM BCD*10.3 Original Extended Cost-Func.
  COMMENTS String*250 Comments
  LABELS Integer Labels
  STOCKITEM Boolean Stock Item
  MANITEMNO String*24 Manufacturer's Item Number
  VENDITEMNO String*24 Vendor Item Number
  DETAILNUM Integer Detail Line Number
  RETQTY BCD*10.4 Quantity Returned To Date
  RETEXTCST BCD*10.3 Returned Ext. Cost To Date
  RETEXTHM BCD*10.3 Returned Ext. Cost-Func. To Date
  ADJEXTCST BCD*10.3 Adjusted Ext. Cost To Date
  ADJEXTHM BCD*10.3 Adjusted Ext. Cost-Func. To Date
  PREVQTY BCD*10.4 Previous Day-End Receipt Qty.
  PREVUNTCST BCD*10.6 Previous Day-End Unit Cost
  PREVEXTCST BCD*10.3 Previous Day-End Ext. Cost
  PREVEXTHM BCD*10.3 Previous Day-End Ext. Cost-Func.
  VALUES Long Optional Fields
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SQTYMOVED Long Serial Quantity Returned
  LQTYMOVED BCD*10.4 Lot Quantity Returned

## ICREEDL - Receipt Detail Lot Numbers (view IC0582)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+LOTNUMF; LOTNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  QTYMOVED BCD*10.4 Lot Quantity Returned
  QTYMOVEDSQ BCD*10.4 Lot Qty Returned in Stocking UOM

## ICREEDO - Receipt Detail Optional Fields (view IC0585)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+OPTFIELD; OPTFIELD+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
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

## ICREEDS - Receipt Detail Serial Numbers (view IC0587)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+SERIALNUMF; SERIALNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MOVED Boolean Serial Returned?

## ICREEH - Receipt Headers (view IC0590)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; DOCUNIQ [D,M]; RECPNUMBER; STATUS+RECPNUMBER [M]
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECPDESC String*60 Description
  RECPDATE Date Receipt Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  PONUM String*22 Purchase Order Number
  REFERENCE String*60 Reference
  RECPTYPE Integer Receipt Type [1=Receipt,2=Return,3=Adjustment,4=Complete]
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  VENDNUMBER String*12 Vendor Number
  RECPCUR String*3 Receipt Currency
  RECPRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOVRRD Boolean Rate Override [0=No,1=Yes]
  ADDCOST BCD*10.3 Additional Cost
  ADDCOSTHM BCD*10.3 Orig. Additional Cost-Func.
  ADDCOSTSRC BCD*10.3 Orig. Additional Cost-Source
  ADDCUR String*3 Additional Cost Currency
  TOTCSTHM BCD*10.3 Total Extended Cost-Functional
  TOTCSTSRC BCD*10.3 Total Extended Cost-Source
  TOTCSTADJ BCD*10.3 Total Extended Cost-Adjusted
  TOTADJHM BCD*10.3 Total Adjusted Cost-Functional
  TOTCSTRET BCD*10.3 Total Return Cost
  NUMCSTDETL Integer Number of Details with Cost
  LABELS Boolean Require Labels [0=No,1=Yes]
  ADDCSTTYPE Integer Additional Cost Allocation Type [1=Leave,2=Prorate]
  COMPLETE Boolean Complete [0=No,1=Yes]
  ORIGTOTSRC BCD*10.3 Original Total Cost-Source
  ORIGTOTHM BCD*10.3 Original Total Cost-Functional
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  DELETED Boolean Record Deleted [0=No,1=Yes]
  TRANSNUM BCD*10.0 Transaction Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  RECPNUMBER String*22 Receipt Number
  NEXTDTLNUM Integer Next Detail Line Number
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## ICREEHO - Receipt Optional Fields (view IC0595)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
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

## ICREOR - Reorder Quantities (view IC0599)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDERFOR Integer Reorder For [1=Specific Location,2=All Locations]
  DTLCOUNT Integer Number of Details
  VALUES Long Optional Fields

## ICREORD - Reorder Quantities Details (view IC0600)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION+PERIODSTRT
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  PERIODSTRT Date Period Start
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MINLEVEL BCD*10.4 Minimum Quantity
  MAXLEVEL BCD*10.4 Maximum Quantity
  REORDERQTY BCD*10.4 Reorder Quantity
  SALESPROJ BCD*10.4 Projected Sales Qty.
  PERIODEND Date Period End
  ORDERFOR Integer Reorder For [1=Specific Location,2=All Locations]

## ICREORO - Reorder Quantities Opt. Fields (view IC0601)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION+OPTFIELD; OPTFIELD+ITEMNO+LOCATION
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
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

## ICRSTRT - Restart (view IC0606)
Keys (first = PK; D=dups allowed, M=modifiable): KEY+USERID
Fields (NAME type description [values]):
  KEY String*50 Key
  USERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## ICSEG - Item Segments (view IC0610)
Keys (first = PK; D=dups allowed, M=modifiable): SEGMENT; DESC [M]
Fields (NAME type description [values]):
  SEGMENT Integer Segment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  LENGTH Integer Length
  VALIDATE Boolean Validate

## ICSEGV - Segment Codes (view IC0620)
Keys (first = PK; D=dups allowed, M=modifiable): SEGMENT+SEGVAL
Fields (NAME type description [values]):
  SEGMENT Integer Segment Number
  SEGVAL String*24 Segment Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## ICSHED - Shipment Details (view IC0630)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  PRICELIST String*6 Price List
  UNITPRICE BCD*10.6 Unit Price
  SHIPPRICE BCD*10.3 Extended Price
  UNITCOST BCD*10.6 Unit Cost
  EXTCOST BCD*10.3 Extended Cost
  JOBNO String*24 *** Obsolete ***
  SERIALNO Boolean Serial Numbers
  SERIALUNIQ Integer Serial Number Uniquifier
  COMMENTS String*250 Comments
  PMCONTRACT String*16 P/M Contract
  PMPROJECT String*16 P/M Project
  PMCATEGORY String*16 P/M Category
  PMDETAIL Long P/M Detail
  PMWIPACCT String*45 P/M WIP Account
  MANITEMNO String*24 Manufacturer's Item Number
  CUSTITEMNO String*24 Customer Item Number
  DETAILNUM Integer Detail Line Number
  VALUES Long Optional Fields
  SAMTCNTL BCD*10.3 GL Control Amount - Shipment
  SAMTCSTVAR BCD*10.3 GL Cost Variance - Shipment
  RAMTCNTL BCD*10.3 GL Control Amount - Shipment Return
  RAMTCSTVAR BCD*10.3 GL Cost Variance - Shipment Return
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Lot Quantity

## ICSHEDL - Shipment Detail Lot Numbers (view IC0632)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+LOTNUMF; LOTNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM

## ICSHEDO - Shipment Detail Optional Fields (view IC0635)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+OPTFIELD; OPTFIELD+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
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

## ICSHEDS - Shipment Detail Serial Numbers (view IC0636)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO+SERIALNUMF; SERIALNUMF+SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ICSHEH - Shipment Headers (view IC0640)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; TRANSNUM [M]; STATUS+TRANSNUM [M]; DOCNUM; DOCUNIQ [D,M]; STATUS+DOCNUM [M]
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  DOCNUM String*22 Shipment Number
  HDRDESC String*60 Description
  TRANSDATE Date Ship Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  REFERENCE String*60 Reference
  TRANSTYPE Integer Entry Type [1=Shipment,2=Return]
  CUSTNO String*12 Customer Number
  CUSTNAME String*60 Customer Name
  CONTACT String*60 Contact
  CURRENCY String*3 Source Currency
  PRICELIST String*6 Price List
  EXCHRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVRRD Boolean Rate Override [0=No,1=Yes]
  SERIALUNIQ Integer Serial Number Uniquifier
  JOBCOST Boolean Job Related [0=No,1=Yes]
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  DELETED Boolean Record Deleted [0=No,1=Yes]
  NEXTDTLNUM Integer Next Detail Line Number
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## ICSHEHO - Shipment Optional Fields (view IC0645)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence Number
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

## ICSHIPD - Shipment Audit List Details (view IC0650)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  LOCATION String*6 Location
  SHIPQTY BCD*10.4 Quantity Shipped
  SHIPUNIT String*10 Unit of Measure
  SHIPCONV BCD*10.6 Conversion Factor
  STOCKQTY BCD*10.4 Quantity in Stocking Unit
  STOCKUNIT String*10 Stocking Unit of Measure
  PRICELIST String*6 Price List Code
  EXPRICSRC BCD*10.3 Extended Price - Source
  EXPRICEHM BCD*10.3 Extended Price - Functional
  UNITCOST BCD*10.6 User-Specified Cost
  SHIPCOST BCD*10.3 User-Specified Extended Cost
  VARIANCE BCD*10.3 Variance
  STOCKITEM Boolean Stock Item
  COGSACCT String*45 Cost of Goods Sold Account
  VARACCT String*45 Cost Variance Account
  ICACCT String*45 Inventory Control Account
  COMMENTS String*250 Comments
  PMCONTRACT String*16 P/M Contract
  PMPROJECT String*16 P/M Project
  PMCATEGORY String*16 P/M Category
  PMDETAIL Long P/M Detail
  PMOHACCT String*45 P/M Overhead Account
  PMOHAMT BCD*10.3 P/M Overhead Amount
  VALUES Long Optional Fields

## ICSHIPH - Shipment Audit List Headers (view IC0652)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; DOCNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  DOCNUM String*22 Shipment Number
  TRANSDATE Date Transaction Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  REFERENCE String*60 Reference
  HDRDESC String*60 Description
  TRANSTYPE Integer Transaction Type [1=Shipment,2=Return,99=Sequence Header]
  CUSTNO String*12 Customer Number
  CUSTNAME String*60 Customer Name
  CONTACT String*60 Contact
  CURCODE String*3 Source Currency
  PRCLSTCDE String*6 Price List Code
  PRCRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVRRD Boolean Rate Override
  PRINTED Boolean Printed
  JOBNO String*24
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICSHPDP - Ship Audit List Det. Opt. Fields (view IC0655)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICSHPHP - Ship Audit List Hdr Opt. Fields (view IC0657)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICSTAT - Transaction Statistics (view IC0700)
Keys (first = PK; D=dups allowed, M=modifiable): YEAR+PERIOD
Fields (NAME type description [values]):
  YEAR String*4 Year
  PERIOD Integer Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECCOUNT Long Number of Receipts
  RECTOTAL BCD*10.3 Cost of Receipts
  RECADJ Long Number of Receipt Adjustments
  RECADJTTL BCD*10.3 Cost of Receipt Adjustments
  RECRTN Long Number of Receipt Returns
  RECRTNTTL BCD*10.3 Cost of Receipt Returns
  SHIPCOUNT Long Number of Shipments
  SHIPTOTAL BCD*10.3 Cost of Shipments
  SHIPPRICE BCD*10.3 Price of Shipments
  SHIPRTN Long Number of Shipment Returns
  SHIPRTNTTL BCD*10.3 Cost of Shipment Returns
  SHIPRTNPRC BCD*10.3 Price of Shipment Returns
  ADJCOUNT Long Number of Adjustments
  ADJTOTAL BCD*10.3 Cost of Adjustments
  TRANFCOUNT Long Number of Transfers
  ICSCOUNT Long Number of Internal Usages
  ICSTOTAL BCD*10.3 Cost of Internal Usages

## ICSTATI - Sales Statistics (view IC0710)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION+YEAR+PERIOD
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  YEAR String*4 Year
  PERIOD Integer Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SALESAMT BCD*10.3 Sales Amount
  SALESCOUNT Long Sales Count
  SALESQTY BCD*10.4 Sales Quantity
  COGS BCD*10.3 Cost of Goods Sold
  SALERTNAMT BCD*10.3 Sales Return Amount
  SALERTNCNT Long Sales Return Count
  SALERTNQTY BCD*10.4 Sales Return Quantity
  COGSRTN BCD*10.3 Cost of Goods Returned

## ICTRAND - Transfer Audit List Details (view IC0714)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  CATEGORY String*6 Category
  FROMLOC String*6 From Location
  TOLOC String*6 To Location
  QTY BCD*10.4 Quantity Transferred
  UNIT String*10 Unit of Measure
  COST BCD*10.3 Total Cost of Transfer
  FROMICACCT String*45 Transfer From I/C Account
  TOICACCT String*45 Transfer To I/C Account
  COMMENT String*250 Comments
  MPRORATE BCD*10.3 Manual Proration
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  PRORATEAMT BCD*10.3 Prorated Amount
  CLEARACCT String*45 Transfer Clearing Account
  GITLOC String*6 Goods in Transit Location
  QTYREQ BCD*10.4 Quantity Requested
  UNITREQ String*10 Unit of Measure Qty Requested
  FACTORREQ BCD*10.6 Conversion Factor Qty Requested
  VALUES Long Optional Fields
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor

## ICTRANH - Transfer Audit List Headers (view IC0716)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ; DOCNUM+DAYENDSEQ+TRANSSEQ [D]; TRANSDATE+DAYENDSEQ+TRANSSEQ [D]
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  HDRDESC String*60 Description
  DOCNUM String*22 Transfer Number
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSTYPE Integer Transaction Type [1=Transfer,99=Sequence Header]
  PRINTED Boolean Printed
  ADDCOST BCD*10.3 Additional Cost
  PROMETHOD Integer Proration Method [1=Prorate by Quantity,2=Prorate by Weight,3=Prorate by Cost,4=Prorate Equally,5=Prorate Manually]
  MPRORATE BCD*10.3 Manual Proration
  DOCTYPE Integer Document Type [1=Transfer,2=Transit Transfer,3=Transit Receipt]
  FROMNUM String*22 From Transfer Number
  EXPARDATE Date Expected Arrival Date
  VALUES Long Optional Fields
  DATEBUS Date Posting Date

## ICTRED - Transfer Details (view IC0730)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ+LINENO
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Description
  FROMLOC String*6 From Location
  FRLOCDESC String*60 Description
  TOLOC String*6 To Location
  TOLOCDESC String*60 Description
  QUANTITY BCD*10.4 Quantity Transferred
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  COMMENTS String*250 Comments
  UNITCOST BCD*10.6 Unit Cost
  EXTCOST BCD*10.3 Extended Cost
  MPRORATE BCD*10.3 Manual Proration
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  MANITEMNO String*24 Manufacturer's Item Number
  GITLOC String*6 Goods in Transit Location
  GITLOCDESC String*60 Goods in Transit Location Desc
  DETAILNUM Integer Detail Line Number
  QTYREQ BCD*10.4 Quantity Requested
  UNITREQ String*10 Unit of Measure Qty Requested
  FACTORREQ BCD*10.6 Conversion Factor Qty Requested
  COMPLETE Integer Line Completed
  FROMTRNLNO Integer From Transfer Detail Line No.
  VALUES Long Optional Fields
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  AMTCONTROL BCD*10.3 GL Control Amount
  AUPRORATE BCD*10.3 Prorated Additional Cost
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SQTYMOVED Long Serial Quantity Received
  LQTYMOVED BCD*10.4 Lot Quantity Received

## ICTREDL - Transfer Detail Lot Numbers (view IC0733)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ+LINENO+LOTNUMF; LOTNUMF+TRANFENSEQ+LINENO
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
  LINENO Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  QTYMOVED BCD*10.4 Lot Quantity Received
  QTYMOVEDSQ BCD*10.4 Lot Qty Returned in Stocking UOM

## ICTREDO - Transfer Detail Optional Fields (view IC0735)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ+LINENO+OPTFIELD; OPTFIELD+TRANFENSEQ+LINENO
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
  LINENO Integer Line Number
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

## ICTREDS - Transfer Detail Serial Numbers (view IC0738)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ+LINENO+SERIALNUMF; SERIALNUMF+TRANFENSEQ+LINENO
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
  LINENO Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MOVED Boolean Serial Received

## ICTREH - Transfer Headers (view IC0740)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ; TRANSNUM [M]; STATUS+TRANSNUM [M]; DOCNUM; DOCUNIQ [D,M]; STATUS+DOCNUM [M]; DOCTYPE+DOCNUM+FROMNUM; DOCTYPE+FROMNUM+DOCNUM
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSNUM BCD*10.0 Transaction Number
  DOCNUM String*22 Document Number
  HDRDESC String*60 Description
  TRANSDATE Date Document Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1 ,2=2 ,3=3 ,4=4 ,5=5 ,6=6 ,7=7 ,8=8 ,9=9 ,10=10,11=11,12=12]
  REFERENCE String*60 Reference
  ADDCOST BCD*10.3 Additional Cost
  PRORMETHOD Integer Proration Method [1=Prorate by Quantity,2=Prorate by Weight,3=Prorate by Cost,4=Prorate Equally,5=Prorate Manually]
  MPRORATE BCD*10.3 Manual Proration
  DOCUNIQ BCD*10.0 IC-Unique Document Number
  STATUS Integer Record Status [1=Entered,2=Posted,3=Costed,20=Day End Completed]
  DELETED Boolean Record Deleted [0=No,1=Yes]
  DOCTYPE Integer Document Type [1=Transfer,2=Transit Transfer,3=Transit Receipt]
  FROMNUM String*22 From Transfer Number
  EXPARDATE Date Expected Arrival
  NEXTDTLNUM Integer Next Detail Line Number
  PRINTED Boolean Record Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  SLIPPRINT Boolean Transfer Slip Printed [0=No,1=Yes]
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## ICTREHO - Transfer Optional Fields (view IC0741)
Keys (first = PK; D=dups allowed, M=modifiable): TRANFENSEQ+OPTFIELD; OPTFIELD+TRANFENSEQ
Fields (NAME type description [values]):
  TRANFENSEQ Long Sequence Number
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

## ICTRID - Transit Transfer/Receipt Detail (view IC0743)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+DETAILNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  DETAILNUM Integer Detail Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTYREQ BCD*10.4 Quantity Requested
  QTYTRA BCD*10.4 Quantity Transfer to Date
  QTYREC BCD*10.4 Quantity Received to Date
  UNITREQ String*10 Unit of Measure Qty Requested
  FACTORREQ BCD*10.6 Conversion Factor Qty Requested
  TRCOMPLETE Integer Transit Completed

## ICTRIDL - Transfer Detail Lot Numbers (view IC0855)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+DETAILNUM+LOTNUMF; LOTNUMF+DOCNUM+DETAILNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  DETAILNUM Integer Detail Line No.
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  QTYRECEIVD BCD*10.4 Quantity Received
  QTYRECVDSQ BCD*10.4 Qty Received in Stocking UOM

## ICTRIDS - Transit Transfer/Receipt Detail Serial Numbers (view IC0860)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+DETAILNUM+SERIALNUMF; SERIALNUMF+DOCNUM+DETAILNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  DETAILNUM Integer Detail Line No.
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECEIVED Boolean Serial Number Received

## ICTRIH - Transit Transfer/Receipt Header (view IC0744)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ICTRIR - Transit Transfer/Receipt (view IC0745)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+TRANSNUM; TRANSNUM+DOCNUM; TRANSNUM
Fields (NAME type description [values]):
  DOCNUM String*22 Document Number
  TRANSNUM String*22 Transfer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ICTRNDP - Tfer Audit List Det. Opt. Fields (view IC0718)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+LINENO+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ+LINENO
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
  LINENO Integer Line Number
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

## ICTRNHP - Tfer Audit List Hdr Opt. Fields (view IC0720)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+TRANSSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+TRANSSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Transaction Sequence
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

## ICUCOD - Units of Measure (view IC0746)
Keys (first = PK; D=dups allowed, M=modifiable): UNIT
Fields (NAME type description [values]):
  UNIT String*10 Units of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFCONV BCD*10.6 Default Conversion Factor

## ICUNIQ - IC Document Uniquifiers (view IC0747)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer IC Uniquifier Dummy Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTRCP BCD*10.0 Next Receipt Number
  NEXTSHP BCD*10.0 Next Shipment Number
  NEXTADJ BCD*10.0 Next Adjustment Number
  NEXTXFER BCD*10.0 Next Transfer Number
  NEXTASS BCD*10.0 Next Assembly Number
  NEXTICS BCD*10.0 Next Internal Usage Number
  NEXTLSSEQ Long Next Serial/Lot Maintenance Entry Number

## ICUNIT - Units of Measure (view IC0750)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+UNIT; UNIT+ITEMNO [M]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  UNIT String*10 Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONVERSION BCD*10.6 Conversion Factor

## ICWCOD - Weight Units of Measure (view IC0758)
Keys (first = PK; D=dups allowed, M=modifiable): WEIGHTUNIT
Fields (NAME type description [values]):
  WEIGHTUNIT String*10 Weight Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WUOMDESC String*60 Description
  CONVERSION BCD*10.6 Weight Conversion Factor

## ICWKL - Inventory Worksheet (view IC0770)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTTYPE Integer Worksheet Status [1=Not Posted,3=Errors on Posting]
  DATE Date Date Created
  DESC String*60 Name
  COMMENT String*60 Worksheet Comment
  SORTBY Integer Sort Order [1=Item Number,2=Category,3=Item Segment,4=Picking Sequence]
  SORTBYDESC String*60 Sort Order Description
  SEGMENT Integer Segment Number [0= ]
  SEGDESC String*60 Segment Description
  FROMCODE String*60 From Code
  TOCODE String*60 To Code
  FRCNTLACCT String*6 From Account Set Code
  TOCNTLACCT String*6 To Account Set Code
  VALUES Long Optional Fields

## ICWKLO - Worksheet Optional Fields (view IC0775)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD; OPTFIELD+LOCATION
Fields (NAME type description [values]):
  LOCATION String*6 Location
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

## ICWKUD - Inventory Worksheet Details (view IC0780)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+SORTCODE+ITEMNO+UNIT
Fields (NAME type description [values]):
  LOCATION String*6 Location
  SORTCODE String*60 Sort Code
  ITEMNO String*24 Item Number
  UNIT String*10 Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTYCOUNTED BCD*10.4 Quantity Counted
  CONVERSION BCD*10.6 Conversion Factor

## ICWKUH - Inventory Worksheet Headers (view IC0790)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+SORTCODE+ITEMNO; LOCATION+ITEMNO+QTYVAR [M]
Fields (NAME type description [values]):
  LOCATION String*6 Location
  SORTCODE String*60 Sort Code
  ITEMNO String*24 Unformatted Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTITEMNO String*24 Item Number
  DESC String*60 Item Description
  PICKINGSEQ String*10 Picking Sequence
  QTYONHAND BCD*10.4 Quantity on Hand
  QTYCOUNTED BCD*10.4 Quantity Counted
  QTYVAR BCD*10.4 Quantity Variance
  STOCKUNIT String*10 Stocking Unit of Measure
  CALCCOST BCD*10.6 Estimated Unit Cost
  ADJCOST BCD*10.6 Adjustment Unit Cost
  COSTVAR BCD*10.3 Cost Variance
  ONHOLD Integer Status [1=Ready to post,2=On hold,3=Item does not exist,4=Non-stock item,5=Item not allowed at location,6=Insufficient quantity,7=Item not active]
  VALUES Long Optional Fields
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Lot Quantity
  SERIALCOST BCD*10.3 Serials' Cost
  LOTCOST BCD*10.3 Lots' Cost

## ICWKUHL - Inventory Worksheet Lot Numbers (view IC0793)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+SORTCODE+ITEMNO+LOTNUMF; LOTNUMF+LOCATION+SORTCODE+ITEMNO
Fields (NAME type description [values]):
  LOCATION String*6 Location
  SORTCODE String*60 Sort Code
  ITEMNO String*24 Unformatted Item Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM
  COST BCD*10.3 Lot Cost

## ICWKUHO - Worksheet Detail Optional Fields (view IC0795)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+SORTCODE+ITEMNO+OPTFIELD; OPTFIELD+LOCATION+SORTCODE+ITEMNO
Fields (NAME type description [values]):
  LOCATION String*6 Location
  SORTCODE String*60 Sort Code
  ITEMNO String*24 Unformatted Item Number
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

## ICWKUHS - Inventory Worksheet Serial Numbers (view IC0797)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+SORTCODE+ITEMNO+SERIALNUMF; SERIALNUMF+LOCATION+SORTCODE+ITEMNO
Fields (NAME type description [values]):
  LOCATION String*6 Location
  SORTCODE String*60 Sort Code
  ITEMNO String*24 Unformatted Item Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COST BCD*10.3 Serial Cost

## ICXCONT - Contract Codes (view IC0800)
Keys (first = PK; D=dups allowed, M=modifiable): CONTCODE
Fields (NAME type description [values]):
  CONTCODE String*6 Contract Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTDESC String*60 Description
  DAYS1 Long Days 1
  EFFDAYS1 Long Effective Days 1
  LIFECONT1 Boolean Lifetime Contract 1 [0=No,1=Yes]
  DESC1 String*60 Description 1
  DAYS2 Long Days 2
  EFFDAYS2 Long Effective Days 2
  LIFECONT2 Boolean Lifetime Contract 2 [0=No,1=Yes]
  DESC2 String*60 Description 2
  DAYS3 Long Days 3
  EFFDAYS3 Long Effective Days 3
  LIFECONT3 Boolean Lifetime Contract 3 [0=No,1=Yes]
  DESC3 String*60 Description 3
  DAYS4 Long Days 4
  EFFDAYS4 Long Effective Days 4
  LIFECONT4 Boolean Lifetime Contract 4 [0=No,1=Yes]
  DESC4 String*60 Description 4
  DAYS5 Long Days 5
  EFFDAYS5 Long Effective Days 5
  LIFECONT5 Boolean Lifetime Contract 5 [0=No,1=Yes]
  DESC5 String*60 Description 5

## ICXLHIS - Lot Number History (view IC0815)
Keys (first = PK; D=dups allowed, M=modifiable): LOTNUM+ITEMNUM+LOCATION+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM; ITEMNUM+LOCATION+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM+LOTNUM; APP+CUSTVEND+LOTNUM+ITEMNUM+TRANSDATE+TRANSTYPE [D,M]; APP+CUSTVEND+ITEMNUM+LOTNUM+TRANSDATE+TRANSTYPE [D,M]; DAYENDSEQ+ENTRYSEQ+LOTNUM+ITEMNUM+LOCATION+LINENO+COMPNUM; DOCNUM+DETAILNUM+LOTNUM+ITEMNUM+LOCATION+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM; TRANSDATE+ITEMNUM+LOTNUM+LOCATION+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM
Fields (NAME type description [values]):
  LOTNUM String*40 Unformatted Lot Number
  ITEMNUM String*24 Unformatted Item Number
  LOCATION String*6 Location
  DAYENDSEQ Long Day End Number
  ENTRYSEQ Long Transaction Sequence
  LINENO Integer Line Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  APP String*2 Source Application
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,3=Receipt Return,4=Shipment,5=Shipment Return,6=Adjustment Quantity Increase,7=Adjustment Quantity Decrease,8=Adjustment Cost Increase,9=Adjustment Cost Decrease,10=Adjustment Both Increase,11=Adjustment Both Decrease,12=Stock Transfer From,13=Stock Transfer To,14=Master Item Assembly,15=Component Item Assembly,16=Invoice,17=Credit Note,18=Debit Note,19=Shipment Adjustment,20=Internal Usage,100=Lot Recall,111=Lot Recall Release,112=Lot Combine,113=Lot Split,114=Lot Receipt,115=Lot Shipment,118=Lot OE Invoice,119=Lot PO Invoice]
  TRANSDATE Date Transaction Date
  QTY BCD*10.4 Transaction Quantity
  TRANSUOM String*10 Transaction Unit Of Measure
  TRANSCONV BCD*10.6 Transaction conversion Factor
  STKQTY BCD*10.4 Stock Quantity
  COST BCD*10.3 Extended Cost
  DOCNUM String*22 Document Number
  DETAILNUM Integer Detail Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  WARRCODE String*6 Warranty Code
  CUSTVEND String*12 Customer/Vendor Number
  RECALLED Boolean Recalled [0=No,1=Yes]
  RECALLDATE Date Date Recalled
  INUSE1 Boolean Warranty Period 1 Is In Use [0=No,1=Yes]
  DATE1 Date Warranty Period 1 Expiry Date
  EFFDATE1 Date Warranty Period 1 Effective Date
  LIFEWARR1 Boolean Warranty Period 1 Lifetime [0=No,1=Yes]
  INUSE2 Boolean Warranty Period 2 Is In Use [0=No,1=Yes]
  DATE2 Date Warranty Period 2 Expiry Date
  EFFDATE2 Date Warranty Period 2 Effective Date
  LIFEWARR2 Boolean Warranty Period 2 Lifetime [0=No,1=Yes]
  INUSE3 Boolean Warranty Period 3 Is In Use [0=No,1=Yes]
  DATE3 Date Warranty Period 3 Expiry Date
  EFFDATE3 Date Warranty Period 3 Effective Date
  LIFEWARR3 Boolean Warranty Period 3 Lifetime [0=No,1=Yes]
  INUSE4 Boolean Warranty Period 4 Is In Use [0=No,1=Yes]
  DATE4 Date Warranty Period 4 Expiry Date
  EFFDATE4 Date Warranty Period 4 Effective Date
  LIFEWARR4 Boolean Warranty Period 4 Lifetime [0=No,1=Yes]
  INUSE5 Boolean Warranty Period 5 Is In Use [0=No,1=Yes]
  DATE5 Date Warranty Period 5 Expiry Date
  EFFDATE5 Date Warranty Period 5 Effective Date
  LIFEWARR5 Boolean Warranty Period 5 Lifetime [0=No,1=Yes]
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  ENTEREDBY String*8 Entered By

## ICXLOT - Inventory Lot Numbers (view IC0810)
Keys (first = PK; D=dups allowed, M=modifiable): LOTNUM+ITEMNUM+LOCATION; ITEMNUM+LOTNUM [D,M]; LOCATION+ITEMNUM [D,M]; LOCATION+LOTNUM [D,M]; ITEMNUM+LOCATION+QTYLEVEL+LOTNUM [M]; ITEMNUM+LOCATION+QTYLEVEL+STOCKDATE+LOTNUM [M]; ITEMNUM+LOCATION+QTYLEVEL+EXPIRYDATE+LOTNUM [M]; STOCKDATE+QTYAVAIL+ASSETQTY+ITEMNUM+LOCATION+LOTNUM [M]
Fields (NAME type description [values]):
  LOTNUM String*40 Unformatted Lot Number
  ITEMNUM String*24 Unformatted Item Number
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTYAVAIL BCD*10.4 Quantity Available
  QTYORDED BCD*10.4 Quantity On order
  STOCKDATE Date Stock Date
  EXPIRYDATE Date Expiry Date
  QUARTRELDT Date Quarantine Release Date
  LOTNUMF String*40 Lot Number
  QTYLEVEL Integer Quantity Level [0=Quantity Zero,1=Quantity Above Zero,-1=Quantity Below Zero]
  ASSETQTY BCD*10.4 Quantity For Costing
  ASSETCOST BCD*10.3 Cost for Costing
  RECALLED Boolean Recalled [0=No,1=Yes]
  RECALLDATE Date Date Recalled
  CONTCODE String*6 Contract Code
  VALUES Long Optional Fields
  INUSE1 Boolean Contract Period 1 In Use [0=No,1=Yes]
  DATE1 Date Contract Period 1 Expiry Date
  EFFDATE1 Date Contract Period 1 Effective Date
  LIFECONT1 Boolean Contract Period 1 Lifetime [0=No,1=Yes]
  INUSE2 Boolean Contract Period 2 In Use [0=No,1=Yes]
  DATE2 Date Contract Period 2 Expiry Date
  EFFDATE2 Date Contract Period 2 Effective Date
  LIFECONT2 Boolean Contract Period 2 Lifetime [0=No,1=Yes]
  INUSE3 Boolean Contract Period 3 In Use [0=No,1=Yes]
  DATE3 Date Contract Period 3 Expiry Date
  EFFDATE3 Date Contract Period 3 Effective Date
  LIFECONT3 Boolean Contract Period 3 Lifetime [0=No,1=Yes]
  INUSE4 Boolean Contract Period 4 In Use [0=No,1=Yes]
  DATE4 Date Contract Period 4 Expiry Date
  EFFDATE4 Date Contract Period 4 Effective Date
  LIFECONT4 Boolean Contract Period 4 Lifetime [0=No,1=Yes]
  INUSE5 Boolean Contract Period 5 In Use [0=No,1=Yes]
  DATE5 Date Contract Period 5 Expiry Date
  EFFDATE5 Date Contract Period 5 Effective Date
  LIFECONT5 Boolean Contract Period 5 Lifetime [0=No,1=Yes]
  ONQUART Boolean Lot On Quarantine [0=No,1=Yes]
  ONQUARTDT Date Date Quarantineed

## ICXLOTO - Lot Optional Fields (view IC0812)
Keys (first = PK; D=dups allowed, M=modifiable): LOTNUM+ITEMNUM+LOCATION+OPTFIELD; OPTFIELD+LOTNUM+ITEMNUM+LOCATION
Fields (NAME type description [values]):
  LOTNUM String*40 Unformatted Lot Number
  ITEMNUM String*24 Unformatted Item Number
  LOCATION String*6 Location
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

## ICXMASK - Mask Structures (view IC0805)
Keys (first = PK; D=dups allowed, M=modifiable): MASKCODE+MASKTYPE; MASKTYPE+MASKCODE
Fields (NAME type description [values]):
  MASKCODE String*6 Structure Code
  MASKTYPE Integer Mask Type [1=Serial,2=Lot]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  PREFIX Integer Prefix [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  SEGTYPE1 Integer Segment Type 1 [1=All Characters,2=Numeric]
  SEGTYPE2 Integer Segment Type 2 [1=All Characters,2=Numeric]
  SEGTYPE3 Integer Segment Type 3 [1=All Characters,2=Numeric]
  SEGTYPE4 Integer Segment Type 4 [1=All Characters,2=Numeric]
  SEGTYPE5 Integer Segment Type 5 [1=All Characters,2=Numeric]
  SEGLEN1 Integer Segment Length 1
  SEGLEN2 Integer Segment Length 2
  SEGLEN3 Integer Segment Length 3
  SEGLEN4 Integer Segment Length 4
  SEGLEN5 Integer Segment Length 5
  SEGSEPAR1 Integer Segment Separator 1 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  SEGSEPAR2 Integer Segment Separator 2 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  SEGSEPAR3 Integer Segment Separator 3 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  SEGSEPAR4 Integer Segment Separator 4 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  SEGSEPAR5 Integer Segment Separator 5 [1=None,2=-  Hyphen,3=/  Forward Slash,4=\  Back Slash,5=*  Asterisk,6=.  Period,7=(  Left Parenthesis,8=)  Right Parenthesis,9=#  Number Sign,10=[  Left Bracket,11=]  Right Bracket,12={  Left Brace,13=}  Right Brace]
  INCREMEN1 Boolean Increment 1 [0=No,1=Yes]
  INCREMEN2 Boolean Increment 2 [0=No,1=Yes]
  INCREMEN3 Boolean Increment 3 [0=No,1=Yes]
  INCREMEN4 Boolean Increment 4 [0=No,1=Yes]
  INCREMEN5 Boolean Increment 5 [0=No,1=Yes]

## ICXRCD - Recall/Release Details (view IC0820)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOCATION String*6 Location
  QUANTITY BCD*10.4 Quantity
  UNIT String*10 Unit of Measure
  DETAILNUM Integer Detail Line Number

## ICXRCH - Recall/Release Headers (view IC0822)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; DOCNUM [M]
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*22 Document Number
  LOTNUM String*40 Lot Number
  TRANSTYPE Integer Entry Type [1=Recall,2=Release]
  TRANSDATE Date Transaction Date
  RECALLNUM String*22 Recall Number
  ITEMNO String*24 Item Number
  NEXTDTLNUM Integer Next Detail Line Number
  PRINTED Boolean Record Printed [0=No,1=Yes]

## ICXRECN - Reconciliation Headers (view IC0825)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; DOCNUM [M]
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*22 Document Number
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  TRANSDATE Date Transaction Date
  TRANSTYPE Integer Transaction Type [0=Receipt,1=Shipment,2=OE Invoice,3=PO Invoice]
  STOCKUNIT String*10 Stock Unit of Measure
  QUANTITY BCD*10.4 Quantity
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  APPLYTODOC String*22 Apply To Invoice Number
  ASSETCOST BCD*10.3 Cost

## ICXRECNL - Lot Reconciliation Details (view IC0827)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LOTNUMF; LOTNUMF+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Quantity
  QTYSQ BCD*10.4 Lot Quantity in Stocking UOM

## ICXRECNS - Serial Reconciliation Details (view IC0828)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+SERIALNUMF; SERIALNUMF+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ICXSCD - Split/Combine Details (view IC0845)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+LINENO; SEQUENCENO+LOTNUMF
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOTNUMF String*40 Lot Number
  LOCATION String*6 Location
  UOM String*10 Unit of Measure
  QTYAVAIL BCD*10.4 Quantity Shippable
  QUANTITY BCD*10.4 Quantity
  DETAILNUM Integer Detail Line Number
  EXPIRYDATE Date Expiry Date
  STOCKDATE Date Stock Date

## ICXSCH - Split/Combine Headers (view IC0843)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO; DOCNUM [M]
Fields (NAME type description [values]):
  SEQUENCENO BCD*10.0 Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*22 Document Number
  LOTNUMF String*40 Lot Number
  LOCATION String*6 Location
  TRANSTYPE Integer Entry Type [1=Split,2=Combine]
  TRANSDATE Date Transaction Date
  ITEMNO String*24 Item Number
  UOM String*10 Unit of Measure
  QTYAVAIL BCD*10.4 Quantity Shippable
  QUANTITY BCD*10.4 Split/Combine Quantity
  QTYDTLSTOT BCD*10.4 Total of Detail Quantities
  NEXTDTLNUM Integer Next Detail Line Number
  EXPIRYDATE Date Expiry Date
  STOCKDATE Date Stock Date
  DTLCOUNT Integer Detail Count

## ICXSER - Inventory Serial Numbers (view IC0830)
Keys (first = PK; D=dups allowed, M=modifiable): SERIALNUM+ITEMNUM; ITEMNUM+SERIALNUM; ITEMNUM+LOCATION+STATUS+RESVFORORD [D,M]; ITEMNUM+LOCATION+STATUS+SERIALNUM [M]; ITEMNUM+LOCATION+STATUS+STOCKDATE+SERIALNUM [M]; ITEMNUM+LOCATION+STATUS+EXPIRYDATE+SERIALNUM [M]; STOCKDATE+STATUS+ASSETSTOCK+ITEMNUM+LOCATION+SERIALNUM [M]
Fields (NAME type description [values]):
  SERIALNUM String*40 Unformatted Serial Number
  ITEMNUM String*24 Unformatted Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOCATION String*6 Location
  STATUS Integer Status [0=Not Available,1=Available]
  STOCKDATE Date Stock Date
  EXPIRYDATE Date Expiry Date
  SERIALNUMF String*40 Serial Number
  RESVFORORD Boolean Reserve For Order [0=No,1=Yes]
  ASSETSTOCK Integer Stocked for Costing
  ASSETCOST BCD*10.3 Cost for Costing
  CONTCODE String*6 Contract Code
  VALUES Long Optional Fields
  INUSE1 Boolean Contract Period 1 In Use [0=No,1=Yes]
  DATE1 Date Contract Period 1 Expiry Date
  EFFDATE1 Date Contract Period 1 Effective Date
  LIFECONT1 Boolean Contract Period 1 Lifetime [0=No,1=Yes]
  INUSE2 Boolean Contract Period 2 In Use [0=No,1=Yes]
  DATE2 Date Contract Period 2 Expiry Date
  EFFDATE2 Date Contract Period 2 Effective Date
  LIFECONT2 Boolean Contract Period 2 Lifetime [0=No,1=Yes]
  INUSE3 Boolean Contract Period 3 In Use [0=No,1=Yes]
  DATE3 Date Contract Period 3 Expiry Date
  EFFDATE3 Date Contract Period 3 Effective Date
  LIFECONT3 Boolean Contract Period 3 Lifetime [0=No,1=Yes]
  INUSE4 Boolean Contract Period 4 In Use [0=No,1=Yes]
  DATE4 Date Contract Period 4 Expiry Date
  EFFDATE4 Date Contract Period 4 Effective Date
  LIFECONT4 Boolean Contract Period 4 Lifetime [0=No,1=Yes]
  INUSE5 Boolean Contract Period 5 In Use [0=No,1=Yes]
  DATE5 Date Contract Period 5 Expiry Date
  EFFDATE5 Date Contract Period 5 Effective Date
  LIFECONT5 Boolean Contract Period 5 Lifetime [0=No,1=Yes]

## ICXSERO - Serial Optional Fields (view IC0832)
Keys (first = PK; D=dups allowed, M=modifiable): SERIALNUM+ITEMNUM+OPTFIELD; OPTFIELD+SERIALNUM+ITEMNUM
Fields (NAME type description [values]):
  SERIALNUM String*40 Unformatted Serial Number
  ITEMNUM String*24 Unformatted Item Number
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

## ICXSHIS - Serial Number History (view IC0835)
Keys (first = PK; D=dups allowed, M=modifiable): SERIALNUM+ITEMNUM+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM; ITEMNUM+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM+SERIALNUM; APP+CUSTVEND+SERIALNUM+ITEMNUM+TRANSDATE+TRANSTYPE [D,M]; APP+CUSTVEND+ITEMNUM+SERIALNUM+TRANSDATE+TRANSTYPE [D,M]; DAYENDSEQ+ENTRYSEQ+SERIALNUM+ITEMNUM+LINENO+COMPNUM; DOCNUM+DETAILNUM+SERIALNUM+ITEMNUM+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM; APP+TRANSTYPE+DOCNUM+ITEMNUM+SERIALNUM+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM; TRANSDATE+ITEMNUM+SERIALNUM+DAYENDSEQ+ENTRYSEQ+LINENO+COMPNUM
Fields (NAME type description [values]):
  SERIALNUM String*40 Unformatted Serial Number
  ITEMNUM String*24 Unformatted Item Number
  DAYENDSEQ Long Day End Number
  ENTRYSEQ Long Transaction Sequence
  LINENO Integer Line Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOCATION String*6 Location
  APP String*2 Source Application
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,3=Receipt Return,4=Shipment,5=Shipment Return,6=Adjustment Quantity Increase,7=Adjustment Quantity Decrease,8=Adjustment Cost Increase,9=Adjustment Cost Decrease,10=Adjustment Both Increase,11=Adjustment Both Decrease,12=Stock Transfer From,13=Stock Transfer To,14=Master Item Assembly,15=Component Item Assembly,16=Invoice,17=Credit Note,18=Debit Note,19=Shipment Adjustment,20=Internal Usage,116=Serial Receipt,117=Serial Shipment,120=Serial OE Invoice,121=Serial PO Invoice]
  TRANSDATE Date Transaction Date
  STOCKED Integer Stocked
  COST BCD*10.3 Extended Cost
  DOCNUM String*22 Document Number
  DETAILNUM Integer Detail Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  WARRCODE String*6 Warranty Code
  REGISTERED Boolean Registered [0=No,1=Yes]
  REGISTDATE Date Date Registered
  CUSTVEND String*12 Customer/Vendor Number
  INUSE1 Boolean Warranty Period 1 Is In Use [0=No,1=Yes]
  DATE1 Date Warranty Period 1 Expiry Date
  EFFDATE1 Date Warranty Period 1 Effective Date
  LIFEWARR1 Boolean Warranty Period 1 Lifetime [0=No,1=Yes]
  INUSE2 Boolean Warranty Period 2 Is In Use [0=No,1=Yes]
  DATE2 Date Warranty Period 2 Expiry Date
  EFFDATE2 Date Warranty Period 2 Effective Date
  LIFEWARR2 Boolean Warranty Period 2 Lifetime [0=No,1=Yes]
  INUSE3 Boolean Warranty Period 3 Is In Use [0=No,1=Yes]
  DATE3 Date Warranty Period 3 Expiry Date
  EFFDATE3 Date Warranty Period 3 Effective Date
  LIFEWARR3 Boolean Warranty Period 3 Lifetime [0=No,1=Yes]
  INUSE4 Boolean Warranty Period 4 Is In Use [0=No,1=Yes]
  DATE4 Date Warranty Period 4 Expiry Date
  EFFDATE4 Date Warranty Period 4 Effective Date
  LIFEWARR4 Boolean Warranty Period 4 Lifetime [0=No,1=Yes]
  INUSE5 Boolean Warranty Period 5 Is In Use [0=No,1=Yes]
  DATE5 Date Warranty Period 5 Expiry Date
  EFFDATE5 Date Warranty Period 5 Effective Date
  LIFEWARR5 Boolean Warranty Period 5 Lifetime [0=No,1=Yes]
  DRILSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link Number
  ENTEREDBY String*8 Entered By

## ICXWARY - Warranty Codes (view IC0850)
Keys (first = PK; D=dups allowed, M=modifiable): WARRCODE
Fields (NAME type description [values]):
  WARRCODE String*6 Warranty Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WARRDESC String*60 Description
  DAYS1 Long Period 1 Days
  EFFDAYS1 Long Period 1 Effective Days
  LIFEWARR1 Boolean Period 1 is Lifetime [0=No,1=Yes]
  DESC1 String*60 Period 1 Description
  DAYS2 Long Period 2 Days
  EFFDAYS2 Long Period 2 Effective Days
  LIFEWARR2 Boolean Period 2 is Lifetime [0=No,1=Yes]
  DESC2 String*60 Period 2 Description
  DAYS3 Long Period 3 Days
  EFFDAYS3 Long Period 3 Effective Days
  LIFEWARR3 Boolean Period 3 is Lifetime [0=No,1=Yes]
  DESC3 String*60 Period 3 Description
  DAYS4 Long Period 4 Days
  EFFDAYS4 Long Period 4 Effective Days
  LIFEWARR4 Boolean Period 4 is Lifetime [0=No,1=Yes]
  DESC4 String*60 Period 4 Description
  DAYS5 Long Period 5 Days
  EFFDAYS5 Long Period 5 Effective Days
  LIFEWARR5 Boolean Period 5 is Lifetime [0=No,1=Yes]
  DESC5 String*60 Period 5 Description
