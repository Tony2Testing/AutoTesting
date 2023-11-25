import unittest
from BSTestRunner import BSTestRunner
import HTMLTestRunner
import os

def main():
    # 测试用例的目录
    case_path = "./test_cases"

    # 测试报告的目录
    report_path = "./test_reports"
    if not os.path.exists(report_path):
        os.makedirs(report_path)

    # 测试报告文件名固定为 report.html
    report_file = os.path.join(report_path, "report.html")

    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")

    # 运行测试用例并生成报告
    with open(report_file, "wb") as report:
        runner =HTMLTestRunner.HTMLTestRunner(
            stream=report,
            title="测试报告",
            description="测试报告明细"
        )
        runner.run(discover)

if __name__ == "__main__":
    main()