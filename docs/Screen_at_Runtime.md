# Screen at Runtime Guide

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

### 1. 🚀 Check Node Status
Displays the current status of the node including network connections and performance metrics.
```plaintext
==================================================
Node Status:
- Status: Running
- Version: v1.2.3
- Network: MainNet
- API Endpoint: http://localhost:8081
- Number of connected peers: 12
- Block Volume: 654,321
- Transactions: 987,654
- Memory used: 256MB
- CPU utilization: 25%
- Disk usage: 10GB/500GB
- Uptime: 48 hours
==================================================
```

### 2. 💸 Submit Transaction
Enables the submission of transactions. Prompts the user for recipient address and transaction amount.
```plaintext
==================================================
Submit Transaction:
Recipient address: [input]
Transfer amount: [input]
==================================================
Transaction sent: recipient address: 0x9876543210fedcba Transaction ID: 0x1234567890abcdef
Waiting for transaction confirmation...
Token successfully transferred.
==================================================
```

### 3. 🌐 Check Network Status
Provides an overview of the network status including connected nodes, transaction volume, and network health.
```plaintext
==================================================
Network Status:
- Network Name: HyperFlux MainNet
- Chain ID: 1
- Number of active nodes: 200
- Number of shards: 8
- Number of nodes per shard: 25
- Synchronization delay between shards: 100ms average
- Number of DAG nodes: 1,000,000
- Depth of DAG: 500
- Width of DAG: 2,000
- Invalid transaction rate in DAG: 0.01%
- Network latency: 50ms average
- Transaction processing speed: 8,500 transactions per second
- Total transactions: 10,000,000
- Average block time: 5 seconds
- Latest block hash: 0xabcdef1234567890
- Latest block timestamp: 2024-06-08 12:34:56 UTC
==================================================
```

### 4. 📜 Smart Contract Management
Allows deployment and management of smart contracts. Users can view, deploy, and manage contracts.
```plaintext
==================================================
Smart Contract Management:
1. Deploy a new smart contract
2. Manage existing smart contracts
3. View smart contract execution history
4. Smart contract security auditing
==================================================
```

### 5. 🗳️ Governance
Provides options for decentralized governance activities including creating proposals, voting, and viewing results.
```plaintext
==================================================
Governance:
1. Create a proposal
2. Vote on an existing proposal
3. View voting results
4. Set governance parameters
==================================================
```

### 6. 🌉 Cross-chain Functionality
Features related to cross-chain interactions such as asset transfers and viewing transaction history.
```plaintext
==================================================
Cross-chain functionality:
1. List of supported blockchains
2. Transfer assets to other blockchains
3. Receive assets from other blockchains
4. Display cross-chain transaction history
==================================================
```

### 7. ⚙️ Configuration
Provides various configuration settings including general, network, security, notifications, and advanced settings.
```plaintext
==================================================
Configuration:
1. General settings
2. Network settings
3. Security settings
4. Notification settings
5. Account settings
6. Advanced settings
==================================================
```
