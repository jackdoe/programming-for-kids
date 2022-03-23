    LD    R0,loc2
    ADD
    ST    R0,loc2
    LD    R0,loc2+1
    DEC   R0
    BZ    loc1+1
    ST    R0,loc2+1
 loc1:
    B     0
 loc2:
    HLT
 count:
    .data 8
