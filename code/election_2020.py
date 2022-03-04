import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):
    with open (IN_PATH, "r") as in_file:
        dict_reader = csv.DictReader(in_file)
        counts = {}

        for row in dict_reader:
            year = row["year"]
            candidate = row["candidate"]
            state_po = row["state_po"]
            key = (year, state_po, candidate)
            if row["candidatevotes"] != 'NA':
                num_v = int(row["candidatevotes"])
            else:
                num_v = 0
            if year == "2020":
                if key in counts:
                    counts[key] += num_v
                if key not in counts:
                    counts[key] = num_v
    return counts



def get_rows(counts):
    rows = []
    for new_key, new_vote in counts.items():
        rows.append([new_key, new_vote])
    return rows


def sort_rows(rows):

    rows_lex_ordered = []
    newlist_vote = sorted(rows, key = lambda x: x[1], reverse = True)
    rows_ordered = sorted(newlist_vote, key = lambda x: x[0][1], reverse= False)
    rows_lex_ordered = [[r[0][0], r[0][1], r[0][2],r[1]] for r in rows_ordered]
    return rows_lex_ordered
   

def write_rows(rows_lex_ordered):
    with open(OUTPUT_PATH, "w+", newline= "")as out_file:
        header = ["year", "state_code", "candidate", "votes"]
        dict_writer = csv.writer(out_file)
        dict_writer.writerow(header)
        dict_writer.writerows(rows_lex_ordered)

if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    counts = count_votes(IN_PATH)
    rows = get_rows(counts)
    sorted_rows = sort_rows(rows)
    write_rows(sorted_rows)
