# -*- coding: utf-8 -*-

import faultsim as sim

class FullAdder(sim.Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.C = self.Node("C")
        self.S = self.Node("S")
        self.Cout = self.Node("Cout")
        self.XOR1 = self.XOR("XOR1")
        self.XOR2 = self.XOR("XOR2")
        self.AND1 = self.AND("AND1")
        self.AND2 = self.AND("AND2")
        self.OR1 = self.OR("OR1")
        self.A.connect(self.XOR1.A, self.AND1.A)
        self.B.connect(self.XOR1.B, self.AND1.B)
        self.C.connect(self.XOR2.A, self.AND2.A)
        self.XOR1.Q.connect(self.XOR2.B, self.AND2.B)
        self.AND1.Q.connect(self.OR1.A)
        self.AND2.Q.connect(self.OR1.B)
        self.XOR2.Q.connect(self.S)
        self.OR1.Q.connect(self.Cout)

A1 = sim.Node("A1")
A2 = sim.Node("A2")
A3 = sim.Node("A3")
A4 = sim.Node("A4")

B1 = sim.Node("B1")
B2 = sim.Node("B2")
B3 = sim.Node("B3")
B4 = sim.Node("B4")

S1 = sim.Node("S1")
S2 = sim.Node("S2")
S3 = sim.Node("S3")
S4 = sim.Node("S4")

C = sim.Node("C")

Cout = sim.Node("Cout")

XOR1 = sim.XOR("XOR1")
XOR2 = sim.XOR("XOR2")
XOR3 = sim.XOR("XOR3")
XOR4 = sim.XOR("XOR4")

ADD1 = FullAdder("ADD1")
ADD2 = FullAdder("ADD2")
ADD3 = FullAdder("ADD3")
ADD4 = FullAdder("ADD4")

PI_A = sim.NodeList(A4, A3, A2, A1)
PI_B = sim.NodeList(B4, B3, B2, B1)
PO_S = sim.NodeList(S4, S3, S2, S1)

A1.connect(ADD1.A)
A2.connect(ADD2.A)
A3.connect(ADD3.A)
A4.connect(ADD4.A)

B1.connect(XOR1.A)
B2.connect(XOR2.A)
B3.connect(XOR3.A)
B4.connect(XOR4.A)

C.connect(ADD1.C, XOR1.B, XOR2.B, XOR3.B, XOR4.B)

XOR1.Q.connect(ADD1.B)
XOR2.Q.connect(ADD2.B)
XOR3.Q.connect(ADD3.B)
XOR4.Q.connect(ADD4.B)

ADD1.Cout.connect(ADD2.C)
ADD2.Cout.connect(ADD3.C)
ADD3.Cout.connect(ADD4.C)
ADD4.Cout.connect(Cout)

ADD1.S.connect(S1)
ADD2.S.connect(S2)
ADD3.S.connect(S3)
ADD4.S.connect(S4)

C.setvalue(1)
C.propagate()

PI_A.setbitstr('1001')
PI_B.setbitstr('0010')

PI_A.propagate()
PI_B.propagate()

ans = PO_S.getbitstr()

print(ans)
