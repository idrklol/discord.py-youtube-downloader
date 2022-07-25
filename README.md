# discord.py youtube downloader <img src="https://c.tenor.com/NA1Zs9FrCWYAAAAi/chika.gif" width="30"/>

Discord bot written in python that downloads youtube videos, either as mp3 or mp4.

<img src="https://cdn.discordapp.com/attachments/1001152399047659682/1001152438167949472/unknown.png" alt="Example screenshot" title="hi!!! this is an example for what the bot does :DDD you can do --mp4 or leave empty for an mp4 output" width="400">

## :bangbang: Warnings
* The bot can't upload videos larger than the server's upload limit (based on boosts)
* The bot will not compress videos to fit the maximum size
* The output will not be the best quality for accessibility

## :gear: Setting up
Make sure you have the latest version of Python installed
* Open the cmd on the folder where requir.txt is located
* Run `pip install -r requir.txt`
* Scroll at the end of the main.py file and put your token
```py
Example
client.run('ODQ2NzQ5NjM1NjA1NDk5OTM0.GhfcgO.uMLYSPpZoUvzxa5ivYRc4htr09yniLx22Ymp3Q')
```
* Lastly, run `python main.py`
## ✅ Usage
* Run .yt <link> [file type (--mp3/mp4)
* Wait for it to download
# 
If you want your videos to not be deleted from your disk after being sent set `delete_after_compl` to `False`

Credit to https://github.com/razordx/disctube because i used it as base
