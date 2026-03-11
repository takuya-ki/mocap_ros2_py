# プロジェクト概要
mocap_ros2_py
Perception NeuronのモーションキャプチャデータをROS 2 (Humble) 環境で受信・可視化するためのシステムおよびDocker環境プロジェクト。


## 1. ディレクトリ構造と実行環境
本プロジェクトは、モーションキャプチャソフトウェア（Axis Studio）を実行するWindows PCと、ROS 2ノードを実行するUbuntu PC（Dockerコンテナ）の連携で構成されます。
- **ROS 2環境**: Docker Composeにより構築される `pnmocap_ros2_container` 内の `/root/ros2_ws/src` で動作します。
- **共有ディレクトリ**: ホストの `./docker/ros2_ws/src` がコンテナにマウントされ、ROS 2のPythonノード（`mocap_to_stickman.py` 等）の実行基盤となります。
- **ミドルウェア**: デフォルトで `rmw_fastrtps_cpp` が設定されており、`FASTDDS_SHM_DISABLE=1` が有効化されています。

## 2. 開発と運用の厳格なルール
### A. ネットワークとファイアウォールの制約
- Axis Studioが稼働するWindows PCとUbuntu PCは同一LAN内にある必要があります。
- Windows Defender等を使用している場合、`wf.msc`（セキュリティが強化されたWindows Defender ファイアウォール）から、ポート `7001` および `7012` に対して受信・送信の許可ルールを追加することが必須です。

### B. ソフトウェアの起動とGUI表示
- RViz2などのGUIアプリケーションを表示するため、コンテナ起動前にホスト側で `xhost +` を実行し、X11フォワーディングの権限を許可する必要があります。
- 実行時は、ROS 2環境のセットアップスクリプト（`source /opt/ros/humble/setup.bash` および `/root/ros2_ws/install/setup.bash`）がロードされていることを確認してください。

## 3. エージェントのルーティングルール（PMへの指示）
タスクのフェーズに応じて、以下の専門エージェントに的確に委譲してください。
- **アーキテクチャ設計・トピック構成・ネットワーク設計**: `architect` に依頼
- **ROS 2ノードの実装・tf2パブリッシャの記述**: `developer` に依頼
- **Colconビルド・RViz2の起動・Axis Studioからの受信テスト**: `tester` に依頼
- **UDP通信ブロック・ビルドエラー・RViz表示エラーの解消**: `debugger` に依頼