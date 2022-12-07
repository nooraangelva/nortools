import os
from pathlib import Path
import numpy as np
import SimpleITK as sitk


def dummy():
    print("I am doing nothing")


if __name__ == "__main__":
    dir_in = "/data/nooraang/Elastix/data"
    fnames_in = ["CT_2D_head_fixed.mha", "CT_2D_head_moving.mha"]

    for f_in in fnames_in:
        f_out = f"{Path(f_in).stem}.nii"
        print(f"{f_in} to {f_out}")

        path_in = Path(dir_in, f_in)
        img = sitk.ReadImage(path_in)
        sitk.WriteImage(img, Path(dir_in, f_out))

