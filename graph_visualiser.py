import matplotlib.pyplot as plt

'''
#NOTE
This code is for visualising SFCS wave of different action for the report.
'''

# Classified actions
action = ["None", "Fingers", "Fist", "Palm", "Side"] #<---- !!! Make sure to change based on use case


# Define the arrays
a = [336, 312, 245, 226, 198, 196, 185, 187, 180, 184, 178, 180, 173, 174, 170, 170, 167, 167, 163, 166, 161, 159, 153, 155, 157, 153, 166, 158, 168, 167, 166, 177, 171, 190, 200, 216, 237, 269, 305, 356, 421, 498, 608, 730, 877, 950, 986, 997, 932, 863, 774, 708, 651, 601, 571, 535, 507, 497, 471, 453, 445, 433, 417, 410, 407, 401, 387, 382, 381, 379, 366, 361, 357, 360, 354, 346, 337, 336, 337, 338, 329, 323, 314, 312, 312, 312, 302, 298, 288, 284, 284, 285, 294, 296, 300, 301, 306, 308, 318, 326, 335, 340, 344, 341, 340, 336, 340, 340, 343, 344, 351, 358, 366, 368, 368, 365, 369, 366, 371, 372, 380, 384, 394, 404, 418, 428, 442, 452, 462, 460, 464, 470, 481, 500, 506, 506, 505, 502, 502, 501, 499, 494, 483, 475, 463, 457, 449, 439, 418, 402, 385, 377, 368, 362, 356, 353, 349, 346, 343, 340, 334, 336, 334, 335, 330, 328, 324, 323, 320, 318, 314, 311, 303, 295, 289, 284, 278, 275, 273, 274, 274, 280, 282, 283, 286, 287, 294, 296, 300, 306, 312, 317, 325, 330, 331, 333, 338, 342, 346, 347, 351]

b = [442, 369, 271, 233, 195, 185, 170, 168, 161, 160, 153, 153, 153, 155, 155, 160, 154, 153, 149, 149, 148, 146, 141, 142, 141, 153, 149, 148, 161, 156, 159, 167, 152, 161, 166, 159, 151, 151, 164, 163, 164, 186, 181, 201, 198, 202, 207, 224, 234, 246, 255, 269, 277, 294, 309, 326, 347, 374, 397, 427, 454, 486, 519, 558, 592, 627, 664, 702, 728, 751, 762, 771, 773, 763, 746, 725, 704, 689, 674, 651, 628, 606, 588, 577, 572, 561, 544, 529, 515, 503, 495, 492, 490, 483, 468, 460, 449, 446, 440, 437, 437, 438, 432, 425, 420, 410, 403, 402, 397, 398, 393, 398, 400, 400, 390, 383, 377, 371, 370, 367, 364, 365, 364, 366, 369, 373, 369, 364, 354, 349, 348, 343, 339, 338, 337, 337, 337, 339, 341, 344, 347, 352, 354, 356, 358, 355, 351, 347, 348, 346, 345, 343, 343, 343, 346, 348, 353, 356, 360, 361, 367, 368, 374, 377, 380, 386, 389, 386, 390, 380, 377, 373, 373, 373, 375, 376, 376, 380, 382, 383, 386, 389, 393, 393, 394, 398, 400, 406, 409, 413, 420, 429, 437, 439, 443, 447, 449, 451, 453, 456, 461]

c = [389, 342, 259, 226, 188, 180, 165, 165, 158, 158, 152, 153, 149, 150, 150, 156, 148, 149, 145, 148, 146, 153, 146, 143, 143, 142, 158, 153, 163, 154, 155, 153, 147, 164, 159, 158, 151, 149, 166, 173, 174, 188, 176, 195, 186, 184, 184, 201, 211, 214, 218, 226, 232, 243, 243, 251, 261, 275, 286, 300, 314, 333, 351, 367, 384, 407, 431, 457, 483, 508, 533, 568, 598, 626, 651, 673, 701, 728, 743, 747, 748, 741, 733, 724, 718, 694, 674, 658, 638, 623, 610, 601, 595, 578, 560, 547, 533, 522, 516, 513, 510, 508, 500, 486, 478, 471, 462, 456, 452, 450, 447, 452, 450, 448, 435, 430, 422, 415, 409, 403, 400, 401, 400, 403, 405, 406, 407, 401, 392, 386, 382, 379, 377, 373, 373, 374, 370, 371, 367, 366, 369, 371, 373, 374, 371, 371, 360, 353, 349, 349, 345, 341, 339, 343, 343, 343, 343, 343, 348, 351, 356, 358, 363, 365, 367, 369, 368, 367, 367, 359, 353, 354, 354, 354, 357, 354, 355, 354, 359, 359, 360, 358, 361, 363, 364, 368, 374, 376, 374, 376, 380, 385, 391, 391, 395, 400, 401, 404, 408, 412, 416]

d = [446, 380, 277, 233, 191, 180, 165, 163, 156, 158, 151, 155, 149, 149, 146, 147, 145, 145, 144, 147, 142, 142, 138, 141, 143, 141, 154, 149, 153, 154, 149, 163, 152, 161, 157, 156, 157, 153, 167, 184, 169, 180, 168, 186, 177, 174, 178, 181, 193, 198, 201, 207, 210, 215, 215, 214, 213, 222, 231, 233, 240, 252, 260, 270, 279, 289, 300, 314, 328, 343, 356, 379, 389, 409, 429, 451, 474, 499, 519, 540, 563, 584, 606, 627, 639, 650, 661, 668, 674, 679, 682, 688, 681, 667, 651, 642, 631, 622, 615, 610, 607, 600, 581, 566, 556, 546, 536, 530, 524, 522, 517, 522, 514, 507, 493, 484, 475, 469, 465, 457, 456, 454, 454, 453, 453, 452, 447, 442, 430, 424, 417, 413, 407, 405, 402, 404, 398, 400, 392, 397, 405, 407, 406, 404, 403, 395, 387, 383, 379, 377, 372, 369, 366, 365, 361, 363, 363, 362, 362, 363, 364, 371, 375, 376, 375, 379, 379, 376, 373, 368, 365, 358, 357, 356, 357, 356, 355, 352, 348, 348, 350, 349, 345, 351, 354, 351, 353, 357, 361, 363, 363, 370, 372, 375, 378, 377, 382, 381, 383, 381, 378]

e = [362, 327, 250, 222, 188, 180, 163, 164, 152, 155, 149, 150, 144, 144, 141, 147, 142, 143, 141, 145, 142, 141, 137, 138, 138, 138, 151, 146, 148, 151, 148, 156, 148, 160, 153, 151, 149, 146, 155, 150, 151, 172, 162, 181, 172, 168, 166, 186, 191, 193, 184, 180, 192, 202, 197, 196, 193, 198, 207, 208, 207, 218, 221, 219, 229, 234, 239, 244, 248, 260, 265, 273, 282, 295, 304, 314, 324, 334, 346, 359, 373, 387, 403, 420, 429, 445, 458, 475, 492, 508, 528, 541, 545, 557, 566, 580, 585, 600, 608, 614, 623, 614, 609, 605, 598, 593, 593, 590, 586, 586, 585, 584, 575, 558, 549, 540, 534, 523, 516, 512, 507, 505, 501, 503, 504, 502, 496, 482, 472, 465, 459, 455, 449, 449, 447, 450, 446, 440, 439, 440, 438, 443, 441, 439, 440, 435, 421, 424, 414, 410, 402, 399, 395, 392, 392, 395, 397, 395, 392, 396, 393, 403, 404, 402, 404, 403, 404, 400, 389, 380, 374, 371, 367, 366, 365, 360, 358, 357, 356, 370, 362, 359, 357, 356, 356, 357, 360, 359, 360, 359, 363, 365, 367, 369, 376, 375, 375, 377, 377, 379, 370]

#f = []


# Plotting
plt.figure(figsize=(10, 6))

plt.plot(a, label=action[0], color='red')
plt.plot(b, label=action[1], color='blue')
plt.plot(c, label=action[2], color='green')
plt.plot(d, label=action[3], color='orange')
plt.plot(e, label=action[4], color='purple')
#plt.plot(f, label=action[5], color='brown')

plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('SFCS Pad')
plt.legend()
plt.grid(True)

plt.show()