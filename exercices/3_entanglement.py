from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

print(circuit.draw())

circuit.measure_all()
simulator = AerSimulator()

job = simulator.run(circuit, shots=500)
result = job.result()

plt = plot_histogram(result.get_counts(), filename="../tmp/ex3_histogram.png")