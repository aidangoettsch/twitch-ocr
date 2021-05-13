import streamlink
import av
import numpy as np
import pytesseract

streamer = "Discord"


def process_image(im):
    print(pytesseract.image_to_string(im))


streams = streamlink.streams('https://www.twitch.tv/%s' % streamer)
if streams:
    stream = streams['best']

    container = av.open(stream.url)
    # video_stream = next(s for s in container.streams if s.type == b'video')
    video_stream = list(s for s in container.streams)[1]

    ts = 0
    for packet in container.demux(video_stream):
        for frame in packet.decode():
            if ts % 20 == 0:
                image = frame.to_image()
                process_image(image)
            ts += 1
