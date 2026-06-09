import numpy as np


social_mice = ( 'social-0914-1', 'social-0914-4', 'social-0921-2', 'social-0043-1', 'social-0051-1', 'social-0051-3','social-0057-1', 'social-0058-3','social-0059-1', 'social-2156-5', 'social-4062-2', 'social-4062-1', 'social-8564-2') #'social_0106_1',


exclude_list = {
}

social_VR_sessions = {
    # 'social_0106_1': (
    #     {'date': '14_03_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 1, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 2, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 3, 'scan':1, 'exp_day':1}
    # ),
    'social-0914-1': (
        # {'date': '03_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 1},
                # {'date': '03_10_2024', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 3, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 5, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 7, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 9, 'exp_day': 1},
                # {'date': '04_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 3, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 8, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 10, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 12, 'exp_day': 2},
                # {'date': '05_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 3},
                {'date': '05_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '05_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 3},
                # {'date': '06_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 11, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_restrict_nov_diffgender', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 3, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_unrestrict_nov_diffgender', 'session': 1, 'scan': 7, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 9, 'exp_day': 4},
                
                ),
        'social-0914-4': (
            # {'date': '03_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 1},
                # {'date': '03_10_2024', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 3, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 5, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 7, 'exp_day': 1},
                {'date': '03_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 9, 'exp_day': 1},
                # {'date': '04_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 3, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 7, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 9, 'exp_day': 2},
                {'date': '04_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 11, 'exp_day': 2},
                # {'date': '05_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 3},
                {'date': '05_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '05_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 3},
                # {'date': '06_10_2024', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 9, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_restrict_nov_diffgender', 'session': 1, 'scan': 3, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 1, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_unrestrict_nov_diffgender', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '06_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 7, 'exp_day': 4},
                
                ),
    'social-0921-2': (
        # {'date': '03_10_2024', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 6, 'exp_day': 1},
                    {'date': '03_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 8, 'exp_day': 1},
                    {'date': '03_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 10, 'exp_day': 1},
                    {'date': '03_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 12, 'exp_day': 1},
                    {'date': '04_10_2024', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 1, 'exp_day': 2},
                    {'date': '04_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3 , 'exp_day': 2},
                    {'date': '04_10_2024', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 5, 'exp_day': 2},
                    {'date': '04_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 7, 'exp_day': 2},
                    {'date': '04_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 9, 'exp_day': 2},
                    {'date': '05_10_2024', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 2, 'exp_day': 3},
                    {'date': '05_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 4, 'exp_day': 3},
                    {'date': '06_10_2024', 'scene': 'social_restrict_nov_diffgender', 'session': 1, 'scan': 3, 'exp_day': 4},
                    {'date': '06_10_2024', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 1, 'exp_day': 4},
                    {'date': '06_10_2024', 'scene': 'social_unrestrict_nov_diffgender', 'session': 1, 'scan': 5, 'exp_day': 4},
                    {'date': '06_10_2024', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 7, 'exp_day': 4},
                    
                    ),

    'social-0043-1': (
        # {'date': '10_05_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 2, 'exp_day': 1},
                {'date': '10_05_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 4, 'exp_day': 1},
                {'date': '10_05_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 6, 'exp_day': 1},
                {'date': '11_05_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 2, 'exp_day': 2},
                {'date': '11_05_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 4, 'exp_day': 2},
                {'date': '11_05_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 6, 'exp_day': 2},
                {'date': '11_05_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 8, 'exp_day': 2},
                {'date': '12_05_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 1, 'exp_day': 3},
                {'date': '12_05_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '13_05_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 16, 'exp_day': 4},
                {'date': '13_05_2025', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 14, 'exp_day': 4},
                {'date': '14_05_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 2, 'exp_day': 5},
                {'date': '14_05_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 0, 'exp_day': 5},
                {'date': '14_05_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 4, 'exp_day': 5},
                {'date': '15_05_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 6},
                {'date': '15_05_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 6},
                
                ),

    'social-0051-1': (
        # {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 13, 'exp_day': 1},
                # {'date': '29_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 16, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 18, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 20, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 23, 'exp_day': 1},

                # {'date': '30_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 44, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 46, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 49, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 52, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 55, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 58, 'exp_day': 2},

                # {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 28,'exp_day': 3},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 30, 'exp_day': 3},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 32, 'exp_day': 3},

                # {'date': '02_07_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 3, 'scan': 2, 'exp_day': 4},
                # {'date': '02_07_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 7, 'exp_day': 4},

                # {'date': '03_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 10, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 14, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 16, 'exp_day': 5},

                # {'date': '04_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 3, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 3, 'scan': 10, 'exp_day': 6},
                ),

    'social-0051-3': (
        # {'date': '27_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 6, 'exp_day': 1},
                # {'date': '27_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 8, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 11, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 14, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_wheel_restrict', 'session': 2, 'scan': 19, 'exp_day': 1},

                # {'date': '28_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 44, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 47, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 49, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 52, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 54, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 56, 'exp_day': 2},

                # {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 4, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 3},

                # {'date': '30_06_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 13, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 16, 'exp_day': 4},
                # {'date': '30_06_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 19, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 21, 'exp_day': 4},

                # {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 8, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 11, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 14, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 16, 'exp_day': 5},

                # {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 13, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 16, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 19, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 3, 'scan': 23, 'exp_day': 6},
                
                ),
    'social-0057-1': (
        # {'date': '27_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 23, 'exp_day': 1},
                # {'date': '27_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 25, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 27, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 29, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 31, 'exp_day': 1},

                # {'date': '28_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 4, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 6, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 8, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 10, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 12, 'exp_day': 2},

                # {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 8, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 10, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 3},

                # {'date': '30_06_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 23, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 25, 'exp_day': 4},
                # {'date': '30_06_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 27, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 34, 'exp_day': 4},

                # {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 19, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 21, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 23, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 2, 'scan': 25, 'exp_day': 5},

                # {'date': '02_07_2025', 'scene': 'Env1_to_Env2_with_nov', 'session': 1, 'scan': 3, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 9, 'exp_day': 6},
                ),
    'social-0058-3': (
        # {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 1},
                # {'date': '29_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 3, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 5, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 7, 'exp_day': 1},
                {'date': '29_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 9, 'exp_day': 1},

                # {'date': '30_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 3, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 7, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 9, 'exp_day': 2},
                {'date': '30_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 11, 'exp_day': 2},

                # {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 1,'exp_day': 3},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 3},

                # {'date': '02_07_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 1, 'exp_day': 4},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 3, 'exp_day': 4},
                # {'date': '02_07_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 7, 'exp_day': 4},

                # {'date': '03_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 4, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 6, 'exp_day': 5},
                {'date': '03_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 8, 'exp_day': 5},

                # {'date': '04_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 18, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 20, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 22, 'exp_day': 6},
                {'date': '04_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 24, 'exp_day': 6},
                ),

    'social-0059-1': (
          # {'date': '27_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 33, 'exp_day': 1},
                # {'date': '27_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 35, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 37, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 39, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 41, 'exp_day': 1},

                # {'date': '28_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 14, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 16, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 18, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 21, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 23, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 25, 'exp_day': 2},

                # {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 25, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 28, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 30, 'exp_day': 3},

                # {'date': '30_06_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 36, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 38, 'exp_day': 4},
                # {'date': '30_06_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 40, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 42, 'exp_day': 4},

                # {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 34, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 36, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 38, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 40, 'exp_day': 5},

                # {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 9, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 11, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 13, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 15, 'exp_day': 6},
                ),

    'social-2156-5': ({'date': '21_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 21, 'exp_day': 1},
                {'date': '21_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 23, 'exp_day': 1},
                {'date': '21_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 25, 'exp_day': 1},

                {'date': '22_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 2},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 4, 'exp_day': 2},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 2},

                {'date': '23_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 13,'exp_day': 3},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 15, 'exp_day': 3},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 18, 'exp_day': 3},

                {'date': '24_03_2026', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 3, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 7, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 12, 'exp_day': 4},

                {'date': '25_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 9, 'exp_day': 5},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 11, 'exp_day': 5},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 13, 'exp_day': 5},

                {'date': '26_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 4, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 8, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 10, 'exp_day': 6},

                {'date': '27_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 5, 'exp_day': 7},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 7},
                {'date': '27_03_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 9, 'exp_day': 7},

                {'date': '28_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 31, 'exp_day': 8},
                {'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 34, 'exp_day': 8},
                 ),  
    
    'social-4062-2': (
                {'date': '22_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 9, 'exp_day': 1},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 11, 'exp_day': 1},

                {'date': '23_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 21, 'exp_day': 2},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 23, 'exp_day': 2},

                {'date': '24_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 14, 'exp_day': 3},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 16, 'exp_day': 3},

                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 15, 'exp_day': 4},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 17, 'exp_day': 4},

                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 5},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 15, 'exp_day': 5},

                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 15, 'exp_day': 6},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 17, 'exp_day': 6},
                {'date': '27_03_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 19, 'exp_day': 6},

                ),

    'social-4062-1': (
                #{'date': '27_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 24, 'exp_day': 1}, #had this data but too bad so don;t want to include
                {'date': '27_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 26, 'exp_day': 1},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 28, 'exp_day': 1},

                #{'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 43, 'exp_day': 2}, #Same
                {'date': '28_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 45, 'exp_day': 2},
                {'date': '28_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 47, 'exp_day': 2},

                #{'date': '29_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 58, 'exp_day': 3}, #Same
                {'date': '29_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '29_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 3},

                {'date': '30_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 8, 'exp_day': 4},
                {'date': '30_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 10, 'exp_day': 4},

                {'date': '31_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 5},
                {'date': '31_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 14, 'exp_day': 5},

                {'date': '01_04_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 2, 'exp_day': 6},
                {'date': '01_04_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 4, 'exp_day': 6},
                {'date': '01_04_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 6, 'exp_day': 7},

                ),
    'social-8564-2': (
                #{'date': '03_05_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 3, 'exp_day': 1}, #had this data but too bad so don;t want to include
                {'date': '05_05_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 1, 'exp_day': 1},
                {'date': '05_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 1},

                #{'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 43, 'exp_day': 2}, #Same
                {'date': '06_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 2},
                {'date': '06_05_2026', 'scene': 'social_unrestrict_nov', 'session': 6, 'scan':21, 'exp_day': 2},

                #{'date': '29_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 58, 'exp_day': 3}, #Same
                {'date': '07_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 1, 'exp_day': 3},
                {'date': '07_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 3, 'exp_day': 3},

                {'date': '08_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 7, 'exp_day': 4},
                {'date': '08_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 4},

                {'date': '10_05_2026', 'scene': 'social_unrestrict_nov', 'session': 3, 'scan': 2, 'exp_day': 5},
                {'date': '10_05_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 4, 'exp_day': 5},

                {'date': '11_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 6},
                {'date': '11_05_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 5, 'scan':13, 'exp_day': 6},
                {'date': '11_05_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 15, 'exp_day': 6},

                ),

}


social_2P_sessions = {
    # 'social_0106_1': (
    #     {'date': '14_03_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 1, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 2, 'scan':1, 'exp_day':1},
    #     {'date': '14_03_2024' , 'scene': 'soical_dark_background', 'session': 3, 'scan':1, 'exp_day':1}
    # ),
    'social-0914-1': (
        # {'date': '02_10_2024' , 'scene': 'soical_dark_background', 'session': 1, 'scan':1, 'exp_day':1},
        # {'date': '02_10_2024' , 'scene': 'soical_dark_background', 'session': 2, 'scan':1, 'exp_day':1},
        # {'date': '02_10_2024' , 'scene': 'soical_dark_background_3', 'session': 2, 'scan':0, 'exp_day':1},
        {'date': '03_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_emptytunnel', 'session': 1, 'scan':3, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':5, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_unrestrict_fam','session': 1,  'scan':7, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':9, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':3, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_restrict_nov', 'session': 1, 'scan':8, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':5, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':10, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':12, 'exp_day':3},
        {'date': '05_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':4},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':3, 'exp_day':4},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':5, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':11, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan':5, 'exp_day':5},
        # {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov',  'scan':, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':3, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan':7, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':9, 'exp_day':5},
    ),
    'social-0914-4': (
        {'date': '03_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_emptytunnel', 'session': 1, 'scan':3, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':5, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_unrestrict_fam','session': 1,  'scan':7, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':9, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':3, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_restrict_nov', 'session': 1, 'scan':7, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':5, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':9, 'exp_day':3},
        {'date': '04_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':11, 'exp_day':3},
        {'date': '05_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':1, 'exp_day':4},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':3, 'exp_day':4},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':6, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan':9, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan':3, 'exp_day':5},
        # {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov',  'scan':, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':1, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan':5, 'exp_day':5},
        {'date': '06_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':7, 'exp_day':5},
    ),
    'social-0921-2': (
        # {'date': '03_10_2024' , 'scene': 'Env1_to_Env2_fixreward',  'scan':, 'exp_day':2},
        {'date': '03_10_2024' , 'scene': 'social_emptytunnel','session': 1,  'scan':6, 'exp_day':1},
        {'date': '03_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':8, 'exp_day':1},
        {'date': '03_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':10, 'exp_day':1},
        {'date': '03_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':12, 'exp_day':1},
        # {'date': '04_10_2024' , 'scene': 'Env1_to_Env2_fixreward',  'scan':, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'social_restrict_fam', 'session': 1, 'scan':1, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'social_restrict_nov', 'session': 1, 'scan':5, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':3, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':7, 'exp_day':2},
        {'date': '04_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':9, 'exp_day':2},
        # {'date': '05_10_2024' , 'scene': 'Env1_to_Env2_fixreward',  'scan':, 'exp_day':3},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_fam', 'session': 1, 'scan':2, 'exp_day':3},
        # {'date': '05_10_2024' , 'scene': 'social_unrestrict_fam',  'scan':, 'exp_day':3},
        {'date': '05_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':4, 'exp_day':3},
        # {'date': '06_10_2024' , 'scene': 'Env1_to_Env2_fixreward',  'scan':, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan':3, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov', 'session': 1, 'scan':1, 'exp_day':4},
        # {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov',  'scan':, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan':5, 'exp_day':4},
        {'date': '06_10_2024' , 'scene': 'social_wheel_restrict', 'session': 1, 'scan':7, 'exp_day':4},
    ),
    'social-0057-1': ({'date': '27_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 23, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 25, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 27, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 29, 'exp_day': 1},
                {'date': '27_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 31, 'exp_day': 1},

                {'date': '28_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_fam', 'session': 1, 'scan': 4, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 6, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_restrict_nov', 'session': 1, 'scan': 8, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 10, 'exp_day': 2},
                {'date': '28_06_2025', 'scene': 'social_wheel_restrict', 'session': 1, 'scan': 12, 'exp_day': 2},

                {'date': '29_06_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 8, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 10, 'exp_day': 3},
                {'date': '29_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 3},

                {'date': '30_06_2025', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 23, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 25, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 27, 'exp_day': 4},
                {'date': '30_06_2025', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 34, 'exp_day': 4},

                {'date': '01_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 19, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 21, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_restrict_nov_diffsex', 'session': 1, 'scan': 23, 'exp_day': 5},
                {'date': '01_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 2, 'scan': 25, 'exp_day': 5},

                {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 3, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 6},
                {'date': '02_07_2025', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 9, 'exp_day': 6},
                ),

    'social-2156-5': ({'date': '21_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 21, 'exp_day': 1},
                {'date': '21_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 23, 'exp_day': 1},
                {'date': '21_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 25, 'exp_day': 1},

                {'date': '22_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 2, 'exp_day': 2},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 4, 'exp_day': 2},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 2},

                {'date': '23_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 13,'exp_day': 3},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 15, 'exp_day': 3},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 18, 'exp_day': 3},

                {'date': '24_03_2026', 'scene': 'Env1_fixreward', 'session': 1, 'scan': 3, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'Env2_fixreward', 'session': 1, 'scan': 7, 'exp_day': 4},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 12, 'exp_day': 4},

                {'date': '25_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 9, 'exp_day': 5},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 11, 'exp_day': 5},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 13, 'exp_day': 5},

                {'date': '26_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 4, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 8, 'exp_day': 6},
                {'date': '26_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 2, 'scan': 10, 'exp_day': 6},

                {'date': '27_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 5, 'exp_day': 7},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 7, 'exp_day': 7},
                {'date': '27_03_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 9, 'exp_day': 7},

                {'date': '28_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 31, 'exp_day': 8},
                {'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 34, 'exp_day': 8},
                 ),  
    
    'social-4062-2': (
                {'date': '22_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 9, 'exp_day': 1},
                {'date': '22_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 11, 'exp_day': 1},

                {'date': '23_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 21, 'exp_day': 2},
                {'date': '23_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 23, 'exp_day': 2},

                {'date': '24_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 14, 'exp_day': 3},
                {'date': '24_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 16, 'exp_day': 3},

                {'date': '25_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 15, 'exp_day': 4},
                {'date': '25_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 17, 'exp_day': 4},

                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 5},
                {'date': '26_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 15, 'exp_day': 5},

                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov', 'session': 2, 'scan': 15, 'exp_day': 6},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 17, 'exp_day': 6},
                {'date': '27_03_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 19, 'exp_day': 6},

                ),

    'social-4062-1': (
                #{'date': '27_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 24, 'exp_day': 1}, #had this data but too bad so don;t want to include
                {'date': '27_03_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 26, 'exp_day': 1},
                {'date': '27_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 28, 'exp_day': 1},

                #{'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 43, 'exp_day': 2}, #Same
                {'date': '28_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 45, 'exp_day': 2},
                {'date': '28_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 47, 'exp_day': 2},

                #{'date': '29_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 58, 'exp_day': 3}, #Same
                {'date': '29_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 3},
                {'date': '29_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 5, 'exp_day': 3},

                {'date': '30_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 8, 'exp_day': 4},
                {'date': '30_03_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 10, 'exp_day': 4},

                {'date': '31_03_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 12, 'exp_day': 5},
                {'date': '31_03_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 14, 'exp_day': 5},

                {'date': '01_04_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 2, 'exp_day': 6},
                {'date': '01_04_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 4, 'exp_day': 6},
                {'date': '01_04_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 6, 'exp_day': 7},

                ),
    'social-8564-2': (
                #{'date': '03_05_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 3, 'exp_day': 1}, #had this data but too bad so don;t want to include
                {'date': '05_05_2026', 'scene': 'social_emptytunnel', 'session': 1, 'scan': 1, 'exp_day': 1},
                {'date': '05_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 3, 'exp_day': 1},

                #{'date': '28_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 43, 'exp_day': 2}, #Same
                {'date': '06_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 2},
                {'date': '06_05_2026', 'scene': 'social_unrestrict_nov', 'session': 6, 'scan':21, 'exp_day': 2},

                #{'date': '29_03_2026', 'scene': 'Env1_to_Env2_fixreward', 'session': 1, 'scan': 58, 'exp_day': 3}, #Same
                {'date': '07_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 1, 'exp_day': 3},
                {'date': '07_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 3, 'exp_day': 3},

                {'date': '08_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 7, 'exp_day': 4},
                {'date': '08_05_2026', 'scene': 'social_unrestrict_fam', 'session': 1, 'scan': 5, 'exp_day': 4},

                {'date': '10_05_2026', 'scene': 'social_unrestrict_nov', 'session': 3, 'scan': 2, 'exp_day': 5},
                {'date': '10_05_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 1, 'scan': 4, 'exp_day': 5},

                {'date': '11_05_2026', 'scene': 'social_unrestrict_nov', 'session': 1, 'scan': 6, 'exp_day': 6},
                {'date': '11_05_2026', 'scene': 'social_unrestrict_nov_diffsex', 'session': 5, 'scan':13, 'exp_day': 6},
                {'date': '11_05_2026', 'scene': 'social_novel_object', 'session': 1, 'scan': 15, 'exp_day': 6},

                ),
}

social_SLP_sessions = {
    'social_0106': (
        
    )
}
        

