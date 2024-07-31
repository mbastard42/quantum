from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.visualization import plot_histogram

ibmq_token = open("ibmq_token", "r").read().strip()
service = QiskitRuntimeService(channel="ibm_quantum", token=ibmq_token)
computer = service.backend("ibmq_qasm_simulator")

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

backend = service.least_busy(operational=True, simulator=True)
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(circuit)

sampler = Sampler(backend=backend)
sampler.options.default_shots = 500
job = sampler.run([isa_circuit])
result = job.result()

plt = plot_histogram(result.get_counts(circuit), filename="../tmp/ex4_histogram.png")
