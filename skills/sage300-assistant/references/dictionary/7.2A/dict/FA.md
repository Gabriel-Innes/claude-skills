# FA module - compiled AOM dictionary

## FAASSET - Sage Fixed Assets Integration Assets (view FA0100)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE; STATUS+SEQUENCE [D,M]
Fields (NAME type description [values]):
  SEQUENCE Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATUS Integer Status [0=Pending,1=Created,99=Error]
  ERRORS Long Errors
  ORGID String*6 Database ID
  DRILLAPP String*2 Drilldown Application Source
  DRILLTYPE Integer Drilldown Type
  DRILLDWNLK BCD*10.0 Drilldown Link Number
  FASDB String*32 Sage Fixed Assets Database
  FASCMP String*32 Sage Fixed Assets Company/Org.
  FASTMPL String*25 Sage Fixed Assets Template
  ASSETDESC String*80 Asset Description
  DATE Date Acquisition Date
  QTY BCD*10.5 Quantity
  UOM String*10 Unit of Measure
  VENDOR String*12 Vendor Number
  DOCUMENTNO String*22 Document Number
  PONUMBER String*22 Purchase Order Number
  CURRENCY String*3 Currency Code
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATE BCD*8.7 Exchange Rate
  VALUETC BCD*10.3 Source Currency Asset Value
  VALUEHC BCD*10.3 Functional Currency Asset Value
  ASSETID Long Sys No
  CREATEDATE Date Date Asset Created

## FACMP - Sage Fixed Assets Companies/Orgs. (view FA0200)
Keys (first = PK; D=dups allowed, M=modifiable): FASDB+FASCMP
Fields (NAME type description [values]):
  FASDB String*32 Sage Fixed Assets Database
  FASCMP String*32 Sage Fixed Assets Company/Org.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ID Integer Sage Fixed Assets Company/Org. ID
  LOCKED Integer Locked [0=No,1=Yes]
  TEMPLATES Long Number of Templates

## FADB - Sage Fixed Assets Integration Databases (view FA0300)
Keys (first = PK; D=dups allowed, M=modifiable): FASDB
Fields (NAME type description [values]):
  FASDB String*32 Sage Fixed Assets Database
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LOCKED Integer Locked [0=No,1=Yes]
  COMPANIES Long Number of Companies

## FAERROR - Sage Fixed Assets Integration Errors (view FA0310)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE+REVISION
Fields (NAME type description [values]):
  SEQUENCE Long Sequence
  REVISION Long Revision
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ERROR String*255 Error

## FAOPT - Sage Fixed Assets Integration Options (view FA0500)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTACT String*60 Contact
  PHONE String*30 Phone
  FAX String*30 Fax
  NEXTSEQ Long Next Asset Sequence Number
  FAS Integer Sage Fixed Assets Product [0=None]
  FASPROD String*255 Sage Fixed Assets Product
  FASDB String*32 Sage Fixed Assets Database
  FASCMP String*32 Sage Fixed Assets Company/Org.
  FASTMPL String*25 Sage Fixed Assets Template
  APPLY Integer Create Assets By [1=Applying Template,3=Applying Template then Forcing Book Defaults]
  SCHEDKEYS String*12 Synch. Sage Fixed Assets Data Schedule
  SCHEDLINKS BCD*10.0 Synch. Sage Fixed Assets Data Schedule Link
  LASTRUNS Date Date Last Synchronized
  SCHEDKEYC String*12 Create Assets Schedule
  SCHEDLINKC BCD*10.0 Create Assets Schedule Link
  LASTRUNC Date Date Create Assets Last Run
  SCHEDKEYP String*12 Clear Assets Schedule
  SCHEDLINKP BCD*10.0 Clear Assets Schedule Link
  LASTRUNP Date Date Clear Assets Last Run

## FARSTRT - Sage Fixed Assets Integration Restart (view FA0600)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*127 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1
  DATA2 Binary*255 Data Block 2
  DATA3 Binary*255 Data Block 3
  DATA4 Binary*255 Data Block 4
  DATA5 Binary*255 Data Block 5
  DATA6 Binary*255 Data Block 6
  DATA7 Binary*255 Data Block 7
  DATA8 Binary*255 Data Block 8

## FATMPL - Sage Fixed Assets Integration Templates (view FA0800)
Keys (first = PK; D=dups allowed, M=modifiable): FASDB+FASCMP+FASTMPL
Fields (NAME type description [values]):
  FASDB String*32 Sage Fixed Assets Database
  FASCMP String*32 Sage Fixed Assets Company/Org.
  FASTMPL String*25 Sage Fixed Assets Template
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ID Long Sage Fixed Assets Template ID
