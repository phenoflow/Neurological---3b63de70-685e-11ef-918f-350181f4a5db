# phekb, 2024.

import sys, csv, re

codes = [{"code":"323.81","system":"ICD9 Diagnosis"},{"code":"323.82","system":"ICD9 Diagnosis"},{"code":"323.9","system":"ICD9 Diagnosis"},{"code":"730.07","system":"ICD9 Diagnosis"},{"code":"730.18","system":"ICD9 Diagnosis"},{"code":"730.2","system":"ICD9 Diagnosis"},{"code":"730.25","system":"ICD9 Diagnosis"},{"code":"730.7","system":"ICD9 Diagnosis"},{"code":"G04.81","system":"ICD9 Diagnosis"},{"code":"G04.89","system":"ICD9 Diagnosis"},{"code":"G04.90","system":"ICD9 Diagnosis"},{"code":"G04.91","system":"ICD9 Diagnosis"},{"code":"M86.072","system":"ICD9 Diagnosis"},{"code":"M86.179","system":"ICD9 Diagnosis"},{"code":"M86.279","system":"ICD9 Diagnosis"},{"code":"M86.8X8","system":"ICD9 Diagnosis"},{"code":"M86.9","system":"ICD9 Diagnosis"},{"code":"M89.60","system":"ICD9 Diagnosis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neurological-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neurological-myelitis---undefined-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neurological-myelitis---undefined-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neurological-myelitis---undefined-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
