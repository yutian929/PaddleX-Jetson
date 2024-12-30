from paddlex import create_pipeline
import os

def test(device='cpu'):
    pipeline = create_pipeline(pipeline="OCR", device=device)

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_ocr_002.png")
    for res in output:
        res.print()
        res.save_to_img("./output/")


if __name__ == "__main__":
    test()