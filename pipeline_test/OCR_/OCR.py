from paddlex import create_pipeline
import os
import gc

def test(settings=None):
    pipeline = create_pipeline(pipeline="OCR", device=settings['device'])

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_ocr_002.png")
    for res in output:
        res.print()
        res.save_to_img("./output/")


    del pipeline
    gc.collect()

if __name__ == "__main__":
    test()