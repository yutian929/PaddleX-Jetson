from paddlex import create_pipeline
import os

def test(device='cpu'):
    pipeline = create_pipeline(pipeline="face_recognition")

    index_data = pipeline.build_index(gallery_imgs=os.path.dirname(os.path.realpath(__file__)) + "/resources/face_demo_gallery", gallery_label=os.path.dirname(os.path.realpath(__file__)) + "/resources/face_demo_gallery/gallery.txt")
    os.makedirs("./output/face_demo_gallery", exist_ok=True)
    index_data.save("./output/face_demo_gallery/face_index")
    breakpoint()
    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/face_demo_gallery/test_images/friends1.jpg", index=index_data, device=device)
    for res in output:
        res.print()
        res.save_to_img("./output/")

if __name__ == "__main__":
    test()