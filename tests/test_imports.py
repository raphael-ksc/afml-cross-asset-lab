import importlib

import pytest

MODULES = [
    "afml_lab.data.schema",
    "afml_lab.data.bars",
    "afml_lab.data.sources.binance",
    "afml_lab.data.sources.yahoo",
    "afml_lab.data.sources.fred",
    "afml_lab.data.sources.defillama",
    "afml_lab.factors.registry",
    "afml_lab.factors.alignment",
    "afml_lab.labeling.triple_barrier",
    "afml_lab.weights.uniqueness",
    "afml_lab.features.fracdiff",
    "afml_lab.features.structural_breaks",
    "afml_lab.features.microstructure",
    "afml_lab.cv.purged_kfold",
    "afml_lab.models.feature_importance",
    "afml_lab.sizing.bet_size",
    "afml_lab.backtest.stats",
    "afml_lab.portfolio.hrp",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(name)
