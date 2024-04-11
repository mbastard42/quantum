from qiskit_ibm_runtime import QiskitRuntimeService

ibmq_token = open("ibmq_token", "r").read().strip()
service = QiskitRuntimeService(channel="ibm_quantum", token=ibmq_token)

unavailables = service.backends(operational=False)

print("\nUnavailable simulators and computers:\n")
if len(unavailables) == 0 :
    print("none")
else :
    for unavailable in unavailables:
        print(unavailable.configuration().n_qubits, "qubits\t[", unavailable.name, "]")

simulators = service.backends(simulator=True, operational=True)

print("\nAvailable simulators:\n")
if len(simulators) == 0 :
    print("none")
else :
    for simulator in simulators :
        status = simulator.status()
        print(simulator.configuration().n_qubits, "qubits\t", simulator.name, "[", status.pending_jobs, "jobs in queue ]")


computers = service.backends(simulator=False, operational=True)

print("\nAvailable computers:\n")
if len(computers) == 0 :
    print("none")
else :
    for computer in computers :
        status = computer.status()
        print(computer.configuration().n_qubits, "qubits\t", computer.name, "[", status.pending_jobs, "jobs in queue ]")


print()
