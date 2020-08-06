from PIL import Image
import time
import binascii


def bindata(message):
    mess_bin = []
    for i in message:
        mess_bin.append(format(ord(i),'08b'))
    return mess_bin

def modPix(image,message):
    mess_bin = bindata(message)
    mess_len = len(mess_bin)
    pix = image.getdata()
    pix_data = iter(pix)
    pix_list=[]

    for i in range(mess_len):
        print(mess_bin[i])
        pix = [val for val in pix_data.__next__()[:3]+
                              pix_data.__next__()[:3]+
                              pix_data.__next__()[:3]]
        print(pix)
        for j in range(0,8):
            if (mess_bin[i][j]=='1' and pix[j]%2==0):
                pix[j] = pix[j]-1
            elif (mess_bin[i][j]=='0' and pix[j]%2 !=0):
                pix[j] = pix[j]-1

        if i <(mess_len -1):
            if (pix[-1]%2 !=0): pix[-1] = pix[-1] -1
        else:
            if (pix[-1]%2 ==0): pix[-1] = pix[-1]-1

        
        pix_list.append(tuple(pix[0:3]))
        pix_list.append(tuple(pix[3:6]))
        pix_list.append(tuple(pix[6:9]))

    print(pix_list,'\n')
    width,height = image.size
    print(width,height)
    iter_obj=iter(pix_list)
    (x, y) = (0, 0)
    j = 0
    while j< (3*mess_len):
        image.putpixel((x,y),iter_obj.__next__())
        image
        print(image.getpixel((x,y)))
        j= j+1
        if (x == width - 1):
            x = 0
            y =y+1
        else:
            x += 1

    return image
        
        
def encode():
    old_image = Image.open("image1.jpg")
    message = input("Enter message to be endcoded: ")
    if len(message)==0:
        raise ValueError("Message is empty")
    new_image = old_image.copy()
    modPix(old_image.copy(), message)
    new_image.save("new_image.jpg")
    
def check():
    old_img = Image.open("image1.jpg",'r')
    new_img = Image.open("new_image.jpg",'r')
    wid_o,he_o = old_img.size
    wid_n,he_n = new_img.size
    (x,y) = (0,0)
    while y < 20:
        while x< 20:
            old_img.getpixel((x,y))
            print("\nold_image_pix: ",old_img.getpixel((x,y)))
            new_img.getpixel((x,y))
            print("new_image_pix: ",new_img.getpixel((x,y)))
            x+=1
        x=0
        y+=1
        
        
    
def decode():
    new_image = Image.open("new_image.jpg",'r')
    image_data = iter(new_image.getdata())
    hid_mess = ""
    while (True):
        pix=[val for val in image_data.__next__()[:3]+image_data.__next__()[:3]+image_data.__next__()[:3]]
        print(pix)
        mess_bin = ""
        for i in pix[:8]:
            if (i%2==0):
                mess_bin += '0'
            else:
                mess_bin += '1'
        print(mess_bin)
        hid_mess += chr(int(mess_bin,2))
        print(hid_mess)
        if (pix[-1]%2!=0):
            break
    return hid_mess

def main():
    choice = int(input("------Welcome to Steganography-----\n 1. Encode\n 2. Decode\n 3. Check\n"))
    if (choice==1):
        encode()
    elif (choice==2):
        print("Decoded message: \n---"+decode()+"----")
    elif (choice==3):
        check()
    else:
        raise Exception("Enter correct input")

if __name__ == '__main__' :
    main()
