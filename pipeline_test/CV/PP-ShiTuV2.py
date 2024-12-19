from paddlex import create_pipeline
import os

pipeline = create_pipeline(pipeline="PP-ShiTuV2")

index_data = pipeline.build_index(gallery_imgs=os.path.dirname(os.path.realpath(__file__)) + "/resources/drink_dataset_v2.0/", gallery_label=os.path.dirname(os.path.realpath(__file__)) + "/resources/drink_dataset_v2.0/gallery.txt")
os.mkdir("./output/drink_dataset_v2.0", exist_ok=True)
index_data.save("./output/drink_dataset_v2.0/drink_index")

output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources//drink_dataset_v2.0/test_images/", index=index_data)
for res in output:
    res.print()
    res.save_to_img("./output/")