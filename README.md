# roc-utils

<!--https://raw.githubusercontent.com/yngvem/group-lasso/master/README.rst-->

<!--[![Downloads](https://pepy.tech/badge/roc-utils)](https://pepy.tech/project/roc-utils)-->
<!--https://pypistats.org/packages/roc-utils-->
[![image](https://img.shields.io/pypi/v/roc-utils)](https://pypi.org/project/roc-utils/)
[![License](https://img.shields.io/pypi/l/roc-utils)](https://github.com/hirsch-lab/roc-utils/blob/main/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/hirsch-lab/roc-utils/badge)](https://www.codefactor.io/repository/github/hirsch-lab/roc-utils)
[![DeepSource](https://deepsource.io/gh/hirsch-lab/roc-utils.svg/?label=active+issues)](https://deepsource.io/gh/hirsch-lab/roc-utils/?ref=repository-badge)
<!--[![Build Status](https://travis-ci.org/hirsch-lab/cyminiball.svg?branch=main)](https://travis-ci.org/hirsch-lab/roc-utils)-->
<!--Travis build and test-->
<!--Coveralls.io-->
<!--Read-the-docs not required for such a small project-->


This Python package provides tools to compute and visualize [ROC curves](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), which are used to graphically assess the diagnostic ability of binary classifiers. 


Use [`roc_utils`](https://github.com/hirsch-lab/roc-utils) to perform ROC analyses, including the calculation of the ROC-AUC (the area under the ROC curve) and the identification of optimal classification thresholds for different objective functions. In addition, it is possible to compute mean, tolerance interval (TI) and confidence interval (CI) for a set of (related) ROC curves. Finally, error bounds can be estimated and visualized by means of boostrap sampling.

![Exemplary plots generated with `roc_utils`](data/plots-small.png)


To create distribution packages (a source archive and a wheel):

```bash 
python setup.py sdist bdist_wheel
```

To install the newly created Python package from the source archive:

```bash
pip uninstall roc-utils
pip cache remove roc_utils
pip install dist/roc_utils*.tar.gz

```

