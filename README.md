# discord.py youtube downloader
Discord bot written in python that downloads youtube videos, either as mp3 or mp4.
## Warnings
* The bot can't upload videos larger than the server's upload limit (based on boosts)
* The bot will not compress videos to fit the maximum size
* The output will not be the best quality for accessibility

## Setting up
Make sure you have the latest version of Python installed
* Open the cmd on the folder where requir.txt is located
* Run `pip install -r requir.txt`
* Scroll at the end of the main.py file and put your token
* Lastly, run `python main.py`
## Usage
* Run .yt <link> [file type (--mp3/mp4)
* Wait for it to download
# 
If you want your videos to not be deleted from your disk after being sent set `delete_after_compl` to `False`

Credit to https://github.com/razordx/disctube because i used it as base
