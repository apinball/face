import os


os.chdir("haircolor\Style-Your-Hair")
os.system("python main.py --input_dir ./ffhq_image/ --im_path1 face.png --im_path2 hair.png  --output_dir ./style_your_hair_output/  --warp_loss_with_prev_list delta_w style_hair_slic_large  --save_all --version final --flip_check")
os.chdir("..")
os.system("python ./makeup.py")