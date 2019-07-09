# Purpose:Helper Function Library for the Elec400s Decoder project.
# Creator: Alex V & Alex H
# Date: 2019/07/09



# Purpose: Converts a standard stream of bits to NRZI
# Input: Standard Bit Array Stream
# Output: bitarray representing '0's as change and 1's as unchanged.
def NRZ2NRZI(NRZ):
    NRZI = NRZ.copy()
    current = True
    for n in range(0,len(NRZ)):
        if NRZ[n]:
            NRZI[n] = current
        else:
            NRZI[n] = not(current)
        current = NRZI[n]
    return NRZI

