
## HyperFlux
🌐 [日本語README](./docs/README_ja.md) | 🇬🇧 [English README](./docs/README_en.md) | 🇫🇷 [Français README](./docs/README_fr.md) | 🇨🇳 [中文 README](./docs/README_zh.md)

### 🌟 Project Objectives
HyperFlux aims to achieve the following goals:
- ⚡ **Ultra-fast Transaction Processing**: Proprietary BFT + DAG algorithms process up to 10,000 transactions per second.
- 🛡️ **High Security**: Verification while protecting transaction privacy using zk-SNARKs technology.
- 🤖 **BFT (Byzantine Fault Tolerance)**: BFT algorithm implemented to improve fault tolerance in distributed systems.
- 🧩 **zk-SNARKs Verification**: Added zk-SNARKs technology to protect transaction privacy while verifying transactions.
- 🔄 **Parallel Transaction Processing with DAG**: Implemented DAG to enable parallel processing of transactions and increase throughput.

### 📁 File List and Description
- **\`docs/\`**: Directory containing project documentation, including:
  - \`README.md\`: Project overview, purpose, setup instructions, usage guidelines, and runtime screen details.
  - \`CONTRIBUTING.md\`: Project contribution guide.
  - \`wiki/\`: Additional documentation about the project.
- **\`src/\`**: Directory containing source code, including:
  - \`bft_network.py\`: Script for managing the BFT network.
  - \`bft_node.py\`: Script for BFT node operations.
  - \`blockchain.py\`: Script for blockchain management.
  - \`dag.py\`: Script for DAG operations.
  - \`dag_node.py\`: Script for DAG node operations.
  - \`dashboard.py\`: Script for the dashboard interface.
  - \`transaction.py\`: Script for transaction processing.
  - \`test_hyperflux.py\`: Script for testing the functionalities of \`hyperflux.py\`.
- **\`hyperflux.py\`**: Main script for starting the HyperFlux project.
- **\`requirements.txt\`**: List of project dependencies.

### 🛠️ Setup Instructions
Follow these steps to set up HyperFlux:
1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yukihamada/HyperFlux.git
   cd HyperFlux
   \`\`\`
2. **Install the required dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### 🚀 How to Use
To start the HyperFlux project, run the following command:
\`\`\`bash
python hyperflux.py
\`\`\`

### 📖 Screen at Runtime Details
When you run \`python hyperflux.py\`, you will encounter a dashboard that allows you to monitor and interact with the HyperFlux system. Below are the detailed views and functionalities that you can access.

## Initial Screen
When you start the project, you will see the following:
\`\`\`plaintext
==================================================
HyperFlux Status: Initializing...
[###----] Loading configuration...
[#####---] Connecting to network...
[########] Node started successfully...
==================================================
HyperFlux WEB interface: http://localhost:8080
==================================================
Dashboard:
1. 🚀 Check node status
2. 💸 Submit transaction
3. 🌐 Check network status
4. 📜 Smart contract management
5. 🗳️ Governance
6. 🌉 Cross-chain functionality
7. ⚙️ Configuration
==================================================
Select functionality (1-7):
\`\`\`
For a detailed explanation of what you will see when you run the project, please refer to the [Screen at Runtime Guide](./docs/Screen_at_Runtime.md).

### 🔧 Key Features
- **Smart Contract Support**: EVM compatibility for development in Solidity. Seamless integration with the existing Ethereum ecosystem.
- **P2P Communication**: Real-time peer-to-peer communication using WebRTC. Fast and secure data transfer between nodes, optimizing distributed applications' performance.
- **Scalability**: Advanced scalability features with sharding and DAG, ensuring consistent high performance even as the network grows.

### 💻 Usage Scenarios
Here is an example for manipulating each HyperFlux function using command line arguments.

#### Checking the status of a node
\`\`\`bash
python hyperflux.py status
\`\`\`

Output:
\`\`\`plaintext
==================================================
Node status:
- State: Active
- Number of connected peers: 12
- Block Height: 654321
- Number of transactions: 987654
- Memory Used: 256MB
- Uptime: 48 hours
==================================================
\`\`\`

#### Transmission of transactions
\`\`\`bash
python hyperflux.py send --address 0x1234abcd --amount 50
\`\`\`

Output:
\`\`\`plaintext
==================================================
Transaction sent to:
- Destination address: 0x1234abcd
- Amount of tokens to send: 50
Transaction being sent...
Transaction ID: 0xabcd1234efgh5678
Transaction successfully submitted.
==================================================
\`\`\`

### ⚙️ Why This is Feasible
HyperFlux achieves its goals through the following innovations:
1. **Proprietary BFT + DAG Algorithm**: Rapid processing and finalization of transactions with high throughput.
2. **zk-SNARKs technology**: Provides a trusted blockchain environment with enhanced data privacy and security.
3. **Sharding technology**: Effectively distributes network load and improves scalability.
4. **EVM compatibility**: Compatibility with the existing Ethereum ecosystem makes it easier for developers to use existing tools and libraries.
5. **Using Autonomous Development Software**: The advent of autonomous development software such as OpenDevin has greatly increased the efficiency of the development process and enabled the implementation of advanced technologies.

### Why this has never been done before.
Traditional blockchain projects have faced the so-called “trilemma” of scalability, security, and decentralization. Many projects focused on some of these elements, making it very difficult to achieve all of them simultaneously. For example, combining EVM compatibility with zk-SNARKs was technically very complex and required a lot of resources and time.

However, HyperFlux has adopted a new approach to overcome these challenges by integrating the research results and technologies accumulated to date. Specifically, the following factors make this possible:
1. **Integration of state-of-the-art research and technology**: By combining state-of-the-art blockchain technology and algorithms, we were able to overcome the previous technical limitations.
2. **Strong Development Team and Community**: The collaboration between the expert team and the open source community enables rapid technology development and problem solving.
3. **Using Autonomous Development Software**: Tools like OpenDevin streamline the development process and make it easier to implement complex technologies.
4. **Continuous Improvement and Testing**: Through continuous testing and feedback loops, we are improving the reliability and performance of our technology.

These factors enable HyperFlux to deliver performance and convenience that outperforms other blockchain projects and enables the next generation of blockchain technology.

For more information, please refer to the [CONTRIBUTING GUIDE](./docs/CONTRIBUTING.md).
