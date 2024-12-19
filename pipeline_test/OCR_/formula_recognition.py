from paddlex import create_pipeline
import os

def test(device='gpu'):
    pipeline = create_pipeline(pipeline="formula_recognition")

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_formula_recognition.png", device=device)
    for res in output:
        res.print()


if __name__ == "__main__":
    test()