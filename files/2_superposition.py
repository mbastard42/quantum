from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(1)
circuit.h(0)

print(circuit.draw())

circuit.measure_all()
simulator = AerSimulator()

job = simulator.run(circuit, shots=500)
result = job.result()

plt = plot_histogram(result.get_counts(), filename="tmp/ex2_histogram.png")
