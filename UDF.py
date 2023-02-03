import sys
for line in sys.stdin:
    line =line.strip("\n\r")
    id, skill=line.split("\t")
    int_val=int(id)
    skill=skill.upper()
    result = '\t'.join([str(int_val*10),skill])
    print(result)
