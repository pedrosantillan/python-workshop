import pathlib
import re
unittest_path = pathlib.Path("/Python/lib/unittest/").resolve()

def analyze(path: pathlib.Path) -> dict:
  analysis = {}
  for node in path.iterdir():
    if node.is_file():
      analysis[node.name] = analyze_file(node)
  return analysis


def analyze_file(path: pathlib.Path):
  with open(path, mode='r') as file_obj:
      line_count = 0
      import_count=0
      for line in file_obj:
          if line != "\n":
              line_count += 1
          if line.startswith("import"):
              import_count += 1
          if re.search(r'\b{value}'.format(value="from"),line) and re.search(r'\b{value}'.format(value="import"),line):
              import_count += 1
  information=("File: ",path.absolute(),"Lines of Code: ", line_count, "Dependencies: ", import_count)
  return information

information = {}
information=analyze(unittest_path)
for i in information.items():
     print(i)
