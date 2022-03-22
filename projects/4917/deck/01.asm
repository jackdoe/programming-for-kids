;; This is an example program

ld r0,15    ;; Some comment
ld r1,14
add
print 15
st_r0 9    ;; Alternative register syntax
hlt

.data
14: 4
15: 3