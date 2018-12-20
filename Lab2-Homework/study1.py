from youtube_dl import YoutubeDL

# Download single video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=IpniN1Wq68Y"])

# Download multiple video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=KdrbBJNFwGw", "https://www.youtube.com/watch?v=fjtjs8ABkmw"])

# Download audio
options = {
    "format": "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=BuZl2sOIL28"])

# Search and download the first video
options = {
    "default_search": "ytsearch",
    "max_downloads": 1
}
dl = YoutubeDL(options)
dl.download(["cho tôi lang thang ngọt"])

# Search and download the first audio
options = {
    "default_search": "ytsearch",
    "max_downloads": 1,
    "format": "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["loving you kimmese"])