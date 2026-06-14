from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create circuit: 2 qubits, 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 1: Put qubit 0 into superposition
qc.h(0)

# Step 2: Entangle qubit 1 with qubit 0
qc.cx(0, 1)

# Step 3: Measure both qubits into classical bits
qc.measure([0, 1], [0, 1])

# Run on local simulator, 1024 shots
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print("Measurement results:", counts)
print("\nCircuit diagram:")
print(qc.draw(output='text'))