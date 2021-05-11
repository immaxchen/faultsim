# faultsim
Basic combinational logic circuit fault simulation

Python 3.6+ required

# Example

download the module and import

```python
import faultsim as sim
```

build the stuck-at faults example circuit in [section 1.3.2.1 of the textbook [1]](https://books.google.com.tw/books?id=P1ea4znZhGsC&lpg=PP1&hl=zh-TW&pg=PA12#v=onepage&q&f=false)

```python
X1 = sim.Node("X1")
X2 = sim.Node("X2")
X3 = sim.Node("X3")

NOT1 = sim.NOT("NOT1")
AND1 = sim.AND("AND1")
AND2 = sim.AND("AND2")
OR1 = sim.OR("OR1")

X1.connect(AND1.A)
X2.connect(AND1.B, NOT1.A)
X3.connect(AND2.B)
NOT1.Q.connect(AND2.A)
AND1.Q.connect(OR1.A)
AND2.Q.connect(OR1.B)

PI = sim.NodeList(X1, X2, X3)
PO = sim.NodeList(OR1.Q)
```

run simulation without fault

```python
PI.setbitstr('000')
PI.propagate()
ans = PO.getbitstr()
```

assign fault and re-run simulation

```python
X3.stuckat = 1
PI.setbitstr('000')
PI.propagate()
ans = PO.getbitstr()
```

# Reference:

[1] Wang et al. (2006). VLSI Test Principles and Architectures: Design for Testability. Elsevier Publish.
