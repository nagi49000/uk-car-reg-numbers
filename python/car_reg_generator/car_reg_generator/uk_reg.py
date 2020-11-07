import numpy as np
from random import choice
from typing import Dict


class DvlaMemoryTag:
    """ definitions derived from https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/359317/INF104_160914.pdf """

    def __init__(self):
        """  object has member region, which is a dict<str, str>, key being uk region, value list of 2-elt memory tags """
        self.regions = self.get_expanded_regions(self.get_regions())

    def get_regions(self) -> Dict[str, str]:
        return {'anglia': ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AJ', 'AK', 'AL', 'AM', 'AN',
                           'AO', 'AP', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY'],
                'birmingham': ['B'],
                'cardiff': ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO'],
                'swansea': ['CP', 'CR', 'CS', 'CT', 'CU', 'CV'],
                'bangor': ['CW', 'CX', 'CY'],
                'chester': ['DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DJ', 'DK'],
                'shrewsbury': ['DL', 'DM', 'DN', 'DO', 'DP', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY'],
                'essex': ['E'],
                'nottingham': ['FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FJ', 'FK', 'FL', 'FM', 'FN', 'FP'],
                'lincoln': ['FR', 'FS', 'FT', 'FV', 'FW', 'FX', 'FY'],
                'maidstone': ['GA', 'GB', 'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO'],
                'brighton': ['GP', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY'],
                'bournemouth': ['HA', 'HB', 'HC', 'HD', 'HE', 'HF', 'HG', 'HH', 'HJ'],
                'portsmouth': ['HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY'],
                'borehamwood': ['KA', 'KB', 'KC', 'KD', 'KE', 'KF', 'KG', 'KH', 'KJ', 'KK', 'KL'],
                'northampton': ['KM', 'KN', 'KO', 'KP', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY'],
                'london': ['LA', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LJ', 'LK', 'LL', 'LM', 'LN',
                           'LO', 'LP', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY'],
                'manchester': ['M'],
                'newcastle': ['NA', 'NB', 'NC', 'ND', 'NE', 'NG', 'NH', 'NJ', 'NK', 'NL', 'NM', 'NN', 'NO'],
                'stockton': ['NP', 'NR', 'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY'],
                'oxford': ['O'],
                'preston': ['PA', 'PB', 'PC', 'PD', 'PE', 'PF', 'PG', 'PH', 'PJ', 'PK', 'PL', 'PM', 'PN',
                            'PO', 'PP', 'PR', 'PS', 'PT'],
                'carlisle': ['PU', 'PV', 'PW', 'PX', 'PY'],
                'reading': ['R'],
                'glasgow': ['SA', 'SB', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SJ'],
                'edinburgh': ['SK', 'SL', 'SM', 'SN', 'SO'],
                'dundee': ['SP', 'SR', 'SS', 'ST'],
                'aberdeen': ['SU', 'SV', 'SW'],
                'inverness': ['SX', 'SY'],
                'worcester': ['V'],
                'exeter': ['WA', 'WB', 'WC', 'WD', 'WE', 'WF', 'WG', 'WH', 'WJ'],
                'truro': ['WK', 'WL'],
                'bristol': ['WM', 'WN', 'WO', 'WP', 'WR', 'WS', 'WT', 'WU', 'WV', 'WW', 'WX', 'WY'],
                'leeds': ['YA', 'YB', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH', 'YJ', 'YK'],
                'sheffield': ['YL', 'YM', 'YN', 'YO', 'YP', 'YR', 'YS', 'YT', 'YU'],
                'beverley': ['YV', 'YW', 'YX', 'YY']
                }

    def get_expanded_regions(self, regions: Dict[str, str]) -> Dict[str, str]:
        for k, v in regions.items():
            for tag in v:
                if len(v) == 1:  # single letter to expand
                    v.remove(tag)
                    v += [tag + chr(x) for x in range(ord('A'), ord('A')+25)]
            regions[k] = v
        return regions


class UkRegGenerator:
    """ definitions derived from https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/359317/INF104_160914.pdf """

    def __init__(self):
        self.memory_tags = sum(DvlaMemoryTag().regions.values(), [])
        self.numbers = [x for x in '0123456789']
        self.letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    def get_reg(self) -> str:
        memory_tag = choice(self.memory_tags)
        age_identifier = choice(self.numbers) + choice(self.numbers)
        rand_letters = choice(self.letters) + choice(self.letters) + choice(self.letters)
        return memory_tag + age_identifier + rand_letters


class UkRegVectorizer:
    """ vectorizing by taking the reg letters, and converting each to a floating point in [0,1],
        so a 7-element string is converted to a 7-element float array
    """

    def __init__(self):
        self.chars = [x for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.encoding_dict = {x[1]: x[0] for x in enumerate(self.chars)}
        self.decoding_dict = {x[0]: x[1] for x in enumerate(self.chars)}

    def vectorize(self, uk_reg_str: str) -> np.array:
        reg_chars = [x for x in uk_reg_str]
        if set(reg_chars) - set(self.chars):
            raise ValueError('out of bound chars found in ' + str(uk_reg_str))
        return np.array([self.encoding_dict[x] for x in reg_chars]) / len(self.encoding_dict)

    def recover(self, vec: np.array) -> str:
        int_list = np.rint(np.array(vec) * len(self.encoding_dict))
        if set(int_list) - set(self.encoding_dict.values()):
            raise ValueError('vector values out of range')
        return ''.join([self.decoding_dict[x] for x in int_list])


class UkRegBowVectorizer:
    """ vectorizing by taking the reg letters, and one-hot encoding on 0-9,A-Z,
        so a 3-element string is converted to a 3*(10+26) = 108-element array;
        all zeros except for 3 entries which are 1
    """

    def __init__(self):
        self.chars = [x for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.encoding_dict = {x[1]: x[0] for x in enumerate(self.chars)}
        self.decoding_dict = {x[0]: x[1] for x in enumerate(self.chars)}

    def vectorize(self, uk_reg_str: str) -> np.array:
        vec = np.zeros(len(self.chars) * len(uk_reg_str))
        for ind, c in enumerate(uk_reg_str):
            vec[ind*len(self.chars) + self.encoding_dict[c]] = 1.0
        return vec

    def recover(self, vec: np.array) -> str:
        if len(vec) % len(self.chars) != 0:
            raise ValueError('vector length not divisible by number of chars')
        reg_len = int(len(vec) / len(self.chars))
        # reshape as matrix, so we can take max along each BoW letter encoding
        mtr = np.reshape(vec, (reg_len, len(self.chars)))
        return ''.join([self.decoding_dict[x] for x in np.argmax(mtr, axis=1)])


class UkRegDvlaVectorizer:
    """ vectorizing by taking the reg letters, and one-hot encoding on
        0-9 for chars 2,3 and A-Z on chars 0-1, 4-6
        so all reg strs must be of the form AA00AAA (for alphas and numerics).
        The vectorized form is a vector of length 2*10 + 5*26, with all zeros
        except 7 elements, which are 1
    """

    def __init__(self):
        self.numbers = [x for x in '0123456789']
        self.letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.encoding_numbers = {x[1]: x[0] for x in enumerate(self.numbers)}
        self.decoding_numbers = {x[0]: x[1] for x in enumerate(self.numbers)}
        self.encoding_letters = {x[1]: x[0] for x in enumerate(self.letters)}
        self.decoding_letters = {x[0]: x[1] for x in enumerate(self.letters)}

    def vectorize(self, uk_reg_str: str) -> np.array:
        if len(uk_reg_str) != 7:
            raise ValueError('expected length 7 string in '+str(uk_reg_str))
        if not uk_reg_str[2:4].isnumeric():
            raise ValueError('expected numeric in positions 2,3 in ' + str(uk_reg_str))
        if not uk_reg_str[:2].isalpha() or not uk_reg_str[4:].isalpha():
            raise ValueError('expected first 2 and last 3 chars to be alpha in ' + str(uk_reg_str))
        n_let = len(self.letters)
        n_num = len(self.numbers)

        vec = np.zeros(n_let * 5 + n_num * 2)
        vec[self.encoding_letters[uk_reg_str[0]]] = 1.0
        vec[self.encoding_letters[uk_reg_str[1]] + n_let] = 1.0
        vec[self.encoding_letters[uk_reg_str[4]] + 2 * n_let] = 1.0
        vec[self.encoding_letters[uk_reg_str[5]] + 3 * n_let] = 1.0
        vec[self.encoding_letters[uk_reg_str[6]] + 4 * n_let] = 1.0
        vec[self.encoding_numbers[uk_reg_str[2]] + 5 * n_let] = 1.0
        vec[self.encoding_numbers[uk_reg_str[3]] + 5 * n_let + n_num] = 1.0
        return vec

    def recover(self, vec: np.array) -> str:
        n_let = len(self.letters)
        n_num = len(self.numbers)

        if len(vec) != 2*n_num + 5*n_let:
            raise ValueError('expected length 140, found '+str(len(vec)))

        s = [' '] * 7
        s[0] = self.decoding_letters[np.argmax(vec[:n_let])]
        s[1] = self.decoding_letters[np.argmax(vec[n_let:2 * n_let])]
        s[4] = self.decoding_letters[np.argmax(vec[2 * n_let:3 * n_let])]
        s[5] = self.decoding_letters[np.argmax(vec[3 * n_let:4 * n_let])]
        s[6] = self.decoding_letters[np.argmax(vec[4 * n_let:5 * n_let])]
        s[2] = self.decoding_numbers[np.argmax(vec[5 * n_let:5 * n_let + n_num])]
        s[3] = self.decoding_numbers[np.argmax(vec[5 * n_let + n_num:5 * n_let + 2 * n_num])]
        return ''.join(s)
