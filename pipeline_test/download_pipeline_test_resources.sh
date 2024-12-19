# clear all resources downloaded before
rm -r ./*/resources/*

# >>> ChatOCR >>>
mkdir -p ChatOCR/resources/
cd ChatOCR/resources/
## PP-ChatOCRv3-doc
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/contract.pdf"
cd ../..
# <<< ChatOCR <<<

# >>> CV >>>
mkdir -p CV/resources/
cd CV/resources/
## anomaly_detection
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/uad_grid.png"
## face_recognition
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/face_demo_gallery.tar
tar -xf ./face_demo_gallery.tar
rm ./face_demo_gallery.tar
## image_classification
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg"
## instance_segmentation
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_instance_segmentation_004.png"
## multi_label_image_classification
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_image_classification_001.jpg"
## object_detection
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_object_detection_002.png"
## pedestrian_attribute_recognition
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/pedestrian_attribute_002.jpg"
## PP-ShiTuV2
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/data/drink_dataset_v2.0.tar"
tar -xf ./drink_dataset_v2.0.tar
rm ./drink_dataset_v2.0.tar
## semantic_segmentation
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/application/semantic_segmentation/makassaridn-road_demo.png"
## small_object_detection
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/small_object_detection.jpg"
## vehicle_attribute_recognition
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/vehicle_attribute_002.jpg"
cd ../..
# <<< CV <<<

# >>> OCR_ >>>
mkdir -p OCR_/resources/
cd OCR_/resources/
## formula_recognition
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/demo_image/general_formula_recognition.png"
## layout_parsing
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/demo_paper.png"
## OCR
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png"
## seal_recognition
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png"
## table_recognition
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/table_recognition.jpg"
cd ../..
# <<< OCR_ <<<

# >>> TS >>>
mkdir -p TS/resources/
cd TS/resources/
## ts_ad
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_ad.csv"
## ts_cls
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_cls.csv"
## ts_fc
wget "https://paddle-model-ecology.bj.bcebos.com/paddlex/ts/demo_ts/ts_fc.csv"
cd ../..
# <<< TS <<<


