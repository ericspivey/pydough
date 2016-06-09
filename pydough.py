# -*- coding: utf-8 -*-

"""
Created on Tue Jun  7 10:56:39 2016

@author: Eric
"""
import matplotlib.pyplot as plt
plt.rcdefaults()

import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#from matplotlib.collections import PatchCollection

def pydough(indat, **kwargs):
    """ pydough is a funtion that returns a doughnut plot of data, where each line of an array or list is a searate ring of the plot, and each column represents a plot category
    Examples:
        pydough([[50,20,10],[40,30,15]],colors=['r','g','b'],catlabels=['First','Second','Third'])
        pydough([50,20,10],catlabels=['First','Second','Third'],pie='y')
    **kwargs:
    colors = <list of colors, one for each category/column> (default viridis)
    pie = 'n' (default doughnut plot) or 'y' (pie chart)
    catlabels = <list of category labels> (default none)
    """
    indat = np.asarray(indat) # indat to array if not already
    if indat.size==indat.shape[0]:
        x = 1
        y = indat.shape[0];
    else:
        x,y = indat.shape # gets dimensions of indat
    
    # Default values
    colorset = plt.cm.viridis(np.linspace(0, 1, y))
    pies = 'n' # 'n' is doughnut plot, 'y' is a pie chart of first row
    thk = 0.95 # thickness of ring in doughnut
    numrng = x # of rings in plot
    legsp = 0 # additional space for legend
    
    if 'colors' in kwargs:
        col = kwargs['colors']
        for cl in range(0,len(col)):
            colorset[cl] = mcolors.ColorConverter().to_rgba(col[cl])
        
    if 'pie'in kwargs:
        pies = kwargs['pie']
    if pies=='y':
        thk = 2 # use full thickness of wedge
        numrng = 1 # use only first row of data
    
    ax1 = plt.axes() # implicitly creates figure object with axes and single subplot
    for r in range(0,numrng): # rings of doughnut
        if numrng==1:
            rvals = indat
        else:
            rvals = indat[r] # values for current ring
        denom = sum(rvals) # total values for current ring
        ratval = rvals/denom # ratio of each wedge value for a ring
        degval = ratval*360 # degree values
        degsum = 90
        for w in range(0,len(rvals)): # wedges of doughnut
            #print(r+2,degsum,degsum+degval[w],r+1)
            wedge = mpatches.Wedge((0,0), r+2, degsum, degsum+degval[w], width=thk,facecolor=colorset[w],edgecolor='black')
            if 'catlabels' in kwargs:
                if r == (numrng-1):
                    catext = kwargs['catlabels']
                    if w <= len(catext)-1:
                        wedge.set_label(catext[w])
                    else:
                        wedge.set_label('-')
                    legsp = 1
            ax1.add_patch(wedge)
            degsum += degval[w]
    
    genlim = (r+2)*1.1


    plt.axis('equal')
    plt.axis('on')
    plt.axis([-genlim,genlim+legsp,-genlim,genlim])
    plt.legend()
    plt.show()
