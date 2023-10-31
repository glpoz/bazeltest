py_library(
    name = "calculation_library",
    srcs = ["calculation_module.py"]
)

py_binary(
    name = "consumer_script",
    srcs = ["consumer_script.py"],
    deps = [":calculation_library"]
)

py_test(
    name = "unittest",
    srcs = ["unittest.py"],
    deps = [":calculation_library"]
)