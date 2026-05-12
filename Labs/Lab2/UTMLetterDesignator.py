## Create a function that provides the UTM letter than corresponds with a respective latitude
## input: latitude value
## output: UTM letter

def UTMLetter(Lat):
    L=['C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W']; ## list of UTM letters 
    R = [range(-80,-72), range(-72,-64),range(-64,-56),range(-56,-48),range(-48,-40)\
        ,range(-40,-32),range(-32,-24),range(-24,-16),range(-16,-8),range(-8,0),\
        range(0,8),range(8,16),range(16,24),range(24,32),range(32,40),range(40,48),\
        range(48,56),range(56,64),range(64,72),range(72,84)] ## list of corresponding latitude ranges
    LR = dict(zip(L,R)) ## form a dictionary that matches UTM letters with their respective ranges
    ## loop through the dictionary (LR) to determines which key (letter) represents the latitude value
    ## (in range), else outputs 'Z'
    for letter, lat_range in LR.items():
        if Lat in lat_range:
            return letter
    return 'Z' 

#Example utilization: 
#a=UTMLetter(-57)
#print(a)
