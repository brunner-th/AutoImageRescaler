# -*- coding: utf-8 -*-

#-----------------------------------------------------------------
#
# name: thomas brunner
# email: brunner.th@hotmail.com
# nr: 12018550
#
#-----------------------------------------------------------------


from PIL import Image
from PIL import ImageFile
import glob
ImageFile.LOAD_TRUNCATED_IMAGES = True 


# path needs an "Input" and an "Output"- folder in the same directory, see 
# below.

# max_resolution is the resolution of the longest side after resizing
# qual is controlling the quality conservation of the compression (in %)


fp_in = (
    r"C:\Users\brunn\Documents\GitHub\AutoImageRescaler\Input/*" #filenames without string "Input"!
)
fp_out = (
    r"C:\Users\brunn\Documents\GitHub\\AutoImageRescaler\Output/"
)



def CompressFolder(input_path, output_path, max_resolution = 1000, qual = 80):
    images=[]
    for f in sorted(glob.glob(fp_in)):
        images.append([Image.open(f),f])
    cnt = 1
    for image in images:
        shape = image[0].size
        max_res = max(shape)
        rescale_factor = max_resolution/max_res
        output_path = image[1].replace("Input", "Output")
        if rescale_factor > 1:
            print("file:")
            print(image[1])
            print("no rescaling, only compression!")
            image[0].save(output_path, optimize=True,quality= qual)
        else:
            new_x_res = int(shape[0]*rescale_factor)
            new_y_res = int(shape[1]*rescale_factor)
            image[0] = image[0].resize((new_x_res,new_y_res),Image.ANTIALIAS)
            image[0].save(output_path, optimize=True,quality= qual)
        print("-> " + str(cnt) + "/" + str(len(glob.glob(fp_in))) + " files done!")
        cnt += 1
            

#function call
CompressFolder(fp_in, fp_out)




