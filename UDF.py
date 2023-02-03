import sys
for line in sys.stdin:
    line =line.strip("\n\r")
    id, skill=line.split("\t")
    int_val=int(id)
    skill=skill.upper()
    result = '\t'.join([str(int_val*10),skill])
    print(result)

    #Select query 
    
    select transform(id, skill) using 'python3 transform_udf.py' as (new_id  int, new_skill string) from tbl_skill;
    
    # select query for single column
    
     select transform(id) using 'python3 multipy_udf.py' as new_id from tbl_skill;
    
import sys
for line in sys.stdin:
    line =line.strip("\n\r")
    int_val=int(line)
    result = int_val*10
    print(str(result))
