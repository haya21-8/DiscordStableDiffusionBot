import discord
import os
import torch
import time
from dotenv import load_dotenv
from torch import autocast
from diffusers import StableDiffusionPipeline

intents = discord.Intents.default()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
client = discord.Client(intents=intents)

# .envファイルから環境変数を読み込む
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') # Discord Botのトークン
MODEL_ID = os.getenv('MODEL_ID') # 学習済みモデルのID
DEVICE = os.getenv('DEVICE') # モデルを実行するデバイスの指定
HAGGINGFACE_TOKEN = os.getenv('HAGGINGFACE_TOKEN') # Hugging Face APIのトークン

# 学習済みモデルを設定し、StableDiffusionPipelineでパイプラインを作成する
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID, revision="fp16", torch_dtype=torch.float16, use_auth_token=HAGGINGFACE_TOKEN
)
pipe.to(DEVICE)

# Discord Botを起動するための設定をする
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Botが起動した時にメッセージを表示する
@client.event
async def on_ready():
    print("起動完了")

# ユーザーからメッセージが送信された時の処理を設定する
@client.event
async def on_message(message):
    # Bot自身からのメッセージは無視する
    if message.author == client.user:
        return
        
    # "!img [入力文字列]"という形式のメッセージが送信された場合
    elif message.content.startswith('!img'):
        prompt = message.content[5:] # ユーザーが入力した文字列を取得する
        with autocast(DEVICE):
            # パイプラインを実行し、画像を生成する
            image = pipe(prompt, guidance_scale=7.5)["images"][0]
            timestamp = int(time.time())
            filename = f"output/image_{timestamp}.png"
            image.save(filename) # 画像をファイルに連番で保存する

        with open(filename, 'rb') as f:
            picture = discord.File(f)
            # 画像をDiscordに送信する
            await message.channel.send(file=picture)


# Discord Botを起動する
client.run(DISCORD_TOKEN)
