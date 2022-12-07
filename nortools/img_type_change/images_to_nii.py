import os
from pathlib import Path
import numpy as np
import SimpleITK as sitk
import dicom2nifti 

def images_to_nii(dir_in, fnames_in):

    for f_in in fnames_in:
        # Create a path and a file for results
        f_out = f"{Path(f_in).stem}.nii"
        path_in = Path(dir_in, f_in)

        # Read image and write to in a new format
        img = sitk.ReadImage(path_in)
        sitk.WriteImage(img, Path(dir_in, f_out))


def dicom_to_nii(dir_in, fnames_in):
    for f_in in fnames_in:
        f_out = f"{Path(f_in).stem}.dcm"
        path_in = Path(dir_in, f_in)
        dicom2nifti.convert_directory(f_out, path_in)
