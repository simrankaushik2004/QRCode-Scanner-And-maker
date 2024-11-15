import qrcode as qr


img=qr.make("https://en.wikipedia.org/wiki/High_fidelity")
aa=qr.make("https://www.geeksforgeeks.org/")
img.save("LETS LEARN CODING.png")
aa.save("GFG.png")

