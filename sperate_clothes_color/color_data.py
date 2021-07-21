# RGB Dictionary
RGB = {
    (0, 200, 255): 'sky',
    (0, 0, 255): 'blue',
    (0, 0, 130): 'navy',
    (255, 150, 0): 'orange',
    (255, 255, 0): 'yellow',
    (255, 0, 0): 'red',
    (255, 0, 200): 'pink',
    (0, 255, 0): 'green',
    (255, 255, 255): 'white',
    (125, 125, 125): 'gray',
    (0, 0, 0): 'black'
}
rgb = list(RGB.keys())
rgb_len = len(rgb)


def extract_color(rgb_list):
    final_color = []
    for i in range(len(rgb_list)):
        minimum = 99999999
        for j in range(rgb_len):
            chai = 0
            for k in range(3):
                chai += abs(rgb_list[i][k] - rgb[j][k])
            if chai < minimum:
                minimum = chai
                temp = RGB[rgb[j]]
        final_color.append(temp)
    return final_color
