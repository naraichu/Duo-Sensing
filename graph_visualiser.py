import matplotlib.pyplot as plt

'''
#NOTE
This code is for visualising SFCS wave of different action for the report.
'''

# Classified actions
action = ["None", "One finger", "Two fingers", "Three fingers", "Palm", "Full"]


# Define the arrays
a = [326, 316, 249, 231, 203, 201, 188, 189, 180, 184, 177, 180, 175, 176, 172, 177, 171, 171, 169, 169, 167, 171, 166, 165, 159, 157, 155, 156, 174, 169, 179, 189, 177, 194, 198, 205, 215, 236, 257, 285, 318, 358, 408, 473, 562, 663, 787, 905, 964, 993, 1008, 1016, 975, 907, 844, 773, 715, 678, 634, 599, 577, 552, 526, 509, 500, 484, 466, 458, 453, 445, 429, 423, 417, 420, 412, 401, 393, 391, 392, 392, 383, 374, 367, 366, 367, 368, 360, 354, 342, 337, 333, 330, 327, 328, 318, 311, 307, 301, 300, 304, 317, 323, 330, 331, 339, 339, 344, 346, 353, 357, 364, 370, 378, 378, 376, 372, 371, 369, 372, 373, 379, 382, 386, 391, 401, 406, 414, 418, 418, 414, 416, 417, 425, 431, 440, 446, 455, 468, 481, 497, 519, 533, 548, 558, 566, 574, 582, 577, 561, 556, 542, 527, 517, 508, 498, 489, 479, 469, 457, 450, 442, 439, 435, 432, 424, 420, 413, 409, 403, 400, 395, 390, 376, 365, 354, 346, 340, 335, 330, 329, 325, 324, 320, 319, 315, 313, 311, 310, 308, 308, 308, 313, 313, 314, 314, 314, 317, 321, 325, 327, 333]

b = [327, 316, 249, 230, 202, 201, 189, 190, 183, 185, 178, 179, 174, 174, 173, 175, 171, 173, 168, 169, 162, 160, 159, 157, 155, 170, 183, 170, 180, 174, 178, 186, 174, 191, 195, 205, 214, 233, 256, 284, 318, 357, 409, 474, 560, 663, 788, 906, 964, 994, 1008, 1016, 975, 906, 843, 775, 716, 679, 634, 599, 576, 552, 525, 508, 499, 485, 467, 457, 453, 445, 430, 423, 418, 421, 411, 402, 393, 391, 392, 393, 383, 376, 368, 366, 367, 369, 360, 356, 344, 339, 331, 333, 329, 330, 317, 310, 303, 299, 302, 305, 316, 322, 331, 332, 340, 339, 345, 346, 353, 355, 363, 368, 377, 379, 376, 372, 373, 371, 374, 374, 377, 380, 386, 391, 401, 406, 415, 419, 418, 413, 417, 417, 425, 432, 441, 446, 453, 467, 482, 497, 517, 531, 547, 559, 565, 573, 580, 574, 568, 556, 542, 525, 515, 509, 498, 489, 478, 468, 458, 452, 443, 437, 433, 431, 425, 420, 413, 409, 403, 401, 395, 391, 378, 366, 356, 347, 340, 336, 330, 329, 337, 331, 325, 322, 317, 316, 311, 310, 309, 309, 308, 310, 311, 315, 315, 316, 316, 319, 324, 328, 333]

c = [321, 310, 246, 232, 203, 203, 189, 190, 180, 183, 177, 176, 172, 174, 174, 179, 171, 171, 168, 169, 166, 163, 158, 159, 156, 171, 163, 160, 174, 170, 176, 184, 173, 193, 195, 205, 214, 235, 259, 286, 318, 357, 409, 477, 564, 664, 788, 905, 964, 994, 1008, 1016, 974, 906, 843, 776, 718, 680, 636, 600, 577, 553, 526, 509, 500, 484, 467, 458, 454, 444, 429, 423, 418, 420, 411, 401, 394, 391, 392, 391, 382, 375, 366, 367, 366, 369, 360, 355, 342, 338, 333, 334, 328, 329, 319, 313, 304, 300, 301, 306, 319, 323, 333, 334, 340, 339, 345, 346, 352, 355, 364, 370, 377, 380, 378, 373, 375, 371, 373, 372, 378, 381, 387, 391, 401, 408, 415, 419, 421, 415, 416, 417, 424, 431, 439, 445, 454, 468, 479, 495, 518, 534, 543, 556, 565, 576, 584, 570, 559, 555, 542, 525, 515, 509, 498, 490, 478, 468, 457, 450, 441, 440, 434, 430, 424, 419, 413, 409, 404, 401, 396, 389, 379, 366, 356, 347, 338, 334, 329, 329, 325, 323, 320, 320, 317, 316, 311, 309, 308, 308, 309, 312, 312, 312, 314, 316, 318, 320, 324, 327, 335]

d = [325, 314, 248, 230, 202, 198, 185, 188, 179, 184, 178, 177, 172, 172, 172, 176, 168, 168, 165, 169, 164, 162, 161, 159, 155, 154, 171, 160, 150, 166, 168, 187, 174, 186, 193, 199, 206, 224, 244, 265, 293, 327, 369, 423, 489, 568, 670, 787, 905, 964, 993, 1008, 1016, 984, 931, 857, 790, 744, 690, 646, 620, 589, 559, 539, 526, 509, 488, 477, 472, 461, 446, 438, 432, 433, 423, 415, 406, 403, 403, 403, 393, 385, 378, 377, 378, 379, 370, 365, 353, 350, 345, 346, 342, 343, 331, 323, 314, 310, 305, 306, 314, 315, 318, 321, 327, 326, 334, 337, 345, 350, 359, 364, 373, 374, 371, 368, 370, 367, 370, 369, 373, 376, 383, 386, 394, 401, 408, 411, 407, 402, 404, 404, 409, 414, 420, 424, 432, 443, 453, 466, 483, 495, 512, 522, 531, 545, 550, 549, 550, 553, 548, 541, 539, 535, 528, 525, 517, 507, 497, 490, 481, 474, 469, 465, 458, 451, 443, 437, 429, 427, 420, 414, 397, 384, 374, 366, 358, 353, 348, 346, 342, 341, 338, 336, 332, 329, 326, 326, 324, 324, 321, 322, 323, 323, 320, 320, 319, 321, 321, 323, 325]

e = [372, 337, 260, 235, 201, 197, 182, 185, 178, 180, 173, 172, 167, 169, 169, 172, 163, 163, 159, 164, 156, 165, 155, 154, 153, 165, 158, 153, 164, 164, 172, 164, 158, 178, 183, 180, 180, 188, 200, 207, 218, 240, 252, 274, 293, 319, 347, 381, 418, 465, 515, 576, 646, 724, 798, 871, 937, 972, 977, 957, 934, 885, 830, 788, 754, 711, 671, 645, 626, 599, 573, 554, 540, 533, 516, 500, 488, 480, 476, 469, 456, 446, 437, 436, 433, 435, 424, 417, 407, 403, 398, 402, 402, 402, 392, 387, 377, 374, 369, 369, 373, 375, 369, 363, 355, 348, 340, 336, 334, 335, 336, 339, 341, 342, 337, 334, 335, 333, 337, 339, 344, 347, 353, 357, 368, 373, 380, 378, 375, 370, 372, 371, 372, 370, 373, 375, 381, 382, 388, 391, 401, 404, 411, 415, 420, 421, 413, 410, 413, 415, 417, 416, 420, 426, 432, 437, 444, 450, 458, 467, 474, 481, 490, 498, 506, 515, 522, 530, 536, 537, 536, 518, 503, 495, 487, 480, 478, 475, 470, 468, 464, 461, 456, 451, 444, 439, 433, 429, 425, 424, 421, 422, 419, 417, 414, 413, 408, 406, 401, 399, 398]

f = [371, 339, 259, 235, 202, 195, 182, 182, 172, 176, 171, 176, 171, 171, 166, 172, 166, 168, 167, 165, 163, 159, 157, 155, 153, 152, 171, 162, 175, 170, 174, 165, 158, 182, 183, 180, 179, 186, 203, 220, 228, 247, 256, 276, 295, 321, 350, 384, 424, 471, 525, 585, 655, 738, 812, 884, 947, 981, 980, 955, 928, 878, 823, 781, 748, 706, 666, 639, 619, 595, 568, 550, 538, 530, 514, 497, 483, 477, 474, 470, 456, 446, 436, 433, 432, 433, 421, 416, 406, 403, 399, 402, 401, 400, 392, 385, 375, 374, 367, 368, 371, 372, 369, 363, 356, 346, 338, 336, 332, 334, 332, 336, 340, 343, 338, 335, 335, 335, 339, 343, 346, 348, 356, 361, 370, 373, 380, 378, 376, 372, 373, 369, 371, 371, 377, 376, 379, 382, 388, 393, 400, 404, 410, 416, 421, 421, 413, 412, 413, 415, 418, 418, 424, 428, 434, 440, 448, 455, 463, 472, 478, 484, 493, 501, 508, 515, 522, 529, 536, 538, 536, 518, 505, 495, 487, 477, 472, 472, 470, 467, 461, 457, 451, 447, 441, 435, 429, 427, 422, 422, 418, 418, 416, 414, 412, 411, 406, 403, 398, 397, 395]


# Plotting
plt.figure(figsize=(10, 6))

plt.plot(a, label=action[0], color='red')
plt.plot(b, label=action[1], color='blue')
plt.plot(c, label=action[2], color='green')
plt.plot(d, label=action[3], color='orange')
plt.plot(e, label=action[4], color='purple')
plt.plot(f, label=action[5], color='brown')

plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('SFCS of long strip')
plt.legend()
plt.grid(True)

plt.show()