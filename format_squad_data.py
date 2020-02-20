import csv


def process_tag(tag):
    correct_strings = [(" ", ""), (".Flights", ".Flight"), (".Hotels", ".Hotel"), (".Timeline", ".RefundTimeline")]

    for tup in correct_strings:
        tag = tag.replace(tup[0], tup[1])
    return tag

def format_squad_data(writer):

    file_obj = open('/Users/saurabh.kumar1/Desktop/Final-Sheet.csv', 'rt')

    with file_obj as f:
        data = csv.reader(f)
        c = 0
        line_count = 0
        for row in data:
            c += 1
            if c == 1:
                continue
            utterance = row[1]
            hm = {}
            m = 0
            intent = None

            if not row[3] and not row[4]:

                ans = row[2]
                if not isinstance(ans, str):
                    continue

                ans = ans.split(',')

                intent = ans[0]
                m = 2

            if not intent:
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

            if intent and m >= 2:
                if intent.lower() != 'noneoftheabove':
                    intent = f'GI.PostSales.{intent}'

                writer.writerow([line_count, intent, utterance])
                line_count += 1


final_csv = open('/Users/saurabh.kumar1/Desktop/formatted_squad_data.csv', mode='w')
writer = csv.writer(final_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['id', 'label', 'text'])

format_squad_data(writer)
final_csv.close()