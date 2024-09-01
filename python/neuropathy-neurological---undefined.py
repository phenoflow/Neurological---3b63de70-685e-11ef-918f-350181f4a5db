# phekb, 2024.

import sys, csv, re

codes = [{"code":"53.13","system":"ICD9 Diagnosis"},{"code":"349.9","system":"ICD9 Diagnosis"},{"code":"354.2","system":"ICD9 Diagnosis"},{"code":"355.8","system":"ICD9 Diagnosis"},{"code":"356.4","system":"ICD9 Diagnosis"},{"code":"356.8","system":"ICD9 Diagnosis"},{"code":"356.9","system":"ICD9 Diagnosis"},{"code":"357.1","system":"ICD9 Diagnosis"},{"code":"357.6","system":"ICD9 Diagnosis"},{"code":"357.7","system":"ICD9 Diagnosis"},{"code":"357.9","system":"ICD9 Diagnosis"},{"code":"B02.23","system":"ICD9 Diagnosis"},{"code":"G56.90","system":"ICD9 Diagnosis"},{"code":"G57.91","system":"ICD9 Diagnosis"},{"code":"G58.0","system":"ICD9 Diagnosis"},{"code":"G60.3","system":"ICD9 Diagnosis"},{"code":"G60.8","system":"ICD9 Diagnosis"},{"code":"G60.9","system":"ICD9 Diagnosis"},{"code":"G62.0","system":"ICD9 Diagnosis"},{"code":"G62.2","system":"ICD9 Diagnosis"},{"code":"G62.9","system":"ICD9 Diagnosis"},{"code":"G63","system":"ICD9 Diagnosis"},{"code":"G90.09","system":"ICD9 Diagnosis"},{"code":"G96.9","system":"ICD9 Diagnosis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neurological-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neuropathy-neurological---undefined-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neuropathy-neurological---undefined-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neuropathy-neurological---undefined-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
