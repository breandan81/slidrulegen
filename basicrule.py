import drawsvg as draw
import numpy as np
import math


strokeWidth = 0.1
ruleLen = 1000
origin = (-100, -10)
d = draw.Drawing(1200, 500, origin=origin)
textLayer = draw.Drawing(1200, 500, origin=origin)
cutLayer = draw.Drawing(1200, 500, origin=origin)
tickLayer = draw.Drawing(1200, 500, origin=origin)
engraveLayer = draw.Drawing(1200, 500, origin=origin)

scaleLength = 1000
shortTick = 3
medTick = 5
longTick = 7
#d.append(draw.Line(30, 20, 0, 10, stroke='red', stroke_width=1, fill='none'))

d.set_pixel_scale(1)  # Set number of pixels per geometry unit
textLayer.set_pixel_scale(1)  # Set number of pixels per geometry unit
cutLayer.set_pixel_scale(1)  # Set number of pixels per geometry unit
tickLayer.set_pixel_scale(1)  # Set number of pixels per geometry unit
#d.set_render_size(400, 200)  # Alternative to set_pixel_scale



def drawTick(xOffset, yOffset, length, label, flip):
    print("DrawTick")
    if flip == False:
        d.append(draw.Line(xOffset, yOffset, xOffset, yOffset+length, stroke='black', stroke_width=strokeWidth, fill='none'))
        tickLayer.append(draw.Line(xOffset, yOffset, xOffset, yOffset+length, stroke='black', stroke_width=strokeWidth, fill='none'))
        d.append(draw.Text(label, 8, xOffset, yOffset+2+length+8, fill='black'))
        textLayer.append(draw.Text(label, 8, xOffset, yOffset+2+length+8, fill='black'))
    else:
        d.append(draw.Line(xOffset, yOffset, xOffset, yOffset-length, stroke='black', stroke_width=strokeWidth, fill='none'))
        d.append(draw.Text(label, 8, xOffset, yOffset - (2 +length), fill='black'))
        tickLayer.append(draw.Line(xOffset, yOffset, xOffset, yOffset-length, stroke='black', stroke_width=strokeWidth, fill='none'))
        textLayer.append(draw.Text(label, 8, xOffset, yOffset - (2 +length), fill='black'))

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

def drawCScale(yOffset, flip): 
    drawLogScale(50,10,1,2,yOffset,flip,1,False)
    drawLogScale(60,6,2,5,yOffset,flip,1,False)
    drawLogScale(50,10,5,10,yOffset,flip,1,True)

def drawAScale(yOffset, flip):
    drawLogScale(20,10,1,2,yOffset,flip,.5,False)
    drawLogScale(30,6,2,5,yOffset,flip,.5,False)
    drawLogScale(25,10,5,10,yOffset,flip,.5,False)
    drawLogScale(20,10,10,20,yOffset,flip,.5,False)
    drawLogScale(30,6,20,50,yOffset,flip,.5,False)
    drawLogScale(25,10,50,100,yOffset,flip,.5,True)


def drawKScale(yOffset, flip):
    drawLogScale(20,5,1,2,yOffset,flip,1/3,False)
    drawLogScale(30,6,2,5,yOffset,flip,1/3,False)
    drawLogScale(25,5,5,10,yOffset,flip,1/3,False)
    drawLogScale(20,5,10,20,yOffset,flip,1/3,False)
    drawLogScale(30,6,20,50,yOffset,flip,1/3,False)
    drawLogScale(25,5,50,100,yOffset,flip,1/3,False)
    drawLogScale(20,5,100,200,yOffset,flip,1/3,False)
    drawLogScale(30,6,200,500,yOffset,flip,1/3,False)
    drawLogScale(25,5,500,1000,yOffset,flip,1/3,True)


def upperRule():
    extraLen = 70;
    d.append(draw.Rectangle(-extraLen, 0, scaleLength+extraLen*2,60, stroke='black',stroke_width=strokeWidth, fill='none'))
    cutLayer.append(draw.Rectangle(-extraLen, 0, scaleLength+extraLen*2,60, stroke='black',stroke_width=strokeWidth, fill='none'))
    drawAScale(60, True)
    drawLScale(200, 35, True)

def lowerRule():
    slideWidth = 60
    topWidth = 60
    extraLen = 70
    d.append(draw.Rectangle(-extraLen, topWidth+slideWidth, scaleLength+extraLen*2,60,stroke_width=strokeWidth, stroke='black', fill='none'))
    cutLayer.append(draw.Rectangle(-extraLen, topWidth+slideWidth, scaleLength+extraLen*2,60,stroke_width=strokeWidth, stroke='black', fill='none'))
    drawCScale(topWidth+slideWidth, False)
    drawKScale(25+topWidth+slideWidth, False)

def outerRule():
    upperRule()
    lowerRule()

def slide():
    extraLen = 70
    d.append(draw.Rectangle(-extraLen, 0, scaleLength+extraLen*2,60, stroke='black',stroke_width=strokeWidth, fill='none'))
    cutLayer.append(draw.Rectangle(-extraLen, 0, scaleLength+extraLen*2,60, stroke='black',stroke_width=strokeWidth, fill='none'))
    drawAScale(0, False)
    drawCScale(60, True)

outerRule()


d.save_svg('outer.svg')
d.save_png('outer.png')
cutLayer.save_svg('outercut.svg')
tickLayer.save_svg('outerticks.svg')
textLayer.save_svg('outertext.svg')

d = draw.Drawing(1200, 500, origin=origin)
tickLayer = draw.Drawing(1200, 500, origin=origin)
textLayer = draw.Drawing(1200, 500, origin=origin)
cutLayer = draw.Drawing(1200, 500, origin=origin)
slide()
d.save_svg("slide.svg")
d.save_png("slide.png")
cutLayer.save_svg('cut.svg')
tickLayer.save_svg('ticks.svg')
textLayer.save_svg('text.svg')
