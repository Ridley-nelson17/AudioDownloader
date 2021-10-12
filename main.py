import sys, youtube_dl, os

if __name__ == "__main__":
	master = {}
	with open(str(sys.argv[1:][0]), 'r') as pointer:
		counter = 0
		for line in pointer:
			if 'http' in line:
				mock_instance = open("pointer.txt", "r").readlines()
				master[line.split('\n')[0]] = [mock_instance[counter + 1].split('\n')[0], mock_instance[counter + 2].split('\n')[0]]
			counter+=1
		pointer.close()

	for url in master:
		song = f'out/{master[url][0]} {master[url][1]}.mp3'
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '320',
			}],
			'outtmpl': song,
			'hls_prefer_native': True,
			'noplaylist': True,
		}

		youtube_dl.YoutubeDL(ydl_opts).download([url], )