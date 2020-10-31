import random
from car_reg_generator.uk_reg import DvlaMemoryTag
from car_reg_generator.uk_reg import UkRegGenerator


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
