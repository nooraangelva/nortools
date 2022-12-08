import nibabel as nib
import numpy as np


def nifti_orien_to_rps(ct_image):
    """
    Check the NIfTI orientation, and flip to  'RPS' if needed.
    :param ct_image: NIfTI file
    :param ct_arr: array file
    :return: array after flipping
    """
    ct_array = np.asarray(ct_image)
    x, y, z = nib.aff2axcodes(ct_image.affine)
    if x != 'R':
        ct_arr = nib.orientations.flip_axis(ct_arr, axis=0)
    if y != 'P':
        ct_arr = nib.orientations.flip_axis(ct_arr, axis=1)
    if z != 'S':
        ct_arr = nib.orientations.flip_axis(ct_arr, axis=2)

    # new_nifti = nib.Nifti1Image(ct_arr.astype(np.float), nii_original_scan.affine)
    # nib.save(new_nifti, f'< path to new scan >.nii.gz')

def lps_to_ras(ct_image):
    """
    Check the NIfTI orientation, and flip   'RAS' if needed.
    :param ct_image: NIfTI file
    :return: array after flipping
    """
    ct_array = np.asarray(ct_image)
    np.diagflat([-1,-1,1,1]).dot(ct_array)

    # new_nifti = nib.Nifti1Image(ct_arr.astype(np.float), nii_original_scan.affine)
    # nib.save(new_nifti, f'< path to new scan >.nii.gz')
