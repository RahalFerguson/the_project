import opc
import time
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

          #H

leds[1] = (131, 182, 146)
leds[61] = (131, 182, 146)
leds[121] = (131, 182, 146)
leds[181] = (131, 182, 146)
leds[241] = (131, 182, 146)
leds[301] = (131, 182, 146)

leds[0] = (131, 182, 146)
leds[60] = (131, 182, 146)
leds[120] = (131, 182, 146)
leds[180] = (131, 182, 146)
leds[240] = (131, 182, 146)
leds[300] = (131, 182, 146)

leds[123] = (131, 182, 146)
leds[124] = (131, 182, 146)
leds[184] = (131, 182, 146)
leds[183] = (131, 182, 146)

leds[182] = (131, 182, 146)
leds[185] = (131, 182, 146)
leds[122] = (131, 182, 146)
leds[125] = (131, 182, 146)

leds[6] = (131, 182, 146)
leds[66] = (131, 182, 146)
leds[126] = (131, 182, 146)
leds[186] = (131, 182, 146)
leds[246] = (131, 182, 146)
leds[306] = (131, 182, 146)

leds[5] = (131, 182, 146)
leds[65] = (131, 182, 146)
leds[125] = (131, 182, 146)
leds[185] = (131, 182, 146)
leds[245] = (131, 182, 146)
leds[305] = (131, 182, 146)

         #E
leds[8] = (249, 173, 160)
leds[68] = (249, 173, 160)
leds[128] = (249, 173, 160)
leds[188] = (249, 173, 160)
leds[248] = (249, 173, 160)
leds[308] = (249, 173, 160)

leds[9] = (249, 173, 160)
leds[69] = (249, 173, 160)
leds[129] = (249, 173, 160)
leds[189] = (249, 173, 160)
leds[249] = (249, 173, 160)
leds[309] = (249, 173, 160)

leds[10] = (249, 173, 160)
leds[11] = (249, 173, 160)
leds[70] = (249, 173, 160)
leds[130] = (249, 173, 160)
leds[131] = (249, 173, 160)
leds[190] = (249, 173, 160)
leds[191] = (249, 173, 160)
leds[12] = (249, 173, 160)
leds[132] = (249, 173, 160)
leds[192] = (249, 173, 160)
leds[250] = (249, 173, 160)
leds[310] = (249, 173, 160)
leds[311] = (249, 173, 160)
leds[312] = (249, 173, 160)

           #l
leds[14] = (249, 98, 125)
leds[74] = (249, 98, 125)
leds[134] = (249, 98, 125)
leds[194] = (249, 98, 125)
leds[254] = (249, 98, 125)
leds[314] = (249, 98, 125)

leds[15] = (249, 98, 125)
leds[75] = (249, 98, 125)
leds[135] = (249, 98, 125)
leds[195] = (249, 98, 125)
leds[255] = (249, 98, 125)
leds[315] = (249, 98, 125)

leds[256] = (249, 98, 125)
leds[316] = (249, 98, 125)


leds[257] = (249, 98, 125)
leds[317] = (249, 98, 125)
leds[258] = (249, 98, 125)
leds[318] = (249, 98, 125)

          #l
leds[20] = (249, 98, 125)
leds[80] = (249, 98, 125)
leds[140] = (249, 98, 125)
leds[200] = (249, 98, 125)
leds[260] = (249, 98, 125)
leds[320] = (249, 98, 125)

leds[21] = (249, 98, 125)
leds[81] = (249, 98, 125)
leds[141] = (249, 98, 125)
leds[201] = (249, 98, 125)
leds[261] = (249, 98, 125)
leds[321] = (249, 98, 125)

leds[262] = (249, 98, 125)
leds[322] = (249, 98, 125)


leds[263] = (249, 98, 125)
leds[323] = (249, 98, 125)
leds[264] = (249, 98, 125)
leds[324] = (249, 98, 125)

          #o
leds[26] = (198, 91, 124)
leds[86] = (198, 91, 124)
leds[146] = (198, 91, 124)
leds[206] = (198, 91, 124)
leds[266] = (198, 91, 124)
leds[326] = (198, 91, 124)

leds[27] = (198, 91, 124)
leds[87] = (198, 91, 124)
leds[147] = (198, 91, 124)
leds[207] = (198, 91, 124)
leds[267] = (198, 91, 124)
leds[327] = (198, 91, 124)

leds[28] = (198, 91, 124)
leds[88] = (198, 91, 124)
leds[268] = (198, 91, 124)
leds[328] = (198, 91, 124)

leds[29] = (198, 91, 124)
leds[89] = (198, 91, 124)
leds[269] = (198, 91, 124)
leds[329] = (198, 91, 124)

leds[30] = (198, 91, 124)
leds[90] = (198, 91, 124)
leds[150] = (198, 91, 124)
leds[210] = (198, 91, 124)
leds[270] = (198, 91, 124)
leds[330] = (198, 91, 124)

leds[31] = (198, 91, 124)
leds[91] = (198, 91, 124)
leds[151] = (198, 91, 124)
leds[211] = (198, 91, 124)
leds[271] = (198, 91, 124)
leds[331] = (198, 91, 124)

              #Smile face
    #Eye
leds[94] = (91, 55, 88)
leds[154] = (91, 55, 88)

leds[95] = (91, 55, 88)
leds[155] = (91, 55, 88)

leds[99] = (91, 55, 88)
leds[159] = (91, 55, 88)

leds[100] = (91, 55, 88)
leds[160] = (91, 55, 88)

              #smile
leds[275] = (91, 55, 88)
leds[276] = (91, 55, 88)
leds[277] = (91, 55, 88)
leds[278] = (91, 55, 88)

leds[279] = (91, 55, 88)

client.put_pixels(leds)
client.put_pixels(leds)

time.sleep(1)

led = 0

while led < 60:  # scroll all rows at the same time
    for rows in range(6):
        leds[59 - led + rows * 60] = (0, 0, 0)

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1