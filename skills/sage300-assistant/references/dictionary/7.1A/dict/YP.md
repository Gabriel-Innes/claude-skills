# YP module - compiled AOM dictionary

## YPMID - Processing Codes (view YP0500)
Keys (first = PK; D=dups allowed, M=modifiable): PROCESSCOD; BANK+CURRENCY [D]; CURRENCY+BANK [D]
Fields (NAME type description [values]):
  PROCESSCOD String*12 Processing Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  BANK String*8 Bank
  CURRENCY String*3 Currency Code
  MERCHID String*12 Merchant ID
  MERCHINFO Binary*16 Merchant Information

## YPOPT - Options (view YP0407)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PHONE String*30 Phone
  FAX String*30 Fax
  CONTACT String*60 Contact Name
  SWCAPTURE Integer Require invoicing at shipping [0=No,1=Yes]
  SWCFMFORCE Integer Warn Before Forcing Expired Pre-authorizations [0=No,1=Yes]
  SWAPPLYDIS Integer Terms disc. on Automatic Payments? [0=No,1=Yes]

## YPPMTINF - Payment Info (view YP0406)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST+IDCARD; PROCESSCOD+IDCUST+IDCARD [M]
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  IDCARD String*12 Card ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Card Description
  CARDTYPE Integer Card Type [0=,3=American Express,4=Visa,5=MasterCard,6=Discover,7=JCB,68=Debit Card]
  PROCESSCOD String*12 Processing Code
  DATELASTMN Date Date Last Maintained
  SWACTV Integer Status [0=Inactive,1=Active]
  DATEINACTV Date Inactive Date
  SWDEFCARD Integer Default Card [0=No,1=Yes]
  NAMEONCARD String*103 Cardholder Name
  BLADDR1 String*50 Billing Address Line 1
  BLADDR2 String*50 Billing Address Line 2
  BLCITY String*50 Billing City
  BLSTATE String*50 Billing State
  BLCOUNTRY String*50 Billing Country
  BLZIPCODE String*50 Billing Zipcode
  VAULTID String*36 Vault ID
  CARDNUMBER String*30 Masked Card Number
  EXPDATE String*4 Expiration Date
  CARDCMNT String*255 Comment
  SWAUTOPAY Integer Allow Auto Pay [0=No,1=Yes]

## YPTRAN - Transaction Log (view YP0700)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSID
Fields (NAME type description [values]):
  TRANSID String*36 Transaction ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BANK String*8 Bank
  CODECURN String*3 Currency Code
  ACTION Integer Action
  RESPIND String*1 Response Indicator
  RESPCD String*6 Response Code
  RESPMSG String*32 Response Message
  GUID String*36 GUID from message
  EXPDATE String*4 Expire Date
  LAST4 String*16 Last 4
  PMTDESC String*30 Payment Description
  PMTTYPEID String*1 Payment Type ID
  REF1 String*50 Reference1
  REF2 String*50 Reference2
  AMOUNT BCD*10.3 Amount
  AUTHCODE String*6 Authorization Code
  VANREF String*16 VANReference
  NAME String*103 Name
  ADDR1 String*50 Address Line1
  ADDR2 String*50 Address Line2
  CITY String*50 City
  STATE String*50 State
  ZIPCODE String*50 Zip Code
  COUNTRY String*50 Country
  EMAIL String*255 Email
  TEL String*50 Telephone
  FAX String*50 Fax
  AVSRESULT String*1 AVSResult
  CVVRESULT String*1 CVVResult
  TIMESTAMP String*22 Timestamp
  BATCHREF String*10 Batch Reference
  SETLTYPE String*1 Settlement Type
  SETLDATE String*22 Settlement Date
  TRANSTYPE String*2 Transaction Type
  DTPROCESS Date Processing Date
  TAXAMOUNT String*9 Tax Amount
  IDCUST String*12 Customer Number
  PROCESSCOD String*12 Processing Code
  IDCARD String*12 Card ID
  DOCNUMBER String*22 Document Number
  CARDDESC String*60 Card Description
  CARDCMNT String*255 Card Comment
  ISCOMPLETE Integer SPS Request Process Completed Flag [0=No,1=Yes]
  APP String*2 Application
