# TW module - compiled AOM dictionary

## TWBOXD - GST Configuration Detail (view TW0200)
Keys (first = PK; D=dups allowed, M=modifiable): BOX+DETAILNUM; BOX+GLACCT+TAXAUTH+BUYERCLASS+ITEMCLASS
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

## TWBOXH - GST Configuration Header (view TW0300)
Keys (first = PK; D=dups allowed, M=modifiable): BOX
Fields (NAME type description [values]):
  BOX Integer Box Number [1=G1 - Total Sales,2=G2 - Export Sales,3=G3 - Other GST-Free Sales,4=G4 - Input Taxed Sales,5=G7 - Sales Adjustments,6=G10 - Capital Purchases,7=G11 - Non-Capital Purchases,8=G13 - Purchases for Making Input Taxes Sales,9=G14 - GST-Free Purchases,10=G15 - Estimated Purchases for Private Use,11=G18 - Purchase Adjustments,16=W1 - Total salary, wages and other payments,17=W2 - Amount withheld from payments shown at W1,18=W4 - Amount withheld where no ABN is quoted,19=W3 - Other amounts withheld (excluding any amounts shown at W2 or W4),20=5B - Credit from PAYG Income Tax Instalment Variation,21=7 - Deferred Company/Fund Instalment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NUMDETAIL Integer Number Of Details

## TWGBAS - Generate BAS Worksheet (view TW0400)
Keys (first = PK; D=dups allowed, M=modifiable): FROMYEAR+FROMPERIOD+TOYEAR+TOPERIOD
Fields (NAME type description [values]):
  FROMYEAR String*4 From Fiscal Year
  FROMPERIOD Integer From Fiscal Period
  TOYEAR String*4 To Fiscal Year
  TOPERIOD Integer To Fiscal Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CALG1 BCD*10.3 Calculated G1
  PMG1 BCD*10.3 Plus OR Minus G1
  CALG2 BCD*10.3 Calculated G2
  PMG2 BCD*10.3 Plus OR Minus G2
  CALG3 BCD*10.3 Calculated G3
  PMG3 BCD*10.3 Plus OR Minus G3
  CALG4 BCD*10.3 Calculated G4
  PMG4 BCD*10.3 Plus OR Minus G4
  CALG7 BCD*10.3 Calculated G7
  PMG7 BCD*10.3 Plus OR Minus G7
  CALG10 BCD*10.3 Calculated G10
  PMG10 BCD*10.3 Plus OR Minus G10
  CALG11 BCD*10.3 Calculated G11
  PMG11 BCD*10.3 Plus OR Minus G11
  CALG13 BCD*10.3 Calculated G13
  PMG13 BCD*10.3 Plus OR Minus G13
  CALG14 BCD*10.3 Calculated G14
  PMG14 BCD*10.3 Plus OR Minus G14
  CALG15 BCD*10.3 Calculated G15
  PMG15 BCD*10.3 Plus OR Minus G15
  CALG18 BCD*10.3 Calculated G18
  PMG18 BCD*10.3 Plus OR Minus G18
  CALW1 BCD*10.3 Calculated W1
  PMW1 BCD*10.3 Plus OR Minus W1
  CALW2 BCD*10.3 Calculated W2
  PMW2 BCD*10.3 Plus OR Minus W2
  CALW4 BCD*10.3 Calculated W4
  PMW4 BCD*10.3 Plus OR Minus W4
  CALW3 BCD*10.3 Calculated W3
  PMW3 BCD*10.3 Plus OR Minus W3
  CAL5B BCD*10.3 Calculated 5B
  PM5B BCD*10.3 Plus OR Minus 5B
  CAL7 BCD*10.3 Calculated 7
  PM7 BCD*10.3 Plus OR Minus 7
  TOTT7 BCD*10.3 Total T7
  TOTT8 BCD*10.3 Total T8
  TOTT9 BCD*10.3 Total T9
  REASONT4 String*2 T4 Reason code for variation
  JSONFILE String*255 JSON Audit File Name

## TWTBOXD - BAS Worksheet Detail Amounts (view TW0580)
Keys (first = PK; D=dups allowed, M=modifiable): FROMYEAR+FROMPERIOD+TOYEAR+TOPERIOD+BOX+DETAILNUM
Fields (NAME type description [values]):
  FROMYEAR String*4 From Fiscal Year
  FROMPERIOD Integer From Fiscal Period
  TOYEAR String*4 To Fiscal Year
  TOPERIOD Integer To Fiscal Period
  BOX Integer Box Number [1=G1 - Total Sales,2=G2 - Export Sales,3=G3 - Other GST-Free Sales,4=G4 - Input Taxed Sales,5=G7 - Sales Adjustments,6=G10 - Capital Purchases,7=G11 - Non-Capital Purchases,8=G13 - Purchases for Making Input Taxes Sales,9=G14 - GST-Free Purchases,10=G15 - Estimated Purchases for Private Use,11=G18 - Purchase Adjustments,16=W1 - Total salary, wages and other payments,17=W2 - Amount withheld from payments shown at W1,18=W4 - Amount withheld where no ABN is quoted,19=W3 - Other amounts withheld (excluding any amounts shown at W2 or W4),20=5B - Credit from PAYG Income Tax Instalment Variation,21=7 - Deferred Company/Fund Instalment]
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
