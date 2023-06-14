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

def float2str(me):
    if(me < 10):
        return "{:.1f}".format(me)
    else:
        return "{:.0f}".format(me)

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
            label = "{:.2g}".format(1+((1/divs)*n))
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
            label = "{:.2g}".format(2+((3/divs2)*n))
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
            label = "{:.2g}".format(5+((5/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 5+(n*(5/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal, yOffset, tickLen, label, flip)

def drawLogScale(divs, labelCount, start, end, yOffset, flip, scale, addOne):
    if addOne == True:
        divsAdj = divs+1
    else:
        divsAdj=divs
    for n in range(0,divsAdj):
        label = ""
        linVal = start+(n*((end-start)/divs))
        if n % (divs/labelCount) == 0:
            tickLen=longTick
            label = float2str(linVal)
        else:
            tickLen=shortTick
        logVal = math.log10(linVal)*scale;
        drawTick(scaleLength*logVal, yOffset, tickLen, label, flip)

def drawAScale(divs, divs2, yOffset, flip):
    #divs from 1 to 2
    for n in range(0,divs):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.1g}".format(1+((1/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 1+(n*(1/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)
    #divs from 2 to 5
    for n in range(0,divs2):
        label = ""
        if n % (divs2/6) == 0:
            tickLen=longTick
            label = "{:.1g}".format(2+((3/divs2)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 2+(n*(3/divs2))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)
    for n in range(0,divs):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.1g}".format(5+((5/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 5+(n*(5/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)
    #divs from 10 to 20
    for n in range(0,divs):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.0f}".format(10+((10/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 10+(n*(10/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)
    #divs from 20 to 50
    for n in range(0,divs2):
        label = ""
        if n % (divs2/6) == 0:
            tickLen=longTick
            label = "{:.0f}".format(20+((30/divs2)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 20+(n*(30/divs2))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)
    for n in range(0,divs+1):
        label = ""
        if n % (divs/10) == 0:
            tickLen=longTick
            label = "{:.0f}".format(50+((50/divs)*n))
        elif n%2 == 0:
            tickLen=medTick
        else:
            tickLen=shortTick
        linVal = 50+(n*(50/divs))
        logVal = math.log10(linVal);
        drawTick(scaleLength*logVal/2, yOffset, tickLen, label, flip)


#drawLScale(200, 0, True)
drawCScale(50, 60, 0, False)
#drawAScale(20, 30, 0, False)
drawLogScale(50,10,1,2,0,True,1,True)
d.save_svg('example.svg')
d.save_png('example.png')
