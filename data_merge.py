import csv

'''
1. Read old data file, fetch all the intents -- (available intents)
2. create new csv file, read squad data file and push all the utterances with the intents in available intents in new csv file.
3. In step 2, create a list --  Considered intents
4. Take the uncommon part from considered and available intents (Uncommon intents)
5. read old data file and push all the utterances with the intents in Uncommon intents in new csv file.
'''

def get_available_intents():
    file_obj = open('/Users/saurabh.kumar1/Desktop/file.csv', 'rt')
    available_intents = set()
    with file_obj as f:
        data = csv.reader(f)
        c = 0
        for row in data:
            c += 1
            if c == 1:
                continue
            available_intents.add(row[1])
    return available_intents


def process_tag(tag):
    correct_strings = [(" ", ""), (".Flights", ".Flight"), (".Hotels", ".Hotel"), (".Timeline", ".RefundTimeline")]

    for tup in correct_strings:
        tag = tag.replace(tup[0], tup[1])
    return tag


def add_squad_data(available_intents, writer):

    file_obj = open('/Users/saurabh.kumar1/Desktop/Final-Sheet.csv', 'rt')
    considered_intents = set()
    all_intents = set()
    line_count = 0
    query_map = {}
    with file_obj as f:
        data = csv.reader(f)
        c = 0
        for row in data:
            c += 1
            if c == 1:
                continue
            utterance = row[1]
            if not utterance or query_map.get(utterance):
                continue
            else:
                query_map[utterance] = True

            hm = {}
            m = 0
            intent = None

            if not row[3] and not row[4]:

                ans = ans.split(',')
                if not isinstance(ans, str):
                    continue

                for tag in ans:
                    tag = process_tag(tag)
                    if not hm.get(tag):
                        hm[tag] = 1
                    else:
                        hm[tag] += 1
                        if hm[tag] > m:
                            m = hm[tag]
                            intent = tag


            for ans in [row[2], row[3], row[4]]:
                if not isinstance(ans, str):
                    continue
                ans = ans.split(',')

                for tag in ans:
                    tag = process_tag(tag)
                    if not hm.get(tag):
                        hm[tag] = 1
                    else:
                        hm[tag] += 1
                        if hm[tag] > m:
                            m = hm[tag]
                            intent = tag

            if intent and intent.lower() != 'noneoftheabove' and m >= 2:

                intent = f'GI.PostSales.{intent}'
                all_intents.add(intent)
                if intent in available_intents:
                    writer.writerow([line_count, intent, utterance])
                    considered_intents.add(intent)
                    line_count += 1
    for i in all_intents:
        print(i)
    return considered_intents, line_count


def push_old_data(uncommon_intents, writer, line_count):
    file_obj = open('/Users/saurabh.kumar1/Desktop/file.csv', 'rt')
    with file_obj as f:
        data = csv.reader(f)
        c = 0
        for row in data:
            c += 1
            if c == 1:
                continue
            intent = row[1]
            utterance = row[2]
            if intent in uncommon_intents:
                writer.writerow([line_count, intent, utterance])
                line_count += 1
    return line_count


def main():
    final_csv = open('/Users/saurabh.kumar1/Desktop/final_training_data.csv', mode='w')
    writer = csv.writer(final_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['id', 'label', 'text'])
    available_intents = get_available_intents()
    # print (available_intents, len(available_intents))
    considered_intents, line_count = add_squad_data(available_intents,writer)
    # print (considered_intents, len(considered_intents))
    uncommon_intents = available_intents - considered_intents
    line_count = push_old_data(uncommon_intents, writer, line_count)
    # print (line_count)
    final_csv.close()

if __name__ == '__main__':
    main()