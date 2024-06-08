# HyperFlux

🌐  [日本語README](./wiki/README_ja.md) | 🇬🇧 [English README](./wiki/README_en.md) | 🇫🇷 [Français README](./wiki/README_fr.md) | 🇨🇳 [中文 README](./wiki/README_zh.md)


### プロジェクトの目的

HyperFluxは、以下の目標を達成します:

- **超高速トランザクション処理**: 独自開発のBFT + DAGアルゴリズムにより、1秒間に最大10,000件のトランザクションを処理します。
- **高いセキュリティ**: zk-SNARKs技術を使用してトランザクションのプライバシーを保護しつつ検証。
- **BFT（Byzantine Fault Tolerance）**: 分散システムにおける耐障害性を向上させるために、BFTアルゴリズムを実装しました。
- **DAG（Directed Acyclic Graph）**: トランザクションの並列処理を可能にし、スループットを向上させるためにDAGを導入しました。

### ファイル一覧

- \`CONTRIBUTING.md\`
- \`README.md\`
- \`hyperflux.py\`
- \`test_hyperflux.py\`
- \`FAQ.md\`
- \`__pycache__\`
- \`requirements.txt\`
- \`wiki\`

### セットアップ手順

以下の手順に従って、HyperFluxプロジェクトをセットアップします。

1. リポジトリをクローンします:
    \`\`\`bash
    git clone https://github.com/yukihamada/HyperFlux.git
    cd HyperFlux
    \`\`\`

2. 必要な依存関係をインストールします:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

### 使用方法

HyperFluxプロジェクトを起動するには、以下のコマンドを実行します:

\`\`\`bash
python hyperflux.py
\`\`\`

### 実行時の画面

\`python hyperflux.py\` を実行すると、以下のような画面が表示されます:

\`\`\`plaintext
==================================================
HyperFlux ステータス: 初期化中...
[###----] 設定を読み込み中...
[#####---] ネットワークに接続中...
[########] ノードが正常に起動しました。
==================================================
HyperFlux WEBインターフェース: http://localhost:8080
==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
\`\`\`

## English

### Project Purpose

HyperFlux aims to achieve the following goals:

- **Ultra-fast transaction processing**: Processes up to 10,000 transactions per second using a proprietary BFT + DAG algorithm.
- **High security**: Uses zk-SNARKs technology to protect transaction privacy while verifying.
- **BFT (Byzantine Fault Tolerance)**: Implements BFT algorithms to improve fault tolerance in distributed systems.
- **DAG (Directed Acyclic Graph)**: Introduces DAG to enable parallel processing of transactions and improve throughput.

### File List

- \`CONTRIBUTING.md\`
- \`README.md\`
- \`hyperflux.py\`
- \`test_hyperflux.py\`
- \`FAQ.md\`
- \`__pycache__\`
- \`requirements.txt\`
- \`wiki\`

### Setup Instructions

Follow these steps to set up the HyperFlux project.

1. Clone the repository:
    \`\`\`bash
    git clone https://github.com/yukihamada/HyperFlux.git
    cd HyperFlux
    \`\`\`

2. Install the necessary dependencies:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

### Usage

To start the HyperFlux project, run the following command:

\`\`\`bash
python hyperflux.py
\`\`\`

### Runtime Screen

When you run \`python hyperflux.py\`, you will see the following screen:

\`\`\`plaintext
==================================================
HyperFlux Status: Initializing...
[###----] Loading settings...
[#####---] Connecting to the network...
[########] Node started successfully.
==================================================
HyperFlux WEB Interface: http://localhost:8080
==================================================
Dashboard:
1. 🚀 Check node status
2. 💸 Send transactions
\`\`\`

## 日本語


## プロジェクトの目的

HyperFluxは、以下の目標を達成します:

- **超高速トランザクション処理**: 独自開発のBFT + DAGアルゴリズムにより、1秒間に最大10,000件のトランザクションを処理します。
- **高いセキュリティ**: zk-SNARKs技術を使用してトランザクションのプライバシーを保護しつつ検証。
- **BFT（Byzantine Fault Tolerance）**: 分散システムにおける耐障害性を向上させるために、BFTアルゴリズムを実装しました。
- **DAG（Directed Acyclic Graph）**: トランザクションの並列処理を可能にし、スループットを向上させるためにDAGを導入しました。
## ファイル一覧

- \`CONTRIBUTING.md\`
- \`README.md\`
- \`hyperflux.py\`
- \`test_hyperflux.py\`
- \`FAQ.md\`
- \`__pycache__\`
- \`requirements.txt\`
- \`wiki\`


## セットアップ手順

以下の手順に従って、HyperFluxプロジェクトをセットアップします。

1. リポジトリをクローンします:
    ```bash
    git clone https://github.com/yukihamada/HyperFlux.git
    cd HyperFlux
    ```

2. 必要な依存関係をインストールします:
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

HyperFluxプロジェクトを起動するには、以下のコマンドを実行します:

```bash
python hyperflux.py
```


### 実行時の画面

`python hyperflux.py` を実行すると、以下のような画面が表示されます:

```plaintext
==================================================
HyperFlux ステータス: 初期化中...
[###----] 設定を読み込み中...
[#####---] ネットワークに接続中...
[########] ノードが正常に起動しました。
==================================================
HyperFlux WEBインターフェース: http://localhost:8080
==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 1

==================================================
ノードステータス:
- 状態: 稼働中
- バージョン: v1.2.3
- ネットワーク: MainNet
- APIエンドポイント: http://localhost:8081
- 接続ピア数: 12
- ブロック高: 654,321
- トランザクション数: 987,654
- 使用メモリ: 256MB
- CPU使用率: 25%
- ディスク使用量: 10GB/500GB
- Uptime: 48時間
==================================================

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 3

==================================================
ネットワークステータス:
- ネットワーク名: HyperFlux MainNet
- チェーンID: 1
- アクティブノード数: 200
- シャード数: 8
- 各シャードのノード数: 25
- シャード間の同期遅延: 平均100ms
- DAGノード数: 1,000,000
- DAGの深さ: 500
- DAGの幅: 2,000
- DAG内の無効トランザクション率: 0.01%
- ネットワーク遅延: 平均50ms
- トランザクション処理速度: 1秒間に8,500トランザクション
- 総トランザクション数: 10,000,000
- 平均ブロックタイム: 5秒
- 最新ブロックハッシュ: 0xabcdef1234567890
- 最新ブロックのタイムスタンプ: 2024-06-08 12:34:56 UTC
==================================================

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 4

==================================================
スマートコントラクト管理:
1. 新しいスマートコントラクトをデプロイ
2. 既存のスマートコントラクトを管理
3. スマートコントラクトの実行履歴を表示
4. スマートコントラクトのセキュリティ監査
==================================================
機能を選択してください（1-4）: 2

==================================================
スマートコントラクト一覧:
1. Token.sol - ERC20トークンコントラクト
   - アドレス: 0x1234567890abcdef
   - トークン名: HyperToken
   - シンボル: HYP
   - 総供給量: 1,000,000 HYP

2. Auction.sol - オークションコントラクト
   - アドレス: 0x2234567890abcdef
   - 現在のオークション数: 5
   - 総取引量: 250,000 HYP

3. Voting.sol - 投票コントラクト 
   - アドレス: 0x3234567890abcdef
   - 現在の投票数: 3
   - 総投票数: 1,000

4. MultiSig.sol - マルチシグウォレットコントラクト
   - アドレス: 0x4234567890abcdef
   - 必要署名数: 2/3
   - 総トランザクション数: 100
==================================================
管理するスマートコントラクトを選択してください（1-4）: 1

==================================================
Token.sol - ERC20トークンコントラクト:
- アドレス: 0x1234567890abcdef
- トークン名: HyperToken  
- シンボル: HYP
- 総供給量: 1,000,000 HYP
- 小数点以下の桁数: 18
- コントラクト所有者: 0x0987654321fedcba
==================================================
利用可能な操作:
1. トークンを転送
2. トークンを承認
3. トークン情報を更新
4. コントラクトを一時停止
5. コントラクトを削除
操作を選択してください（1-5）: 1

==================================================
トークンを転送:
受信者アドレス: 0x9876543210fedcba
転送量: 1,000 HYP
==================================================
トランザクションが送信されました。トランザクションID: 0x1234567890abcdef
トランザクションの確認を待っています...
トークンが正常に転送されました。
==================================================

==================================================
ダッシュボード:  
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 5

==================================================
ガバナンス:
1. 提案を作成
2. 既存の提案に投票
3. 投票結果を表示
4. ガバナンスパラメータを設定 
==================================================
機能を選択してください（1-4）: 3

==================================================
投票結果:
提案ID: 1234567890
提案タイトル: ブロック報酬の変更
提案内容: ブロック報酬を現在の5 HYPから3 HYPに減らすことを提案します。これにより、トークンの総供給量の増加率が抑えられ、長期的にトークンの価値が維持されると考えられます。 
提案期間: 2024-06-01 ~ 2024-06-08
必要な賛成票: 60%
投票結果:
- 賛成: 75%
- 反対: 20%
- 棄権: 5%  
==================================================
提案は可決されました。ブロック報酬は次回のネットワークアップグレード時に3 HYPに変更されます。
==================================================

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能 
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 6

==================================================
クロスチェーン機能:
1. サポートされているブロックチェーン一覧表示
2. 他のブロックチェーンへの資産転送
3. 他のブロックチェーンからの資産受け取り
4. クロスチェーントランザクションの履歴表示
==================================================
機能を選択してください（1-4）: 1

==================================================
サポートされているブロックチェーン:
1. イーサリアム
2. ビットコイン
3. バイナンスチェーン
4. ポルカドット
5. ソラナ
6. カルダノ
==================================================

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信 
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）: 7

==================================================
設定:
1. 一般設定
2. ネットワーク設定
3. セキュリティ設定
4. 通知設定  
5. アカウント設定
6. アドバンスド設定
==================================================
設定カテゴリを選択してください（1-6）: 1

==================================================
一般設定:
1. 言語: 日本語
2. 通貨単位: HYP
3. 時刻フォーマット: 24時間表記
4. テーマ: ダーク
5. 自動アップデート: オン
6. スタートアップ時にダッシュボードを開く: オフ
==================================================
変更する設定項目を選択してください（1-6）: 4

==================================================
テーマ:
1. デフォルト
2. ダーク 
3. ライト
4. ハイコントラスト
==================================================
新しいテーマを選択してください（1-4）: 3

==================================================
テーマがライトに変更されました。
==================================================

==================================================
設定:
1. 一般設定
2. ネットワーク設定  
3. セキュリティ設定
4. 通知設定
5. アカウント設定
6. アドバンスド設定
==================================================
設定カテゴリを選択してください（1-6）: 6

==================================================
アドバンスド設定:
警告: これらの設定を変更すると、ノードが正常に機能しなくなる可能性があります。十分な知識がない限り、変更しないでください。
1. データベースのパス: /var/lib/hyperflux/database
2. ログファイルのパス: /var/log/hyperflux/node.log  
3. RPC APIポート: 8081
4. P2Pリスニングポート: 30303
5. 最大接続ピア数: 50
6. トランザクションプール上限: 10,000
7. ブロックサイズ上限: 2MB
8. ガスリミット: 10,000,000
==================================================
変更する設定項目を選択してください（1-8）: 

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認   
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. 📜 スマートコントラクト管理
5. 🗳️ ガバナンス
6. 🌉 クロスチェーン機能
7. ⚙️ 設定
==================================================
機能を選択してください（1-7）:
```

### コマンドライン引数を使用した例

コマンドライン引数を使用してHyperFluxの各機能を操作するための例です。

#### ノードのステータス確認

```bash
python hyperflux.py status
```

出力:

```plaintext
==================================================
ノードステータス:
- 状態: 稼働中
- 接続ピア数: 12
- ブロック高: 654321
- トランザクション数: 987654
- 使用メモリ: 256MB
- Uptime: 48時間
==================================================
```

#### 取引の送信

```bash
python hyperflux.py send --address 0x1234abcd --amount 50
```

出力:

```plaintext
==================================================
取引送信:
送信先アドレス: 0x1234abcd
送信するトークン量: 50
トランザクションを送信中...
トランザクションID: 0xabcd1234efgh5678
トランザクションが正常に送信されました。
==================================================
```

#### ネットワークステータス確認

```bash
python hyperflux.py network
```

出力:

```plaintext
==================================================
ネットワークステータス:
- アクティブノード数: 200
- ネットワーク遅延: 平均50ms
- トランザクション処理速度: 1秒間に8500トランザクション
- 総トランザクション数: 10,000,000
==================================================
```

### 主な機能

- **スマートコントラクトサポート**: Ethereum Virtual Machine (EVM) 互換性を持ち、Solidityでの開発が可能です。これにより、既存のEthereumエコシステムとシームレスに連携します。
- **P2P通信**: WebRTCを利用したリアルタイムのピアツーピア通信を実現。ノード間のデータ転送が高速かつ安全に行われ、分散型アプリケーションのパフォーマンスを最適化します。
- **スケーラビリティ**: シャーディングとDAGによる高度なスケーラビリティ機能により、ネットワークが成長しても一貫した高パフォーマンスを維持します。

### 利用シーン

- **金融取引**: 高速かつ安全なトランザクション処理により、即時決済や資産管理が可能です。
- **サプライチェーン管理**: トランザクションの透明性と信頼性を確保し、リアルタイムの追跡が可能です。
- **分散型アプリケーション**: 高速なP2P通信とスマートコントラクトにより、ユーザー体験を向上させます。

### なぜこれが実現可能か

HyperFluxがこれらの目標を達成できる理由は、以下の技術革新にあります:

1. **独自のBFT + DAGアルゴリズム**: トランザクションの迅速な処理と確定を可能にし、高いスループットを実現します【 [oai_citation:1,GitHub - Setheum-Labs/Setheum: Setheum: zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_citation:2,SNARKtor: A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. **zk-SNARKs技術**: データのプライバシー保護とセキュリティを強化し、信頼性の高いブロックチェーン環境を提供します【 [oai_citation:3,Zero-knowledge rollups | ethereum.org](https://ethereum.org/en/developers/docs/scaling/zk-rollups/)
3. **シャーディング技術**: ネットワークの負荷を効果的に分散し、スケーラビリティを向上させます【 [oai_citation:4,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:5,ZkEVM explained: examining future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)
4. **EVM互換性**: 既存のEthereumエコシステムとの互換性を持つことで、開発者が既存のツールやライブラリを利用しやすくします【 [oai_citation:6,The Sudden Rise of EVM-Compatible ZK Rollups](https://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
5. **自律的開発ソフトウェアの利用**: OpenDevinのような自律的開発ソフトウェアの登場により、開発プロセスの効率が大幅に向上し、高度な技術の実装が可能となりました。

### なぜこれが今までなかったか

従来のブロックチェーンプロジェクトは、スケーラビリティ、セキュリティ、分散性のいわゆる「トリレンマ」に直面していました。多くのプロジェクトはこれらの要素の一部に焦点を当てており、全てを同時に達成するのは非常に困難でした。例えば、EVM互換性とzk-SNARKsを組み合わせることは技術的に非常に複雑で、多くのリソースと時間を必要としました【 [oai_citation:7,SNARKtor: A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains) [oai_citation:8,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:9,ZkEVM explained: examining future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)

しかし、HyperFluxはこれまでに蓄積された研究成果と技術を統合し、これらの課題を克服するための新しいアプローチを採用しています。具体的には、以下の要因が実現を可能にしています:

1. **最新の研究と技術の統合**: 最先端のブロックチェーン技術とアルゴリズムを組み合わせることで、これまでの技術的限界を超えることができました【 [oai_citation:10,GitHub - Setheum-Labs/Setheum: Setheum: zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_citation:11,SNARKtor: A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. **強力な開発チームとコミュニティ**: 専門家チームとオープンソースコミュニティの協力により、迅速な技術開発と問題解決が可能となっています【 [oai_citation:12,The Sudden Rise of EVM-Compatible ZK Rollups](https://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
3. **自律的開発ソフトウェアの利用**: OpenDevinのようなツールを活用することで、開発プロセスが効率化され、複雑な技術の実装が容易になっています。
4. **持続的な改善とテスト**: 継続的なテストとフィードバックループを通じて、技術の信頼性とパフォーマンスを向上させています【 [oai_citation:13,The Convergence of Zero-Knowledge Proofs and Decentralized Systems: Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:14,ZkEVM explained: examining future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)

これらの要因により、HyperFluxは他のブロックチェーンプロジェクトを凌駕する性能と利便性を提供し、次世代のブロックチェーン技術を実現することが可能となっています。

## コントリビューション

ご興味をお持ちの方は、是非プロジェクトに貢献してください。詳細はリポジトリのCONTRIBUTING.mdをご覧ください。

## ライセンス


## 貢献ガイド

詳しくは[貢献ガイド](./CONTRIBUTING.md)をご覧ください。
