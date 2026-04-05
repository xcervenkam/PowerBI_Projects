import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def plot_conf_matrix(y_true, y_pred, labels, title, figsize=(5, 4)):
    fig, ax = plt.subplots(figsize=figsize)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix(y_true, y_pred),
        display_labels=labels
    )
    disp.plot(ax=ax, values_format="d", colorbar=False)
    ax.set_title(title)
    plt.show()
    