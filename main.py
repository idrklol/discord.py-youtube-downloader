import discord
import pytube
import time
import os
import io
import binascii

from io import BytesIO
from discord.ext import commands
from pytube import YouTube

delete_after_compl = True
token = 'token here (in quotes)'

mp4path = 'cache/mp4dl'
mp3path = 'cache/mp3dl'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(
		type=discord.ActivityType.watching, name="the void"))
	print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
	await client.process_commands(message)


@client.command()
@commands.is_owner()
async def shutdown(ctx):
	await ctx.message.add_reaction('⭕')
	print("-"*10)
	print(f"SHUT DOwN BY {ctx.author.name}")
	await client.change_presence(status=discord.Status.offline)
	await ctx.bot.logout()


@client.command()
async def ping(ctx):
	before = time.monotonic()
	message = await ctx.reply("Pinging...")
	ping = (time.monotonic() - before) * 1000
	await message.edit(content=f"Pong! `{int(ping)} ms`")


@client.command(aliases=["yt", "ytdownload", "youtube"])
async def ytdl(ctx, link, filetype=None):

	if 14 >= ctx.guild.premium_subscription_count >= 7:
		maxUpload = 50000000
		maxUploadMB = 50
	elif ctx.guild.premium_subscription_count >= 14:
		maxUpload = 100000000
		maxUploadMB = 100
	else:
		maxUpload = 8000000
		maxUploadMB = 8

	async with ctx.typing():
		if filetype == None:
			filetype = '--mp4'

		embed1 = discord.Embed(title=f'Searching {link}')
		fmsg = await ctx.send(embed=embed1)

		url = pytube.YouTube(link)

		fname = str(
			f'download_{str(ctx.author)}_{binascii.b2a_hex(os.urandom(5))}')
		if filetype == '--mp4':
			video = url.streams.filter(
				progressive=True, file_extension='mp4').first()
			embed2 = discord.Embed(
				title='Video found, downloading...')
			before = time.monotonic()
			await fmsg.edit(embed=embed2)
			video.download(mp4path, filename=fname + '.mp4')
			time.sleep(10)
			fsize = os.path.getsize(f"{mp4path}\{fname}.mp4")
			if fsize >= maxUpload:
				embed = discord.Embed(
					title='Where\'s my video?', description=f"Your video is larger than `{maxUploadMB}mb`.\nReason behind is the [upload limit](https://github.com/discord/discord-api-docs/issues/2037).")
				await fmsg.edit(embed=embed)
				if delete_after_compl == True:
					await os.remove(f'{mp4path}\{fname}.mp4')
				await fmsg.delete()
				return
			after = (time.monotonic() - before)
			await ctx.reply(f'Downloaded in {round(after, 2)}s', file=discord.File(f'{mp4path}\{fname}.mp4'))
			if delete_after_compl == True:
				await os.remove(f'{mp4path}\{fname}.mp4')
			await fmsg.delete()

		elif filetype == '--mp3':
			video = url.streams.filter(only_audio=True).first()
			embed2 = discord.Embed(
				title='Audio found, downloading...')
			before = time.monotonic()
			await fmsg.edit(embed=embed2)

			video.download(mp3path, filename=fname + '.mp3')
			fsize = os.path.getsize(f"{mp3path}\{fname}.mp3")
			if fsize >= maxUpload:
				embed = discord.Embed(
					title='Where\'s my audio?', description=f"Your audio is larger than `{maxUploadMB}mb` (somehow).\nReason behind is the [upload limit](https://github.com/discord/discord-api-docs/issues/2037).")
				await ctx.reply(embed=embed)
				if delete_after_compl == True:
					await os.remove(f'{mp3path}\{fname}.mp3')
				await fmsg.delete()
				return
			after = (time.monotonic() - before)
			await ctx.reply(f'Downloaded in {round(after, 2)}s', file=discord.File(f'{mp3path}\{fname}.mp3'))
			if delete_after_compl == True:
				await os.remove(f'{mp3path}\{fname}.mp3')
			await fmsg.delete()
		else:
			await ctx.send(f"`{filetype}` is not a supported filetype")
			await fmsg.delete()

client.run(token)
