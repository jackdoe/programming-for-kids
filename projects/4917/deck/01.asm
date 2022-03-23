;; 01.asm

LD R0,data+1    ;; Some comment
LD R1,data
ADD
PRINT data+1
ST R0,9   
HLT
HLT
HLT
HLT
HLT

data: 
  .data 4
  .data 3