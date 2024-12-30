from paddlex import create_pipeline
import os
import gc

def test(settings=None):
    pipeline = create_pipeline(pipeline="ts_fc", device=settings['device'])

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/ts_fc.csv")
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_csv("./output/") ## 保存csv格式结果

    del pipeline
    gc.collect()

if __name__ == "__main__":
    test()