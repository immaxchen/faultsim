# -*- coding: utf-8 -*-

class Node:
    def __init__(self, name=None, parent=None):
        self.name = name if parent is None else f"{parent.name}/{name}"
        self.parent = parent
        self.value = None
        self.stuckat = None
        self.outputs = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    def setvalue(self, value):
        self.value = False if value == '0' else bool(value)

    def getvalue(self):
        return bool(self.value) if self.stuckat is None else bool(self.stuckat)

    def connect(self, *args):
        self.outputs = args

    def drive(self):
        for node in self.outputs:
            node.value = self.getvalue()

    def propagate(self):
        self.drive()
        for node in self.outputs:
            node.propagate()

    def trace(self):
        yield self
        for node in self.outputs:
            for next in node.trace():
                yield next

class NodeList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)

    def setbitstr(self, bitstr):
        for node, bit in zip(self, bitstr):
            node.setvalue(bit)

    def getbitstr(self):
        return str().join('1' if node.getvalue() else '0' for node in self)

    def propagate(self):
        for node in self:
            node.propagate()

    def trace(self):
        for node in self:
            for next in node.trace():
                yield next

class Block:
    def __init__(self, name=None, parent=None):
        self.name = name if parent is None else f"{parent.name}/{name}"
        self.parent = parent
        self.define()

    def define(self):
        pass

    def Node(self, *args, **kwargs):
        return Node(*args, **kwargs, parent=self)

    def register(block):
        def block_factory(self, *args, **kwargs):
            return block(*args, **kwargs, parent=self)
        setattr(Block, block.__name__, block_factory)

class AND(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = self.A.getvalue() and self.B.getvalue()
        self.A.drive = _drive
        self.B.drive = _drive

class OR(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = self.A.getvalue() or self.B.getvalue()
        self.A.drive = _drive
        self.B.drive = _drive

class NOT(Block):
    def define(self):
        self.A = self.Node("A")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        def _drive():
            self.Q.value = not self.A.getvalue()
        self.A.drive = _drive

class NAND(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = not (self.A.getvalue() and self.B.getvalue())
        self.A.drive = _drive
        self.B.drive = _drive

class NOR(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = not (self.A.getvalue() or self.B.getvalue())
        self.A.drive = _drive
        self.B.drive = _drive

class XOR(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = self.A.getvalue() != self.B.getvalue()
        self.A.drive = _drive
        self.B.drive = _drive

class XNOR(Block):
    def define(self):
        self.A = self.Node("A")
        self.B = self.Node("B")
        self.Q = self.Node("Q")
        self.A.connect(self.Q)
        self.B.connect(self.Q)
        def _drive():
            self.Q.value = not (self.A.getvalue() != self.B.getvalue())
        self.A.drive = _drive
        self.B.drive = _drive

Block.register(AND)
Block.register(OR)
Block.register(NOT)
Block.register(NAND)
Block.register(NOR)
Block.register(XOR)
Block.register(XNOR)
