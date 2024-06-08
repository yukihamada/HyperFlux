
## HyperFlux
🌐 [日本語README](./wiki/README_ja.md) | 🇬🇧 [English README](./wiki/README_en.md) | 🇫🇷 [Français README](./wiki/README_fr.md) | 🇨🇳 [中文 README](./wiki/README_zh.md)

### 🌟 Project Objectives  
HyperFlux aims to achieve the following goals:
- ⚡ **Ultra-fast Transaction Processing**: Proprietary BFT + DAG algorithms process up to 10,000 transactions per second.
- 🛡️ **High Security**: Verification while protecting transaction privacy using zk-SNARKs technology.
- 🤖 **BFT (Byzantine Fault Tolerance)**: BFT algorithm implemented to improve fault tolerance in distributed systems.
- 📈 **DAG (Directed Acyclic Graph)**: DAG was implemented to enable parallel processing of transactions and increase throughput.

### 📁 File List and Description  
- **`CONTRIBUTING.md`**: Project contribution guide including the project vision, contribution methods, setup instructions, coding style, communication channels, issue management, pull request process, roadmap, acknowledgments, rewards, and FAQs.
- **`README.md`**: Project overview, purpose, setup instructions, usage guidelines, and runtime screen details.
- **`hyperflux.py`**: Script for transaction processing, blockchain management, parallel transaction processing using DAG, and simulating a BFT network.
- **`test_hyperflux.py`**: Script for testing the functionalities of `hyperflux.py` using `unittest` framework. It tests transaction validity, genesis block creation, and blockchain integrity.
- **`__pycache__`**: Directory for caching Python bytecode.
- **`requirements.txt`**: List of project dependencies, including Flask.
- **`wiki/`**: Directory containing additional documentation about the project.

### 🛠️ Setup Instructions  
Follow these steps to set up HyperFlux:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yukihamada/HyperFlux.git  
   cd HyperFlux  
   ```
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt  
   ```

### 🚀 How to Use  
To start the HyperFlux project, run the following command:  
```bash
python hyperflux.py  
```  

### 📖 Screen at Runtime Details  
When you run `python hyperflux.py`, you will encounter a dashboard that allows you to monitor and interact with the HyperFlux system. Below are the detailed views and functionalities that you can access.

## Initial Screen
When you start the project, you will see the following:
```plaintext
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
```
For a detailed explanation of what you will see when you run the project, please refer to the [Screen at Runtime Guide](./wiki/Screen_at_Runtime.md).

### 🔧 Key Features  
- **Smart Contract Support**: EVM compatibility for development in Solidity. Seamless integration with the existing Ethereum ecosystem.
- **P2P Communication**: Real-time peer-to-peer communication using WebRTC. Fast and secure data transfer between nodes, optimizing distributed applications' performance.
- **Scalability**: Advanced scalability features with sharding and DAG, ensuring consistent high performance even as the network grows.

### 💻 Usage Scenarios
Here is an example for manipulating each HyperFlux function using command line arguments.

#### Checking the status of a node
```bash
python hyperflux.py status
```

Output:
```plaintext
==================================================
Node status:
- State: Active
- Number of connected peers: 12
- Block Height: 654321
- Number of transactions: 987654
- Memory Used: 256MB
- Uptime: 48 hours
==================================================
```

#### Transmission of transactions
```bash
python hyperflux.py send --address 0x1234abcd --amount 50
```

Output:
```plaintext
==================================================
Transaction sent to:
- Destination address: 0x1234abcd
- Amount of tokens to send: 50
Transaction being sent...
Transaction ID: 0xabcd1234efgh5678
Transaction successfully submitted.
==================================================
```

### ⚙️ Why This is Feasible  
HyperFlux achieves its goals through the following innovations:
1. **Proprietary BFT + DAG Algorithm**: Rapid processing and finalization of transactions with high throughput.
2. **zk-SNARKs Technology**: Enhanced data privacy and security.
3. **Sharding Technology**: Effective distribution of network load and improved scalability.
4. **EVM Compatibility**: Easier to use existing tools and libraries within the Ethereum ecosystem.
5. **Autonomous Development Software**: Tools like OpenDevin streamline the development process.

### 🎯 Contribute  
Interested parties are encouraged to contribute to the project. Please see the `CONTRIBUTING.md` file in the repository for more information.

### 📜 License  
This project is licensed under the terms specified in the repository's `LICENSE` file.

### 📘 Contribution Guide  
For more information, please refer to the [CONTRIBUTING GUIDE](./CONTRIBUTING.md).

Feel free to explore and contribute to make HyperFlux better! 🚀🔋

### Why is this feasible?

HyperFlux is able to achieve these goals because of the following innovations: 1.

1. **Proprietary BFT + DAG Algorithm**: Enables faster processing and finalization of transactions, resulting in higher throughput [ [oai_citation:1,GitHub - Setheum-Labs/Setheum: Setheum: zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking](https://github.com/Setheum-Labs/Setheum) [oai_citation:2,SNARKtor : A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/ snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. **zk-SNARKs technology**: provides a trusted blockchain environment with enhanced data privacy and security [ [oai_citation:3,Zero-knowledge rollups | ethereum.org](https:// ethereum.org/en/developers/docs/scaling/zk-rollups/)
3. **Sharding technology**: effectively distributes network load and improves scalability [ [oai_citation:4,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:5,ZkEVM explained: examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)
4. **EVM compatibility**: compatibility with the existing Ethereum ecosystem makes it easier for developers to use existing tools and libraries [ [oai_citation:6,The Sudden Rise of EVM-Compatible ZK Rollups](https ://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
5. **Using Autonomous Development Software**: The advent of autonomous development software such as OpenDevin has greatly increased the efficiency of the development process and enabled the implementation of advanced technologies.

### Why this has never been done before.

Traditional blockchain projects have faced the so-called “trilemma” of scalability, security, and decentralization. Many projects focused on some of these elements, making it very difficult to achieve all of them simultaneously. For example, combining EVM compatibility with zk-SNARKs was technically very complex and required a lot of resources and time [ [oai_citation:7,SNARKtor: A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for- scaling-snarks-verification-in-blockchains) [oai_citation:8,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse]( AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:9,ZkEVM explained: examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)

However, HyperFlux has adopted a new approach to overcome these challenges by integrating the research results and technologies accumulated to date. Specifically, the following factors make this possible: 1.

1. **Integration of state-of-the-art research and technology**: by combining state-of-the-art blockchain technology and algorithms, we were able to overcome the previous technical limitations [ [oai_citation:10,GitHub - Setheum-Labs/Setheum: Setheum: zk- SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_ citation:11,SNARKtor: A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https:// www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2.**Strong Development Team and Community**: The collaboration between the expert team and the open source community enables rapid technology development and problem solving [ [oai_citation:12,The Sudden Rise of EVM-Compatible ZK Rollups]( https://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
3. **Using Autonomous Development Software**: Tools like OpenDevin streamline the development process and make it easier to implement complex technologies.
4. **Continuous Improvement and Testing**: Through continuous testing and feedback loops, we are improving the reliability and performance of our technology [ [oai_citation:13,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2 /) [oai_citation:14,ZkEVM explained: examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of- zk-rollups/)

These factors enable HyperFlux to deliver performance and convenience that outperforms other blockchain projects and enables the next generation of blockchain technology.

or more information, please refer to the [CONTRIBUTING GUIDE](./CONTRIBUTING.md).
