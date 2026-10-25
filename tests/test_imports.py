import importlib

import pytest

MODULES = [
    "afml_fx.data.loader",
    "afml_fx.data.bars",
    "afml_fx.labeling.triple_barrier",
    "afml_fx.weights.uniqueness",
    "afml_fx.features.fracdiff",
    "afml_fx.features.structural_breaks",
    "afml_fx.features.microstructure",
    "afml_fx.cv.purged_kfold",
    "afml_fx.models.feature_importance",
    "afml_fx.sizing.bet_size",
    "afml_fx.backtest.stats",
    "afml_fx.portfolio.hrp",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(name)
