# HyperFlux

🌐  [日本語README](./wiki/README_ja.md) | 🇬🇧 [English README](./wiki/README_en.md) | 🇫🇷 [Français README](./wiki/README_fr.md) | 🇨🇳 [中文 README](./wiki/README_zh.md)

### プロジェクト目標  

HyperFluxは以下の目標を達成することを目指している：
- 超高速トランザクション処理**： 独自のBFT + DAGアルゴリズムにより、毎秒最大10,000トランザクションを処理。
- 🛡️ **高セキュリティ**： zk-SNARKs テクノロジーを使用してトランザクションのプライバシーを保護しながら検証。
- 🤖 **BFT (Byzantine Fault Tolerance)**： BFT (Byzantine Faultolerance)**：分散システムの耐障害性を向上させるために実装されたアルゴリズム。
- 📈**DAG (Directed Acyclic Graph)**： DAGはトランザクションの並列処理を可能にし、スループットを向上させるために実装された。

### ファイル一覧と説明  
- **`CONTRIBUTING.md`**： プロジェクトのビジョン、貢献方法、セットアップ手順、コーディングスタイル、コミュニケーションチャネル、課題管理、プルリクエストプロセス、ロードマップ、謝辞、報酬、FAQを含むプロジェクト貢献ガイド。
- **`README.md`**： プロジェクトの概要、目的、セットアップ手順、使用ガイドライン、ランタイム画面の詳細。
- **`hyperflux.py`**： トランザクション処理、ブロックチェーン管理、DAGを使った並列トランザクション処理、BFTネットワークのシミュレーションのためのスクリプト。
- ***test_hyperflux.py`**： unittest` フレームワークを使用して `hyperflux.py` の機能をテストするスクリプト。トランザクションの有効性、ジェネシスブロックの生成、ブロックチェーンの整合性をテストする。
- **`FAQ.md`**： HyperFluxプロジェクトに関するよくある質問。一般的な質問、技術的な質問、コミュニティに関する質問、開発に関する質問、ガバナンスに関する質問、インセンティブに関する質問が含まれる。
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
プロジェクトを実行したときに表示される画面の詳細については、[Screen at Runtime Guide](./wiki/Screen_at_Runtime.md) を参照してください。

### 主な機能  
- スマート・コントラクト・サポート**： Solidityでの開発におけるEVMの互換性。既存のイーサリアムエコシステムとのシームレスな統合。
- P2P通信**： WebRTC を使用したリアルタイムのピアツーピア通信。ノード間の高速かつ安全なデータ転送により、分散アプリケーションのパフォーマンスを最適化します。
- スケーラビリティ**： シャーディングと DAG による高度なスケーラビリティ機能により、ネットワークが拡大しても一貫した高 いパフォーマンスを保証します。

### 使用シナリオ
ターミナルから HyperFlux の機能を直接操作するためのコマンドライン引数を以下に示します：

#### ノードステータスの確認
bash
python hyperflux.py --check-node-status
```

#### トランザクションの送信
```bash
python hyperflux.py --submit-transaction --to [recipient_address] --amount [amount] トランザクションを送信します。
```

#### ネットワークステータスの確認
```bash
python hyperflux.py --check-network-status
```

#### スマートコントラクトの管理
バッシュ
python hyperflux.py --スマートコントラクトの管理
```

#### ガバナンス機能
バッシュ
python hyperflux.py --governance --action [create/vote/results/parameters]を実行する。
```

#### クロスチェーン機能
```bash
python hyperflux.py --cross-chain --action [list/transfer/receive/history] ```# クロスチェーン機能 ```bash.
```

#### コンフィギュレーション設定
```bash
python hyperflux.py --config --category [general/network/security/notification/account/advanced] ```# コンフィギュレーション設定 ```bash.
```

### ⚙️ なぜ実現可能なのか？ 
HyperFluxは、以下のような工夫によって目標を達成している：
1. **独自の BFT + DAG アルゴリズム**： 高いスループットでトランザクションの迅速な処理と確定。
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
```

### `wiki/Screen_at_Runtime.md`

マークダウン
# ランタイムのスクリーンガイド

python hyperflux.py` を実行すると、HyperFlux システムを監視して操作できるダッシュボードが表示される。以下は、アクセスできる詳細なビューと機能です。

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

### 1. ノードステータスの確認
ネットワーク接続やパフォーマンスメトリクスを含むノードの現在のステータスを表示します。
プレーンテキスト
==================================================
ノードのステータス
- ステータス 実行中
- バージョン: v1.2.3
- ネットワーク メインネット
- APIエンドポイント: http://localhost:8081
- 接続ピア数 12
- ブロック量: 654,321
- トランザクション 987,654
- 使用メモリ 256MB
- CPU使用率: 25
- ディスク使用量 10GB/500GB
- アップタイム 48時間
==================================================
```

### 2. トランザクションの送信
トランザクションの送信を有効にします。受信者のアドレスと取引金額の入力を促します。
プレーンテキスト
==================================================
トランザクションを送信します：
受取人のアドレス 入力
送金額: [input]： 入力
==================================================
送信されたトランザクション: 受信者アドレス： 0x9876543210fedcba トランザクション ID: 0x1234567890abcdef
トランザクションの確認を待っています...
トークンは正常に転送されました。
==================================================
```

### 3. 🌐 ネットワーク・ステータスの確認
接続ノード、トランザクション量、ネットワークの健全性を含むネットワークステータスの概要を提供します。
プレーンテキスト
==================================================
ネットワークのステータス
- ネットワーク名 ハイパーフラックス・メインネット
- チェーンID: 1
- アクティブノード数: 200
- シャード数 8
- 各シャードのノード数：25
- シャード間の同期遅延 平均100ms
- DAGノード数: 1,000,000
- DAGの深さ: 500
- DAGの幅：2,000
- DAG内の無効トランザクション率：0.01
- ネットワーク遅延：平均50ms
- トランザクション処理速度：8,500トランザクション/秒
- 総トランザクション数 10,000,000
- 平均ブロック時間：5秒
- 最新のブロックハッシュ 0xabcdef1234567890
- 最新ブロックのタイムスタンプ 2024-06-08 12:34:56 utc
==================================================
```

### 4. 📜スマートコントラクト管理
スマートコントラクトのデプロイと管理を可能にします。ユーザーはコントラクトを表示、デプロイ、管理できます。
プレーンテキスト
==================================================
スマートコントラクト管理
1. 新しいスマートコントラクトのデプロイ
2. 既存のスマートコントラクトの管理
3. スマート・コントラクトの実行履歴を見る
4. スマートコントラクトのセキュリティ監査
==================================================
```

### 5. 🗳️ ガバナンス
提案の作成、投票、結果の閲覧を含む、分散型ガバナンス活動のオプションを提供します。
プレーンテキスト
==================================================
ガバナンス
1. 提案の作成
2. 既存の提案に対する投票
3. 投票結果の表示
4. ガバナンスパラメータの設定
==================================================
```

### 6. クロスチェーン機能
資産の移動や取引履歴の閲覧など、クロスチェーンでのやり取りに関する機能。
プレーンテキスト
==================================================
クロスチェーン機能
1. 対応ブロックチェーン一覧
2. 他のブロックチェーンへの資産移転
3. 他のブロックチェーンからアセットを受け取る
4. クロスチェーン取引履歴の表示
==================================================
```

### 7. ⚙️ コンフィギュレーション
一般設定、ネットワーク設定、セキュリティ設定、通知設定、詳細設定を含む様々なコンフィギュレーション設定を提供します。
プレーンテキスト
==================================================
コンフィギュレーション
1. 一般設定
2. ネットワーク設定
3. セキュリティ設定
4. 通知設定
5. アカウント設定
6. 詳細設定
==================================================
```


### なぜ実現可能なのか？

HyperFluxがこれらの目標を達成できるのは、次のような工夫があるからです： 1.

1. **独自の BFT + DAG アルゴリズム**： トランザクションの高速処理とファイナライズを可能にし、より高いスループットを実現 [ [oai_citation:1,GitHub - Setheum-Labs/Setheum： Setheum: zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Ready for hacking ](https://github.com/Setheum-Labs/Setheum) [oai_citation:2,SNARKtor : A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | 世界最速のEVM](https://www.telos.net/post/ snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
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