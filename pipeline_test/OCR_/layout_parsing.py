from paddlex import create_pipeline
import os

def test(device='cpu'):
    pipeline = create_pipeline(pipeline="layout_parsing", device=device)

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/demo_paper.png")
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_img("./output/") ## 保存img格式结果
        res.save_to_xlsx("./output/") ## 保存表格格式结果
        res.save_to_html("./output/") ## 保存html结果


if __name__ == "__main__":
    test()