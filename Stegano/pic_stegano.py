from PIL import Image
import click

def int_bin(rgb):
    """Takes pixels in int-pixel(tuples)
    and converts those into bin-pixel(tuples)
    """
    (r,g,b) = rgb
    return ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))

def mer_pix(rgb1,rgb2):
    r1,g1,b1=rgb1
    r2,g2,b2=rgb2
    rgb_mer = (r1[:4]+r2[:4],
               g1[:4]+g2[:4],
               b1[:4]+b2[:4])
    return rgb_mer

def bin_int(rgb):
    """Takes pixels in bin-pixel(tuples)
    and converts those into int-pixel(tuples)
    """
    r,g,b= rgb
    return (int(r,2),int(g,2),int(b,2))
    
def merge(img1,img2):

    #picture1 is the target picture where pic2 is to be hidden
    map_img1 = img1.load()
    map_img2 = img2.load()

    mer_img = Image.new(img1.mode, img1.size)
    map_new = mer_img.load()

    #Checking if pic2 can be contained in pic1
    if img2.size[0]>img1.size[0] or img2.size[1]>img1.size[1]:
        raise ValueError("pic2 is oversized as compared to pic1")

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            rgb1 = int_bin(map_img1[i,j])
            rgb2 = int_bin((0,0,0))
            if (i<img2.size[0] and j<img2.size[1]):
                rgb2 = int_bin(map_img2[i,j])
            rgb_mer = mer_pix(rgb1,rgb2)
            map_new[i,j]= bin_int(rgb_mer)
    return mer_img

def unmerge(img):
    """Unmerge an image.
    :param img: The input image.
    :return: The unmerged/extracted image.
    """
    #loading the pixel map
    map_img = img.load()

    #creating extracted image and loading its pixel map
    unmerge_pic = Image.new(img.mode,img.size)
    map_unmerge = unmerge_pic.load()

    original_size = img.size

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = int_bin(map_img[i,j])
            #extracting significant digits of unmerged image and setting it to 8 bit binary code
            rgb = (r[5:]+'0000',g[5:]+'0000',b[5:]+'0000')
            #converting to int pixel rgb values
            map_unmerge[i,j]=bin_int(rgb)
            # If this is a 'valid' position, store it as the last valid position
            if map_unmerge[i,j] != (0, 0, 0):
                original_size = (i + 1, j + 1)

    # Crop the image based on the 'valid' pixels
    unmerge_pic = unmerge_pic.crop((0, 0, original_size[0], original_size[1]))
    return unmerge_pic

##def merge_pic():
##    merge_pic = merge(Image.open("img1.jpg"),Image.open("img2.jpg"))
##    merge_pic.save("merged_pic.jpg")
##
##def unmerge_pic():
##    unmerged_pic = unmerge(Image.open("merged_pic.jpg"))
##    unmerged_pic.save("img2_copy.jpg")
##
##def main():
##    choice = int(input("\nWhat do you want to do:\n1. Hide image2 into image1\n2. Reveal hidden imgage2 from image1\n"))
##    if choice == 1:
##        merge_pic()
##    elif choice == 2:
##        unmerge_pic()
##    else:
##        raise ValueError("Please enter only 1 or 2")
##    
##if __name__ == '__main__':
##    main()



@click.group()
def cli():
    pass

@cli.command()
@click.option('--img1', required=True, type=str, help='Image that will hide another image')
@click.option('--img2', required=True, type=str, help='Image that will be hidden')
@click.option('--output', required=True, type=str, help='Output image')
def mer_cli(img1,img2,output):
    merge_pic = merge(Image.open(img1),Image.open(img2))
    merge_pic.save(output)

@cli.command()
@click.option('--img', required=True, type=str, help='Image that will be hidden')
@click.option('--output', required=True, type=str, help='Output image')
def unmer_cli(img, output):
    unmerged_image = Steganography.unmerge(Image.open(img))
    unmerged_image.save(output)


if __name__ == '__main__':
    cli()



    
