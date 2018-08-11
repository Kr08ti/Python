with open("name.txt",mode='r') as f:
    with open("name_backup.txt",mode='w') as f1:
        for line in f:
            f1.write(line)
