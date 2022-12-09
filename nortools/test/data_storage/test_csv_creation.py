def test_dataframe_to_csv():

    df_full = ''
    data_folder = ''
    dataframe_to_csv(df_full, data_folder)
    assert pd.load_csv('') == pd.load_csv('')


def test_read_nii_data_from_dir():

    dir_root = Path("/data/nooraang/Data/")
    data_path = '/p03_OAI_SAG_3D_DESS_prep__210819/p03_OAI_SAG_3D_DESS_prep/*/*/*/*.nii.gz'
    nii_create_data_storage(dir_root, data_path)