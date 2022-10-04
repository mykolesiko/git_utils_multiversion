__version__ = "0.2.2"
__author__ = "Norman Juchler"

from ._roc import (get_objective,
                   compute_roc,
                   compute_mean_roc,
                   compute_roc_bootstrap,
                   compute_roc_multi,
                   calculate_bootstrap_auc_way2)
from ._plot import (plot_roc,
                    plot_mean_roc,
                    plot_roc_simple,
                    plot_roc_bootstrap)
from ._demo import (demo_basic,
                    demo_bootstrap,
                    demo_sample_data)
