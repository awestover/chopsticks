from PIL import Image, ImageDraw

def updatePicture(state, mod=5):
    im = Image.open("arena.png")

    w, h = im.size
    xs = [w*0.25, w*0.75]

    ys = h*0.1

    fw = w*0.1
    fh = (h*0.8) / mod

    for i in range(0, 2):
        for j in range(0, mod):
            bbox =  (xs[i], ys + fh*j, fw, fh)
            draw = ImageDraw.Draw(im)
            draw.ellipse(bbox, fill=128)
            del draw

    im.save("arenaCurrent.png")
