import drawsvg as draw
import numpy as np
import math

d = draw.Drawing(1100, 100, origin=(-50,-50))
origin = (50, 50)
scaleLength = 1000
shortTick = 3
medTick = 5
longTick = 7
#d.append(draw.Line(30, 20, 0, 10, stroke='red', stroke_width=1, fill='none'))

d.set_pixel_scale(1)  # Set number of pixels per geometry unit
#d.set_render_size(400, 200)  # Alternative to set_pixel_scale



#def drawLScale(yOffset):
#    print("Drawing L scale")
##    yOffset = 0;
#    for n in range(0, 201):
#        if n % 20 == 0:
#            tickLen = longTick
#            d.append(draw.Text(str(int(n/20)), 8, origin[0]+(n*scaleLength/200), origin[1] + yOffset+2+longTick+8, fill='black'))
#        elif n%2 == 0:
#            tickLen = medTick
#        else:
#            tickLen = shortTick
#        d.append(draw.Line(origin[0]+(n*scaleLength/200), origin[1] + yOffset, origin[0]+(n*scaleLength/200), origin[1] + yOffset+tickLen, stroke='black', stroke_width=1, fill='none'))

def drawTick(xOffset, yOffset, length, label, flip):
    print("DrawTick")
    if flip == False:
        d.append(draw.Line(xOffset, yOffset, xOffset, yOffset+length, stroke='black', stroke_width=1, fill='none'))
        d.append(draw.Text(label, 8, xOffset, yOffset+2+length+8, stroke_width=1, fill='none'))
    else:
        d.append(draw.Line(xOffset, yOffset, xOffset, yOffset-length, stroke='black', stroke_width=1, fill='none'))
        d.append(draw.Text(label, 8, xOffset, yOffset - (2 +length),stroke_width=1 , fill='none'))

def drawLScale(divs, yOffset, flip):
    for n in range(0,divs+1):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.1f}".format((1/divs)*n)
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        drawTick((scaleLength/divs)*n, yOffset, tickLen, label, flip)

def drawCScale(divs, divs2, yOffset, flip):
    #divs from 1 to 2
    for n in range(0,divs):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.1f}".format(1+((1/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 1+(n*(1/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal, yOffset, tickLen, label, flip)
    #divs from 2 to 5
    for n in range(0,divs2):
        label = ""
        if n % (divs2/6) == 0:
            tickLen=longTick
            label = "{:.1f}".format(2+((3/divs2)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 2+(n*(3/divs2))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal, yOffset, tickLen, label, flip)
    for n in range(0,divs+1):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.1f}".format(5+((5/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 5+(n*(5/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal, yOffset, tickLen, label, flip)
    

#drawLScale(200, 0, True)
drawCScale(100, 120, 0, False)
d.save_svg('example.svg')
d.save_png('example.png')
