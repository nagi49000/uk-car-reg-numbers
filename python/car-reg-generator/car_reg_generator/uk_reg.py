from random import choice


class DvlaMemoryTag:
    """ definitions derived from https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/359317/INF104_160914.pdf """

    def __init__(self):
        """  object has member region, which is a dict<str, str>, key being uk region, value list of 2-elt memory tags """
        self.regions = self.get_expanded_regions(self.get_regions())

    def get_regions(self) -> dict[str, str]:
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

    def get_expanded_regions(self, regions: dict[str, str]) -> dict[str, str]:
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
        self.numbers = [chr(x) for x in range(ord('0'), ord('0')+10)]
        self.letters = [chr(x) for x in range(ord('A'), ord('A')+26)]

    def get_reg(self):
        memory_tag = choice(self.memory_tags)
        age_identifier = choice(self.numbers) + choice(self.numbers)
        rand_letters = choice(self.letters) + choice(self.letters) + choice(self.letters)
        return memory_tag + age_identifier + rand_letters
