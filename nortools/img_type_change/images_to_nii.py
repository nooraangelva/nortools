import os
from pathlib import Path
import numpy as np
import SimpleITK as sitk
import dicom_numpy
import nibabel as nib
import glob

def images_to_nii(dir_in, dir_out):

    path_in = Path(dir_in)
    dicomlist = list(path_in.glob("*"))

    for f_in in dicomlist:
        # Create a path and a file for results
        # Read image and write to in a new format
        img = sitk.ReadImage(f_in)
        sitk.WriteImage(img, Path(dir_out, os.path.basename(f_in), '.nii.gz'))


def dicom_to_nii(dir_in, out_dir):

    if os.path.isdir(dir_in):
        # check for common DICOM suffixes
        for ext in ("*.dcm", "*.DCM", "*.dc", "*.DC", "*.IMG"):
            pattern = os.path.join(dir_in, ext)
            dicomlist = glob.glob(pattern)
            if dicomlist:
                break

    vol, affine_LPS = dicom_numpy.combine_slices(dicomlist)

    # Convert the LPS affine to RAS
    affine_RAS = np.diagflat([-1,-1,1,1]).dot(affine_LPS)

    # Create nibabel nifti object
    niiimg = nib.Nifti1Image(vol, affine_RAS)
    nib.save(niiimg, Path(out_dir, os.path.basename(dir_in), '.nii.gz'))