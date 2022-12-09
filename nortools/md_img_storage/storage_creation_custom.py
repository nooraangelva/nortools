from pathlib import Path
import pandas as pd
import nortools as nt
#https://github.com/MIPT-Oulu/SubregionalCartilageAnalysis/tree/main/scartan/datasets
#https://github.com/MIPT-Oulu/SubregionalCartilageAnalysis

def nii_create_data_storage(dir_root, data_paths, file_name):

    paths, df_images = read_extract_metadata(dir_root, data_paths)
    # Process images (fixed size, normalized [0,1])
    raw_paths, proc_paths = nt.image_processing(paths)
    # Add the raw and processed image paths to dataframe and remove redundant collumn
    df_images = add_columns_to_df(df_images, [raw_paths, proc_paths], ['path_image_raw', 'path_images_proc'])
    df_images = rm_columns_from_df(df_images, ['path_image'])
    # Put the data to 
    dataframe_to_csv(df_images, file_name)


def read_extract_metadata(dir_root, data_paths):

    # Store the paths to the images in a list
    paths_images = list(dir_root.glob(data_paths[0]))
    paths_seg_manual = list(dir_root.glob(data_paths[1]))
    paths_seg_class = list(dir_root.glob(data_paths[2]))
    paths = [paths_images, paths_seg_manual, paths_seg_class]

    # Extract metadata from the directory structure and names
    dict_images = {"patient": [], "protocol": [], "path_image": [], "anatomical_location": [], 'visit_time': [], 'path_segmentation_manual':[], 'path_segmentation_class': []}

    for path_image, path_seg_manual, path_seg_class in [paths_images, paths_seg_manual, paths_seg_class]:
        dict_images["patient"].append(path_image.parts[-3])
        dict_images["protocol"].append(path_image.parts[-4])
        dict_images["path_image"].append(str(path_image))
        dict_images["anatomical_location"].append(path_image.parts[-1])
        dict_images["visit_time"].append(path_image.parts[-2])
        dict_images["path_segmentation_manual"].append(str(path_seg_manual))
        dict_images["path_segmentation_class"].append(str(path_seg_class))
    
    # Create a pandas dataframe with extracted images metadata
    df_images = pd.DataFrame.from_dict(dict_images)

    return [paths, df_images]


def add_columns_to_df(df, collumns, names):
    for coll, name in [collumns, names]:
        df[name] = coll
    return df


def rm_columns_from_df(df, names):
    for name in names:
        df.drop([name], axis=1)
    return df


def dataframe_to_csv(df_full, data_folder):
    # Save the resulting dataframe
    f_out = f"{Path(data_folder).stem}.csv"
    path = Path(data_folder, f_out)
    df_full.to_csv(path, index=None)