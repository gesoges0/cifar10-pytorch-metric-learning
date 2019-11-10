# cifar10-pytorch-metric-learning

metric learning for cifar10 [3channels images]

## 概要
Metric Learning を3チャネル画像で行うためのプログラム

- Network構造
  - Siamse Network
  - Triplet Newtowrk 
- 損失関数
  - Contrastive Loss
  - Online Contrastive Loss
  - Triplet Loss
  - Online Triplet Loss
  - Ranked List Loss
  - N-pair MC Loss
  
## 対象データセット
まず, cifar10のミラーサイトから画像としてのcifar10を取得する.
各クラスに対してディレクトリを作り, 以下のようなディレクトリ構成にする.
- ./dataset/cifar
  - train
    - bird
    - cat
    - deer
    - dog
    - frog
    - horse
  - test
    - airplane
    - automobile
    - ship
    - truck
    
 trainデータの各クラスは5000枚, testデータの各クラスは1000枚である.

## 学習の流れ
- データ読み込み
- ネットワーク定義
- 損失関数の定義
- 最適化関数の定義
- 学習
- 視覚化
- 推論

## 埋め込みネットワーク
基本となるネットワークは, 次のような構成とする. [EmbeddingNet](https://github.com/elasticnet12345/cifar10-pytorch-metric-learning/network.py)
