from textwrap import fill
from turtle import color, width
from PIL import Image, ImageDraw, ImageChops
import random
import colorsys

def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

def interpolate(start_color, end_color, factor:float):
    recip = 1 - factor
    return(
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor),
    )

def generate_NFT(path: str):
    #Creates Background Image
    print('Creating NFT!')
    target_size = 256
    scale_factor = 2
    image_size = target_size * scale_factor
    padding_px = 15 * scale_factor
    line_thickness = scale_factor
    image_bg_color = (0, 0, 0)
    start_color = random_color()
    end_color = random_color()
    points = []
    n_points = len(points) - 1 
    image = Image.new('RGB', size = (image_size, image_size), color = image_bg_color)

    #Drawlines
    draw = ImageDraw.Draw(image)   
    

    for _ in range(10):
        random_point = (random.randint(padding_px, (image_size - padding_px)), random.randint(padding_px, (image_size - padding_px)))
        points.append(random_point)


    #Draw Box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    


    #Center NFT
    delta_x = min_x - (image_size - max_x)
    delta_y = min_y - (image_size - max_y)

    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)
    


    #Draw points
    for i, point in enumerate(points):

        #overlay canvas
        overlay_image = Image.new('RGB', size = (image_size, image_size), color = image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point
        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i + 1]
        
        line_cords = (p1, p2)
        color_factor = i /n_points
        line_color = interpolate(start_color, end_color, color_factor)
        line_thickness += 1
        overlay_draw.line(line_cords, fill=line_color, width=line_thickness)
        image = ImageChops.add(image, overlay_image)
    image = image.resize((target_size, target_size), resample=Image.ANTIALIAS)
    image.save(path)




if __name__ == '__main__':
    for i in range(10):
        generate_NFT(f'test_nft_{i}.png')