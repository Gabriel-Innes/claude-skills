# TS module - compiled AOM dictionary

## TSEFAUD - GST eFiling Audit (view TS0215)
Keys (first = PK; D=dups allowed, M=modifiable): FORMTYPE+FROMYEAR+FROMPERIOD+TOYEAR+TOPERIOD
Fields (NAME type description [values]):
  FORMTYPE Integer GST Form Type [1=F5,2=F8]
  FROMYEAR String*4 From Year
  FROMPERIOD Integer From Period
  TOYEAR String*4 To Year
  TOPERIOD Integer To Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CEJOBNUM String*100 Cloud Enablement Job Number
  DATEFILED Date Date Submitted
  TIMEFILED Time Time Submitted
  IRASCONNUM String*20 IRAS Confirmation Number
  STATUS Integer Status [0=None,1=Sent,2=Failed]
  TAXNBR String*20 Tax Number
  TITLE String*60 Declarant Designation
  CONTACT String*60 Contact Person
  PHONE String*30 Contact Telephone
  EMAIL String*50 Contact Email

## TSGAUD - GST F5 Audit (view TS0180)
Keys (first = PK; D=dups allowed, M=modifiable): GSTRPTFLD+DETAILSEQ+UNIQUE
Fields (NAME type description [values]):
  GSTRPTFLD String*10 GST Report Field
  DETAILSEQ BCD*10.0 Detail Sequence
  UNIQUE BCD*10.0 Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCDATE Date Document Date
  DOCNUMBER String*22 Document Number
  RLGALOXREF String*22 Realized Gain/Loss Reference
  AUTHORITY String*12 Tax Authority
  TTYPE Integer Transaction Type [0=Exchange,1=Sales,2=Purchase]
  BUYERCLASS Integer Customer/Vendor Class
  BUYERCLASD String*60 Customer/Vendor Class Description
  ITEMCLASS Integer Item Class
  ITEMCLASSD String*60 Item Class Description
  TAXRCODE String*10 Tax Code
  TBASEAMT BCD*10.3 Tax Base Amount
  TCURNTAX BCD*10.3 Tax Amount
  TOTALWTAX BCD*10.3 Document Amount
  CUSTVEND String*12 Customer/Vendor Number
  CUSTVENDNM String*60 Customer/Vendor Name
  POSTDATE Date Posting Date
  DESCRIPTIO String*60 Description
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  SRCEAPP String*2 Source ID

## TSGLT - GL Audit Transactions (view TS0650)
Keys (first = PK; D=dups allowed, M=modifiable): POSTINGSEQ+BATCHNBR+ENTRYNBR; TRANSID [D,M]
Fields (NAME type description [values]):
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  BATCHNBR String*6 Batch Number
  ENTRYNBR String*5 Journal Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSID Long Transaction ID

## TSRCODE - Tax Rate Codes (view TS0400)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+AUTHORITY+TTYPE+BUYERCLASS+ITEMCLASS; AUTHORITY+EFFDATE+TTYPE+BUYERCLASS+ITEMCLASS
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  AUTHORITY String*12 Tax Authority
  TTYPE Integer Transaction Type
  BUYERCLASS Integer Buyer Class
  ITEMCLASS Integer Item Class
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXRCODE String*10 Tax Rate Code

## TSRECOND - Tax Reconciliation Detail (view TS0432)
Keys (first = PK; D=dups allowed, M=modifiable): RUNID+TTYPE+TAXRCODE+DETAILSEQ+UNIQUE
Fields (NAME type description [values]):
  RUNID Long Run ID
  TTYPE Integer Transaction Type [1=Sales,2=Purchase]
  TAXRCODE String*10 Tax Code
  DETAILSEQ BCD*10.0 Detail Sequence
  UNIQUE BCD*10.0 Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCDATE Date Document Date
  DOCNUMBER String*22 Document Number
  RLGALOXREF String*22 Realized Gain/Loss Reference
  AUTHORITY String*12 Tax Authority
  BUYERCLASS Integer Customer/Vendor Class
  BUYERCLASD String*60 Customer/Vendor Class Description
  ITEMCLASS Integer Item Class
  ITEMCLASSD String*60 Item Class Description
  TBASEAMT BCD*10.3 Tax Base Amount
  TCURNTAX BCD*10.3 Tax Amount
  TOTALWTAX BCD*10.3 Document Amount
  CUSTVEND String*12 Customer/Vendor Number
  CUSTVENDNM String*60 Customer/Vendor Name
  POSTDATE Date Posting Date
  DESCRIPTIO String*60 Description
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  SRCEAPP String*2 Source ID

## TSRECONH - Tax Reconciliation Total (view TS0434)
Keys (first = PK; D=dups allowed, M=modifiable): RUNID+TTYPE+TAXRCODE
Fields (NAME type description [values]):
  RUNID Long Run ID
  TTYPE Integer Transaction Type [1=Sales,2=Purchase]
  TAXRCODE String*10 Tax Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TBASEAMT BCD*10.3 Tax Base Total
  TCURNTAX BCD*10.3 Tax Total
  TOTALWTAX BCD*10.3 Document Total

## TSTXMAP - Singapore GST Tax Codes (view TS0500)
Keys (first = PK; D=dups allowed, M=modifiable): EFFDATE+TAXRCODE+TTYPE
Fields (NAME type description [values]):
  EFFDATE Date Effective Date
  TAXRCODE String*10 Tax Code
  TTYPE Integer Transaction Type [1=Sales,2=Purchase]
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
