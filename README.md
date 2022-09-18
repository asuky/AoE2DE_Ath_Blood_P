Ath Blood P は、[AoE2 DE](https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/) 用対戦シナリオです。

# 前提
- AoE2 DE がインストールされていること
- Docker Compose が利用可能であること（要するに WSL 環境）

# 手を加えたい人向けのビルド手順
- 予め AoE2 DE のエディタで、トリガを入れないマップを作っておく
    - 極小マップで作成
    - エディタのコピー機能で、既存のマップをまるごとコピーすると早い（位置合わせが必要のため、細かい作業にはなる）
- .env.template をコピーして .env を作成、必要事項の記載（詳細は .env.template 参照のこと）
- WSL 上で docker-compose build
- ビルド完了後 docker-compose up -d
- コンテナ起動後 docker-compose exec scn bash
- シェル起動後、下記実施しシナリオファイルを書き出す
    - cd src
    - python main.py
- AoE2 DE 上のエディター等で Ath_Blood_P_{バージョン番号}.aoe2scenario を開く

