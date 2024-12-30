# >>> ChatOCR >>>
from pipeline_test.ChatOCR.PP_ChatOCRv3_doc import test as test_PP_ChatOCRv3_doc
# >>> CV >>>
from pipeline_test.CV.anomaly_detection import test as test_anomaly_detection
from pipeline_test.CV.face_recognition import test as test_face_recognition
from pipeline_test.CV.image_classification import test as test_image_classification
from pipeline_test.CV.instance_segmentation import test as test_instance_segmentation
from pipeline_test.CV.multi_label_image_classification import test as test_multi_label_image_classification
from pipeline_test.CV.object_detection import test as test_object_detection
from pipeline_test.CV.pedestrian_attribute_recognition import test as test_pedestrain_attribute_recognition
from pipeline_test.CV.PP_ShiTuV2 import test as test_PP_ShiTuV2
from pipeline_test.CV.semantic_segmentation import test as test_semantic_segmentation
from pipeline_test.CV.small_object_detection import test as test_small_object_detection
from pipeline_test.CV.vehicle_attribute_recognition import test as test_vehicle_attribute_recognition
# >>> OCR_ >>>
from pipeline_test.OCR_.formula_recognition import test as test_formula_recognition
from pipeline_test.OCR_.layout_parsing import test as test_layout_parsing
from pipeline_test.OCR_.OCR import test as test_OCR
from pipeline_test.OCR_.seal_recognition import test as test_seal_recognition
from pipeline_test.OCR_.table_recognition import test as test_table_recognition
## >>> TS >>>
from pipeline_test.TS.ts_ad import test as test_ts_ad
from pipeline_test.TS.ts_cls import test as test_ts_cls
from pipeline_test.TS.ts_fc import test as test_ts_fc

def settings_log(settings:dict):
    print(f"* FILE: {__file__}")
    print(f"* AUTHOR: yutian929")
    print(f"* NOTES: 2024-12-19 v1")
    print("* settings:")
    for key, val in settings.items():
        print(f"# {key}:\t{val}")

if __name__ == '__main__':
    ## gloabl settings
    settings = {"device":'gpu'}
    
    ## >>> ChatOCR >>>
    # test_PP_ChatOCRv3_doc(settings)

    ## >>> CV >>>
    settings_log(settings)
    test_anomaly_detection(settings)
    settings_log(settings)
    test_face_recognition(settings)
    settings_log(settings)
    test_image_classification(settings)
    settings_log(settings)
    test_instance_segmentation(settings)
    settings_log(settings)
    test_multi_label_image_classification(settings)
    settings_log(settings)
    test_object_detection(settings)
    settings_log(settings)
    test_pedestrain_attribute_recognition(settings)
    settings_log(settings)
    test_PP_ShiTuV2(settings)
    settings_log(settings)
    test_semantic_segmentation(settings)
    settings_log(settings)
    test_small_object_detection(settings)
    settings_log(settings)
    test_vehicle_attribute_recognition(settings)

    # ## >>> OCR_ >>>
    # test_formula_recognition(settings)
    # test_layout_parsing(settings)
    # test_OCR(settings)
    # test_seal_recognition(settings)
    # test_table_recognition(settings)
    
    # ## >>> TS >>>
    # test_ts_ad(settings)
    # test_ts_cls(settings)
    # test_ts_fc(settings)