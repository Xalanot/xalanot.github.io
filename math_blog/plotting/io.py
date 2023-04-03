from pathlib import Path

import matplotlib.pyplot as plt


def set_matplotlib_dpi(dpi: int = 300):
    plt.rcParams['figure.dpi'] = dpi
    plt.rcParams['savefig.dpi'] = dpi


def save_figure(fig: plt.Figure, output_filepath: Path):
    set_matplotlib_dpi()
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    current_figure = plt.gcf()
    plt.figure(fig)
    plt.tight_layout()
    plt.savefig(output_filepath)
    plt.figure(current_figure)
