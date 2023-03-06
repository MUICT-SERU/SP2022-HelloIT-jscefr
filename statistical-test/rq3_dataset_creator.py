import os, csv, json

columns = ['Competency Levels', 'Code Constructs', 'Files']
levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
rows = levels + ['Total']
modules = {'react': {'report name': 'react', 'test files location': '/__tests__/'}, 'svelte': {'report name': 'kit', 'test files location': '/test/'}, 'next_js': {'report name': 'next.js', 'test files location': '/test/'}}
C2_files = {'test': [], 'non-test': []}

all_code_constructs = [[0] * 7] * 2
all_files = [[0] * 7] * 2

for module in modules:

    for test in [True, False]:

        test_or_non_test = 0 if test else 1

        report = json.load(open(os.getcwd() + f'/report/DATA_JSON/{modules[module]["report name"]}.json'))[modules[module]['report name']]
        test_or_non_test_files = {f: report[f] for f in report if (modules[module]['test files location'] in f) == test}
        all_files[test_or_non_test][6] += len(test_or_non_test_files.keys())

        code_constructs = [0, 0, 0, 0, 0, 0, 0]
        files = [0, 0, 0, 0, 0, 0, len(test_or_non_test_files)]

        for f in test_or_non_test_files:

            for i in range(len(levels)):

                if levels[i] in test_or_non_test_files[f]['Levels']:

                    code_constructs[i] += test_or_non_test_files[f]['Levels'][levels[i]]
                    code_constructs[6] += test_or_non_test_files[f]['Levels'][levels[i]]
                    all_code_constructs[test_or_non_test][i] += test_or_non_test_files[f]['Levels'][levels[i]]
                    all_code_constructs[test_or_non_test][6] += test_or_non_test_files[f]['Levels'][levels[i]]
                    
                    files[i] += 1
                    all_files[test_or_non_test][i] += 1

                    if levels[i] == 'C2':
                        C2_files[('non-' if not test else '') + 'test'].append(f)

        with open(f'statistical-test/datasets/rq3/{module + ("_non" if not test else "")}_test.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            for i in range(len(rows)):
                writer.writerow([rows[i], code_constructs[i], files[i]])

for test in [True, False]:

    test_or_non_test = 0 if test else 1

    with open(f'statistical-test/datasets/rq3/all{"_non" if not test else ""}_test.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for i in range(len(rows)):
            writer.writerow([rows[i], all_code_constructs[test_or_non_test][i], all_files[test_or_non_test][i]])