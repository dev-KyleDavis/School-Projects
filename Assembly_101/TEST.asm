MSG 30 "ENTER YOUR FIRST NUMBER "
PMT 30
INP 25
LDA 25
MSG 31 "ENTER YOUR SECOND NUMBER "
PMT 31
INP 26
LDC 26
PNT 25
STRA 27
LDB 27
INC B
STRB 27
PNT 27
CMP B C
JLT 11
STP