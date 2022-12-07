import nortools.img_type_change as nt
import pathlib
import nibabel as nib

def test_mha_to_nii():

    dir_in = "test_data"
    fnames_in = ["CT_2D_head_fixed.mha", "CT_2D_head_moving.mha"]

    new_file_paths = nt.images_to_nii(dir_in, fnames_in)

    assert new_file_paths == ['test_data/CT_2D_head_fixed.nii', 'test_data/CT_2D_head_moving.nii']
    for file in new_file_paths:
        assert "<class 'nibabel.nifti1.Nifti1Image'>" == str(type(nib.load(file)))
