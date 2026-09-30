# AS module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

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
