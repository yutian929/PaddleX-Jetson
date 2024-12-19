from paddlex import create_pipeline
import os

pipeline = create_pipeline(
    pipeline="PP-ChatOCRv3-doc",
    llm_name="ernie-3.5",
    llm_params={"api_type": "qianfan", "ak": "123", "sk": "abc"} # 请填入您的ak与sk，否则无法调用大模型
    # llm_params={"api_type": "aistudio", "access_token": ""} # 请填入您的access_token，否则无法调用大模型
    )

visual_result, visual_info = pipeline.visual_predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/contract.pdf")

for res in visual_result:
    res.save_to_img("./output")
    res.save_to_html('./output')
    res.save_to_xlsx('./output')

vector = pipeline.build_vector(visual_info=visual_info)

chat_result = pipeline.chat(
    key_list=["乙方", "手机号"],
    visual_info=visual_info,
    vector=vector,
    )
chat_result.print()