import subprocess as sp 

print("[*] STARTING THE ALGORITHIM")
path= r'"C:\Users\iamne\Desktop\New folder\EL Project\Code\"'  #put \ after the folder path for optimal usep
path = str.rstrip('"')

while True:
    print("1. ImageMaskHSV \n2. ImageMasking(RGB)\n3. ImageMasking(Shapes)\n4. PersepectiveWarpSlider\n5. Canny Image\n6. Affine Transformation\n7. Exit ")
    print('----------------------------------------------')
    usr = int(input("Option Number: "))
    if  usr ==1:
        sp.call(r'python '+path+'imhsv.py"')
    elif usr == 2 :
        sp.call(r'python '+path+'imrgb.py"')
    elif usr ==3 :
        sp.call(r'python '+path+'imshapes.py"')
    elif usr ==4 :
        sp.call(r'python '+path+'PersepectiveWarpSlider.py"')
    elif usr ==5:
        sp.call(r'python '+path+'heycanny.py"')
    elif usr ==6:
        sp.call(r'python '+path+'affine.py"')
    elif usr ==7:
        exit(1)
