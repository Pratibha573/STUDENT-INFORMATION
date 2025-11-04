import sys
if len(sys.argv) == 3:
  script name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("User provided input values:")
else:
  script name = sys.argv[0]
  name = "Pratibha"
  rollno = "055"
  print("no input given -using default values:")
 print(script Name:",script_name)
 print(student Name:",name)
 print("Roll Number:",rollno)
