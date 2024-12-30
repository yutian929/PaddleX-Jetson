from paddlex import create_pipeline
import os
import gc

def test(settings=None):
    pipeline = create_pipeline(pipeline="formula_recognition", device=settings['device'])

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_formula_recognition.png")
    for res in output:
        res.print()


    del pipeline
    gc.collect()

if __name__ == "__main__":
    test()