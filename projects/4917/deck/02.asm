    LD    R0,data
    LD    R1,data+1
    SUB
    BZ    loc1
    PRINT 1
    B     loc2
loc1:
    PRINT 0
loc2:
    HLT
data:
    .data 9
    .data 9