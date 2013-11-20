
CyberconStl = "/Cybercon - STL/210 N.Tucker/Floor7/"

row = "/Row "
rack = "/Rack "

x = 'S1J7'

om = ''

newval = om

def location(newval):
    if len(newval):
        if newval[0] == 'S':
            newval = ( CyberconStl + newval[0:2] + row + newval[2] + rack 
                     + newval[3] )
                     

            # run prepId() on all parts between slashes:
#        newval = "/".join(map(self.prepId, newval.split("/")))
            
            # likely, an initial "/" was not in the SNMP location. Check. Add 
            #   if needed.
#        if newval[0] != "/":
#           newval = "/" + newval
            
            # update our objectMap with our tweaked value:
    om = newval

#        log.info('Location: %s', om.setSNMPLocation)

    return om

print location(x)