from nft.nft import NFT
from gui_loader.guihandler import Window
from threading import Thread


# disp1=NFT()
# disp1.display('img/image2.jpg','img/frame0.jpg')

if __name__ == "__main__":
    window=Window()
    t = Thread(name='non-daemon', target=window.mainloop())
    t.start()
    t.join()
    

