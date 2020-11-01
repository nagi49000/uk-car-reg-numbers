import numpy as np
import random
import pytest
from car_reg_generator.uk_reg import DvlaMemoryTag
from car_reg_generator.uk_reg import UkRegGenerator
from car_reg_generator.uk_reg import UkRegVectorizer
from car_reg_generator.uk_reg import UkRegBowVectorizer


def test_dvla_memory_tag():
    d = DvlaMemoryTag()
    assert d.regions['reading'] == ['RA', 'RB', 'RC', 'RD', 'RE', 'RF', 'RG',
                                    'RH', 'RI', 'RJ', 'RK', 'RL', 'RM', 'RN',
                                    'RO', 'RP', 'RQ', 'RR', 'RS', 'RT', 'RU',
                                    'RV', 'RW', 'RX', 'RY']


def test_uk_reg_generator():
    random.seed(0)
    g = UkRegGenerator()
    assert g.get_reg() == 'YK66BIQ'
    assert g.get_reg() == 'MQ64PLS'


def test_uk_reg_vectorizer():
    v = UkRegVectorizer().vectorize('YK09AIZ')
    assert v == pytest.approx([0.94444444, 0.55555556, 0.0, 0.25, 0.27777778, 0.5, 0.97222222])

    s = UkRegVectorizer().recover([0.94444444, 0.55555556, 0.0, 0.25, 0.27777778, 0.5, 0.97222222])
    assert s == 'YK09AIZ'

    with pytest.raises(ValueError):
        UkRegVectorizer().vectorize(';')

    with pytest.raises(ValueError):
        UkRegVectorizer().recover([1.5])

    with pytest.raises(ValueError):
        UkRegVectorizer().recover([-0.5])


def test_uk_reg_bow_vectorizer():
    v = UkRegBowVectorizer().vectorize('YK09AIZ')
    assert len(v) == 36 * 7
    assert np.sum(np.abs(v)) == pytest.approx(7.0)
    assert list(np.where(v == 1)[0]) == [34,  56,  72, 117, 154, 198, 251]

    assert UkRegBowVectorizer().recover(v) == 'YK09AIZ'

    with pytest.raises(ValueError):
        # length of vector inconsistent with BoW
        UkRegBowVectorizer().recover(np.zeros(17))
