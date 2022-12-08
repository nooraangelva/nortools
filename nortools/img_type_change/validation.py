import nibabel as nib

def check_nifti_coord_sys(image):
        x, y, z = nib.aff2axcodes(image.affine)
        return ' '.join([x,y,z])