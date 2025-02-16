START 200
X     DS     1
Y     DS     1
Z     DS     1
A     DC     5       
B     DC     10     
MOVER AREG, ='7'
ADD   BREG, X
MOVEM CREG, Y
SUB   AREG, ='3'
MULT  BREG, ='15'
LTORG
DIV   CREG, ='6'
MOVEM BREG, Z
LTORG
END