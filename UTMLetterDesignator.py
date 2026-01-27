def UTMLetterDesignator(lat):
    """This routine determines the correct UTM letter designator for the given latitude
    returns 'Z' if latitude is outside the UTM limits of 84N to 80S
    Originally written by Chuck Gantz- chuck.gantz@globalstar.com
    Refactored by Ed Blum- eblum2@alaska.edu
    """
    if lat > 84 or lat < -80:
        return 'Z' # if the Latitude is outside the UTM limits

    zones = {
        10: 'X', # this will go 80 to 87.9 when I have the floor division set up
        9: 'W', 
        8: 'V', 
        7: 'U', 
        6: 'T', 
        5: 'S', 
        4: 'R', 
        3: 'Q', 
        2: 'P', 
        1: 'N', 
        0: 'M', 
        -1: 'L', 
        -2: 'K', 
        -3: 'J', 
        -4: 'H', 
        -5: 'G', 
        -6: 'F', 
        -7: 'E', 
        -8: 'D', 
        -9: 'C', 
    }
   
    lat_index = (lat // 8) + 1 # The +1 is necessary to make the floor division work and prevent off-by-one errors
    
    return zones[lat_index]