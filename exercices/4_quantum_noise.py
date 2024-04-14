from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

ibmq_token = open("ibmq_token", "r").read().strip()
service = QiskitRuntimeService(channel="ibm_quantum", token=ibmq_token)
computer = service.least_busy(simulator=False, operational=True)

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
pub_result = job.result()

print(pub_result)