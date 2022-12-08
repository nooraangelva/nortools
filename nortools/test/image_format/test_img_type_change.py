import nortools.img_type_change as nt
import pathlib
import nibabel as nib

def test_mha_to_nii():

    dir_in = "test_data"
    dir_out = "results/images_to_nii"

    new_file_paths = nt.images_to_nii(dir_in, dir_out)

    assert new_file_paths == ['test_data/CT_2D_head_fixed.nii', 'test_data/CT_2D_head_moving.nii']
    for file in new_file_paths:
        assert "<class 'nibabel.nifti1.Nifti1Image'>" == str(type(nib.load(file)))
        assert 'RAS' == nt.check_nifti_coord_sys(nib.load(file))


def test_dicom_to_nii():
    dir_in = "test_data/dicom"
    dir_out = "results/dicom_to_nii"

    new_file_path = nt.images_to_nii(dir_in, dir_out)

    assert new_file_path == 'results/dicom_to_niidicom.nii.gz'
    assert "<class 'nibabel.nifti1.Nifti1Image'>" == str(type(nib.load(new_file_path)))
    assert 'RAS' == nt.check_nifti_coord_sys(nib.load(new_file_path))