# Discord AI Art Bot
このプロジェクトは、Discordで動作するAIアートを生成するBotです。

## 概要
Stable Diffusionモデルを使用して、ユーザーのメッセージから画像を生成し、Discordのチャットに投稿します。

## 機能

- Discordのメッセージをトリガーとして画像生成
- Stable Diffusionを使用した高品質な画像生成
- Discordで簡単に利用可能

## 前提条件

- Python 3.8 以上
- Discordアカウント
- Hugging Faceアカウント（Stable Diffusion APIアクセス用）

## Discord Botアカウントの作成

1. Discordアカウントにログインします。
2. Discord Developer Portalにアクセスします。
3. 「New Application」をクリックして新しいアプリケーションを作成します。
4. アプリケーション名を入力し、「Create」をクリックします。
5. 左サイドバーから「Bot」を選択し、「Add Bot」をクリックします。
6. Botトークンは後ほどプログラムで使用するため、安全に保管してください。

## セットアップ

### 仮想環境の作成
このプロジェクトは、Pythonの仮想環境内で実行することをお勧めします。以下の手順に従ってください。

1. このリポジトリをクローンまたはダウンロードします。
2. プロジェクトのルートディレクトリで仮想環境を作成します。
```
python -m venv venv
```
3. 仮想環境をアクティベートします。
- Windows:
```
venv\Scripts\activate
```
- macOS/Linux:
```
source venv/bin/activate
```

### 依存関係のインストール

1. 必要なPythonライブラリをインストールします。
```
pip install -r requirements.txt
```
2. .envファイルをプロジェクトのルートディレクトリに作成し、以下の環境変数を設定します。
```
DISCORD_TOKEN=<あなたのDiscord Botトークン>
MODEL_ID=<Hugging FaceのモデルID>
DEVICE=<使用するデバイス: 'cuda' または 'cpu'>
HAGGINGFACE_TOKEN=<あなたのHugging Face APIトークン>
```

### 使用方法
1. Botを起動します。
```
python DiscordStableDiffusionBot.py
```
2. DiscordサーバーにBotを招待します。
3. Discordチャットで !img [画像を生成するためのテキスト] と入力します。
4. BotがAIを使用して画像を生成し、チャットに投稿します。
5. 作業が完了したら、以下のコマンドで仮想環境を終了します。
```
deactivate
```

## .gitignore ファイルの設定
このリポジトリには .gitignore ファイルが含まれており、それにより venv ディレクトリや他の不要なファイルがGitの追跡対象から除外されています。

## 作者
- Hayate Esaki

## ライセンス
このプロジェクトは、GNU General Public License v3.0の下でリリースされています。詳しくは「コピー」をご覧ください。詳しくは https://www.gnu.org/licenses/gpl-3.0.html をご覧ください。
