# TK module - compiled AOM dictionary

## TKAUDH - VAT Return Audit Header (view TK0410)
Keys (first = PK; D=dups allowed, M=modifiable): FROMDATE+TODATE
Fields (NAME type description [values]):
  FROMDATE Date From Date
  TODATE Date To Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXREG String*60 Tax Number

## TKAUGL - VAT Return Audit Details - GL (view TK0414)
Keys (first = PK; D=dups allowed, M=modifiable): FROMDATE+TODATE+BOX+POSTINGSEQ+CNTDETAIL+DOCDATE; FROMDATE+TODATE+BOX+ACCTID [D,M]
Fields (NAME type description [values]):
  FROMDATE Date From Date
  TODATE Date To Date
  BOX Integer Box Number
  POSTINGSEQ BCD*4.0 Posting Sequence Number
  CNTDETAIL BCD*4.0 Detail Count
  DOCDATE Date Document Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTID String*45 Account Number
  SRCELEDGER String*2 Source Ledger Code
  SRCETYPE String*2 Source Type Code
  JNLDTLDESC String*60 Journal Detail Dscription
  JNLDTLREF String*60 Journal Detail Description
  AMOUNT BCD*10.3 Amount

## TKAUTX - VAT Return Audit Details - TX (view TK0412)
Keys (first = PK; D=dups allowed, M=modifiable): FROMDATE+TODATE+BOX+SEQUENCE+ITEMCLASS+DOCDATE; FROMDATE+TODATE+BOX+AUTHORITY [D,M]
Fields (NAME type description [values]):
  FROMDATE Date From Date
  TODATE Date To Date
  BOX Integer Box Number
  SEQUENCE BCD*10.0 Sequence
  ITEMCLASS Integer Number Of Details
  DOCDATE Date Document Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AUTHORITY String*12 Tax Authority
  BUYERCLASS Integer Cust/Vend Tax Class
  DOCNUMBER String*22 Document No.
  SRCEAPP String*2 Source Application
  DOCTYPE String*2 Document Type
  CUSTVENDNM String*60 Customer/Vendor Name
  AMOUNT BCD*10.3 Amount

## TKBOXD - VAT Configuration Detail (view TK0200)
Keys (first = PK; D=dups allowed, M=modifiable): BOX+DETAILNUM; BOX+GLACCT+TAXAUTH+TTYPE+BUYERCLASS+ITEMCLASS
Fields (NAME type description [values]):
  BOX Integer Box Number
  DETAILNUM BCD*10.0 Detail Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FROM Integer From GL or TX? [1=General Ledger,2=Tax Services]
  GLACCT String*45 GL Account Number
  TAXAUTH String*12 Tax Authority
  BUYERCLASS Integer Customer/Vendor Tax Class
  ITEMCLASS Integer Item Tax Class
  TTYPE Integer Transaction Type [1=Sales,2=Purchases,3=Not Applicable]

## TKBOXH - VAT Configuration Header (view TK0300)
Keys (first = PK; D=dups allowed, M=modifiable): BOX
Fields (NAME type description [values]):
  BOX Integer Box Number [1=1 - VAT due in this period on sales and other outputs,2=2 - VAT due in this period on acquisitions from other EC member states,4=4 - VAT reclaimed in this period on purchases and other inputs (including acquisitions from the EC),6=6 - Total value of sales and all other outputs excluding any VAT,7=7 - Total value of purchases and all other inputs excluding any VAT,8=8 - Total sales of goods/related services, excluding VAT, to EC member states,9=9 - Total goods/related services acquisitions, excluding VAT, from EC member states]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NUMDETAIL Integer Number Of Details

## TKGBAS - Generate VAT Worksheet (view TK0400)
Keys (first = PK; D=dups allowed, M=modifiable): FROMDATE+TODATE
Fields (NAME type description [values]):
  FROMDATE Date From Date
  TODATE Date To Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CALB1 BCD*10.3 Calculated B1
  PMB1 BCD*10.3 Plus OR Minus B1
  CALB2 BCD*10.3 Calculated B2
  PMB2 BCD*10.3 Plus OR Minus B2
  CALB3 BCD*10.3 Calculated B3
  CALB4 BCD*10.3 Calculated B4
  PMB4 BCD*10.3 Plus OR Minus B4
  CALB5 BCD*10.3 Calculated B5
  CALB6 BCD*10.3 Calculated B6
  PMB6 BCD*10.3 Plus OR Minus B6
  CALB7 BCD*10.3 Calculated B7
  PMB7 BCD*10.3 Plus OR Minus B7
  CALB8 BCD*10.3 Calculated B8
  PMB8 BCD*10.3 Plus OR Minus B8
  CALB9 BCD*10.3 Calculated B9
  PMB9 BCD*10.3 Plus OR Minus B9
  STATUS Integer Status [0=Not Submitted,1=Not Submitted,2=Submitted]
  JSONFILE String*255 JSON Submit File Name
  MISSED Boolean Include unreported transactions dated on or after
  BACKDATE Date

## TKTBOXD - VAT Worksheet Detail Amounts (view TK0580)
Keys (first = PK; D=dups allowed, M=modifiable): FROMDATE+TODATE+BOX+DETAILNUM
Fields (NAME type description [values]):
  FROMDATE Date From Date
  TODATE Date To Date
  BOX Integer Box Number [1=1 - VAT due in this period on sales and other outputs,2=2 - VAT due in this period on acquisitions from other EC member states,4=4 - VAT reclaimed in this period on purchases and other inputs (including acquisitions from the EC),6=6 - Total value of sales and all other outputs excluding any VAT,7=7 - Total value of purchases and all other inputs excluding any VAT,8=8 - Total sales of goods/related services, excluding VAT, to EC member states,9=9 - Total goods/related services acquisitions, excluding VAT, from EC member states]
  DETAILNUM BCD*10.0 Detail Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FROM Integer From GL or TX? [1=General Ledger,2=Tax Services]
  GLACCT String*45 GL Account Number
  TAXAUTH String*12 Tax Authority
  BUYERCLASS Integer Customer/Vendor Tax Class
  ITEMCLASS Integer Item Tax Class
  AMOUNT BCD*10.3 Amount
  TTYPE Integer Transaction Type [1=Sales,2=Purchases,3=Not Applicable]
