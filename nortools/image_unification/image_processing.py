import numpy as np

def image_processing(paths):
    #TODO
    norm_images = normalize_images(paths)
    uni_images = unify_image_size(norm_images)
    #TODO save images


def normalize_images(paths):

    #TODO paths to images
    images = ''
    proc_images = []

    for img in images:
        proc_images.append( (img - np.min(img)) / (np.max(img) - np.min(img)))
    return proc_images
    

def unify_image_size():
    #TODO
    images = ''
    proc_images = []

    for img in images:
        # Process to a constant shape TODO
        '''
        fixed_shape = (600, 520)

        for idx, row in df_sel.iterrows():
            path_image_in = row["path_image"]
            path_image_out = row["path_image"].replace("/images_raw/", "/images_proc/")
            # Create output directory
            Path(path_image_out).parent.mkdir(parents=True, exist_ok=True)
            
            image_in = cv2.imread(path_image_in, cv2.IMREAD_GRAYSCALE)
            image_out = pad_to(image_in, fixed_shape)
            cv2.imwrite(path_image_out, image_out)
            
            # If annotation exists for the current image, apply the same transformation
            if not pd.isna(row["path_annot"]):
                path_annot_in = row["path_annot"]
                path_annot_out = row["path_annot"].replace("/images_raw/", "/images_proc/")

                annot_in = cv2.imread(path_annot_in, cv2.IMREAD_GRAYSCALE)
                annot_out = pad_to(annot_in, fixed_shape)
                cv2.imwrite(path_annot_out, annot_out)'''
    return proc_images
