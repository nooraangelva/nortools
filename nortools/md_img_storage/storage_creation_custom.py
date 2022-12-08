from pathlib import Path

https://github.com/MIPT-Oulu/SubregionalCartilageAnalysis/tree/main/scartan/datasets
https://github.com/MIPT-Oulu/SubregionalCartilageAnalysis

def dataframe_to_csv(df_full, data_folder, file_name):
    # Save the resulting dataframe
    df_full["path_image"] = df_full["path_image"].str.replace("images_raw", "images_proc")
    df_full["path_annot"] = df_full["path_annot"].str.replace("images_raw", "images_proc")
    f_out = f"{Path(data_folder).stem}.csv"
    path = Path(data_folder, f_out)
    df_full.to_csv(path, index=None)


def read_data_from_dir():
    # Index of images
    dir_root = Path("./s4/dataset_mw85/")
    paths_data = list(dir_root.glob("images_raw/*/*/*.jpg"))
    print(len(paths_data))

    paths_images = [p for p in paths_data if "HGE" not in str(p)]
    paths_annots = [p for p in paths_data if "HGE" in str(p)]

    # Extract metadata from the directory structure and names
    dict_images = {"patient": [], "slice_idx": [], "path_image": []}

    for path_image in paths_images:
        dict_images["patient"].append(path_image.parts[-3])
        dict_images["slice_idx"].append(int(path_image.stem))
        dict_images["path_image"].append(str(path_image))

    df_images = pd.DataFrame.from_dict(dict_images)

    dict_annots = {"patient": [], "slice_idx": [], "path_annot": []}

    for path_annot in paths_annots:
        dict_annots["patient"].append(path_annot.parts[-3])
        dict_annots["slice_idx"].append(int(path_annot.stem.split("_")[0]))
        dict_annots["path_annot"].append(str(path_annot))

    df_annots = pd.DataFrame.from_dict(dict_annots)

    # Merge all the information
    df_meta = df_demo.merge(df_diag, on="PatientNumber", how="outer")
    df_meta = df_meta.rename({"PatientNumber": "patient",
                            "SliceNumber": "slice_idx"}, axis=1)

    df_data = df_images.merge(df_annots, on=["patient", "slice_idx"], how="left")

    df_full = df_meta.merge(df_data, on=["patient", "slice_idx"], how="right")