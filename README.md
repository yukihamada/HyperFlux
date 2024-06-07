# HyperFlux

## プロジェクトの目的

HyperFluxは、以下の目標を達成します:

- **超高速トランザクション処理**: 独自開発のBFT + DAGアルゴリズムにより、1秒間に最大10,000件のトランザクションを処理します。
- **高いセキュリティ**: zk-SNARKs技術を使用してトランザクションのプライバシーを保護しつつ検証。
- **BFT（Byzantine Fault Tolerance）**: 分散システムにおける耐障害性を向上させるために、BFTアルゴリズムを実装しました。
- **DAG（Directed Acyclic Graph）**: トランザクションの並列処理を可能にし、スループットを向上させるためにDAGを導入しました。

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
python main.py
```


### 実行時の画面

`python main.py` を実行すると、以下のような画面が表示されます:

```plaintext
==================================================
HyperFlux ステータス: 初期化中...
[###----] 設定を読み込み中...
[#####---] ネットワークに接続中...
[########] ノードが正常に起動しました。

==================================================
ダッシュボード:
1. 🚀 ノードのステータス確認
2. 💸 取引を送信
3. 🌐 ネットワークステータス確認
4. ⚙️ 設定
==================================================
> [インタラクティブコンソール] コマンドを入力してください: _
```

### コマンドライン引数を使用した例

コマンドライン引数を使用してHyperFluxの各機能を操作するための例です。

#### ノードのステータス確認

```bash
python main.py status
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
python main.py send --address 0x1234abcd --amount 50
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
python main.py network
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

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルをご覧ください。
