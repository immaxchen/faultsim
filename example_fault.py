# -*- coding: utf-8 -*-

import faultsim as sim

X1 = sim.Node("X1")
X2 = sim.Node("X2")
X3 = sim.Node("X3")

NOT1 = sim.NOT("NOT1")
AND1 = sim.AND("AND1")
AND2 = sim.AND("AND2")
OR1 = sim.OR("OR1")

PI = sim.NodeList(X1, X2, X3)
PO = sim.NodeList(OR1.Q)

X1.connect(AND1.A)
X2.connect(AND1.B, NOT1.A)
X3.connect(AND2.B)
NOT1.Q.connect(AND2.A)
AND1.Q.connect(OR1.A)
AND2.Q.connect(OR1.B)

sites = {
    "a": X1,
    "b": X2,
    "c": X3,
    "d": AND1.B,
    "e": NOT1.A,
    "f": NOT1.Q,
    "g": AND1.Q,
    "h": AND2.Q,
    "i": OR1.Q
}

for name, site in sites.items():
    for val in [0, 1]:
        site.stuckat = val
        s = []
        for bits in ['000','001','010','011','100','101','110','111']:
            PI.setbitstr(bits)
            PI.propagate()
            res = PO.getbitstr()
            s.append(res)
        site.stuckat = None
        print(' '.join([name, f"sa{val}", *s]))
