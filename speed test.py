#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn
import speedtest
import time 

def speedtest1():
    start_time = time.time()
    st = speedtest.Speedtest()
    ds = st.download() / 10**6
    us = st.upload() / 10**6
    ping = st.results.ping
    end_time = time.time()
    sett = end_time - start_time

    print(f"download speed: {ds: .2f} Mbps")
    print(f"upload speed: {us: .2f} Mbps")
    print(f"ping: {ping: .2f} ms")
    print(f"test time: {sett: .2f} s")

speedtest1()
#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn