<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCRN - Currency Codes
Module: Administration | 28 columns | ObjType: 37
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CurrCode
  CUR_NAME: CurrName
Fields (name type(len) description [values] ->parent table):
  CurrCode nVarChar(3) Currency Code
  CurrName nVarChar(20) Currency
  ChkName nVarChar(20) Name on Printed Checks
  Chk100Name nVarChar(20) Name of 100's on checks
  DocCurrCod nVarChar(3) Name on Printed Docs.
  FrgnName nVarChar(20) English
  F100Name nVarChar(20) English Hundredth Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  RoundSys Int(6) Rounding default=0 [0=No Rounding, 4=Round to Five Hundredth, 1=Round to Ten Hundredth, 2=Round to One, 3=Round to Ten]
  UserSign2 Int(6) Updating User ->OUSR
  Decimals Int(6) Decimals default=-1 [-1=Default, 0=Without Decimals, 1=1 Digit, 2=2 Digits, 3=3 Digits, 4=4 Digits, 5=5 Digits, 6=6 Digits]
  ISRCalc VarChar(1) ISR Calculation default=N [Y=Yes, N=No]
  RoundPym VarChar(1) Rounding in Pmnt default=N [Y=Yes, N=No]
  ConvUnit VarChar(1) Is a Conventional Unit default=N [Y=Yes, N=No]
  BaseCurr nVarChar(3) Base Currency for Conv. Unit ->OCRN
  Factor Num(19,6) Factor
  ChkNamePl nVarChar(20) Plural for Int.Description
  Chk100NPl nVarChar(20) Plural for Hundredth Name
  FrgnNamePl nVarChar(20) Plural for English
  F100NamePl nVarChar(20) Plural for Eng. Hundredth Name
  ISOCurrCod nVarChar(3) ISO Currency Code [AED=United Arab Emirates, Dirhams, AFN=Afghanistan, Afghanis, ALL=Albania, Leke, AMD=Armenia, Drams, ANG=Netherlands Antilles, Guilders (also called Florins), AOA=Angola, Kwanzas, ARS=Argentina, Pesos, AUD=Australia, Dollars, AWG=Aruba, Guilders (also called Florins), AZM=Azerbaijan, Manats [obsolete], AZN=Azerbaijan, New Manats, BAM=Bosnia and Herzegovina, Convertible Marks, BBD=Barbados, Dollars, BDT=Bangladesh, Taka, BGN=Bulgaria, Leva, BHD=Bahrain, Dinars, BIF=Burundi, Francs, BMD=Bermuda, Dollars, BND=Brunei, Ringgits, BOB=Bolivia, Bolivianos, BRL=Brazil, Brazilian Reals, BSD=Bahamas, Dollars, BTN=Bhutan, Ngultrum, BWP=Botswana, Pulas, BYN=Belarus, Rubles, BYR=Belarus, Rubles, BZD=Belize, Dollars, CAD=Canada, Dollars, CDF=Congo/Kinshasa, Congolese Francs, CHF=Switzerland, Francs, CLP=Chile, Pesos, CNY=China, Yuan Renminbi, COP=Colombia, Pesos, CRC=Costa Rica, Colones, CUP=Cuba, Pesos, CVE=Cape Verde, Escudos, CYP=Cyprus, Pounds, CZK=Czech Republic, Koruny, DJF=Djibouti, Francs, DKK=Denmark, Kroner, DOP=Dominican Republic, Pesos, DZD=Algeria, Algerian Dinars, EEK=Estonia, Krooni, EGP=Egypt, Pounds, ERN=Eritrea, Nakfa, ETB=Ethiopia, Birr, EUR=EU Member Countries, Euro, FJD=Fiji, Dollars, FKP=Falkland Islands (Malvinas), Pounds, GBP=United Kingdom, Pounds, GEL=Georgia, Lari, GGP=Guernsey, Pounds, GHC=Ghana, Cedis, GHS=Ghana, Cedis, GIP=Gibraltar, Pounds, GMD=Gambia, Dalasi, GNF=Guinea, Francs, GTQ=Guatemala, Quetzales, GYD=Guyana, Dollars, HKD=Hong Kong, Dollars, HNL=Honduras, Lempiras, HRK=Croatia, Kuna, HTG=Haiti, Gourdes, HUF=Hungary, Forint, IDR=Indonesia, Rupiahs, ILS=Israel, New Shekels, IMP=Isle of Man, Pounds, INR=India, Rupees, IQD=Iraq, Dinars, IRR=Iran, Rials, ISK=Iceland, Kronur, JEP=Jersey, Pounds, JMD=Jamaica, Dollars, JOD=Jordan, Dinars, JPY=Japan, Yen, KES=Kenya, Shillings, KGS=Kyrgyzstan, Soms, KHR=Cambodia, Riels, KMF=Comoros, Francs, KPW=Korea (North), Won, KRW=Korea (South), Won, KWD=Kuwait, Dinars, KYD=Cayman Islands, Dollars, KZT=Kazakhstan, Tenge, LAK=Laos, Kips, LBP=Lebanon, Pounds, LKR=Sri Lanka, Rupees, LRD=Liberia, Dollars, LSL=Lesotho, Maloti, LTL=Lithuania, Litai, LVL=Latvia, Lati, LYD=Libya, Dinars, MAD=Morocco, Dirhams, MDL=Moldova, Lei, MGA=Madagascar, Ariary, MKD=Macedonia, Denars, MMK=Myanmar (Burma), Kyats, MNT=Mongolia, Tugriks, MOP=Macau, Patacas, MRO=Mauritania, Ouguiyas, MTL=Malta, Liri, MUR=Mauritius, Rupees, MVR=Maldives (Maldive Islands), Rufiyaa, MWK=Malawi, Kwachas, MXN=Mexico, Pesos, MYR=Malaysia, Ringgits, MZM=Mozambique, Meticais [obsolete], MZN=Mozambique, Meticais [newer unit, same name], NAD=Namibia, Dollars, NGN=Nigeria, Nairas, NIO=Nicaragua, Cordobas, NOK=Norway, Krone, NPR=Nepal, Nepal Rupees, NZD=New Zealand, Dollars, OMR=Oman, Rials, PAB=Panama, Balboa, PEN=Peru, Nuevos Soles, PGK=Papua New Guinea, Kina, PHP=Philippines, Pesos, PKR=Pakistan, Rupees, PLN=Poland, Zlotych, PYG=Paraguay, Guarani, QAR=Qatar, Rials, ROL=Romania, Lei [obsolete], RON=Romania, New Lei, RSD=Serbia, Dinars, RUB=Russia, Rubles, RWF=Rwanda, Rwandan Francs, SAR=Saudi Arabia, Riyals, SBD=Solomon Islands, Dollars, SCR=Seychelles, Rupees, SDD=Sudan, Dinars [obsolete], SDG=Sudan, Pounds, SEK=Sweden, Kronor, SGD=Singapore, Dollars, SHP=Saint Helena, Pounds, SIT=Slovenia, Tolars [obsolete], SKK=Slovakia, Koruny, SLL=Sierra Leone, Leones, SOS=Somalia, Shillings, SPL=Seborga, Luigini, SRD=Suriname, Dollars, STD=Sao Tome and Principe, Dobras, SVC=El Salvador, Colones, SYP=Syria, Pounds, SZL=Swaziland, Emalangeni, THB=Thailand, Baht, TJS=Tajikistan, Somoni, TMT=Turkmenistan, Manats, TND=Tunisia, Dinars, TOP=Tonga, Pa'anga, TRY=Turkey, New Lira, TTD=Trinidad and Tobago, Dollars, TVD=Tuvalu, Tuvalu Dollars, TWD=Taiwan, New Dollars, TZS=Tanzania, Shillings, UAH=Ukraine, Hryvnia, UGX=Uganda, Shillings, USD=United States of America, Dollars, UYU=Uruguay, Pesos, UZS=Uzbekistan, Sums, VEB=Venezuela, Bolivares, VND=Viet Nam, Dong, VUV=Vanuatu, Vatu, WST=Samoa, Tala, XAF=Communaute Financiere Africaine BEAC, Francs, XAG=Silver, Ounces, XAU=Gold, Ounces, XCD=East Caribbean Dollars, XDR=International Monetary Fund (IMF) Special Drawing Rights, XOF=Communaute Financiere Africaine BCEAO, Francs, XPD=Palladium Ounces, XPF=Comptoirs Francais du Pacifique Francs, XPT=Platinum, Ounces, YER=Yemen, Rials, ZAR=South Africa, Rand, ZMK=Zambia, Kwacha, ZWD=Zimbabwe, Zimbabwe Dollars]
  MaxInDiff Num(19,6) Incoming Amt Diff. Allowed
  MaxOutDiff Num(19,6) Outgoing Amt Diff. Allowed
  MaxInPcnt Num(19,6) Incoming % Diff. Allowed
  MaxOutPcnt Num(19,6) Outgoing % Diff. Allowed
  ISOCurrNum nVarChar(3) ISO Currency Number
