import matplotlib.pyplot as plt

# Define the arrays
none = [378, 348, 272, 252, 222, 219, 206, 208, 200, 203, 197, 198, 194, 193,
        187, 192, 190, 190, 185, 185, 183, 180, 177, 175, 172, 170, 169, 169,
        180, 186, 191, 193, 190, 213, 225, 247, 269, 308, 351, 415, 499, 600,
        745, 884, 953, 988, 1006, 1014, 949, 881, 798, 740, 685, 639, 608, 575,
        546, 525, 506, 491, 482, 470, 454, 446, 443, 435, 422, 417, 415, 412,
        401, 395, 391, 394, 386, 378, 369, 368, 367, 369, 358, 349, 338, 335,
        334, 333, 326, 320, 312, 311, 310, 315, 328, 331, 338, 343, 349, 353,
        361, 362, 374, 380, 386, 381, 381, 376, 379, 379, 382, 385, 391, 398,
        406, 409, 410, 407, 408, 407, 412, 416, 424, 427, 441, 453, 468, 481,
        501, 516, 528, 525, 529, 544, 554, 571, 581, 574, 573, 567, 558, 554,
        543, 535, 523, 511, 498, 489, 477, 465, 443, 430, 413, 403, 394, 403,
        391, 385, 377, 373, 366, 363, 360, 362, 360, 360, 356, 354, 349, 347,
        343, 342, 337, 332, 325, 318, 312, 306, 303, 301, 300, 301, 304, 306,
        310, 315, 320, 328, 331, 335, 342, 346, 352, 359, 367, 370, 376, 377,
        381, 383, 386, 388, 391]

one_finger = [392, 354, 272, 249, 215, 211, 195, 197, 187, 190, 183, 183, 178, 179, 
              173, 179, 178, 178, 174, 175, 172, 178, 168, 167, 164, 174, 186, 173, 
              182, 177, 174, 165, 159, 184, 182, 177, 171, 179, 189, 206, 200, 215, 
              213, 228, 231, 240, 246, 259, 270, 284, 296, 311, 325, 344, 361, 380, 
              397, 416, 432, 453, 472, 490, 504, 524, 534, 541, 546, 554, 556, 553, 
              547, 544, 545, 542, 533, 523, 516, 515, 516, 506, 498, 488, 482, 479, 
              479, 478, 469, 462, 453, 449, 445, 448, 449, 442, 435, 429, 422, 420, 
              418, 418, 419, 422, 419, 412, 406, 400, 396, 394, 392, 393, 394, 399, 
              400, 399, 392, 387, 382, 378, 375, 374, 374, 374, 375, 378, 382, 385, 
              387, 385, 377, 373, 371, 368, 366, 366, 365, 366, 368, 370, 373, 376, 
              380, 384, 387, 390, 390, 388, 381, 376, 375, 375, 372, 371, 372, 372, 
              373, 374, 376, 377, 379, 382, 385, 390, 395, 398, 401, 403, 405, 408, 
              410, 407, 398, 391, 388, 387, 386, 384, 383, 383, 385, 387, 388, 389, 
              390, 390, 392, 393, 395, 395, 397, 400, 402, 408, 411, 412, 413, 414, 
              415, 416, 417, 418]

two_fingers = [383, 350, 270, 247, 212, 208, 193, 196, 187, 189, 182, 184, 178, 179, 
               176, 181, 174, 174, 168, 170, 167, 172, 166, 165, 165, 171, 164, 162, 
               169, 173, 169, 183, 166, 176, 179, 173, 166, 174, 176, 177, 178, 194, 
               193, 213, 211, 214, 215, 226, 235, 241, 251, 259, 266, 275, 284, 296, 
               307, 319, 328, 340, 353, 366, 376, 392, 403, 414, 424, 440, 449, 460, 
               466, 476, 486, 491, 493, 493, 495, 499, 503, 499, 495, 491, 489, 490, 
               495, 489, 482, 477, 471, 468, 468, 469, 470, 462, 457, 453, 446, 443, 
               441, 442, 446, 448, 441, 435, 428, 423, 419, 417, 417, 417, 419, 423, 
               425, 421, 412, 407, 402, 399, 395, 395, 394, 393, 395, 399, 402, 405, 
               405, 398, 392, 388, 385, 381, 377, 375, 375, 375, 377, 378, 380, 382, 
               386, 389, 391, 393, 392, 388, 380, 376, 373, 372, 368, 368, 368, 368, 
               368, 369, 369, 371, 372, 374, 378, 381, 385, 387, 390, 392, 394, 395, 
               394, 388, 383, 377, 374, 373, 371, 370, 369, 369, 370, 371, 372, 373, 
               373, 373, 375, 377, 377, 379, 381, 384, 387, 392, 394, 396, 398, 400, 
               403, 404, 405, 405, 407]

three_fingers = [401, 359, 276, 250, 213, 209, 193, 195, 183, 187, 181, 184, 178,
                 179, 176, 180, 173, 173, 168, 170, 167, 165, 159, 159, 154, 155,
                 155, 158, 175, 170, 176, 188, 170, 165, 171, 175, 171, 178, 190,
                 190, 191, 211, 208, 224, 224, 232, 238, 249, 260, 271, 279, 292,
                 305, 321, 334, 349, 364, 380, 395, 411, 429, 444, 457, 477, 489,
                 501, 509, 521, 526, 529, 527, 529, 534, 533, 527, 520, 516, 515,
                 517, 509, 501, 493, 488, 493, 493, 489, 478, 471, 463, 458, 456,
                 457, 457, 451, 444, 438, 431, 429, 426, 427, 431, 434, 428, 422,
                 416, 409, 405, 404, 402, 402, 403, 408, 410, 408, 399, 402, 393,
                 388, 384, 383, 382, 384, 383, 385, 390, 394, 394, 393, 385, 379,
                 377, 373, 371, 370, 370, 370, 372, 374, 376, 377, 382, 386, 389,
                 391, 393, 389, 381, 385, 379, 375, 371, 370, 371, 372, 373, 374,
                 375, 376, 378, 380, 383, 386, 392, 394, 398, 399, 402, 403, 403,
                 402, 395, 388, 384, 382, 382, 380, 379, 379, 379, 395, 389, 387,
                 386, 386, 387, 386, 389, 390, 393, 396, 399, 404, 406, 407, 408,
                 410, 411, 412, 414, 414, 416]

palm = [376, 347, 270, 246, 210, 205, 190, 191, 182, 186, 178, 178, 172, 176,
        173, 177, 170, 173, 169, 170, 164, 161, 159, 160, 159, 167, 160, 158,
        169, 165, 172, 177, 163, 179, 175, 168, 160, 167, 176, 172, 170, 189,
        180, 203, 194, 192, 188, 204, 207, 206, 214, 220, 226, 233, 231, 234,
        237, 245, 250, 255, 261, 271, 276, 285, 292, 302, 308, 318, 326, 335,
        341, 351, 361, 369, 376, 384, 392, 405, 411, 420, 427, 433, 441, 452,
        461, 464, 467, 470, 472, 477, 482, 490, 487, 483, 482, 482, 479, 478,
        480, 483, 488, 487, 479, 474, 471, 466, 463, 462, 463, 464, 465, 470,
        468, 458, 451, 448, 444, 440, 437, 436, 436, 436, 435, 437, 440, 443,
        441, 433, 426, 421, 418, 415, 411, 409, 408, 408, 407, 409, 410, 412,
        415, 418, 418, 419, 414, 405, 398, 395, 392, 391, 387, 386, 385, 384,
        383, 384, 383, 385, 386, 388, 388, 391, 395, 398, 399, 400, 401, 400,
         396, 387, 380, 377, 377, 375, 374, 372, 370, 370, 370, 371, 372, 371,
        372, 373, 373, 375, 376, 378, 379, 381, 384, 388, 390, 392, 393, 395,
        396, 398, 399, 399, 398]

full = [382, 350, 271, 248, 213, 210, 194, 196, 185, 190, 182, 184, 180, 181,
        174, 178, 173, 176, 173, 176, 168, 166, 160, 160, 159, 157, 170, 163,
        167, 164, 169, 176, 162, 177, 175, 168, 161, 163, 180, 190, 178, 187,
        179, 201, 195, 193, 190, 192, 206, 210, 213, 219, 222, 231, 236, 234,
        235, 239, 244, 249, 254, 261, 264, 273, 277, 285, 289, 299, 306, 314,
        318, 326, 334, 342, 349, 355, 363, 373, 379, 386, 392, 397, 405, 415,
        422, 426, 430, 434, 436, 442, 449, 456, 455, 455, 456, 457, 455, 457,
        460, 463, 469, 466, 462, 459, 457, 455, 452, 451, 453, 455, 459, 462,
        461, 454, 448, 445, 442, 438, 434, 433, 433, 433, 435, 437, 440, 442,
        438, 431, 424, 420, 418, 413, 410, 408, 407, 407, 407, 409, 410, 410,
        415, 417, 419, 419, 416, 408, 400, 396, 394, 392, 388, 387, 385, 383,
        384, 385, 385, 386, 387, 389, 390, 392, 395, 399, 400, 401, 402, 399,
        395, 386, 380, 378, 376, 375, 373, 370, 368, 368, 368, 369, 369, 369,
        369, 371, 372, 373, 374, 374, 376, 378, 380, 385, 387, 389, 390, 391,
        392, 394, 395, 396, 393]


# Plotting
plt.figure(figsize=(10, 6))

plt.plot(none, label='None', color='red')
plt.plot(one_finger, label='One finger', color='blue')
plt.plot(two_fingers, label='Two fingers', color='green')
plt.plot(three_fingers, label='Three fingers', color='orange')
plt.plot(palm, label='Palm', color='purple')
plt.plot(full, label='Full', color='brown')

plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Swept Frequency Capacitive Sensing (SFCS)')
plt.legend()
plt.grid(True)

plt.show()