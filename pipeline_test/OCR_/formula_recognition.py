from paddlex import create_pipeline
import os

pipeline = create_pipeline(pipeline="formula_recognition")

output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_formula_recognition.png")
for res in output:
    res.print()
