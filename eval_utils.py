from typing import List, Literal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix


def show_confusion_matrix(
        y_true: np.ndarray, y_pred: np.ndarray, classes: List[str],
        normalize: Literal['true', 'pred', 'all'] = 'pred',
        n_decimals=2, figsize=(10, 10), linewidth=0.01, fontsize=11) -> None:
    
    mat = confusion_matrix(y_true, y_pred, normalize=normalize)
    mat_df = pd.DataFrame(np.around(mat, n_decimals),
                          index=classes, columns=classes)
    plt.figure(figsize=figsize)
    sns.heatmap(mat_df, annot=True, cbar=False, linewidths=linewidth,
                annot_kws={'fontsize': fontsize})
    

def evaluate(y_true: np.ndarray, y_pred: np.ndarray,
             classes: List[str]) -> None:
    
    print(classification_report(y_true, y_pred))
    show_confusion_matrix(y_true, y_pred, classes)
