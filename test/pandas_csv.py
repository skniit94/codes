import pandas as pd
import traceback
#
# df = pd.read_csv('/Users/saurabh.kumar1/Desktop/test.csv', engine='python', sep=',')
# new_df = pd.DataFrame(columns=['label', 'text'])
# line_count = 0
# for i, row in df.iterrows():
#     utterance = row['query']
#     answer1 = row['Answer 1']
#     answer2 = row['Answer 2']
#     answer3 = row['Answer 3']
#     print (answer1.split(','), type(answer1))
#     print (answer2, type(answer2))
#     print (answer3)

class test(object):

    @staticmethod
    def test1():
        print ('test1 called')

    @staticmethod
    def test2():
        print ('test2 called')
        test.test1()


test().test2()



def format_squad_data(filepath):
    try:
        df = pd.read_csv(filepath, engine='python', sep=',')
        new_df = pd.DataFrame(columns=['label', 'text'])
        line_count = 0
        for i, row in df.iterrows():
            utterance = row['query']

            hm = {}
            m = 0
            intent = None
            for ans in [row['Answer 1'], row['Answer 2'], row['Answer 3']]:
                ans = [x.strip() for x in ans.split(',')]
                for i in ans:
                    if not hm.get(i):
                        hm[i] = 1
                    else:
                        hm[i] += 1
                        if hm[i] > m:
                            m = hm[i]
                            intent = i
                    print(i)
            if intent and m >= 2:
                if intent.lower() == 'noneoftheabove':
                    intent = 'nota'
                else:
                    intent = f'GI.PostSales.{intent}'
                new_df.loc[line_count] = [intent, utterance]
                line_count += 1

        return new_df

    except Exception as e:
        print ("Error while formating Squad Data")
        print (traceback.format_exc())


# print (format_squad_data('/Users/saurabh.kumar1/Desktop/test.csv'))