# AS module - compiled AOM dictionary

## ASACTLOG - Activation Log (view AS0034)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE
Fields (NAME type description [values]):
  SEQUENCE Long Log Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATE Date Date
  TIME Time Time
  PREFIX String*2 Application Prefix
  VERSION String*3 Application Version
  STAGE Long Stage
  MESSAGE String*255 Message

## ASAUDT - User Audit (view AS0088)
Keys (first = PK; D=dups allowed, M=modifiable): SEQNUM
Fields (NAME type description [values]):
  SEQNUM ???
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USERID String*8
  ORGID String*6
  DATE Date
  TIME Time
  ACTION Integer
  PLATFORM Integer
  SCREENID String*36
  ADDR String*60

## ASCUSTD - UI Customization Details (view AS0052)
Keys (first = PK; D=dups allowed, M=modifiable): SCREENID+CUSTID+PARTNUM
Fields (NAME type description [values]):
  SCREENID String*36 Screen ID
  CUSTID String*20 Customization ID
  PARTNUM Long Part Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BLOBDAT Binary*3800 Blob Data

## ASCUSTH - UI Customization Headers (view AS0051)
Keys (first = PK; D=dups allowed, M=modifiable): SCREENID+CUSTID
Fields (NAME type description [values]):
  SCREENID String*36 Screen ID
  CUSTID String*20 Customization ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESCRIPT String*255 Description
  DATASIZE Long Data Size
  NUMOFPARTS Long Number of Parts

## ASRPTH - Custom Reports (view AS0040)
Keys (first = PK; D=dups allowed, M=modifiable): REPORTID
Fields (NAME type description [values]):
  REPORTID String*36 Report GUID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REPORTNAME String*255 Report Filename
  REPORTITLE String*255 Report Title

## ASWPCR - Working Profile Custom Reports (view AS0050)
Keys (first = PK; D=dups allowed, M=modifiable): PROFILEID+COMPANYID+REPORTID
Fields (NAME type description [values]):
  PROFILEID String*20 Profile ID
  COMPANYID String*6 Company ID
  REPORTID String*36 Report GUID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## ASWPCST - Working Profile UI Customization (view AS0053)
Keys (first = PK; D=dups allowed, M=modifiable): PROFILEID+COMPANYID+SCREENID+CUSTID; COMPANYID+SCREENID+CUSTID+PROFILEID
Fields (NAME type description [values]):
  PROFILEID String*20 Profile ID
  COMPANYID String*6 Company ID
  SCREENID String*36 Screen ID
  CUSTID String*20 Customization ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
