# OrcaSatDecoder AX.25 
## OrcaSat Ground Station telemetry Decoder for Elec400s Course in UBC
### GroundStation and Signal Specs:

- Frequency: 433Mhz

- Modulation: GFSK 

- Bandwidth: 15kHz

- Callsign: TBD

- Link Layer: AX.25

- Baud Rate: 9800 bit/s

- TLE: TBD

### AX.25 Info

AX.25 does not encode NRZ 1's and 0's, instead is issues NRZI(non return to zero inverter).
NRZI encodes a 0 bit as a change from mark to space and a 1 is encoded as no change. 
To decode we will have to convert a NRZI signal to a bit sequence.

- Bit-Order: Leas-significant-bit first.

- Flags: starts and end each package. 0x7E or: 01111110. It is the only place in the packet in which 6 consecutive 1s appear.

- FCS: for error correction/detection they are the checksum to determine the integrity of the packet.

#### Frame Structure:
Flag|Dest. Addr| Src. Addr.| Digipeter Addr.| Control Field| ID| Information Field| FCS| Flag|
1   |   7      | 7         | 56             | 1            |  1| 256              | 2  | 1   |


#### Task List:
- [x] AX.25 stream - BistreamGenerator.py
- [ ] Helper Functions - helperLib.py
- [ ] Decode Sample - decoderMain.py
- [ ] OOT implementation for GNURadio
- [ ] GUI and command creation
- [ ] Automation 
- [ ] USRP Connection
- [ ] CubeSat Live Test.


#### Sources:
- https://www.tapr.org/pub_ax25.html
- http://n1vg.net/packet/

