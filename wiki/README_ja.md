
## ハイパーフラックス
🌐 [日本語README](./wiki/README_ja.md) | 🇬🇧 [英語README](./wiki/README_ja.md) | 🇫🇷 [フランス語README](./wiki/README_fr.md) | 🇨🇳 [中文README](./wiki/README_zh.md)

### プロジェクト目標  
HyperFluxは以下の目標を達成することを目指しています：
- 超高速トランザクション処理**： 独自のBFT + DAGアルゴリズムにより、毎秒最大10,000トランザクションを処理。
- 🛡️ **高セキュリティ**： zk-SNARKs テクノロジーを使用してトランザクションのプライバシーを保護しながら検証。
- 🤖 **BFT (Byzantine Fault Tolerance)**： BFT (Byzantine Faultolerance)**：分散システムの耐障害性を向上させるために実装されたアルゴリズム。
- 📈**DAG (Directed Acyclic Graph)**： DAGはトランザクションの並列処理を可能にし、スループットを向上させるために実装された。

### ファイル一覧と説明  
- **`CONTRIBUTING.md`**： プロジェクトのビジョン、貢献方法、セットアップ手順、コーディングスタイル、コミュニケーションチャネル、課題管理、プルリクエストプロセス、ロードマップ、謝辞、報酬、FAQを含むプロジェクト貢献ガイド。
- **`README.md`**： プロジェクトの概要、目的、セットアップ手順、使用ガイドライン、ランタイム画面の詳細。
- **`hyperflux.py`**： トランザクション処理、ブロックチェーン管理、DAGを使った並列トランザクション処理、BFTネットワークのシミュレーションのためのスクリプト。
- ***test_hyperflux.py`**： unittest` フレームワークを使用して `hyperflux.py` の機能をテストするスクリプト。トランザクションの有効性、ジェネシスブロックの生成、ブロックチェーンの整合性をテストする。
- **`__pycache__`**： Python バイトコードをキャッシュするためのディレクトリ。
- **`requirements.txt`**： Flask を含むプロジェクトの依存関係のリスト。
- **`wiki/`**： プロジェクトに関する追加ドキュメントを含むディレクトリ。

### 🛠️ セットアップ手順  
以下の手順に従って、HyperFlux をセットアップします：
1. **リポジトリをクローンする：
   bash
   git clone https://github.com/yukihamada/HyperFlux.git  
   cd HyperFlux  
   ```
2. **必要な依存関係**をインストールします：
   bash
   pip install -r requirements.txt  
   ```

### 🚀 使い方  
HyperFlux プロジェクトを起動するには、以下のコマンドを実行します：  
bash
python hyperflux.py  
```  

### 📖 実行時の画面詳細  
python hyperflux.py` を実行すると、HyperFlux システムを監視し、操作するためのダッシュボードが表示されます。以下は、アクセスできる詳細なビューと機能です。

## 初期画面
プロジェクトを開始すると、次のような画面が表示されます：
プレーンテキスト
==================================================
HyperFluxのステータス： 初期化中...
[設定の読み込み中...
[ネットワークに接続中...
[ノードの起動に成功しました。
==================================================
HyperFlux WEB インターフェース: http://localhost:8080
==================================================
ダッシュボード
1. ノードステータスの確認
2. トランザクションの送信
3. 🌐 ネットワークステータスの確認
4. スマート・コントラクトの管理
5. 🗳️ ガバナンス
6. クロスチェーン機能
7. ⚙️ コンフィギュレーション
==================================================
機能を選択 (1-7)：
```
プロジェクトを実行したときに表示される詳細な説明については、[Screen at Runtime Guide](./wiki/Screen_at_Runtime.md) を参照してください。

### 主な機能  
- スマート・コントラクト・サポート**： Solidityでの開発におけるEVMの互換性。既存のイーサリアムエコシステムとのシームレスな統合。
- P2P通信**： WebRTC を使用したリアルタイムのピアツーピア通信。ノード間の高速かつ安全なデータ転送により、分散アプリケーションのパフォーマンスを最適化します。
- スケーラビリティ**： シャーディングと DAG による高度なスケーラビリティ機能により、ネットワークが拡大しても一貫した高 いパフォーマンスを保証します。

### 使用例
以下は、コマンドライン引数を使用して HyperFlux の各機能を操作する例です。

#### ノードの状態を確認する
```bash
python hyperflux.py status
```

出力される：
プレーンテキスト
==================================================
ノードの状態：
- 状態： アクティブ
- 接続ピア数 12
- ブロックの高さ: 654321
- トランザクション数 987654
- 使用メモリ 256MB
- アップタイム 48時間
==================================================
```

#### トランザクションの送信
```bash
python hyperflux.py send --address 0x1234abcd --amount 50
```

出力する：
プレーンテキスト
==================================================
トランザクションが送信されました：
- 宛先アドレス 0x1234abcd
- 送信するトークンの量： 50
送信中のトランザクション
トランザクションID: 0xabcd1234efgh5678
トランザクションは正常に送信されました。
==================================================
```

### ⚙️ これが実現可能な理由  
HyperFluxは以下の革新的な技術によって目標を達成する：
1. **独自のBFT + DAGアルゴリズム**： 高いスループットでトランザクションの迅速な処理と確定。
2. **zk-SNARKsテクノロジー**： データプライバシーとセキュリティの強化。
3. **シャーディング・テクノロジー**： ネットワーク負荷の効果的な分散とスケーラビリティの向上。
4. **EVMの互換性**： イーサリアムエコシステム内の既存ツールやライブラリの使用が容易に。
5. **自律開発ソフトウェア**： OpenDevinのようなツールが開発プロセスを効率化する。

### 貢献する  
興味のある方はプロジェクトに貢献することが推奨されます。詳しくはリポジトリの`CONTRIBUTING.md`ファイルをご覧ください。

### ライセンス  
このプロジェクトはリポジトリの `LICENSE` ファイルで指定された条件の下でライセンスされています。

### 📘 貢献ガイド  
詳細については、[CONTRIBUTING GUIDE](./CONTRIBUTING.md)を参照してください。

HyperFluxをより良くするために、自由に探求し、貢献してください！🚀🔋

### なぜ実現可能なのか？

HyperFluxがこれらの目標を達成できるのは、次のような工夫があるからです： 1.

1. **独自のBFT + DAGアルゴリズム**： トランザクションの高速処理とファイナライズを可能にし、より高いスループットを実現 [ [oai_citation:1,GitHub - Setheum-Labs/Setheum： Setheum: zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_citation:2,SNARKtor : A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | 世界最速のEVM](https://www.telos.net/post/ snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. **zk-SNARKsテクノロジー**: データのプライバシーとセキュリティを強化した信頼できるブロックチェーン環境を提供する[ [oai_citation:3,Zero-knowledge rollups | ethereum.org](https:// ethereum.org/ja/developers/docs/scaling/zk-rollups/)].
3. **シャーディング技術**: ネットワークの負荷を効果的に分散し、スケーラビリティを向上させる [ [oai_citation:4,The Convergence of Zero-Knowledge Proofs and Decentralized Systems： パート2｜AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:5,ZkEVMの説明：zkロールアップの未来を検証する - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)
4. **EVM互換性**：既存のイーサリアムエコシステムとの互換性により、開発者は既存のツールやライブラリを使いやすくなる [ [oai_citation:6,The Sudden Rise of EVM-Compatible ZK Rollups]](https ://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
5. **自律型開発ソフトウェアの使用**： OpenDevinのような自律型開発ソフトウェアの登場は、開発プロセスの効率を大幅に向上させ、高度な技術の実装を可能にした。

### なぜこのようなことがこれまでになかったのか。

従来のブロックチェーン・プロジェクトは、スケーラビリティ、セキュリティ、分散化といういわゆる「トリレンマ」に直面してきた。多くのプロジェクトは、これらの要素の一部に焦点を当てており、すべてを同時に実現することは非常に困難であった。例えば、EVMの互換性とzk-SNARKsを組み合わせることは技術的に非常に複雑で、多くのリソースと時間を必要とした[[oai_citation:7,SNARKtor： A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for- scaling-snarks-verification-in-blockchains) [oai_citation:8,The Convergence of Zero-Knowledge Proofs and Decentralized Systems： その2｜AdaPulse]( AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:9,ZkEVMの説明：zkロールアップの未来を検証する - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)

しかし、HyperFluxは、これまで蓄積してきた研究成果や技術を統合することで、これらの課題を克服する新たなアプローチを採用した。具体的には、1.

1. **最先端の研究と技術の統合**：最先端のブロックチェーン技術とアルゴリズムを組み合わせることで、これまでの技術的限界を克服することができました [ [oai_citation:10,GitHub - Setheum-Labs/Setheum： Setheum: zk- SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_ citation:11,SNARKtor： A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | 世界最速のEVM](https:// www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2.**強力な開発チームとコミュニティ**： 専門家チームとオープンソースコミュニティの連携により、迅速な技術開発と問題解決が可能である[[oai_citation:12,EVM互換ZKロールアップの急浮上]]( https://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
3. **自律型開発ソフトウェアの使用**： OpenDevinのようなツールは開発プロセスを合理化し、複雑な技術の実装を容易にする。
4. **継続的な改善とテスト**： 継続的なテストとフィードバック・ループを通じて、私たちは技術の信頼性と性能を向上させています： パート2｜AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2 /) [oai_citation:14,ZkEVM explained: zk rollupsの未来を検証する - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of- zk-rollups/)

これらの要因により、HyperFluxは他のブロックチェーン・プロジェクトを凌駕するパフォーマンスと利便性を実現し、次世代のブロックチェーン技術を可能にする。

## 貢献する

関心のある方は、プロジェクトに貢献することをお勧めします。詳しくはリポジトリのCONTRIBUTING.mdをご覧ください。

## コントリビューションガイド

詳細は[CONTRIBUTING GUIDE](./CONTRIBUTING.md)を参照してください。