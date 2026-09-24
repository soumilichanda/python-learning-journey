import numpy as np


class ComputationalNode:
    """Scalar node tracking the mathematical forward pass and local derivatives."""

    def __init__(self, val: float, children: tuple = (), op: str = ""):
        self.val = float(val)
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(children)
        self._op = op

    def __add__(self, other: "ComputationalNode | float") -> "ComputationalNode":
        other = other if isinstance(other, ComputationalNode) else ComputationalNode(other)
        out = ComputationalNode(self.val + other.val, (self, other), "+")

        def _backward():
            # d(out)/d(self) = 1.0, d(out)/d(other) = 1.0
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

        out._backward = _backward
        return out

    def __mul__(self, other: "ComputationalNode | float") -> "ComputationalNode":
        other = other if isinstance(other, ComputationalNode) else ComputationalNode(other)
        out = ComputationalNode(self.val * other.val, (self, other), "*")

        def _backward():
            # d(out)/d(self) = other.val, d(out)/d(other) = self.val
            self.grad += other.val * out.grad
            other.grad += self.val * out.grad

        out._backward = _backward
        return out

    def backward(self) -> None:
        # Build topological sort of graph
        topo: list[ComputationalNode] = []
        visited: set[ComputationalNode] = set()

        def build_topo(v: ComputationalNode):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)

        build_topo(self)

        # Seed the output gradient
        self.grad = 1.0
        # Propagate gradients backwards in reverse topological order
        for node in reversed(topo):
            node._backward()

    def __repr__(self) -> str:
        return f"Node(val={self.val:.4f}, grad={self.grad:.4f})"


if __name__ == "__main__":
    # Simulating a linear neuron: output = (x * w) + b
    x = ComputationalNode(2.0)
    w = ComputationalNode(3.0)
    b = ComputationalNode(1.5)

    # Forward Pass
    xw = x * w
    out = xw + b

    # Backward Pass (Backpropagation)
    out.backward()

    print("=== Computational Graph Forward & Backward Pass ===")
    print(f"Forward Output: {out.val}")
    print(f"d(out)/dw [Weight Gradient]: {w.grad} (Expected: x.val = 2.0)")
    print(f"d(out)/dx [Input Gradient] : {x.grad} (Expected: w.val = 3.0)")
    print(f"d(out)/db [Bias Gradient]  : {b.grad} (Expected: 1.0)")