from PIL import Image, ImageDraw

def updatePicture(state, mod=5):
    print("State:\t" + str(state))
    im = Image.open("arena.png")

    w, h = im.size
    xs = [w*0.25, w*0.25, w*0.75, w*0.75]
    ys = [h*0.1, h*0.5, h*0.1, h*0.5]

    fw = w*0.25
    fh = (h*0.4) / mod

    yBuff = fh*0.1

    draw = ImageDraw.Draw(im)

    for i in range(0, 4):
        for j in range(0, mod):
            if state[i] > j:
                bbox = (xs[i] - fw/2, ys[i] + fh*(j-0.5) + yBuff,
                    xs[i] + fw/2, ys[i] + fh*(j + 0.5) - yBuff)
                draw.ellipse(bbox, fill=(50,50,50,200))
    del draw

    im.save("arenaCurrent.png")
