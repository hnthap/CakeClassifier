import os
import zipfile

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from my_secrets import data_zip_filepath


def load_cakes(zip_filepath: str = data_zip_filepath,
               verbose = True) -> pd.DataFrame:
    
    # Extract the ZIP file
    assert os.path.exists(zip_filepath)
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(os.path.curdir)

    # Create two lists, one contains the paths of the images,
    # one contains each image's label (classname)
    data_path = os.path.join(os.path.curdir, 'Cake')
    assert os.path.exists(data_path)
    img_paths = []
    y = []
    for classname in os.listdir(data_path):
        img_dirpath = os.path.join(data_path, classname)
        if verbose:
            print(f'Trying iterating through {img_dirpath} ...')
        assert os.path.exists(img_dirpath)

        n_items = None
        for root, _, filenames in os.walk(img_dirpath, topdown=False):
            for filename in filenames:
                img_paths.append(os.path.join(root, filename))
                y.append(classname)
            n_items = len(filenames)
            break

        if verbose:
            print(f'SUCCESS! There is (are) {n_items} item(s)')

    assert len(img_paths) == len(y)
    if verbose:
        print(f'Overall, there is (are) {len(y)} item(s)')

    # Create a data frame out of the two lists
    df = pd.DataFrame(data={'filepath': img_paths, 'label': y})
    return df


def show_cv_image(img: np.ndarray, title: str = None) -> None:
    try:
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    except:
        img_rgb = img.copy()
    plt.imshow(img_rgb)
    plt.axis('off')
    if title is not None:
        plt.title(title)
    plt.show()


def show_sample(df_arg: pd.DataFrame, i: int) -> None:
    img_temp = cv.imread(df_arg.filepath.iloc[i], 0)
    label = df_arg.label.iloc[i]
    show_cv_image(img_temp, f'{label}\nID {i}')
