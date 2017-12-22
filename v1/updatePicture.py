from PIL import Image, ImageDraw

def updatePicture(state, mod=5):
    print("State:\t" + str(state))
    im = Image.open("arena.png")

    w, h = im.size
    xs = [w*0.25, w*0.75]

    ys = h*0.1

    fw = w*0.1
    fh = (h*0.8) / mod

    draw = ImageDraw.Draw(im)
    for i in range(0, 2):
        for j in range(0, mod):
            if state[2*i + 0] > j and state[2*i + 1] > j:
                bbox = (xs[i], ys + fh*j, fw, fh)
                print(bbox)
                draw.ellipse(bbox, fill=128)
    del draw

    im.save("arenaCurrent.png")


updatePicture([1,1,1,1])
