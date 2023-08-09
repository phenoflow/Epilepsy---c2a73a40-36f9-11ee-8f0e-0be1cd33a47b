# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100652.0","system":"med"},{"code":"100920.0","system":"med"},{"code":"102359.0","system":"med"},{"code":"11015.0","system":"med"},{"code":"12848.0","system":"med"},{"code":"13073.0","system":"med"},{"code":"13219.0","system":"med"},{"code":"13220.0","system":"med"},{"code":"13221.0","system":"med"},{"code":"18899.0","system":"med"},{"code":"19549.0","system":"med"},{"code":"19550.0","system":"med"},{"code":"19551.0","system":"med"},{"code":"19552.0","system":"med"},{"code":"20566.0","system":"med"},{"code":"22991.0","system":"med"},{"code":"26512.0","system":"med"},{"code":"26618.0","system":"med"},{"code":"26619.0","system":"med"},{"code":"26620.0","system":"med"},{"code":"31877.0","system":"med"},{"code":"34473.0","system":"med"},{"code":"36696.0","system":"med"},{"code":"3783.0","system":"med"},{"code":"38919.0","system":"med"},{"code":"39160.0","system":"med"},{"code":"40863.0","system":"med"},{"code":"45757.0","system":"med"},{"code":"46603.0","system":"med"},{"code":"48462.0","system":"med"},{"code":"50012.0","system":"med"},{"code":"50702.0","system":"med"},{"code":"52632.0","system":"med"},{"code":"55706.0","system":"med"},{"code":"6709.0","system":"med"},{"code":"6983.0","system":"med"},{"code":"72384.0","system":"med"},{"code":"8385.0","system":"med"},{"code":"9326.0","system":"med"},{"code":"98442.0","system":"med"},{"code":"98536.0","system":"med"},{"code":"98977.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('epilepsy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["epilepsy-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["epilepsy-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["epilepsy-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
