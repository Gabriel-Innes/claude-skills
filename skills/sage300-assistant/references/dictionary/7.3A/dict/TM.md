# TM module - compiled AOM dictionary

## TMAUDD - GST 03 Detail (view TM0100)
Keys (first = PK; D=dups allowed, M=modifiable): SESSION+GSTRPTFLD+DETAILSEQ
Fields (NAME type description [values]):
  SESSION BCD*10.0 Session Number
  GSTRPTFLD String*10 GST Report Field
  DETAILSEQ BCD*10.0 Detail Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCDATE Date Document Date
  DOCNUMBER String*22 Document Number
  TAXRCODE String*10 Tax Code
  TBASEAMT BCD*10.3 Tax base Amount
  TCURNTAX BCD*10.3 Tax Amount
  CUSTVEND String*12 Customer/Vendor Number
  CUSTVENDNM String*60 Customer/Vendor Name
  POSTDATE Date Posting Date
  DESCRIPTIO String*60 Description
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  SRCEAPP String*10 Source ID

## TMEXID - Execution ID Audit (view TM0300)
Keys (first = PK; D=dups allowed, M=modifiable): EXID
Fields (NAME type description [values]):
  EXID String*18 Execution ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATUS Integer Filing Status [0=None,1=Initiated,2=Filed]
  BYUSER String*8 Filed By

## TMOPTION - Malaysia Tax Reports Options (view TM0007)
Keys (first = PK; D=dups allowed, M=modifiable): OPTION
Fields (NAME type description [values]):
  OPTION String*100 Option
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FOREXDATE Date Forex Date
  FRXENABLE Integer Forex Enable [-1=Checked,0=Unchecked]
  SALESTAXNO String*100 Sales Tax No.
  SRVCETAXNO String*100 Service Tax No.
  TARIFFLINK Integer Link Tariff Codes To [1=A/R Items,2=I/C Items]

## TMRCODE - Tax Code Mapping (view TM0006)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+AUTHORITY+TTYPE+BUYERCLASS+ITEMCLASS
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  AUTHORITY String*12 Tax Authority
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  BUYERCLASS Integer Buyer Class
  ITEMCLASS Integer Item Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXRCODE String*10 Tax Code

## TMSAUDD - SST 02 Detail (view TM0051)
Keys (first = PK; D=dups allowed, M=modifiable): SESSION+SSTRPTFLD+DETAILSEQ
Fields (NAME type description [values]):
  SESSION BCD*10.0 Session Number
  SSTRPTFLD String*10 SST Report Field
  DETAILSEQ BCD*10.0 Detail Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCDATE Date Document Date
  DOCNUMBER String*22 Document Number
  LINENUM Integer Line Number
  TAXRCODE String*10 Tax Code
  TARIFF String*20 Tariff
  QUANTITY BCD*10.5 Quantity
  TAXRATE BCD*8.5 Tax Rate
  TBASEAMT BCD*10.3 Tax base Amount
  TCURNTAX BCD*10.3 Tax Amount
  CUSTVEND String*12 Customer/Vendor Number
  CUSTVENDNM String*60 Customer/Vendor Name
  POSTDATE Date Posting Date
  DESCRIPTIO String*60 Description
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  SRCEAPP String*10 Source ID

## TMSRCODE - SST Tax Code Mapping (view TM0056)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+AUTHORITY+TTYPE+BUYERCLASS+ITEMCLASS
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  AUTHORITY String*12 Tax Authority
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  BUYERCLASS Integer Buyer Class
  ITEMCLASS Integer Item Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXRCODE String*10 Tax Code

## TMSRDC - Malaysia Tax Distribution Codes (view TM0055)
Keys (first = PK; D=dups allowed, M=modifiable): IDDIST
Fields (NAME type description [values]):
  IDDIST String*6 Distribution Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TARIFFCODE String*20 Tariff Code

## TMSTXMAP - Malaysia SST Tax Codes (view TM0053)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+TAXRCODE+TTYPE
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  TAXRCODE String*10 Tax Code
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*250 Description
  REMARK String*250 Remark
  DEPRECATED Integer Deprecated [0=No,1=Yes]
  REPLACEDBY String*10 Replacement
  FIELD1 String*10 Field 1
  FIELD2 String*10 Field 2
  FIELD3 String*10 Field 3
  FIELD4 String*10 Field 4
  FIELD5 String*10 Field 5
  TAXTYPE Integer Tax Type [1=Sales Tax,2=Service Tax]

## TMTARC - Malaysia SST Tariff Codes (view TM0054)
Keys (first = PK; D=dups allowed, M=modifiable): TARIFF
Fields (NAME type description [values]):
  TARIFF String*20 Tariff Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*250 Description
  STATUS Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Date last modified

## TMTXMAP - Malaysia GST Tax Codes (view TM0003)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+TAXRCODE+TTYPE
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  TAXRCODE String*10 Tax Code
  TTYPE Integer Transaction Type [1=Sales,2=Purchases]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*250 Description
  REMARK String*250 Remark
  DEPRECATED Integer Deprecated [0=No,1=Yes]
  REPLACEDBY String*10 Replacement
  FIELD1 String*10 Field 1
  FIELD2 String*10 Field 2
  FIELD3 String*10 Field 3
  FIELD4 String*10 Field 4
  FIELD5 String*10 Field 5
